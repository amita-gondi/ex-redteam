# Evidence grounding rule (binding since Amita, Nov 21, 2026, 12:04 PM PT)

Applies to every attack estimate made by a screen, a re-score or a red team. Verbatim sources are in `refs/AMEND_2026-11-21_1204.md` and `refs/frontier_reference_snapshot_2026-11-21.md`. The second is a snapshot taken at 1:54 PM PT on Nov 21, while the audit job that maintains it was still running, so later versions may differ.

## 1. Anchor every attack to demonstrated results
An attack estimate must cite **demonstrated** results: a published or measured agent or model result on that capability, or the closest comparable one. Examples are RE-Bench, METR time-horizon, MLE-bench, PaperBench, KernelBench/KernelAgent, AlphaEvolve, AI Scientist-v2, PostTrainBench, system-card ML-R&D evals, and the subfield's own SOTA papers or leaderboards. For each one, record:
- what was achieved,
- by which model and scaffold,
- in what time and with what compute,
- the **gap** between that and what this task's attack needs.

Fetch everything you cite. Never fabricate. Mark anything unverified.

## 2. Three evidence classes (`attack_basis`)
| Value | Meaning | What it can justify |
|---|---|---|
| `DEMONSTRATED-AGENT` | An identified frontier model, in a documented agent protocol, found, integrated, executed and validated the relevant combined recipe without human steering, within a comparable time and compute budget. | The only basis for a high attack score. It is necessary, not sufficient. |
| `LITERATURE-ONLY` | A human-built recipe exists (KNOWN-RECIPE), but autonomous discovery, integration and validation within the budget is undemonstrated. Longer-budget, partial or non-agent automation also lands here. | A task-specific ESTIMATE of what an agent must still discover, integrate and validate in 12 h. The verdict **rests on assumption** and must say so. |
| `ASSUMED` | Neither of the above. | ESTIMATED projections only. No invented success probabilities. |

Notes:
- Demonstrating components A and B separately does not demonstrate A+B.
- Missing autonomy, budget or validation metadata blocks promotion to `DEMONSTRATED-AGENT`.
- Published demonstrations stay author-reported until replicated.
- Don't reflexively lower every score. Where agents *have* demonstrated the capability (for example short-loop HPO, kernel speedups, post-training gap closure), say so and score high.

## 3. Subfield SOTA anchor
Record the subfield's best known human or system result, with its source and year. Anchor the task's north star (what R≈1 or the reference R corresponds to) to it, not to an invented target.

## 4. Anchored estimate and verdict (upper bound on survival)
Every verdict record carries:
- an ANCHORED estimate: single run (point and range), best-of-4, pass@4 at R≥0.60, and upper 95%, derived from a stated distribution rather than a fixed offset, and marked ESTIMATED;
- the anchored verdict;
- its binding line;
- its flip against the earlier verdict;
- `verdict_rests_on_assumption: yes|no`.

The field names are in `verdict_schema.yaml` (`evidence.*`, `anchored.*`). The anchored verdict is **not** the promotion decision. It is an upper bound on survival: the most optimistic desk reading, in which only demonstrated agent capability justifies a high attack score.

## 5. Promotion gate (Amita, 3:02 PM PT, Nov 21 2026)
`config/runner.yaml` sets `gate_rule: strict` and `anchored_upper_bound: true`.

The **strict** rule is the promotion gate (`advance_if`, `outcome`, whether a task moves forward):

- If `attack_basis` is `LITERATURE-ONLY` or `ASSUMED`, treat that attack as executable by a 12-hour frontier agent and use the evidence-only / pre-anchoring scores and verdict (`new_verdict` after a screen re-score; the earlier stage's verdict on an addendum).
- Only `DEMONSTRATED-AGENT` evidence may lower an attack score below that pre-anchoring estimate. In that case the anchored scores and verdict are also the gate values.
- Record both. `strict_verdict` is the gate. `anchored_verdict` is kept as the upper bound.

A task that survives only in the anchored reading is not promoted. It remains a hypothesis for later rollouts, which still need Amita's GO.

## 6. Status of imported results
Every verdict imported into `runs/` is an **ESTIMATED desk verdict, UNMEASURED**. No rollout, canary or panel has been run.
