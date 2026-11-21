# C006 — Train set-valued scientific predictions — screen audit
## 1. What the screen claimed
The screen fitted correlated outcome predictions, computed score-optimal winner sets, calibrated by pool and distilled the decisions into submitted weights. Its ESTIMATED single/bo4/pass@4/ub95 were 0.76/0.83/0.96/0.95; CUT, category EXP, reflected calibrated Bayes decisions targeting the stated reward. The sole cited URL was https://arxiv.org/abs/2006.02544.

## 2. Evidence audit
Classification with Valid and Adaptive Coverage — Yaniv Romano, 2020 — https://arxiv.org/abs/2006.02544 — fetched — demonstrates adaptive categorical prediction sets with marginal coverage. It supports useful uncertainty wrappers, but does not establish a joint distribution over tied scientific winners, downstream decision value, weights-only distillation or validity across recipe mechanisms.

Grade: PARTIAL. Calibration is evidenced; correlated winner inference is extrapolated. Moreover, the card never specifies its “proper set score,” so the supposedly exact Bayes action is not yet defined. The screen correctly observes that active diagnosis is absent from the actual grader; it cannot nevertheless claim that predicting profitable sets is already solved on this distribution.

## 3. Research done now
- Conformal Risk Control — Anastasios N. Angelopoulos, 2022, revised 2025 — https://arxiv.org/abs/2208.02814 — fetched — Extends calibration to monotone expected losses. This strengthens risk-aware inclusion rules, while an inclusion/exclusion utility need not satisfy its monotonicity requirement.
- Towards Human-AI Complementarity with Prediction Sets — Giovanni De Toni, 2024 — https://proceedings.neurips.cc/paper_files/paper/2024/file/37d4d4413b7c7558cc27a6d3d42ea998-Paper-Conference.pdf — fetched — Shows ordinary conformal sets can be suboptimal for subsequent decisions and supplies stronger greedy alternatives. It weakens the wrapper-only claim and strengthens decision-aware search; human choice differs from recipe continuation.
- CAP: A General Algorithm for Online Selective Conformal Prediction with FCR Control — Yajie Bao, 2025 — https://jmlr.org/beta/papers/v26/24-0452.html — fetched — Demonstrates calibration adjusted to selection. It supports accounting for recipe-pool selection rather than treating row-level coverage as sufficient.
- Valid Selection among Conformal Sets — Mahmoud Hegazy, 2025 — https://arxiv.org/abs/2506.20173 — fetched — Explains how choosing attractive sets can invalidate coverage and proposes stability corrections. This lowers confidence in an unrestricted threshold sweep whose winner is evaluated on its calibration data.

Searches addressed current set-selection and risk-control methods, including negative evidence about downstream utility. None supplies a leaderboard for this scientific winner-set objective.

## 4. Re-estimated attack
All card-score quantities here are ESTIMATED. Give correlated outcome modeling 0.34, decision-aware set construction another 0.20, and honest pool-level calibration plus distillation 0.10: total approximately 0.64. Residual uncertainty includes the tie estimand and unseen-mechanism covariance. These incremental credits describe a hypothetical competent implementation, not a demonstrated agent.

A relatively mature recipe, once integrated, has narrow ESTIMATED states {0.55,0.64,0.73}, masses {0.15,0.75,0.10}. Differences reflect predictor quality and whether validation handles selection, rather than a single novel insight. Single=0.15×0.55+0.75×0.64+0.10×0.73=0.64, range 0.55–0.73. Bo4=0.73−0.09×0.90^4−0.09×0.15^4=0.67. With p=0.85, pass@4=1−0.15^4=1.00 after rounding; ub95=0.73 because CDF at 0.64 is 0.90. This conditional recipe distribution has a small selection gap. It reduces the old point because coverage guarantees are weaker than decision optimality, but still predicts a kill if integration succeeds routinely.

## 4A. Demonstrated capability and subfield SOTA
SOTA anchor: Romano's adaptive sets, Angelopoulos's risk control and De Toni's decision-aware greedy construction are strong demonstrated systems for different estimands. No opened result defines the unspecified scientific set score, so none anchors R≈1 numerically. Use their strongest applicable combination as a measured floor; a feasible superior predictor must improve actual continuation utility, not merely produce smaller sets.

- PostTrainBench v1.2: More reliable scores and verdicts — PostTrainBench team, 2026 — https://posttrainbench.com/blog/posttrainbench-1-2/ — fetched; setup at https://posttrainbench.com/ — fetched. Opus 5.5/Claude Code has reported weighted performance 43.8% under ten hours on one H100. This demonstrates small-model post-training, not joint scientific-winner calibration; that percentage is not C006 reward.
- PaperBench Science — Elvis Zhang Research/Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched. Astra's author-launcher configuration reports 59.08% partial but 13.98% full reproduction, with four-to-twenty-four-hour limits; device allocation is unspecified. Its evidence-validation gap is relevant to verifying calibrated winner sets, without measuring that skill directly.

