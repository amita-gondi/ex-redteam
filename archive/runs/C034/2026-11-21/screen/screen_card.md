# C034 — Decode under a metered energy envelope — saturation screen
## 1. What the grader actually rewards
Verified useful work per trusted joule is the primary outcome, modified by disclosed latency penalties from the same request stream. Waiting, memory stalls and underfilled batches remain part of energy accounting, so lowering instantaneous watts alone may worsen utility. ESTIMATED R≈0 is the competent energy-tuned operating floor and ESTIMATED R≈1 an attainable latency-feasible efficiency control; maximum-clock starter utility plausibly maps to ESTIMATED R=0.00, with reference ESTIMATED R=0.60 unconfirmed.
## 2. Strongest lawful combined attack
Start with a healthy fused inference engine, measure energy/latency curves jointly across power cap, batch size and prefill/decode mix, and retain only Pareto-efficient operating points. [Zeus](https://arxiv.org/abs/2208.06102) establishes joint workload/GPU energy optimization for training; its [power-limit optimizer](https://ml.energy/zeus/optimize/power_limit_optimizer/) exposes explicit energy and slowdown objectives. Adapting that control logic to inference is an inference here, not a claim that its training optimizer already solves this service.

Combine the sweep with a phase-aware lookup controller and hysteresis: use lower clocks during bandwidth-limited decode and higher power when prefill or latency pressure makes compute limiting. [Towards Greener LLMs](https://arxiv.org/abs/2403.20306) directly studies inference energy under performance constraints. Tune request batching, memory-efficient kernels and the switching policy together, with the trusted meter as the only energy authority. The small operating-point space makes exhaustive calibration and conservative fallback practical within the attacker allowance.

ESTIMATED single-run R=0.80, range ESTIMATED 0.56–0.93; ESTIMATED best-of-4=0.87; ESTIMATED pass@4 at R≥0.60=0.97; ESTIMATED upper-95% projection=0.98. On the provisional reward scale, obvious power/batch corrections supply most of the gain over the wasteful starter, and dynamic phase selection recovers much of the remainder. Residual inefficiency comes from switching delays, thermal drift and unpredictable arrival transitions. Those effects need measured magnitude; merely naming them does not establish a distant attainable control.
## 3. Other routes
A single fixed power-and-batch sweep yields ESTIMATED R=0.70, range ESTIMATED 0.45–0.88. It can solve stationary mixes and is the first cheap kill test.

Searching a compact policy over phase, queue depth, power cap and batch threshold reaches ESTIMATED R=0.76, range ESTIMATED 0.51–0.91. An agent can cross-validate policies on distinct traffic traces and use sequential elimination to reduce meter time. A kernel-only memory-traffic improvement is another lawful route, ESTIMATED R=0.49, range ESTIMATED 0.25–0.71, though its benefit may shrink after the energy-optimal operating point is retuned.
## 4. What would lower lawful saturation
Require a real cumulative energy budget with nontrivial deadline coupling and thermal history, where immediate efficiency choices change later feasible service. Keep those dynamics and the meter equally visible in development, and show a legal control beyond a tuned phase lookup table. ESTIMATED combined R might fall to 0.50–0.64. ESTIMATED cost is three thermal-systems weeks and ESTIMATED 72 H100 GPU-h for stable device-specific curves. Energy as a replacement denominator alone does not make a known tuning problem difficult, and an unreachable physical efficiency endpoint must not inflate normalized headroom.
## 5. Decisive-check GPU-h re-estimate
Old figure: ESTIMATED 8 GPU-h. Revised ESTIMATED 24 H100 GPU-h uses an ESTIMATED 7B frozen decoder, ESTIMATED twelve power/batch configurations, ESTIMATED two independently repeated traffic traces and ESTIMATED 0.5 hour of thermally stabilized execution: ESTIMATED 12×2×0.5=12. Replaying ESTIMATED three selected controller arms over ESTIMATED two mixed traces for ESTIMATED one hour adds ESTIMATED 6; trusted output checks and stabilization reserve add ESTIMATED 6. No model training occurs. The old budget is short mainly because meaningful power comparisons need stabilization and order-balanced repeats.
## 6. Duplicate check
05A: MODERATE. Its source optimizes exact serving under latency/resource limits, but measured energy is a changed native scientific target rather than simply another throughput constraint. 05B: WEAK, as inspected training-graph optimization has a different execution and utility. No STRONG duplicate is established from the existing index.
## 7. Verdict
CUT. The ESTIMATED best-of-four breach is 0.27; ESTIMATED single-run reward is 0.10 above its cutoff. A mature energy/Pareto controller plus inference tuning is a convincing lawful saturation route.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete fixed and dynamic operating policies). Grader noise UNMEASURED (planned: meter repeatability across thermal orderings). Score ladder UNMEASURED (planned: maximum clocks, fixed optimum, phase controller and attainable energy control).
## Screen record
id: C034
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.80
attack_single_range: 0.56-0.93
bo4_est: 0.87
pass4_est: 0.97
ub95_est: 0.98
gpuh_old: 8
gpuh_new_est: 24
duplicate_of: 05A MODERATE; 05B WEAK
kill_reason: energy operating frontier is small and directly searchable
souping_flag: no
