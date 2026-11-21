# C041 — Pretrain with a tokenizer whose byte cost changes — screen audit
## 1. What the screen claimed
The screen combined byte-balanced sampling, boundary-correct packing, delivered-work learning-rate schedules and proxy-fitted language mixtures. Its ESTIMATED single/bo4/pass@4/ub95 were 0.81/0.88/0.98/0.98, yielding CUT, category DATA, because exposure correction and mixture optimization supposedly captured almost all useful improvement. It cited these URLs:
- https://arxiv.org/abs/2305.10429
- https://arxiv.org/abs/2407.01492

## 2. Evidence audit
DoReMi demonstrates transfer of learned domain weights to a larger model; RegMix establishes that tiny-model experiments can rank useful mixtures. Neither paper evaluates byte-normalized multilingual loss jointly with packing and delivered-FLOP schedules, and neither measures an autonomous researcher assembling that combination. The old justification also credits unit correction although the design contract places competent byte-aware allocation in the floor. Grade: PARTIAL; the mixture component is real, but its incremental reward and the claimed integration reliability were extrapolated.

## 3. Research done now
All performance forecasts below, including audit-record values, are ESTIMATED; quoted publication results describe external experiments, never measurements of C041.
- DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining — Sang Michael Xie et al., 2023 — https://arxiv.org/abs/2305.10429 — fetched — A 280M proxy informs an 8B model. This strengthens the mixture attack while leaving language-specific byte utility untested.
- RegMix: Data Mixture as Regression for Language Model Pre-training — Qian Liu et al., 2024, revised 2025 — https://arxiv.org/abs/2407.01492 — fetched — Its 512 small-model fits and larger-model validation support response modeling; the substantial experimental programme cannot simply be assumed to fit this attack's budget.
- Revisiting Multilingual Data Mixtures in Language Model Pretraining — Negar Foroutan et al., 2025 — https://arxiv.org/abs/2510.25947 — fetched — Experiments at 1.1B and 3B find useful multilingual transfer and challenge simplistic language-family allocation. This cuts against treating byte balance as the optimal learning allocation.
- RegMix-D: Dynamic Data Mixing via Proxy Training Trajectories — Kaiyan Zhao et al., 2026 — https://aclanthology.org/2026.findings-aacl.84/ — fetched — Trajectory-based mixture selection expands the lawful baseline beyond a static response surface; it does not establish the byte/packing interaction here.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — The NanoGPT experiment demonstrates autonomous training improvements, raising confidence in ordinary training-loop edits but not multilingual allocation discovery.
- PaperBench: Evaluating AI’s Ability to Replicate AI Research — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched — Incomplete executed replications warn against converting the existence of mixture code into reliable end-to-end scientific validation.

## 4. Re-estimated attack
Use accepted-byte instrumentation and a competent packer first, then optimize exposure temperatures, proxy response models and work-indexed schedules together. Conditional on successful integration, attribute ESTIMATED 0.12 reward to residual packing/exposure improvements above the frozen floor, 0.26 to mixture selection and 0.12 to schedule interactions: total 0.50. These are increments on the provisional normalized scale, not measured additive fractions of multilingual loss. The unresolved part is transfer to dialects whose learning response differs despite matching token expansion.

For a literature-informed implementation forecast, use scores {0.30,0.51,0.68} with probabilities {0.25,0.50,0.25}. Failed proxy transfer, ordinary integration and unusually good allocation explain the modes; training-seed variability is folded into those representative outcomes. Mean = 0.25×0.30+0.50×0.51+0.25×0.68 = 0.50, range 0.30–0.68. With independent researcher restarts, E[max4] = 0.68−0.17×0.75^4−0.21×0.25^4 = 0.63. Here p=0.25, so pass@4=1−0.75^4=0.68; the single-run 95th percentile is 0.68. Unlike the old 0.81, this forecast gives no second payout for repairing the floor's byte ledger.

## 4A. Demonstrated capability and subfield SOTA
Subfield SOTA anchor: RegMix-D (Zhao, 2026) is a current dynamic-mixture comparator; RegMix supplies demonstrated scale transfer, and Foroutan supplies multilingual evidence at relevant subject sizes. No fetched result establishes a best achievable byte-loss/FLOP frontier under C041's exact constraints. R≈1 therefore requires a measured stronger control built from these methods; it cannot honestly be assigned to an invented optimal scheduler.

