# C020: Train a memory admission predictor for inference state — independent adversarial review

**Verdict: CUT.** Workflow-conditioned future-use estimation with transfer/reconstruction costs is already a direct learned-cache recipe, and the card identifies no obstacle beyond its normal prediction errors. The throughput objective also permits workload selection unless completion obligations and the accounting interval are fixed independently of the candidate.

Source file: `/workspace/task_ideation_v4_creative/cards/C020.md`.

This review concerns a proposed predictor and workflow replayer, not a deployed cache. No cache runtime, admission-weight file or private workflow manifest is named in the card. I therefore refer to those conceptual artifacts explicitly rather than inventing inspected paths. Numerical performance below is ESTIMATED and conditional on yet-unwritten native-to-reward calibration.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Predict reuse value with ordinary supervised labels | From legal training workflows label next-use/rejoin time, bytes, transfer cost and recompute cost; fit a small conditional ranker and use value-per-byte admission. | ESTIMATED 0.72–0.91 | No: this is the natural implementation of the task itself. | Full joint learned future-use/cost baseline with legal workflow-progress features and tuned allocator. | ESTIMATED 0.72–0.91 | New tool outcomes are ordinary conditional-distribution uncertainty, not a new algorithmic barrier. |
| Replace independent entries with shared prefix ancestry | Use a canonical prefix tree, reference-count common ancestor blocks and prioritize shared state with many live descendants. | ESTIMATED 0.64–0.87 | Ancestry validation prevents wrong hits, not beneficial exact sharing. | Include exact shared-prefix reuse in the corrected starter and baseline; account physical rather than logical duplicates. | ESTIMATED 0.60–0.84 | The inherited eviction problem may disappear after ordinary block sharing. |
| Select cheap workflows to inflate completed/GPU-second | Reject expensive joins, preferentially run short branches, or let idle/tool wait disappear from the denominator while counting completions. | ESTIMATED 0.78–1.00 | No rejection, horizon or fairness law is defined. | Fixed offered mix, end-to-end clock and explicit rejected/missing work costs; compare throughput specialists. | ESTIMATED 0.28–0.59 | A legitimate batching policy may still sacrifice expensive workflows unless utility values them. |
| Filesystem/mount/proc/IPC/frozen-asset access | Inspect workflow-replayer memory, pending tool responses or mount-backed traces to obtain future rejoins; modify pinned model state to make reconstruction cheaper. | ESTIMATED 0.96–1.00 | Correct hit ancestry does not isolate future requests or base assets. | Separate causal request service from private future trace; read-only model/runtime and no shared descriptors, IPC or writable trusted libraries. | ESTIMATED 0.00 | Prefetch RPCs can become a future-trace oracle. |
| Interface or encoded-state smuggling | Hide evicted KV blocks in predictor weights, Python arrays, host page cache or compressed feature payloads outside declared cache bytes. | ESTIMATED 0.86–1.00 | Joint host/device state is promised without a complete object inventory. | Meter canonical predictor, metadata, staging, mapped and reconstructed bytes; enforce declared persistent artifacts and prevent unauthorized tensor import. | ESTIMATED 0.00 | Legal learned parameters and exact offloading need consistent accounting across all arms. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Report cache hits and workflow completion without recomputation, replay a stored answer, or recognize validation fixture hashes. | ESTIMATED 1.00 | The card explicitly rejects candidate hit counters, which blocks only that assertion channel. | Parent runs actual resumed generation and terminal checks; independent equivalent positives; fake completions and absent work fail closed. | ESTIMATED 0.00 | A reconstruction check on a separate shadow request does not authenticate the timed request. |
| Timing/check-decoupling/branch laundering | Begin transfers before timing, finish kernels after stopping the timer, validate slow correct state while timing a no-op, or reuse another branch's warmed KV. | ESTIMATED 0.90–1.00 | Transfer/predictor charges are stated; synchronization boundaries are absent. | Synchronize device events, capture the exact timed resume outputs, meter ancestors and all tiers, and restore cold per-workflow state. | ESTIMATED 0.00 | Useful prefetch is allowed but must be charged inside the same horizon. |
| Dev-hidden leakage/cue inference | Learn rejoin choices from workflow IDs, tool-latency padding, serialization order or deterministic trace suffixes instead of observable task progress. | ESTIMATED 0.75–0.97 | Shared visible signals and latency distributions do not remove joint labeling cues. | Swap hidden futures under matched lawful histories; crossed IDs/encodings and provenance-disjoint workflow families. | ESTIMATED 0.18–0.44 | A real progress signal may predict nearly every rejoin lawfully. |
| Adaptive aggregate oracle | Sweep admission thresholds and feature masks, use throughput differences to identify the private cost mix, then overfit the reused workflow bank. | ESTIMATED 0.68–0.90 | Feedback budget and precision are unspecified. | Globally metered protected development feedback and untouched final workflow set; include full-query threshold optimization in the floor. | ESTIMATED 0.49–0.77 | Cheap CPU fitting allows many candidate policies within the research budget. |
| Slice abandonment/denominator optimization | Retain short common prefixes while repeatedly evicting rare large joins; omit stalled workflows or failed ancestry checks from reported completion rates. | ESTIMATED 0.67–0.94 | Exactness protects accepted hits but not coverage or missing-work denominators. | Parent fixes offered workflow strata and completion horizon; publish per-rejoin-size utility and smooth deficits. | ESTIMATED 0.31–0.62 | Aggregate throughput can rationally favor small jobs even after omission is blocked. |
| Strongest lawful combined recipe | Train cost-sensitive relaxed-Belady/rejoin prediction, combine exact radix sharing with tuned host/device placement and prefetch, and optimize admission/eviction thresholds on legal outcome feedback. | ESTIMATED 0.77 (ESTIMATED 0.57–0.94) | Nothing in the contract blocks this compatible systems stack. | Benchmark an independently competent end-to-end implementation before asserting research reserve. | ESTIMATED 0.77 (ESTIMATED 0.57–0.94) | Hardening counters and memory isolation does not lower legal caching quality. |

