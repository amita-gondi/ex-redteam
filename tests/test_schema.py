
import yaml

from redteam.taskspec import validate_task


def _load_toy(repo_root):
    return yaml.safe_load((repo_root / "examples" / "toy_task" / "task.yaml").read_text())


def test_toy_task_valid(repo_root, cfg, schema_path):
    spec = validate_task(repo_root / "examples" / "toy_task", cfg, schema_path)
    assert spec.errors == [], spec.errors
    assert spec.id == "toy_task"


def test_missing_required_lists_all(tmp_path, repo_root, cfg, schema_path):
    d = tmp_path / "bad01"
    d.mkdir()
    (d / "task.yaml").write_text("schema_version: 1\nid: bad01\n")
    spec = validate_task(d, cfg, schema_path)
    # many required fields missing -> many errors, not just one
    assert len(spec.errors) >= 5
    joined = " ".join(spec.errors)
    assert "version" in joined and "owner" in joined and "card" in joined and "grader" in joined


def test_bad_values_and_placeholders(tmp_path, repo_root, cfg, schema_path):
    data = _load_toy(repo_root)
    data["id"] = "has space"
    data["reward"]["scale"]["frozen"] = False
    data["card"]["goal"] = "TODO"
    data["souping_dependency"] = True
    d = tmp_path / "toy_task"
    d.mkdir()
    (d / "task.yaml").write_text(yaml.safe_dump(data))
    # copy referenced files so only the intended errors show
    import shutil
    for f in ("card.md", "grader_interface.md", "sota_sources.md"):
        shutil.copy(repo_root / "examples" / "toy_task" / f, d / f)
    shutil.copytree(repo_root / "examples" / "toy_task" / "grader_src", d / "grader_src")
    spec = validate_task(d, cfg, schema_path)
    j = " ".join(spec.errors)
    assert "$.id" in j
    assert "frozen" in j
    assert "placeholder" in j.lower()
    assert "souping_dependency" in j


def test_hidden_data_must_not_be_shared_input(tmp_path, repo_root, cfg, schema_path):
    import shutil
    src = repo_root / "examples" / "toy_task"
    d = tmp_path / "toy_task"
    shutil.copytree(src, d)
    data = yaml.safe_load((d / "task.yaml").read_text())
    # point an extra shared input at the hidden dir -> must be rejected
    data.setdefault("inputs", {})["extra"] = ["grader_src/hidden/heldout.csv"]
    (d / "task.yaml").write_text(yaml.safe_dump(data))
    spec = validate_task(d, cfg, schema_path)
    assert any("hidden" in e.lower() or "grader source" in e.lower() for e in spec.errors), spec.errors
