"""redteam CLI entrypoint.

  redteam run <task_dir> [--stage S ...] [--dry-run] [--resume] [--force] [--continue-on-cut]
                         [--run-id ID] [--new-run] [--backend B] [--model M] [--effort E] [--offline]
  redteam validate <task_dir>
  redteam status  <task_dir|task_id> [--version V]
  redteam report  <task_dir|task_id> [--version V]

Exit codes: 0 ok; 1 a stage failed/incomplete; 2 usage/validation; 3 gated stage refused; 4 gate open but no rollouts.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .config import ConfigError, find_root, load_config, rel
from .pipeline import EXIT_OK, EXIT_USAGE, Options, Pipeline, PipelineError
from .report import report as do_report
from .report import status as do_status
from .stages import GATED, ORDER
from .taskspec import validate_task

DESK_ORDER = [s for s in ORDER]


def _add_common(ap):
    ap.add_argument("--root", help="project root (default: $REDTEAM_ROOT or search upward for config/runner.yaml)")
    ap.add_argument("--config", help="path to runner.yaml (default: <root>/config/runner.yaml)")


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="redteam", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", action="version", version=f"redteam {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="run the desk pipeline (or selected stages) on a task")
    _add_common(r)
    r.add_argument("task_dir")
    r.add_argument("--stage", action="append", dest="stages", choices=ORDER + GATED,
                   help="run only this stage (repeatable); default: the full desk pipeline in order")
    r.add_argument("--dry-run", action="store_true", help="print rendered prompts, workdir contents and commands; write nothing")
    r.add_argument("--resume", action="store_true", help="resume the agent session of a partial stage")
    r.add_argument("--force", action="store_true", help="re-run a COMPLETE/partial stage fresh (old attempt kept under .superseded/)")
    r.add_argument("--continue-on-cut", action="store_true", help="run the red team and probes even if the strict gate is CUT")
    r.add_argument("--run-id", help="explicit run id (default: latest run of this task version, else today's date)")
    r.add_argument("--new-run", action="store_true", help="start a new run id instead of continuing the latest")
    r.add_argument("--backend", choices=["codex", "stub"], help="override desk_agent.backend")
    r.add_argument("--model", help="override desk_agent.model")
    r.add_argument("--effort", help="override desk_agent.reasoning_effort")
    r.add_argument("--offline", action="store_true", help="skip URL liveness checks (no outbound network)")

    v = sub.add_parser("validate", help="validate task.yaml and its referenced files; list every problem")
    _add_common(v)
    v.add_argument("task_dir")

    for name, helptext in (("status", "show a task's run status"), ("report", "print a markdown report of a task's latest run")):
        s = sub.add_parser(name, help=helptext)
        _add_common(s)
        s.add_argument("task", help="task directory or task id")
        s.add_argument("--version", help="restrict to task version V")
    return ap


def _resolve(args):
    start = None
    if getattr(args, "task_dir", None):
        start = Path(args.task_dir).resolve()
        start = start if start.is_dir() else start.parent
    root = find_root(getattr(args, "root", None), str(start) if start else None)
    cfg = load_config(root, getattr(args, "config", None))
    return root, cfg


def _task_arg_to_dir(root, cfg, task: str):
    p = Path(task)
    if p.is_dir() and (p / "task.yaml").is_file():
        return p.resolve(), None
    cand = Path.cwd() / task
    if (cand / "task.yaml").is_file():
        return cand.resolve(), None
    return None, task   # treat as task id for status/report


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.cmd == "status" or args.cmd == "report":
            start = Path(args.task)
            start = start if start.is_dir() else (start.parent if start.parent != Path("") else None)
            root = find_root(args.root, str(start.resolve()) if start and start.exists() else None)
            cfg = load_config(root, args.config)
            tdir, tid = _task_arg_to_dir(root, cfg, args.task)
            if tdir is not None:
                import yaml
                data = yaml.safe_load((tdir / "task.yaml").read_text(encoding="utf-8")) or {}
                tid = str(data.get("id") or tdir.name)
                version = args.version or (str(data.get("version")) if data.get("version") else None)
            else:
                version = args.version
            fn = do_status if args.cmd == "status" else do_report
            return fn(root, cfg, tid, version, sys.stdout)

        root, cfg = _resolve(args)
        schema_path = rel(root, cfg["paths"]["schema"])
        spec = validate_task(args.task_dir, cfg, schema_path)
        if args.cmd == "validate":
            if spec.errors:
                print(f"redteam validate: {args.task_dir}: INVALID ({len(spec.errors)} error(s), "
                      f"{len(spec.warnings)} warning(s))", file=sys.stderr)
                for e in spec.errors:
                    print(f"  ERROR {e}", file=sys.stderr)
                for w in spec.warnings:
                    print(f"  warn  {w}", file=sys.stderr)
                return EXIT_USAGE
            print(f"redteam validate: {args.task_dir}: OK (id={spec.id} v{spec.version}; {len(spec.warnings)} warning(s))")
            for w in spec.warnings:
                print(f"  warn  {w}")
            return EXIT_OK

        opts = Options(stages=args.stages, dry_run=args.dry_run, resume=args.resume, force=args.force,
                       run_id=args.run_id, new_run=args.new_run, backend=args.backend, model=args.model,
                       effort=args.effort, offline=args.offline, continue_on_cut=args.continue_on_cut)
        return Pipeline(root, cfg, spec, opts).run()
    except (ConfigError, PipelineError) as e:
        print(f"redteam: {e}", file=sys.stderr)
        return getattr(e, "code", EXIT_USAGE)
    except KeyboardInterrupt:
        print("redteam: interrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
