# C110 — A benchmark generator that must survive its own learner's progress — screen audit
## 1. What the screen claimed
The old CUT in DATA treated learning-progress replay, ACCEL editing, prerequisite retention and transfer probes as sufficient adaptation to the learner's progress. ESTIMATED single/bo4/pass@4/ub95 were 0.63/0.73/0.82/0.89. The cited URLs were https://arxiv.org/abs/2010.03934 and https://arxiv.org/abs/2203.01302.
## 2. Evidence audit
Prioritized Level Replay — Minqi Jiang, 2020, revised 2021 — first URL — fetched, demonstrates changing level selection as policy competence changes. Evolving Curricula with Regret-Based Environment Design — Jack Parker-Holder, 2022, revised 2023 — second URL — fetched, supports editing levels near a learning frontier. Those experiments establish adaptive curricula, but not a language-model researcher modifying a causal-program generator, then validating its usefulness after an abstraction transition.

Grade PARTIAL. The screen correctly identified that nonstationary competence is already addressed by standard methods. However, causal operator representations, useful prerequisite detection and transfer-sensitive selection were additional proposed components, not consequences established by the two cited results. No old source measured their autonomous integration cost.
## 3. Research done now
- Absolute Zero: Reinforced Self-play Reasoning with Zero Data — Andrew Zhao, 2025 — https://arxiv.org/abs/2505.03335 — fetched — code execution validates self-proposed reasoning problems, materially strengthening the executable generator baseline.
- R-Zero: Self-Evolving Reasoning LLM from Zero Data — Chengsong Huang, 2025, revised 2026 — https://arxiv.org/abs/2508.05004 — fetched — challenger/solver co-evolution produces downstream reasoning gains; this is closer than level replay, though human-engineered.
- Questioning the Questions: Sustaining Self-Evolution in Reasoning Models — Jinyuan Li, 2026 — https://arxiv.org/html/2610.04299v2 — fetched — invalid and repeated questions can collapse self-training; validity and novelty feedback improve sustained learning, supporting both a stronger floor and a real remaining problem.
- Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents — Xing Zhang, 2026 — https://arxiv.org/html/2607.12790v1 — fetched — coupled metric/skill improvement is possible, but anchor discipline and repair limit transfer to autonomous generator research.
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search — Yutaro Yamada, 2025 — https://arxiv.org/html/2504.08066v1 — fetched — autonomous experiment trees can yield research, without a demonstrated twelve-hour curriculum redesign.

Search targeted zero-data co-evolution and repeated-round collapse. These five new publications and both historical sources were opened, with negative findings retained.
## 4. Re-estimated attack
All utility allocations and outcome probabilities below are ESTIMATED. Replace the old generic level editor with executable self-play, a current-checkpoint challenger, validity/novelty scoring and a prerequisite reservoir. Central contributions above the provisional floor are 0.25 executable task coverage, 0.20 progress-conditioned generation and 0.13 retention/transfer selection, totaling 0.58. Unmeasured overlap between these contributions means they are a reasoning decomposition, not separate grader subrewards. Costs include rejected programs and reference execution.

ESTIMATED scores 0.36/0.58/0.81 have masses 0.22/0.53/0.25. A stalled generator, useful local adaptation and sustained transferable generation are qualitatively different outcomes. Mean=0.59, range 0.36–0.81; bo4=0.81−0.23×0.75^4−0.22×0.22^4=0.74; pass@4=1−0.75^4=0.68 with p=0.25; q95=0.81. Generator collapse and learner seed determine which regime is reached. New literature strengthens the recipe but exposes why reward cannot follow complexity labels. Relative to the screen, the mean falls modestly while search tails remain dangerous.
## 4A. Demonstrated capability and subfield SOTA
The appropriate north-star comparator is sustained self-evolution, not simply longer generated code. R-Zero reports Qwen3-4B gains of 6.49 on mathematical and 7.54 on general reasoning; Absolute Zero supplies executable verification. R-Quest's validity/novelty treatment is the newer sustained-round comparator located. None establishes a universal causal-program leaderboard winner, so R≈1 must come from a same-budget stronger generator replayed through the actual learner transition. Public reasoning gains cannot fix that reward scale.

