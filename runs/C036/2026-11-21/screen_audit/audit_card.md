# C036 — Recover useful output from preemptible inference leases — screen audit
## 1. What the screen claimed
Durable token logging, incremental KV snapshots, asynchronous transfer and hazard-conditioned checkpoint intervals were predicted to recover most lost progress. The screen reported ESTIMATED single/bo4/pass@4/ub95=0.69/0.78/0.88/0.92 and CUT, category SYS, on the strength of conventional recovery machinery. It cited:
- https://arxiv.org/abs/2311.15566
- https://arxiv.org/abs/2406.03243

## 2. Evidence audit
SpotServe demonstrates recovery on preemptible instances, using the cloud grace period; Llumnix demonstrates live request migration while source state is available. Neither establishes inexpensive acknowledged persistence when the entire leased worker and its host memory disappear without warning. Grade: ASSUMED: that durability boundary is central to the claimed asynchronous savings, and replacing migration with durable cold restoration is not a minor evidenced detail. Token logs remain plausible, but they do not prove that large-cache persistence beats charged recomputation.

## 3. Research done now
- SpotServe: Serving Generative Large Language Models on Preemptible Instances — Xupeng Miao et al., 2023 — https://arxiv.org/abs/2311.15566 — fetched — Fine-grained stateful recovery on real preemption traces supports the general mechanism; its grace-period opportunity weakens transfer to abrupt loss.
- Llumnix: Dynamic Scheduling for Large Language Model Serving — Biao Sun et al., 2024 — https://arxiv.org/abs/2406.03243 — fetched — Efficient in-memory migration raises confidence in state serialization and transfer. It leaves independent durable-storage acknowledgment and source disappearance untested.
- GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving — Shakya Jayakody et al., 2026 — https://arxiv.org/abs/2605.00831 — fetched — Measured coded KV recovery reduces checkpoint/recovery overhead, strengthening the attack against device failure. Host-memory parity is not automatically durable across the whole lease boundary.
- Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference — Yuhang Gan et al., 2026 — https://arxiv.org/html/2606.23521v1 — fetched — GPU-side deltas and committed host/CXL logs demonstrate a sophisticated recovery substrate. Its prototype scale and survival domain prevent treating it as a turnkey whole-worker persistence result.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched — Executed replication remains incomplete despite plausible implementations, a warning for checkpoint code that only looks correct before cold replay.
- Evaluating frontier AI R&D capabilities of language model agents against human experts — METR research organization, 2024 — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/ — fetched — Fast implementation and experimentation support testing several checkpoint intervals, while uneven sustained progress argues against assuming complete recovery integration.

## 4. Re-estimated attack
ESTIMATED shares of recoverable opportunity: 0.30 token/receipt logging, 0.45 avoiding prefix recomputation and 0.25 persistence scheduling. Recovering ESTIMATED fractions 0.95/0.50/0.43 gives 0.30×0.95+0.45×0.50+0.25×0.43=0.62. This explicitly discounts cache preservation because device-to-host transfer and truly durable remote storage have different latency and failure semantics.

An ESTIMATED recipe distribution assigns 0.38/0.64/0.78 probabilities 0.25/0.45/0.30. These are token-log recovery, working periodic snapshots and effective hazard/value adaptation, respectively. ESTIMATED single=0.25×0.38+0.45×0.64+0.30×0.78=0.62, range 0.38–0.78; bo4=0.78−0.14×0.70^4−0.26×0.25^4=0.75. With p=0.75, ESTIMATED pass@4=1−0.25^4=1.00 rounded, and ub95=0.78. Restart correctness and storage survival, not an arbitrary seed offset, produce this broad spread. The mean and upper tail are substantially below the screen because its durability substitution was unsupported, though repeated recipe success would still kill.

## 4A. Demonstrated capability and subfield SOTA
The appropriate north star is a same-failure-domain implementation of GhostServe or Concordia-style deltas, compared with durable token logging and measured recomputation. These are the strongest checkpoint-specific systems opened, but neither proves a full lease-loss optimum. A host-memory recovery benchmark cannot anchor R≈1 when the host is destroyed. No verified durable-progress ceiling exists for the exact contract yet.

Two fetched agent results constrain integration expectations. Starace et al.'s 2025 PaperBench gives Claude 3.5 Sonnet+BasicAgent twelve hours with one A10 and reports partial replication rather than reliable full reproduction. Cold-worker recovery requires similarly executable validation beyond code completion. METR's fetched 2024 RE-Bench shows Claude 3.5 Sonnet and o1-preview using its scaffolds on GPU-equipped R&D computers; aggregate short-budget success coexists with weak median attempts. Exact device allocations vary by task, and neither study measures durable inference recovery. These source outcomes are analogues, not forecasts calibrated to this card.

