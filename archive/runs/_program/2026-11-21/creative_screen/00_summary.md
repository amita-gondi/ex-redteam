# Creative v4 saturation screen: summary

This is a desk review done on CPU only, with no GPU work and no rollouts. It was screened against the bar on Nov 21 2026 (PT). Every number below is an **ESTIMATED** forecast, and every measurement (rollouts, grader noise, score ladders) is **UNMEASURED**. Nothing here is a measured result or a certification.

The attacker is a frontier model of about 10T parameters with 12 hours of test-time compute. A card is CUT if a single run is likely to score above 0.70, oracle best-of-4 is above 0.60, pass@4 at R≥0.60 is above 0.50, or the projected upper 95% bound is at least 0.75. Souping and model merging were excluded: no card depends on them and no attack uses them.

## Counts (125 cards)

| Verdict | Count |
|---|---|
| PASS-SCREEN | 5 |
| CONDITIONAL | 21 |
| CUT | 99 |

Two cards were reconciled. C002 and C008 were written up as CONDITIONAL, but their own ESTIMATED numbers cross a kill line. C002 has best-of-4 0.63, pass@4 0.54 and upper 95% 0.79; C008 has upper 95% 0.76. Both are therefore CUT under the bar. The author verdict is kept in `screen.tsv` (`author_verdict`), and a note was added to each card.

## Survivors, ranked
PASS-SCREEN cards come first, then CONDITIONAL. Within each group they are sorted by best-of-4, then upper 95%, then the single-run estimate, all ESTIMATED.

