# C075 — Rollback research branches that stay rolled back — saturation screen
## 1. What the grader actually rewards
The chosen branch must survive a kill with its intended weights, optimizer history and ancestry intact, and final reward follows the best valid model reached under joint runtime and storage limits. A newer directory from an abandoned run is not a valid continuation of the selected hypothesis. R≈0 is the competent immutable-checkpoint floor and R≈1 the attainable storage-efficient campaign control; every numerical forecast here is ESTIMATED because the model-quality/storage frontier is UNMEASURED.

Storage-aware reference retention is provisionally targeted at ESTIMATED R=0.60, but its additional final-model quality over conventional snapshots is UNMEASURED.

## 2. Strongest lawful combined attack
Give every branch an immutable identity and explicit parent manifest, commit complete checkpoint metadata atomically, and make restart follow a selected committed manifest rather than a step-number glob. Use [PyTorch Distributed Checkpoint](https://docs.pytorch.org/docs/main/distributed/checkpoint.html) for state serialization and its documented [asynchronous save/staging recipe](https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html) to overlap persistence safely. A save acknowledgement must follow complete durable state, and delayed writes from abandoned branches must not update the selected pointer.

Add exact content-addressed chunk storage for unchanged checkpoint bytes, with immutable references and copy-on-write isolation for all live optimizer tensors. This is lossless storage deduplication, never parameter averaging or any alteration of model values. Retain the incumbent and live branch ancestors, collect unreachable chunks only after manifest publication, and limit exploratory branching by measured storage. Tune branch width, checkpoint interval and eviction using ordinary incumbent value and recomputation cost; compare against full copies first.

ESTIMATED single-run R=0.83, range 0.64–0.94; ESTIMATED best-of-4=0.90; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED upper-95% projection=0.98. These are planning scenarios beyond frozen checkpoint controls, not crash tests. The remainder is a real tradeoff between retaining uncertain alternatives and spending storage on the incumbent. However, a bounded beam and full-copy snapshots may already explore enough recipes to maximize useful quality. The card does not establish that many retained branches are simultaneously necessary or that exact deduplication leaves a hard decision.

## 3. Other routes
Immutable complete snapshots with a small best-first branch beam are the strongest single recipe: ESTIMATED R=0.74, range 0.52–0.89. Correct ancestry handles the reported failure without requiring a novel storage representation.

A sweep over retention count, branch width, snapshot cadence, exact chunk size and prune threshold has ESTIMATED R=0.80, range 0.59–0.93. It selects against actual final model utility and cold-resume correctness. Deleting a branch and regenerating it later is lawful only when its recomputation and randomness contract are fully charged; no saved-state recovery can be assumed from discarded bytes.

## 4. What would lower lawful saturation
Demonstrate supported delayed recipe reversals where early losers become valuable and cannot all be kept as full snapshots, with storage costs derived from actual model and optimizer states. Provide equivalent development reversals and an executable reference that improves final utility through better retained ancestry. ESTIMATED combined R after redesign is 0.50–0.66. ESTIMATED work is 9–14 person-days plus ESTIMATED 320 H100-h for a campaign pilot. If a small conventional beam matches the reference, the task remains ordinary checkpoint engineering despite private kill points.

## 5. Decisive-check GPU-h re-estimate
Old budget: ESTIMATED 8 GPU-h. New ESTIMATED 320 H100-GPU-h assumes an ESTIMATED 1B training subject, ESTIMATED 4 retention implementations×3 campaign seeds×20 H100-h of real branch training and replay=240. Cold kills and complete optimizer-ancestry verification add ESTIMATED 48; independent held-out model evaluation and asynchronous persistence profiling add ESTIMATED 32. Total ESTIMATED 240+48+32=320. Branch exploration work is included even when those branches are later discarded. The original amount could reproduce the overwrite and prove one resume path, but it does not establish whether saved storage buys better scientific search.

## 6. Duplicate check
T03: MODERATE after reading its controller packet, which already retains reversible ancestor state and scores actual training outcomes, but this artifact specifically changes branch persistence and storage rather than the entire research policy. 05B: MODERATE from its exact-resume source; checkpoint lineage and optimizer state overlap, while C075 allows different branch allocations to improve model quality instead of accelerating a fixed update graph. Neither identity is strong enough to cut solely as a duplicate.

## 7. Verdict
CUT. ESTIMATED single-run reward exceeds the binding line by 0.13 and best-of-4 exceeds its line by 0.30. Mature immutable snapshots, transactional selection and bounded branch retention are a capable complete recipe; no demonstrated storage-dependent research residual presently defeats them.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget branch-persistence implementations on fresh kill histories); grader noise UNMEASURED (planned: repeated fixed-policy branch campaigns with independent training seeds); score ladder UNMEASURED (planned: collision negative, immutable full copies, bounded beam, exact chunk storage and attainable storage-aware campaign control).

## Screen record
id: C075
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.83
attack_single_range: 0.64-0.94
bo4_est: 0.90
pass4_est: 0.99
ub95_est: 0.98
gpuh_old: 8
gpuh_new_est: 320
duplicate_of: T03 MODERATE; 05B MODERATE
kill_reason: immutable checkpoint DAG and bounded retention likely solve the storage extension
souping_flag: no