Two demonstrations address different parts of this research chain. Double Ratchet uses Opus 4.7 for skill and metric roles, interleaving metric phases with 100 skill rounds; reported retained lift is 88–110% of oracle-driven improvement. Wall time and GPU consumption are unreported, and unaided repair status is unverified. Its solver is a direct model call, not a newly trained learner. AI Scientist-v2 combines Sonnet 3.5 code generation with GPT-4o feedback in agentic tree search, capped at fifteen hours; one of three selected workshop submissions passed review. Accelerator totals were not established from the fetched paper. That is research-process evidence, not a successful generator transition.

KNOWN-RECIPE is now strong for self-generated curricula; AGENT-DEMONSTRATED does not cover autonomously adapting this generator and validating causal transfer in twelve hours. Basis LITERATURE-ONLY. The remaining unaided work is recognizing when learning progress ceases to predict future teaching value, then making an economical corrective intervention.

ANCHORED ESTIMATED scenarios: 0.24 (0.22), 0.49 (0.65), 0.73 (0.13). Central credits become 0.23 valid coverage, 0.17 adaptation and 0.09 validated delayed transfer. Mean=0.47, range 0.24–0.73; bo4=0.73−0.24×0.87^4−0.25×0.22^4=0.59; pass@4=1−0.87^4=0.43; q95=0.73. The high-case frequency is expressly assumed; no benchmark reports it for this task.
## 5. Verdict under the kill lines
Evidence re-estimate CUT, bo4 0.14 above threshold. ANCHORED verdict CONDITIONAL, FLIPPED CUT→CONDITIONAL: bo4 margin is about 0.01 and ub95 margin 0.02. The new self-play literature preserves saturation risk, while research-agent demonstrations fail to establish the complete budget-matched attack. The design must instantiate delayed teaching value rather than rely on the phrase “learner progress.”
## 6. Redesign
Kill cause (a), standard adaptive-data/RL techniques; REDESIGNABLE. Build causal-program families in which a reusable abstraction changes which decomposition is instructive. Provide actual before/after learner checkpoints and dev transfer tasks exhibiting the same interaction. A previously easy primitive can become useful again when composed with a newly learned abstraction; direct component success must therefore disagree with measured subsequent transfer. Keep executable labels, legal reference solving and a realistic training budget.

The strongest re-attack is executable self-play plus validity/novelty reward, retained prerequisites and transfer-probe selection. Merely targeting current failure or replaying past high-regret examples does not determine the value of an intermediate decomposition after the learner changes. A reference must demonstrate that the interaction is learnable and that its gain survives the combined baseline, rather than earning extra points for novelty. This capability matters for frontier synthetic-data pipelines. Main risk: sufficiently diverse static programs may already cover the relevant bridge.

Redesign basis LITERATURE-ONLY. ESTIMATED scores 0.25/0.44/0.66 with masses 0.31/0.60/0.09 yield mean 0.40; bo4=0.66−0.22×0.91^4−0.19×0.31^4=0.51; pass@4=1−0.91^4=0.31; q95=0.66. ESTIMATED decisive check: 1B inherited learner, four generators × three seeds × sixteen hours × one H100=192 GPU-h; generating/checking programs=24; disjoint transfer and retention=24; longer continuation of selected arms=16. Total 256 H100 GPU-h. This tests one genuine transition, not an entire saturation panel.
## 7. Measurement status
Rollouts UNMEASURED (planned: independent generator edits through complete learner updates). Grader noise UNMEASURED (planned: fixed-generator seeds and repeated causal-program draws). Score ladder UNMEASURED (planned: static coverage, PLR/ACCEL, executable self-play, novelty-aware generation and delayed-transfer reference).
## Audit record
id: C110
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.63
old_bo4: 0.73
old_pass4: 0.82
old_ub95: 0.89
new_single: 0.59
new_single_range: 0.36-0.81
new_bo4: 0.74
new_pass4: 0.68
new_ub95: 0.81
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Instantiate checkpoint-dependent causal decomposition value and score later transfer under equal generation cost.
redesign_single: 0.40
redesign_bo4: 0.51
redesign_pass4: 0.31
redesign_ub95: 0.66
redesign_gpuh: 256
attack_basis: LITERATURE-ONLY
demonstrated_ref: Double Ratchet, Opus 4.7, 2026; AI Scientist-v2, Sonnet 3.5 and GPT-4o, 2025
gap_to_attack: validated delayed teaching-value adaptation after learner transition
subfield_sota_ref: Absolute Zero, Zhao, 2025; R-Zero, Huang, 2025/2026; R-Quest, Li, 2026
anchored_single: 0.47
anchored_bo4: 0.59
anchored_pass4: 0.43
anchored_ub95: 0.73
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
