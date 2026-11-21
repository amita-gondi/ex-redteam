# C019 — Autotune without teaching the model the tuner workload — screen audit
## 1. What the screen claimed
The earlier screen repaired the public feasible-space defect, rotated weight buffers, replayed representative requests and cached kernel choices by shape and residency regime. It assigned ESTIMATED single/bo4/pass@4/ub95 = 0.73/0.81/0.94/0.94 and CUT, category SYS, because disciplined replay tuning should avoid hot-buffer misselection. It cited:
- https://github.com/sgl-project/sglang/issues/50057
- https://nvidia.github.io/CompileIQ/v1.1/benchmarking.html
- https://tvm.apache.org/docs/deep_dive/tensor_ir/tutorials/meta_schedule.html
## 2. Evidence audit
The issue exists and describes the two claimed failure modes, but a report is not a reproduction or proof of current upstream status. CompileIQ supports cold-cache benchmarking; MetaSchedule supplies measured search. Neither establishes a deployment-conditioned multimodal tuning policy whose probes perturb allocator state, nor measures its amortized end-to-end utility.

The strongest public repair should enter the floor before any headroom claim. Grade: PARTIAL: the search/measurement ingredients are real, while the old near-best-winner assumption lacked a comparable end-to-end demonstration. Newly consulted production tuning and autonomous optimization results substantially strengthen the integration route, with a remaining modality/residency gap.
## 3. Research done now
- tuning_block_wise_kernel.py cannot tune the [32, 32] block recipe and times candidates with the weight resident in L2 — sgl-project/sglang issue contributors, 2026 as accessed — https://github.com/sgl-project/sglang/issues/50057 — fetched — Confirms a concrete brownfield lead; the claim is reported behavior, not a locally verified fault or a reason to reward a public bug fix.
- Benchmarking Guidelines — NVIDIA CompileIQ, 2026 accessed documentation — https://nvidia.github.io/CompileIQ/v1.1/benchmarking.html — fetched — Cold-cache tooling makes the naïve timing confound cheap to challenge, raising the competent measurement baseline.
- MetaSchedule: Search-Based Auto-Tuning — Apache TVM, 2026 accessed documentation — https://tvm.apache.org/docs/deep_dive/tensor_ir/tutorials/meta_schedule.html — fetched — A complete measured-search framework reduces implementation novelty; the cost model still needs representative deployment observations.
- FlashInfer Autotuner v2: Tune the Way You Serve — Yang Xu et al., 2026 — https://flashinfer.ai/2026/09/22/autotuner-v2.html — fetched — Demonstrates execution-mode-aware tactic ranking, contextual persistent identity and independent selection-regret measurement. This directly strengthens the repaired policy/cache attack; its fixed candidate-pool measurements do not certify every VLM residency transition.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — Demonstrates a profile/diagnose/measure loop that changes kernel structure rather than merely tweaking tiles, raising the lawful agent's tuning ability.
- InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents — Jehyeok Yeon et al., 2026 — https://arxiv.org/html/2607.20468v1 — fetched — Agent serving optimization succeeds on fast feedback, while simple search beats agents and hardware transfer is brittle. Both findings matter: the attack should include ordinary search, but its portability is not automatic.

Search targeted cache-sensitive kernel benchmarks and contemporary production autotuning, including evidence against robust transfer.
## 4. Re-estimated attack
All modeled rewards are ESTIMATED. Representative timing and feasible-space repair capture about 0.31 of reward; independent full-request selection contributes 0.24; contextual cache identity and budget-aware retuning add 0.15. These marginal allocations exclude any separate reward for fixing the known issue and remain conditional on the original provisional anchors.

Recipe-conditioned R=0.51/0.70/0.84 has probabilities 0.15/0.65/0.20, representing a poor residency proxy, successful routine replay and a good conditional policy. ESTIMATED single=0.15×0.51+0.65×0.70+0.20×0.84=0.70, range 0.51–0.84; bo4=0.51×0.15^4+0.70×(0.80^4−0.15^4)+0.84×(1−0.80^4)=0.78. With ESTIMATED p=0.85, pass@4=1−0.15^4=1.00 rounded; ub95=0.84 because the lower states accumulate probability 0.80. Search-path choices and hardware/workload suitability create the spread; unknown timing noise is not assigned a measured variance. Against the old screen, the estimate falls modestly because the native amortization horizon and transition costs are still missing.
## 4A. Demonstrated capability and subfield SOTA
FlashInfer Autotuner v2 is the closest verified current production frontier for choosing reusable tactics under their actual execution boundary. Its independent-oracle regret is an appropriate native anchor; it does not justify an invented globally optimal VLM tuner. Set the task reference by reproducing its policy-aware selection on the authorized kernel pool, then establish R≈1 only from a stronger feasible end-to-end control under the frozen amortization horizon.

