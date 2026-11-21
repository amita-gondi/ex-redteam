# C093 — Spend late research budget on complementary compression failures — screen audit
ANCHORED headline: CUT because T21 already covers the intervention and deployment outcome.
## 1. What the screen claimed
The screen combined quantization, pruning, single-teacher recovery, error-covariance diagnostics and longer continuation of diverse finalists. Its ESTIMATED single/bo4/pass@4/ub95 were 0.62/0.73/0.82/0.90; CUT, category DUP, because T21 already jointly selects compression and recovery under deployment constraints. It cited:
- https://arxiv.org/abs/2210.17323
- https://arxiv.org/abs/2301.00774
- https://arxiv.org/abs/2408.11796
- https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/pruning/README.md

## 2. Evidence audit
GPTQ and SparseGPT support individual transformations; Minitron demonstrates substantial pruning with recovery, and NVIDIA explicitly recommends recovering candidate architectures before selecting among them. These establish a strong human-built recipe, without measuring whether error complementarity predicts delayed recoverability or whether an agent can validate the combined stack inside twelve hours. The old numerical saturation claim is PARTIAL. The duplicate claim has firmer local evidence: T21 explicitly covers coupled sensitivity, structured reduction, quantization, recovery and packed deployment of one immutable model.

## 3. Research done now
- *GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers* — Elias Frantar et al., 2022 preprint, revised 2023 — https://arxiv.org/abs/2210.17323 — fetched — makes quantization available but does not show that pruning interactions are easy to recover.
- *SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot* — Elias Frantar and Dan Alistarh, 2023 — https://arxiv.org/abs/2301.00774 — fetched — establishes fast pruning; actual packed sparse execution and joint quality remain separate obligations.
- *LLM Pruning and Distillation in Practice: The Minitron Approach* — Sharath Turuvekere Sreenivas et al., 2024 — https://arxiv.org/html/2408.11796v4 — fetched — successful 8B-to-4B and 12B-to-8B conversions raise the recovery baseline, without demonstrating a twelve-hour autonomous search campaign.
- *Pruning examples and best practices* — NVIDIA Model Optimizer contributors, repository documentation inspected 2026, publication year unspecified — https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/pruning/README.md — fetched — finalist recovery is established guidance, so a greedy-only comparator would be inadequate.
- *Optimal Brain Restoration for Joint Quantization and Sparsification of LLMs* — Hang Guo et al., 2026 — https://proceedings.iclr.cc/paper_files/paper/2026/hash/e45d826ee52dce029198b6968a10423e-Abstract-Conference.html — fetched — second-order joint error compensation directly strengthens the compression recipe beyond independently chosen transformations.
- *APQF: Agentic Profiling-Guided Structured Pruning and Mixed-Precision Quantization with Adaptive Fine-Tuning* — Sadegh Jafari et al., 2026 — https://arxiv.org/html/2608.05499v1 — fetched — agents actually coordinate profiling, pruning and quantization/recovery, but only on much smaller vision subjects with some human-selected configuration.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — supports autonomous recovery-style training orchestration, leaving compressed-LLM delayed-error selection untested.

## 4. Re-estimated attack
Conditional recipe capture is ESTIMATED 0.18 from strong single-axis conversion, 0.14 from joint error compensation/order selection, and 0.14 from multi-fidelity recovery with finalist continuation. All transformations act on one original model. These are estimated portions of normalized deployment improvement, not claimed additive paper results. Unresolved losses arise when cheap recovery curves misrank complementary failures, and when sparse/quantized layouts fail to deliver their nominal resource advantage.

ESTIMATED states {0.24,0.49,0.71}, probabilities {0.25,0.60,0.15}, model a conversion/recovery mismatch, a useful ordinary program and a delayed joint win. ESTIMATED single = 0.46, range 0.24–0.71; bo4 = 0.71−0.22×0.85^4−0.25×0.25^4 = 0.59; pass@4 = 1−0.85^4 = 0.48; ub95 = 0.71. Delayed recovery discovery creates a larger selection effect than deterministic conversion. These replace the old substantially higher forecasts because cheap covariance measurement is not demonstrated to predict a final quality/bytes frontier.

