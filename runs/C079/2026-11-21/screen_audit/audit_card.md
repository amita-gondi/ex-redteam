# C079 — A kernel benchmark that selects the fastest real training graph — screen audit

## 1. What the screen claimed
The old recipe bypassed isolated timing by substituting kernels inside full graph replay, with paired timing, coordinate descent and early elimination. It assigned ESTIMATED single/bo4/pass4/ub95 0.74/0.83/0.95/0.95 and CUT, category SYS, because replay directly measures the downstream quantity being rewarded.

Old cited URLs, fetched now, with documentation redirects followed:
- Triton issue listing — triton-lang, 2026 — https://github.com/triton-lang/triton/issues
- CUDA semantics, including CUDA Graphs — PyTorch, 2026 accessed docs — https://docs.pytorch.org/docs/stable/notes/cuda
- Benchmark Utils — PyTorch, 2026 accessed docs — https://docs.pytorch.org/docs/stable/benchmark_utils.html

## 2. Evidence audit
Graph capture and careful synchronized measurement are available; the screen's tools are real. Documentation does not establish that coordinate descent finds the best interacting kernel tuple after charging selection, or that a learned cheap selector generalizes to unseen graph mechanisms. Its original citation to an issue listing also left the cache phenomenon less directly evidenced than necessary.

Grade: PARTIAL. Full replay is a powerful lawful attack, but the old numerical conversion from accessible feedback to reward was assumed. Here the interface genuinely permits observing the target utility, so recent agent short-loop search results are more relevant than generic software benchmarks.

## 3. Research done now
- do_bench: zero_() L2 flush leaves dirty lines; their write-back is timed in the next kernel — triton-lang/triton, 2026 — https://github.com/triton-lang/triton/issues/12554 — fetched — Supplies the actual dirty-cache mechanism and explicitly limits its measurements to A100, narrowing hardware transfer.
- GPT-6.2 System Card, NanoGPT evaluation — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/safeguards — fetched — Astra improves complete time-to-quality within two hours on one H100, supporting autonomous empirical optimization rather than merely a known human recipe.
- Session report: 0.9979 → 0.9697 in 126 experiments — agent posting in Andrej Karpathy's autoresearch repository, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — The Claude session logs repeated train/evaluate/retain decisions over roughly 10.5 hours on H100; exact model version and independent replication are missing.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — Profiler-guided search outperforms default compilation on many H100 kernels; missing campaign duration prevents treating it as budget-matched evidence by itself.
- AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference — Xuanzhe Li et al., 2026, November revision — https://arxiv.org/html/2606.07665v3 — fetched — Measured in-graph admission and fallback produce reported 1.04–1.16× speedups over vLLM; human-designed runtime integration and unspecified search duration keep this a recipe comparator.

Search covered dirty-L2 reproduction, whole-training agent optimization and logged autonomous experimental loops. No source directly reports C079 rewards.

## 4. Re-estimated attack
Every score, probability and resource forecast in this analysis is ESTIMATED. Contextual replay can plausibly recover 0.29 reward by avoiding irrelevant flush-conditioned rankings. Joint candidate selection could add 0.20, and early elimination/cost-aware stopping 0.13. The 0.62 sum assumes these are incremental above a competent replay floor; measured native graph-time anchors must later replace that provisional allocation.

Use reward outcomes 0.43/0.63/0.72 with probabilities 0.15/0.65/0.20. Low runs choose mostly independent winners; middle runs exploit contextual timing; upper runs discover a beneficial coupled substitution. Single = 0.0645+0.4095+0.144 = 0.62, range 0.43–0.72. Bo4 = 0.72−0.09×0.80^4−0.20×0.15^4 = 0.68. With p=0.85, pass4 = 1−0.15^4 = 1.00 rounded; ub95 = 0.72. This mature feedback loop has a smaller best-of-four gap than an insight-dependent compiler project. The old upper tail was too high because neither source established an almost-optimal whole-graph selector.

## 4A. Demonstrated capability and subfield SOTA
AgentCompile is the closest verified selector-system reference located: generated candidates face correctness gates and in-graph measured admission. Its inference runtime differs from exact training updates and does not establish a universal best selector. OpenAI's NanoGPT human control saves 72.38% training time, a separate complete-training comparator. R≈1 must come from an independently achieved exact-graph selector beyond replay coordinate descent, with identical candidate choices and amortization horizon.

