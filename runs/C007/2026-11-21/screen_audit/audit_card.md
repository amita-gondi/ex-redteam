# C007 — A loss that preserves counterexample repair — screen audit
## 1. What the screen claimed
The attack inferred valid old tests from specification changes, then combined counterexample likelihood, applicable replay and selective behavioral distillation through the objective channel. Its ESTIMATED single/bo4/pass@4/ub95 were 0.66/0.75/0.84/0.91. CUT, category TRAIN, assumed validity-aware protection removed the major regression gap. URLs:
- https://arxiv.org/abs/1706.08840
- https://github.com/facebookresearch/agem

## 2. Evidence audit
Gradient Episodic Memory for Continual Learning — David Lopez-Paz, 2017, fetched at the arXiv URL — demonstrates episodic constraints against forgetting. Efficient Lifelong Learning with A-GEM — Arslan Chaudhry, 2019, fetched through the official repository — supplies a cheaper implementation and replay controls. These are principally gradient/update interventions; an objective-only learner does not automatically inherit them.

Grade: PARTIAL. Replay and selective protection are defensible ingredients, but the key validity classifier and a loss expressing safe changes to shared code representations are not demonstrated by those sources. Ordinary continual-learning classification neither replaces obsolete specifications nor evaluates composed program repairs. The screen identifies this gap in prose but allocates reward as though the integration were established.

## 3. Research done now
- Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning — Yinjie Wang, 2025 — https://proceedings.nips.cc/paper_files/paper/2025/hash/d38653cdaa8e992549e1e9e1621610d7-Abstract-Conference.html — fetched — CURE demonstrates learned code/test interaction and downstream testing gains. It raises confidence in execution-generated repair supervision, without addressing sequential obsolescence or objective-only retention.
- Keeping Code-Aware LLMs Fresh: Full Refresh, In-Context Deltas, and Incremental Fine-Tuning — Pradeep Kumar Sharma, 2025 — https://arxiv.org/abs/2511.14022 — fetched — Finds that old-aware mixing and delta format matter under code drift. It supports version-aware evidence, but predicts repository paths rather than synthesizing behavior-preserving repairs.
- Learning without Overwriting: A Theory of Self-Distillation and Supervised Fine-Tuning in Continual Reasoning — Shinichi Uemura, 2026 — https://arxiv.org/abs/2610.05200 — fetched — Explains contrasting update interference through a reasoning-graph model. It makes selective distillation plausible and also emphasizes structural assumptions; this theoretical guarantee is not an empirical repair benchmark.
- SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks — Gabriel Orlanski, 2026 — https://arxiv.org/html/2603.24755v1 — fetched — Directly tests evolving code requirements and finds accumulated correctness/structure problems. It cuts against automatic compositional repair, though it tests deployed coding agents rather than loss designers.

Search focused on counterexample training, code drift and regression during repeated edits. Future-dated and non-objective interventions were not used to certify this attack.

## 4. Re-estimated attack
ESTIMATED incremental contributions: 0.21 from current-counterexample supervision, 0.20 from applicable replay, and 0.13 from gated behavioral penalties, suggesting mean 0.54. Shared-representation changes remain costly even if the old-target validity label is correct. Training examples and generated traces must follow the original fixed-data permissions; optimizer projection is not silently added.

Use an ESTIMATED two-mode distribution: R=0.38 with probability 0.60 when selective protection remains local, and R=0.79 with probability 0.40 when a gate generalizes through the edit sequence. This is deliberately bimodal: finding the validity/dependency abstraction changes the whole trajectory. Its internal learner-seed scatter is UNMEASURED and compressed into representative modes.

Single=0.60×0.38+0.40×0.79=0.54, range 0.38–0.79. For independent restarts given one history family, bo4=0.79−0.41×0.60^4=0.74; p=0.40, so pass@4=1−0.60^4=0.87. CDF below the high mode is 0.60, giving ub95=0.79. All are ESTIMATED. The lower mean than the screen reflects objective/interface mismatch; the larger selection jump reflects an abstraction-dependent rather than uniform improvement.

## 4A. Demonstrated capability and subfield SOTA
CURE is the closest strong code/test training system opened: its human-designed procedure reports gains in agentic unit testing and code generation with small models. It establishes attainable improvement, not the maximum on dependent repair sequences. Uemura supplies a structural retention hypothesis. Use these to construct legal loss baselines, then require a same-budget repair objective exceeding their best permitted combination; no published result currently fixes this card's R≈1 or reference reward.

- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched. Reported PostTrainBench Lite gap closure is 74.79% for Astra's training agent, using five hours and one H100. Scaffold details are absent. This supports competent fine-tuning, but provides no dependent-repair objective result.
- SlopCodeBench (Orlanski, 2026, fetched above): Opus 4.6/Claude Code has reported strict checkpoint solve rate 17.2%, averaging 14.4 minutes per checkpoint; no evaluated agent completes an entire problem. Execution hardware allocation is unspecified. It measures the relevant regression hazard, not the ability to train a new repair learner.

KNOWN-RECIPE retention exists; the combined lawful loss is not AGENT-DEMONSTRATED. Basis LITERATURE-ONLY. The missing twelve-hour capability is constructing and validating a semantic gate whose protections remain useful after later dependent edits.

ANCHORED ESTIMATED modes are 0.38 with mass 0.87 and 0.69 with mass 0.13. The ordinary mode retains useful fine-tuning; the rarer one integrates a transferable loss. Single=0.87×0.38+0.13×0.69=0.42, range 0.38–0.69; bo4=0.69−0.31×0.87^4=0.51; pass@4=1−0.87^4=0.43; ub95=0.69. Mode probabilities and their normalized heights are assumptions, not transformed benchmark percentages.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT, ESTIMATED bo4 exceeds the line by 0.14. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL. Its ESTIMATED bo4 margin is 0.09 and pass@4 margin 0.07. Demonstrated fine-tuning raises the basic attack, while iterative-code evidence undermines assumed integration. Native anchors and a compositional mechanism distinct from contract migration are mandatory conditions; this judgment rests on assumption.

## 6. Redesign
Cause (a): conventional replay/regularization may repair simple regressions. The concrete condition is a sequence where a shared abstraction serves both changed and retained requirements, with the entire validity predicate disclosed. Require repair learning on new compositions of those requirements after both branches have changed. Hold training examples and optimizer work equal across losses, and use independently implemented invariant tests. This preserves real code-model adaptation R&D and makes obsolete-test classification insufficient by itself.

Attack the revision with validity-gated replay, affected-input distillation, execution-generated counterexamples where permitted, and joint coefficient search. Re-attack basis LITERATURE-ONLY. It falls short only if shared representation repair needs a learned structural penalty beyond per-test applicability; demonstrate that against the complete legal stack. If the sequence simply recodes tool-contract migration, the reported MODERATE T08 overlap becomes a duplicate concern, not evidence of novelty.

ESTIMATED revised modes {0.34,0.64}, masses {0.93,0.07}, distinguish generic preservation from discovery of the structural loss. Single=0.93×0.34+0.07×0.64=0.36; bo4=0.64−0.30×0.93^4=0.42; pass@4=1−0.93^4=0.25; ub95=0.64. REDESIGNABLE; residual risks are a standard distillation gate solving the shared abstraction, or no feasible loss realizing it. Pilot GPU-h ESTIMATED: 1B learner, five losses×three seeds×twelve H100-hours, plus twenty-four H100-hours for repair generation and evaluation: 5×3×12+24=204.

## 7. Measurement status
Rollouts UNMEASURED (planned objective-restricted attacks over independently authored edit chains). Grader noise UNMEASURED (planned paired learner seeds and frozen executable invariant suites). Score ladder UNMEASURED (planned new-only, uniform replay/KL, validity-aware loss, structural objective and stronger legal retention control).

## Audit record
id: C007
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.66
old_bo4: 0.75
old_pass4: 0.84
old_ub95: 0.91
new_single: 0.54
new_single_range: 0.38-0.79
new_bo4: 0.74
new_pass4: 0.87
new_ub95: 0.79
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Expose validity fully and require objective-driven repair of shared abstractions across later program compositions.
redesign_single: 0.36
redesign_bo4: 0.42
redesign_pass4: 0.25
redesign_ub95: 0.64
redesign_gpuh: 204
attack_basis: LITERATURE-ONLY
demonstrated_ref: PostTrainBench Lite, GPT-6.2 Astra internal training agent, 2026; SlopCodeBench, Opus 4.6 Claude Code, 2026
gap_to_attack: Discover a validity-aware loss that preserves dependent repairs through subsequent updates
subfield_sota_ref: Code/test interaction training, Wang CURE, 2025; dependent-sequence optimum unidentified
anchored_single: 0.42
anchored_bo4: 0.51
anchored_pass4: 0.43
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
