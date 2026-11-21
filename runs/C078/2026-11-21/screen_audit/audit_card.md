# C078 — Rotary KV appends that remain correct after repeated reuse — screen audit

## 1. What the screen claimed
The screen attacked the actual out-of-range store, then added reference-counted pages, selective copying and layout-specific tuning instead of blanket snapshots. Its ESTIMATED single/bo4/pass4/ub95 were 0.83/0.90/0.99/0.98; CUT, category SYS, on the argument that bounded stores remove corruption without losing normal cache efficiency.

Old source URLs, fetched during this audit:
- Silent KV corruption with non-interleaved rotary — Dao-AILab/flash-attention, 2026 — https://github.com/Dao-AILab/flash-attention/issues/3014
- Automatic Prefix Caching — vLLM authors, 2026 accessed docs — https://docs.vllm.ai/en/stable/features/automatic_prefix_caching/

## 2. Evidence audit
The upstream report gives a concrete inequality for the failing padded dimensions, a reproduction and an explanation of writes beyond the logical key. This is stronger evidence than a generic corruption anecdote. The vLLM page establishes prefix reuse, but does not show a selective-copy transaction implementation curing this defect across delayed ownership changes.

Grade: PARTIAL. The local repair is highly actionable, while complete lifecycle integration and its reward remain inferred. The screen correctly challenged conservative universal copying, but its near-certain saturation numbers were unsupported by an agent trajectory or a measured corrected-service floor.

## 3. Research done now
- Efficient Memory Management for Large Language Model Serving with PagedAttention — Woosuk Kwon et al., 2023 — https://arxiv.org/abs/2309.06180 — fetched — The established paged-sharing system strengthens a reference-count/copy-on-write baseline; it is not evidence about this later rotary store bug.
- CudaForge: An Agent Framework with Hardware Feedback for CUDA Kernel Optimization — Zijian Zhang et al., 2025 — https://arxiv.org/abs/2511.01884 — fetched — Fast verified kernel iteration supports changing store predicates, but benchmark correctness does not exercise a page's future owner.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Its valid agent-built engine preserves sparse and recurrent prefix state, providing stronger integration evidence than isolated kernel scores.
- SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving — Jennifer Williams et al., 2026 — https://arxiv.org/abs/2609.26777 — fetched — End-to-end serving tests reject many otherwise passing patches, lowering confidence that immediate append parity establishes correct future service.
- KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch? — Yunxiang Zhang et al., 2026 — https://arxiv.org/abs/2607.16241 — fetched — Hidden input distributions expose shortcut-dependent performance claims, supporting delayed reads and realistic baselines here.

Search targeted the precise corruption report and current serving-agent integration. No fetched artifact was a complete C078 attack run.

## 4. Re-estimated attack
All projected rewards, mixture masses, uncertainty ranges and pilot costs below are ESTIMATED. A correctly bounded stock append avoids temporary-buffer traffic and plausibly recovers 0.34 reward relative to a conservative inherited path. Ownership-aware dispatch might add 0.15 and full-service tuning 0.12, totaling 0.61. These allocations assume the normalized scale retains a real service-throughput gap after the repaired stock path is measured; validity by itself is worth no above-floor reward.

The literature stress distribution has rewards 0.43/0.62/0.75 with probabilities 0.20/0.55/0.25. Low outcome: safe repair with fragmentation overhead; middle: stock-fast append with conventional ownership; upper: profitable selective-copy integration. Single = 0.086+0.341+0.1875 = 0.61, range 0.43–0.75. Bo4 = 0.75−0.13×0.75^4−0.19×0.20^4 = 0.71; pass4 = 1−0.20^4 = 1.00 rounded; ub95 = 0.75. The old estimates were higher because they essentially treated identifying a localized defect as guaranteed optimization of the entire service. Here spread is integration/dispatch success, not artificial measurement noise.

## 4A. Demonstrated capability and subfield SOTA
PagedAttention establishes an efficient cache-sharing reference, and the original issue establishes the necessary rotary bounds contract. The newer agent-built engine is a useful systems comparator, not a universal exact-cache SOTA. Set R≈1 only from an independently achieved legal lifecycle-throughput control; reported cache hit rates cannot substitute for post-transfer correctness or physical reserve.

