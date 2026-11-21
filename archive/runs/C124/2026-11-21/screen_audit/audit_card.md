# C124 — Self-repairing tools that learn when repair evidence is enough — screen audit
## 1. What the screen claimed
The attack paired coding-agent repair with stateful differential tests, minimal rollback, operation adapters and short learning continuations. Old ESTIMATED single/bo4/pass4/ub95 were 0.82/0.89/0.98/0.97; CUT, category TRAIN, because independent replay appeared to make the runner contract easy to restore. References: https://arxiv.org/abs/2405.15793 and https://hypothesis.readthedocs.io/en/latest/stateful.html.

## 2. Evidence audit
SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering — John Yang, 2024 — fetched at the arXiv URL, demonstrates repository repairs with execution feedback, not a learned stopping policy for scientific validation. Stateful tests — HypothesisWorks, 2026 retrieved documentation, original publication year unstated — fetched at the documentation URL, supplies generated state-machine tests. Those tests still need a correct invariant and meaningful scientific state coverage.

Grade: PARTIAL. Ordinary repair has direct evidence, but the high old utility score depends on preserving the actual training operation through checkpoint, retry and data-state transitions. An independent implementation used by the grader is not necessarily an unlimited solver-accessible repair oracle; the original card promises independent validation, not disclosure of that implementation. This distinction materially weakens the screen's attack as written.

## 3. Research done now
- DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories — Josias Moukpe, 2026 — https://arxiv.org/html/2608.19653v1 — fetched — demonstrates agents improving imperfect ML repositories in a comparable wall-clock envelope, raising repair-plus-continuation plausibility; critically broken repositories were screened out.
- MLOps-Bench: Benchmarking AI Agents on Production ML Engineering in Real Repositories — Tran et al., 2026 — https://arxiv.org/html/2610.23506v1 — fetched — supports autonomous lifecycle changes but reports substantial incomplete functionality, pushing against near-universal repair success.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — OpenAI, 2024 — https://arxiv.org/html/2410.07095v1 — fetched — reveals that execution-capable search scaffolds can miss validation, so a successful launch cannot stand in for a trustworthy resumed campaign.

Search focused on current real-repository ML repair evaluations. No source verified adaptive repair-validation stopping on fresh scientific runner incidents with the complete downstream utility endpoint.

## 4. Re-estimated attack
Prospective scores and mixture probabilities are ESTIMATED throughout. A recipe-installed scenario allows 0.29 for localized contract restoration, 0.21 for generated transition checks and 0.15 for economical continuation validation: total 0.65. That assumes useful small-case references are lawful development assets. It does not assume access to the independent hidden checker, and blanket replacement is legal if it preserves required operations.

Take R={0.42,0.67,0.81}, probabilities {0.20,0.60,0.20}. These encode a repaired launch with residual learning damage, a sound ordinary repair and a cheaper broad validation policy. Single=0.20×0.42+0.60×0.67+0.20×0.81=0.65, range 0.42–0.81. Bo4=0.81−0.14×0.80^4−0.25×0.20^4=0.75; p=0.80, pass4=1−0.20^4=1.00 rounded; ub95=0.81. Fault localization and semantic-state coverage drive most spread; subject seeds and timeout placement remain unmeasured. This is less optimistic than the old screen because reference replay does not reveal every scientific invariant.

## 4A. Demonstrated capability and subfield SOTA
Closest verified current production-repair comparator: GPT-5.5/Codex leads the evaluated MLOps-Bench configurations at 31.2% task completion; test pass rate is a separate metric. DeltaML supplies the more relevant research-continuation comparator. Neither establishes global software-repair SOTA, and no published repair-validation-efficiency leaderboard was verified. Anchor the card to independently repaired healthy-runner campaigns, preserving the same newly required operations and charging validation; actual reference utility and R≈1 reserve are UNMEASURED.

Demonstrated result one: GPT-5/ARG on Vivaria reports 49.0% per-run DeltaML success in its twelve-hour allocation, one H100 per task. The target repositories already initialize, so this does not demonstrate recovering a broken runner. Result two: GPT-5.5/Codex's MLOps completion figure above comes from repository lifecycle patches; runtime and hardware are unreported. It verifies code integration capability without scientific continuation equivalence.