First agent result: GPT-6.2 Astra, in OpenAI's unnamed evaluation scaffold, saves 42.87% baseline training time within two hours on one H100. It demonstrates code modification, empirical selection and valid endpoint evaluation; architecture/recipe freedom differs from C079's fixed-update requirement. Second: the autoresearch Claude session reports 126 experiments and validation bits/byte 0.997900→0.969686 using one H100 over approximately 10.5 hours. Its scaffold and retained-trial ledger demonstrate the search loop, although model version and unaided verification are incompletely documented.

The first result establishes AGENT-DEMONSTRATED empirical selection; the second corroborates that component with weaker provenance. KNOWN-RECIPE covers graph capture, measured candidate admission and paired coordinate search. The combined attack remains LITERATURE-ONLY: exact interacting-kernel selection, complete update validation and amortized integration are unverified together. Once valid replay works, direct measurements should make restarts more consistent than open-ended scientific campaigns. Anchored ESTIMATED atoms 0.54/0.59/0.65, weights 0.20/0.60/0.20, model that narrower spread: single 0.59, range 0.54–0.65; bo4 = 0.65−0.06×0.80^4−0.05×0.20^4 = 0.63; pass4 = 1−0.80^4 = 0.59; ub95 = 0.65. This modest maximum-selection gain follows the mature measurement loop; the absolute reward placement and successful-mode frequency remain assumptions.

## 5. Verdict under the kill lines
Evidence re-estimate CUT; ANCHORED CUT, UNCHANGED. Anchored bo4 exceeds its line by ESTIMATED 0.03 and pass4 by 0.09, even though single remains below 0.70. The fetched short-budget training optimization results support a serious empirical-selection threat. They justify a higher attack than API documentation alone, while not supporting the old near-perfect upper tail.

## 6. Redesign
Class b; REDESIGNABLE. Freeze replay coordinate descent, clean-cache probes and paired elimination as the floor. Use naturally short-lived training graph specializations arising from adaptive sequence packing or changing parallel layouts; publish their lifetime distribution and charge all candidate profiling against that actual horizon. Provide representative interaction mechanisms in development. The submitted selector learns when to reuse information across related graphs and when a coupled probe is worth its deployment cost. The baseline remains feasible and useful; no arbitrary cap is added solely to defeat replay.

Strongest re-attack: warm-started coordinate replay plus a standard surrogate cost model and successive elimination. It loses when coupled substitutions share evidence across new graph compositions and blind per-graph probing spends more than the useful lifetime permits. This benefit must be shown by a reference, not presumed. ESTIMATED LITERATURE-ONLY redesigned atoms 0.18/0.43/0.66, masses 0.25/0.67/0.08, give single 0.39; bo4 = 0.66−0.23×0.92^4−0.25×0.25^4 = 0.49; pass4 = 1−0.92^4 = 0.28; ub95 0.66. Residual risk is a generic contextual tuner capturing all transfer. Decisive-check GPU-h ESTIMATED: frozen 125M and 1B update graphs, four selector policies×three graph banks×one H100-hour = 12; exact-update comparison 6, compilation/timing 6 and lifetime-amortization replay 6; total 30 H100-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: full-budget contextual replay selectors). Grader noise UNMEASURED (planned: repeated paired graph times under identical cache transitions). Score ladder UNMEASURED (planned: dirty timer, clean timer, full replay search, transfer-aware selector and stronger attainable control).

## Audit record
id: C079
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.74
old_bo4: 0.83
old_pass4: 0.95
old_ub95: 0.95
new_single: 0.62
new_single_range: 0.43-0.72
new_bo4: 0.68
new_pass4: 1.00
new_ub95: 0.72
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Learn probe allocation and cross-graph transfer on naturally short-lived coupled specializations above replay-based selection.
redesign_single: 0.39
redesign_bo4: 0.49
redesign_pass4: 0.28
redesign_ub95: 0.66
redesign_gpuh: 30
attack_basis: LITERATURE-ONLY
demonstrated_ref: NanoGPT, GPT-6.2 Astra OpenAI scaffold, 2026; autoresearch, unspecified Claude, 2026
gap_to_attack: exact interacting kernel choices and profiling amortization
subfield_sota_ref: AgentCompile in-graph measured selection, Li et al., 2026; universal training selector SOTA unverified
anchored_single: 0.59
anchored_bo4: 0.63
anchored_pass4: 0.59
anchored_ub95: 0.65
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
