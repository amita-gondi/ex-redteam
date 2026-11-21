# C097 — A speedup claim that must survive changed training arithmetic — saturation screen
## 1. What the grader actually rewards
The system must reach protected quality faster while its timed updates respect the declared reduction and optimizer contract; its committed gain forecast is checked against independent execution. R≈0 means the competent semantically valid training floor, and R≈1 means an attainable faster valid process with a calibrated claim. The no-op/reference are provisionally ESTIMATED R=0.00/0.60; the unspecified utility-versus-claim weight prevents a unique numerical reward calculation.
## 2. Strongest lawful combined attack
Reconstruct per-example and per-token weights from trusted receipts, then use a mature compatible training engine such as verified [TorchTitan](https://github.com/pytorch/torchtitan). Explicitly audit the reduction behavior described in [PyTorch DistributedDataParallel](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html), particularly summed versus averaged losses under distributed gradient averaging. Bind those checks to the optimized timed path, use paired complete-run measurements, and submit a conservative forecast derived from independent finalist confirmations. Add only semantics-preserving fusion, graph capture and communication overlap.

This attack does not need to identify a subtle arithmetic substitution from short-run loss alone. It can compare gradients, moments and parameter deltas against the receipt-defined computation before spending long training runs, then optimize a correct incumbent. ESTIMATED single-run R=0.78, range 0.57–0.92; ESTIMATED best-of-4=0.86; ESTIMATED pass@4 at R≥0.60=0.97; ESTIMATED projected upper-95% bound=0.96. Residual loss comes from new exact systems optimization after the false speedup is removed, plus uncertainty in time-to-quality. A forecast penalty may reward honest uncertainty handling, but conventional confirmation already handles that dimension; no special research mechanism is identified beyond the existing exact-training task.
## 3. Other routes
- Replace the suspect training update with a tuned compatible exact implementation: ESTIMATED R=0.68, range 0.44–0.86. A large payoff from this alone would show that the supposed scientific difficulty was a correctness defect.
- Sweep valid fusion, accumulation layout and communication schedules, rejecting configurations that change receipt-derived sample weights: ESTIMATED R=0.74, range 0.51–0.90. Repeated complete timings supply both selection evidence and the gain forecast.
- Repair semantics only and report a near-zero speedup honestly: ESTIMATED R=0.24, range 0.00–0.47. If this scores highly because forecast accuracy dominates utility, the metric is misweighted and needs redesign before interpreting saturation.
## 4. What would lower lawful saturation
Freeze the claim-scoring rule and its weight, floor receipt-aware mature exact training, and identify a genuine coupled optimization obstacle whose solution improves time-to-quality after parity is restored. ESTIMATED combined reward could become 0.42–0.57 with a substantive new workload mechanism. ESTIMATED author effort is two engineer-weeks plus ESTIMATED 192 H100 GPU-h for semantic and quality calibration. To distinguish a new task, the submitted intervention would need to improve a reusable semantic measurement instrument across new systems rather than simply submitting another faster exact graph and a forecast. This must still yield downstream learning value, not merely more tests.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 8 GPU-h. Revised ESTIMATED total: 480 H100 GPU-h. Assume ESTIMATED 1B training subjects with a real protected quality horizon: ESTIMATED 4 system variants × 2 seeds × 48 H100-hours = 384 GPU-h, plus ESTIMATED 48 GPU-h for update/optimizer-state differential replay and ESTIMATED 48 GPU-h for independent claim confirmation. No extra model capacity is permitted. A kernel-level semantic check can be cheap, but the card explicitly grades complete time-to-quality; the old allocation does not price replicated multibillion-token trajectories or forecast uncertainty. A separate smaller replay-only pilot could reject obvious substitutions first.
## 6. Duplicate check
v3 05B — STRONG. Its source already grades faster training graphs while preserving updates, optimizer state and resumability, with trusted execution tied to timing and exactness/tolerance contracts. C097 adds numerical claim calibration but submits the same systems intervention toward the same useful-training target. A forecast check is valuable audit practice, not enough scientific novelty to count a separate task.
## 7. Verdict
CUT for duplicate. Saturation independently supports rejection: ESTIMATED single-run reward is 0.08 above its line and ESTIMATED best-of-4 exceeds its boundary by 0.26. The arithmetic discrepancy should become a validation case for the existing task rather than a new task card.
## 8. Measurement status
Rollouts UNMEASURED (planned: receipt-aware exact replacements and optimization searches); grader noise UNMEASURED (planned: independent complete training and forecast confirmation); score ladder UNMEASURED (planned: suspect process, parity repair, tuned exact engine and attainable stronger process).
## Screen record
id: C097
verdict: CUT
binding_line: duplicate
attack_single_est: 0.78
attack_single_range: 0.57-0.92
bo4_est: 0.86
pass4_est: 0.97
ub95_est: 0.96
gpuh_old: 8
gpuh_new_est: 480
duplicate_of: v3 05B STRONG
kill_reason: exact training system and grader target already covered by 05B
souping_flag: no
