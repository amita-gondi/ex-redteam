# C102 — Learn useful failed experiments under sparse scientific feedback — screen audit
## 1. What the screen claimed
The screen combined structured failure summaries, condition-matched retrieval, adapter training and Optuna selection of corpus/memory settings. It CUT under EXP with ESTIMATED single 0.64, bo4 0.73, pass@4 0.82 and ub95 0.88, arguing that ordinary context-sensitive memory could improve downstream experiment selection. Its citations were:
- https://arxiv.org/abs/2303.11366
- https://arxiv.org/abs/2106.09685
- https://arxiv.org/abs/1907.10902

## 2. Evidence audit
Reflexion demonstrates linguistic experience reuse; LoRA makes selective training practical; Optuna offers configuration search. None measures a curated scientific-failure corpus improving a reset agent's executed learning interventions after corpus costs. In particular, remembering that a run failed is not evidence that an agent understands whether the result rules out a mechanism.

Grade: ASSUMED. The load-bearing causal transfer claim exceeded the sources, although each engineering component exists. New scientific-memory evidence makes the gap sharper: recovering the relevant fact and judging whether it is valid for the current decision are distinguishable capabilities.

## 3. Research done now
- *Reflexion: Language Agents with Verbal Reinforcement Learning* — Noah Shinn et al., 2023 — https://arxiv.org/abs/2303.11366 — fetched — Experience summaries can help action, but the reported tasks do not establish scientific null interpretation.
- *LoRA: Low-Rank Adaptation of Large Language Models* — Edward J. Hu et al., 2021 — https://arxiv.org/abs/2106.09685 — fetched — Confirms economical adaptation; it contributes no evidence about which failed experiments should be learned from.
- *Optuna: A Next-generation Hyperparameter Optimization Framework* — Takuya Akiba et al., 2019 — https://arxiv.org/abs/1907.10902 — fetched — Corpus/retrieval settings are searchable, without guaranteeing a predictive development signal for new causal mechanisms.
- *ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory* — Siru Ouyang et al., 2025, revised 2026 — https://arxiv.org/html/2509.25140v2 — fetched — Success-and-failure memory improves web/coding agents, raising the ordinary-memory floor while leaving training-corpus transfer untested.
- *The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory* — Yuexi Pan and Yongchao Chen, 2026 — https://arxiv.org/html/2610.34767v1 — fetched — Explicit governing scientific state beats generic memory views; retrieval alone does not reproduce the gain. This directly challenges the screen's strongest shortcut.
- *Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents* — Lasse B. Strand et al., 2026 — https://arxiv.org/html/2610.08452v1 — fetched — Diagnosis-guided retrieval tuning is demonstrated, but its answer metrics and unreported elapsed campaign time prevent transferring the result wholesale to scientific experimentation.

## 4. Re-estimated attack
The ESTIMATED recipe account allocates 0.16 to removing invalid/duplicate failure records, 0.24 to condition-sensitive retrieval and 0.14 to selective adapter training plus configuration search: single 0.54. These are proposed increments in downstream utility, not independent reward terms. The difficult residual is learning the scope of a null result when conditions, statistical power or intervention exposure change.

Use probabilities 0.25 at R=0.30 for useful housekeeping only, 0.55 at 0.56 for successful conditional reuse and 0.20 at 0.77 for a transferable mechanism abstraction. ESTIMATED mean=0.54, range 0.30–0.77; bo4=0.30+0.26(1−0.25⁴)+0.21(1−0.80⁴)=0.68. Here p=0.20, hence pass@4=1−0.80⁴=0.59; ub95=0.77. This still CUTs but is materially below the old forecast. Variation is mostly whether the corpus supports the right abstraction and whether training preserves it; downstream learner stochasticity and grader noise are not separately measured. A retrieval-only success receives credit only if the allowed data artifact actually changes the reset agent through the declared interface.

## 4A. Demonstrated capability and subfield SOTA
SciValidityBench supplies the closest scientific-memory comparator located: compiling decision-governing state improves validity over generic event memory across model families, and the authors test state interventions. That result is stronger evidence about null interpretation than generic recall benchmarks, but is not a measured optimum for live ML research. The north star must be a lawful corpus whose trained agent improves actual project learning after all costs; no fetched publication anchors that exact R≈1.

ReasoningBank with Gemini-2.5-Pro improves SWE-bench Verified resolve rate from 54.0% without memory to 57.4%; elapsed memory-building time and accelerator-hours are unreported. Its scaffold learns reusable reasoning from successful and failed experiences, but the gain concerns software resolution rather than causal scientific choice. Agentic AutoRAG uses Kimi-K2.5 diagnosis/proposal for thirty-trial searches and reports healthcare exam accuracy 77% versus 71.5% for its strongest compared baseline. GPU count and total elapsed time are unspecified. Diagnosing retrieval versus generation is relevant experience use, but it is not a trained reset researcher interpreting underpowered nulls.

