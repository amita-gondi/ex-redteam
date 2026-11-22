import json

from redteam.blind import (
    build_workdir,
    bwrap_available,
    destroy_workdir,
    independence_check,
    isolation_mode,
    plan_inputs,
)
from redteam.config import load_config
from redteam.taskspec import validate_task


def _spec(repo_root):
    cfg = load_config(repo_root)
    from redteam.config import rel
    return cfg, validate_task(repo_root / "examples" / "toy_task", cfg,
                              rel(repo_root, cfg["paths"]["schema"]))


def test_redteam_workdir_excludes_prior_and_grader_source(repo_root):
    cfg, spec = _spec(repo_root)
    w = build_workdir("redteam", spec, cfg, repo_root, repo_root / "method")
    files = {p.relative_to(w.path).as_posix() for p in w.path.rglob("*") if p.is_file()}
    assert "task/card.md" in files and "task/grader_interface.md" in files
    assert "task/task_public.yaml" in files
    assert not any("grader_src" in f for f in files)          # red team gets no grader source
    assert not any(f.startswith("prior/") for f in files)      # and no prior verdicts
    # hidden data and its canary are absent
    assert not any("hidden" in f for f in files)
    pub = (w.path / "task" / "task_public.yaml").read_text()
    assert "TOYTASK-CANARY" not in pub and "source_path" not in pub
    destroy_workdir(w)


def test_whitebox_probe_gets_grader_source_readonly_but_not_hidden(repo_root):
    cfg, spec = _spec(repo_root)
    w = build_workdir("probe_whitebox", spec, cfg, repo_root, repo_root / "method")
    files = {p.relative_to(w.path).as_posix() for p in w.path.rglob("*") if p.is_file()}
    assert "grader_src/score.py" in files and "grader_src/config.yaml" in files
    assert not any("hidden" in f for f in files)               # hidden labels withheld even white-box
    # grader_src copies are read-only
    import os
    sc = w.path / "grader_src" / "score.py"
    assert not (os.stat(sc).st_mode & 0o222)
    # no canary leaked anywhere in the workdir
    for p in w.path.rglob("*"):
        if p.is_file():
            assert "TOYTASK-CANARY-9f13ab27" not in p.read_text(errors="replace")
    destroy_workdir(w)


def test_blackbox_probe_has_no_grader_source(repo_root):
    cfg, spec = _spec(repo_root)
    items = plan_inputs("probe_blackbox", spec, repo_root, repo_root / "method")
    assert not any("grader_src" in d for _, d in items)


def test_independence_check_flags_runs_access_and_canary():
    log = '\n'.join([
        json.dumps({"type": "item.completed", "item": {"type": "command_execution", "command": "cat runs/T01/screen/run.yaml"}}),
    ])
    r = independence_check(log, "redteam", ["/some/repo"], ["SECRET-CANARY-1"])
    assert r["status"] == "FAIL"
    assert any("runs/" in h for h in r["leaks"])
    clean = json.dumps({"type": "item.completed", "item": {"type": "command_execution", "command": "ls task"}})
    r2 = independence_check(clean, "redteam", ["/some/repo"], ["SECRET-CANARY-1"])
    assert r2["status"] == "PASS"
    leaked = "the agent printed SECRET-CANARY-1 somehow"
    r3 = independence_check(leaked, "redteam", [], ["SECRET-CANARY-1"])
    assert r3["status"] == "FAIL"


def test_isolation_mode_reports():
    cfg = load_config_dummy()
    m = isolation_mode(cfg)
    assert m in ("bwrap", "copy-only")
    assert isinstance(bwrap_available(), bool)


def load_config_dummy():
    import copy

    from redteam.config import DEFAULTS
    return copy.deepcopy(DEFAULTS)