| Rank | Card | Verdict | Single (range) | Best-of-4 | pass@4 | Upper 95% | Decisive GPU-h old→new | Nearest existing (strength) |
|---|---|---|---|---|---|---|---|---|
| 1 | [C086](cards/C086.md) Research world models graded only by executed improvements | PASS-SCREEN | 0.40 (0.20-0.57) | 0.50 | 0.12 | 0.67 | 20→1200 | catalog T03 MODERATE; D21 WEAK |
| 2 | [C045](cards/C045.md) Pretraining with stateful external memory under update churn | PASS-SCREEN | 0.42 (0.21-0.59) | 0.51 | 0.23 | 0.68 | 18→400 | T05 MODERATE; T20 WEAK; 06A WEAK |
| 3 | [C116](cards/C116.md) A tool-building curriculum for unfamiliar accelerator DSLs | PASS-SCREEN | 0.41 (0.24-0.64) | 0.51 | 0.24 | 0.69 | 20→144 | T03 MODERATE; 05B WEAK; D24 WEAK |
| 4 | [C099](cards/C099.md) Recheck a curriculum proxy when the learner changes | PASS-SCREEN | 0.42 (0.22-0.58) | 0.52 | 0.16 | 0.68 | 12→480 | v3 01A MODERATE; D26 MODERATE |
| 5 | [C081](cards/C081.md) Masked-input regularization after repetitions stop being exchangeable | PASS-SCREEN | 0.43 (0.24-0.58) | 0.52 | 0.16 | 0.68 | 14→408 | catalog T02 MODERATE; FIX T02 MODERATE |
| 6 | [C024](cards/C024.md) Retain scientific uncertainty in compressed experiment records | CONDITIONAL | 0.42 (0.23-0.61) | 0.53 | 0.29 | 0.70 | 8→120 | catalog-T05 MODERATE; catalog-T03 WEAK |
| 7 | [C106](cards/C106.md) Improve a world model by limiting its planner's evidence access | CONDITIONAL | 0.44 (0.25-0.66) | 0.54 | 0.31 | 0.71 | 22→144 | T13 WEAK; D32 WEAK; D22 WEAK |
| 8 | [C112](cards/C112.md) Recover scientific images while learning a better acquisition policy | CONDITIONAL | 0.45 (0.26-0.65) | 0.55 | 0.33 | 0.72 | 18→160 | T10 MODERATE; FIX T11 WEAK |
| 9 | [C064](cards/C064.md) Router regularization invariant to token packing | CONDITIONAL | 0.47 (0.26-0.64) | 0.56 | 0.32 | 0.70 | 14→768 | 04A MODERATE; 05B WEAK |
| 10 | [C010](cards/C010.md) Train through delayed simulator corrections | CONDITIONAL | 0.46 (0.25-0.64) | 0.56 | 0.34 | 0.72 | 14→120 | FIX-T13 WEAK; D03 MODERATE |
| 11 | [C103](cards/C103.md) First build a privacy attack, then train a deletion method | CONDITIONAL | 0.46 (0.28-0.65) | 0.56 | 0.38 | 0.72 | 20→176 | T17 MODERATE; 07B WEAK |
| 12 | [C127](cards/C127.md) A curriculum flywheel that learns from cross-project interference | CONDITIONAL | 0.45 (0.26-0.68) | 0.56 | 0.34 | 0.73 | 22→400 | FIX T08 MODERATE; D21 MODERATE; 01B WEAK |
| 13 | [C056](cards/C056.md) Search that learns executable query rewrites for codebases | CONDITIONAL | 0.48 (0.28-0.65) | 0.57 | 0.35 | 0.71 | 14→192 | T20 MODERATE; T04 WEAK |
| 14 | [C087](cards/C087.md) Prior-support diagnostics that unlock genuinely new RL behavior | CONDITIONAL | 0.47 (0.26-0.64) | 0.57 | 0.29 | 0.72 | 14→352 | catalog T06 MODERATE; v3 02A MODERATE |
| 15 | [C096](cards/C096.md) Discover an image representation that retains violated constraints | CONDITIONAL | 0.47 (0.25-0.65) | 0.57 | 0.28 | 0.72 | 16→336 | catalog T11 MODERATE; FIX T11 MODERATE; catalog T21 WEAK |
| 16 | [C044](cards/C044.md) Choose pretraining architectures using downstream editability | CONDITIONAL | 0.48 (0.26-0.67) | 0.57 | 0.37 | 0.72 | 16→480 | T03 MODERATE; FIX-T09 WEAK; D23 WEAK |
| 17 | [C053](cards/C053.md) Search for absent evidence without inventing a negative result | CONDITIONAL | 0.50 (0.31-0.65) | 0.58 | 0.40 | 0.72 | 5→48 | T14 MODERATE; T15 MODERATE |
| 18 | [C080](cards/C080.md) Recover address-generation speed without changing integer semantics | CONDITIONAL | 0.48 (0.28-0.65) | 0.58 | 0.32 | 0.73 | 8→20 | v3 05B MODERATE |
| 19 | [C042](cards/C042.md) Pretrain conditional computation with delayed expert utility | CONDITIONAL | 0.49 (0.27-0.67) | 0.58 | 0.41 | 0.73 | 18→432 | 04A WEAK; FIX-T08 MODERATE |
| 20 | [C119](cards/C119.md) Train the agent to detect its own research dead ends | CONDITIONAL | 0.48 (0.29-0.69) | 0.58 | 0.44 | 0.74 | 20→304 | T03 MODERATE; 02B MODERATE |
| 21 | [C020](cards/C020.md) Train a memory admission predictor for inference state | CONDITIONAL | 0.48 (0.26-0.67) | 0.59 | 0.44 | 0.74 | 10→68 | v3-06A WEAK; v3-05A MODERATE |
| 22 | [C012](cards/C012.md) Recover learnability after curriculum-induced gradient starvation | CONDITIONAL | 0.49 (0.27-0.68) | 0.59 | 0.43 | 0.74 | 16→252 | FIX-T11 MODERATE |
| 23 | [C084](cards/C084.md) Approximate speculation with a real downstream regret contract | CONDITIONAL | 0.49 (0.28-0.67) | 0.59 | 0.36 | 0.74 | 8→48 | catalog T21 WEAK; v3 05A MODERATE |
| 24 | [C095](cards/C095.md) Find an optimizer coordinate system beyond standard recipe sweeps | CONDITIONAL | 0.49 (0.28-0.66) | 0.59 | 0.34 | 0.74 | 18→624 | catalog T09 WEAK; catalog T02 MODERATE |
| 25 | [C122](cards/C122.md) Self-training a research critic without rewarding persuasive prose | CONDITIONAL | 0.50 (0.29-0.71) | 0.59 | 0.46 | 0.74 | 18→256 | 07B MODERATE; T03 MODERATE; D24 WEAK |
| 26 | [C037](cards/C037.md) Co-schedule draft training and target inference | CONDITIONAL | 0.51 (0.30-0.68) | 0.59 | 0.46 | 0.74 | 12→60 | 03B WEAK; 05A MODERATE |

