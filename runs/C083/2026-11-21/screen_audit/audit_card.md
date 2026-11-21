# C083 — Augmentation gains after semantic invariance is broken — screen audit

## 1. What the screen claimed
The screen corrected the premise that every corrupted input must preserve program meaning: denoising can legitimately predict clean targets. It combined tagged auxiliary objectives, clean code, prose augmentation and bounded equivalence checking, forecasting ESTIMATED single/bo4/pass4/ub95 0.69/0.78/0.91/0.93; CUT, category DATA, because disabling questionable code transformations could bypass the proposed difficulty.

Old URLs, fetched in this session:
- Data augmentations for pretraining implementation — Michael Chen lab, 2026 — https://github.com/michaelchen-lab/data-augmentations-for-pretraining
- Bitvectors — Microsoft Z3 guide, 2026 accessed version — https://microsoft.github.io/z3guide/docs/theories/Bitvectors/

## 2. Evidence audit
The implementation distinguishes noisy inputs, sequence reorderings and offset targets; the screen's objective correction is substantive. Z3 can validate bounded bit-vector transformations, but it cannot establish beneficial learning transfer or cover an unspecified mini-language with richer effects automatically. No old source shows prose-only augmentation retaining enough reward while clean code satisfies this task's combined utility.

Grade: PARTIAL. Correct objective construction is supported, whereas the bypass's magnitude and autonomous code/text policy discovery were extrapolated. Syntax filtering is a weak baseline, but replacing that weak baseline with a sensible one does not prove the remaining task is saturated.

## 3. Research done now
- Demystifying Training-Time Augmentation for Data-Constrained Language Model Pretraining — Michael K. Chen et al., 2026 — https://arxiv.org/html/2606.16246v3 — fetched — The best reported post-decay loss is 3.792 on 150M subjects, yet several category combinations interfere and loss ranking imperfectly predicts downstream accuracy; both facts matter for a mixed execution/loss objective.
- Can Generalist Agents Automate Data Curation? — Feiyang Kang et al., 2026 — https://arxiv.org/html/2606.04261v1 — fetched — Opus 4.7/Claude Code runs selection-and-evaluation cycles and beats strong data baselines, but local policy search dominates unless scaffolding forces method adaptation.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern et al., 2024 — https://arxiv.org/html/2410.07095v1 — fetched — o1-preview/AIDE's valid competition submissions establish empirical ML search ability; its medal rate does not demonstrate semantic augmentation transfer to new interpreters.
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search — Yutaro Yamada et al., 2025 — https://arxiv.org/html/2504.08066v1 — fetched — The compositional-regularization investigation includes negative generalization results, reinforcing that executing an augmentation study and finding a useful invariance are different achievements.
- Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations? — Pedro Orvalho and Marta Kwiatkowska, 2025, revised 2026 — https://arxiv.org/abs/2505.10443 — fetched — Its program-mutation evaluation makes semantic robustness a real concern, but evaluates models as code reasoners rather than agents engineering training policies.

Search addressed augmentation target semantics, code mutation robustness and autonomous data research. The domain paper's own interaction failures cut against indiscriminate recipe stacking.

## 4. Re-estimated attack
All reward shares, probabilities, uncertainty spans and prospective costs below are ESTIMATED. Correct clean-target construction and task tags remove false supervision, plausibly capturing 0.22 reward; modality-specific clean replay/prose regularization might provide 0.21; mixture and corruption-strength selection another 0.12. The 0.55 total assumes useful code coverage remains adequate without aggressive augmentation. That assumption depends on the unfinished utility weights and cannot be read from the prose paper's loss gain.

Literature-capability outcomes 0.32/0.55/0.73 have probabilities 0.20/0.55/0.25. Low runs preserve code but achieve weak regularization; middle runs get a robust modality split; upper runs find compatible objectives that improve both slices. Single = 0.064+0.3025+0.1825 = 0.55, range 0.32–0.73. Bo4 = 0.73−0.18×0.75^4−0.23×0.20^4 = 0.67; pass4 = 1−0.75^4 = 0.68; ub95 = 0.73. Spread arises from training interference, chosen policy family and learner variability, rather than adding a uniform best-of-four bonus. Compared with the old 0.69 mean, this removes assumed transfer from text loss to executable behavior.

## 4A. Demonstrated capability and subfield SOTA
Chen et al.'s measured augmentation stack is the closest verified subfield reference: low-rate replacement, reversed prediction and weighted offsets outperform their clean-text baseline after decay. It is a 150M repeated-text study, not a frontier-scale code/text champion. The task's R≈1 control must beat that complete recipe plus clean-code/prose-only conditioning on actual private execution and loss at equal work. The published 3.792 loss supplies a reproduction target, not this card's reward denominator.

