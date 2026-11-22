"""Project root discovery and config loading (config/runner.yaml merged over built-in defaults).

The project root is the directory that holds config/runner.yaml, method/ and schema/. It is found by
--root, then $REDTEAM_ROOT, then by walking up from the current directory. Nothing is hardcoded:
every path in the config is relative to the project root unless it is absolute.
"""
from __future__ import annotations

import copy
import os
from pathlib import Path

import yaml

CANONICAL_PAIRINGS = [
    {"id": "P1", "model": "Claude Opus 5.5", "harness": "Claude Code"},
    {"id": "P2", "model": "Gemini 4 Argon", "harness": "Antigravity"},
    {"id": "P3", "model": "Qwen 3.8 Max", "harness": "Qwen Code"},
    {"id": "P4", "model": "GPT-6.2 Sol", "harness": "Codex"},
]

DEFAULTS: dict = {
    "version": 2,
    "kill_lines": {"single_max": 0.70, "best_of_4": 0.60, "pass_at_4": 0.50, "upper95": 0.75, "tau": 0.60},
    "gate_rule": "strict",
    "anchored_upper_bound": True,
    "pairings": copy.deepcopy(CANONICAL_PAIRINGS),
    "desk_agent": {"backend": "codex", "cli": "codex", "model": "gpt-6.1-sol", "reasoning_effort": "high",
                   "web_search": True, "sandbox": "workspace-write", "extra_args": []},
    "probe_modes": {"blackbox": {"enabled": True, "count": 1}, "whitebox": {"enabled": True, "count": 1}},
    "pipeline": {"stop_on_strict_cut": True},
    "compute": {"gpu": False},
    "supervisor": {"stall_minutes": 15, "max_resumes": 4, "poll_seconds": 5, "kill_grace_seconds": 10},
    "retries": {"max_attempts": 4, "backoff_initial_seconds": 30, "backoff_factor": 2.0, "backoff_max_seconds": 600},
    "stage_timeouts_minutes": {"screen": 120, "anchored_rescore": 150, "redteam": 180,
                               "probe_blackbox": 120, "probe_whitebox": 120},
    "isolation": {"mode": "auto", "extra_hide": [], "workdir_root": None, "keep_workdirs": False},
    "checks": {
        "wording": {"enabled": True, "enforce": True, "max_repeat_frac": 0.10, "max_pair_jaccard": 0.10,
                    "max_prompt_copy_frac": 0.10, "min_sentence_words": 15, "shingle": 8},
        "urls": {"enabled": True, "enforce": False, "timeout_seconds": 20, "workers": 8},
        "independence": {"enabled": True, "enforce": True},
    },
    "paths": {"runs_dir": "runs", "method_dir": "method", "schema": "schema/task.schema.json",
              "state_dir": ".redteam_state"},
    "cost_rates": {"usd_per_gpu_hour": 3.0, "api_usd_per_run": 100.0, "basis": "ESTIMATED"},
    "gates": {"canary": "OFF", "panel": "OFF", "publish_or_share": "OFF"},
    "gate_go_records": {"canary": {"who": "", "when": "", "source": ""},
                        "panel": {"who": "", "when": "", "source": ""}},
}


class ConfigError(Exception):
    pass


def deep_merge(base: dict, over: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def find_root(explicit: str | None = None, start: str | None = None) -> Path:
    cand = explicit or os.environ.get("REDTEAM_ROOT")
    if cand:
        p = Path(cand).expanduser().resolve()
        if not (p / "config" / "runner.yaml").is_file():
            raise ConfigError(f"{p} is not a redteam project root (no config/runner.yaml)")
        return p
    p = Path(start or os.getcwd()).resolve()
    for d in [p, *p.parents]:
        if (d / "config" / "runner.yaml").is_file() and (d / "method").is_dir():
            return d
    raise ConfigError("could not find the project root (a directory with config/runner.yaml and method/). "
                      "Run from inside the repo, or pass --root / set REDTEAM_ROOT.")


def load_config(root: Path, path: str | None = None) -> dict:
    p = Path(path) if path else root / "config" / "runner.yaml"
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as e:
        raise ConfigError(f"cannot read config {p}: {e}") from e
    cfg = deep_merge(DEFAULTS, raw)
    cfg["_root"] = str(root)
    cfg["_path"] = str(p)
    if cfg["compute"].get("gpu"):
        raise ConfigError("config compute.gpu is true; every desk stage is CPU-only. Set it back to false.")
    if str(cfg.get("gate_rule", "")).lower() != "strict":
        raise ConfigError("gate_rule must be 'strict': the strict verdict is the promotion gate "
                          "(Amita, Nov 21 2026, 3:02 PM PT); the anchored verdict is only an upper bound")
    return cfg


def rel(root: Path, p: str | os.PathLike) -> Path:
    p = Path(os.path.expanduser(str(p)))
    return p if p.is_absolute() else (root / p)