KNOWN-RECIPE covers repair, model-based testing and bounded replay. AGENT-DEMONSTRATED evidence reaches pieces of the workflow; the complete fresh-fault validation controller remains LITERATURE-ONLY. In twelve hours an agent must infer the relevant invariant, patch without erasing a new operation, and stop testing only when remaining risk is worth the saved research time.

ANCHORED increments are approximately 0.22 restoration, 0.13 state validation and 0.10 saved continuation budget. Use R={0.19,0.48,0.72}, probabilities {0.28,0.50,0.22}; single=0.45, range 0.19–0.72; bo4=0.72−0.24×0.78^4−0.29×0.28^4=0.63; pass4=1−0.78^4=0.63; ub95=0.72. The larger mean-to-bo4 gap reflects bimodal diagnosis, not a fixed adjustment. Success mass is a task-specific assumption; neither reported benchmark success is copied into this distribution.

## 5. Verdict under the kill lines
Evidence verdict CUT. ANCHORED verdict CUT, UNCHANGED; pass4 binds at ESTIMATED 0.13 above its line, while bo4 exceeds by 0.03. The original near-certain success claim is unsupported, but ordinary faults, flexible repair permissions and a modest successful-diagnosis tail still threaten repeated attempts. This CUT rests on the explicitly assumed transfer probability, not a claimed measured threshold breach.

## 6. Redesign
Cause (a): mature repair and testing capture the routine runner intervention. Supply a healthy versioned runner, differential unit references and a strong repair loop as baseline. Use documented classes of ML state incidents where local operations remain correct but combined resume behavior changes learning: for example sampler progression interacting with accumulation boundaries after restart. Expose the complete operation contract and diagnostic access; let the submitted policy choose affordable state probes and validation depth. Score useful training after repair and all validation costs.

Strongest attack: minimal patch search, stateful invariant generation, differential small runs, then confidence-based continuation. It cannot earn gain simply by restoring startup, and must identify the cross-state learning interaction before paying full continuation cost. ESTIMATED outcomes {0.18,0.41,0.62}, masses {0.27,0.64,0.09}, yield single=0.37; bo4=0.62−0.21×0.91^4−0.23×0.27^4=0.47; pass4=1−0.91^4=0.31; ub95=0.62. Basis LITERATURE-ONLY. REDESIGNABLE; a generic resume-state checksum may still eliminate the intended mechanism, so include it as a control.

Decisive check ESTIMATED 128 H100 GPU-h: 1B subject, 4 policies×2 incident mechanisms×2 seeds×5 hours×1 H100=80; independent healthy/new-operation controls=24; 4B agent repair inference and endpoint repeats=24. Feasibility requires a valid affordable diagnostic; delayed failures alone do not establish research value.

## 7. Measurement status
Rollouts UNMEASURED (planned fault repair and reset continuation attempts). Grader noise UNMEASURED (planned fixed-repair repetitions across learner seeds). Score ladder UNMEASURED (planned retries, minimal repair, component replacement, adaptive validation and healthy-runner control).

## Audit record
id: C124
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.82
old_bo4: 0.89
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.65
new_single_range: 0.42-0.81
new_bo4: 0.75
new_pass4: 1.00
new_ub95: 0.81
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Start from mature repair and learn validation depth for real coupled training-state incidents.
redesign_single: 0.37
redesign_bo4: 0.47
redesign_pass4: 0.31
redesign_ub95: 0.62
redesign_gpuh: 128
attack_basis: LITERATURE-ONLY
demonstrated_ref: DeltaML GPT-5 ARG 2026; MLOps-Bench GPT-5.5 Codex 2026
gap_to_attack: trustworthy repair stopping on fresh scientific-state faults
subfield_sota_ref: MLOps-Bench Codex completion Tran 2026; DeltaML ARG Moukpe 2026
anchored_single: 0.45
anchored_bo4: 0.63
anchored_pass4: 0.63
anchored_ub95: 0.72
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
