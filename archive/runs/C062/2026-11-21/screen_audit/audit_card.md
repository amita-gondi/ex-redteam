# C062 — Prevent persistent NaN poisoning at graph padding transitions — screen audit
## 1. What the screen claimed
The screen combined guarded writes, dummy-state isolation, generation tags and tuned graph/eager fallback. ESTIMATED single/bo4/pass@4/ub95=0.80/0.88/0.98/0.97 supported CUT, category SYS: those repairs supposedly removed persistent poisoning. Its sources:
- https://triton-lang.org/main/python-api/generated/triton.language.store.html
- https://docs.nvidia.com/dl-cuda-graph/latest/torch-cuda-graph/best-practices.html
- https://docs.nvidia.com/dl-cuda-graph/latest/troubleshooting/memory-issues.html

## 2. Evidence audit
Triton's masked stores suppress writes; CUDA graph documentation specifies address-lifetime and pool constraints. These support the implementation pattern, but cannot establish alias coverage, later-request exactness or complete-service performance.

Grade: PARTIAL. The old attack's primitives are credible, but its claimed normalized gain and end-to-end safety were extrapolated from API documentation. The inherited source issue is a report with unresolved causal hypotheses, not proof that a particular inactive-lane write is the sole cause. The public repair must precede the measured floor, so it cannot earn positive headroom twice.

## 3. Research done now
All audit reward estimates, probability allocations and proposed pilot costs are ESTIMATED. Published results concern the linked workloads only.
- triton.language.store — Triton project, 2026 documentation snapshot — https://triton-lang.org/main/python-api/generated/triton.language.store.html — fetched — confirms masked stores suppress inactive writes; supports structural isolation rather than output sanitization.
- Best Practices for PyTorch CUDA Graphs — NVIDIA, 2026 documentation snapshot — https://docs.nvidia.com/dl-cuda-graph/latest/torch-cuda-graph/best-practices.html — fetched — clarifies capture/address constraints that an isolation patch must preserve.
- Memory Issues — NVIDIA CUDA Graph guidance, 2026 documentation snapshot — https://docs.nvidia.com/dl-cuda-graph/latest/troubleshooting/memory-issues.html — fetched — makes persistent inputs and graph-pool costs part of the actual throughput comparison.
- GLM-5.3-Flash/EAGLE padded graph batch latches later NaN logits, issue 49881 — SGLang contributors, 2026 — https://github.com/sgl-project/sglang/issues/49881 — fetched — confirms the reported persistent failure; unconfirmed state-index explanations lower confidence in a one-cause repair narrative.
- Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent — Lingyun Yang et al., 2026 — https://arxiv.org/html/2607.14541v1 — fetched — recurrent-kernel case studies demonstrate useful agent optimization, while production-wide gaps caution against equating local correctness with service readiness.
- InferenceBench — InferenceBench team, 2026 — https://inferencebench.ai/ — fetched — shows autonomous serving-stack integration under short budgets; does not exercise persistent recurrent poisoning across graph boundaries.

## 4. Re-estimated attack
First establish the actual contamination path using continued slot reuse and an independent eager trace. Then apply write ownership and dummy-state isolation at every identified persistent buffer, preserving valid active-request state. Keep graph capture on verified shapes and tune fallback against complete useful throughput. Reject replacing NaNs after corrupting a live state: that cannot satisfy the continuation oracle.

A successful recipe plausibly gains ESTIMATED 0.24 from safe graph retention beyond the repaired fallback floor, 0.20 from reducing unnecessary scratch/state work and 0.24 from graph inventory plus transition scheduling: total 0.68. These are assumed utility contributions after correctness, not a score for adding a guard. If the public repair already restores all useful throughput, the task lacks native reserve rather than offering a large new optimization reward.

The recipe-level ESTIMATED states are 0.46/0.68/0.81 with probabilities 0.20/0.65/0.15. Missed aliases or excessive fallback cause the low state; complete ownership and profitable graph reuse produce the high state. ESTIMATED single=0.20×0.46+0.65×0.68+0.15×0.81=0.66, range 0.46–0.81. ESTIMATED bo4=0.46+0.22(1−0.20^4)+0.13(1−0.85^4)=0.74; ESTIMATED pass@4=1−0.20^4=1.00, p=0.80; ESTIMATED ub95=0.81. The old mean and extreme bound assumed both a diagnosed cause and spare throughput that have not been demonstrated.

## 4A. Demonstrated capability and subfield SOTA
The closest inspected recurrent-kernel SOTA comparator is Atrex-Kernel-Agent's chunk_gated_delta: Opus 4.7 reaches 1.31× the production kernel on its selected shape. This does not establish graph-pool continuation safety. C062 needs a production-size control preserving exact state over future requests; R≈1 remains unanchored pending independent eager equivalence and native throughput reserve.

Two demonstrations inform the attacker. Atrex-Kernel-Agent uses profiling, a GPU knowledge base and iterative revisions with Opus 4.7 or Qwen3.7-Max; its recurrence result changes fallback code into native FlyDSL kernels. The tested accelerator is labeled XPU-A and comparable wall time/total GPU-hours are unreported. InferenceBench demonstrates Opus 5.5 Max/Claude Code combining serving optimizations within a two-hour allowance, with all twelve reported submissions passing its validity gates. The overview does not disclose a hardware-hour total. Neither experiment validates state isolation over an entire poisoned-slot continuation history.

