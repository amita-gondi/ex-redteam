# C125 — An agent that learns to make its uncertainty actionable — screen audit
## 1. What the screen claimed
Fixed beliefs and measurement choices supposedly permit direct cost-aware knowledge-gradient planning, robust joint-model sensitivity and short lookahead. The screen assigned ESTIMATED single 0.90, bo4 0.95, pass4 0.99 and ub95 0.99; CUT, category EXP, because decision value directly addresses uncertainty that can change the selected recipe. Sources were https://optimallearning.princeton.edu/Papers/FrazierPowellDayanik_KnowledgeGradientSICON.pdf and https://archive.botorch.org/tutorials/one_shot_kg.

## 2. Evidence audit
A Knowledge-Gradient Policy for Sequential Information Collection — Peter I. Frazier, 2008 — fetched at the PDF address, studies sequential ranking and selection under explicit distributional assumptions. It is strong evidence for the objective, but not evidence that the card exposes a correct joint generative model or tractable posterior update. One-shot Knowledge Gradient — BoTorch developers, 2026 retrieved archived tutorial, publication year unspecified — fetched at the tutorial URL, provides an implementation using a fitted surrogate, rather than a guarantee for arbitrary fixed uncertainty intervals.

Grade: PARTIAL. The screen correctly rejects entropy-only acquisition as the strongest attack. However, a menu of measurements plus calibrated marginal predictions does not necessarily specify the joint responses needed by its planner; both this interface assumption and autonomous validation of the resulting decisions were unsupported.

## 3. Research done now
- Session report: 0.9979 → 0.9697 in 126 experiments — autoresearch agent posting for Andrej Karpathy, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — supports sustained short-loop training experimentation, raising the ability to tune action thresholds, although it does not optimize fixed-belief information value.
- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment — Kanke (University of Minnesota), 2026 — https://arxiv.org/html/2610.40488v1 — fetched — weak evidence of improved proposal ordering cautions against assuming that reported uncertainty already produces good experiment choices.
- Amortizing Sequential Experimental Design in Reasoning LLMs — Anita Kriz, 2026 — https://arxiv.org/html/2610.20832v1 — fetched — demonstrates learned acquisition under a separately specified generative model, and examines misspecified priors and nonmyopic rewards. It raises feasibility of decision policies while highlighting assumptions missing from the old attack.

Research queries targeted current cost-aware multistep design and agent experiment allocation. No located study established this complete fixed-belief ML-utility mapping autonomously in twelve hours.

## 4. Re-estimated attack
All score forecasts, proposed masses and compute envelopes here are ESTIMATED. With a usable joint update interface, terminal-utility sensitivity plausibly captures 0.35, cost-aware stopping 0.26 and multistep complementary checks 0.15: total 0.76. The fixed forecast score cannot create an unconditional learning gain shared by every policy. These increments therefore concern the action-dependent normalized utility, conditional on scientifically defensible aggregation weights.

Model R={0.62,0.79,0.88}, masses {0.25,0.60,0.15}, covering approximate acquisition, effective one-step decisions and helpful lookahead. Single=0.25×0.62+0.60×0.79+0.15×0.88=0.76, range 0.62–0.88. Bo4=0.88−0.09×0.85^4−0.17×0.25^4=0.83. In this deliberately optimistic recipe scenario p=1.00, pass4=1−0.00^4=1.00; ub95=0.88. This is not observed certainty: all modes condition on the unverified generative-model access. Numerical integration choices and finding useful lookahead generate the spread. The old score was still too high even on that favorable premise.

## 4A. Demonstrated capability and subfield SOTA
Current subfield comparator: Kriz's amortized BED policies outperform the paper's inference/training-time baselines on information acquisition and transfer to Medi-Q. This does not settle utility-aware ML experimental-design SOTA; the exact comparable leaderboard is unverified. Knowledge gradient is the appropriate known-recipe floor if its joint model exists. R≈1 must correspond to an executed stronger allocation under the identical beliefs, measurement costs and terminal training budget; no native value for it has been measured.

Two agent anchors: the Claude-based autoresearch report lists 126 trials, about 10.5 hours on one H100, and validation bits/byte improving from 0.997900 to 0.969686. Exact Claude version is unreported and the run reuses earlier findings; it demonstrates search execution rather than unaided acquisition-policy design. rTaste's frontier researchers use solo/team scaffolds with separate forty-five-minute A100/H200 executors; rankings have limited advantage beyond first-written ideas, and proposing time is unspecified. Its fixed proposal pool is narrower than adaptive recipe measurement.

