# C079 — A kernel benchmark that selects the fastest real training graph — saturation screen
## 1. What the grader actually rewards
The submitted instrument selects kernels, but its score comes from complete training-graph time after charging profiling and tuning, with update equivalence checked independently. R≈0 corresponds to the competent replay-based floor; R≈1 would select an attainable faster graph with sufficiently little selection overhead. The untouched dirty-cache instrument is ESTIMATED R=0.00 and the intended reference is ESTIMATED R=0.60; neither anchor has been executed, so kernel-ranking accuracy cannot be translated directly into reward.
## 2. Strongest lawful combined attack
Repair the cache-preparation issue described in the verified [Triton issue listing](https://github.com/triton-lang/triton/issues), then avoid depending on isolated cold-kernel rankings at all. Capture representative full graphs with [PyTorch CUDA Graphs](https://docs.pytorch.org/docs/stable/notes/cuda), time candidate substitutions in context, and use the warmup, synchronization and replicate discipline in [torch.utils.benchmark](https://docs.pytorch.org/docs/stable/benchmark_utils.html). The attack combines graph replay, coordinate descent over kernel choices, paired timing and early elimination of clearly slower alternatives. It retains the best complete incumbent, which limits the cost of misleading local measurements.

The unrestricted candidate interface is central: when full graph replay is lawful, cache transitions become observable treatment effects rather than an unknown microbenchmark correction. A frontier agent can spend its research budget fitting a lightweight cost model, then use short graph replays only for close choices. ESTIMATED single-run R=0.74, range 0.55–0.89; ESTIMATED oracle best-of-4=0.83; ESTIMATED pass@4 at R≥0.60=0.95; ESTIMATED projected upper-95% bound=0.95. Unrecovered reward concerns nonlocal interactions between several simultaneous substitutions and amortization on short-lived graphs. Those effects are real, but the card provides neither a restrictive profiling allowance nor a demonstrated counterexample where the standard replay stack fails.
## 3. Other routes
- Whole-graph coordinate descent alone is ESTIMATED R=0.67, range 0.45–0.84. It already measures the quantity the outer grader rewards, so cleaning a microbenchmark is optional to its success.
- A successive-elimination sweep over kernel tuples, first on short graph windows and then on complete steps, is ESTIMATED R=0.72, range 0.50–0.88. Exploration costs must be included; choosing an enormous tuple space without an amortization horizon would invalidate a high forecast.
- A repaired clean-cache benchmark with independent per-operation winners is ESTIMATED R=0.42, range 0.20–0.65. It is cheaper but still ignores residency inherited from neighboring operations.
## 4. What would lower lawful saturation
Publish a strict profiling-work allowance tied to a short graph lifetime and supply independently authored graph families with complementary kernel interactions. The development bank must expose the same interaction mechanism, not merely different tensor names. Put graph-replay coordinate descent in the frozen floor and demonstrate an attainable information-sharing selector beyond it. ESTIMATED combined attack could fall to R=0.44–0.58; ESTIMATED added cost is an engineer-week plus 24 H100 GPU-h for interaction and amortization calibration. A profiling cap chosen only to stop the known attacker would be unconvincing unless it models an actual workload horizon.
## 5. Decisive-check GPU-h re-estimate
Old card estimate: ESTIMATED 5 GPU-h. Revised narrow comparison: ESTIMATED 24 H100 GPU-h. Assume fixed ESTIMATED 125M and 1B transformer update graphs, no convergence training: ESTIMATED 4 selection policies × 3 independently seeded graph banks × 1 H100-hour = 12 GPU-h, plus ESTIMATED 6 GPU-h of full-update correctness checks and ESTIMATED 6 GPU-h of compilation, cache conditioning and timing replication. The old budget suffices for demonstrating a contaminated timer, not for establishing that graph-aware conventional selection leaves useful reserve. Large-model training would be unnecessary for this specific falsification pilot.
## 6. Duplicate check
v3 07B — WEAK after opening its evaluator specification: that task trains an evidence evaluator against researcher optimization, while this one selects executable kernels. v3 05B — MODERATE: both ultimately reward exact training-graph speed, but this card fixes the intervention to the measurement-and-selection instrument rather than the graph implementation. Shared downstream timing alone does not establish a strong duplicate.
## 7. Verdict
CUT. ESTIMATED single-run reward exceeds the single>0.70 line by 0.04, and ESTIMATED best-of-4 exceeds its threshold by 0.23. Charging profiling is useful, but without a concrete short-horizon contract it does not rule out ordinary end-to-end autotuning.
## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget graph-replay selector attempts); grader noise UNMEASURED (planned: paired whole-step timing across hosts and cache states); score ladder UNMEASURED (planned: dirty timer, clean timer, replay search and independently stronger selector).
## Screen record
id: C079
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.74
attack_single_range: 0.55-0.89
bo4_est: 0.83
pass4_est: 0.95
ub95_est: 0.95
gpuh_old: 5
gpuh_new_est: 24
duplicate_of: v3 07B WEAK; v3 05B MODERATE
kill_reason: lawful full graph replay selects the scored quantity directly
souping_flag: no
