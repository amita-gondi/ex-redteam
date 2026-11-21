# C060 — Sampler consensus without serializing tensor parallelism — saturation screen
## 1. What the grader actually rewards
Every participating rank must commit the same token sequence under the authoritative sampling semantics, and throughput counts only those correct completed requests. Consensus on a wrong distribution or checking only an initial token fails the outcome contract. R≈0 is the known-correct repaired sampler floor, including authoritative selection; R≈1 is the attainable service-rate control under identical communication and decoding limits, and the numerical scenarios below are ESTIMATED while this rate ladder remains UNMEASURED.

For efficient exact consensus, the nominal author-reference target is ESTIMATED R=0.60, without evidence that compact token broadcast leaves that reserve.

## 2. Strongest lawful combined attack
Normalize effective sampler configuration at admission and whenever a backend transition occurs. Select on an authoritative rank and broadcast compact token and transition metadata, using [NCCL Broadcast](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) with consistent collective ordering. This does not require broadcasting the whole vocabulary of logits at every step; when vocabulary logits are sharded, price the required gather or distributed selection separately. Token broadcast is often tiny beside model communication already required by tensor parallelism.

Optimize only after that baseline: share counter-based request/position RNG identities, keep backend epochs explicit, batch token receipts, and use local selection only where numeric and RNG semantics match. [PyTorch DTensor](https://docs.pytorch.org/docs/main/distributed/tensor.html) documents distributed randomness for replicated and sharded tensors, verifying that coordinated RNG is a standard systems concern. It does not promise arbitrary sampler backends produce bitwise-identical categorical draws. Fall back to authoritative selection at every uncertain transition, retaining exact output validation.

ESTIMATED single-run R=0.84, range 0.67–0.94; ESTIMATED best-of-4=0.91; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED upper-95% projection=0.98. These are desk beliefs for a workload-tuned stack beyond frozen calibration, not empirical intervals. The gap is communication latency at small batches and sharded-vocabulary selection overhead. The card has not established that removing that gap yields enough native reserve to support a research task; a correct token-broadcast baseline may already sit near the legal ceiling.

## 3. Other routes
Authoritative sampling plus batched token broadcast alone has ESTIMATED R=0.78, range 0.58–0.91. It is the strongest single conventional repair and should be measured before assuming distributed independent sampling is needed for useful capacity.

Joint autotuning of authoritative versus local-safe modes, communication grouping, graph capture and batch size has ESTIMATED R=0.82, range 0.63–0.94. The selector uses legal development timings and full-sequence checks. Replaying a fixed seed without maintaining request-position counters is not an adequate shortcut: changed batching consumes RNG differently and must fail correctness where outputs diverge.

## 4. What would lower lawful saturation
Specify an actual sharded-vocabulary, small-batch regime where centralized selection has a measurable complete-service penalty and a stronger exact distributed control is executable. Cross fallback transitions with request migration and heterogeneous backend state, using the same disclosed freedoms in development. ESTIMATED revised attack R=0.56–0.72, which still threatens the screen. ESTIMATED preparation is 6–9 person-days and ESTIMATED 64 H100-h for a topology-faithful pilot. Artificially charging compact broadcast like full-logit broadcast would create the desired result through accounting rather than science.

## 5. Decisive-check GPU-h re-estimate
Old allocation: ESTIMATED 8 GPU-h. Revised ESTIMATED 64 H100-GPU-h assumes an ESTIMATED 8B model using ESTIMATED 4 H100 ranks, ESTIMATED 3 sampler arms×3 workload seeds×1.5 cluster-hours: 3×3×1.5×4=54. Cross-rank receipt collection, cold fallback runs and independent sequence verification add ESTIMATED 10, giving ESTIMATED 64. No weights are trained. The prior amount buys only ESTIMATED 2 cluster-hours on this topology, too little for repeated transition coverage and fair goodput comparisons; a CPU RNG test cannot price distributed service behavior.

## 6. Duplicate check
05A: MODERATE from its source, as both submit exact serving code and score validated capacity, but sampler consensus is a different named mechanism from coupled sessions/adapters/shapes. 04A: WEAK after reading its asynchronous MoE contract; distributed version consistency overlaps, while that task grades learning across actor/learner states rather than rank agreement within inference. Neither is a STRONG target-and-intervention identity.

## 7. Verdict
CUT. The binding single-run forecast crosses 0.70 by ESTIMATED 0.14, and ESTIMATED best-of-4 exceeds 0.60 by 0.31. Compact authoritative token distribution is a lawful, technically ordinary route that the card has not shown to be costly enough to leave useful research headroom.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget distributed sampler implementations); grader noise UNMEASURED (planned: repeated matched-topology service timing with fixed RNG contracts); score ladder UNMEASURED (planned: corrected authoritative rank, token broadcast, safe shared RNG, hybrid fallback and attainable exact distributed control).

## Screen record
id: C060
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.84
attack_single_range: 0.67-0.94
bo4_est: 0.91
pass4_est: 0.99
ub95_est: 0.98
gpuh_old: 8
gpuh_new_est: 64
duplicate_of: 05A MODERATE; 04A WEAK
kill_reason: compact authoritative token broadcast likely approaches capacity ceiling
souping_flag: no