### What keeps each survivor below the lines, and what CONDITIONAL cards need
These are one-line readings of section 7 of each card.

1. **C086, research world models graded only by executed improvements.** Every disambiguating observation needs a real training run, and the strongest stack (proposal learning in the style of LM²LM, an ensemble of outcome predictors, trust-region search) still shares blind spots on new interactions.
2. **C045, pretraining with stateful external memory under update churn.** Forced private replacement waves mean a controller can anticipate vulnerable entries but cannot veto harmful evictions. A single winning consolidation and refresh rule would overturn this.
3. **C116, a tool-building curriculum for unfamiliar accelerator DSLs.** Unseen DSL semantics can't be replaced by public KernelBench tasks. The semantic holdout and the physical speedup ceiling are unbuilt.
4. **C099, rechecking a curriculum proxy when the learner changes.** PLR plus ALP-GMM removes stale rankings, but it can't tell which contrast the representation shift has made informative.
5. **C081, masked-input regularization after repetitions stop being exchangeable.** The 2026 data-constrained regularization recipe plus RegMix-style tuning handles exact duplicates. Surface frequency doesn't show which repeats carry new conditional relations.
6. **C024, CONDITIONAL.** Needs a binding cap on all storage, reversals that are inferable from history, and a reference that doesn't rely on hindsight. With a free archive it saturates as ordinary retrieval.
7. **C106, CONDITIONAL.** Needs identifiable shared-alias tasks, paid sensing and a matched direct-controller comparison.
8. **C112, CONDITIONAL.** Needs identifiable observation aliases and full raw-observation and decision-focused controls.
9. **C064, CONDITIONAL.** Needs rare-expert compositional mixtures, a published packing-invariant objective and a tuned loss-free capacity control.
10. **C010, CONDITIONAL.** Needs a generator with byte pressure and sufficient causal evidence. Delay alone saturates.
11. **C103, CONDITIONAL.** Needs a relational counterfactual and relearning design, plus a cost audit of clean replay and retraining.
12. **C127, CONDITIONAL.** Needs demonstrated conditional causal interference, matched bridge and replay controls, and a joint-retraining comparison.
13. **C056, CONDITIONAL.** Needs a charged tracing interface, holdouts by dispatch mechanism and a causal finding-shuffle ablation.
14. **C087, CONDITIONAL.** Needs discovery defined by transfer, support uncertainty and a matched ablation of diagnostic against curriculum.
15. **C096, CONDITIONAL.** Needs a numerical byte budget, a sparse-symbol-codec baseline and evidence that selective retention is attainable.
16. **C044, CONDITIONAL.** Needs matched isolated probes with consequential reversals in sequential ranking. Edit-aware Bayesian optimization remains a threat.
17. **C053, CONDITIONAL.** Needs a probe-identifiability contract, aggregation by proper score, and a same-budget reference that can't anticipate the answer.
18. **C080, CONDITIONAL.** Needs a wrapping and shape generator balanced by mechanism, plus fully charged guarded specialization.
19. **C042, CONDITIONAL.** Needs a generator of interactions with matched marginals, and precursor-retention capacity shown to bind.
20. **C119, CONDITIONAL.** Needs randomized continuation support, plateaus that depend identifiably on the intervention, and a full restart-portfolio control.

