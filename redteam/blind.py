"""Enforced blindness: one isolated, disposable workdir per desk stage.

Only the inputs a stage is allowed to see are COPIED into a fresh temp dir outside the project:
  task/    card.md, grader_interface.md, sota_sources.md, task_public.yaml, extra/   (all stages)
  method/  the method files the prompt names                                       (all stages)
  peers/   other tasks' card files for duplicate checks (card prose only)          (all stages)
  prior/   the screen report                                                       (anchored_rescore only)
  grader_src/  READ-ONLY copy of the grader source minus secrets/hidden data       (probe_whitebox only)
  out/     the only place the agent writes
The red team and the probes never get prior verdicts, runs/ or anything else.

With isolation mode "bwrap" (default "auto" = bwrap when it works), the desk agent process additionally runs
in a mount namespace where the project root, the task dir, the grader source, every hidden_data path and the
workdir root (other stages' workdirs) are replaced by empty tmpfs mounts, and only this stage's workdir is
bound back in. Without bwrap, blindness relies on the copy-only workdir, the prompt and the post-hoc
independence check (see GETTING_STARTED.md, known gaps).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

METHOD_FILES = {
    "screen": ["kill_thresholds.md", "evidence_grounding_rule.md", "verdict_schema.md"],
    "anchored_rescore": ["kill_thresholds.md", "evidence_grounding_rule.md", "verdict_schema.md",
                         "refs/AMEND_2026-11-21_1204.md", "refs/frontier_reference_snapshot_2026-11-21.md"],
    "redteam": ["kill_thresholds.md", "evidence_grounding_rule.md", "verdict_schema.md"],
    "probe_blackbox": ["kill_thresholds.md"],
    "probe_whitebox": ["kill_thresholds.md"],
}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


@dataclass
class Workdir:
    path: Path
    manifest: dict = field(default_factory=dict)   # dest -> sha256
    readonly: list = field(default_factory=list)
    withheld: list = field(default_factory=list)

    @property
    def out(self) -> Path:
        return self.path / "out"

    def inputs_hash(self) -> str:
        return sha256_text(json.dumps(self.manifest, sort_keys=True))


def workdir_root(cfg: dict) -> Path:
    r = (cfg.get("isolation") or {}).get("workdir_root")
    base = Path(r).expanduser() if r else Path(tempfile.gettempdir()) / f"redteam-work-{os.getuid()}"
    base.mkdir(parents=True, exist_ok=True)
    os.chmod(base, 0o700)
    return base


def plan_inputs(stage: str, spec, root: Path, method_dir: Path, prior_report: Path | None = None) -> list[tuple[Path, str]]:
    """(source, dest) pairs a stage may see. Pure: used by both the real build and --dry-run."""
    items = [(src, "task/" + dest) for src, dest in spec.shared_inputs()]
    items += [(src, dest) for src, dest in spec.peer_cards()]
    for m in METHOD_FILES.get(stage, []):
        p = method_dir / m
        if p.is_file():
            items.append((p, "method/" + m))
    if stage == "anchored_rescore":
        if prior_report is None:
            raise ValueError("anchored_rescore needs the screen report")
        items.append((prior_report, "prior/screen_card.md"))
    if stage == "probe_whitebox":
        items += spec.whitebox_files()
    return items


def build_workdir(stage: str, spec, cfg: dict, root: Path, method_dir: Path, prior_report: Path | None = None,
                  public_yaml: str | None = None) -> Workdir:
    base = workdir_root(cfg)
    wd = Path(tempfile.mkdtemp(prefix=f"{spec.id}-{stage}-", dir=base))
    w = Workdir(path=wd)
    for src, dest in plan_inputs(stage, spec, root, method_dir, prior_report):
        t = wd / dest
        t.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, t)
        w.manifest[dest] = sha256_file(t)
    t = wd / "task" / "task_public.yaml"
    t.parent.mkdir(parents=True, exist_ok=True)
    t.write_text(public_yaml if public_yaml is not None else spec.public_yaml(), encoding="utf-8")
    w.manifest["task/task_public.yaml"] = sha256_file(t)
    if stage == "probe_whitebox":
        g = wd / "grader_src"
        if g.exists():
            for p in sorted(g.rglob("*"), reverse=True):
                mode = p.stat().st_mode
                p.chmod(mode & ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))
                w.readonly.append(p.relative_to(wd).as_posix())
            g.chmod(g.stat().st_mode & ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))
        w.withheld = spec.withheld_whitebox()
    w.out.mkdir()
    (wd / "MANIFEST.json").write_text(json.dumps({"stage": stage, "task_id": spec.id, "files": w.manifest,
                                                   "read_only": w.readonly, "withheld_from_grader_src": w.withheld},
                                                  indent=1, sort_keys=True), encoding="utf-8")
    return w


def destroy_workdir(w: Workdir) -> None:
    for p in [w.path, *w.path.rglob("*")]:
        try:
            if not p.is_symlink():
                p.chmod(p.stat().st_mode | stat.S_IWUSR | (stat.S_IXUSR if p.is_dir() else 0))
        except OSError:
            pass
    shutil.rmtree(w.path, ignore_errors=True)


# ---------------------------------------------------------------------- process isolation
_BWRAP_OK: dict = {}


def bwrap_available() -> bool:
    if "ok" not in _BWRAP_OK:
        exe = shutil.which("bwrap")
        ok = False
        if exe:
            try:
                ok = subprocess.run([exe, "--dev-bind", "/", "/", "--tmpfs", "/tmp", "true"],
                                    capture_output=True, timeout=10).returncode == 0
            except (OSError, subprocess.SubprocessError):
                ok = False
        _BWRAP_OK["ok"] = ok
    return _BWRAP_OK["ok"]


def isolation_mode(cfg: dict) -> str:
    m = str((cfg.get("isolation") or {}).get("mode", "auto")).lower()
    if m == "auto":
        return "bwrap" if bwrap_available() else "copy-only"
    if m == "bwrap" and not bwrap_available():
        raise RuntimeError("isolation.mode is bwrap but bubblewrap is not available or does not work here")
    if m in ("none", "copy-only"):
        return "copy-only"
    return m


def hide_paths(spec, cfg: dict, root: Path) -> list[Path]:
    hide = [root.resolve(), spec.task_dir.resolve()]
    src = spec.grader_source()
    if src:
        hide.append(src)
    hide += spec.hidden_paths()
    for x in (cfg.get("isolation") or {}).get("extra_hide", []) or []:
        hide.append(Path(os.path.expanduser(x)).resolve())
    hide.append(workdir_root(cfg).resolve())
    # keep unique, existing paths only
    out = []
    for p in hide:
        if p.exists() and p not in out:
            out.append(p)
    return out


def wrap_command(cmd: list[str], workdir: Path, hide: list[Path]) -> list[str]:
    """bwrap: keep the host view, mask every hidden path with an empty tmpfs (dirs) or /dev/null (files),
    then bind this stage's workdir back in. Order matters: later mounts win."""
    w = ["bwrap", "--dev-bind", "/", "/"]
    for p in sorted(hide, key=lambda x: len(x.parts)):
        if p.is_dir():
            w += ["--tmpfs", str(p)]
        else:
            w += ["--ro-bind", "/dev/null", str(p)]
    w += ["--bind", str(workdir), str(workdir), "--chdir", str(workdir), "--die-with-parent", "--"]
    return w + cmd


