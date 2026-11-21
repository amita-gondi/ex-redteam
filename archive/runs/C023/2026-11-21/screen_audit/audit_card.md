# C023 — Allocate replication compute to detect nonportable speedups — screen audit
## 1. What the screen claimed
The screen used paired host blocks, hierarchical patch/shape interactions, sequential elimination and a reserved confirmation block. It forecast ESTIMATED single/bo4/pass@4/ub95=0.80/0.87/0.98/0.97, CUT with category EXP, on the premise that standard adaptive replication selects portable patches. Sources listed there were:

- https://arxiv.org/abs/1910.01500
- https://docs.pytorch.org/docs/stable/notes/numerical_accuracy.html
- https://github.com/google-research/rliable

## 2. Evidence audit
MLPerf Training Benchmark — Peter Mattson, 2019, fetched — establishes careful end-to-end performance comparison, not optimal placement of replication trials. Numerical accuracy — PyTorch, 2026 documentation snapshot, fetched through its versioned redirect — motivates correctness checks across execution arrangements; it supplies no evidence of profitable patch selection. rliable — Google Research, 2021, fetched — offers uncertainty and aggregate reporting tools, rather than a cross-host best-arm allocator.

Grade: PARTIAL. The measurement hygiene is well grounded, and the attack can plainly be implemented. Its claimed normalized gain and efficient discovery of patch-by-host reversals were not supported by the original references. The bibliography mostly explains how to report trustworthy measurements, leaving adaptive scientific selection assumed.

## 3. Research done now
- GPU Performance Portability needs Autotuning — Burkhard Ringlein, 2025 — https://arxiv.org/abs/2505.03780 — fetched — Demonstrates JIT and parameter search on performance-critical language-model kernels. It strengthens the adversary's ability to use configuration features and measured device behavior, although autotuning kernels is broader than choosing among this card's fixed patches.
- Bringing Auto-tuning to HIP: Analysis of Tuning Impact and Difficulty on AMD and Nvidia GPUs — Milo Lurati, 2024 — https://arxiv.org/abs/2407.11488 — fetched — Finds that settings tuned on one vendor do not perform optimally on another. That cuts against the assumption that first-host wins transfer, while supporting the proposed attack's explicit target-specific checks.
- Towards a Benchmarking Suite for Kernel Tuners — Jacob O. Tørring, 2023 — https://arxiv.org/abs/2303.08976 — fetched — Parameter importance transfers more readily than optimal values across devices. This supports informative code/parameter priors but also warns that borrowing strength cannot replace actual placement measurements.

Search deliberately covered performance portability, rather than generic Bayesian optimization alone. These studies demonstrate the relevant hazard and useful search primitives; none measures this exact deployment-selection reward with all replication costs charged.

## 4. Re-estimated attack
All score statements here are ESTIMATED, with native throughput anchors still absent. Paired blocking and complete initial host-class coverage plausibly recover 0.38 of reward by eliminating misleading host offsets. Code-informed shape stratification contributes 0.18, and uncertainty-directed repetitions plus independent confirmation contribute 0.14. This yields approximately 0.70, leaving genuinely sparse interaction evidence and selection cost unresolved.

Use ESTIMATED probability 0.23 at R=0.51 when a rare reversal escapes useful measurement, and probability 0.77 at R=0.76 when ordinary stratification identifies a transferable winner. The relatively reliable upper regime follows from declared host classes and predictive dev coverage; the residual spread is ranking error, workload mix and correlated timing disturbances. ESTIMATED single=0.23×0.51+0.77×0.76=0.70, range 0.51–0.76. ESTIMATED bo4=0.51×0.23^4+0.76×(1−0.23^4)=0.76. With p=0.77, ESTIMATED pass@4=1−0.23^4=1.00 after rounding. ESTIMATED ub95=0.76 from the upper atom.

The unrounded mean slightly breaches the single-run line; repeated-search kills do not depend on rounding. Separate host/workload blocks must test these regime assumptions and dependence. The old projection lacked such a distribution, and this percentile still supplies no stronger-tier extrapolation.

## 4A. Demonstrated capability and subfield SOTA
For portability, Ringlein's JIT/autotuning study (2025, fetched in section 3) is the strongest directly relevant system result located. Its kernel performance is a realistic baseline for placement-aware search. A reward ceiling based on deployment selection still cannot be inferred: the card lacks fixed candidate patches, workload weights and a demonstrated optimal selection harness.

KernelAgent — Kaiming Cheng/PyTorch, 2026, fetched https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — reports 1.56× H100 speedup over default compilation. Its Opus 4.5 case uses parallel workers and repeated rounds, without a full time/compute cap. That demonstrates within-device tuning, not selecting cross-host observations. AlphaEvolve — Google DeepMind, 2025, fetched https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ — uses Gemini Flash/Pro with evolutionary evaluators and reports a 23% production training-kernel speedup. Experiments take days; total compute is undisclosed. Both are source-reported achievements, without a matched twelve-hour portability-selection result.

