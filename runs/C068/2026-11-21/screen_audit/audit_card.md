# C068 — Preserve mixed DPO/SFT semantics while packing uneven responses — screen audit
## 1. What the screen claimed
The proposed attack used an unpacked scalar loss oracle, correct global reductions, packed pair/mask preservation and joint tuning of DPO temperature, supervised weight and length conditioning. The old CUT/TRAIN verdict rested on ESTIMATED single 0.81, best-of-four 0.89, pass@4 0.98 and upper-95% 0.97. It cited:
- https://arxiv.org/abs/2305.18290
- https://huggingface.co/docs/trl/main/en/dpo_trainer

## 2. Evidence audit
DPO establishes effective preference training, while TRL exposes mixed objectives and response-length handling. Neither demonstrates the card's exact invariant gradients plus retained generation quality on fresh length-correlated mechanisms. Nevertheless, this is a short-feedback post-training problem, so absence of a paper implementing this precise reduction bug is weak protection. Grade: PARTIAL: the empirical method is established, while its expected share of the unmeasured card reward was asserted.

## 3. Research done now
Search covered mixed preference objectives, length effects and autonomous small-model post-training. All referenced material was fetched. This audit's rewards, probabilities and budgets are ESTIMATED; reported evaluation statistics are not card measurements.
- Direct Preference Optimization: Your Language Model is Secretly a Reward Model — Rafael Rafailov et al., 2023, revised 2024 — https://arxiv.org/abs/2305.18290 — fetched — validates the preference component, without resolving supervised-token versus pair-level reduction units.
- DPO Trainer — Hugging Face TRL, 2026 documentation snapshot — https://huggingface.co/docs/trl/main/en/dpo_trainer — fetched — mixed-loss support makes the search inexpensive to implement; configuration availability does not prove partition-equivalent training.
- Pre-DPO: Improving Data Utilization in Direct Preference Optimization Using a Guiding Reference Model — Junshu Pan et al., 2025 — https://arxiv.org/abs/2504.15843 — fetched — identifies reference-dependent data weighting and robustness/forgetting problems, both broadening the attack menu and warning that mixture tuning is not automatically retention-safe.
- GPT-6.2 System Card, PostTrainBench Lite — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — actual autonomous post-training closes much of a base-to-instruct gap at the relevant subject scale, raising the attack substantially.
- PostTrainBench — PostTrainBench team, 2026 — https://posttrainbench.com/ — fetched — documents ten-hour, one-H100 CLI-based training with data access and submitted checkpoints, a credible operational comparator for the mixture search.
- PostTrainBench v1.2: More reliable scores and verdicts — PostTrainBench team, 2026 — https://posttrainbench.com/blog/posttrainbench-1-2/ — fetched — publishes agent scores after scoring/compliance changes; the modest overall benchmark accuracies temper any inference of universal post-training success.

## 4. Re-estimated attack
After fixing semantics, a static joint mixture/temperature search plausibly captures ESTIMATED 0.38, length-conditioned coefficients ESTIMATED 0.17, and packing/reference-computation efficiency ESTIMATED 0.12 of provisional reward. These amounts represent combined preference/retention utility, not permission to change declared normalization. A correct unpacked implementation is a lawful competitor if it fits the same resource envelope. Missing novel semantic mechanisms make a small coefficient family unusually competitive.

Assuming a strong recipe integrator, assign ESTIMATED probability {0.15,0.60,0.25} to R={0.46,0.69,0.83}. The lower outcome preserves gradients but overfits a length correlation; the upper mode finds a mixture that transfers and retains quality. ESTIMATED single=0.0690+0.4140+0.2075=0.69, range 0.46–0.83. ESTIMATED best-of-four=0.83−0.14×0.75^4−0.23×0.15^4=0.79. Since p=0.85, ESTIMATED pass@4=1−0.15^4=1.00; upper-95%=0.83. The old single estimate was too high for unmeasured preference/retention tradeoffs, but repeated search remains dangerous.

## 4A. Demonstrated capability and subfield SOTA
Pre-DPO is the strongest newly fetched preference-specific comparator: it reports improved DPO/SimPO results on AlpacaEval and Arena-Hard without extra data or external models. These judged-chat metrics differ from exact preference behavior and retained generation in this card, so they do not establish a universal current champion. Anchor the reference to a measured competent mixed-loss implementation, with reference-guided and length-aware alternatives as controls. A native R≈1 endpoint is UNMEASURED; public chat win rates must not be substituted for it.

