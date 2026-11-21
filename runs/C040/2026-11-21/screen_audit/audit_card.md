# C040 — Pretrain exact arithmetic without washing out language — screen audit
## 1. What the screen claimed
The screen proposed parser/interpreter emission with scratchpads, intermediate labels, execution filtering and language replay. ESTIMATED single/bo4/pass@4/ub95=0.77/0.85/0.95/0.97 led to CUT/DATA because program execution bypasses neural arithmetic. It cited:
- https://arxiv.org/abs/2112.00114
- https://arxiv.org/abs/2211.12588

## 2. Evidence audit
Show Your Work establishes intermediate supervision; Program of Thoughts delegates arithmetic to generated code. The latter uses capable pretrained models, without demonstrating objective-only compiler learning in a smaller model while retaining language. Grade: ASSUMED: inference success was extrapolated to constrained training. An objective-code artifact also does not authorize replacing the corpus.

## 3. Research done now
- Show Your Work: Scratchpads for Intermediate Computation with Language Models — Maxwell Nye et al., 2021 — https://arxiv.org/abs/2112.00114 — fetched — Scratchpad training helps multi-step execution, supporting useful intermediate labels here. It does not establish general notation transfer with a language-retention constraint.
- Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks — Wenhu Chen et al., 2022, revised 2023 — https://arxiv.org/abs/2211.12588 — fetched — Codex-generated programs make external exact arithmetic a real lawful capability. The paper supports the grader-alignment concern, while the learner-training route remains an extrapolation.
- Arithmetic Transformers Can Length-Generalize in Both Operand Length and Count — Hanseul Cho et al., 2024, revised 2025 — https://arxiv.org/abs/2410.15787 — fetched — Task-structured scratchpads and position coupling achieve meaningful arithmetic generalization. These task-specific positional mechanisms cannot be silently added through an objective-only channel.
- Program-of-Thought Reveals LLM Abstraction Ceilings — Mike Zhou et al., 2026 — https://aclanthology.org/2026.findings-eacl.257/ — fetched — PoT fine-tuning improves consistency without reliably closing accuracy gaps under isomorphic changes. This directly weakens the assumption that executable traces automatically induce transferable structure.
- Procedural Pretraining: Warming Up Language Models with Abstract Data — Liangze Jiang et al., 2026 — https://proceedings.mlr.press/v306/jiang26ap.html — fetched — A small early procedural-data fraction improves language/code/mathematics learning in evaluated models. It raises confidence that algorithmic learning need not wash out language, but its data intervention is outside a strictly fixed-corpus objective unless explicitly authorized.

## 4. Re-estimated attack
ESTIMATED opportunity shares: 0.40 simple executable-program emission, 0.35 compositional/notation transfer and 0.25 arithmetic-language retention. ESTIMATED recovery fractions 0.90/0.65/0.26 yield 0.40×0.90+0.35×0.65+0.25×0.26=0.65. This is the recipe's possible capability, conditional on sufficient legal traces. It assumes neither extra objective FLOPs nor new synthetic examples are free.

An ESTIMATED distribution places probability 0.25/0.50/0.25 on R=0.42/0.68/0.83. These correspond to brittle program imitation, a useful generic emitter and good transfer with retained language. Learner initialization, objective selection and whether a reusable interpreter matches the problem interface produce the spread. ESTIMATED single=0.25×0.42+0.50×0.68+0.25×0.83=0.65, range 0.42–0.83; bo4=0.83−0.15×0.75^4−0.26×0.25^4=0.78. ESTIMATED p=0.75 gives pass@4=1−0.25^4=1.00 rounded; ub95=0.83. Compared with the screen, this removes substantial unsupported transfer and retention credit while keeping the program-execution route dangerous.

## 4A. Demonstrated capability and subfield SOTA
For internal arithmetic, Cho et al.'s fetched 2025 result is a concrete attainable length-generalization reference; for mixed pretraining, Jiang et al.'s 2026 procedural warmup is the closest retained-language result consulted. For the actual executed-program interface, PoT establishes a strong synthesis baseline. None combines objective-only access, novel numeral compositions, equal total FLOPs and language loss into a demonstrated top anchor. R≈1 must await such a legal joint control; separate task maxima cannot be added together.

- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — Astra's internal training agent closes much of the instruction-model gap on tasks including GSM8K, using five hours and one H100. This supports arithmetic-related training search, not numeral-system transfer plus retained prose.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern and colleagues at OpenAI, 2024 — https://arxiv.org/html/2410.07095v1 — fetched — o1-preview+AIDE performs complete training/data experiments with one A10 over twenty-four hours and earns medals on some tasks. It does not demonstrate designing a general exact-computation objective inside the shorter budget.

