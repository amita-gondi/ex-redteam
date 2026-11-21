# C073 — Packed attention whose speedup survives semantic isolation — screen audit

## 1. What the screen claimed
The screen combined a boundary-aware attention replacement, length packing, local positions, mask checks and end-to-end tuning. Its ESTIMATED single/bo4/pass4/ub95 were 0.86/0.92/0.99/0.99; it assigned CUT, category DUP, because the artifact and valid-training-speed objective substantially repeat v3 05B.

Old URLs, both fetched in this session:
- FlashAttention interface — Dao-AILab, 2026 repository snapshot — https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/flash_attn_interface.py
- FlashAttention-2 — Tri Dao, 2023 — https://arxiv.org/abs/2307.08691

## 2. Evidence audit
The interface documents boundary-carrying attention, while the paper establishes efficient exact attention. Neither demonstrates an autonomous agent porting that implementation into this JAX training project, preserving backward isolation and achieving the claimed normalized time-to-loss score. Bin selection and safe fallback are plausible additions, but their combined integration and complete cost were unsupported.

Grade: PARTIAL. The semantic primitive is established; the performance forecast conflated its availability with successful research execution. Separately, I read 05B's problem, environment and state-validation contract: it already optimizes an exact training graph across sequence lengths with FlashAttention available. Ordinary independent packed documents do not establish a distinct scientific objective.

## 3. Research done now
- FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision — Jay Shah et al., 2024 — https://arxiv.org/abs/2407.08608 — fetched — Hopper attention reaches reported FP16 speedups of 1.5–2.0×, raising the replacement threat; it does not measure packed JAX training campaigns.
- cudnn_flash_jax silently attends across packed sequence boundaries — AI-Hypercomputer/maxtext, 2026 — https://github.com/AI-Hypercomputer/maxtext/issues/4476 — fetched — The report identifies the correctly packed Transformer Engine path, making a public repair more concrete than the screen acknowledged.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — H100 forward-kernel optimization supports local speed search; missing campaign time and backward coverage weaken transfer to this card.
- CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation — Weinan Dai et al., 2026 — https://arxiv.org/abs/2602.24286 — fetched — The trained kernel agent exceeds torch.compile on most tested programs, raising synthesis capability without demonstrating a packed JAX training port.

Search covered variable-length packing/isolation, recent attention kernels and agent research engineering. No fetched result measured this exact combined task.

## 4. Re-estimated attack
All following reward quantities and mixture probabilities are ESTIMATED forecasts. Correct segmentation and masks provide validity, not reward above the competent isolated floor. I provisionally attribute 0.30 to a better supported backend/packing schedule, 0.15 to eliminating avoidable layout/dispatch costs and 0.08 to coordinated recomputation and batching. That component budget totals 0.53; absent measured floor/control utilities, these are allocations of possible reward, not measured speedups or calibrated conversions.

For a literature-capability stress model, use reward atoms 0.35/0.51/0.67 with probabilities 0.20/0.50/0.30. The low mode represents a correct but conversion-heavy port; the high mode finds a favorable packing/backend combination. ESTIMATED single = 0.20×0.35+0.50×0.51+0.30×0.67 = 0.53, range 0.35–0.67. For independent attempts, expected maximum = 0.67−0.16×0.70^4−0.16×0.20^4 = 0.63. With p=0.30, pass4 = 1−0.70^4 = 0.76; the single-run 95th percentile is 0.67. This already differs sharply from the screen's near-certain success: validity restoration cannot be counted twice above a corrected baseline.

## 4A. Demonstrated capability and subfield SOTA
Subfield comparator: Shah et al.'s FlashAttention-3 is a verified high-performance Hopper attention result. A universal November 2026 packed-training champion was not established. R≈1 must mean an independently achieved exact time-to-loss control on this workload, with the best supported packed backend in the floor; the paper's kernel ratio supplies no normalized reward anchor.

Two fetched agent comparators matter differently. KernelAgent's profiler-driven scaffold reports 1.56× over torch.compile on H100 L1 kernels; backbone and total search duration are unreported in the opened article. Its forward-only scope leaves the packed backward/update chain unproven. CUDA Agent's specialized agentic-RL model reaches a reported 92% faster-than-compile rate on KernelBench L3, but the fetched abstract does not identify inference campaign time or this task's training semantics. Its expensive prior RL development is not a twelve-hour discovery result. Neither identifies an unaided within-budget solution to C073.

KNOWN-RECIPE therefore exceeds AGENT-DEMONSTRATED coverage: attack_basis=LITERATURE-ONLY. In twelve hours the attacker still must reconcile metadata conventions, demonstrate neighbor-independent gradients and recover a useful complete-training gain after the supported repair. The anchored distribution is ESTIMATED 0.22/0.42/0.62 with probabilities 0.25/0.65/0.10, representing incomplete integration, serviceable port and validated profitable integration. Single = 0.39, range 0.22–0.62; bo4 = 0.62−0.20×0.90^4−0.20×0.25^4 = 0.49; pass4 = 1−0.90^4 = 0.34; ub95 = 0.62. Those probabilities are assumptions, not empirical agent frequencies.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT on ESTIMATED bo4 0.63 and pass4 0.76. ANCHORED verdict: CUT, binding duplicate, UNCHANGED against the old verdict. Anchored numerical margins would clear the lines by 0.31/0.11/0.16/0.13 respectively; they do not rescue an independently supported strong duplicate. The lower saturation forecast follows the missing end-to-end agent demonstration, whereas the duplicate judgment follows the actual 05B contract.

## 6. Redesign
DUPLICATE-STAYS-CUT. Kill cause class d: repeated exact-training-graph intervention and endpoint. A nonstandard dependency-graph compiler could become a different task, but changing independent packing into that research problem would require a new distinctness comparison and executable reference. No replacement card or speculative redesign score is assigned here.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent full-budget backend/packing integrations). Grader noise UNMEASURED (planned: repeat identical exact updates and complete loss endpoints). Score ladder UNMEASURED (planned: unpacked path, supported packed repair, tuned packing, independent faster exact control).

## Audit record
id: C073
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.86
old_bo4: 0.92
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.53
new_single_range: 0.35-0.67
new_bo4: 0.63
new_pass4: 0.76
new_ub95: 0.67
new_verdict: CUT
binding_line: pass4>0.50
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
demonstrated_ref: KernelAgent, unspecified backbone, 2026; CUDA Agent, specialized agentic-RL model, 2026
gap_to_attack: packed JAX backward isolation and end-to-end gain
subfield_sota_ref: FlashAttention-3 Hopper attention, Shah et al., 2024
anchored_single: 0.39
anchored_bo4: 0.49
anchored_pass4: 0.34
anchored_ub95: 0.62
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
