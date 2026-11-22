"""run.yaml writing/reading, the runs/INDEX.tsv upsert, and small provenance helpers."""
from __future__ import annotations

import contextlib
import datetime as dt
import fcntl
import os
import subprocess
from pathlib import Path

import yaml

from . import LABEL

HEADER = ("# Written by the redteam CLI. Desk verdicts are ESTIMATED LLM judgements, UNMEASURED by rollouts.\n"
          "# AIUC-internal: private repo only.\n")
INDEX_COLS = ["task_id", "version", "run_id", "stage", "status", "stage_verdict", "outcome", "strict_verdict",
              "anchored_verdict", "backend", "model", "effort", "inputs_sha256", "finished", "path", "label"]


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def today() -> str:
    return dt.date.today().isoformat()


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(HEADER)
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=120)
    os.replace(tmp, path)


def read_yaml(path: Path) -> dict:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return {}


def git_head(root: Path) -> str:
    try:
        r = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=10)
        head = r.stdout.strip() or "none"
        d = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "--", "method", "config", "schema", "redteam"],
                           capture_output=True, text=True, timeout=10).stdout.strip()
        return head + ("+dirty" if d else "")
    except (OSError, subprocess.SubprocessError):
        return "none"


@contextlib.contextmanager
def file_lock(path: Path, blocking: bool = True):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a+") as f:
        flags = fcntl.LOCK_EX | (0 if blocking else fcntl.LOCK_NB)
        try:
            fcntl.flock(f, flags)
        except BlockingIOError:
            raise RuntimeError(f"lock held by another redteam process: {path}") from None
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


def index_upsert(index_path: Path, rows: list[dict]) -> int:
    """Idempotent upsert keyed by (task_id, version, run_id, stage). Returns the number of rows written."""
    with file_lock(index_path.with_suffix(".lock")):
        existing: dict = {}
        order: list = []
        if index_path.is_file():
            lines = index_path.read_text(encoding="utf-8").splitlines()
            body = [ln for ln in lines if ln and not ln.startswith("#")]
            if body:
                hdr = body[0].split("\t")
                for ln in body[1:]:
                    r = dict(zip(hdr, ln.split("\t"), strict=False))
                    k = (r.get("task_id"), r.get("version"), r.get("run_id"), r.get("stage"))
                    if k not in existing:
                        order.append(k)
                    existing[k] = r
        for r in rows:
            r = {c: _cell(r.get(c)) for c in INDEX_COLS}
            k = (r["task_id"], r["version"], r["run_id"], r["stage"])
            if k not in existing:
                order.append(k)
            existing[k] = r
        tmp = index_path.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(f"# {LABEL}. One row per (task, version, run, stage); rewritten by `redteam run`.\n")
            f.write("\t".join(INDEX_COLS) + "\n")
            for k in sorted(order, key=lambda x: tuple(str(i) for i in x)):
                f.write("\t".join(existing[k].get(c, "") for c in INDEX_COLS) + "\n")
        os.replace(tmp, index_path)
        return len(order)


def _cell(v) -> str:
    if v is None:
        return ""
    return str(v).replace("\t", " ").replace("\n", " ")
