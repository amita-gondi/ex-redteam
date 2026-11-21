# C018 — Checkpoint faster by recomputing the right state — screen audit
## 1. What the screen claimed
The screen combined asynchronous consistent saves, incremental dirty-state tracking, dependency analysis, safe derived-buffer omission and cadence tuning. ESTIMATED single/bo4/pass@4/ub95 were 0.83/0.89/0.99/0.98; CUT, category DUP, binding on STRONG overlap with v3 05B as well as a predicted mature-stack solve. The URLs were:
- https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html
- https://www.usenix.org/conference/fast21/presentation/mohan
- https://arxiv.org/abs/1910.02653
## 2. Evidence audit
PyTorch provides an asynchronous persistence implementation, and CheckFreq supports frequent checkpointing. The cited Checkmate is activation rematerialization, not recovery of optimizer history after process death. Its dependency-optimization idea transfers, but it cannot justify discarding moments or reconstructing an unavailable random/data stream.

No old source demonstrates an agent integrating the whole stack and validating durable equivalent updates within twelve hours. Grade: PARTIAL for the attack: asynchronous saving is concrete, while safe omission and end-to-end timing still require work. The duplicate claim is separate evidence, checked locally here: v3 05B explicitly permits recomputation and checkpoint/state transitions and grades amortized durability plus cold-resumed optimizer-equivalent work.
## 3. Research done now
- Asynchronous Saving with Distributed Checkpoint — PyTorch, 2026 accessed documentation — https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html — fetched — Supplies the practical staged-save route; staging-memory pressure and consistent snapshot boundaries remain candidate obligations.
- CheckFreq: Frequent, Fine-Grained DNN Checkpointing — Jayashree Mohan et al., 2021 — https://www.usenix.org/conference/fast21/presentation/mohan — fetched — Establishes that optimizing checkpoint cadence and serialization is ordinary systems work, raising the no-omission baseline.
- Checkmate: Breaking the Memory Wall with Optimal Tensor Rematerialization — Paras Jain et al., 2019, revised 2020 — https://arxiv.org/abs/1910.02653 — fetched — Makes dependency-cost optimization credible, with a precise gap: live activation ancestors are not necessarily durable restart ancestors.
- AdaCheck: An Adaptive Checkpointing System for Efficient LLM Training with Redundancy Utilization — Weijie Liu et al., 2026 — https://www.usenix.org/system/files/fast26-liu-weijie.pdf — fetched — Directly exploits state redundancy across parallelism and iterations, a much closer threat to this card's omission novelty than activation checkpointing.
- Checkmate: Zero-Overhead Model Checkpointing via Network Gradient Replication — Ankit Bhardwaj et al., 2025 — https://arxiv.org/abs/2507.13522 — fetched — A different Checkmate uses a CPU shadow cluster to reconstruct state from gradients. It strengthens the reconstruction concept only where that extra network/CPU/storage allocation is lawful and fully charged.
- DataStates-LLM: Lazy Asynchronous Checkpointing for Large Language Models — Avinash Maurya et al., 2024 — https://arxiv.org/abs/2406.10707 — fetched — Demonstrates scalable asynchronous model/optimizer capture; it supports a high-quality floor before claiming omitted-state research headroom.

Search also found an inaccessible MPI checkpoint-agent paper; it is not cited as demonstrated support. Both namesake Checkmate papers were distinguished to avoid importing recovery claims from the wrong method.
## 4. Re-estimated attack
All score amounts and scenario probabilities are ESTIMATED. Consistent asynchronous saving contributes 0.38, eliminating redundant copies adds 0.22, and lawful omission/cadence optimization adds 0.17 after restore cost. This forecast is conditional on a competent implementation and enough reconstructible state; it does not claim new buffers always exist.

