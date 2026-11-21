# C109 — Fix calibration, then optimize a scheduler whose decisions change calibration — screen audit
## 1. What the screen claimed
The screen forecast a censoring-aware runtime model, randomized completions and BOHB/ASHA allocation would suffice, producing CUT in category EXP. Its ESTIMATED single/bo4/pass@4/ub95 were 0.66/0.75/0.86/0.90, with counterfactual unfinished-job utility acknowledged but largely discounted. Listed sources were https://proceedings.mlr.press/v80/falkner18a.html and https://arxiv.org/abs/1810.05934.
## 2. Evidence audit
BOHB: Robust and Efficient Hyperparameter Optimization at Scale — Stefan Falkner, 2018 — first URL — fetched, supports efficient candidate selection using multi-fidelity feedback. A System for Massively Parallel Hyperparameter Tuning — Liam Li, 2018, revised 2020 — second URL — fetched, establishes asynchronous continuation rather than inference under informative censoring. Neither source demonstrates a runtime predictor whose selection policy changes both observed durations and delivered learning value.

Grade PARTIAL. Resource allocation is well-established; correct survival likelihoods, overlap-aware bias correction and useful exploration under live interference are additional load-bearing work. Merely logging selection probabilities cannot recover unobserved utility without overlap or appropriate causal assumptions. The screen's sufficient-stack conclusion therefore exceeded its evidence.
## 3. Research done now
- Pollux: Co-adaptive Cluster Scheduling for Goodput-Optimized Deep Learning — Aurick Qiao, 2020, revised 2021 — https://arxiv.org/abs/2008.12260 — fetched — joins statistical efficiency and allocation, raising the mature scheduling floor beyond throughput-only controls.
- Sia: Heterogeneity-aware, Goodput-optimized ML-cluster Scheduling — CMU Parallel Data Laboratory, 2023 — https://www.pdl.cmu.edu/PDL-FTP/BigLearning/sia_sosp23-final_abs.shtml — fetched — heterogeneous resource adaptation is a real comparator; it does not settle policy-induced calibration.
- Overtuning in Hyperparameter Optimization — Lennart Schneider, 2025 — https://proceedings.mlr.press/v293/schneider25a.html — fetched — repeated validation search can select worse-generalizing configurations, weakening the claim that scheduler sweeps safely resolve the problem.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern/OpenAI, 2024 — https://arxiv.org/html/2410.07095v1 — fetched — demonstrates experimental automation and substantial resource-planning failures, reducing confidence in an integrated endogenous scheduler.
- Evaluating frontier AI R&D capabilities of language model agents against human experts — METR, 2024 — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/ — fetched — agents achieve useful short-horizon optimization but lose relative ground over longer research sequences.

Search included recent scheduling, goodput, learning-curve censoring and HPO failure modes. Newer papers with unrelated static prediction objectives were not used to certify this causal capability.
## 4. Re-estimated attack
The strongest literature-informed route combines a Pollux/Sia-style resource model, explicit censored-duration fitting, randomized finishing and asynchronous multi-fidelity promotion. ESTIMATED central reward credits are 0.23 for useful allocation, 0.18 for removing naive censoring bias, and 0.16 for exploration/continuation tuning, totaling 0.57. These are hypotheses about incremental normalized utility after the frozen competent floor; the floor and ceiling have not been measured. No calibration points are awarded independently of model improvement.

ESTIMATED run scenarios: 0.35 with mass 0.20 when exploration wastes expensive jobs; 0.57 with mass 0.60 for stable but incomplete correction; 0.77 with mass 0.20 when probe information predicts subsequent utility. Mean=0.35×0.20+0.57×0.60+0.77×0.20=0.57, range 0.35–0.77. Expected max4=0.77−0.20×0.80^4−0.22×0.20^4=0.69. With p=0.20, pass@4=1−0.80^4=0.59; q95=0.77. Queue composition and discovery of the right intervention dominate spread; learner variability matters after allocation. This is less confident than the old mean yet still CUT under implementation-success assumptions.
## 4A. Demonstrated capability and subfield SOTA
Pollux reports substantial job-completion improvements while modeling useful learning progress; Sia extends goodput optimization to heterogeneous resources. They are the strongest directly relevant established system families verified here. No fetched source establishes a field-wide best policy for the card's joint informative-censoring/learning-utility objective. The north star must be a same-resource controller beating these systems plus corrected ASHA on live queues. R≈1 and the reference target cannot be fixed from published completion-time gains alone.