KNOWN-RECIPE covers blocked timing, hierarchical ranking and adaptive replication. AGENT-DEMONSTRATED covers kernel optimization with engineered evaluation, leaving campaign-level selection across hosts unshown. The complete attack is LITERATURE-ONLY. Assuming all those procedures integrate cheaply was the main reason section 4 overshot demonstrated capability.

ANCHORED ESTIMATED R∼U[0.35,0.64]: 0.35 captures reliable timing controls, while the remaining 0.29 varies with successful interaction modeling and replication allocation. ESTIMATED single=0.50, range 0.35–0.64; bo4=0.35+0.29×4/5=0.58. With p=(0.64−0.60)/0.29, ESTIMATED pass@4=1−(1−p)^4=0.45; ub95=0.35+0.95×0.29=0.63. The independent uniform model is a planning assumption, particularly fragile for rare workload interactions.

## 5. Verdict under the kill lines
The section 4 verdict is CUT with an ESTIMATED bo4 breach of 0.16. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL. ESTIMATED bo4 clears by just 0.02 and pass@4 by 0.05; neither supports clear passage. KernelAgent and AlphaEvolve demonstrate valuable optimization but do not demonstrate bounded-cost cross-host selection. Resolve that gap with equal-budget deployment campaigns and measured workload anchors before deciding between CUT and passage.

## 6. Redesign
The ANCHORED borderline requires a defined deployment/selection comparison. The proposed re-attack is LITERATURE-ONLY: available systems support its profiler components, without demonstrating its fleet-level decision rule in twelve hours.
Cause (b), conventional selection design; REDESIGNABLE. Replace generic replication allocation with a mechanism-informed deployment experiment for coupled kernel and input-pipeline patches. Include observable profiler traces, compiler resource reports, tensor-shape distributions and host topology. Construct authentic campaigns in which a patch changes the bottleneck, so a host measurement's information value depends on an earlier diagnosis of overlap, memory pressure or launch scheduling. All host classes and shifts must be represented in dev.

Score independent deployed training throughput with exact output/quality checks and full measurement cost. Establish hierarchical best-arm selection, target-specific autotuning, complete stratified sampling and conservative incumbent retention as competent floors. A useful reference must predict which topology/shape intervention resolves the disputed bottleneck, and retain its advantage under equal-budget ablation. A frontier lab would use that capability to avoid fleet-wide regressions. Merely making a fixed matrix unaffordable is insufficient; the stronger method must exploit available explanatory signals rather than receive privileged host knowledge.

The strongest redesigned attack builds a conditional latency surrogate from profiler features and chooses targeted measurements. ESTIMATED ordinary outcome R=0.33 with probability 0.65; successful causal bottleneck identification reaches R=0.56 with probability 0.35. Thus ESTIMATED single=0.65×0.33+0.35×0.56=0.41; bo4=0.33×0.65^4+0.56×(1−0.65^4)=0.52; pass@4=0.00; ub95=0.56. These estimates pass the desk lines with useful margins, subject to a measured attainable control. Risk remains that ordinary regression on compiler features solves the whole relation.

Pilot cost ESTIMATED 96 H100 GPU-h: a fixed 1B language-training graph, four harness arms, three campaign seeds, four hours per campaign on one H100 gives 48; independent topology/shape replays add 32; correctness and final throughput evaluation add 16. Arithmetic: 4×3×4×1+32+16=96. Use H100 hosts with disclosed topology/CPU differences for this pilot; it cannot certify AMD portability. A later multi-SKU claim needs actual device-specific costing.

## 7. Measurement status
Rollouts UNMEASURED (planned: complete selection campaigns including failed placements). Grader noise UNMEASURED (planned: repeated baseline/candidate timing with load and warmup controlled). Score ladder UNMEASURED (planned: initial-host choice, stratified replication, adaptive hierarchical allocation, profiler-informed diagnosis and attainable fleet control).

## Audit record
id: C023
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.80
old_bo4: 0.87
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.70
new_single_range: 0.51-0.76
new_bo4: 0.76
new_pass4: 1.00
new_ub95: 0.76
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Select deployment experiments by diagnosing observable bottleneck changes across coupled pipeline and kernel patches.
redesign_single: 0.41
redesign_bo4: 0.52
redesign_pass4: 0.00
redesign_ub95: 0.56
redesign_gpuh: 96
attack_basis: LITERATURE-ONLY
demonstrated_ref: KernelAgent, Opus 4.5 case study, 2026; AlphaEvolve, Gemini Flash/Pro, 2025
gap_to_attack: cost-aware cross-host replication and final patch selection
subfield_sota_ref: portable LLM kernel autotuning, Ringlein, 2025
anchored_single: 0.50
anchored_bo4: 0.58
anchored_pass4: 0.45
anchored_ub95: 0.63
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