## Published recipe shortcut — web checked

- [Learning Relaxed Belady for Content Distribution Network Caching](https://www.usenix.org/conference/nsdi20/presentation/song) presents learned approximation of future-aware caching with attention to training, memory and prediction overhead. Request sizes and reconstruction costs require adaptation here.
- [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104) supplies RadixAttention for exact KV reuse across structured calls, directly relevant to branches sharing prefix ancestry.
- [Stateful Large Language Model Serving with Pensieve](https://arxiv.org/abs/2312.05516) uses persistent conversation state and GPU/CPU caching, establishing that multiple memory tiers are part of the ordinary serving design space.

I opened the USENIX page and Pensieve abstract and found the SGLang primary abstract through web search this session. Verification covers described mechanisms, not implementation fidelity, pinned dependencies or compatibility of the assembled runtime. The complete recipe is ESTIMATED 0.77, with ESTIMATED range 0.57–0.94. These are judgement-based reward scenarios and contain no transferred paper speedups. An offline future-aware schedule can diagnose room for improvement but must never be passed off as a causal deployment baseline.

## Saturation against the hypothetical 10T researcher / 12h

The public training workflows naturally generate next-use supervision. The candidate can condition on progress, live descendants, pending tool type, elapsed latency and reconstruction price, then learn the expected benefit of retention. When a newly observed tool outcome changes which branch will rejoin, recomputing the ranking is routine conditional inference. If the outcome is not yet observable, an author with privileged future knowledge cannot be the feasible stronger control. A residual may exist in risk-aware multi-entry allocation, but the card does not specify a coupling that ordinary ranking plus allocator search cannot handle.

I forecast a single-run high score of ESTIMATED 0.92 against the binding >0.70 kill; oracle best-of-4 mean ESTIMATED 0.85 against >0.60; pass@4 ESTIMATED 0.94 against >0.50 at the source R>=0.60 threshold; and projected upper-95% reward ESTIMATED 0.99 against >=0.75. This last number is an ESTIMATED stress endpoint rather than an empirically supported prediction interval. Every absolute line is likely breached in the as-specified distribution if the combined baseline is implemented competently.

S1 remains unresolved: no measured native throughput frontier or feasible stronger predictor establishes reserve beyond the reference. A useful CPU bound is the best possible causal cache under the disclosed history, distinguished from a clairvoyant trace optimum. S7 also remains unresolved until an independently demonstrated same-resource policy lower-bounds the attainable ceiling. Normalizing tiny throughput differences would not supply physical headroom.

Observed runs and rollout rewards are UNMEASURED. Observed pass@k is UNMEASURED, to be estimated from complete independent research attempts on fresh branching-workflow families, not repeated traces of one selected cache. Grader noise is UNMEASURED; plan repeated identical-policy replay across matched warm/cold runs and actual hardware host variation, retaining rejected workflows and timeouts. Selection must be shown both with legal dev feedback and retrospective oracle access. The target researcher is assumed to preserve notes, use the available reservation and verify its timing, so current-agent passivity is not part of the forecast.

## Revised estimate versus the source card

The source ESTIMATED 0.49 already acknowledges a Belady-inspired progress/cost predictor but discounts it because tool outcomes can change future state value. I estimate the complete lawful stack at ESTIMATED 0.77. Updating predictions when an outcome arrives is the expected behavior of a workflow-conditioned model, and shared-prefix representation plus host placement removes avoidable pressure before prediction is even difficult. The source supplies no examples where these standard ingredients fail together. Its proposed pilot compares prefix frequency with conditioned admission, which establishes the benefit of the known attack rather than the residual above it.

## Boilerplate and missing build content

The card is ESTIMATED 0.70–0.85 task-specific and ESTIMATED 0.15–0.30 generic. It is concise and not mostly boilerplate. Missing build decisions are substantial: subject/runtime and state granularity, workflow observation API, arrival/rejoin law, legal scheduler actions, host/device accounting, staging limits, total memory budget, actual GPU-second definition, predictor size, training/replay budget and final reward mapping. The strongest legal baseline and reference are descriptions, not runnable artifacts.

The completion predicate must also distinguish correct workflow outcomes from merely resumed tokens. If caches are exact, output should match a correctly recomputed reference under identical sampling streams. If only a downstream task predicate is used, weaker generation or a changed decoder could buy throughput. Model version, prefix ancestry and positional state must be authenticated together. A hit that is valid for an ancestor is not automatically valid after a tool-message edit or a different attention mask.

## Duplicate check

The checked v3 file `06_architecture_resource_codesign.md` includes 06A, recoverable compressed attention under whole-system budgets. C020 shares exact-reconstruction and memory-accounting concerns but changes the intervention to admission prediction; 06A changes the representation itself. This is adjacent, not a demonstrated duplicate. No unchecked card IDs are asserted as matches. The known-method overlap with ordinary learned caching is stronger than the checked task overlap.

## Verdict, required fixes and cheapest decisive check

CUT for lack of a specified residual beyond a standard learned-cache implementation. A future design could examine partially observed, coupled rejoin value with demonstrably useful legal evidence and a competent cost-sensitive baseline, but adding secret futures or forbidding radix sharing would not preserve the current task's claim.

The cheapest decisive check costs ESTIMATED 0 H100-hours: CPU trace simulation of the offered-workflow objective, using authentic profiled reconstruction/transfer costs when available, comparing conditional value ranking, exact ancestor sharing, a tuned allocator and a causal-information bound. First test whether selective rejection or deadline accounting alone improves the metric. This is an analytical early-cut check; a surrogate simulator cannot certify GPU throughput. If it survives, a proposed hardware validation at ESTIMATED 7 H100-hours would replay compact held-out traces with the fixed model and all transfers/predictor work charged, including paired cold restores. No subject-model training is intrinsically necessary to fit a small CPU ranker, so the card's source ESTIMATED 10 GPU-h should not be copied as an automatic training cost.

Before any revival, require a portable unprivileged lifecycle, immutable assets, trusted completion channel, decoded-payload limits and all-process memory accounting. Test fabricated hits, wrong ancestry, delayed kernels, hidden host stores, skipped execution and independent positive implementations through `tests/test_anticheat.py`. Match compilation warmup, retain failed workflow slots, cap each replay, keep evaluation gold protected, audit decontamination and export the exact timed artifact with raw per-workflow receipts. Those are measurement prerequisites, not a way to rescue saturated caching research.

## Verdict record

id: C020
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.77 (ESTIMATED 0.57–0.94)
combined_recipe_attack: ESTIMATED 0.77 (ESTIMATED 0.57–0.94)
best_of_4: ESTIMATED 0.85
pass_at_4: ESTIMATED 0.94
single_run_max: ESTIMATED 0.92
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: none
main_kill_reason: conditional learned caching is the complete standard recipe
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
