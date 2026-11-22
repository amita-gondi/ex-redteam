"""The desk pipeline for one task:
validate -> screen -> anchored_rescore -> strict_gate -> redteam -> probe_blackbox -> probe_whitebox -> aggregate -> index.

Idempotent: a COMPLETE stage whose inputs hash is unchanged is skipped. A COMPLETE stage whose inputs changed,
or a partial stage, is never silently re-run: use --resume (continue the same agent session) or --force (fresh;
the old attempt is kept under <stage>/.superseded/). canary and panel are gated and never launch rollouts.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

from . import LABEL, __version__
from .backends import LaunchRequest, get_backend
from .blind import (
    build_workdir,
    destroy_workdir,
    hide_paths,
    independence_check,
    isolation_mode,
    plan_inputs,
    sha256_file,
    sha256_text,
    workdir_root,
    wrap_command,
)
from .checks import peer_reports, url_check, wording_check
from .config import rel
from .gate import aggregate, strict_gate
from .provenance import file_lock, git_head, index_upsert, now_iso, read_yaml, today, write_yaml
from .records import parse_record
from .stages import DESK, GATED, ORDER, OUTCOME, interpret, primary_verdict
from .supervisor import Clock, supervise

DONE = "COMPLETE"
EXIT_OK, EXIT_STAGE, EXIT_USAGE, EXIT_REFUSED, EXIT_NO_ROLLOUTS = 0, 1, 2, 3, 4
LOCAL_STAGES = ("validate", "strict_gate", "aggregate", "index")


class PipelineError(Exception):
    def __init__(self, msg: str, code: int = EXIT_USAGE):
        super().__init__(msg)
        self.code = code


@dataclass
class Options:
    stages: list | None = None
    dry_run: bool = False
    resume: bool = False
    force: bool = False
    run_id: str | None = None
    new_run: bool = False
    backend: str | None = None
    model: str | None = None
    effort: str | None = None
    offline: bool = False
    continue_on_cut: bool = False
    clock: Clock = field(default_factory=Clock)


def is_on(v) -> bool:
    return v is True or str(v).strip().upper() in ("ON", "TRUE", "YES")


def check_gate(cfg: dict, stage: str) -> tuple[int, str]:
    """canary/panel: refuse (3) unless the gate is ON and a GO is recorded with who/when/source; even then, 4."""
    gate = (cfg.get("gates") or {}).get(stage)
    rec = (cfg.get("gate_go_records") or {}).get(stage) or {}
    missing = [k for k in ("who", "when", "source") if not str(rec.get(k) or "").strip()]
    if not is_on(gate):
        return EXIT_REFUSED, (f"REFUSED: stage '{stage}' is gated and gates.{stage} is OFF in config/runner.yaml. "
                              f"Rollout stages need Amita's GO: the gate must be ON and gate_go_records.{stage} must "
                              "record who/when/source. Don't flip a gate yourself.")
    if missing:
        return EXIT_REFUSED, (f"REFUSED: gates.{stage} is ON but gate_go_records.{stage} is missing {missing}. "
                              "Record the GO (who, when, link or quote) before any rollout.")
    return EXIT_NO_ROLLOUTS, (f"gate '{stage}' is ON with a GO recorded ({rec.get('who')}, {rec.get('when')}), but this "
                              "CLI never launches rollouts. Follow method/rollout_spec.md by hand.")


class Pipeline:
    def __init__(self, root: Path, cfg: dict, spec, opts: Options, out=None):
        self.root = Path(root)
        self.cfg = cfg
        self.spec = spec
        self.o = opts
        self.out = out or sys.stdout
        self.runs_dir = rel(self.root, cfg["paths"]["runs_dir"])
        self.method_dir = rel(self.root, cfg["paths"]["method_dir"])
        desk = dict(cfg.get("desk_agent") or {})
        desk.update({k: v for k, v in (spec.data.get("desk") or {}).items() if v is not None})
        for k, v in (("backend", opts.backend), ("model", opts.model), ("reasoning_effort", opts.effort)):
            if v:
                desk[k] = v
        self.desk = desk
        self.backend = get_backend(desk.get("backend", "codex"), desk)
        self.task_root = self.runs_dir / spec.id / f"v{spec.version}"
        self.run_id = self._pick_run_id()
        self.run_dir = self.task_root / self.run_id
        self.exit_code = EXIT_OK
        if not opts.dry_run:
            wr = workdir_root(cfg).resolve()
            if wr == self.root.resolve() or self.root.resolve() in wr.parents:
                raise PipelineError("isolation.workdir_root must be outside the project root (blindness)")

    def say(self, msg: str) -> None:
        print(msg, file=self.out, flush=True)

    def _pick_run_id(self) -> str:
        if self.o.run_id:
            if not all(c.isalnum() or c in "-_." for c in self.o.run_id):
                raise PipelineError(f"bad --run-id {self.o.run_id!r}")
            return self.o.run_id
        existing = sorted(p.name for p in self.task_root.iterdir() if p.is_dir()) if self.task_root.is_dir() else []
        if existing and not self.o.new_run:
            return existing[-1]
        base = today()
        rid, n = base, 2
        while rid in existing:
            rid, n = f"{base}-{n}", n + 1
        return rid

    def stage_dir(self, stage: str) -> Path:
        return self.run_dir / stage

    def state(self, stage: str) -> dict:
        return read_yaml(self.stage_dir(stage) / "run.yaml")

    def _parsed(self, stage: str) -> dict | None:
        st = self.state(stage)
        return st.get("parsed") if st.get("status") == DONE else None

    def _probe_stages(self) -> list[str]:
        out = []
        for mode in ("blackbox", "whitebox"):
            pm = (self.cfg.get("probe_modes") or {}).get(mode) or {}
            if pm.get("enabled", True) and int(pm.get("count", 1)) > 0:
                out.append(f"probe_{mode}")
        return out

    # ------------------------------------------------------------------ prompt rendering
    def _render(self, stage: str) -> str:
        st = DESK[stage]
        tpl = (self.method_dir / "prompts" / st.prompt).read_text(encoding="utf-8")
        common = (self.method_dir / "prompts" / "_common.md").read_text(encoding="utf-8")
        kl = self.spec.kill_lines
        meta = read_yaml(self.run_dir / "RUN.yaml")
        date = meta.get("date") or today()
        subs = {
            "TASK_ID": self.spec.id, "TASK_VERSION": self.spec.version,
            "TASK_TITLE": str(self.spec.data.get("title", "")), "DATE": date, "STAGE": stage, "OUT_DIR": "out",
            "TASK_DIR": "task", "REPORT": f"out/{st.report}", "PRIOR_SCREEN": "prior/screen_card.md",
            "METHOD_VERSION": git_head(self.root)[:12], "KILL_LINES": kl.as_text(),
            "SINGLE_MAX": f"{kl.single_max:.2f}", "BO4": f"{kl.best_of_4:.2f}", "PASS4": f"{kl.pass_at_4:.2f}",
            "UB95": f"{kl.upper95:.2f}", "TAU": f"{kl.tau:.2f}", "WALLCLOCK_HOURS": f"{self.spec.wallclock_hours():g}",
            "PEERS": "\n".join(f"- {d}" for _, d in self.spec.peer_cards()) or "- (none listed in task.yaml)",
        }
        prompt = tpl.replace("{{COMMON}}", common)
        for k, v in subs.items():
            prompt = prompt.replace("{{" + k + "}}", v)
        left = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", prompt)))
        if left:
            raise PipelineError(f"{st.prompt}: unrendered placeholders {left}")
        return prompt

    def _prior_report(self, stage: str) -> Path | None:
        if stage != "anchored_rescore":
            return None
        p = self.stage_dir("screen") / "out" / DESK["screen"].report
        return p if p.is_file() and self.state("screen").get("status") == DONE else None

    def _desk_inputs_hash(self, stage: str, prompt: str) -> str:
        items = plan_inputs(stage, self.spec, self.root, self.method_dir, self._prior_report(stage))
        man = {dest: sha256_file(src) for src, dest in items}
        return sha256_text(json.dumps({"manifest": man, "prompt": sha256_text(prompt),
                                       "public_yaml": sha256_text(self.spec.public_yaml()),
                                       "backend": self.desk.get("backend"), "model": self.desk.get("model"),
                                       "effort": self.desk.get("reasoning_effort")}, sort_keys=True))

    # ------------------------------------------------------------------ dry run
    def _dry_run(self, stages: list) -> int:
        for s in stages:
            if s in LOCAL_STAGES:
                self.say(f"  {s}: local stage (no agent)")
                if s == "validate":
                    self.say(f"    task.yaml {'valid' if not self.spec.errors else 'INVALID'}; "
                             f"{len(self.spec.errors)} error(s), {len(self.spec.warnings)} warning(s)")
                continue
            if s not in DESK:
                continue
            if s.startswith("probe_") and s not in self._probe_stages():
                self.say(f"  {s}: disabled in config")
                continue
            prompt = self._render(s)
            items = plan_inputs(s, self.spec, self.root, self.method_dir,
                                self.stage_dir("screen") / "out" / DESK["screen"].report if s == "anchored_rescore" else None)
            req = self._request(s, prompt, Path("<WORKDIR>"), Path("<WORKDIR>/events.jsonl"), Path("<WORKDIR>/log.txt"))
            cmd = self.backend.command(req)
            mode = isolation_mode(self.cfg)
            self.say(f"\n=== {s}: rendered prompt (sha256 {sha256_text(prompt)[:16]}) ===")
            self.say(prompt)
            self.say(f"=== {s}: isolated workdir would contain (copy-only inputs) ===")
            for _, dest in items:
                self.say(f"    {dest}")
            self.say("    task/task_public.yaml   out/")
            if s == "probe_whitebox":
                for w in self.spec.withheld_whitebox():
                    self.say(f"    WITHHELD from grader_src: {w}")
            self.say(f"=== {s}: isolation mode = {mode} ===")
            if mode == "bwrap":
                self.say("    masked with empty tmpfs/devnull: project root, task dir, grader source, hidden_data, workdir root")
            self.say(f"=== {s}: command (NOT executed) ===")
            self.say("    " + " ".join(cmd))
        self.say("\ndry-run: nothing written, no agent called")
        return EXIT_OK

    def _request(self, stage: str, prompt: str, workdir: Path, events: Path, log: Path) -> LaunchRequest:
        return LaunchRequest(stage=stage, task_id=self.spec.id, prompt=prompt, workdir=workdir, events_path=events,
                             log_path=log, model=str(self.desk.get("model")), effort=str(self.desk.get("reasoning_effort")),
                             web_search=bool(self.desk.get("web_search", True)), sandbox=str(self.desk.get("sandbox", "workspace-write")),
                             extra_args=list(self.desk.get("extra_args") or []))

    # ------------------------------------------------------------------ run meta
    def _write_run_meta(self) -> None:
        p = self.run_dir / "RUN.yaml"
        meta = read_yaml(p)
        if not meta:
            meta = {"label": LABEL, "visibility": "AIUC-internal (private repo only)", "task_id": self.spec.id,
                    "task_version": self.spec.version, "run_id": self.run_id, "date": today(), "created": now_iso(),
                    "redteam_version": __version__}
        meta.update({"task_yaml_sha256": sha256_file(self.spec.task_dir / "task.yaml"),
                     "repo_commit": git_head(self.root), "updated": now_iso(),
                     "kill_lines": self.spec.kill_lines.to_dict(), "pairings": self.spec.pairings,
                     "isolation_mode": isolation_mode(self.cfg), "gate_rule": "strict", "anchored_upper_bound": True,
                     "desk_agent": {k: self.desk.get(k) for k in ("backend", "model", "reasoning_effort", "web_search")}})
        write_yaml(p, meta)

    # ------------------------------------------------------------------ driver
    def run(self) -> int:
        stages = self.o.stages or ORDER
        for s in stages:
            if s in GATED:
                code, msg = check_gate(self.cfg, s)
                self.say(f"redteam: {msg}")
                return code
            if s not in ORDER:
                raise PipelineError(f"unknown stage {s!r}; stages: {ORDER + GATED}")
        if self.spec.errors and not (self.o.dry_run or stages == ["validate"]):
            raise PipelineError("task.yaml is invalid; run `redteam validate` for the full list:\n  - "
                                + "\n  - ".join(self.spec.errors))
        self.say(f"redteam {__version__}: task {self.spec.id} v{self.spec.version}  run {self.run_id}  "
                 f"backend {self.desk.get('backend')}  model {self.desk.get('model')}  effort {self.desk.get('reasoning_effort')}"
                 + ("  [DRY-RUN]" if self.o.dry_run else ""))
        if self.o.dry_run:
            return self._dry_run(stages)
        self.run_dir.mkdir(parents=True, exist_ok=True)
        with file_lock(self.run_dir / ".lock", blocking=False):
            self._write_run_meta()
            stopped = False
            for s in stages:
                handler = {"validate": self._stage_validate, "strict_gate": self._stage_strict_gate,
                           "aggregate": self._stage_aggregate, "index": self._stage_index}.get(s, None)
                ok = handler(s) if handler else self._desk(s)
                if ok is False:
                    self.exit_code = max(self.exit_code, EXIT_STAGE)
                    if s not in ("aggregate", "index"):
                        self.say(f"  pipeline stopped at {s}; fix the cause then re-run with --resume or --force")
                        stopped = True
                        break
            if stopped:
                if "aggregate" in stages:
                    self._stage_aggregate("aggregate")
                if "index" in stages:
                    self._stage_index("index")
        return self.exit_code

    # ------------------------------------------------------------------ local stages
    def _local_write(self, stage: str, data: dict, status: str = DONE, reason: str = "") -> None:
        d = self.stage_dir(stage)
        d.mkdir(parents=True, exist_ok=True)
        run = {"label": LABEL, "task_id": self.spec.id, "task_version": self.spec.version, "run_id": self.run_id,
               "stage": stage, "status": status, "reason": reason or None, "finished": now_iso(),
               "repo_commit": git_head(self.root), "inputs_sha256": data.pop("_inputs_sha256", None)}
        run.update(data)
        write_yaml(d / "run.yaml", run)

    def _stage_validate(self, stage: str) -> bool:
        data = {"errors": self.spec.errors, "warnings": self.spec.warnings,
                "_inputs_sha256": sha256_file(self.spec.task_dir / "task.yaml"),
                "kill_lines": self.spec.kill_lines.to_dict(), "wallclock_hours": self.spec.wallclock_hours(),
                "pairings": self.spec.pairings}
        self._local_write(stage, data, DONE if not self.spec.errors else "INCOMPLETE")
        self.say(f"  validate: {'OK' if not self.spec.errors else 'FAILED'} ({len(self.spec.warnings)} warning(s))")
        for w in self.spec.warnings:
            self.say(f"    WARN {w}")
        for e in self.spec.errors:
            self.say(f"    ERROR {e}")
        return not self.spec.errors

    def _stage_strict_gate(self, stage: str) -> bool:
        scr, anc = self._parsed("screen"), self._parsed("anchored_rescore")
        if scr is None or anc is None:
            self._local_write(stage, {}, "INCOMPLETE", "needs COMPLETE screen and anchored_rescore")
            self.say("  strict_gate: waiting for COMPLETE screen + anchored_rescore")
            return False
        res = strict_gate(scr, anc, self.spec.kill_lines)
        res["_inputs_sha256"] = sha256_text(json.dumps([scr, anc], sort_keys=True))
        ok = res["strict_verdict"] is not None
        self._local_write(stage, res, DONE if ok else "INCOMPLETE", "" if ok else "no strict verdict derivable")
        self.say(f"  strict_gate: strict={res['strict_verdict']} (gate)  anchored={res['anchored_verdict']} (upper bound)  "
                 f"basis={res['attack_basis']}  outcome={res['outcome']}")
        for n in res["notes"]:
            self.say(f"    note: {n}")
        return ok

    def _gate_allows(self, stage: str) -> tuple[bool, str]:
        if self.o.continue_on_cut:
            return True, ""
        sg = self.state("strict_gate")
        if sg.get("status") != DONE:
            return False, "strict_gate not COMPLETE (run earlier stages, or pass --continue-on-cut)"
        if not sg.get("advance") and (self.cfg.get("pipeline") or {}).get("stop_on_strict_cut", True):
            return False, f"strict verdict {sg.get('strict_verdict')}: later stages skipped (stop_on_strict_cut; --continue-on-cut overrides)"
        return True, ""

    def _stage_aggregate(self, stage: str) -> bool:
        sg = self.state("strict_gate")
        rt = self._parsed("redteam")
        probes = {s: self._parsed(s) for s in self._probe_stages()}
        skipped = [s for s in ("redteam", *self._probe_stages()) if self.state(s).get("status") == "SKIPPED"]
        res = aggregate(sg if sg.get("status") == DONE else None, rt, probes, skipped)
        if skipped and res["saturation_outcome"] == "CUT":
            res["outcome"] = "CUT"
        res["_inputs_sha256"] = sha256_text(json.dumps([sg.get("strict_verdict"), rt, probes], sort_keys=True, default=str))
        complete = res["outcome"] != "INCOMPLETE"
        self._local_write(stage, res, DONE if complete else "INCOMPLETE", "" if complete else "earlier stages incomplete")
        meta = read_yaml(self.run_dir / "RUN.yaml")
        meta.update({"strict_verdict": res["strict_verdict"], "anchored_verdict": res["anchored_verdict_upper_bound"],
                     "redteam_verdict": res["redteam_verdict"], "outcome": res["outcome"],
                     "environment_fix_required": res["environment_fix_required"],
                     "probe_findings_by_mode": res["probe_findings_by_mode"], "updated": now_iso()})
        write_yaml(self.run_dir / "RUN.yaml", meta)
        self.say(f"  aggregate: outcome={res['outcome']}  strict={res['strict_verdict']}  "
                 f"anchored(upper bound)={res['anchored_verdict_upper_bound']}  redteam={res['redteam_verdict']}  "
                 f"env_fix_required={res['environment_fix_required']}")
        return complete

    def _stage_index(self, stage: str) -> bool:
        rows = []
        for s in ORDER:
            if s == "index":
                continue
            st = self.state(s)
            if not st:
                continue
            be = st.get("backend") or {}
            rows.append({"task_id": self.spec.id, "version": self.spec.version, "run_id": self.run_id, "stage": s,
                         "status": st.get("status"), "stage_verdict": st.get("stage_verdict") or st.get("strict_verdict"),
                         "outcome": st.get("outcome"), "strict_verdict": st.get("strict_verdict"),
                         "anchored_verdict": st.get("anchored_verdict") or st.get("anchored_verdict_upper_bound"),
                         "backend": be.get("backend"), "model": be.get("model"), "effort": be.get("reasoning_effort"),
                         "inputs_sha256": (st.get("inputs_sha256") or "")[:16], "finished": st.get("finished"),
                         "path": os.path.relpath(self.stage_dir(s), self.root), "label": LABEL})
        total = index_upsert(self.runs_dir / "INDEX.tsv", rows)
        self.say(f"  index: {os.path.relpath(self.runs_dir / 'INDEX.tsv', self.root)} updated "
                 f"({len(rows)} rows this run; {total} total)")
        return True

    # ------------------------------------------------------------------ desk stages
    def _desk(self, stage: str) -> bool:
        st_def = DESK[stage]
        if stage.startswith("probe_") and stage not in self._probe_stages():
            self.say(f"  {stage}: disabled in config probe_modes")
            return True
        if stage in ("redteam", *self._probe_stages()):
            allowed, why = self._gate_allows(stage)
            if not allowed:
                if self.state(stage).get("status") != DONE:
                    self._local_write(stage, {}, "SKIPPED", why)
                self.say(f"  {stage}: SKIPPED ({why})")
                return True
        prior = self._prior_report(stage)
        if stage == "anchored_rescore" and prior is None:
            self.say("  anchored_rescore: needs a COMPLETE screen first")
            self._local_write(stage, {}, "INCOMPLETE", "no COMPLETE screen report")
            return False
        prompt = self._render(stage)
        inputs_hash = self._desk_inputs_hash(stage, prompt)
        cur = self.state(stage)
        if cur.get("status") == DONE and cur.get("inputs_sha256") == inputs_hash and not self.o.force and not self.o.resume:
            self.say(f"  {stage}: up to date (COMPLETE, inputs unchanged) - skipped")
            return True

        resume_sid = None
        d = self.stage_dir(stage)
        if self.o.resume and cur.get("session_id") and cur.get("status") != DONE:
            resume_sid = cur["session_id"]
            self.say(f"  {stage}: resuming session {resume_sid}")
        elif cur and (cur.get("status") == DONE or (d / "out").exists()):
            if not (self.o.force or self.o.resume):
                self.say(f"  {stage}: previous {cur.get('status')} present; re-run with --force (fresh) or --resume")
                return False
            if self.o.force:
                self._supersede(stage)

        d.mkdir(parents=True, exist_ok=True)
        (d / "prompt.md").write_text(prompt, encoding="utf-8")
        events = d / "codex_events.jsonl"
        log = d / "codex.log"
        meta = {"label": LABEL, "task_id": self.spec.id, "task_version": self.spec.version, "run_id": self.run_id,
                "stage": stage, "status": "IN-PROGRESS", "started": now_iso(), "finished": None,
                "backend": self.backend.describe(self._request(stage, prompt, d, events, log)),
                "prompt_sha256": sha256_text(prompt), "inputs_sha256": inputs_hash, "repo_commit": git_head(self.root),
                "isolation_mode": isolation_mode(self.cfg)}
        write_yaml(d / "run.yaml", meta)

        # preflight the backend (e.g. codex login) before building a workdir
        pf = self.backend.preflight()
        if pf:
            meta.update({"status": "FAILED", "finished": now_iso(), "reason": f"backend preflight: {pf}"})
            write_yaml(d / "run.yaml", meta)
            self.say(f"  {stage}: FAILED backend preflight: {pf}")
            return False

        wd = build_workdir(stage, self.spec, self.cfg, self.root, self.method_dir, prior, self.spec.public_yaml())
        mode = isolation_mode(self.cfg)
        wrap = wrap_command([], wd.path, hide_paths(self.spec, self.cfg, self.root))[:-1] if mode == "bwrap" else []
        req = self._request(stage, prompt, wd.path, events, log)
        req.wrap = wrap
        meta["inputs_manifest_sha256"] = wd.inputs_hash()
        meta["workdir"] = str(wd.path)
        write_yaml(d / "run.yaml", meta)

        def is_done() -> bool:
            return (wd.out / "DONE.txt").is_file() and (wd.out / st_def.report).is_file()

        timeout_s = float((self.cfg.get("stage_timeouts_minutes") or {}).get(stage, 120)) * 60.0
        self.say(f"  {stage}: launching {self.desk.get('backend')} (isolation {mode}, timeout {timeout_s/60:.0f} min)")
        res = supervise(self.backend, req, is_done, self.cfg.get("supervisor") or {}, self.cfg.get("retries") or {},
                        timeout_s, clock=self.o.clock, resume_sid=resume_sid,
                        report_name=f"out/{st_def.report}", log=self.say)
        # copy outputs back
        for src in sorted(wd.out.rglob("*")):
            if src.is_file():
                t = d / src.relative_to(wd.path)
                t.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, t)
        meta.update({"finished": now_iso(), "supervisor": res.status, "session_id": res.session_id,
                     "resumes": res.resumes, "retries": res.errors, "attempts": res.attempts,
                     "supervisor_reason": res.reason or None})
        ok = self._finalise_desk(stage, d, meta, events)
        if not (self.cfg.get("isolation") or {}).get("keep_workdirs"):
            destroy_workdir(wd)
        elif meta:
            meta["workdir_kept"] = str(wd.path)
            write_yaml(d / "run.yaml", meta)
        return ok

    def _supersede(self, stage: str) -> None:
        d = self.stage_dir(stage)
        if not d.is_dir():
            return
        keep = d / ".superseded" / time.strftime("%Y%m%dT%H%M%S")
        keep.mkdir(parents=True, exist_ok=True)
        for p in list(d.iterdir()):
            if p.name != ".superseded":
                shutil.move(str(p), str(keep / p.name))

    def _finalise_desk(self, stage: str, d: Path, meta: dict, events: Path) -> bool:
        st_def = DESK[stage]
        report = d / "out" / st_def.report if (d / "out" / st_def.report).is_file() else d / st_def.report
        report = report if report.is_file() else d / "out" / st_def.report
        text = report.read_text(encoding="utf-8", errors="replace") if report.is_file() else ""
        rec, how = parse_record(text, st_def.record_names, st_def.known_keys)
        info = interpret(stage, rec) if rec else {}
        verdict = primary_verdict(stage, info) if info else None
        prompt = (d / "prompt.md").read_text(encoding="utf-8") if (d / "prompt.md").is_file() else ""

        checks: dict = {}
        if text:
            peers = peer_reports(self.runs_dir, stage, st_def.report, self.spec.id)
            peers.pop(self.spec.id, None)
            wc = (self.cfg.get("checks") or {}).get("wording") or {}
            if wc.get("enabled", True):
                checks["wording"] = wording_check(text, prompt, peers, wc)
            uc = (self.cfg.get("checks") or {}).get("urls") or {}
            if uc.get("enabled", True):
                checks["urls"] = url_check(text, uc, offline=self.o.offline)
        ic = (self.cfg.get("checks") or {}).get("independence") or {}
        if st_def.blind and ic.get("enabled", True):
            forbidden = [str(self.root.resolve()), str(self.spec.task_dir.resolve())]
            src = self.spec.grader_source()
            if src and stage != "probe_whitebox":
                forbidden.append(str(src))
            forbidden += [str(p) for p in self.spec.hidden_paths()]
            ev_text = events.read_text(encoding="utf-8", errors="replace") if events.is_file() else ""
            checks["independence"] = independence_check(ev_text, stage, forbidden, self.spec.canaries())

        supervisor_ok = meta.get("supervisor") == "OK"
        enforced_fail = []
        wc_cfg = (self.cfg.get("checks") or {}).get("wording") or {}
        if wc_cfg.get("enforce", True) and checks.get("wording", {}).get("status") == "FAIL":
            enforced_fail.append("wording")
        if ((self.cfg.get("checks") or {}).get("independence") or {}).get("enforce", True) \
                and checks.get("independence", {}).get("status") == "FAIL":
            enforced_fail.append("independence")
        if ((self.cfg.get("checks") or {}).get("urls") or {}).get("enforce", False) \
                and checks.get("urls", {}).get("status") == "FAIL":
            enforced_fail.append("urls")

        status = DONE
        reason = None
        if not supervisor_ok:
            status, reason = "INCOMPLETE", f"supervisor {meta.get('supervisor')}: {meta.get('supervisor_reason')}"
        elif how == "none" or not rec:
            status, reason = "INCOMPLETE", "no parseable record block in the report"
        elif not verdict and not stage.startswith("probe_"):
            status, reason = "INCOMPLETE", "record parsed but no verdict"
        elif enforced_fail:
            status, reason = "CHECK-FAILED", f"enforced check failed: {enforced_fail}"
        if info.get("souping") == "yes":
            reason = (reason + "; " if reason else "") + "souping_flag yes (excluded)"

        meta.update({"status": status, "reason": reason, "report": os.path.relpath(report, d) if report.is_file() else None,
                     "record_parsed_via": how, "record": rec, "parsed": info, "stage_verdict": verdict,
                     "outcome": OUTCOME.get(verdict or "", "FINDINGS" if stage.startswith("probe_") else "UNKNOWN"),
                     "checks": checks, "enforced_check_failures": enforced_fail})
        if stage == "anchored_rescore":
            meta["anchored_verdict"] = info.get("anchored_verdict")
        write_yaml(d / "run.yaml", meta)
        extra = ""
        if stage.startswith("probe_"):
            extra = f" findings_total={info.get('findings_total')} high={info.get('high')} (never counted toward saturation)"
        self.say(f"  {stage}: status={status} verdict={verdict}{extra}"
                 + (f"  [{reason}]" if reason else "")
                 + ("  checks: " + ", ".join(f"{k}={v.get('status')}" for k, v in checks.items()) if checks else ""))
        return status == DONE
