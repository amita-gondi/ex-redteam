# C031 — Optimize inference under live vocabulary constraints — saturation screen
## 1. What the grader actually rewards
The measured utility is complete guided-generation speed while each emitted token obeys the automaton state induced by actual observations. Host parsing, mask production and transfers remain on the clock, so an isolated sampling-kernel speedup is insufficient. ESTIMATED R≈0 denotes the independently frozen competent floor and ESTIMATED R≈1 a stronger feasible end-to-end control; the unchanged implementation should be near ESTIMATED R=0.00 and the unmeasured reference near ESTIMATED R=0.60. The high forecast below assumes fresh live constraints leave a substantial native gap after that fixed floor; if the complete dynamic backend already defines the floor and exhausts throughput reserve, the task fails its physical-headroom premise instead.
## 2. Strongest lawful combined attack
Use [XGrammar 2](https://arxiv.org/abs/2601.04426), whose stated mechanisms include dynamic dispatch, just-in-time compilation and cross-grammar substructure caching. That source directly contradicts treating mature grammar engines as only static compilers. Combine its incremental structures with [llguidance's documented background mask computation](https://github.com/guidance-ai/llguidance/blob/main/parser/README.md), overlapping eligible CPU work with model execution rather than blocking the decode stream.

Maintain observation-version tags on compiled fragments and device buffers, transmit changed bitset blocks when sparse, and switch to a complete mask when delta bookkeeping is more expensive. Fuse mask application with sampling, reuse pinned transfer buffers, and keep an independently checked fallback for unsupported semantic predicates. Tune the representation switch and worker pool jointly with generation batch size. Public engines provide the bulk of the machinery; the frontier agent's remaining work is integration and profiling against live update traces.

ESTIMATED single-run R=0.85, range ESTIMATED 0.63–0.95; ESTIMATED best-of-4=0.91; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED upper-95% projection=0.99. These estimates assume observable constraints can be compiled or evaluated through the permitted automaton interface. The score reflects recovering most of the attainable latency gap over a naive full-mask pipeline, not raw token validity alone. Residual work comes from observations that destroy shared structure and synchronize previously overlapped stages. If model compute already dominates, neither this stack nor the author has much native speed headroom.
## 3. Other routes
Installing and correctly integrating the dynamic grammar backend alone is worth ESTIMATED R=0.75, range ESTIMATED 0.50–0.91. It lacks workload-specific transfer and overlap tuning but is already stronger than the card's static-cache straw baseline.

A bounded joint sweep over sparse/dense masks, transfer chunks, parser concurrency and batch size reaches ESTIMATED R=0.79, range ESTIMATED 0.56–0.93. Kernels are cheap to benchmark compared with retraining, making broad search credible within the attacker budget. A lawful CPU-only mask path can also exploit overlap, ESTIMATED R=0.56, range ESTIMATED 0.31–0.77, if host-device synchronization rather than parsing is the dominant issue.
## 4. What would lower lawful saturation
Make live observations modify shared semantic dependencies that cannot be reduced to selecting cached grammar fragments, and provide a same-budget exact control demonstrating substantial remaining latency improvement. Include dense invalidations and unrelated concurrent requests in the disclosed development distribution. ESTIMATED attack R could become 0.55–0.68, with ESTIMATED two author-weeks and ESTIMATED 24 H100 GPU-h for a validated workload mix. Merely enlarging automata is unlikely to defeat JIT compilation, substructure caching and adaptive dense fallback. The likely redesign still approaches repeated-search kill territory.
## 5. Decisive-check GPU-h re-estimate
Old budget: ESTIMATED 6 GPU-h. New ESTIMATED 10 H100 GPU-h assumes an ESTIMATED 7B frozen model, ESTIMATED four backend/kernel arms, ESTIMATED three independent observation traces and ESTIMATED 0.5 hour per complete run: ESTIMATED 4×3×0.5=6. Add ESTIMATED 2 GPU-h for full token-legality truth and ESTIMATED 2 GPU-h for warmup and host-variance repeats. CPU parser profiling is additional elapsed author time but no GPU training. The old figure is close for a narrow implementation comparison and short on correctness and host replication.
## 6. Duplicate check
05A: MODERATE. Its inspected contract measures exact end-to-end serving and permits complete backend replacement, but live semantic-mask generation is an identifiable narrower intervention here. D27: WEAK after reading its policy-learning and durable-browser-state contract; safe action grouping differs from vocabulary-mask execution. The established serving overlap alone is insufficient for STRONG status.
## 7. Verdict
CUT with ESTIMATED best-of-four margin above the cutoff of 0.31. The ESTIMATED single-run breach is 0.15, and verified dynamic-grammar work removes the central claim that standard backends cannot follow live constraints.
## 8. Measurement status
Rollouts UNMEASURED (planned: backends on fresh observation-driven automata). Grader noise UNMEASURED (planned: parser-host and warmed GPU repetitions). Score ladder UNMEASURED (planned: full mask, dynamic engine, delta pipeline and attainable fused control).
## Screen record
id: C031
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.85
attack_single_range: 0.63-0.95
bo4_est: 0.91
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 6
gpuh_new_est: 10
duplicate_of: 05A MODERATE
kill_reason: dynamic grammar compilation and overlap are established
souping_flag: no
