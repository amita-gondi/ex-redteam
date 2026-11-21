# C100 — Public throughput versus durable scientific throughput — screen audit
## 1. What the screen claimed
The old attack joined goodput instrumentation, mature serving, cancellation, bounded admission and durable-store backpressure, then optimized the real completion metric. ESTIMATED single 0.85, bo4 0.91, pass@4 0.99 and ub95 0.98 supported CUT; the TSV category was DUP, citing strong overlap with v3 05A. Its sources were:
- https://arxiv.org/abs/2401.09670
- https://docs.vllm.ai/en/stable/cli/bench/serve/

## 2. Evidence audit
DistServe demonstrates SLO-constrained request goodput, and vLLM documents serving benchmarks. Neither proves correctness of downstream scientific workflows, durable consumer acknowledgment or autonomous integration with a stateful validator. “Optimize the real metric” identifies a sound objective, not a demonstrated method for attaining the old reward.

Grade: PARTIAL. Cancellation/backpressure are plausible known components, but the durable pipeline is an extrapolation. Separately, the local 05A verification and reward text checks actual completion, continuation/side effects, deadlines and original-request coverage, making the intervention/target duplication substantive even though its workload vocabulary differs.

## 3. Research done now
- *DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving* — Yinmin Zhong et al., 2024 — https://arxiv.org/abs/2401.09670 — fetched — Establishes that scheduling around useful request completion can improve serving; storage durability and scientific validation are outside that experiment.
- *bench serve* — vLLM, 2026 documentation snapshot — https://docs.vllm.ai/en/stable/cli/bench/serve/ — fetched — Offers workload and latency measurement machinery. It lowers benchmarking effort, not uncertainty about the downstream acknowledgment contract.
- *AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines* — Li Chen, 2026 — https://arxiv.org/html/2609.18123v1 — fetched — Honest-baseline tuning sometimes gives modest gains, opposing the screen's near-ceiling certainty. Its deterministic proposer must not be described as frontier-agent discovery.
- *Singularity-Bench: Can Agents Build Agents?* — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Demonstrates an agent-built serving engine on real coding-agent traffic with validation gates; it lacks the durable scientific-consumer stage.
- *KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration* — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — Hardware-guided kernel successes justify a useful inner optimization loop, while leaving request dependencies and persistent effects untested.

## 4. Re-estimated attack
The ESTIMATED recipe budget assigns 0.18 to eliminating useless generated work, 0.31 to engine/batching optimization and 0.24 to dependency scheduling plus durable backpressure, giving 0.73. These contributions are conditional on a raw-token incumbent and a scientifically justified completion utility. Relative gains cannot be converted from DistServe throughput ratios into normalized reward without a measured competent floor and stronger attainable control.

An ESTIMATED three-outcome model uses probability 0.10 at 0.43 for a correct but bottlenecked pipeline, 0.65 at 0.72 for effective lifecycle tuning and 0.25 at 0.86 for a broadly successful scheduler. Single=0.10×0.43+0.65×0.72+0.25×0.86=0.73, range 0.43–0.86; bo4=0.43+0.29(1−0.10⁴)+0.14(1−0.75⁴)=0.82. The latter two branches exceed 0.60: p=0.90, pass@4=1−0.10⁴=1.00; ub95=0.86. Variability comes from discovering the actual critical path and cross-stage interference, not a constant best-of-four increment. These lower the old mean and upper tail but still give a literature-based CUT. Unrepresented timing uncertainty requires future measurement rather than another invented precision term.

## 4A. Demonstrated capability and subfield SOTA
The closest current system comparator is Singularity-Bench's SGLang reference and stronger agent engine; neither grades durable scientific workflows. AutoTuneBench's reported 1.2753× SGLang throughput after twenty iterations is a narrower tuning comparator, not universal serving SOTA. A card-specific R≈1 cannot be anchored until a same-resource system demonstrates better durable validated completions than the mature completion-aware floor.

Singularity-Bench reports Opus 5.5+Claude Code earning 11.52 simulated income units versus SGLang's 8.18 in twelve hours on four GB300s. The result demonstrates a complete optimized inference engine, but passing answer-quality gates does not establish exactly-once durable workflow semantics. KernelAgent's multi-agent hardware loop produces correct accelerated kernels; its article leaves backbone version and full search runtime unspecified. That is evidence for component engineering, not a timed consumer/storage integration demonstration.

The combined cancellation/admission/storage recipe is KNOWN-RECIPE. No fetched AGENT-DEMONSTRATED run combines those pieces with this scientific validation objective under comparable resources. attack_basis=LITERATURE-ONLY. In twelve hours, the agent must still trace dependencies, place cancellation boundaries correctly and prove that acknowledgment represents persistent useful output rather than a local queue transition.

ANCHORED ESTIMATED masses are 0.20 at 0.30, 0.65 at 0.51 and 0.15 at 0.71. Mean=0.50, range 0.30–0.71; bo4=0.30+0.21(1−0.20⁴)+0.20(1−0.85⁴)=0.61; pass@4=1−0.85⁴=0.48; ub95=0.71. This assumption-dependent forecast substantially discounts unsupported integration. It still admits a capable tail because end-to-end serving construction is actually demonstrated. The percentile is a proposed single-run tail, not an empirical S4 projection fit.

## 5. Verdict under the kill lines
The section-4 verdict is CUT through bo4 and other lines. The ANCHORED numerical verdict narrowly CUTs on ESTIMATED bo4, approximately 0.01 over its boundary; that conclusion alone is fragile. The headline ANCHORED CUT is UNCHANGED and binds on duplicate, independently of that forecast: 05A already grades useful externally checked serving with full denominators and side-effect obligations. Adding durable acknowledgment enriches its workload without changing the submitted scientific intervention.

## 6. Redesign
DUPLICATE-STAYS-CUT, class (d): duplicated serving optimization. The original card submits the resulting server and explicitly treats its proposed metric only as an internal optimization guide. A distinct reusable measurement-acquisition policy might become another task, but that would replace the intervention, require a new causal utility demonstration and exceed a justified repair of this card. Keep durable-consumer receipts as candidate validation cases for 05A. No redundant redesign score or additional GPU budget is asserted.

## 7. Measurement status
Rollouts UNMEASURED (planned lifecycle-aware serving attacks if consolidated into 05A). Grader noise UNMEASURED (planned repeated arrival traces, validator timing and clean durable-store restarts). Score ladder UNMEASURED (planned raw-token incumbent, completion-aware mature engine, dependency controller and independent feasible durable control).

## Audit record
id: C100
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.85
old_bo4: 0.91
old_pass4: 0.99
old_ub95: 0.98
new_single: 0.73
new_single_range: 0.43-0.86
new_bo4: 0.82
new_pass4: 1.00
new_ub95: 0.86
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
demonstrated_ref: Singularity-Bench serving, Opus 5.5+Claude Code, 2026; KernelAgent, model unreported, 2026
gap_to_attack: validated durable scientific workflows with dependent cancellation and storage
subfield_sota_ref: SGLang and agent engine on Singularity-Bench serving, 2026
anchored_single: 0.50
anchored_bo4: 0.61
anchored_pass4: 0.48
anchored_ub95: 0.71
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
