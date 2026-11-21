# C008 — Grade latent visual decisions before training the policy — screen audit
## 1. What the screen claimed
The screen used a privileged-state teacher, action/role rewards, identity and actuator interventions, and on-policy correction. Its ESTIMATED single/bo4/pass@4/ub95 were 0.50/0.59/0.42/0.76. The final reconciliation and TSV override the author's CONDITIONAL with CUT, category RECON, because the upper bound crossed its line. Cited URLs:
- https://proceedings.mlr.press/v100/chen20a.html
- https://proceedings.mlr.press/v89/czarnecki19a.html

## 2. Evidence audit
Learning by Cheating — Dian Chen, 2020, fetched at the first URL — demonstrates privileged-state teaching of a vision-based driving policy, a genuinely relevant transfer mechanism. Distilling Policy Distillation — Wojciech M. Czarnecki, 2019, fetched at the second URL — demonstrates that the choice of transfer objective materially affects learning. Neither discovers the useful perception/control decomposition through causal probes or implements it only through a restricted reward harness.

Grade: PARTIAL. State-to-pixel transfer is substantially more evidenced than a generic “auxiliary heads help” claim. However, transferring a working teacher, automating its integration, and selecting useful reward gradients after crossed identity/actuation changes remain separate capabilities. The old upper envelope is not derived from any demonstrated agent distribution.

## 3. Research done now
- Eureka: Human-Level Reward Design via Coding Large Language Models — Yecheng Jason Ma, 2023/2024 — https://arxiv.org/html/2310.12931v2 — fetched — Autonomously proposes executable reward components and improves them using policy-learning feedback. This strongly raises the reward-code attack, but its accelerated state-based environments do not establish causal pixel-policy repair.
- Text2Reward: Reward Shaping with Language Models for Reinforcement Learning — Tianbao Xie, 2023/2024 — https://arxiv.org/abs/2309.11489 — fetched — Generates dense robotic rewards and demonstrates competitive policy training. Its refinement can use human feedback, so it cannot establish an entirely unaided twelve-hour solve.
- DrEureka: Language Model Guided Sim-To-Real Transfer — Yecheng Jason Ma, 2024 — https://arxiv.org/abs/2406.01967 — fetched — Automatically chooses rewards and physics randomization with real transfer demonstrations. This strengthens actuator-robust training, while changing simulation settings is not automatically legal for C008's submitted harness.
- ROSETTA: Constructing Code-Based Reward from Unconstrained Language Preference — Sanjana Srivastava, 2026 — https://www.jiajunwu.com/papers/rosetta_iclr.pdf — fetched — Grounds visual/language evidence, stages rewards and trains manipulation policies. It is recent positive evidence for decomposition; its state-augmented demonstrations and preference input are richer than this task's unlabeled interventions.

Searches targeted automated grounded reward generation rather than only policy distillation. Positive reward-agent results coexist with substantial observation and compute mismatches.

## 4. Re-estimated attack
ESTIMATED contributions are 0.20 from teacher-guided targeting, 0.16 from code-generated staged control rewards and 0.12 from on-policy/intervention corrections: total 0.48. Protected scene identifiers never enter student observations. The residual is discovering a training signal that changes perceptual decisions rather than merely fitting an auxiliary predictor.

Use ESTIMATED states {0.24,0.46,0.63,0.82} with masses {0.20,0.50,0.23,0.07}: teacher-transfer failure, ordinary targeting repair, useful causal gating and a near-complete transferable decomposition. Policy seeds and search-path discoveries produce this asymmetric spread. Single=0.20×0.24+0.50×0.46+0.23×0.63+0.07×0.82=0.48, range 0.24–0.82. Bo4=0.82−0.19×0.93^4−0.17×0.70^4−0.22×0.20^4=0.64; pass@4=1−0.70^4=0.76; ub95=0.82 because the preceding CDF is 0.93. All quantities are forecasts under independent restarts within an instance block. Compared with the screen, a similar mean has a larger repeated-search tail because automatic reward synthesis supplies a credible high-outcome path.

## 4A. Demonstrated capability and subfield SOTA
ROSETTA is the strongest recent grounded/staged reward system consulted, reporting 87% average success across its preference benchmark. Learning by Cheating establishes vision-student feasibility on driving. These cannot be ranked on one shared metric, and neither defines a ceiling for new object/action relations. Anchor the floor to teacher transfer plus competent automatic reward search; require the reference to exceed it on closed-loop completion under identical observations before fixing R≈1.

