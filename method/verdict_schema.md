# Verdict schema (explainer for `verdict_schema.yaml`)

One schema covers every desk stage, so a task's history reads as a single sequence of records under `runs/<task_id>/<date>/<run_kind>/run.yaml`.

## Two verdict fields
- **`stage_verdict`**: the label exactly as the stage wrote it.
  - Screens and audits: PASS-SCREEN / CONDITIONAL / CUT.
  - Red teams: HOLDS / FIX / CUT.
  - The v2 design red team: "needs fixes" / cut.
  - The v3 catalog self-review: likely-pass / at-risk, with "release HOLD" on every task.
- **`outcome`**: one cross-stage value, via `outcome_mapping`:

| Stage label | outcome |
|---|---|
| PASS-SCREEN, HOLDS, likely-pass | ADVANCE (go to the next stage; never "cleared") |
| CONDITIONAL, FIX, needs fixes, at-risk | FIX |
| CUT, cut | CUT |
| (panel stage, later) any interval touching a line | HOLD |

`ADVANCE` only means the next desk stage should look at the task. Nothing in this repo is measured, and a panel can kill but not clear (see `kill_thresholds.md`).

## Estimates and anchoring
- `estimates.*` is the stage's own ESTIMATED attack distribution.
- `evidence.*` holds the fields from Amita's 12:04 PM PT rule: `attack_basis` (DEMONSTRATED-AGENT / LITERATURE-ONLY / ASSUMED), `demonstrated_ref`, `gap_to_attack`, `subfield_sota_ref` and `verdict_rests_on_assumption`.
- `anchored.*` is the re-score against demonstrated agent results. When it exists, it is the headline.
  - For a `screen_audit` run, `outcome` is computed from `anchored.verdict` if present, otherwise from `stage_verdict`.
- Records made before the 12:04 rule have `evidence.attack_basis: na` and `anchored_addendum: pending`.

## Labels
Every imported record carries `label: "ESTIMATED desk verdict, UNMEASURED"` and `measurement_status: UNMEASURED`. Only a run with real rollouts and a clean re-grade (`rollout_spec.md`, section 6) may set `MEASURED`.
