# C091 — Optimize long-horizon infrastructure without selecting a lucky ending — saturation screen
## 1. What the grader actually rewards
The useful object is a final deployable candidate whose speed survives independent cold reconstruction, with all earlier search failures and selection cost retained. R≈0 is the robust anytime-optimization floor and R≈1 is an attainable better independently replayed system. The starting implementation is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; an unusually favorable development timing, or an oracle winner never selected by the agent, contributes no legitimate deployed gain.
## 2. Strongest lawful combined attack
Use the sustained optimization workflow motivated by the verified [Infrathon paper record](https://huggingface.co/papers/2611.11995), but make selection deliberately conservative. Combine incumbent-preserving search, multiple independent restarts, paired interleaved comparisons, warmup and synchronized timing from [PyTorch benchmark utilities](https://docs.pytorch.org/docs/stable/benchmark_utils.html). Reserve a fixed final tranche for clean-process reconstruction and confirmation of the best few candidates, using holdout timing sessions distinct from the search sessions. Search candidate changes jointly where profiling shows shared bottlenecks.

This stack addresses both opportunity for late discovery and the winner's curse. It does not need the model to forget notes, stop prematurely or mistake an unverified patch for progress; the attacker is assumed competent throughout the full research horizon. ESTIMATED single-run R=0.70, range 0.47–0.86; ESTIMATED oracle best-of-4=0.80; ESTIMATED pass@4 at R≥0.60=0.92; ESTIMATED projected upper-95% bound=0.94. The single-run point equals rather than exceeds its strict line, but the repeated-search and projection estimates kill. Residual loss is genuine delayed interaction discovery, not timing hygiene; the card does not yet identify a specific interaction that defeats robust standard search after selection bias is controlled.
## 3. Other routes
- Robust local search with a fixed confirmation reserve is ESTIMATED R=0.61, range 0.39–0.79. It sacrifices some exploration but produces a credible deployable incumbent.
- An autotuning sweep with randomized trial order, restart allocation and independent finalist reevaluation is ESTIMATED R=0.67, range 0.44–0.85. Its selection rule can use uncertainty penalties without seeing hidden scores.
- Optimize once, then spend the remaining budget validating that single artifact: ESTIMATED R=0.44, range 0.22–0.68. This avoids lucky endings but misses discoveries that require sustained exploration, so it is a meaningful weak control rather than the main attack.
## 4. What would lower lawful saturation
Specify concrete delayed coupled infrastructure changes whose value becomes observable through earlier discriminating experiments, and provide a development distribution with the same observation noise and reconstruction rules. Put robust search and held-session confirmation in the floor. ESTIMATED reward could fall to 0.41–0.57 if the remaining bottleneck is a transferable research-allocation decision. ESTIMATED authoring effort is two to three weeks with ESTIMATED 192 H100 GPU-h for real change histories. Correlated host drift should be randomized or modeled, not used as an artificial source of difficulty. The independent replays are necessary measurement infrastructure, but do not alone supply research depth.
## 5. Decisive-check GPU-h re-estimate
Old allocation: ESTIMATED 12 GPU-h. New ESTIMATED total: 180 H100 GPU-h. Assume fixed ESTIMATED 1B/8B infrastructure workloads with no convergence training: ESTIMATED 4 anytime strategies × 3 campaign seeds × 12 H100-hours = 144 GPU-h; independently reconstruct ESTIMATED 12 finalists for 2 hours each = 24 GPU-h; add ESTIMATED 12 GPU-h for reference warmups and grade repetition. A whole long-horizon search cannot be meaningfully compared with a single short replay allocation. The revised envelope screens sustained selection behavior, but is still smaller than the full independent frontier-tail and extrapolation programme.
## 6. Duplicate check
Catalog T03 — MODERATE: its opened reusable research-controller task includes multi-fidelity allocation and strategy switching, while C091 focuses on durable infrastructure winners under noisy selection. v3 05B — MODERATE: it shares exact system performance but directly submits graph changes rather than a time-allocation plan. The current broad wording risks collapsing into those parents, although a specific delayed-interaction allocation treatment could distinguish it.
## 7. Verdict
CUT. ESTIMATED best-of-4 is 0.20 above its kill line and ESTIMATED pass@4 is 0.42 above its threshold. Long duration and honest independent replay improve evidence quality, but a competent robust anytime optimizer is already the natural complete method for the stated objective.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-horizon search-and-selection campaigns); grader noise UNMEASURED (planned: same-artifact cold reconstruction across sessions and hosts); score ladder UNMEASURED (planned: initial system, one-shot tuning, robust anytime search and attainable delayed-interaction control).
## Screen record
id: C091
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.70
attack_single_range: 0.47-0.86
bo4_est: 0.80
pass4_est: 0.92
ub95_est: 0.94
gpuh_old: 12
gpuh_new_est: 180
duplicate_of: catalog T03 MODERATE; v3 05B MODERATE
kill_reason: robust anytime search and independent confirmation cover proposed obstacle
souping_flag: no