- Eureka (Ma, 2023/2024, fetched above): GPT-4-0314 with evolutionary reward reflection outperforms human rewards on a reported 83% of evaluated tasks. Each search uses an eight-A100 station for under a day, with repeated candidate training. That demonstrates autonomous reward optimization, not twelve-hour pixel/causal-transfer validation.
- ROSETTA (Srivastava, 2026, fetched above): GPT-4o grounding/staging and o1-mini coding produce the reported manipulation gains. Training takes twenty-to-ninety minutes for short tasks and eight-to-twelve hours for long tasks on a Titan RTX/RTX 2080-class device. Preference supervision and state augmentation leave an autonomy and perception gap.

The artifact family is AGENT-DEMONSTRATED in simpler settings, but the complete C008 attack basis remains LITERATURE-ONLY under the comparable-budget rule. KNOWN-RECIPE reward search is strong; the unshown work is integrating teacher transfer with causal perceptual corrections and validating composition within the remaining training window.

ANCHORED ESTIMATED distribution {0.24,0.46,0.63,0.74}, masses {0.25,0.60,0.13,0.02}, preserves conventional reward competence but reduces complete integration. Single=0.25×0.24+0.60×0.46+0.13×0.63+0.02×0.74=0.43, range 0.24–0.74; bo4=0.74−0.11×0.98^4−0.17×0.85^4−0.22×0.25^4=0.55; pass@4=1−0.85^4=0.48; ub95=0.63 since CDF there is 0.98. The extreme state lies above that percentile. Integration masses and normalized values remain assumed.

## 5. Verdict under the kill lines
Section 4's evidence forecast is CUT: ESTIMATED bo4 exceeds 0.60 by 0.04. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL using the reconciled screen. ESTIMATED pass@4 is only 0.02 below its line and bo4 has 0.05 margin. Domain-specific agents make the attack serious; their budget and information differences prevent calling the complete result demonstrated. This assumption-dependent condition requires an observable interaction regime that a full teacher/search baseline fails to teach.

## 6. Redesign
Cause (a): privileged teaching and automated reward search can solve simple perception/control failures. Require crossed object-role and actuator mechanisms where a perceptually identical mistake needs a different control correction after an observable calibration interaction. Provide those calibration observations and matched development interventions to every method. Keep simulator supervision legal during training, and assess held-out causal compositions by actual completion with attribution probes used only diagnostically.

Re-attack with teacher rewards, ROSETTA-style staging, Eureka-style feedback search and actuator randomization where allowed. Basis LITERATURE-ONLY for this combined revision. It falls short if selecting when to train identity versus control requires student-response evidence that teacher action agreement does not supply. Prove that residual against a well-tuned full teacher, rather than withholding state information. Frontier labs would value decomposition that makes visual policy learning more sample efficient; an artificial teacher handicap would not qualify.

ESTIMATED revised states {0.23,0.41,0.62}, masses {0.45,0.49,0.06}, give single=0.45×0.23+0.49×0.41+0.06×0.62=0.34; bo4=0.62−0.21×0.94^4−0.18×0.45^4=0.45; pass@4=1−0.94^4=0.22; ub95=0.62. REDESIGNABLE. Risk: automatic reward search may already discover the interaction, or the student may lack capacity. Decisive pilot GPU-h ESTIMATED: 100M vision student, five reward arms×three seeds×eight H100-hours, eighteen H100-hours for teacher training and twenty-four for causal evaluation: 5×3×8+18+24=162. Rendering CPU time must fit separately.

## 7. Measurement status
Rollouts UNMEASURED (planned full reward-harness searches with teacher and generated-reward controls). Grader noise UNMEASURED (planned repeated students and fixed-policy identity/actuator intervention replay). Score ladder UNMEASURED (planned native completion from distance, teacher transfer, automatic staging, causal decomposition and stronger control).

## Audit record
id: C008
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.50
old_bo4: 0.59
old_pass4: 0.42
old_ub95: 0.76
new_single: 0.48
new_single_range: 0.24-0.82
new_bo4: 0.64
new_pass4: 0.76
new_ub95: 0.82
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Cross observable identity and actuator mechanisms so student-response diagnosis must improve on complete privileged-teacher reward search.
redesign_single: 0.34
redesign_bo4: 0.45
redesign_pass4: 0.22
redesign_ub95: 0.62
redesign_gpuh: 162
attack_basis: LITERATURE-ONLY
demonstrated_ref: Eureka, GPT-4-0314 evolutionary reward reflection, 2023/2024; ROSETTA, GPT-4o and o1-mini staged reward code, 2026
gap_to_attack: Fit autonomous causal pixel-policy diagnosis and teacher transfer into a matched twelve-hour training budget
subfield_sota_ref: Grounded staged manipulation rewards, Srivastava ROSETTA, 2026; vision teaching Chen 2020
anchored_single: 0.43
anchored_bo4: 0.55
anchored_pass4: 0.48
anchored_ub95: 0.63
anchored_verdict: CONDITIONAL
anchored_binding_line: pass4>0.50
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
