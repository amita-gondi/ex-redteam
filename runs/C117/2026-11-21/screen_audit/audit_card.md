# C117 — A data flywheel that retires solved failure modes — screen audit
## 1. What the screen claimed
The DATA CUT combined checkpoint-refreshed competence, mechanism-stratified replay, interference prediction and conservative retirement, claiming that this covers redundant generation and forgotten prerequisites. ESTIMATED single/bo4/pass@4/ub95 were 0.69/0.78/0.91/0.92. The URLs were https://proceedings.mlr.press/v139/jiang21b.html, https://arxiv.org/abs/1908.04742 and https://arxiv.org/abs/1706.08840.
## 2. Evidence audit
Prioritized Level Replay — Minqi Jiang, 2021 — first URL, fetched, selects levels using estimated learning potential. Online Continual Learning with Maximally Interfered Retrieval — Rahaf Aljundi, 2019 — second URL, fetched, selects replay examples threatened by imminent updates. Gradient Episodic Memory for Continual Learning — David Lopez-Paz, 2017, revised 2022 — third URL, fetched, supplies a retention mechanism. These are real methods, but neither their conjunction nor their transfer to repair-agent data generation is demonstrated by those sources.

Grade PARTIAL. The old attack has plausible selection and retention ingredients; generating genuinely new bug mechanisms and predicting delayed precursor value are unverified. One-step gradient interference can miss a prerequisite whose immediate loss stays flat. A replay buffer's existence does not establish the attainable exact repair gains after several coding-learning rounds.
## 3. Research done now
- SWE-smith: Scaling Data for Software Engineering Agents — John Yang, 2025 — https://arxiv.org/abs/2504.21798 — fetched — executable bug/task synthesis trains a 32B repair agent, strengthening the generation floor but not autonomous retirement policy discovery.
- CoderForge-Preview — Together AI, 2026 — https://www.together.ai/blog/coderforge-preview — fetched — test-verified multi-source trajectories deliver strong repair results, including a 4B student; the enormous generation ledger weakens budget comparability.
- How to Learn from Negative Trajectories in Coding Agents — Minseon Kim/Microsoft Research, 2026 — https://microsoft.github.io/debug-gym/blog/2026/08/negative-pi/ — fetched — failed trajectories still contain useful factual corrections, warning against equating a solved or unsuccessful category with useless support.
- Can Generalist Agents Automate Data Curation? — Feiyang Kang, 2026 — https://arxiv.org/html/2606.04261v1 — fetched — autonomous subset selection improves learning, but fixed-pool curation does not validate checkpoint-dependent generation and retirement.
- TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration — Xuannan Liu, 2026 — https://arxiv.org/html/2611.20430v1 — fetched — shows an agent selecting and executing training strategies on small base models within a comparable wall-clock budget, raising the practical attack.

Search focused on executable coding-data synthesis, negative trajectories and multi-round learning. One SWE-Gym PDF timed out and is excluded from cited-source counts. Five additions and three screen works were fetched successfully.
## 4. Re-estimated attack
Construct valid repair examples with repository tests, refresh competence after each checkpoint, reduce solved-family generation smoothly, and keep mechanism-stratified examples selected through candidate-update interference. ESTIMATED typical contributions are 0.25 from eliminating duplicate solved work, 0.19 from failure-directed synthesis and 0.14 from retained support, totaling 0.58. They refer to useful final repair gains after the strongest fixed combined floor. There is no reward for retirement itself, and native baseline/ceiling anchors remain absent.

ESTIMATED outcomes 0.37/0.58/0.80 at masses 0.23/0.57/0.20 describe redundant or forgetting-prone training, useful ordinary selection and successful support-aware generation. Mean=0.58, range 0.37–0.80; bo4=0.80−0.22×0.80^4−0.21×0.23^4=0.71. Only the high case clears the success threshold, giving p=0.20 and pass@4=1−0.80^4=0.59; q95=0.80. Major spread comes from discovering the correct support granularity and composition generator before paying for multiple training rounds. Generator randomness and learner seeds contribute; this is not grader noise masquerading as search diversity. The old 0.69 mean is not warranted, although a literature-conditional repeated-search kill remains.
## 4A. Demonstrated capability and subfield SOTA
SWE-smith's reported 40.2% SWE-bench Verified pass@1 is an established synthesis-to-training comparator. The newer CoderForge-Preview report gives 59.4% for its 32B model and 43.0% for its 4B student. These are the strongest verified directly relevant data-pipeline results located, not a claim of universal current coding-agent leadership. Its generation uses Qwen3-Coder-480B and millions of API completions: that budget cannot be silently imported into the task. The north star should be a feasible same-budget repair-learning trajectory exceeding static verified corpora plus progress/replay controls; public SWE-bench scores do not define its R≈1.

