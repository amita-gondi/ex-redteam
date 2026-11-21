# archive/: imported history (read-only record)

> **Every verdict in this folder is an ESTIMATED desk verdict, UNMEASURED.** They are LLM desk judgements (screens, re-scores, red teams). No rollout, canary or panel was run for any task. Nothing here certifies a task. A 4×4 panel can kill a task but cannot clear it (`method/kill_thresholds.md`).

This folder holds everything that was in the repo before the generic `redteam` CLI rebuild (Nov 21, 2026). It was moved here with `git mv`; nothing was deleted, and `git log --follow <path>` still shows each file's history. The snapshot of the source pipelines was taken Nov 21, 2026, 1:54 PM PT, with later commits up to `4a9c004`.

Paths written *inside* these files (for example `/workspace/...` in `PROVENANCE.md`, `legacy/tools/import_runs.py` or the snapshot method docs) are provenance records of where material came from on the original machine. They are not used by the CLI and will not resolve on another machine.

## Contents
| Path | What it is |
|---|---|
| `runs/` | Imported desk runs: `runs/<task_id>/<date>/<run_kind>/run.yaml` (+ copied report), `runs/_program/` cross-task summaries, `runs/INDEX.tsv` (the imported index). `run_kind` is `design_redteam` (v2), `self_review` (v3, same session, not independent), `redteam` (v3/v4 independent), `screen` (creative v4, W), `screen_audit` (creative v4 audit with anchored fields). |
| `tasks/` | Imported task cards: `T*` = v4 FIX packets (pairing tables are pre-migration: old roster), `D*` = hidden task cards, `C010` = the worked-example creative card. Each has a `PROVENANCE.md`. These cards are prose only and have **no `task.yaml`**, so the new CLI cannot run them until someone writes one (see `tasks/_template/`). |
| `legacy/bin/redteam` | The previous single-stage wrapper (superseded by the `redteam` package). |
| `legacy/tools/` | `import_runs.py` (how the records above were imported), `wording_check.py`, `independence_check.py` (logic now in `redteam/checks.py` and `redteam/blind.py`). |
| `legacy/tasks_template_v0/` | The old prose-only task template. |
| `legacy/method_4a9c004/`, `legacy/config_4a9c004/`, `legacy/README_4a9c004.md`, `legacy/GETTING_STARTED_4a9c004.md` | Verbatim copies of the method docs, config and top-level docs as of commit `4a9c004`, before the paths were made generic. Kept so the provenance references in them survive. |

## Status at import (unchanged by the move)
- The creative v4 screen audit was IN-PROGRESS at import: its 120 `screen_audit` runs carry `status: IN-PROGRESS`.
- The weakness (W) screen was partial at import (W01–W11).
- Runs made before Amita's 12:04 PM PT evidence rule carry `anchored_addendum: pending` and an `ANCHORED_ADDENDUM_PENDING.md` placeholder.
- Later results (strict view, anchored addenda for the v4 red team and W tasks) were produced outside this repo and are **not** imported here.

## Excluded at import (and why)
Souping/merging material (excluded entirely), GDM feedback and other source inputs, Codex session JSONLs and logs, large binaries, and anything matching the secret scan.
