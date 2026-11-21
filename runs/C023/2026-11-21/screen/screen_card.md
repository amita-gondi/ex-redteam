# C023 — Allocate replication compute to detect nonportable speedups — saturation screen
## 1. What the grader actually rewards
The harness selects a patch whose validated throughput transfers to independent host/workload blocks after paying for all replication used in selection. Confidence intervals and repetition counts are diagnostic rather than separate prizes, and failed placements remain in the campaign record. ESTIMATED R≈0 is the competent blocked-replication floor and ESTIMATED R≈1 an attainable stronger selection harness; inherited uniform replication is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60, with the deployment aggregation still requiring native calibration.
## 2. Strongest lawful combined attack
Use stratified paired host/workload blocks, a hierarchical latency model with patch-by-shape and patch-by-host interactions, and sequential best-candidate elimination. [MLPerf Training](https://arxiv.org/abs/1910.01500) verifies why throughput, quality and diverse systems need careful benchmarking; this card uses validated throughput rather than importing MLPerf's metric. [PyTorch numerical-accuracy documentation](https://docs.pytorch.org/docs/stable/notes/numerical_accuracy.html) verifies that execution arrangements can affect numerical behavior, supporting correctness checks on each measured placement.

Start with one matched baseline/candidate measurement on every declared host class for serious contenders. Allocate the remaining budget where posterior ranking uncertainty times deployment importance is largest, using code inspection to prioritize architecture-sensitive tiles, memory paths and reduction orders. Reserve an untouched host/workload block to confirm the winner. [rliable](https://github.com/google-research/rliable), verified elsewhere in this batch's web checks, can support interval reporting after adapting its resampling units; it is not itself an optimal experiment allocator. Tune selection thresholds and robust deployment value rather than rewarding an optimistic fastest-host statistic.

ESTIMATED single-run R=0.80, range 0.58–0.92; ESTIMATED oracle best-of-4=0.87; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED upper-95% projection envelope=0.97. These values are desk estimates. Blocking removes host offsets, hierarchical interactions borrow strength across related shapes, and targeted confirmation tests the uncertain winner. The residual consists of rare interactions absent from current evidence and noisy timing. However, declaring a bounded set of host classes and matching them in dev gives a competent adaptive benchmark substantial ability to cover that uncertainty. Uniform replication is not a credible strongest baseline.
## 3. Other routes
- A fixed stratified portability matrix with conservative deployment-average ranking: ESTIMATED R=0.65, range 0.41–0.84. It wastes some trials but can already avoid the most damaging host-specific patches.
- Search replication allocation, posterior risk penalty, shape clustering and early-elimination rules on public campaign pools. ESTIMATED R=0.74, range 0.51–0.90. Candidate code and profiler features make informative host selection easier than blind repeated measurements.
- Deploy the portable incumbent unless a challenger wins paired checks on every important host class. ESTIMATED R=0.51, range 0.25–0.77. This sacrifices some upside but may perform well if catastrophic portability losses dominate the utility.
## 4. What would lower lawful saturation
Construct patch families where a legal low-cost diagnostic predicts a cross-host ranking reversal, while a complete fixed matrix cannot be afforded within the campaign budget. Provide that diagnostic in dev and keep all host classes represented. Require adaptive replication to improve the final deployed throughput beyond hierarchical best-arm selection. Forecast revised attack: ESTIMATED R=0.48, range 0.26–0.70. Cost is ESTIMATED several weeks of real patch/host assets and ESTIMATED 96 additional H100-equivalent GPU-h of characterization. Introducing an unseen host architecture only in hidden would violate the stated fidelity instead of supplying legitimate research depth.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 6 GPU-h. Revised ESTIMATED 48 H100-equivalent GPU-h uses an ESTIMATED 1B-parameter fixed training-graph workload, ESTIMATED 6 patch arms, ESTIMATED 3 independently seeded host/workload blocks per arm, ESTIMATED 2 process repetitions per seed and ESTIMATED 1 H100-equivalent hour per measurement: ESTIMATED 6×3×2×1=36. Add ESTIMATED 8 GPU-h for adaptive selection probes and ESTIMATED 4 GPU-h for independent correctness/confirmation: ESTIMATED total 48. The default assumption is H100 hosts with different disclosed CPU/topology conditions; a genuine multi-SKU study requires separate device-hour rates and cannot literally run all architectures on H100s. The original budget omits both enough placements and untouched confirmation.
## 6. Duplicate check
v3 05B (`task_design_v3_codex/05_exact_systems.md`, source previously opened): WEAK, since it submits a training execution optimization while C023 submits the replication harness selecting fixed patches. D24 (`hidden_task_cards_v4/cards/D24.md`, opened earlier): MODERATE; both build a diagnostic selector, but its policy-session deployment effects differ from host/shape-sensitive ML systems patches. This is not a STRONG duplicate solely because both allocate tests.
## 7. Verdict
CUT. ESTIMATED single-run exceeds its line by 0.10 and best-of-four by ESTIMATED 0.27. Standard blocked portability measurement plus uncertainty-directed confirmation appears to capture the stated selection advantage.
## 8. Measurement status
Rollouts UNMEASURED (planned: replication harnesses with fixed complete launch ledgers). Grader noise UNMEASURED (planned: repeated matched placements, clock/load controls and host-block resampling). Score ladder UNMEASURED (planned: first-host ranking, uniform replication, stratified matrix, sequential hierarchical selection and stronger diagnostic control).
## Screen record
id: C023
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.80
attack_single_range: 0.58-0.92
bo4_est: 0.87
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 6
gpuh_new_est: 48
duplicate_of: v3-05B WEAK; D24 MODERATE
kill_reason: standard blocked adaptive replication targets portability directly
souping_flag: no