Two fetched agent results bracket the inference. OpenAI's GPT-6.2 Astra, using its internal training-agent evaluation, saved 42.87% of baseline NanoGPT training time in two hours on one H100; the public card does not specify the scaffold's detailed architecture. That validates short training-code experiments, not per-language exposure transfer. PaperBench's o1 with IterativeAgent obtained 24.4% replication credit with twelve hours and an A10 development environment; reproducing interacting mixture/packing effects is closer to its execution burden than to a pure sampler patch, though its older model and from-scratch constraints are less favorable.

KNOWN-RECIPE exists; AGENT-DEMONSTRATED multilingual joint allocation does not. attack_basis=LITERATURE-ONLY. An agent must build a trustworthy byte-loss ledger, choose informative mixture probes, establish proxy ranking transfer and validate full-horizon winners within twelve hours. Those steps remain assumptions.

ANCHORED distribution: {0.29,0.48,0.65} with mass {0.20,0.65,0.15}, reflecting a smaller chance of finding and validating the transferable policy. ESTIMATED mean=0.20×0.29+0.65×0.48+0.15×0.65=0.47, range 0.29–0.65; bo4=0.65−0.17×0.85^4−0.19×0.20^4=0.56; pass@4=1−0.85^4=0.48; ub95=0.65. These are scenario probabilities, not fitted benchmark frequencies, and the verdict rests on assumption.

## 5. Verdict under the kill lines
Section 4 yields CUT through bo4=0.63 and pass@4=0.68. Headline ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL, with bo4 0.04 below its line and pass@4 0.02 below its line. Published scale-transfer results keep the attack credible, but the agent evidence does not substantiate the old near-certain solve. Promotion requires the coupled-transfer condition below and frozen native anchors.

## 6. Redesign
Cause (a): mature data-allocation stack. REDESIGNABLE. Give the learner visible parallel-domain corpora where early cross-language prerequisites improve later technical-dialect learning, while long packed contexts compete with the prerequisite's exposure budget. Publish matched dev trajectories showing an actual allocation-ranking reversal; independently author held-out dependency structures with the same observable statistics. Grade full-run byte losses under equal realized FLOPs and language coverage. Put byte balancing, RegMix-D, length packing and delivered-work schedules into the combined floor.

The strongest re-attack fits trajectory-dependent transfer and jointly searches allocation and packing. Static efficiency corrections no longer earn reward; transferable sequencing must improve native learning. No needed language metadata is withheld. Frontier labs would value predicting multilingual transfer under physical compute constraints. Residual risk: dynamic regression already captures the reversal, or the stronger control has negligible physical reserve; either observation kills the revised task.

Redesign basis LITERATURE-ONLY. ESTIMATED outcomes {0.25,0.43,0.58}, masses {0.25,0.65,0.10}: single=0.40, bo4=0.58−0.15×0.90^4−0.18×0.25^4=0.48, pass@4=0.00, ub95=0.58. Pilot cost ESTIMATED 240 H100 GPU-h: 1B subject, four allocation/packing arms × three seeds × sixteen hours × one H100 =192, plus 24 proxy GPU-h and 24 evaluation GPU-h. This is a future falsification pilot, not work performed here.

## 7. Measurement status
Rollouts UNMEASURED (planned independent allocation searches on fresh transfer structures). Grader noise UNMEASURED (planned paired seed repeats of byte-loss training). Score ladder UNMEASURED (planned token sampler, byte-aware combined floor, sequencing reference and stronger attainable control).

## Audit record
id: C041
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.81
old_bo4: 0.88
old_pass4: 0.98
old_ub95: 0.98
new_single: 0.50
new_single_range: 0.30-0.68
new_bo4: 0.63
new_pass4: 0.68
new_ub95: 0.68
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Require validated context-dependent multilingual transfer reversals beyond the complete byte-aware mixture floor.
redesign_single: 0.40
redesign_bo4: 0.48
redesign_pass4: 0.00
redesign_ub95: 0.58
redesign_gpuh: 240
attack_basis: LITERATURE-ONLY
demonstrated_ref: NanoGPT, GPT-6.2 Astra, 2026; PaperBench, o1 IterativeAgent, 2025
gap_to_attack: Joint byte-aware multilingual transfer is untested autonomously
subfield_sota_ref: RegMix-D, Zhao, 2026; multilingual transfer, Foroutan, 2025
anchored_single: 0.47
anchored_bo4: 0.56
anchored_pass4: 0.48
anchored_ub95: 0.65
anchored_verdict: CONDITIONAL
anchored_binding_line: pass4>0.50
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
