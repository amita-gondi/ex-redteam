# C018 — Checkpoint faster by recomputing the right state — saturation screen
## 1. What the grader actually rewards
Only durable optimizer-equivalent progress counts, including checkpoint writes, an unexpected kill, reconstruction and verified post-resume updates. Omitting state is profitable only when reconstructing it is cheaper overall and preserves the trusted trajectory. ESTIMATED R≈0 denotes the healthy complete-state checkpoint floor and ESTIMATED R≈1 an attainable stronger durable-progress control; the inherited serializer is provisionally ESTIMATED R=0.00, reference ESTIMATED R=0.60, and all native update-rate anchors are missing.
## 2. Strongest lawful combined attack
Replace synchronous serialization with consistent asynchronous staged saves, incremental dirty-state tracking where useful, and explicit provenance for every omitted derived buffer. [PyTorch's asynchronous distributed checkpoint recipe](https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html), verified in this review's web searches, supplies a concrete implementation path. [CheckFreq](https://www.usenix.org/conference/fast21/presentation/mohan) supplies iteration-level persistence and save-frequency profiling. Add dependency-cost analysis inspired by [Checkmate](https://arxiv.org/abs/1910.02653), while recognizing that activation rematerialization does not permit dropping irrecoverable optimizer history.

Classify tensors into indispensable history, reproducible function of saved state, and disposable runtime caches. Preserve moments, RNG and data position unless an exact legal reconstruction exists; rebuild graph captures, deterministic position buffers and cheap derived layouts from saved ancestors. Profile write bandwidth and reconstruction costs on public graph partitions, solve a small omission/retention optimization, then tune save cadence and overlap jointly. Freeze state before asynchronous copying so the saved model and optimizer represent one real update. Cold kill/resume conformance tests must compare later updates from the actual delivered files, not a separately prepared full checkpoint.

ESTIMATED single-run R=0.83, range 0.64–0.94; ESTIMATED oracle best-of-4=0.89; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED upper-95% projection envelope=0.98. These are provisional saturation forecasts. Most reward appears obtainable from mature persistence and a conservative cheap-buffer omission policy. The residual is phase-dependent reconstruction cost and complicated state aliasing, but dependency analysis plus a modest parameter sweep is a credible complete answer. Arbitrary tensor volume increases engineering load without creating a different scientific choice.
## 3. Other routes
- Complete-state asynchronous checkpointing with ordinary cadence tuning: ESTIMATED R=0.69, range 0.45–0.87. It could consume the entire useful range without omitting anything scientifically interesting.
- Enumerate safe omission subsets after CPU dependency analysis, then search cadence, write chunk sizes and staging depth with full restart cost. ESTIMATED R=0.79, range 0.57–0.92. Most unsafe choices can be rejected before costly learning trajectories.
- Save an earlier complete state plus a deterministic replay log. ESTIMATED R=0.64, range 0.35–0.86 if replay work and all required inputs fit the same storage/runtime envelope. This legal route trades write volume for recomputation and must count replayed updates only once.
## 4. What would lower lawful saturation
Begin from a tuned asynchronous checkpoint stack and construct phase transitions where derived-state regeneration changes future communication or layout costs. Require an online omission choice based on observable upcoming-work evidence rather than a fixed tensor whitelist. A same-budget stronger control must show real reserve after restore overhead. Forecast with that redesign: ESTIMATED R=0.48, range 0.26–0.71. Cost is ESTIMATED several weeks of distributed-state authoring and ESTIMATED 128 additional H100 GPU-h for phase-crossed durability tests. If no reconstructible state remains after mature controls, retire the task rather than invent an unattainable ceiling.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 8 GPU-h. New ESTIMATED 64 H100 GPU-h assumes an ESTIMATED 3B-parameter transformer using ESTIMATED 2 H100s, ESTIMATED 4 checkpoint arms, ESTIMATED 3 workload/failure-placement seeds per arm and ESTIMATED 2 elapsed hours per save–kill–resume trajectory: ESTIMATED 4×3×2×2=48 GPU-h. Add ESTIMATED 8 GPU-h for configuration search and ESTIMATED 8 GPU-h for exact post-resume comparison, giving ESTIMATED 64. Long fresh pretraining is unnecessary because this grader requires equivalent update execution rather than proving a new statistical learning effect. The old micro-pilot is directionally sensible but omits stack comparisons and failure-location variation.
## 6. Duplicate check
v3 05B (`task_design_v3_codex/05_exact_systems.md`, task and reward source opened): STRONG. Its stated intervention combines overlap and recomputation with correct checkpoint/state transitions, and its reward explicitly amortizes persistence costs while checking cold-resumed updates. C018 restricts that existing treatment to reconstructible saved state without adding a scientific endpoint or a workload interaction beyond the earlier contract. The overlap concerns both the implementation intervention and the durable exact-progress target.
## 7. Verdict
CUT, binding duplicate, with independent saturation grounds as well. The ESTIMATED best-of-four breach is 0.29 and the single-run breach ESTIMATED 0.13. A new omission-specific causal mechanism would need to change the intervention/target pair before this merits a separate card.
## 8. Measurement status
Rollouts UNMEASURED (planned: asynchronous/incremental/reconstruction attacks under full persistence accounting). Grader noise UNMEASURED (planned: repeated cold process starts and storage-load blocks). Score ladder UNMEASURED (planned: inherited serialization, tuned full saves, safe omission, replay-log control and stronger durable-progress implementation).
## Screen record
id: C018
verdict: CUT
binding_line: duplicate
attack_single_est: 0.83
attack_single_range: 0.64-0.94
bo4_est: 0.89
pass4_est: 0.99
ub95_est: 0.98
gpuh_old: 8
gpuh_new_est: 64
duplicate_of: v3-05B STRONG
kill_reason: checkpoint intervention and durable exact-update grader already exist
souping_flag: no