KNOWN-RECIPE covers retrieval and lightweight adaptation. The proposed causal failure-data flywheel itself remains unsupported by comparable AGENT-DEMONSTRATED results; attack_basis=ASSUMED. The twelve-hour gap is constructing valid cross-condition contrasts and validating their downstream learning effect, rather than generating convincing failure explanations.

The ANCHORED ESTIMATED distribution places 0.25 at 0.18, 0.63 at 0.40 and 0.12 at 0.72. Mean=0.38, range 0.18–0.72; bo4=0.18+0.22(1−0.25⁴)+0.32(1−0.88⁴)=0.53; pass@4=1−0.88⁴=0.40; ub95=0.72. The thin high branch preserves the possibility of a very effective memory scheme; lack of a demonstration does not eliminate it. The resulting verdict rests on assumptions about that transfer and the unmeasured utility anchors.

## 5. Verdict under the kill lines
Section 4 remains CUT, binding on bo4 and also crossing pass@4/ub95. The ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL: ESTIMATED ub95 is only 0.03 below its line. SciValidityBench's retrieval-versus-valid-use distinction and the absence of corpus-to-live-research demonstrations overturn the old confident kill, without establishing a safe margin.

## 6. Redesign
Class (b), with data validity as the key scientific uncertainty. REDESIGNABLE. Supply trustworthy raw launch status and matched histories where an early null is caused either by insufficient exposure or by a genuinely ineffective mechanism. Provide a lawful, affordable diagnostic with predictive dev support that distinguishes those causes. Permit corpus creation to select and encode diagnostic contrasts, and train the same reset agent for every arm. Fix retrieval permissions explicitly and include raw replay, ReasoningBank-style summaries and scientific-state compilation in the floor.

This makes the combined recipe of deduplication, nearest-condition retrieval, LoRA and Optuna insufficient unless it teaches when to reverse a previous avoidance decision. The mechanism is observable rather than hidden, and a legal diagnostic-aware corpus must demonstrate achievable downstream reserve. Better use of negative scientific evidence is frontier-relevant. Strongest re-attack: compile validity state and distill contrastive intervention choices; its basis is ASSUMED. A compact universal state summary may still solve the family, which would falsify the redesign.

ESTIMATED redesigned masses 0.30 at 0.16, 0.63 at 0.36 and 0.07 at 0.61 give single 0.32; bo4=0.16+0.20(1−0.30⁴)+0.25(1−0.93⁴)=0.42; pass@4=1−0.93⁴=0.25; ub95=0.61. Decisive compute is ESTIMATED 4 corpus arms×2 seeds×2 H100-hours for a 4B adapter learner=16, plus 4×2×3 projects×3 H100-hours for 1B downstream subjects=72, plus 8 evaluation hours: 96 H100 GPU-h. Corpus-generation CPU work must also be metered.

## 7. Measurement status
Rollouts UNMEASURED (planned fresh corpus-building attempts with downstream interventions executed). Grader noise UNMEASURED (planned repeated fixed-corpus training and project seeds). Score ladder UNMEASURED (planned raw replay, conditional memory, validity-state data, reference and stronger legal corpus).

## Audit record
id: C102
old_verdict: CUT
evidence_grade: ASSUMED
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.64
old_bo4: 0.73
old_pass4: 0.82
old_ub95: 0.88
new_single: 0.54
new_single_range: 0.30-0.77
new_bo4: 0.68
new_pass4: 0.59
new_ub95: 0.77
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Train on diagnostic contrasts that distinguish uninformative nulls from ineffective mechanisms and grade live downstream learning.
redesign_single: 0.32
redesign_bo4: 0.42
redesign_pass4: 0.25
redesign_ub95: 0.61
redesign_gpuh: 96
attack_basis: ASSUMED
demonstrated_ref: ReasoningBank, Gemini-2.5-Pro, 2025/2026; Agentic AutoRAG, Kimi-K2.5, 2026
gap_to_attack: failure-corpus training that improves causal choices on actual learning projects
subfield_sota_ref: SciValidityBench scientific-state comparison, Pan and Chen, 2026
anchored_single: 0.38
anchored_bo4: 0.53
anchored_pass4: 0.40
anchored_ub95: 0.72
anchored_verdict: CONDITIONAL
anchored_binding_line: ub95>=0.75
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: ASSUMED
souping_flag: no
