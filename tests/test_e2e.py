import os
import shutil

from redteam.cli import main


def _run_root(repo_root, tmp_path, extra_cfg=""):
    """Copy a minimal project (package not needed; we run via main() with REDTEAM_ROOT) into tmp so runs/ land there."""
    root = tmp_path / "proj"
    root.mkdir()
    for name in ("method", "schema", "config", "examples"):
        shutil.copytree(repo_root / name, root / name)
    if extra_cfg:
        with open(root / "config" / "runner.yaml", "a") as f:
            f.write("\n" + extra_cfg + "\n")
    return root


def _cli(root, *args):
    os.environ["REDTEAM_ROOT"] = str(root)
    return main(list(args))


def test_toy_end_to_end_stub(repo_root, tmp_path):
    root = _run_root(repo_root, tmp_path)
    rc = _cli(root, "run", str(root / "examples" / "toy_task"), "--backend", "stub", "--offline", "--new-run")
    assert rc == 0
    run = root / "runs" / "toy_task" / "v1"
    runs = list(run.iterdir())
    assert len(runs) == 1
    rdir = runs[0]
    import yaml
    agg = yaml.safe_load((rdir / "aggregate" / "run.yaml").read_text().split("\n", 2)[2])
    assert agg["outcome"] == "FIX"
    assert agg["strict_verdict"] == "CONDITIONAL"
    assert agg["anchored_verdict_upper_bound"] == "PASS-SCREEN"   # upper bound kept, not the gate
    assert agg["redteam_verdict"] == "FIX"
    assert agg["probe_findings_count_toward_saturation"] is False
    # every stage COMPLETE
    for stage in ("screen", "anchored_rescore", "strict_gate", "redteam", "probe_blackbox", "probe_whitebox"):
        st = yaml.safe_load((rdir / stage / "run.yaml").read_text().split("\n", 2)[2])
        assert st["status"] == "COMPLETE", (stage, st.get("reason"))
    # INDEX written and labelled
    idx = (root / "runs" / "INDEX.tsv").read_text()
    assert "ESTIMATED desk verdict, UNMEASURED" in idx and "toy_task" in idx


def test_idempotent_rerun_skips(repo_root, tmp_path):
    root = _run_root(repo_root, tmp_path)
    assert _cli(root, "run", str(root / "examples" / "toy_task"), "--backend", "stub", "--offline", "--new-run") == 0
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = _cli(root, "run", str(root / "examples" / "toy_task"), "--backend", "stub", "--offline")
    assert rc == 0
    assert buf.getvalue().count("up to date") >= 4


def test_gated_stage_refused(repo_root, tmp_path):
    root = _run_root(repo_root, tmp_path)
    rc = _cli(root, "run", str(root / "examples" / "toy_task"), "--stage", "canary")
    assert rc == 3   # REFUSED while gate OFF


def test_gate_on_but_no_record_still_refused(repo_root, tmp_path):
    root = _run_root(repo_root, tmp_path, extra_cfg="gates: {canary: ON, panel: OFF, publish_or_share: OFF}")
    rc = _cli(root, "run", str(root / "examples" / "toy_task"), "--stage", "canary")
    assert rc == 3   # ON but gate_go_records empty


def test_gate_on_with_record_never_runs_rollout(repo_root, tmp_path):
    cfg = ("gates: {canary: ON, panel: OFF, publish_or_share: OFF}\n"
           "gate_go_records: {canary: {who: Amita, when: '2026-11-21', source: 'quote'}, panel: {who: '', when: '', source: ''}}")
    root = _run_root(repo_root, tmp_path, extra_cfg=cfg)
    rc = _cli(root, "run", str(root / "examples" / "toy_task"), "--stage", "canary")
    assert rc == 4   # gate open + GO recorded, but the CLI never launches rollouts


def test_resume_after_stall_completes(repo_root, tmp_path):
    # stub stalls once on the screen, then the supervisor resumes and finishes.
    cfg = ('desk_agent: {backend: stub, stub: {behaviour: {screen: stall_once}}}\n'
           'supervisor: {stall_minutes: 0.05, max_resumes: 4, poll_seconds: 1, kill_grace_seconds: 1}')
    root = _run_root(repo_root, tmp_path, extra_cfg=cfg)
    assert _cli(root, "run", str(root / "examples" / "toy_task"), "--stage", "validate", "--stage", "screen",
                "--backend", "stub", "--offline", "--new-run") == 0
    import yaml
    rdir = next((root / "runs" / "toy_task" / "v1").iterdir())
    st = yaml.safe_load((rdir / "screen" / "run.yaml").read_text().split("\n", 2)[2])
    assert st["status"] == "COMPLETE"
    assert st["resumes"] >= 1


def test_dry_run_writes_nothing(repo_root, tmp_path):
    root = _run_root(repo_root, tmp_path)
    rc = _cli(root, "run", str(root / "examples" / "toy_task"), "--dry-run")
    assert rc == 0
    assert not (root / "runs" / "toy_task").exists()
