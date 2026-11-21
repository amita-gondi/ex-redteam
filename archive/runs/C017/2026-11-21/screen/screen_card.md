# C017 — Keep useful GPU work under adversarially correlated arrivals — saturation screen
## 1. What the grader actually rewards
Exact returned tokens count only when they satisfy deadlines, divided by consumed GPU time, with delayed requests retained in their original workload strata. Admission therefore cannot create reward simply by excluding the hardest synchronized arrivals; offered-load coverage must remain part of the fixed workload contract. ESTIMATED R≈0 denotes competent serving goodput and ESTIMATED R≈1 the stronger attainable scheduling control; the stalled inherited server is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60, without measured capacity anchors.
## 2. Strongest lawful combined attack
Install a mature continuous-batching engine, add chunked prefill and deadline-aware admission, and forecast tool-return bursts from observed dependency completions rather than assuming Poisson arrivals. [Sarathi-Serve](https://www.usenix.org/conference/osdi24/presentation/agrawal) verifies chunked-prefill scheduling that reduces decode interference; [DistServe](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) verifies prefill/decode separation for goodput. The attacker should compare these architectures under the actual GPU allocation instead of pretending every published optimization can coexist for free.

For the feasible engine, maintain a rolling estimate of pending tool completions, request lengths and KV demand. Use short-horizon scheduling to reserve limited prefill capacity before a predicted burst, then release reservations when arrivals fail to materialize. Combine aging and per-stratum service guarantees so a burst predictor does not starve ongoing decode. Tune chunk size, reserve fraction, queue priority and concurrency jointly on full dependency-graph replays. Verify exact token sequences with a fixed reference path; engine numerical changes that break required tokens cannot earn throughput credit.

ESTIMATED single-run R=0.70, range 0.48–0.86; ESTIMATED oracle best-of-4=0.79; ESTIMATED pass@4 at R≥0.60=0.91; ESTIMATED upper-95% projection envelope=0.94. They represent provisional attack scenarios. The point equals the single-run boundary rather than exceeding it, but the repeated-search and projection lines are clearly breached. Most gain should come from removing ordinary prefill/decode interference and avoiding blind admission just before correlated returns. Remaining loss is forecast error and the feedback whereby completed inference changes later tool arrivals. Those interactions deserve investigation, but no concrete residual is yet separated from a full engine upgrade plus robust online control.
## 3. Other routes
- Chunked prefill with deadline aging and no burst predictor: ESTIMATED R=0.54, range 0.31–0.75. It can absorb substantial bursts without identifying their causal graph.
- Sweep prefill token budget, maximum active sequences, admission headroom and deadline weights on coupled traces, using exact conformance as a hard validity check. ESTIMATED R=0.65, range 0.43–0.83. Short serving replays make this route inexpensive relative to training tasks.
- Conservative admission may favor easy useful tokens if rejected requests are absent from the coverage denominator. ESTIMATED R=0.84, range 0.58–0.97 under that faulty interpretation. The main estimate assumes offered requests remain accountable, so it does not rely on this grader shortcut.
## 4. What would lower lawful saturation
Place a fully tuned modern engine in the floor and use graph families where servicing one branch changes the future burst distribution enough to reverse the best current admission choice. Disclose the causal interface and provide matched protected dev graphs. Require complete offered-request strata and same-capacity attainability. This could reduce the combined attack to ESTIMATED R=0.45, range 0.24–0.67. Cost: ESTIMATED several weeks of closed-loop trace construction plus ESTIMATED 64 H100 GPU-h for independent/coupled causal comparisons. Replaying only fixed arrival timestamps would weaken the endogenous-arrival claim.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 6 GPU-h. Revised ESTIMATED 40 H100 GPU-h uses an ESTIMATED 8B dense model on ESTIMATED 1 H100, ESTIMATED 4 scheduler arms, ESTIMATED 3 independent trace seeds per arm and ESTIMATED 2 process starts per seed, each ESTIMATED 1 H100-hour: ESTIMATED 4×3×2×1=24. Reserve ESTIMATED 8 GPU-h for tuning and ESTIMATED 8 GPU-h for warmup plus independent exact-output checks, totaling ESTIMATED 40. No subject training is needed. The original allowance can screen one trace but misses engine comparisons, process variance and charged search; very large multi-GPU models would need recosting.
## 6. Duplicate check
v3 05A (`task_design_v3_codex/05_exact_systems.md`, task opened): MODERATE. Both submit serving code and grade exact useful capacity across coupled sessions; C017's claimed extra mechanism is action-dependent tool-return synchronization rather than heterogeneous session/model-state mixtures. If implemented as another static arrival trace, that distinction collapses toward STRONG, but current prose specifies causal dependency graphs and warrants testing that difference first.
## 7. Verdict
CUT. ESTIMATED best-of-four is 0.19 above its gate, with pass@4 above by ESTIMATED 0.41. The whole-stack serving replacement and online burst-aware tuning must be beaten before attributing headroom to causal scheduling.
## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget exact-serving changes on closed-loop graph arrivals). Grader noise UNMEASURED (planned: repeated process starts, warm traces and GPU-clock controls). Score ladder UNMEASURED (planned: inherited server, mature engine, tuned batching, burst-aware control and stronger causal scheduler).
## Screen record
id: C017
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.70
attack_single_range: 0.48-0.86
bo4_est: 0.79
pass4_est: 0.91
ub95_est: 0.94
gpuh_old: 6
gpuh_new_est: 40
duplicate_of: v3-05A MODERATE
kill_reason: modern serving plus burst-aware admission likely consumes reserve
souping_flag: no