KNOWN-RECIPE consists of masked ownership, scratch isolation and graph fallback. The complete attack_basis=LITERATURE-ONLY because unaided root-cause confirmation, alias coverage and profitable graph recapture are not jointly demonstrated. Nevertheless, the recurrent-kernel and serving results justify a meaningful successful-integration tail; this is not evidence that frontier agents cannot optimize systems.

ANCHORED ESTIMATED R has probability 0.18 at 0.22 for missed persistent aliases; otherwise R is uniform on [0.53,0.69], representing fairly mature graph-pool tuning after correct isolation. ESTIMATED single=0.18×0.22+0.82×0.61=0.54, range 0.22–0.69. Integrating 1−CDF(r)^4 gives ESTIMATED bo4=0.22+0.31(1−0.18^4)+0.16[1−(1−0.18^5)/(5×0.82)]=0.65. ESTIMATED p=0.82×(0.69−0.60)/0.16=0.46; using unrounded p=0.46125, pass@4=1−0.53875^4=0.92. ESTIMATED ub95=0.53+0.16(0.95−0.18)/0.82=0.68. The failure atom reflects alias coverage, and the continuous portion reflects tuning rather than grader noise. Independent attempts and usable reward anchors remain assumptions.

## 5. Verdict under the kill lines
The evidence estimate remains CUT. The headline ANCHORED verdict is CUT, UNCHANGED, binding ESTIMATED pass@4=0.92, approximately 0.42 over its threshold; bo4 also exceeds its line by approximately 0.05. The point estimate no longer crosses the single-run boundary. Recurrent-kernel and serving successes support useful tuning after isolation, but the probability of reaching that stage is assumed. A measured high-quality floor could instead expose the absence of remaining scientific headroom.

## 6. Redesign
Class (a): standard memory ownership and capture/fallback infrastructure. REDESIGNABLE. Begin after a complete, tested isolation repair. Make the optimization target safe transactional state sharing across speculative branch fork, verification commit, rejection rollback and graph-pool reuse. Supply explicit ownership manifests, all transition semantics and matched development histories. Couple capture inventory, copy-on-write recurrent state and branch acceptance so duplicating every state and falling back on every transition incur genuine measured costs within a realistic memory envelope.

The strongest re-attack uses guarded stores, per-request generation tags, dedicated scratch pools, copy-on-write state and adaptive graph/eager selection. Include that combined policy in the floor. Its remaining weakness is deciding when state may be materialized or shared without making future commit/rollback expensive. That is valuable inference R&D, provided a stronger exact implementation demonstrates reserve; simply multiplying padding sizes would fail this requirement.

ESTIMATED redesign states 0.29/0.48/0.64 at probabilities 0.24/0.61/0.15 represent failed transaction integration, safe conservative sharing and successful scheduling. ESTIMATED single=0.24×0.29+0.61×0.48+0.15×0.64=0.46; bo4=0.29+0.19(1−0.24^4)+0.16(1−0.85^4)=0.56; pass@4=1−0.85^4=0.48; ub95=0.64. Re-attack basis LITERATURE-ONLY; CONDITIONAL because pass@4 is close. The affordable change is the specified transactional workload plus measured reserve over combined caches; existing cache dominance or prohibitive copying would invalidate it.

ESTIMATED decisive check: an 8B hybrid subject on two H100s, four state/graph arms × three independent lifetime/decoding seeds × 1.5 cluster-hours × two devices=36 H100-GPU-h. Twelve additional device-hours cover reference continuation, graph capture and repeated timing, totaling 48. The expanded branch-transaction comparison costs more than the screen's narrower pilot.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent safe-state implementation attempts across full lifetime traces). Grader noise UNMEASURED (planned: deterministic continuation comparison separated from warmed service-timing repeats). Score ladder UNMEASURED (planned: repaired eager, isolated graph state, tuned fallback, transactional sharing and stronger exact service control).

## Audit record
id: C062
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.80
old_bo4: 0.88
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.66
new_single_range: 0.46-0.81
new_bo4: 0.74
new_pass4: 1.00
new_ub95: 0.81
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize exact speculative recurrent-state transactions after complete dummy-lane isolation and fallback repairs.
redesign_single: 0.46
redesign_bo4: 0.56
redesign_pass4: 0.48
redesign_ub95: 0.64
redesign_gpuh: 48
attack_basis: LITERATURE-ONLY
demonstrated_ref: Atrex-Kernel-Agent, Opus 4.7 and Qwen3.7-Max, 2026; InferenceBench, Opus 5.5 Max Claude Code, 2026
gap_to_attack: alias-complete state isolation and profitable graph reuse over future requests
subfield_sota_ref: recurrence selected-shape 1.31x production, Atrex-Kernel-Agent Yang et al., 2026
anchored_single: 0.54
anchored_bo4: 0.65
anchored_pass4: 0.92
anchored_ub95: 0.68
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