Curation-Bench's Opus 4.7/Claude Code reaches 33.7±0.3 across its multimodal instruction evaluations after ten policy iterations, training LLaVA-1.5-7B on one A100 per subset. Total session duration is not established; the separate CLIP instantiation takes approximately four H100-hours per train/evaluate cycle. The gap is objective invention for fresh program semantics rather than selecting existing instruction examples. MLE-bench's o1-preview/AIDE obtains bronze-or-better in 16.9% with twenty-four hours and one A10 per competition. It demonstrates search, but takes twice this card's wall budget and lacks the joint semantic/prose endpoint.

KNOWN-RECIPE covers lawful corruption targets and conservative modality conditioning. The complete augmentation attack remains LITERATURE-ONLY: no fetched twelve-hour agent result integrates new mini-language semantics, objective selection and validated learning improvements. Anchored ESTIMATED atoms 0.23/0.48/0.69 with weights 0.23/0.65/0.12 give single 0.45, range 0.23–0.69; bo4 = 0.69−0.21×0.88^4−0.25×0.23^4 = 0.56; pass4 = 1−0.88^4 = 0.40; ub95 = 0.69. The reward-scale mapping and upper-mode frequency are explicit assumptions.

## 5. Verdict under the kill lines
Evidence re-estimate CUT; ANCHORED CONDITIONAL, FLIPPED CUT→CONDITIONAL. The ESTIMATED bo4 margin is 0.04, with ub95 0.06 below its boundary. The screen correctly identified a lawful clean-target bypass, but current agent evidence does not demonstrate that bypass capturing enough joint learning utility. Retention requires an explicit objective contract and demonstrable improvement beyond the clean-code/prose-only control.

## 6. Redesign
Class b; REDESIGNABLE. Specify each augmentation as noisy conditioning, a reordered prediction task or newly labeled executable content. Supply the interpreter and semantics for every mini-language, including legitimate effect/order behavior. Start from correctly tagged auxiliary targets and the complete modality-conditioned baseline. Grade gains in execution coverage with a precommitted prose-retention constraint and complete transformed-pass costs, using independently composed program relations. A policy may disable any augmentation; the reference must demonstrate why doing so leaves worthwhile achievable utility.

The strongest re-attack combines clean-code replay, the published text stack, bounded-equivalent rewrites and standard mixture search. It will miss useful content-dependent objectives only if task-relevant effects and causal dependencies require different predictive views beyond a global modality switch. This is a frontier-relevant data-efficiency question, not a demand to preserve semantics in every corrupted input. ESTIMATED LITERATURE-ONLY redesigned outcomes 0.19/0.41/0.63, weights 0.30/0.62/0.08, yield single 0.36; bo4 = 0.63−0.22×0.92^4−0.22×0.30^4 = 0.47; pass4 = 1−0.92^4 = 0.28; ub95 0.63. Risk remains that conservative replay wins or gains vanish at scale. Decisive-check GPU-h ESTIMATED: 350M proxy, four policies×two seeds×four hours×one H100 = 32; 1B transfer, three finalists×two seeds×twelve hours×two H100 = 144; evaluation/accounting overhead 32; total 208 H100-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent content-conditioned augmentation agents). Grader noise UNMEASURED (planned: paired retraining seeds with deterministic interpreter checks). Score ladder UNMEASURED (planned: clean training, complete text augmentation, modality-conditioned baseline, semantics-conditioned policy and stronger joint control).

## Audit record
id: C083
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.69
old_bo4: 0.78
old_pass4: 0.91
old_ub95: 0.93
new_single: 0.55
new_single_range: 0.32-0.73
new_bo4: 0.67
new_pass4: 0.68
new_ub95: 0.73
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Define lawful targets and demonstrate execution gains from content-conditioned augmentation beyond the complete modality-conditioned baseline.
redesign_single: 0.36
redesign_bo4: 0.47
redesign_pass4: 0.28
redesign_ub95: 0.63
redesign_gpuh: 208
attack_basis: LITERATURE-ONLY
demonstrated_ref: Curation-Bench, Opus 4.7 Claude Code, 2026; MLE-bench, o1-preview AIDE, 2024
gap_to_attack: fresh program-semantic objective design and mixed pretraining validation
subfield_sota_ref: three-category text augmentation loss 3.792 at 150M, Chen et al., 2026
anchored_single: 0.45
anchored_bo4: 0.56
anchored_pass4: 0.40
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
