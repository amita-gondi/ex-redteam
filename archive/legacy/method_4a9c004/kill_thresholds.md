# Kill thresholds

**Attacker model:** a ~10T-parameter research model (an **assumption**; parameter counts for closed systems are unverified) with **12 hours** and the task's full budget, using every lawful known recipe. Paper recall and lawful algorithmic generalization are valid solutions and count against the task.

R is the task score in [0, 1]. The pass threshold is τ = 0.60 (bar v2 S2).

| Line | Kill when | Notes |
|---|---|---|
| Single-run max | > 0.70 | Highest valid R across all runs except exploit probes and disqualified runs |
| Best-of-4 | > 0.60 | Per pairing: max of its 4 panel runs; report the highest pairing |
| pass@4 at τ | > 0.50 | Per pairing: P(any of 4 runs has R ≥ τ); Clopper–Pearson (exact) |
| Upper 95% bound | ≥ 0.75 | On the strongest pairing's mean R (t-interval at n=4: mean ± 3.18·SD/√4), or the S4 projected upper 95% |

Any line crossed → CUT or REDESIGN.

## A panel can kill, but it cannot clear
Computed, not estimated (also in `rollout_spec.md`, section 5):
- With 0 of 4 runs passing, the Clopper–Pearson 95% upper bound on p is 0.602. The implied pass@4 upper bound is 0.975.
- Even 0 of 16 pooled gives p ≤ 0.206, which is still a pass@4 bound of 0.602.
- So a 4×4 panel can **trigger** a kill but cannot by itself **clear** the pass@4 line.
- Clearing needs the S2 study: at least 3 instance blocks × at least 8 runs. At 24 runs, 0 passes gives a pass@4 bound of 0.459.

Decision rule:
1. Any kill line crossed → CUT/REDESIGN.
2. Otherwise, any interval touching a line → **HOLD** ("borderline CI = HOLD").
3. Otherwise → PASS-PANEL, still subject to S2/S4.

## Desk screens
The screens, audits and red teams imported here apply the same four lines to **ESTIMATED** attack distributions. Their verdicts are forecasts and never certify a pass. `binding_line` records which line decided the verdict (`single>0.70`, `bo4>0.60`, `pass4>0.50`, `ub95>=0.75`, `none`, `duplicate`, `souping`).
