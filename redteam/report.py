"""`redteam status` and `redteam report`: read-only summaries of a task's runs/ history. No agent, no writes."""
from __future__ import annotations

import os
from pathlib import Path

from .config import rel
from .provenance import read_yaml
from .stages import ORDER


def _runs_for(runs_dir: Path, task_id: str, version: str | None):
    base = runs_dir / task_id
    out = []
    if not base.is_dir():
        return out
    for vdir in sorted(base.iterdir()):
        if not vdir.is_dir() or not vdir.name.startswith("v"):
            continue
        if version and vdir.name != f"v{version}":
            continue
        for rdir in sorted(vdir.iterdir()):
            if rdir.is_dir() and (rdir / "RUN.yaml").is_file():
                out.append(rdir)
    return out


def status(root: Path, cfg: dict, task_id: str, version: str | None, out) -> int:
    runs_dir = rel(root, cfg["paths"]["runs_dir"])
    runs = _runs_for(runs_dir, task_id, version)
    if not runs:
        print(f"redteam status: no runs for {task_id}" + (f" v{version}" if version else "")
              + f" under {os.path.relpath(runs_dir, root)}/", file=out)
        return 0
    for rdir in runs:
        meta = read_yaml(rdir / "RUN.yaml")
        print(f"\n{task_id} v{meta.get('task_version')}  run {meta.get('run_id')}  ({os.path.relpath(rdir, root)})", file=out)
        print(f"  outcome={meta.get('outcome')}  strict={meta.get('strict_verdict')} (gate)  "
              f"anchored={meta.get('anchored_verdict')} (upper bound)  redteam={meta.get('redteam_verdict')}  "
              f"env_fix={meta.get('environment_fix_required')}", file=out)
        print(f"  {meta.get('label')}  |  backend={(meta.get('desk_agent') or {}).get('backend')} "
              f"model={(meta.get('desk_agent') or {}).get('model')}  isolation={meta.get('isolation_mode')}", file=out)
        for s in ORDER:
            st = read_yaml(rdir / s / "run.yaml")
            if not st:
                print(f"    {s:16} -", file=out)
                continue
            v = st.get("stage_verdict") or st.get("strict_verdict") or ""
            chk = st.get("checks") or {}
            chks = " ".join(f"{k}:{(chk[k] or {}).get('status')}" for k in chk) if chk else ""
            extra = ""
            if s.startswith("probe_"):
                p = st.get("parsed") or {}
                extra = f" findings={p.get('findings_total')} high={p.get('high')} (uncounted)"
            print(f"    {s:16} {st.get('status'):12} {v:14} {chks}{extra}"
                  + (f"  [{st.get('reason')}]" if st.get("reason") else ""), file=out)
    return 0


def report(root: Path, cfg: dict, task_id: str, version: str | None, out) -> int:
    runs_dir = rel(root, cfg["paths"]["runs_dir"])
    runs = _runs_for(runs_dir, task_id, version)
    if not runs:
        print(f"# {task_id}: no runs found", file=out)
        return 0
    rdir = runs[-1]
    meta = read_yaml(rdir / "RUN.yaml")
    agg = read_yaml(rdir / "aggregate" / "run.yaml")
    sg = read_yaml(rdir / "strict_gate" / "run.yaml")
    p = print
    p(f"# {task_id} v{meta.get('task_version')} desk red-team report", file=out)
    p(f"\n_Run {meta.get('run_id')} ({os.path.relpath(rdir, root)}). {meta.get('label')}. "
      f"Rollouts UNMEASURED; a 4x4 panel can kill a task but not clear it._\n", file=out)
    p(f"- **Aggregate outcome:** {agg.get('outcome', 'INCOMPLETE')}", file=out)
    p(f"- **Strict verdict (promotion gate):** {sg.get('strict_verdict')} "
      f"(basis {sg.get('attack_basis')}; {sg.get('strict_source')})", file=out)
    p(f"- **Anchored verdict (upper bound on survival, not the gate):** {sg.get('anchored_verdict')}", file=out)
    p(f"- **Red team:** {agg.get('redteam_verdict')}", file=out)
    p(f"- **Flips:** strict vs anchored {sg.get('flip_strict_vs_anchored')}; strict vs screen {sg.get('flip_strict_vs_screen')}; "
      f"anchored vs screen {sg.get('flip_anchored_vs_screen')}", file=out)
    p(f"- **Kill lines:** {meta.get('kill_lines')}", file=out)
    by_mode = agg.get("probe_findings_by_mode") or {}
    p("\n## Desk exploit probes (tagged by mode; NEVER counted toward saturation metrics)", file=out)
    if not by_mode:
        p("- none run", file=out)
    for mode, lst in by_mode.items():
        for f in lst:
            p(f"- **{mode}**: high={f.get('high')} medium={f.get('medium')} low={f.get('low')} "
              f"blocks_panel={f.get('blocks_panel')} hidden_data_reachable={f.get('hidden_data_reachable')} "
              f"- top: {f.get('top_finding')}", file=out)
    p(f"- environment_fix_required: {agg.get('environment_fix_required')}", file=out)
    p("\n## Stage records", file=out)
    for s in ORDER:
        st = read_yaml(rdir / s / "run.yaml")
        if not st:
            continue
        p(f"\n### {s}  ({st.get('status')})", file=out)
        rec = st.get("record") or {}
        if rec:
            for k, v in rec.items():
                p(f"- {k}: {v}", file=out)
        elif st.get("reason"):
            p(f"- {st.get('reason')}", file=out)
    return 0