Ranks 21–26 are C020, C012, C084, C095, C122 and C037. Each has an ESTIMATED best-of-4 of 0.59, so its margin is only 0.01. They are the weakest CONDITIONALs. C122's single-run range reaches 0.71.

## Main kill reasons (99 CUT)

The binding lines on the 97 cards that were CUT as written: best-of-4 above 0.60 on 58, a single run above 0.70 on 28, and a STRONG duplicate on 11. The two reconciled cards (C002, C008) bring the total to 99.

I grouped the reasons myself, editorially; the codes are in the `kill_category` column of `screen.tsv`.

| Category | n | Gist |
|---|---|---|
| SYS | 29 | A mature serving, kernel or compiler stack already covers the intervention: prefix caching, speculation, grammar engines, multi-LoRA serving, batch-invariant kernels, overlap and placement search. |
| EXP | 18 | Standard experimental design, search or decision theory optimizes the grader directly: blocked factorials, adaptive replication, BO/TuRBO, independent confirmation, Bayes decisions. |
| DATA | 14 | Standard curation, curriculum and acquisition recipes recover the reward: tuple-preserving dedupe, PLR-style replay, mixture optimization, diverse acquisition. |
| TRAIN | 14 | Known training, RL or repair-loss stacks close the gap: router precision, DPO/SFT mixture search, conservative or offline RL, selective repair losses. |
| MEM | 11 | Standard retrieval, memory, versioning and provenance stacks: version graphs, condition-scoped memory, event logs. |
| DUP | 11 | STRONG duplicate of an existing task (see below). |
| RECON | 2 | The card's own estimates cross a line (C002, C008). |

This is the same pattern that sank the 10 FIX tasks: a lawful stack of standard recipes plus a sweep, not an exploit. On average the screen raised the authors' attack estimates by ESTIMATED +0.185 (118 raised, 6 lowered, 1 unchanged).

## Duplicates
There were 11 STRONG matches, all CUT:
- **v3 05B:** C018, C073, C090 (also STRONG with 05A), C097.
- **v3 05A:** C100.
- **v3 02A:** C101.
- **Catalog T03:** C028, C050, C055.
- **Catalog T21:** C093, C104.

No card matches a FIX packet or a D card at STRONG. No survivor has a STRONG match.

Among survivors, the MODERATE overlaps with D cards are C099 (D26), C010 (D03) and C127 (D21). Others overlap the catalog or v3 at MODERATE, for example C086 and C116 with T03, C081 with T02/FIX-T02, C096 with T11/FIX-T11 and C012 with FIX-T11. These should be checked before any survivor is promoted.

## Decisive-check GPU-h re-estimate (all ESTIMATED H100-hours)

| Set | Old total | New total |
|---|---|---|
| All 125 | 1,458 | 27,584 |
| 26 survivors | 395 | 7,992 |
| 5 PASS-SCREEN | 84 | 2,632 |

- The median per card went from 12 to 180, with an interquartile range of 64–320 and extremes of 10 to 1,200.
- The old values took 13 distinct numbers; the new ones take 58.
- New distribution: 0–25: 14, 25–50: 12, 50–100: 14, 100–200: 28, 200–400: 36, 400–800: 20, 800+: 1 (C086).
- The main reason for the rise is that the old pilots priced one illustrative run. A decisive check needs several arms × seeds × full training or campaign trajectories on 0.3B–4B subjects. Each card shows its arithmetic in section 5.

## Caveats
Read the calibration section of VALIDATION.md before relying on the ranking. Best-of-4 is close to a fixed offset from the single-run estimate, and the survivors' upper 95% bounds sit just under 0.75. These are forecasts. A real CPU dry run and a pilot would be needed before any survivor counts as more than a desk hypothesis.
