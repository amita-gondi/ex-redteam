# Trimmed validation budget: top-tier staged plan (ESTIMATED)

All numbers are **ESTIMATED H100 GPU-hours** from `/workspace/task_design_v2_codex/validation_budget.csv` (per-row in `trimmed_budget.csv`) and $ at the design's assumed $3/GPU-h ("ESTIMATE_NOT_QUOTE"). Preparation, outer inference and failed-version redesign are excluded, as in the v2 plan (99_open_questions). This is a plan, not a spend authorization.

## Principles

1. Fund the full bar program only for the 4 likely-pass tasks (04A, 05B, 05A, 01A).
2. Give each at-risk task one decisive anchor (the gated slice). Promotion of any at-risk task needs a separate owner decision; its full cost is listed below but **not** included.
3. Likely-cut tasks get 0 GPU-h (decided analytically or by merge).
4. Order inside the funded tasks: cheap kills (B1/B2/B3/A5) → saturation kills (S2 best-of-k, A8) → E6 + structural evidence → native panel and scaling. E6 and S1/S3/S4 run only after the earlier gates pass.

## Staged table

| Stage | Tasks | Experiments | Est. GPU-h | Est. $ (at $3/h) | Gate to proceed |
|---|---|---|---:|---:|---|
| 0 | All 16 | Red-team spec/contract fixes; analytic checks (04B speed bound, 08A exp(−loss), 03B/07A/02B reward formulas); typed-interface/probe harness. CPU + prep only. | 0 | $0 | Fixes written and reviewed; formula counterexamples rerun on CPU. |
| 1a | 01A, 04A, 05A, 05B | E1, E2, E3 (v2 default + red-team strongest combined baseline, 3 seeds each), E5 (5 seeds) | 38,332 | $114,996 | B1 = 0; B2 = 0; B3 mean ≥ 0.5; A5 strongest baseline ≤ reference − 0.20. Fail → kill. |
| 1b | 01B, 02A, 02B, 03B, 04B, 06A, 07A, 07B | One decisive anchor each (06A grade-only quantizer anchors; others baseline ×3 vs reference ×3) | 22,368 | $67,104 | ≥0.20 raw gap over the red-team baseline → owner decides promotion (unfunded here). Else cut/merge. |
| 2 | Likely-pass passing 1a | E4 checklist, S2 best-of-k/pass@k, E12 adversarial audits, E14 resource contracts | 64,820 | $194,460 | A8; hard kills: max ≤ 0.70, mean oracle best-of-4 ≤ 0.60, pass@4 ≤ 0.50 at R ≥ 0.60; D1 audits. Fail → kill before E6. |
| 3 | Likely-pass passing 2 | E6 (all 105 runs, unchanged), E7, E13, E8 canaries | 270,772 | $812,316 | B4 M ≥ 0.2 with lower CI > 0.1; A7; B8; B9; C7; owner-signed canaries. |
| 4 | Likely-pass passing 3 | E9 native panel (4 pairings × 4), E10, E11, E15, S1, S3, S4 at 2 of 4 levels | 274,820 | $824,460 | B5; C2/C6; B7/B11; A9; A6; projected upper-95% < 0.75. |
| **Total** | | | **671,112** | **$2,013,336** | |

- **vs the v2 fixed plan:** 3,433,336 GPU-h ($10,300,008) → **671,112 GPU-h ($2,013,336)**. Savings **2,762,224 GPU-h ($8,286,672), 80.5%**.
- **Committed up front (Stages 0–1):** 60,700 GPU-h ($182,100). Stages 2–4 (610,412 GPU-h) are released only by gates, so the realized spend is lower if any likely-pass task is killed.
- **Where the savings come from:** dropping 12 tasks from the full program saves 2,729,712 GPU-h, of which the at-risk slice spends back 22,368; halving S4 on the 4 funded tasks saves 54,880. Check: 3,433,336 − 2,729,712 − 54,880 + 22,368 = 671,112.

Per funded task (full v2 ledger → trimmed):

| Task | v2 ledger GPU-h | S4 halved | Trimmed GPU-h | of which E6 |
|---|---:|---:|---:|---:|
| 04A | 346,528 | −28,160 | 318,368 | 94,080 |
| 05B | 143,136 | −10,240 | 132,896 | 47,040 |
| 05A | 62,488 | −4,320 | 58,168 | 21,420 |
| 01A | 151,472 | −12,160 | 139,312 | 42,000 |

## Contingent promotions (not in the total)

If an at-risk task passes its anchor and the owner promotes it, its trimmed full program (v2 ledger with S4 halved, minus the anchor already spent) would be:

| Task | Trimmed full program GPU-h | Est. $ |
|---|---:|---:|
| 06A | 156,880 | $470,640 |
| 02B | 156,496 | $469,488 |
| 07A | 156,496 | $469,488 |
| 02A | 136,912 | $410,736 |
| 01B | 117,328 | $351,984 |
| 07B | 136,912 | $410,736 |
| 03B | 136,912 | $410,736 |
| 04B | 312,992 | $938,976 |

## Statistical cost of the trims, and whether the bar is still met

- **Dropped tasks (12 of 16 receive no E6/S1–S4/E9).** No bar evidence at all for them; they cannot be certified under this plan. For the 4 funded tasks every A/B/C criterion keeps its v2 experiment.
- **E6 unchanged** (105 runs, 5 seeds per cell, per the settled "E6 on all tasks" decision applied to every task that is carried forward). B4 (lower CI > 0.1), A7 and B8 (2³ factorial, insight share lower CI ≥ 50%) keep their full power. No trim.
- **S4 halved (4 → 2 difficulty levels, still 5 fresh seeds per level).** A9 (generator + B1–B3 on ≥ 5 instances) and B4 at the tested levels are unchanged in n. Cost: only 2 points on the difficulty curve, so no monotone difficulty fit and a coarser choice of the "calibrated harder setting"; if the harder level fails, a third level must be run (+1/4 of the original S4 each). Bar status: A9 is still met (and is also covered by E15); B4 is primarily established by E6, which is untouched. The real loss is to Amita's saturation gate: fewer demonstrated difficulty knobs to fall back on if a frontier model saturates the base level.
- **S1, S2, S3 unchanged** for funded tasks. S2 (3 instances × 8 attempts) was already flagged by v2 and the red team as a minimum pilot; the hard kill thresholds keep their v2 uncertainty.
- **At-risk anchors (3 vs 3 seeds).** 95% CI half-width on the gap is ≈ 2.78·σ·√(2/3): ±0.18 raw at σ = 0.08, ±0.23 at σ = 0.10. Power to detect a true 0.20 gap (one-sided α = 0.05): ≈0.80 at σ = 0.08, 0.65 at σ = 0.10, 0.39 at σ = 0.15. Using the v2 E5 design (3 baseline vs 5 reference seeds) raises power to 0.91 / 0.78 / 0.49. These anchors are reliable for **kills** and for HOLD, not for promotion; promotion still requires the full Stage 1a–4 program. σ is unmeasured until E10 (C6).
- **Stage 1a for funded tasks** uses the v2 seeds (E3: 3 per recipe; E5: 5) with the red-team baseline replacing one of the two E3 recipes at the same cost. Comparing that baseline with the reference is the 3 vs 5 design above.

Sources: `validation_budget.csv` (all row values), experiment tables in the 01–08 files (run counts), `ACCEPTANCE_BAR_GENERAL.md` summary table (criteria thresholds), red-team `00_summary.md` (cuts and issue list).