Basis LITERATURE-ONLY. KNOWN-RECIPE statistical decisions exist; AGENT-DEMONSTRATED pool-covariance learning and distilled set boundaries do not. Twelve hours must cover outcome-label checks, estimand implementation, calibration and weights-only transfer.

ANCHORED distribution ESTIMATED: {0.33,0.51,0.68}, probabilities {0.33,0.56,0.11}, for integration errors, useful calibrated prediction and successful complete transfer. Single=0.33×0.33+0.56×0.51+0.11×0.68=0.47, range 0.33–0.68; bo4=0.68−0.17×0.89^4−0.18×0.33^4=0.57; pass@4=1−0.89^4=0.37; ub95=0.68. Research restarts are assumed independent within pools. Unknown native anchors and integration probabilities make this assumption-dependent.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT on ESTIMATED bo4 0.67 and near-certain repeated success conditional on a working recipe. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL. Its binding bo4 is ESTIMATED 0.03 below the line; single, pass@4 and ub95 margins are respectively 0.23, 0.13 and 0.07. The unimplemented scoring rule and absent agent-level validation drive the change, rather than a claim that uncertainty wrappers are weak.

## 6. Redesign
Cause (b): a score-aware statistical decision can optimize a static grader. Concrete condition: specify winner membership from continuation expected utility with a disclosed practical-equivalence tolerance, output membership probabilities scored by Brier loss, and define the set as a disclosed cost-optimal action. Do not call a bare hard-set penalty strictly proper. Make actual selected-recipe utility the primary scientific outcome, with calibration and inclusion costs precommitted.

To justify scientific discrimination, allow a charged diagnostic continuation before final probabilities and recipe choice. Cross observable mechanism types where the same apparent tie is resolved by different available diagnostics. All diagnostic options, costs and legal evidence are supplied. This expands the artifact to a predictor/diagnostic policy whose utility is measured on real small-model continuations; a passive wrapper remains a required control.

The strongest re-attack is a joint predictor plus conformal calibration, expected-information-gain selection and decision-rule distillation. Its basis remains LITERATURE-ONLY. It misses reward if a useful diagnostic must separate mechanism hypotheses rather than merely shrink marginal intervals. Risks include routine Bayesian experimental design solving the menu, or diagnostics revealing no learnable distinction. Require an equal-cost attainable reference before promotion.

ESTIMATED revised scores {0.24,0.43,0.62}, masses {0.40,0.52,0.08}: single=0.40×0.24+0.52×0.43+0.08×0.62=0.37; bo4=0.62−0.19×0.92^4−0.19×0.40^4=0.48; pass@4=1−0.92^4=0.28; ub95=0.62. REDESIGNABLE. Pilot GPU-h ESTIMATED: four 1B predictor arms×three seeds×four H100-hours=48; four 1B recipe families×three seeds×eight H100-hours including diagnostics=96; evaluation eighteen H100-hours; total 48+96+18=162.

## 7. Measurement status
Rollouts UNMEASURED (planned weights-only static attacks followed by the diagnostic-policy comparison). Grader noise UNMEASURED (planned repeated continuation labels with pool-clustered uncertainty). Score ladder UNMEASURED (planned singleton, all-recipes, adaptive sets, joint calibrated decisions and diagnostic reference in native utility).

## Audit record
id: C006
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 1
sources_new_count: 7
sources_fetched_count: 8
old_single: 0.76
old_bo4: 0.83
old_pass4: 0.96
old_ub95: 0.95
new_single: 0.64
new_single_range: 0.55-0.73
new_bo4: 0.67
new_pass4: 1.00
new_ub95: 0.73
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Define probabilistic winner membership precisely and score a costed diagnostic policy through actual continuation utility.
redesign_single: 0.37
redesign_bo4: 0.48
redesign_pass4: 0.28
redesign_ub95: 0.62
redesign_gpuh: 162
attack_basis: LITERATURE-ONLY
demonstrated_ref: PostTrainBench v1.2, Opus 5.5 Claude Code, 2026; PaperBench Science, GPT-6 Astra author launcher, 2026
gap_to_attack: Learn and distill correlated scientific winner sets with verified decision calibration
subfield_sota_ref: Adaptive sets Romano 2020; risk control Angelopoulos 2025 revision; decision-aware greedy sets De Toni 2024
anchored_single: 0.47
anchored_bo4: 0.57
anchored_pass4: 0.37
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