KNOWN-RECIPE is clear for value of information; AGENT-DEMONSTRATED integration with this fixed estimator and downstream ML endpoint is absent. attack_basis=LITERATURE-ONLY. The missing twelve-hour work is recovering a usable joint model from the lawful interface, validating update semantics and proving that acquisition cost is repaid in training utility.

ANCHORED allowances are 0.23 for decision sensitivity, 0.19 for cost-sensitive checks and 0.09 for lookahead. Use R={0.32,0.53,0.70}, probabilities {0.23,0.59,0.18}: single=0.51, range 0.32–0.70; bo4=0.70−0.17×0.82^4−0.21×0.23^4=0.62; pass4=1−0.82^4=0.55; ub95=0.70. An interface mismatch accounts for the low mode, with successful policy integration in the upper mode. These judgments are assumptions, not benchmark-derived frequencies.

## 5. Verdict under the kill lines
Recipe analysis CUT; ANCHORED CUT, UNCHANGED. ESTIMATED bo4 exceeds by 0.02 and pass4 by 0.05. Fixed predictions remove a major research burden, so a moderate central forecast can still fail the repeated-search bar. The decision rests on assumed transfer; the old claim of virtually complete single-run success is withdrawn. If the posterior interface cannot support the proposed update, rebuild the attack estimate rather than silently supplying extra information.

## 6. Redesign
Cause (b): standard expected-utility planning can solve the fixed-belief action problem. Make the research treatment jointly learn intervention-response uncertainty and its measurement policy from real training probes. Provide the existing estimator, raw permitted histories and full operation semantics; introduce genuine optimizer/data interactions where the current surrogate is observably misspecified. Score out-of-family final learning gains, and use committed proper forecasts as a diagnostic or a precommitted nonconstant component. This expands the original intervention explicitly; it preserves a valuable frontier-lab capability rather than disguising ordinary planning.

Strongest re-attack combines a fitted causal surrogate, cost-aware knowledge gradient, short lookahead and random identifying probes. Decision planning cannot correct the wrong response model automatically, while blind entropy reduction need not improve terminal training. ESTIMATED distribution {0.20,0.44,0.66}, masses {0.25,0.65,0.10}, gives single=0.40; bo4=0.66−0.22×0.90^4−0.24×0.25^4=0.51; pass4=1−0.90^4=0.34; ub95=0.66. Basis LITERATURE-ONLY. REDESIGNABLE; a reusable surrogate might still fit every mechanism, so test full surrogate-plus-planner controls.

Pilot ESTIMATED 192 H100 GPU-h: 1B subject projects, 4 policies×2 seeds×3 mechanisms×6 hours×1 H100=144; response-model fitting and 4B agent inference=24; forecast validation and independent final continuations=24. A useful stronger control must demonstrate learnable response structure, not merely receive extra measurements.

## 7. Measurement status
Rollouts UNMEASURED (planned fixed-belief action-policy construction followed by real selected experiments). Grader noise UNMEASURED (planned repeated terminal training and immutable forecast checks). Score ladder UNMEASURED (planned favorite recipe, nearest competitor, KG, multistep planner and equal-information stronger control).

## Audit record
id: C125
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.90
old_bo4: 0.95
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.76
new_single_range: 0.62-0.88
new_bo4: 0.83
new_pass4: 1.00
new_ub95: 0.88
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Learn intervention-response uncertainty and its acquisition policy from identifiable training interactions.
redesign_single: 0.40
redesign_bo4: 0.51
redesign_pass4: 0.34
redesign_ub95: 0.66
redesign_gpuh: 192
attack_basis: LITERATURE-ONLY
demonstrated_ref: autoresearch Claude version unspecified 2026; rTaste frontier solo and team agents 2026
gap_to_attack: utility-calibrated acquisition with fixed estimator and costly joint outcomes
subfield_sota_ref: amortized sequential BED Kriz 2026; KG Frazier 2008
anchored_single: 0.51
anchored_bo4: 0.62
anchored_pass4: 0.55
anchored_ub95: 0.70
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
