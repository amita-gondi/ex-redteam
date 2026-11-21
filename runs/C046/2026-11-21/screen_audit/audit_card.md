# C046 — Pretrain a model that can change its own activation budget — screen audit
## 1. What the screen claimed
Layer dropout, shared exits, depth-conditioned distillation, transition curricula and explicit handling of missing historical states formed the old combined attack. The screen assigned ESTIMATED single/bo4/pass@4/ub95 of 0.68/0.77/0.87/0.93 and CUT, category TRAIN, because elastic-depth training already addresses much of the mechanism. Its sources were:
- https://arxiv.org/abs/2404.16710
- https://arxiv.org/abs/2207.07061

## 2. Evidence audit
LayerSkip supports shared-exit training, but its self-speculative verification cannot be imported without charging deeper verification work. CALM directly discusses missing representations after per-token early exits, making this a better-supported attack than generic distillation alone. Neither source establishes autonomous integration under externally imposed depth traces or a reference-normalized reward on C046. Grade PARTIAL: the transition problem has published solutions, yet their applicability under the exact active-FLOP contract needs testing.

## 3. Research done now
All task scores, run probabilities and proposed pilot costs here are ESTIMATED; the published demonstrations are external evidence.
- LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding — Mostafa Elhoushi et al., 2024 — https://arxiv.org/abs/2404.16710 — fetched — Its early-layer accuracy training strengthens the elastic floor. Reported speculative speedups do not establish compliance with a hard shallow-depth interval.
- Confident Adaptive Language Modeling — Tal Schuster et al., 2022 — https://arxiv.org/abs/2207.07061 — fetched — Missing earlier-token hidden states are explicitly addressed, so abrupt resumed depth cannot be described as an unexplored problem.
- ADEPT: Adaptive Dynamic Early-Exit Process for Transformers — Sangmin Yoo et al., 2026 — https://arxiv.org/abs/2601.03700 — fetched — Dynamic exits in both prefill and generation extend the relevant baseline beyond old independent-depth training; external availability constraints remain a mismatch.
- River-LLM: Large Language Model Seamless Exit Based on KV Share — Yingtao Shen and An Zou, 2026 — https://aclanthology.org/2026.acl-long.1746/ — fetched — A lightweight shared-cache path maintains historical states and yields practical generation speedups. This substantially raises the attack against an unspecified missing-cache defect, provided that path is legal and metered.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — Profiling-guided agents demonstrate real low-level performance optimization, supporting implementation of efficient conversion paths, but not learning their semantic sufficiency.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — The NanoGPT result shows autonomous training-loop improvement within a short GPU budget. It provides evidence for experimentation, with no variable-depth compatibility evaluation.

## 4. Re-estimated attack
Combine shared-exit training, trace-matched depth dropout, distillation and cache-preserving exit machinery. Probe all allowed abrupt switches, then optimize depth sampling and legal projection/backfill against complete loss and executed FLOPs. Above a measured elastic baseline, ESTIMATED reward contributions are 0.15 from better transition exposure, 0.29 from historical-state handling and 0.18 from joint alignment/schedule selection, totaling 0.62. The large state contribution depends on the original card not already incorporating current cache-preserving methods into its floor.

Literature-level scenarios R={0.40,0.63,0.81}, mass={0.20,0.60,0.20}, reflect an illegal/ineffective cache shortcut, competent integration, or strong legal cache sharing. State-path legality and learned transition robustness dominate variation; generation traces and learner seeds add smaller uncertainty. ESTIMATED single=0.62, range 0.40–0.81; bo4=0.81−0.18×0.80^4−0.23×0.20^4=0.74. With p=0.80, pass@4=1−0.20^4=1.00 after rounding; ub95=0.81. The new human-recipe forecast is below the old single estimate while retaining a severe repeated-search risk, now connected to explicit integration outcomes.

## 4A. Demonstrated capability and subfield SOTA
Subfield reference: River-LLM reports 1.71–2.16× practical speedup on mathematical reasoning and code generation while retaining high generation quality. ADEPT and CALM address complementary dynamic-exit/cache issues. These are strong contemporary controls, not a proven global optimum under forced depth traces. C046 must reproduce their legal pieces at its allowed architecture interface, charge every shared-cache operation, and set the stronger reference from a measured native loss/FLOP frontier. The current files do not supply that frontier.

