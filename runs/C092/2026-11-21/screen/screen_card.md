# C092 — Entropy-robust control for an actual GPU training scheduler — saturation screen
## 1. What the grader actually rewards
The queue must deliver measured private model improvement within real accelerator leases, including telemetry delay, preemption and unfinished jobs. R≈0 is the competent useful-progress scheduler and R≈1 is an attainable better allocation of actual learning work, not a simulated robustness certificate. The inherited scheduler is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; allocated GPU time cannot substitute for checkpoint-derived utility.
## 2. Strongest lawful combined attack
Replace the continuous-time premise with a discrete event controller that models lease boundaries directly. Use [Pollux](https://arxiv.org/abs/2008.12260) for progress-aware allocation and the round-based optimization framework in [Gavel's official implementation](https://github.com/stanford-futuredata/gavel), adding delayed-state filtering and a conservative short-horizon planner. Train a residual policy only for systematic errors remaining after those controls, with entropy regularization as an optional stabilizer. The cited continuous-time paper was verified through a bibliographic search result, but its theorem is not assumed to cover these discrete observations and no unverified theorem statement is used.

The combined controller estimates each job's marginal validation improvement, discounts stale telemetry, accounts for restart and lease loss, and replans when events arrive. A training-only discrete planner can supply labels for the residual policy. ESTIMATED single-run R=0.68, range 0.45–0.84; ESTIMATED best-of-4=0.78; ESTIMATED pass@4 at R≥0.60=0.90; ESTIMATED projected upper-95% bound=0.92. The residual is uncertainty about true learning curves and prerequisite-dependent value, especially when an irreversible lease decision precedes informative telemetry. These difficulties are genuine, but the card does not establish an interaction beyond what mature goodput scheduling plus delayed-state prediction is designed to handle.
## 3. Other routes
- Pollux-style goodput control with explicit lease-aware admission is ESTIMATED R=0.58, range 0.36–0.77. Translating throughput into actual model gain remains necessary; the published objective is a starting point, not the task's final oracle.
- Search scheduling weights, stale-state discount, rescheduling interval and restart thresholds against real queue replays: ESTIMATED R=0.64, range 0.42–0.82. Tune complete useful outcomes, retaining every unfinished-job loss.
- Conservative shortest-remaining-work allocation with delayed-progress estimates is ESTIMATED R=0.46, range 0.23–0.68. It may win if utility mostly tracks completion and job dependencies are weak, making it an essential simple control.
## 4. What would lower lawful saturation
Construct learnable job-value interactions where completing a precursor changes another job's learning return and delayed telemetry determines whether that dependency is worth funding. Expose equivalent dependency signals in development and freeze the full discrete goodput/lease controller as the floor. ESTIMATED attack could fall to 0.42–0.57, at ESTIMATED author effort of two weeks and ESTIMATED added calibration of 192 H100 GPU-h. Do not introduce hidden-only delays or confuse useless idle reservation with research depth. If a deterministic receding-horizon planner already captures the interactions, a learned entropy-robust controller supplies no defensible reserve.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 16 GPU-h. Revised ESTIMATED total: 384 H100 GPU-h. Assume mixed ESTIMATED 125M and 1B language-model jobs on an ESTIMATED 4-H100 queue: ESTIMATED 4 scheduler arms × 3 queue seeds × 4 GPUs × 6 hours = 288 GPU-h. Add ESTIMATED 48 GPU-h for residual-controller training and ESTIMATED 48 GPU-h for checkpoint validation, restoration and utility evaluation. Simulation can debug event logic on CPU but cannot replace these actual learning campaigns. The old figure omits the multiplicative cost of policies, queue realizations and real concurrent training, even at modest subject scale.
## 6. Duplicate check
v3 05B — WEAK, because the inspected task accelerates the computation of fixed exact updates rather than selecting which training jobs receive resources. Catalog T03 — MODERATE: it allocates experiments on live projects and shares downstream learning utility, but this artifact is a scheduler policy constrained by leases and delayed event telemetry. Those resource-state dynamics distinguish the intervention; a strong duplicate is not established.
## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds its line by 0.18, with ESTIMATED pass@4 exceeding its boundary by 0.40. The strongest lawful route bypasses theorem transport entirely through mature discrete scheduling plus measured learning-value prediction.
## 8. Measurement status
Rollouts UNMEASURED (planned: trained scheduler and discrete-planner queue campaigns); grader noise UNMEASURED (planned: repeated job-seed and delayed-telemetry executions); score ladder UNMEASURED (planned: inherited scheduler, goodput/lease baseline, residual policy and attainable dependency-aware controller).
## Screen record
id: C092
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.68
attack_single_range: 0.45-0.84
bo4_est: 0.78
pass4_est: 0.90
ub95_est: 0.92
gpuh_old: 16
gpuh_new_est: 384
duplicate_of: v3 05B WEAK; catalog T03 MODERATE
kill_reason: discrete goodput and lease aware planning bypass continuous time transfer
souping_flag: no