# ---------------------------------------------------------------------- post-hoc independence check
_RECURSIVE = re.compile(r"(?:^|[\s\"';&|(])(grep\s+-[A-Za-z]*[rR]|rg\s|find\s+(?:/|~|\.\.))")


def _commands(events_text: str) -> list[str]:
    """Shell commands the agent ran, from a JSONL event log (codex --json or the stub). Falls back to [] on
    non-JSON logs; the canary scan below still covers the full text."""
    cmds: list[str] = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("command", "cmd") and isinstance(v, (str, list)):
                    cmds.append(v if isinstance(v, str) else " ".join(map(str, v)))
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for line in events_text.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            walk(json.loads(line))
        except ValueError:
            continue
    return cmds


def independence_check(events_text: str, stage: str, forbidden: list[str], canaries: list[str]) -> dict:
    """Post-hoc blindness check of one stage's session log.
    FAIL ("leak") if a command touched a forbidden path (project root, task dir, runs/, hidden data, grader
    source outside a white-box copy, the Codex session store) or any canary string appears anywhere in the log.
    WARN for recursive searches that start outside the workdir. Matched canary strings are never printed."""
    leaks, warns = [], []
    cmds = _commands(events_text)
    for c in cmds:
        for f in forbidden:
            if f and f in c:
                leaks.append(f"command touched forbidden path {f}")
        for pat in ("runs/", ".codex/sessions", ".codex/history", "thread_history", "state_5.sqlite"):
            if re.search(r"(?:^|[\s\"'=/])" + re.escape(pat), c):
                leaks.append(f"command references {pat}")
        if stage in ("redteam", "probe_blackbox", "probe_whitebox") and re.search(r"(screen_card|audit_card)\.md", c):
            leaks.append("command references a prior-stage report")
        if _RECURSIVE.search(c):
            warns.append("recursive search starting outside the workdir: " + _RECURSIVE.search(c).group(1).strip())
    n = sum(1 for c in canaries if c and c in events_text)
    if n:
        leaks.append(f"{n} hidden-data canary string(s) appear in the session log")
    status = "FAIL" if leaks else ("WARN" if warns else "PASS")
    return {"status": status, "commands_seen": len(cmds), "leaks": sorted(set(leaks)), "warnings": sorted(set(warns))}
