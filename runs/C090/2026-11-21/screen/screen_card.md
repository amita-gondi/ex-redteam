# C090 — Reproduce agent-built systems against a stronger inherited stack — saturation screen
## 1. What the grader actually rewards
The final system must improve real training or inference utility above a competent replacement stack on matched hardware, with setup and adaptation charged. R≈0 means matching that replacement floor, while R≈1 means reaching an independently attainable stronger deployed system. The untouched inherited implementation is ESTIMATED R=0.00 and the intended residual-change reference ESTIMATED R=0.60; auditing a paper's headline improvement earns no separate reward.
## 2. Strongest lawful combined attack
Start by replacing compatible subsystems with [TorchTitan](https://github.com/pytorch/torchtitan) for training and a mature serving runtime for inference, then use its supported compiled kernels, graph capture, checkpointing and parallelism controls wherever semantics permit. Apply the profiling and replication workflow documented by [PyTorch benchmark utilities](https://docs.pytorch.org/docs/stable/benchmark_utils.html), followed by search over complete configurations and targeted changes to the dominant residual bottleneck. These are compatible system components and configuration choices, not parameter combination. The source Singularity-Bench identifier was located through web search, but no published benchmark score is used as evidence for this card's reward.

The most credible attack fully respects the stronger inherited floor: compare replacements under identical update/serving contracts, remove any gains attributable solely to setup asymmetry, then optimize fusion, batching and workload dispatch above that floor. ESTIMATED single-run R=0.76, range 0.48–0.91; ESTIMATED best-of-4=0.85; ESTIMATED pass@4 at R≥0.60=0.95; ESTIMATED projected upper-95% bound=0.97. These wide forecasts reflect an unspecified residual workload, not evidence of a measured engineering gap. Remaining reward might require an original coupled bottleneck fix, but the card identifies no particular dependency or intervention that would make such a residual systematically hard rather than ordinary systems tuning.
## 3. Other routes
- Port a compatible mature training stack and tune its public configuration without novel code: ESTIMATED R=0.64, range 0.31–0.85. Its score should be zero when actually identical to the frozen floor; the forecast refers to fresh residual cases where the floor misses compatible tuning.
- Profile-guided search across graph capture, batch layout, recomputation and kernel dispatch is ESTIMATED R=0.72, range 0.43–0.90. A capable agent can retain a complete valid incumbent throughout exploration.
- Optimize only the largest measured operator and preserve the surrounding stack: ESTIMATED R=0.50, range 0.23–0.75. This loses cross-component gains but often captures a substantial fraction of ordinary bottleneck headroom.
## 4. What would lower lawful saturation
Replace the generic mandate with a concrete workload invariant and a demonstrated residual dependency that survives full compatible stack replacement. For example, a specified state-continuation interaction could require a new coupled change, but it must have its own attainable control and cannot merely relabel generic exact graph optimization. ESTIMATED attack could become R=0.42–0.58 after such a substantive redesign. ESTIMATED effort is several systems engineer-weeks and ESTIMATED 128 H100 GPU-h of residual calibration. This would effectively create a more specific card; baseline auditing alone is an evaluation practice, not an additional task intervention.
## 5. Decisive-check GPU-h re-estimate
Old card estimate: ESTIMATED 12 GPU-h. New ESTIMATED total: 96 H100 GPU-h. Assume ESTIMATED 1B and 8B fixed training/inference subjects, with no convergence requirement: ESTIMATED 4 complete stacks/configurations × 3 replay seeds × 2 H100s × 3 hours = 72 GPU-h, plus ESTIMATED 24 GPU-h for update equivalence, cold restore and independent warmed timing. Larger distributed subject configurations would require a separate recost. The earlier budget can compare a few runs but omits compatible replacement adaptation and replicated end-to-end state checks, which are central to this card's own premise.
## 6. Duplicate check
v3 05B — STRONG for the training branch: the inspected task already submits complete exact training-graph changes and grades faster valid updates above complete tuned defaults. v3 05A — STRONG for the inference branch: its source likewise permits mature serving replacement and measures exact useful capacity. C090 adds baseline-audit procedure but no distinct intervention or downstream target to either branch.
## 7. Verdict
CUT for STRONG duplicate, independently reinforced by saturation risk. ESTIMATED single-run reward is 0.06 above its cutoff and ESTIMATED best-of-4 is 0.25 above its line. Preserve the competent-replacement lesson as methodology for existing systems tasks rather than counting another task with the same action and outcome.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete-stack replacements on specified residual workloads); grader noise UNMEASURED (planned: independent cold restores and warmed performance repeats); score ladder UNMEASURED (planned: inherited stack, complete floor, residual reference and stronger compatible system).
## Screen record
id: C090
verdict: CUT
binding_line: duplicate
attack_single_est: 0.76
attack_single_range: 0.48-0.91
bo4_est: 0.85
pass4_est: 0.95
ub95_est: 0.97
gpuh_old: 12
gpuh_new_est: 96
duplicate_of: v3 05B STRONG; v3 05A STRONG
kill_reason: same complete system intervention and training or serving target
souping_flag: no