GPT-6.2 Astra's tool-enabled PostTrainBench Lite setup post-trains 1.7B, 3B and 4B base models, using five hours on one H100. It reports 74.79% mean closure of the base-to-instruction-reference performance gap. This is direct evidence for finding, running and validating small-model training recipes within less than this task's wall time. It does not measure exact DPO/SFT gradient invariance, and its scaffold internals are only partly public. Independently, PostTrainBench v1.2 reports Opus 5.5 at 43.8% aggregate task performance in its CLI-based ten-hour/one-H100 setting; its native setup lists the same small-model scale. That is benchmark performance, not reference-gap closure or a solve probability. It reinforces autonomous post-training feasibility while showing substantial remaining errors.

KNOWN-RECIPE covers reduction algebra and mixed-loss trainers. AGENT-DEMONSTRATED covers the load-bearing empirical recipe search and checkpoint validation at comparable scale/budget, so attack_basis=DEMONSTRATED-AGENT, with explicit transfer uncertainty for invariant packing and joint retention. This classification does not claim either agent solved C068. The remaining twelve-hour work is comparatively bounded: implement the scalar oracle, check several batch partitions and use real validation to select a small coefficient family.

Anchored ESTIMATED R={0.41,0.65,0.78}, probabilities {0.16,0.60,0.24}, gives single=0.0656+0.3900+0.1872=0.64, range 0.41–0.78. ESTIMATED best-of-four=0.78−0.13×0.76^4−0.24×0.16^4=0.74; pass@4=1−0.16^4=1.00; upper-95%=0.78. Forecast probabilities remain assumptions about transfer, not copied benchmark percentages.

## 5. Verdict under the kill lines
Evidence and ANCHORED verdicts are CUT; anchored status is UNCHANGED. Best-of-four binds at ESTIMATED 0.74, exceeding 0.60 by 0.14; pass@4 and upper-95% also breach. The agent evidence justifies substantial recipe-search capability here, unlike a claim based solely on knowing DPO's formula. The verdict still assumes the task's unmeasured reward scale has the proposed native reserve.

## 6. Redesign
Cause (b), REDESIGNABLE. Keep correct packed reduction as infrastructure, then grade evidence-dependent preference weighting. Supply auditable provenance features and development examples from disclosed preference mechanisms: some pairs encode valid factual corrections, others legitimate stylistic choices, and supervised targets sometimes omit required evidence. Cross these relationships with length so equal-length pairs require different weights. Hold out new semantic compositions, with the same provenance schema and learning resources. A trusted executable oracle defines downstream behavior; retention is measured on an independent generation suite.

The baseline includes corrected DPO/SFT, length-aware mixtures, reference-guided weighting and a competent provenance classifier. The re-attack combines those components with validation search; it no longer wins merely by selecting length bins. Its basis is LITERATURE-ONLY for transferring evidence-reliability estimation into useful loss allocation. ESTIMATED outcomes {0.27,0.45,0.64}, probabilities {0.36,0.56,0.08}, imply single=0.40, best-of-four=0.64−0.19×0.92^4−0.18×0.36^4=0.50, pass@4=1−0.92^4=0.28, upper-95%=0.64. Risk: the provenance classifier may solve every mechanism; include that lawful control before promotion. ESTIMATED pilot: 3B policy plus charged 3B frozen reference, four arms × three seeds × twelve hours × one H100=144 H100-h; reference preparation/parity 24 plus endpoint/retention evaluation 24 yields 192 H100-h. No training was executed.

## 7. Measurement status
Rollouts UNMEASURED (planned independent mixed-loss searches); grader noise UNMEASURED (planned paired-seed preference and retention endpoints); score ladder UNMEASURED (planned corrected static mixture, length policy, reference weighting, provenance weighting and feasible stronger control).

## Audit record
id: C068
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.81
old_bo4: 0.89
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.69
new_single_range: 0.46-0.83
new_bo4: 0.79
new_pass4: 1.00
new_ub95: 0.83
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Learn evidence-dependent preference weighting after correct packing and mature mixed-loss search enter the floor.
redesign_single: 0.40
redesign_bo4: 0.50
redesign_pass4: 0.28
redesign_ub95: 0.64
redesign_gpuh: 192
attack_basis: DEMONSTRATED-AGENT
demonstrated_ref: PostTrainBench Lite, GPT-6.2 Astra, 2026; PostTrainBench v1.2, Opus 5.5+Claude Code, 2026
gap_to_attack: packing-invariant mixed-loss implementation and joint retention transfer
subfield_sota_ref: reference-guided Pre-DPO, Pan et al., 2025
anchored_single: 0.64
anchored_bo4: 0.74
anchored_pass4: 1.00
anchored_ub95: 0.78
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