- KernelAgent's reported Opus-4.5 case uses four workers, eight rounds and H100 profiling to beat torch.compile on matrix-vector multiplication; elapsed time is not disclosed. The source above demonstrates integrating diagnosis and validation into the optimization loop. This is closer than a human-written TVM recipe, but its standalone operator oracle does not reproduce multimodal request state.
- InferenceBench reports Sonnet 4.6+Claude Code at 8.08 times naïve PyTorch aggregate performance after two hours on one H100, with automatic continuation and no user intervention. Same-budget SMAC reaches 11.53 times. That supports autonomous deployment and configuration search, while the paper's accuracy-tolerance gate is less strict than exact token conformance and its workload is text-only.

attack_basis=DEMONSTRATED-AGENT for the core measured-search integration, not for a proven exact VLM solve. The KNOWN-RECIPE contextual-timing machinery narrows the remaining implementation. ANCHORED ESTIMATED states 0.36/0.63/0.78 have probabilities 0.25/0.55/0.20 after allowing more validity and residency-transfer failures. ESTIMATED single=0.25×0.36+0.55×0.63+0.20×0.78=0.59, range 0.36–0.78; bo4=0.36×0.25^4+0.63×(0.80^4−0.25^4)+0.78×(1−0.80^4)=0.72; pass@4=1−0.25^4=1.00 rounded; ub95=0.78. This headline uses demonstrated nearby agent capability; normalized rewards remain forecasts rather than conversions of benchmark speedups.
## 5. Verdict under the kill lines
Evidence re-estimate CUT; ANCHORED CUT, UNCHANGED. Anchored ESTIMATED bo4 breaches by 0.12, pass@4 by 0.50 rounded and ub95 by 0.03. FlashInfer's actual contextual-timing results plus demonstrated agent search support rejection of an ordinary hot-versus-representative-timing task. A single exactness failure would invalidate that artifact, but does not erase the credible conforming implementation route.
## 6. Redesign
Cause (b): standard experimental search optimizes a grader with cheaply restorable measurement conditions. REDESIGNABLE as an online probe-allocation problem with real state opportunity costs.

Start from repaired execution-mode-aware tuning and validated contextual cache keys. Mix image-encoder, projector and long-context decoding stages so probing or compiling a candidate allocates buffers that evict useful state and changes future miss costs. Expose allocator receipts, request DAGs and predictive dev examples. Permit snapshot/restore, replay and robust defaults; charge their actual cost in the same deployment horizon. Use independently authored compositions of disclosed transitions and score complete useful requests, with compilation, tuning and state restoration in the denominator.

The strongest re-attack combines restored-prelude replay, FlashInfer contextual tactics, Bayesian candidate elimination and a predictor of state opportunity cost. Its re-attack basis is LITERATURE-ONLY: fetched agents do not demonstrate learning when a probing action changes future deployment value. It falls short only if choosing whether to measure and when to restore depends on coupled future requests, beyond a fixed cache key. A low-cost replay reset or near-universal robust kernel remains the leading kill risk. The target—tuning without sacrificing live multimodal service—is useful frontier infrastructure, and feasibility requires a same-budget control with positive native reserve.

ESTIMATED redesign R=0.30/0.48/0.67, probabilities 0.42/0.50/0.08, models damaging probes, partial state pricing and successful predictive stopping. ESTIMATED single=0.42×0.30+0.50×0.48+0.08×0.67=0.42; bo4=0.30×0.42^4+0.48×(0.92^4−0.42^4)+0.67×(1−0.92^4)=0.53; pass@4=1−0.92^4=0.28; ub95=0.67. It plausibly clears every line without secret state or artificial noise.

ESTIMATED decisive cost: 3B VLM, 4 tuner arms × 3 traffic seeds × 2 starts × 1 hour × 1 H100=24 GPU-h; legal tuning adds 12 and independent exact/amortization evaluation 12, total 48 H100 GPU-h.
## 7. Measurement status
Rollouts UNMEASURED (planned autonomous replay/search policies after public repair). Grader noise UNMEASURED (planned matched residency preludes and new process repetitions). Score ladder UNMEASURED (planned contextual production tuner through a feasible adaptive sensing control). Audit-record score and GPU values are ESTIMATED.
## Audit record
id: C019
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.73
old_bo4: 0.81
old_pass4: 0.94
old_ub95: 0.94
new_single: 0.70
new_single_range: 0.51-0.84
new_bo4: 0.78
new_pass4: 1.00
new_ub95: 0.84
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Optimize live probe timing and state restoration under fully charged multimodal residency opportunity costs.
redesign_single: 0.42
redesign_bo4: 0.53
redesign_pass4: 0.28
redesign_ub95: 0.67
redesign_gpuh: 48
attack_basis: DEMONSTRATED-AGENT
demonstrated_ref: KernelAgent, Opus-4.5, 2026; InferenceBench, Sonnet 4.6 Claude Code, 2026
gap_to_attack: exact VLM requests and deployment-state-conditional tactic selection
subfield_sota_ref: execution-mode-aware persistent tactic selection, FlashInfer Autotuner v2, 2026
anchored_single: 0.59
anchored_bo4: 0.72
anchored_pass4: 1.00
anchored_ub95: 0.78
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