Two agent demonstrations inform the automation discount. TrainExplorer's GLM-5.2 plan/decouple scaffold, built on Claude Code, reaches 59.04 HumanEval averaged across four base models under ten hours and one 80GB flagship GPU per configuration. This supports useful code post-training, not successive repository-repair retirement. Curation-Bench's Opus 4.7/Claude Code obtains 33.7 versus ICONS 33.3 using ten data-selection iterations and one A100 per LLaVA-7B training run. Overall session duration is unspecified. That demonstrates automated selection with training feedback, but no bug synthesis, changing-checkpoint support or delayed retention.

KNOWN-RECIPE covers executable synthesis, current-competence sampling and interference replay. AGENT-DEMONSTRATED is missing for their complete multi-round composition under twelve hours. attack_basis=LITERATURE-ONLY. The agent must still choose a semantic mechanism partition, make economical retirement decisions and validate future combined bugs without merely measuring current success.

ANCHORED ESTIMATED scores 0.29/0.51/0.72 have masses 0.29/0.60/0.11. Typical utility credits become 0.23 redundancy removal, 0.17 synthesis and 0.11 verified retention. Mean=0.47, range 0.29–0.72; bo4=0.72−0.21×0.89^4−0.22×0.29^4=0.59; pass@4=1−0.89^4=0.37; q95=0.72. The masses are explicit integration forecasts, not experimentally estimated transition probabilities. This verdict rests on assumption about autonomous transfer, with the optimistic tail retained because code-data and training components demonstrably work.
## 5. Verdict under the kill lines
Section 4 gives CUT, binding bo4 by about 0.11. ANCHORED verdict CONDITIONAL, FLIPPED CUT→CONDITIONAL: bo4 margin is only about 0.01 and ub95 margin 0.03. The flip follows missing multi-round autonomous evidence, while CoderForge and TrainExplorer prevent dismissing the known recipe. Concrete delayed prerequisite dependence must replace the underspecified claim that some solved bugs remain useful.
## 6. Redesign
Class (a), data-generation and continual-learning stack. REDESIGNABLE. Use real repair histories with executable bug compositions in which several individually mastered precursor families support distinct later repairs. Preserve ordinary token/context/training costs and allow unlimited logical replay policies within those actual costs; do not impose an arbitrary tiny buffer. Dev histories should expose the same kinds of dependency reversals as private sequences, with affordable intervention probes. A nonuniform support-preserving reference must beat smooth downweighting and a broad fixed corpus before launch.

The strongest re-attack joins verified bug synthesis, refreshed competence, interference scoring and a conservative replay reservoir. It stops capturing most utility if current success and one-update interference cannot identify which precursor supports a later composition, while replaying all examples spends useful training exposure inefficiently. This is a real frontier synthetic-data allocation problem. Residual risk: broad generative replay or a static curriculum may cheaply preserve all necessary mechanisms; those remain legal and would refute the task's headroom.

Redesign basis LITERATURE-ONLY. ESTIMATED mixture 0.24/0.42/0.65 with probabilities 0.30/0.61/0.09 yields mean 0.39; bo4=0.65−0.23×0.91^4−0.18×0.30^4=0.49; pass@4=1−0.91^4=0.31; q95=0.65. ESTIMATED decisive budget: 4B coding agent with adapter continuation, four flywheels × two seeds × three rounds × six hours × one H100=144 GPU-h; verified generation and interference probes=48; independent combined-bug/retention evaluation=32; repeated grades=16. Total 240 H100 GPU-h. This is a falsification pilot, not a measured saturation study.
## 7. Measurement status
Rollouts UNMEASURED (planned: full independent flywheel-development attempts). Grader noise UNMEASURED (planned: fixed-policy generation/retraining and composed-bug repeats). Score ladder UNMEASURED (planned: frozen corpus, current-competence sampling, smooth retirement, interference replay and stronger dependency-aware support allocation).
## Audit record
id: C117
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.69
old_bo4: 0.78
old_pass4: 0.91
old_ub95: 0.92
new_single: 0.58
new_single_range: 0.37-0.80
new_bo4: 0.71
new_pass4: 0.59
new_ub95: 0.80
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Test delayed precursor support under realistic exposure costs with feasible dependency-aware retention and static-corpus controls.
redesign_single: 0.39
redesign_bo4: 0.49
redesign_pass4: 0.31
redesign_ub95: 0.65
redesign_gpuh: 240
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; Curation-Bench, Opus 4.7 Claude Code, 2026
gap_to_attack: autonomous coding-data generation and retirement across delayed support dependencies
subfield_sota_ref: CoderForge-Preview 59.4% 32B and 43.0% 4B, Together AI, 2026
anchored_single: 0.47
anchored_bo4: 0.59
anchored_pass4: 0.37
anchored_ub95: 0.72
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
