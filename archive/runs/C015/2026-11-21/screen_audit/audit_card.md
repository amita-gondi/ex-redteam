# C015 — Learn a grader whose abstention triggers useful data collection — screen audit
## 1. What the screen claimed
The earlier attack refreshed duration-aware disagreement, gradient and diversity scores after each ASR update, explored confidently missed clusters and distilled the ranking into the permitted predictor. It gave ESTIMATED single/bo4/pass@4/ub95 of 0.58/0.68/0.72/0.85 and CUT, category DATA, because a normal iterative acquisition loop already handles acquisition-induced drift. Sources listed were:
- https://arxiv.org/abs/1612.03226
- https://arxiv.org/abs/1906.08158
## 2. Evidence audit
The speech paper measures acquisition against ASR error; BatchBALD demonstrates batch redundancy control elsewhere. Neither validates duration pricing or distillation of multi-refresh selection into the permitted predictor.

Drift adaptation is routine, but gains beyond a competent floor, feature costs and accent-ranking reversals remain unresolved. Grade: PARTIAL. New speech-specific composition results strengthen the mechanism without establishing its budgeted reward.
## 3. Research done now
- Active Learning for Speech Recognition: the Power of Gradients — Jiaji Huang et al., 2016 — https://arxiv.org/abs/1612.03226 — fetched — Shows useful acquisition signals beyond confidence on ASR itself; raises the gradient-feature arm, but its learner predates the proposed inherited acoustic model.
- BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning — Andreas Kirsch et al., 2019 — https://arxiv.org/abs/1906.08158 — fetched — Demonstrates why independent uncertainty rankings waste purchases on redundant batches, strengthening joint selection without proving speech-specific scale transfer.
- Combining X-Vectors and Bayesian Batch Active Learning: Two-Stage Active Learning Pipeline for Speech Recognition — Ognjen Kundacina et al., 2024, revised 2025 — https://arxiv.org/abs/2406.02566 — fetched — Combines speaker-space clustering with Bayesian ASR selection and evaluates heterogeneous/OOD speech. This is close empirical support for the screen's combined recipe, with duration pricing and predictor distillation still unverified.
- Advancing African-Accented English Speech Recognition: Epistemic Uncertainty-Driven Data Selection for Generalizable ASR Models — Bonaventure F. P. Dossou, 2025 — https://aclanthology.org/2025.acl-srw.1/ — fetched — Multi-round accented-speech adaptation directly raises confidence that refreshed uncertainty and core-set selection improve downstream WER. Its annotation protocol and baseline comparisons cannot be imported as this card's normalized reward.
- Understanding Uncertainty-based Active Learning Under Model Mismatch — Amir Hossein Rahmati et al., 2024 — https://arxiv.org/abs/2408.13690 — fetched — Demonstrates failure of uncertainty sampling under model misspecification, lowering confidence that harder accents are always the best purchases. This is a general warning, not evidence that the proposed ASR instance actually has that failure.

The search deliberately included ASR acquisition successes and uncertainty failures. The three added sources replace a generic drift argument with speech-specific positive evidence and a defined negative mechanism.
## 4. Re-estimated attack
Every quantity in this forecast is ESTIMATED. Duration-aware informative sampling earns roughly 0.25 of the available improvement, diversity/exploration adds 0.17, and refreshing a learned ranking after retraining adds 0.17 net of feature-scoring and distillation costs. These are marginal score allocations on unmeasured anchors, not reported WER improvements. Remaining reward depends on shared confident blind spots and acquisitions whose value appears only after complementary examples have trained the learner.

Use three campaign outcomes: R=0.37 with probability 0.20 when model mismatch makes uncertainty misleading; R=0.59 with probability 0.55 when a strong routine policy reaches a good but imperfect ranking; R=0.77 with probability 0.25 when cluster coverage and refresh expose the important speech mechanisms. Spread comes from early purchase paths, ASR seeds and finding a good cost normalization, not independent transcript noise. ESTIMATED single=0.20×0.37+0.55×0.59+0.25×0.77=0.59, range 0.37–0.77. ESTIMATED bo4=0.37×0.20^4+0.59×(0.75^4−0.20^4)+0.77×(1−0.75^4)=0.71. ESTIMATED p=0.25 gives pass@4=1−0.75^4=0.68. ESTIMATED ub95=0.77, with cumulative mass 0.75 below the upper outcome.

Asymmetric acquisition success raises bo4 despite a similar mean; missing tail evidence lowers ub95. Independence applies to campaign restarts, not purchases. Accent-family difficulty and scaling remain unmeasured.
## 4A. Demonstrated capability and subfield SOTA
The closest acquisition anchors are Dossou and Kundacina (fetched above). Agentic Data Sampling Framework for Multilingual ASR via Linguistic-Aware Error-Driven Optimization — Zhiheng Qian et al., 2026 — https://arxiv.org/html/2610.36538v1 — fetched — reports mean WER/CER improving from 23.9 to 19.4 with Whisper-medium on eight Ascend 910Bs. LLM identity and elapsed runtime are unreported; audio-hours denote exposure. It resamples labeled speech, without purchasing unrevealed transcripts. These results anchor multi-refresh WER capability; minute-priced R≈1 remains unmeasured.

- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern et al., 2024 — https://arxiv.org/html/2410.07095v1 — fetched. o1-preview+AIDE reaches a reported bronze-or-better result on 16.9% of tasks with twenty-four hours and one A10 per attempt. It demonstrates pipeline experimentation, with twice this card's wall budget and no demonstrated minute-priced acquisition loop.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-used-to-assess-high-ai-self-improvement-capabilities — fetched: PostTrainBench Lite's Astra agent closes reported 74.79% of the instruction-reference gap in five hours on one H100; detailed scaffold is undisclosed. Dataset choice/retraining transfer directly, unlike unpurchased-speech valuation and predictor distillation.

The Qian system is valuable AGENT-DEMONSTRATED sampling evidence, but not unaided discovery/integration of this attack within a comparable elapsed budget. Overall attack_basis=LITERATURE-ONLY. In twelve hours a researcher still must build the paid-label loop, adapt blind-spot exploration and validate the predictor's effects; treating a human-authored sampling scaffold as autonomous R&D would overstate the evidence.

ANCHORED ESTIMATED states 0.32/0.52/0.71 have probabilities 0.30/0.59/0.11 for ineffective paid selection, useful ordinary integration and successful acquisition-aware tuning. ESTIMATED single=0.30×0.32+0.59×0.52+0.11×0.71=0.48, range 0.32–0.71; bo4=0.32×0.30^4+0.52×(0.89^4−0.30^4)+0.71×(1−0.89^4)=0.59; pass@4=1−0.89^4=0.37; ub95=0.71. This assumption-dependent forecast keeps substantial recipe strength without claiming the label-acquisition integration was demonstrated.
## 5. Verdict under the kill lines
Section 4's evidence re-estimate says CUT; ANCHORED headline says CONDITIONAL, FLIPPED CUT→CONDITIONAL. ESTIMATED bo4 clears by 0.01 and ub95 by 0.04. Recent agentic ASR sampling raises the attack, but its labeled-corpus access, unnamed LLM and missing elapsed budget leave the actual paid-transcript capability unresolved. Require the concrete blind-spot/complementarity and acquisition-cost controls below.
## 6. Redesign
Potential cause (a) is iterative acquisition. This REDESIGNABLE full-cost complementarity condition has LITERATURE-ONLY re-attack support: Qian does not demonstrate discovery of paid-label prerequisites.

Use real speech with interacting pronunciation, channel and lexical mechanisms: clean-context examples may unlock a later pronunciation distinction. Supply audio embeddings, learner diagnostics and equal-minute transcript access. Demonstrate ordered benefits through dev purchase ablations; hidden combines disclosed mechanisms without secret accent labels.

Score final WER and a frozen acquisition-curve utility, charging transcripts, feature passes and rejected campaigns. The floor includes gradient/diversity/refresh/exploration. The strongest re-attack adds lookahead updates and marginal-value learning, trading prerequisite discovery against acoustic training. This is useful transcript-efficient adaptation; random coverage cheaply supplying every prerequisite is the critical bypass to test.

ESTIMATED redesigned states 0.26/0.44/0.63 carry probabilities 0.40/0.52/0.08 for prerequisite misses, partial lookahead and effective complementarity discovery. ESTIMATED single=0.40×0.26+0.52×0.44+0.08×0.63=0.38; bo4=0.26×0.40^4+0.44×(0.92^4−0.40^4)+0.63×(1−0.92^4)=0.49; pass@4=1−0.92^4=0.28; ub95=0.63. The numbers plausibly clear the screen but depend on a same-budget attainable control, rather than normalization over negligible WER differences.

ESTIMATED falsification budget: 300M ASR plus 30M predictor; 4 policies × 3 seeds × 3 refreshes × 3 hours × 1 H100=108 GPU-h. Predictor/scoring work adds 30, and independent WER evaluation 24: total 162 H100 GPU-h. No transcription is purchased in this audit; future pilots use already authorized transcript assets behind the acquisition interface.
## 7. Measurement status
Rollouts UNMEASURED (planned clean-state full acquisition campaigns with the speech-specific composite). Grader noise UNMEASURED (planned speaker-cluster WER intervals and retraining seeds). Score ladder UNMEASURED (planned static confidence through lookahead acquisition, priced in minutes and total compute).
The numerical reward and future-cost fields are ESTIMATED, rather than ASR measurements.
## Audit record
id: C015
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 8
old_single: 0.58
old_bo4: 0.68
old_pass4: 0.72
old_ub95: 0.85
new_single: 0.59
new_single_range: 0.37-0.77
new_bo4: 0.71
new_pass4: 0.68
new_ub95: 0.77
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Evaluate ordered complementary speech acquisitions with disclosed interaction examples and fully costed lookahead baselines.
redesign_single: 0.38
redesign_bo4: 0.49
redesign_pass4: 0.28
redesign_ub95: 0.63
redesign_gpuh: 162
attack_basis: LITERATURE-ONLY
demonstrated_ref: Agentic ASR sampling, LLM unspecified with Whisper-medium, 2026; MLE-bench, o1-preview AIDE, 2024; PostTrainBench Lite, GPT-6.2 Astra, 2026
gap_to_attack: discovering minute-priced acquisition with unrevealed transcript labels
subfield_sota_ref: multi-round accented acquisition, Dossou, 2025; adaptive multilingual sampling, Qian, 2026
anchored_single: 0.48
anchored_bo4: 0.59
anchored_pass4: 0.37
anchored_ub95: 0.71
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
