# C036 — Recover useful output from preemptible inference leases — saturation screen
## 1. What the grader actually rewards
Only exact output acknowledged durably before lease loss contributes, and a fresh worker must restore the submitted state successfully. Consumed lease time includes transfer and repeated prefix computation, so frequent snapshots and prompt restart have different measurable costs. ESTIMATED R≈0 corresponds to a competent restart/checkpoint floor and ESTIMATED R≈1 to attainable durable progress; the reference is provisionally ESTIMATED R=0.60 and prompt-only restart near ESTIMATED R=0.00.
## 2. Strongest lawful combined attack
Combine a write-ahead output log with periodic cache checkpoints, asynchronous durable transfer and phase-conditioned interruption estimates. [SpotServe](https://arxiv.org/abs/2311.15566) directly studies generative inference on preemptible instances. [Llumnix](https://arxiv.org/abs/2406.03243) establishes efficient request/state migration; adapting its transfer machinery to acknowledged durable storage still requires explicit cold-worker validation.

Persist token IDs, decoder randomness, tool receipts and committed ancestry cheaply; save large KV blocks only when their expected recomputation cost exceeds persistence cost. Use incremental snapshots with checksummed manifests and an atomic commit marker. At a clean restart reconstruct missing cache blocks from the durable token log, preserving exact decoding semantics. Fit a hazard-dependent checkpoint interval and allow special snapshots at expensive prefill or tool boundaries. A full-budget researcher can sweep these few policy parameters and compare them with a simple periodic schedule.

ESTIMATED single-run R=0.69, range ESTIMATED 0.44–0.86; ESTIMATED best-of-4=0.78; ESTIMATED pass@4 at R≥0.60=0.88; ESTIMATED upper-95% projection=0.92. The provisional score credits avoiding most long-prefix rework while keeping persistence off the critical path. The residual is irreversible work lost without warning, storage stalls and changing value of future branches. Unlike the card's framing, reasoning tokens themselves generally have ordinary decoder-state costs; a scientific distinction needs actual expensive state or tool dependencies rather than labeling phases as reasoning.
## 3. Other routes
Periodic decoder checkpoints plus durable output logging yield ESTIMATED R=0.58, range ESTIMATED 0.33–0.78. They are strong when interruption hazard and state size are stable.

A sweep over checkpoint interval, incremental block size, cache-versus-recompute threshold and asynchronous transfer depth reaches ESTIMATED R=0.64, range ESTIMATED 0.39–0.83. Candidate preparation and discarded trials must consume the same discovery budget. A lawful token-log-only route gives ESTIMATED R=0.45, range ESTIMATED 0.21–0.68: it avoids losing committed answers while recomputing KV on each lease, potentially adequate for short contexts or slow storage.
## 4. What would lower lawful saturation
Build tasks in which durable state has branching future value, lease hazard depends observably on current workload, and deciding what to persist competes with useful inference under a hard storage cap. Provide matched development continuation information and a feasible stronger policy. ESTIMATED composite R could decline to 0.46–0.58, at ESTIMATED three author-weeks and ESTIMATED 48 H100 GPU-h for independent interruption traces. This is a plausible redesign, but it must beat cost-aware checkpointing rather than merely introduce more interruptions or reduce storage below feasibility.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 6 GPU-h. Revised ESTIMATED 18 H100 GPU-h assumes an ESTIMATED 7B model, ESTIMATED four persistence arms, ESTIMATED three independent lease processes, and ESTIMATED one H100-hour of aggregate consumed leases per arm/process: ESTIMATED 4×3×1=12. Add ESTIMATED 4 GPU-h for replacement-worker restore checks and ESTIMATED 2 GPU-h for reference token generation and warmup. No training is required; storage latency is real elapsed time and must remain in service accounting. The old budget tests a restart mechanism but not the changing state-value hypothesis.
## 6. Duplicate check
05A: MODERATE; exact inference service is shared, but repeated external lease loss and durable completion add a distinct target. 05B: WEAK after reading its cold-resume contract, because it persists training/optimizer state and scores update throughput. Both provide useful baseline machinery without matching this inference intervention exactly.
## 7. Verdict
CUT, driven by ESTIMATED best-of-four excess 0.18 and pass@4 excess 0.38. The point single-run estimate lies below its line, but repeated search and a high projected tail invalidate a pass. The proposed branching-state revision would need a fresh screen.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete interrupted service across cold leases). Grader noise UNMEASURED (planned: identical artifacts on repeated storage and lease traces). Score ladder UNMEASURED (planned: prompt restart, token log, periodic cache and value-aware persistence).
## Screen record
id: C036
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.69
attack_single_range: 0.44-0.86
bo4_est: 0.78
pass4_est: 0.88
ub95_est: 0.92
gpuh_old: 6
gpuh_new_est: 18
duplicate_of: 05A MODERATE; 05B WEAK
kill_reason: durable logs and adaptive checkpoint schedules recover most progress
souping_flag: no
