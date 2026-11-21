# C122 — Self-training a research critic without rewarding persuasive prose — screen audit
## 1. What the screen claimed
The attack trained an execution-outcome ranker over code and project state, removed style cues, and actively executed uncertain proposals. The screen's ESTIMATED single 0.50, bo4 0.59, pass4 0.46 and ub95 0.74 led to CONDITIONAL, category none: unfamiliar useful mechanisms and costly labels remained unresolved. Sources: https://arxiv.org/abs/1311.4319, https://arxiv.org/abs/2207.01780 and https://arxiv.org/abs/1910.06403.

## 2. Evidence audit
Ranking Algorithms by Performance — Lars Kotthoff, 2013 — fetched at the first address, supports ranking an existing algorithm portfolio rather than judging new scientific mechanisms. CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning — Hung Le, 2022 — fetched at the second, trains a functional-correctness critic; passing code tests differs from predicting model-learning gains. BoTorch: A Framework for Efficient Monte-Carlo Bayesian Optimization — Maximilian Balandat, 2019 preprint/2020 publication — fetched at the third, makes acquisition practical without establishing a transferable research representation.

Grade: PARTIAL. Outcome supervision and exploration are supported components. The consequential missing evidence is that their trained representation recognizes unfamiliar beneficial interventions after the project and proposer both change; style randomization does not establish that capability.

## 3. Research done now
- Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents — Xing Zhang, 2026 — https://arxiv.org/html/2607.12790v1 — fetched — strengthens the possibility of useful internal selection feedback, but its small anchored detector compositions and frozen model differ from learned critic weights for ML research.
- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment — Art Kanke, 2026 — https://arxiv.org/html/2610.40488v1 — fetched — proposal rankings did not demonstrably improve on selecting the first-written idea; this directly lowers confidence in a critic's marginal scientific utility.
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search — Yutaro Yamada, 2025 — https://arxiv.org/html/2504.08066v1 — fetched — shows that a critique-guided experimental tree can yield research output, raising the critic-free/search alternative without isolating critic learning as its cause.

Search examined outcome-trained research critics and current proposal-ranking evaluations; none verified this complete self-training treatment under the stated horizon.

## 4. Re-estimated attack
The following scores, probabilities and decompositions are ESTIMATED. Beyond a competent execution-trained ranker, allow 0.14 for code/state inputs that remove misleading presentation, 0.19 for uncertainty-directed outcome acquisition, and 0.12 for selection-trajectory distillation. Total expected contribution is 0.45; labels bought for this gain compete with directly executing proposals. The residual is asymmetric: a conservative critic may repeatedly exclude the novel positive examples required to improve it.

Model R={0.27,0.48,0.70}, probabilities {0.28,0.57,0.15}. These are selection-bias failure, useful local ranking and transferable active critique. Single=0.28×0.27+0.57×0.48+0.15×0.70=0.45, range 0.27–0.70. Bo4=0.70−0.22×0.85^4−0.21×0.28^4=0.58. Pass4=1−0.85^4=0.48 because p=0.15; ub95=0.70. Corpus support and discovery of a useful project probe dominate run variation; training randomness can amplify either outcome. Unlike the screen's near-fixed increment, the 0.13 best-of-four gap reflects a distinct transferable-critic outcome.

## 4A. Demonstrated capability and subfield SOTA
Closest current selection SOTA located: Double Ratchet reports retaining 88–110% of oracle-driven held-out skill improvement across its three tasks. This is a useful paired-control target, not evidence for an equivalent fraction of scientific discovery utility. Anchor C122 to realized gains from the same proposal pool under a competent outcome ranker and an affordable stronger selector. Their private project utilities and R≈1 endpoint remain UNMEASURED; arbitrary preference agreement cannot define the reference.

Demonstrated agents: Opus 4.7 in Double Ratchet runs a hundred skill rounds with interleaved metric evolution; time and hardware are unreported. It supports internal feedback transfer but not training a research critic unaided. In rTaste, GPT-6 Astra, Opus 5.5 and other models use single-researcher/team scaffolds; separate executors get forty-five minutes and one A100, with some H200 runs. Rankings show limited added value, while proposing wall time is unspecified. Neither is a twelve-hour learned-critic demonstration.

KNOWN-RECIPE: outcome ranking plus active labels. AGENT-DEMONSTRATED: critique and proposal execution, with no verified autonomous learned scientific-utility critic. attack_basis=LITERATURE-ONLY. The attacker still needs to obtain unbiased counterexamples, separate causal utility from style and transfer across interventions without spending away the gain.

ANCHORED expected components are 0.13 for representation repair, 0.16 for useful labels and 0.09 for transferable selection. Distribution R={0.21,0.41,0.65}, masses {0.29,0.61,0.10}, gives single=0.38, range 0.21–0.65; bo4=0.65−0.24×0.90^4−0.20×0.29^4=0.49; pass4=1−0.90^4=0.34; ub95=0.65. The reduction reflects direct negative ranking evidence, not an assumption that executing research is generally beyond agents. Forecast weights are not empirical rates; native anchor uncertainty means this verdict rests on assumption.

## 5. Verdict under the kill lines
Section 4 remains CONDITIONAL: ESTIMATED pass4 is only 0.02 below its threshold. ANCHORED verdict PASS-SCREEN, FLIPPED CONDITIONAL→PASS-SCREEN. Margins are ESTIMATED 0.32 single, 0.11 bo4, 0.16 pass4 and 0.10 upper percentile, all beyond the requested screening margin. rTaste's weak ranking advantage, together with the gap between CodeRL correctness and scientific utility, drives the change. This desk result is not release certification or a measured stronger-model projection.

## 6. Redesign
NOT-NEEDED. The original outcome-only reward and fresh intervention mechanisms retain plausible reserve against the demonstrated selection capability; preserve them and measure the critic-free execution portfolio before building a larger packet. No requirement should reward elaborate critique language or force the researcher to retain an unhelpful critic. A cheap portfolio matching the stronger selector would falsify the forecast rather than justify restricting that legal route.

## 7. Measurement status
Rollouts UNMEASURED (planned independent critic-training attempts with executed selected and random rejected proposals). Grader noise UNMEASURED (planned repeated proposal-agent resets and subject training seeds under one fixed critic). Score ladder UNMEASURED (planned code-only ranker, active critic, direct execution portfolio, reference and feasible stronger selection policy).

## Audit record
id: C122
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.50
old_bo4: 0.59
old_pass4: 0.46
old_ub95: 0.74
new_single: 0.45
new_single_range: 0.27-0.70
new_bo4: 0.58
new_pass4: 0.48
new_ub95: 0.70
new_verdict: CONDITIONAL
binding_line: pass4>0.50
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
demonstrated_ref: Double Ratchet Opus 4.7 2026; rTaste Astra Opus 5.5 and others 2026
gap_to_attack: trained critic transferring scientific utility beyond its outcome corpus
subfield_sota_ref: Double Ratchet oracle-relative skill lift Zhang 2026
anchored_single: 0.38
anchored_bo4: 0.49
anchored_pass4: 0.34
anchored_ub95: 0.65
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CONDITIONAL->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