KNOWN-RECIPE is present for checkpointing and migration. AGENT-DEMONSTRATED evidence does not cover the recipe's cold, acknowledged durability. attack_basis=LITERATURE-ONLY; an agent must integrate cache format, RNG state, atomic commit manifests and replay receipts while testing actual loss of every local byte. The anchored verdict rests on this unmeasured transfer, not on an assumption that models cannot understand recovery protocols.

ANCHORED ESTIMATED modes: 0.30/0.52/0.69 with probabilities 0.30/0.60/0.10. ESTIMATED mean=0.30×0.30+0.60×0.52+0.10×0.69=0.47, range 0.30–0.69. ESTIMATED bo4=0.69−0.17×0.90^4−0.22×0.30^4=0.58; pass@4=1−0.90^4=0.34 with p=0.10; ub95=0.69. Most variance is whether the integrated snapshots actually improve cost-inclusive recovery; independent restarts share the disclosed storage regime.

## 5. Verdict under the kill lines
Section 4 gives CUT via ESTIMATED bo4=0.75. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL, with bo4 ESTIMATED 0.02 below its boundary. The fetched recovery papers narrow, rather than eliminate, the gap between live migration and external durability. Retention needs a frozen failure-survival contract, exact cold-replay tests and proof of reserve beyond the strongest durable-log/checkpoint baseline.

## 6. Redesign
Cause (a): ordinary fault-tolerant serving. REDESIGNABLE as selective persistence for real branching inference with shared prefix ancestry and tool-produced state. Expose the continuation DAG as it becomes available, branch probabilities/features, storage topology and lease hazard telemetry equally in development. Request loss removes local CPU and GPU memory; trusted remote storage acknowledgments define survival. Score independently verified committed useful completions per lease consumption, including remote transfer and future reconstruction.

The strongest attack combines token/receipt logs, prefix-trie sharing, coded/delta cache persistence and a hazard-aware knapsack policy. It remains fully legal. The research question becomes which shared state to persist before future branch reuse, given that copying one ancestor can save several restorations while delaying current output. Avoid labeling ordinary decoder tokens as special expensive reasoning. All branches must arise from actual inference workloads, and a feasible dependency-aware control must demonstrate more utility than standard cost-aware checkpointing.

Redesign attack_basis=LITERATURE-ONLY. ESTIMATED scores 0.22/0.43/0.65 at probabilities 0.40/0.52/0.08 give single=0.40×0.22+0.52×0.43+0.08×0.65=0.36, range 0.22–0.65; bo4=0.65−0.22×0.92^4−0.21×0.40^4=0.49; pass@4=1−0.92^4=0.28; ub95=0.65. The upper mode requires useful cross-branch value estimation. Main risk: generic cache replacement and DAG checkpoint dynamic programming already solve the attainable instance family, or remote storage erases all physical reserve.

Decisive-check GPU-h ESTIMATED: an 8B subject on one H100, five persistence arms, three independent continuation/lease seeds and one hour of consumed leases each costs 5×3×1×1=15.00. Add ESTIMATED 6.00 for clean-worker reconstruction and 3.00 for trusted reference generation: total 24.00 H100 GPU-h. This pilot would falsify the persistence-value premise without training.

## 7. Measurement status
Rollouts UNMEASURED (planned complete lease termination and fresh-worker restoration). Grader noise UNMEASURED (planned repeated remote-storage timings with receipt validation). Score ladder UNMEASURED (planned prompt replay, durable log, incremental snapshot and attained selective-persistence policies).

## Audit record
id: C036
old_verdict: CUT
evidence_grade: ASSUMED
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.69
old_bo4: 0.78
old_pass4: 0.88
old_ub95: 0.92
new_single: 0.62
new_single_range: 0.38-0.78
new_bo4: 0.75
new_pass4: 1.00
new_ub95: 0.78
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize externally acknowledged persistence of shared inference ancestry under actual worker loss and visible continuation structure.
redesign_single: 0.36
redesign_bo4: 0.49
redesign_pass4: 0.28
redesign_ub95: 0.65
redesign_gpuh: 24
attack_basis: LITERATURE-ONLY
demonstrated_ref: PaperBench, Claude 3.5 Sonnet plus BasicAgent, 2025; RE-Bench, Claude 3.5 Sonnet and o1-preview plus METR scaffolds, 2024
gap_to_attack: no demonstrated autonomous durable cold-recovery pipeline
subfield_sota_ref: GhostServe coded KV recovery and Concordia delta logging, Jayakody et al. and Gan et al., 2026
anchored_single: 0.47
anchored_bo4: 0.58
anchored_pass4: 0.34
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
