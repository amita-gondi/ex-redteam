# C094 — Keep improving the worst-conditioned training phase — saturation screen
## 1. What the grader actually rewards
The endpoint is complete elapsed time to protected model quality, including curriculum transitions, durable checkpoints and restart work. R≈0 means the full-run competent systems floor, while R≈1 requires an attainable faster complete learning trajectory with the same durability obligations. The steady-state-only starting agent is ESTIMATED R=0.00 and the intended phase-aware reference ESTIMATED R=0.60; favorable phase attribution is explanatory evidence, not an independent reward term.
## 2. Strongest lawful combined attack
Collect complete phase traces using [PyTorch Profiler](https://docs.pytorch.org/docs/stable/profiler), stratify expensive events by frequency and critical-path contribution, and optimize the largest expected total-time savings first. Combine compiled steady-state kernels with [asynchronous distributed checkpointing](https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html), prewarming of known upcoming shapes and restart-state validation. [TorchTitan's checkpoint documentation](https://github.com/pytorch/torchtitan/blob/main/docs/checkpoint.md) provides a concrete inherited implementation family; every memory and state cost still belongs in the ledger.

A competent agent would replay a short legal transition from an inherited checkpoint, estimate how often it occurs, and compare its amortized benefit against further steady-state tuning. It should not wait for a full training run every time it wants to observe a rare phase. ESTIMATED single-run R=0.75, range 0.54–0.89; ESTIMATED best-of-4=0.84; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED projected upper-95% bound=0.95. Residual reward lies in truly unforeseen future learning phases and interactions between resource preparations and final quality. The card promises fresh dependencies but does not show that full-run profiling plus checkpoint-local replay cannot expose them cheaply.
## 3. Other routes
- A full-horizon profiler followed by critical-path tuning is ESTIMATED R=0.66, range 0.43–0.84. It directly corrects the steady-state selection mistake without a learned research allocator.
- Sweep checkpoint overlap, phase-specific batch/shape choices, prewarming and exploration reserve against complete time-to-quality: ESTIMATED R=0.72, range 0.49–0.88. Equal final quality prevents simply shortening or weakening the difficult phase.
- Use the inherited schedule but replace only synchronous checkpoint staging and repeated cold compilation: ESTIMATED R=0.49, range 0.26–0.72. This simple lawful control can be powerful when rare events account for a large share of wall time.
## 4. What would lower lawful saturation
Require a concrete earlier decision that changes the cost or learning dynamics of a later phase, with matching development evidence and an independently attainable anticipatory policy. Floor full-run profiling, local transition replay and asynchronous durability. ESTIMATED combined reward might fall to R=0.43–0.58; ESTIMATED added effort is two systems engineer-weeks and ESTIMATED 192 H100 GPU-h for real coupled trajectories. Randomly withholding a future shape is not enough if replay from a legal checkpoint reveals the entire cost. Conversely, a future phase unobservable from any permitted evidence would establish uncertainty rather than an agent research deficit.
## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 12 GPU-h. New ESTIMATED total: 480 H100 GPU-h. Assume a fixed ESTIMATED 1B learner and genuinely long repeated-exposure curriculum: ESTIMATED 4 allocation strategies × 2 seeds × 48 H100-hours = 384 GPU-h, plus ESTIMATED 48 GPU-h for phase-local probes and ESTIMATED 48 GPU-h for durability, final-quality and restart evaluation. The per-run allocation corresponds to billions of tokens at a plausible but UNMEASURED effective H100 rate. The original estimate cannot exercise a complete long-horizon training process and independently compare research allocations; it mostly prices a few trace snippets.
## 6. Duplicate check
v3 05B — MODERATE: its opened source includes exact training graphs, checkpoint state and resume, but C094 permits phase-aware allocation and grades full time-to-quality rather than fixed exact-update throughput. Catalog T03 — MODERATE: adaptive experiment allocation overlaps, yet the proposed policy is specialized to evolving training phases. The distinction is presently thin, but neither source proves the same narrow allocation intervention and quality-time endpoint.
## 7. Verdict
CUT, with ESTIMATED single-run reward 0.05 above its line and ESTIMATED best-of-4 0.24 above its cutoff. Assuming the attacker profiles the whole run and replays rare phases removes most of the difficulty attributed to an inherited agent's premature stopping.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete phase-aware optimization campaigns); grader noise UNMEASURED (planned: training-seed, transition-time and cold-restart replication); score ladder UNMEASURED (planned: steady-state agent, full-run profiler, joint phase tuning and attainable anticipatory control).
## Screen record
id: C094
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.75
attack_single_range: 0.54-0.89
bo4_est: 0.84
pass4_est: 0.96
ub95_est: 0.95
gpuh_old: 12
gpuh_new_est: 480
duplicate_of: v3 05B MODERATE; catalog T03 MODERATE
kill_reason: full run profiling and local transition replay expose rare bottlenecks
souping_flag: no