## 4A. Demonstrated capability and subfield SOTA
The closest fetched joint-compression frontier is OBR: its Llama2-7B result combines W4A4KV4 with 50% sparsity at a reported 1.4 perplexity degradation, with up to 4.72× speedup and 6.4× memory reduction against FP16 dense. This is a specific reported operating point, not a universal best frontier or evidence for delayed recovery. Minitron supplies the relevant structured-recovery comparator. The task reference must independently achieve executable utility at the frozen byte/recovery budget, above these compatible recipes; a nominal bit count cannot anchor R≈1.

Agent result one is APQF, defaulting to Claude Opus 4.8 across five cooperating roles. On H200/A100 nodes it reports, for example, ViT-Small ImageNet Top-1 of 76.50 at 5.93% relative bit-operations after its constrained-data pipeline. Total wall time and GPU-hours are unreported; the authors retain human choices of compression aggressiveness and some recovery settings. This is genuine agent-assisted compression evidence with substantial scale, autonomy and budget gaps. Agent result two is GLM-5.2 with TrainExplorer's planned, decoupled post-training scaffold: ten hours and one 80GB GPU per configuration, reported aggregate 39.02. It demonstrates small-LLM training integration without compressed layouts or delayed complementarity selection.

KNOWN-RECIPE covers joint compensation and recovery continuation. The full LLM campaign is not AGENT-DEMONSTRATED at a comparable budget; attack_basis=LITERATURE-ONLY. In twelve hours an agent still must establish packed compatibility, explore interacting transformations and choose which initially poor branch deserves long recovery. The numerical forecast rests on that extrapolation.

Anchored ESTIMATED outcomes {0.16,0.39,0.64}, masses {0.35,0.57,0.08}, yield single 0.33, range 0.16–0.64; bo4 = 0.64−0.25×0.92^4−0.23×0.35^4 = 0.46; pass@4 = 1−0.92^4 = 0.28; ub95 = 0.64. The lower branch represents valid but uncompetitive packed conversions. Invalid attempts would receive zero during measurement rather than disappear from the denominator. This is far less optimistic than the screen, without implying that compression itself lacks mature methods.

## 5. Verdict under the kill lines
Section 4 is numerically CONDITIONAL: bo4 has only ESTIMATED 0.01 clearance; the overall evidence re-estimate is nevertheless CUT for duplicate. Anchored attack numbers are below all absolute lines, yet the ANCHORED verdict is also CUT, UNCHANGED. Reading T21's intervention, coupled sensitivity graph, recovery requirements and final packed-model grader confirms the same scientific action and outcome. Spending late budget on a complementary branch is already a lawful search policy within that task. No numerical margin is needed for this structural kill.

## 6. Redesign
DUPLICATE-STAYS-CUT, class (d). The existing compression task already accepts the final conversion/recovery program and charges rejected branches. A reusable predictor evaluated across reset campaigns could become a distinct research-process environment, but that changes the intervention and is not the card currently specified. Preserve its late-recovery hypothesis as a T21 experiment; no redesigned re-attack or GPU allocation is proposed here.

## 7. Measurement status
Rollouts UNMEASURED (planned paired conversion-order and recovery-continuation campaigns within T21). Grader noise UNMEASURED (planned recovery-seed and packed-runtime repeats). Score ladder UNMEASURED (planned individual conversion, joint compensation, continued recovery and feasible compressed controls).

Compression-reward fields in the record are ESTIMATED rather than measured conversion results.

## Audit record
id: C093
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 4
sources_new_count: 3
sources_fetched_count: 7
old_single: 0.62
old_bo4: 0.73
old_pass4: 0.82
old_ub95: 0.90
new_single: 0.46
new_single_range: 0.24-0.71
new_bo4: 0.59
new_pass4: 0.48
new_ub95: 0.71
new_verdict: CUT
binding_line: duplicate
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
demonstrated_ref: APQF, Opus 4.8 multi-role planner, 2026; TrainExplorer, GLM-5.2, 2026
gap_to_attack: delayed complementary LLM recovery lacks timed autonomous validation
subfield_sota_ref: OBR Llama2-7B joint quantization-sparsity point, Guo, 2026
anchored_single: 0.33
anchored_bo4: 0.46
anchored_pass4: 0.28
anchored_ub95: 0.64
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
