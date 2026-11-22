import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


@pytest.fixture
def repo_root():
    return ROOT


@pytest.fixture
def cfg(repo_root):
    from redteam.config import load_config
    return load_config(repo_root)


@pytest.fixture
def schema_path(repo_root, cfg):
    from redteam.config import rel
    return rel(repo_root, cfg["paths"]["schema"])


@pytest.fixture(autouse=True)
def _tmp_workdir_root(tmp_path, monkeypatch):
    # keep every test's isolated workdirs under tmp, never near the repo
    monkeypatch.setenv("TMPDIR", str(tmp_path))
