# <TASK_ID> grader

## Contract
- Inputs accepted from the candidate (types, size caps); everything else is ignored.
- Trusted parent computes the truth from executed state; it never imports candidate code.
- Missing, malformed or skipped work scores 0 (fail closed).

## Scoring
- Raw metric S, anchors b and c (frozen before any rollout), F(S) piecewise as in bar v2.
- Seeds: ≥3 private seeds including one secret seed.
- Re-grade noise: {REGRADE_SD} (UNMEASURED until bar C2 study).

## Anti-gaming fixtures (each must score 0 on the vulnerable path)
| Attack | Fixture | Expected | Measured |
|---|---|---|---|
| spoofed result / early exit | | 0 | UNMEASURED |
| protected-dev extraction | | 0 | UNMEASURED |
| weight/label smuggling | | 0 | UNMEASURED |

## Clean re-measurement
Fresh container, pinned grader version, all seeds; the clean score is official (rollout_spec.md §6).
