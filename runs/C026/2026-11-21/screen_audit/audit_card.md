# C026 — A self-auditing scaffold that chooses when to distrust its tests — screen audit
## 1. What the screen claimed
The old attack combined contract-aware differential execution, mutations, metamorphic checks and miniature training, with Optuna tuning escalation spend. Its ESTIMATED single/bo4/pass@4/ub95 were 0.72/0.80/0.92/0.94; CUT, category EXP, because this audit stack supposedly recovers deployment selection. The screen cited:

- https://arxiv.org/abs/1705.06640
- https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html?highlight=hyperband

## 2. Evidence audit
DeepXplore: Automated Whitebox Testing of Deep Learning Systems — Kexin Pei, 2017, fetched — demonstrates disagreement-driven input testing, not distinguishing a valid training-objective change from a faulty update. Efficient Optimization Algorithms — Optuna project, 2026 documentation snapshot, fetched — supplies samplers and pruning, without a validated scientific acceptance utility. In particular, rejecting disagreements can lose genuine improvements, which the card explicitly charges.

Grade: PARTIAL. Independent execution and mutation checks are available, but the central allocation decision is whether an expensive training comparison will reverse deployment. The screen treats that decision as a small controller implementation problem without comparable evidence. It also lacks the proportions of routine bugs versus legitimate semantic changes needed to justify its high mean.

## 3. Research done now
- DeepCrime: Mutation Testing of Deep Learning Systems Based on Real Faults — Nargiz Humbatova, 2021 — https://conf.researchr.org/details/issta-2021/issta-2021-technical-papers/42/DeepCrime-Mutation-Testing-of-Deep-Learning-Systems-Based-on-Real-Faults — fetched — Pre-training mutations grounded in real faults strengthen the attack's test adequacy checks. They do not label novel objective edits as scientifically desirable.
- CRADLE: Cross-Backend Validation to Detect and Localize Bugs in Deep Learning Libraries — Hung Viet Pham, 2019 — https://www.cs.purdue.edu/homes/lintan/publications/cradle-icse19.pdf — fetched — Cross-implementation checks uncover backend inconsistencies, supporting genuinely independent runners. Its expected-equivalence setting differs from intentional algorithm changes.
- KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch? — Yunxiang Zhang, 2026 — https://arxiv.org/abs/2607.16241 — fetched — Narrow correctness distributions and unrealistic baselines exaggerate kernel gains. This raises the value of independent audits while reducing confidence that familiar tests alone select useful patches.
- GPT-6.2 System Card, evaluations with challenging prompts — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — Research-debugging and post-training evaluations establish relevant current capabilities; the missing endpoint is an agent-built acceptance policy that also prices missed improvements.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace, 2025 — https://arxiv.org/html/2504.01848v1 — fetched — Executable replication remains distinct from plausible implementation, a negative check on equating test construction with scientific validation.

## 4. Re-estimated attack
All reward quantities are ESTIMATED on the provisional scale. Cheap differential checks plausibly recover 0.23, training-aware mutation and metamorphic checks add 0.15, and selective long-run escalation adds 0.14. The resulting mean near 0.52 leaves objective validity, slow-benefit patches and false rejection unresolved.

Use ESTIMATED outcomes 0.36/0.55/0.68 with probabilities 0.25/0.65/0.10. These represent overcautious rejection, useful routine screening and unusually successful scientific escalation. Spread is mainly policy/patch-family interaction, with training-seed effects secondary. ESTIMATED single=0.25×0.36+0.65×0.55+0.10×0.68=0.52, range 0.36–0.68. ESTIMATED bo4=0.36×0.25^4+0.55×(0.90^4−0.25^4)+0.68×(1−0.90^4)=0.59. With p=0.10, ESTIMATED pass@4=1−0.90^4=0.34; ub95=0.68 because cumulative mass below it is 0.90. This replaces the old broad optimism with an explicit small success tail. Attempt independence and mixture weights require measurement; the percentile is no fitted stronger-model projection.

## 4A. Demonstrated capability and subfield SOTA
DeepCrime and CRADLE are the strongest directly relevant validated testing tools found, while KernelBench-Verified supplies a contemporary robust-evaluation control. None reports the card's combined acceptance/missed-gain utility. The north star must therefore be a selection policy whose trained outcomes beat those tools at equal spend; R≈1 cannot be assigned from a mutation score.