Two agent results delimit transfer. MLE-bench's o1-preview/AIDE reaches bronze or better on 16.9% of competitions with 24 hours and one A10. Agents often neglect resource limits; this directly weakens confidence in costly exploration/completion decisions, although it is older evidence. RE-Bench tests o1-preview and Claude 3.5 Sonnet in METR's agent harness: agents outperform average experts at two-hour budgets, while humans approach twice their performance at 32 hours. Hardware differs by task and no live censored-scheduler trajectory is reported there. Short optimization success does not demonstrate selection-bias identification.

KNOWN-RECIPE applies to goodput scheduling and multi-fidelity allocation. AGENT-DEMONSTRATED is absent for identifying censoring mechanisms, fitting runtime/utility jointly and validating changed exposure within twelve hours. attack_basis=LITERATURE-ONLY. The inference is narrower than a claim that agents cannot schedule jobs: the missing capability is the coupled statistical experiment.

ANCHORED ESTIMATED central credits are 0.21 allocation, 0.15 defensible runtime correction and 0.11 verified exploration, yielding 0.47. Use scores 0.28/0.47/0.67 at probabilities 0.28/0.63/0.09. Mean=0.43, range 0.28–0.67; bo4=0.67−0.20×0.91^4−0.19×0.28^4=0.53; pass@4=1−0.91^4=0.31; q95=0.67. The reduced high-outcome mass reflects unverified causal integration; it is an explicit assumption, not a frequency inferred from either benchmark. Four attempts are independent conditional on one task block; correlated instance difficulty needs separate measurement.
## 5. Verdict under the kill lines
Section 4's evidence re-estimate is CUT, binding bo4 by approximately 0.09. The ANCHORED verdict is PASS-SCREEN, FLIPPED CUT→PASS-SCREEN: single is 0.27 below its limit, bo4 0.07 below, pass@4 0.19 below and q95 0.08 below. Pollux/Sia establish a serious floor, but the old CUT depended on autonomous integration that neither its sources nor the fetched agent benchmarks demonstrate. The headline remains a desk forecast resting on assumption, not S2 certification or proof of an attainable normalized ceiling.
## 6. Redesign
NOT-NEEDED: the anchored attack clears all four forecast lines with the requested margin, so this audit does not impose an unvalidated harder scheduler. Class na. Before building, freeze actual pool capacity, intervention observability, censoring semantics and delivered-learning accounting from the original contract; those are implementation specifications, not new difficulty knobs. If randomized completions plus a standard goodput scheduler achieve the reference, refreeze or cut instead of making duration information inaccessible. No redesigned score or GPU allocation is claimed.
## 7. Measurement status
Rollouts UNMEASURED (planned: independent complete scheduler-development runs on fresh live queues). Grader noise UNMEASURED (planned: fixed-policy queue repeats with paired contention and learner seeds). Score ladder UNMEASURED (planned: static allocation, ASHA, Pollux/Sia-style goodput, censored forecasting, joint exploration and a feasible stronger controller; record native learning gain before normalization).
## Audit record
id: C109
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.66
old_bo4: 0.75
old_pass4: 0.86
old_ub95: 0.90
new_single: 0.57
new_single_range: 0.35-0.77
new_bo4: 0.69
new_pass4: 0.59
new_ub95: 0.77
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: na
redesign_status: NOT-NEEDED
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: MLE-bench, o1-preview AIDE, 2024; RE-Bench, o1-preview and Sonnet 3.5, 2024
gap_to_attack: endogenously censored runtime and utility inference
subfield_sota_ref: Pollux, Qiao, 2020/2021; Sia, CMU PDL, 2023
anchored_single: 0.43
anchored_bo4: 0.53
anchored_pass4: 0.31
anchored_ub95: 0.67
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CUT->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