CudaForge's o3-based Coder/Judge pipeline reports approximately 26.5 minutes per optimized kernel on one RTX6000. That is a comparable short-loop capability for a bounds-preserving append, but not for persistent ownership. Singularity-Bench's Opus 5.5/Claude Code serving engine integrates prefix-state restoration and passes completion/accuracy gates after twelve hours on four GB300s. Its hybrid-state integration raises this attack more than ordinary library documentation does; the benchmark still lacks C078's exact mutation/reuse assertions.

The combined bounds repair, ownership policy and delayed validation is KNOWN-RECIPE rather than directly AGENT-DEMONSTRATED; basis=LITERATURE-ONLY. The agent must turn a supplied diagnosis into a valid lifecycle artifact and identify profitable dispatch during twelve hours. Anchored ESTIMATED rewards 0.30/0.55/0.69 with probabilities 0.18/0.65/0.17 give single 0.53, range 0.30–0.69; bo4 = 0.69−0.14×0.83^4−0.25×0.18^4 = 0.62; pass4 = 1−0.83^4 = 0.53; ub95 = 0.69. The modest mean and substantial upper mode express near-comparable agent evidence, not the old near-perfect forecast. The upper-mode frequency remains an assumption and drives the anchored cut.

## 5. Verdict under the kill lines
Both re-estimates are CUT; the ANCHORED verdict is UNCHANGED. Anchored bo4 exceeds its line by ESTIMATED 0.02 and pass4 by 0.03, while single and ub95 remain below their cutoffs. This is a fragile forecast, not measured saturation: the concrete public bounds diagnosis and demonstrated hybrid-cache integration justify a serious success mode, but no matching agent frequency was observed. The record therefore explicitly marks the verdict as assumption-dependent.

## 6. Redesign
Class a; REDESIGNABLE. Supply the bounded-store fix and a tested reference-counted copy-on-write engine. Grade transactional append/read throughput across disclosed ownership DAGs with concurrent speculative branches, cancellation and shared partial pages. Define linearization and immutability semantics openly; give development traces that exercise the same ordering interactions. Keep a serialized legal path comfortably feasible and require a faster exact reference before committing this version.

The strongest re-attack uses stock append, copy-on-write, generic locks and tuned batching. It remains correct but pays unnecessary copies or serialization when ownership, commit order and page placement interact. A research solution must coordinate those decisions, a useful frontier serving capability. ESTIMATED LITERATURE-ONLY redesigned outcomes 0.19/0.42/0.65 with probabilities 0.30/0.62/0.08 give single 0.37, bo4 = 0.65−0.23×0.92^4−0.23×0.30^4 = 0.48, pass4 = 1−0.92^4 = 0.28, ub95 0.65. Risk: mature locking or exclusive-page dispatch may eliminate most overhead, so include both as complete baselines. Decisive-check GPU-h ESTIMATED: frozen 1B decoder, four implementations×three ownership blocks×one hour×one H100 = 12; delayed-read auditing, compilation and whole-service replay add 12; total 24 H100-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: repaired append and ownership integrations). Grader noise UNMEASURED (planned: paired deterministic trace replays with synchronized timings). Score ladder UNMEASURED (planned: bounded stock, temporary-buffer fallback, selective-copy engine and transactional reference).

## Audit record
id: C078
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.83
old_bo4: 0.90
old_pass4: 0.99
old_ub95: 0.98
new_single: 0.61
new_single_range: 0.43-0.75
new_bo4: 0.71
new_pass4: 1.00
new_ub95: 0.75
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Start with repaired stores and optimize explicit speculative ownership transactions above mature copy-on-write baselines.
redesign_single: 0.37
redesign_bo4: 0.48
redesign_pass4: 0.28
redesign_ub95: 0.65
redesign_gpuh: 24
attack_basis: LITERATURE-ONLY
demonstrated_ref: CudaForge, o3, 2025; Singularity-Bench serving, Opus 5.5 Claude Code, 2026
gap_to_attack: delayed ownership-transfer correctness after rotary mutation
subfield_sota_ref: PagedAttention cache sharing, Kwon et al., 2023; hybrid agent engine, Zhou et al., 2026
anchored_single: 0.53
anchored_bo4: 0.62
anchored_pass4: 0.53
anchored_ub95: 0.69
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
