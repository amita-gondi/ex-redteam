# C100 — Public throughput versus durable scientific throughput — saturation screen
## 1. What the grader actually rewards
The server earns completed, validated and durably acknowledged workflows per full elapsed time over the original request population. R≈0 denotes the competent completion-aware service floor, and R≈1 is an attainable higher rate of useful durable outcomes under the same semantics. The raw-token-optimized server is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; a locally finished queue entry, discarded generation or flattering submitted metric earns no direct credit.
## 2. Strongest lawful combined attack
Adopt end-to-end goodput measurement, using verified [DistServe](https://arxiv.org/abs/2401.09670) and [vLLM's serving benchmark](https://docs.vllm.ai/en/stable/cli/bench/serve/) as concrete conventional baselines for optimizing completed requests rather than raw generation. Extend each request lifecycle through independent validation and durable consumer acknowledgment. Combine cancellation propagation, dependency-aware admission, bounded outstanding work, completion-aware batching and backpressure from the durable store. Profile actual critical paths, then tune the whole pipeline against the protected-fidelity development slice.

Goodput alone does not certify durable scientific correctness; the proposed attack explicitly adds the card's trusted downstream receipt condition. Once that target is visible during development, however, the agent need not invent a predictive proxy: it can optimize the real metric directly and use cheaper component timings only for screening. ESTIMATED single-run R=0.85, range 0.68–0.95; ESTIMATED oracle best-of-4=0.91; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% bound=0.98. The residual is coupled workflow dependencies, tail validation latency and durable-write scheduling. These are ordinary end-to-end service bottlenecks unless the author demonstrates a new causal interaction after complete completion-aware controls.
## 3. Other routes
- Instrument the actual completion lifecycle and tune a mature serving engine directly for durable goodput: ESTIMATED R=0.76, range 0.56–0.91. This is the strongest isolated recipe because correcting the optimization target may already eliminate most wasted work.
- Sweep concurrency, batching, cancellation thresholds, admission reserve and durable-write group size on complete dependency traces: ESTIMATED R=0.82, range 0.62–0.94. The original request denominator prevents presenting dropped hard work as extra capacity.
- Cap in-flight requests and prioritize nearly complete workflows: ESTIMATED R=0.59, range 0.35–0.81. A simple bounded-work policy can sharply reduce unfinished tails even without a learned metric or new scheduler.
## 4. What would lower lawful saturation
Make the submitted artifact a reusable measurement policy that must choose which costly downstream validations to commission before tuning new servers, and evaluate its choices through actual durable outcomes. Keep direct-metric optimization as a legal same-budget control and specify why validation cost makes it insufficient. ESTIMATED attack could drop to R=0.43–0.58 if evidence acquisition is a real bottleneck. ESTIMATED authoring effort is two weeks and ESTIMATED additional calibration 64 H100 GPU-h. That is a substantive new intervention; merely renaming receipts or adding more dependency graphs leaves the current server-optimization task unchanged.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 6 GPU-h. Revised ESTIMATED total: 48 H100 GPU-h. Assume a frozen ESTIMATED 8B serving model and CPU validators/durable storage, with no training: ESTIMATED 4 server/controller variants × 3 trace seeds × 3 H100-hours = 36 GPU-h; add ESTIMATED 8 GPU-h for request-output verification and ESTIMATED 4 GPU-h for warmup, cold reconstruction and repeated end-to-end accounting. CPU storage/validation authoring is separate. The old budget could expose token/receipt disagreement, but underprices replicated saturation loads, cancellation tails and downstream acknowledgments needed to establish the actual useful-capacity frontier.
## 6. Duplicate check
v3 05A — STRONG. The inspected exact-serving source already grades correct-on-time requested work with continuation/side-effect checks, complete request denominators and full-engine replacement. C100 ultimately submits and grades another completion-aware server; its metric is only an internal guide. Durable acknowledgment is a valuable workload obligation, but the current card supplies no distinct scientific intervention beyond that serving-capacity task.
## 7. Verdict
CUT for strong duplicate and clear saturation. ESTIMATED single-run reward exceeds its line by 0.15, with ESTIMATED best-of-4 0.31 above its cutoff. Receipt reconciliation belongs in the existing serving grader unless the metric-acquisition artifact becomes an independently consequential research treatment.
## 8. Measurement status
Rollouts UNMEASURED (planned: direct durable-goodput tuning and lifecycle-aware servers); grader noise UNMEASURED (planned: independent full arrival traces and storage-state repeats); score ladder UNMEASURED (planned: raw-token server, receipt-aware engine, dependency scheduler and attainable durable control).
## Screen record
id: C100
verdict: CUT
binding_line: duplicate
attack_single_est: 0.85
attack_single_range: 0.68-0.95
bo4_est: 0.91
pass4_est: 0.99
ub95_est: 0.98
gpuh_old: 6
gpuh_new_est: 48
duplicate_of: v3 05A STRONG
kill_reason: exact useful serving capacity already grades complete trusted outcomes
souping_flag: no