KNOWN-RECIPE covers scratchpads, programs and mixed data; AGENT-DEMONSTRATED evidence concerns neighboring training. attack_basis=LITERATURE-ONLY. Twelve hours must cover lawful labels, objective implementation, full-cost learning curves and code/language validation. Transfer to this learner remains assumed; a compiler that wins legally must receive its reward.

ANCHORED ESTIMATED modes 0.29/0.50/0.68 have probabilities 0.30/0.60/0.10, encoding insufficient legal supervision, useful objective integration and rare robust synthesis. ESTIMATED single=0.30×0.29+0.60×0.50+0.10×0.68=0.46, range 0.29–0.68; bo4=0.68−0.18×0.90^4−0.21×0.30^4=0.56; pass@4=1−0.90^4=0.34 with p=0.10; ub95=0.68. Independent attempt assumptions concern objective discovery and training seeds, not oracle access to hidden answers.

## 5. Verdict under the kill lines
The section-4 recipe re-estimate is CUT at ESTIMATED bo4=0.78. Headline ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; bo4 is ESTIMATED 0.04 below its line. PoT's measured abstraction failures and the objective-channel mismatch weaken the old near-saturation claim. Before retention, freeze whether training data may change and measure an interpreter-emission floor under the same language constraint; the current contract does not establish either safe passage or a demonstrated kill.

## 6. Redesign
Cause (c): the executable-program output delegates the capability the title intends to study. REDESIGNABLE through an explicit product change to model-native exact numeracy: deploy the trained model to emit a bounded numeral answer, optionally with metered token scratchpad, with no external execution in the deployed path. Tool-free arithmetic inside a general language model is valuable for offline inference and numerical consistency. This is a substantive interface redesign, not a claim that program synthesis was cheating.

Provide all primitive semantics, numeral conventions, tokenizer access and representative composition families during development. Keep a fixed architecture and disclosed executable training corpus; objective code may derive intermediate labels from those legal examples, charging every auxiliary computation. Hold training and evaluation lengths within a demonstrated feasible extrapolation band rather than making numbers arbitrarily large. Preserve language-loss utility and demonstrate an attained stronger joint control. Scratchpad supervision, positional hints available through the permitted interface, carry-state losses and retention-aware weighting all enter the lawful floor.

The strongest re-attack combines these intermediate-state objectives with execution-checked labels and joint loss-weight/curriculum search. It can no longer substitute an interpreter at deployment, but known arithmetic mechanisms may still solve the redesign. Re-attack basis=LITERATURE-ONLY, because autonomous discovery with language retention has not been shown by the fetched agent results.

ESTIMATED scores 0.26/0.43/0.64 at probabilities 0.40/0.53/0.07 produce single=0.40×0.26+0.53×0.43+0.07×0.64=0.38, range 0.26–0.64; bo4=0.64−0.21×0.93^4−0.17×0.40^4=0.48; pass@4=1−0.93^4=0.25; ub95=0.64. Risks include ordinary scratchpads generalizing universally, or an objective-only architecture lacking attainable reserve. Either outcome must be resolved with controls rather than stricter output restrictions.

Decisive-check GPU-h ESTIMATED: a 1.3B mixed-language learner, five objective arms, three seeds, ten hours per single-H100 run costs 5×3×10×1=150.00. ESTIMATED complete numeral/language evaluation adds 24.00 and auxiliary-FLOP calibration 6.00, totaling 180.00 H100 GPU-h. The full trial length, rather than a proxy-only win, must demonstrate retention; no training ran in this audit.

## 7. Measurement status
Rollouts UNMEASURED (planned legal-objective comparisons with executed-program and direct-answer controls). Grader noise UNMEASURED (planned repeated learner seeds and exact parser checks). Score ladder UNMEASURED (planned program imitation, scratchpad/state supervision and attainable joint numeracy-language objective).

## Audit record
id: C040
old_verdict: CUT
evidence_grade: ASSUMED
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.77
old_bo4: 0.85
old_pass4: 0.95
old_ub95: 0.97
new_single: 0.65
new_single_range: 0.42-0.83
new_bo4: 0.78
new_pass4: 1.00
new_ub95: 0.83
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: c
redesign_status: REDESIGNABLE
redesign_oneline: Evaluate model-native exact numeral answers with metered scratchpads and a fixed legal objective-training corpus while retaining language utility.
redesign_single: 0.38
redesign_bo4: 0.48
redesign_pass4: 0.25
redesign_ub95: 0.64
redesign_gpuh: 180
attack_basis: LITERATURE-ONLY
demonstrated_ref: PostTrainBench Lite, GPT-6.2 Astra plus internal training scaffold, 2026; MLE-bench, o1-preview plus AIDE, 2024
gap_to_attack: arithmetic compiler learning with objective-only edits and language retention lacks an agent result
subfield_sota_ref: arithmetic length generalization, Cho et al., 2025; procedural mixed pretraining, Jiang et al., 2026
anchored_single: 0.46
anchored_bo4: 0.56
anchored_pass4: 0.34
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