Recipe-conditioned R=0.61/0.78/0.89 has probabilities 0.20/0.60/0.20. The low branch reflects expensive restore or little safe redundancy; the high branch combines overlap with useful omission. ESTIMATED single=0.20×0.61+0.60×0.78+0.20×0.89=0.77, range 0.61–0.89. ESTIMATED bo4=0.61×0.20^4+0.78×(0.80^4−0.20^4)+0.89×(1−0.80^4)=0.84. Here p=1.00, so ESTIMATED pass@4=1−0.00^4=1.00; ub95=0.89 because lower-state cumulative probability is 0.80. Variation represents differing omission discoveries and failure placements; storage timing and validation noise are UNMEASURED. Compared with the old forecast, reserve uncertainty lowers the mean and upper tail, despite stronger modern redundancy evidence.
## 4A. Demonstrated capability and subfield SOTA
AdaCheck is the closest verified recent state-redundancy SOTA; DataStates-LLM anchors asynchronous capture, and gradient-replication Checkmate offers a different hardware frontier. The attainable native target is durable equivalent progress near a healthy no-save execution after charging recovery. None establishes that frontier under this card's exact resource contract, so R≈1 and the reference require measurements rather than a fabricated perfect-save baseline.

- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts — Hjalmar Wijk et al., 2024, revised 2025 — https://arxiv.org/html/2411.15114v2 — fetched; its o1-preview and Claude 3.5 Sonnet AIDE agents produce kernels reported around twice as fast as the reference in the repeated-attempt regime, using one H100 and attempts capped at eight hours. This demonstrates low-level optimization, not durable checkpoint reconstruction or cold-state validation.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched; its reported Opus-4.5 configuration uses four optimization workers across eight rounds on H100, with elapsed time unstated. Correctness/performance-guided redesign is relevant to copying kernels, while restart equivalence crosses processes and training history beyond its operator oracle.

attack_basis=LITERATURE-ONLY: KNOWN-RECIPE persistence exists, but AGENT-DEMONSTRATED twelve-hour durable state omission is unverified. An agent must discover reconstructible ancestors and validate later optimizer transitions after every original process is gone. ANCHORED ESTIMATED R=0.28/0.47/0.70 with probabilities 0.30/0.57/0.13 gives single=0.30×0.28+0.57×0.47+0.13×0.70=0.44, range 0.28–0.70; bo4=0.28×0.30^4+0.47×(0.87^4−0.30^4)+0.70×(1−0.87^4)=0.57; pass@4=1−0.87^4=0.43; ub95=0.70. Numerical saturation is assumption-dependent; the structural duplicate decision is not.
## 5. Verdict under the kill lines
Section 4 would CUT numerically. The ANCHORED verdict also remains CUT, binding duplicate, UNCHANGED versus the old screen even though the anchored forecast crosses no numeric line. In /workspace/task_design_v3_codex/05_exact_systems.md, task 05B's problem allows recomputation, its dependency node D includes checkpoint/state transitions, and its reward explicitly amortizes persistence while cold-resume verification compares subsequent updates. Restricting that intervention to a reconstructible-state subset does not create a new research outcome.
## 6. Redesign
Cause (d): structural duplication of an existing durable-update execution task. DUPLICATE-STAYS-CUT. No separate redesign is proposed, because the identified omission/overlap tradeoffs already fit 05B's legal intervention and grader; inventing additional phase interactions would belong in that existing task's workload. This is a consolidation decision rather than a claim that checkpoint research itself is solved. Redesign re-attack basis and GPU allowance are not applicable.
## 7. Measurement status
Rollouts UNMEASURED (planned only if the omission mechanism is piloted inside the retained 05B contract). Grader noise UNMEASURED (planned storage-load blocks and identical-artifact cold restores). Score ladder UNMEASURED (planned complete asynchronous save, redundancy removal and independently feasible exact reconstruction). All forecast-valued record fields are ESTIMATED.
## Audit record
id: C018
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.83
old_bo4: 0.89
old_pass4: 0.99
old_ub95: 0.98
new_single: 0.77
new_single_range: 0.61-0.89
new_bo4: 0.84
new_pass4: 1.00
new_ub95: 0.89
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
demonstrated_ref: RE-Bench kernels, o1-preview and Claude 3.5 Sonnet AIDE, 2024/2025; KernelAgent, Opus-4.5, 2026
gap_to_attack: validated optimizer-equivalent cold recovery after selective state omission
subfield_sota_ref: redundancy-aware checkpointing, AdaCheck, 2026; gradient shadow recovery, Checkmate, 2025
anchored_single: 0.44
anchored_bo4: 0.57
anchored_pass4: 0.43
anchored_ub95: 0.70
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
