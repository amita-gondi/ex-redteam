# C101 — Explore a training loss surface when every initial run fails — screen audit
## 1. What the screen claimed
DreamCoder-style abstraction, counterexample-guided synthesis and STaR-style verified self-training supplied demonstrations before curriculum RL. The screen's ESTIMATED single/bo4/pass@4/ub95 were 0.64/0.75/0.84/0.92; it CUT in category DUP because v3 02A already learns transferable signals beyond a policy's successful frontier. Listed URLs:
- https://arxiv.org/abs/2006.08381
- https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm
- https://arxiv.org/abs/2203.14465

## 2. Evidence audit
DreamCoder demonstrates learned program abstractions, the synthesis lecture explains CEGIS, and STaR supports iterative reasoning supervision. None establishes that backward-generated demonstrations in a new language produce transferable long programs within the learner and generation budget. CEGIS can solve training specifications while leaving amortized neural transfer unresolved.

Grade: PARTIAL. The escape from an empty learner-success buffer is a lawful and serious route; its combined downstream score was not demonstrated. The duplicate claim can be checked independently: the opened 02A statement and interface cover objective changes, intermediate supervision, transfer schedules and executable compositional families.

## 3. Research done now
- *DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning* — Kevin Ellis et al., 2020 — https://arxiv.org/abs/2006.08381 — fetched — Library learning weakens the claim that generic exploration is the only baseline; its structured domains do not establish this long-code transfer result.
- *Introduction to Program Synthesis, Lecture 10* — Armando Solar-Lezama, 2018 page copyright, hosted in a 2020 course — https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm — fetched — Explains counterexample-guided search, not autonomous training-signal discovery or a budgeted capability measurement.
- *STaR: Bootstrapping Reasoning With Reasoning* — Eric Zelikman et al., 2022 — https://arxiv.org/abs/2203.14465 — fetched — Correct-answer filtering supports distillation, but does not prove that available partial programs teach extendable prefixes.
- *Absolute Zero: Reinforced Self-play Reasoning with Zero Data* — Andrew Zhao et al., 2025 — https://arxiv.org/html/2505.03335v3 — fetched — Code-executor-verified self-play improves reasoning without external task data, strengthening the legal synthesis route. Its human-designed training procedure is not an agent inventing that procedure during a task.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — Shows agents selecting and executing post-training strategies; does not demonstrate escaping all-failure long synthesis with new language semantics.
- *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search* — Yutaro Yamada et al., 2025 — https://arxiv.org/html/2504.08066v1 — fetched — Its compositional-generalization experiment reports an ineffective proposed regularizer, directly cautioning against crediting a plausible precursor as a successful learning mechanism.

## 4. Re-estimated attack
In ESTIMATED reward units, legal short-solution construction contributes 0.23, curriculum and abstraction reuse 0.18, and execution-trace/self-training refinement 0.14: single 0.55. These sequential contributions assume that generated examples fit the new language and charge all search. The unclaimed remainder is long-horizon transfer, especially separating extendable prefixes from superficially promising partial tests.

ESTIMATED scenario probabilities are 0.20 at R=0.24 when demonstrations fail to transfer, 0.55 at 0.56 when curriculum works, and 0.25 at 0.78 when a compact reusable library is discovered. Mean=0.20×0.24+0.55×0.56+0.25×0.78=0.55, range 0.24–0.78. Bo4=0.24+0.32(1−0.20⁴)+0.22(1−0.75⁴)=0.71; p=0.25 implies pass@4=1−0.75⁴=0.68; ub95=0.78. This large best-of-four gap follows from discovering a useful abstraction, unlike a deterministic optimizer import. All four forecasts fall below the screen except where rounding obscures detail, but this recipe-level account still CUTs. Learner-seed and evaluator variance remain unmeasured rather than silently calibrated.

## 4A. Demonstrated capability and subfield SOTA
Absolute Zero is the closest fetched contemporary learning reference: its paper reports strong coding/math generalization from executable self-play, including a leading comparison among its evaluated zero-data models. It is not verified current SOTA for unseen-language long synthesis. R≈1 requires a legal precursor/control that actually improves independent terminal completions on this language family; neither a general coding leaderboard nor a perfect training-program synthesizer anchors that reward.

TrainExplorer with GLM-5.2 improves its aggregate from the base models' 7.53% to 39.02% under ten hours and one 80 GB flagship GPU per task. That demonstrates autonomous training, not construction of novel compositional credit. AI Scientist-v2 uses Claude 3.5 Sonnet for code and GPT-4o for feedback, with a fifteen-hour paper limit; per-paper GPU-hours are unreported. Its accepted compositional-regularization study found no improvement from the intervention. A successful research process can therefore demonstrate a negative learning result, which should lower confidence in an untested precursor attack rather than count as solved C101.

The full synthesis/curriculum integration is KNOWN-RECIPE, not AGENT-DEMONSTRATED under matching feedback and time. attack_basis=LITERATURE-ONLY. The missing autonomous step is identifying an intermediate objective that improves unseen complete programs after training, rather than merely generating more valid easy examples.

ANCHORED ESTIMATED masses: 0.30 at 0.16, 0.62 at 0.40 and 0.08 at 0.66. Single=0.35, range 0.16–0.66; bo4=0.16+0.24(1−0.30⁴)+0.26(1−0.92⁴)=0.47; pass@4=1−0.92⁴=0.28; ub95=0.66. The lower success branch reflects missing transfer evidence, not a measured impossibility. Quantitative forecasts rest on assumptions, and native reward anchors remain open.

## 5. Verdict under the kill lines
Section 4 gives CUT, binding on ESTIMATED bo4 0.71. The ANCHORED numerical distribution would PASS-SCREEN, with bo4 clearance 0.13 and ub95 clearance 0.09. The headline remains CUT, UNCHANGED, because the independently verified STRONG duplicate applies: 02A already changes the signal and supervision schedule for unhinted executable composition. That disposition does not require assuming high autonomous attack competence.

## 6. Redesign
DUPLICATE-STAYS-CUT, class (d): the submitted learning treatment and terminal transfer target are already represented by 02A. Its source explicitly includes executable code among coupled skill families; making the program longer or starting with no successful samples does not define a distinct intervention. Treat this card's all-failure and misleading-prefix cases as useful instance-design hypotheses for that existing task. No replacement task, re-attack numbers or new decisive GPU budget is warranted under the duplicate exception.

## 7. Measurement status
Rollouts UNMEASURED (planned teacher-free synthesis/curriculum and learned-precursor attempts within a consolidated objective task). Grader noise UNMEASURED (planned learner seeds and independently authored executable families). Score ladder UNMEASURED (planned terminal-only, partial-test, verified demonstrations and stronger transferable-signal controls).

## Audit record
id: C101
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.64
old_bo4: 0.75
old_pass4: 0.84
old_ub95: 0.92
new_single: 0.55
new_single_range: 0.24-0.78
new_bo4: 0.71
new_pass4: 0.68
new_ub95: 0.78
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: d
redesign_status: DUPLICATE-STAYS-CUT
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; AI Scientist-v2, Claude 3.5 Sonnet+GPT-4o, 2025
gap_to_attack: discovering precursor signals with verified long-program transfer
subfield_sota_ref: Absolute Zero executable self-play comparison, Zhao et al., 2025
anchored_single: 0.35
anchored_bo4: 0.47
anchored_pass4: 0.28
anchored_ub95: 0.66
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