For agent capability, PyTorch demonstrates an Opus-4.5 KernelAgent case with four optimization workers over eight rounds on H100, improving a matrix-vector kernel to 1.95 ms against a 2.09 ms compiled baseline. Its total wall time is not disclosed. This supports optimizing a known conversion implementation, not discovering a representation that preserves missing information. OpenAI's Astra training agent saved 42.87% on NanoGPT using two hours and one H100; scaffold details are incomplete. That demonstrates useful empirical training edits, but its scalar loss target does not require state transfer after a shallow interval.

The literature gives a KNOWN-RECIPE for ordinary early-exit continuity; no fetched agent independently trains and validates forced-depth continuity at comparable budget. attack_basis=LITERATURE-ONLY. Twelve-hour work still includes legality analysis, adaptation of cache paths and complete mixed-history training. The forecast's elevated middle branch reflects how closely River-LLM targets the mechanism, rather than calling its human result an agent success.

ANCHORED R={0.35,0.56,0.73} with probabilities {0.15,0.65,0.20}: ESTIMATED single=0.56, range 0.35–0.73; bo4=0.73−0.17×0.80^4−0.21×0.15^4=0.66; pass@4=1−0.80^4=0.59; ub95=0.73. The 0.20 successful-integration mass is an explicit assumption; source metrics are not mapped directly to normalized task reward.

## 5. Verdict under the kill lines
Section 4 and the ANCHORED result both give CUT, UNCHANGED. Anchored bo4 exceeds its line by 0.06 and pass@4 by 0.09; the upper percentile remains 0.02 below its separate limit. The key new evidence is a current cache-preserving exit method, which makes ordinary missing-state repair a plausible sufficient recipe. The cut remains assumption-dependent because autonomous training integration and native anchors are unmeasured.

## 6. Redesign
Cause (a), established elastic computation and cache maintenance; REDESIGNABLE. Begin with CALM/LayerSkip-style trace training and a fully charged cache-sharing path. Evaluate recoverable long-context dependencies where an early token's fine-grained information must be compressed during a shallow interval and later combined with newly observed content. Permit a learned common-state summary and state translator within the original memory and activation budget; supply dev examples with the same dependency structure and all availability traces. Demonstrate a legal stronger summary-learning control before claiming headroom.

Layer dropout, static projection, generic cache sharing and trace oversampling now form the floor. They preserve continuity but do not automatically optimize which information a constrained common state should retain for subsequent compositions. A frontier lab would want such learned state portability for elastic serving. The strongest re-attack distills a task-aware summary and trains transition-specific translators; it may still saturate the task, particularly if simple lower-layer states are sufficient. Impossible information recovery is excluded through the capacity-matched feasibility control.

Redesign basis LITERATURE-ONLY. ESTIMATED R={0.24,0.42,0.61}, probability={0.25,0.65,0.10}: single=0.39, bo4=0.61−0.19×0.90^4−0.18×0.25^4=0.48, pass@4=0.34, ub95=0.61. ESTIMATED decisive check 280 H100 GPU-h: 1B subject, four state/training arms × two seeds × twenty-eight hours × one H100=224; teacher/summary preparation adds 24 and switch-trace evaluation 32 GPU-h. These comparisons must show native reserve rather than magnifying negligible transition loss.

## 7. Measurement status
Rollouts UNMEASURED (planned end-to-end elastic training under fresh availability traces). Grader noise UNMEASURED (planned switch-history repeats across learner seeds). Score ladder UNMEASURED (planned shared exits, charged cache-preserving floor, summary translator and feasible stronger representation).

## Audit record
id: C046
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.68
old_bo4: 0.77
old_pass4: 0.87
old_ub95: 0.93
new_single: 0.62
new_single_range: 0.40-0.81
new_bo4: 0.74
new_pass4: 1.00
new_ub95: 0.81
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Learn useful constrained common-state summaries beyond a fully charged cache-preserving elastic baseline.
redesign_single: 0.39
redesign_bo4: 0.48
redesign_pass4: 0.34
redesign_ub95: 0.61
redesign_gpuh: 280
attack_basis: LITERATURE-ONLY
demonstrated_ref: KernelAgent, Opus-4.5, 2026; NanoGPT, GPT-6.2 Astra, 2026
gap_to_attack: Efficient code and training edits versus semantic forced-depth continuity
subfield_sota_ref: River-LLM, Shen and Zou, 2026; ADEPT, Yoo, 2026
anchored_single: 0.56
anchored_bo4: 0.66
anchored_pass4: 0.59
anchored_ub95: 0.73
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
