# ex-redteam (private)

> **AIUC-internal. Private repo only.** Everything here is AIUC/Extrapolate internal: task designs, hidden task cards, desk verdicts and method drafts. Do not make the repo public, fork it publicly or share it outside the team without Amita's approval (bar F4).

**New here? Start with [GETTING_STARTED.md](GETTING_STARTED.md)**: prerequisites, adding your task, `bin/redteam` commands, gates, DO NOT list, worked example and known gaps.

## Purpose
A task-agnostic home for red-teaming RL research tasks against saturation by a strong frontier researcher (a ~10T model with 12 h; assumption). It holds:
- one method: the attacker prompt, rollout spec, evidence grounding rule, kill thresholds and verdict schema;
- one pipeline config (`gate_rule: strict`; `anchored_upper_bound: true`);
- a per-task history of every desk verdict so far.

## Status
- **Every imported verdict is an ESTIMATED desk verdict, UNMEASURED.** No rollout, canary or panel has been run for any task. Nothing here certifies a task, and a 4×4 panel can kill but not clear (`method/kill_thresholds.md`).
- Canary and panel stages are **OFF** and require Amita's GO (`config/runner.yaml`).
- Snapshot taken Nov 21, 2026, 1:54 PM PT.
- **IN-PROGRESS at import:**
  - The creative v4 screen audit was still RUNNING. All 120 cards have anchored records, but aggregation and validation weren't done. Its 120 `screen_audit` runs are marked `status: IN-PROGRESS`.
  - The weakness (W) screen is partial: W01–W11 are screened, W12–W14 aren't yet, and the Claude W pipeline was still writing. The W10 anchored addendum was running; a snapshot is included and marked IN-PROGRESS.
- **Awaiting anchored addenda:** every run made before Amita's 12:04 PM PT evidence rule carries `anchored_addendum: pending` and an `ANCHORED_ADDENDUM_PENDING.md` placeholder:
  - the v2 design red team,
  - the v3 self-review and v3 independent red team,
  - the v4 independent red team,
  - the creative screen (the audit covers 120 of its 125 cards),
  - the W screen.

## Layout
```
method/      attacker_prompt.md, rollout_spec.md (canonical pairing set), spec_notes.md (open questions + alignment debt),
             evidence_grounding_rule.md, kill_thresholds.md, verdict_schema.yaml + verdict_schema.md,
             refs/ (AMEND 12:04 rule verbatim; frontier_reference snapshot)
config/      runner.yaml (screen -> anchored re-score -> red team; canary/panel OFF) + README.md
tasks/       _template/ (card.md, grader.md, sota_sources.md); T02..T18 = v4 FIX packets; D01..D32 = hidden task cards
runs/        <task_id>/<date>/<run_kind>/run.yaml (+ copied record); _program/ = cross-task summaries; INDEX.tsv
tools/       import_runs.py (how the records were imported; read-only on sources),
             wording_check.py (boilerplate check), independence_check.py (post-hoc red-team blindness check)
bin/         redteam: thin wrapper; one desk stage for one task via codex exec (--dry-run supported)
method/prompts/  _common.md + screen.md, anchored_rescore.md, redteam.md (task-agnostic stage prompts)
```

`run_kind` is one of:
- `design_redteam` (v2),
- `self_review` (v3, same session),
- `redteam` (v3 independent, v4 independent),
- `screen` (creative v4, W),
- `screen_audit` (creative v4 audit with the anchored fields).

## Workflow
1. Write `tasks/<id>/card.md`, `grader.md` and `sota_sources.md` from `tasks/_template/`.
2. **Screen**: a desk saturation screen against the kill lines, giving PASS-SCREEN, CONDITIONAL or CUT.
3. **Anchored re-score**: apply `method/evidence_grounding_rule.md` (attack_basis, demonstrated refs with gap, subfield SOTA). The **strict** verdict is the promotion gate (`config/runner.yaml` → `gate_rule: strict`): LITERATURE-ONLY and ASSUMED attacks use the evidence-only / pre-anchoring scores; only DEMONSTRATED-AGENT evidence may lower an attack score. The anchored verdict is recorded as an **upper bound** on survival, not the advance decision.
4. **Red team**: an independent review that doesn't read earlier verdicts, giving HOLDS, FIX or CUT.
5. Write each stage as `runs/<id>/<date>/<run_kind>/run.yaml` (`method/verdict_schema.yaml`).
6. **Canary, then panel**: only after Amita's GO, per `method/rollout_spec.md`.

## Imported runs
| Source | Date (PT) | Runs | Notes |
|---|---|---|---|
| v2 design red team | Nov 20 | 15 tasks | 03A excluded (merging) |
| v2 rerank | Nov 20 | `_program/` | 03A rows dropped |
| v3 catalog self-review T01–T23 | Nov 20, 11:21 PM | 23 | same-session review, not independent |
| v3 independent red team T01–T23 | Nov 21, 12:19 AM | 23 | 0 HOLDS / 10 FIX / 13 CUT |
| v4 independent red team | Nov 21 | 50 | 0 HOLDS / 24 FIX / 26 CUT |
| creative v4 screen | Nov 21 | 125 | |
| creative v4 screen audit | Nov 21 | 120 | IN-PROGRESS |
| weakness screen W01–W11 | Nov 21 | 11 | W12–W14 pending |

Task cards: `tasks/T*` are copies of the v4 FIX packets. Their pairing tables are pre-migration (they list Carbon, 6.1 Sol and Astra); the canonical set is in `config/runner.yaml`. `tasks/D*` are the hidden D cards.

## Excluded (and why)
- Souping/merging material: model-souping-ro and the v2 task 03A (expert consolidation with task-arithmetic/TIES attacks).
- GDM feedback and other source inputs, including the v3 `feedback_disposition.md`.
- Codex session JSONLs, `codex_run.log`, watcher logs and `logs/` directories.
- Prompts other than the binding AMEND rule, and run tooling scripts.
- Large binaries.
- Anything matching the secret scan.

Sources were copied, never modified or moved.

## Canonical pairings (Amita, Nov 21)
Opus 5.5 + Claude Code; Gemini 4 Argon + Antigravity; Qwen 3.8 Max + Qwen Code; GPT-6.2 Sol + Codex. Exact pins are OPEN (bar F7).