OpenAI's 2026 system card reports GPT-6.2 Astra receiving 81.85% mean rubric credit on real research debugging. Its proprietary harness, runtime and compute for that subtest are not fully specified; diagnosis credit is not deployed patch utility. PostTrainBench Lite closes 74.79% of the base-to-instruction-reference gap with five hours on an H100 and small-billion-parameter subjects. That demonstrates training and recipe selection, not an acceptance oracle. PaperBench's Claude 3.5 Sonnet/BasicAgent receives 21.0% replication credit in twelve-hour attempts on one A10. Its partial implementation outcome limits what test-writing skill implies about validation. These are published observations, distinct from audit rollouts.

KNOWN-RECIPE supports differential/mutation screening. AGENT-DEMONSTRATED supports research diagnosis and ordinary training, without establishing cost-aware selective distrust across legitimate objective changes. attack_basis=LITERATURE-ONLY. In twelve hours, integrating these pieces and validating both accepted and rejected counterfactual patches is additional unshown work.

ANCHORED ESTIMATED R∼U[0.29,0.57] credits the demonstrated diagnostic building blocks but discounts policy transfer. ESTIMATED single=0.43, range 0.29–0.57; bo4=0.29+0.28×4/5=0.51; pass@4=1−(1−0)^4=0.00; ub95=0.29+0.95×0.28=0.56. The range expresses many incremental acceptance decisions. Native utility anchors and the fraction of legitimate semantic revisions remain assumptions.

## 5. Verdict under the kill lines
Section 4 gives CONDITIONAL: ESTIMATED bo4 clears by only 0.01. ANCHORED verdict is also CONDITIONAL, FLIPPED CUT→CONDITIONAL versus the old screen, with bo4 clearance 0.09. Current research debugging strengthens the attack, but no observed result connects that capability to priced false-rejection avoidance. The condition is an executable, public distinction between implementation equivalence and scientific objective validity, plus a measured gain over the full audit stack.

## 6. Redesign
Cause (b), audit allocation optimized by ordinary search; REDESIGNABLE. Publish a versioned mathematical objective and evaluation contract for each campaign. Supply authentic patch proposals where an approximation preserves its intended objective yet changes optimization dynamics, and others silently violate masking, reduction or gradient rules. Let independent runners check equivalence where appropriate, and allow every controller to commission same-budget training when equivalence is insufficient.

Score final model quality with validation spend and missed valid improvements charged continuously. Include DeepCrime-like mutation coverage, CRADLE-style diversity, contract compilation and tuned short-training selection in the floor. The reference must predict when longer measurements change a decision from disclosed gradient/learning-curve evidence. This remains useful ML reliability research without an obsolete oracle dictating the answer.

Strongest redesigned recipe adds uncertainty-directed continuation to those controls. Its basis remains LITERATURE-ONLY. ESTIMATED uniform [0.28,0.53] yields single=0.41, bo4=0.28+0.25×4/5=0.48, pass@4=0.00 and ub95=0.28+0.95×0.25=0.52. The residual is learning-dynamics diagnosis beyond equivalence checking; a general conservative selector could still erase it. Cost ESTIMATED 144 H100 GPU-h: 1B subjects, four acceptance arms, three campaign seeds, eight hours on one H100 each gives 96; an 8B reset actor costs 24; independent rejected-patch evaluation adds 24. Arithmetic: 4×3×8×1+24+24=144. Calibrate feasibility before a full attack panel.

## 7. Measurement status
Rollouts UNMEASURED (planned: independently authored harnesses on matched patch campaigns). Grader noise UNMEASURED (planned: fixed selections rerun with paired training seeds). Score ladder UNMEASURED (planned: narrow self-tests, independent runner, complete mutation/differential stack, selective continuation and attainable oracle-allocation control).

## Audit record
id: C026
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.72
old_bo4: 0.80
old_pass4: 0.92
old_ub95: 0.94
new_single: 0.52
new_single_range: 0.36-0.68
new_bo4: 0.59
new_pass4: 0.34
new_ub95: 0.68
new_verdict: CONDITIONAL
binding_line: none
flip: CUT->CONDITIONAL
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Separate public objective equivalence from learning-dynamics evidence and price both false acceptance and missed gains.
redesign_single: 0.41
redesign_bo4: 0.48
redesign_pass4: 0.00
redesign_ub95: 0.52
redesign_gpuh: 144
attack_basis: LITERATURE-ONLY
demonstrated_ref: Internal Research Debugging/PostTrainBench Lite, GPT-6.2 Astra, 2026; PaperBench BasicAgent, Claude 3.5 Sonnet, 2025
gap_to_attack: autonomous audit commissioning with priced false rejections and objective changes
subfield_sota_ref: training mutation DeepCrime 2021; cross-backend CRADLE 2019; KernelBench-Verified 2026
anchored_single: 0.43
anchored_bo4: 0.51
anchored_pass4: 0.00
anchored_ub95: 0.56
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
