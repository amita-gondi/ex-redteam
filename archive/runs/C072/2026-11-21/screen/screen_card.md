# C072 — Crash-consistent experience buffers that preserve learning — saturation screen
## 1. What the grader actually rewards
After a forced crash, the learner must resume with an auditable accounting of sampled, durable, consumed and deliberately discarded groups, then achieve policy utility within the total runtime allowance. Saving weights while silently changing exposure does not satisfy that state contract. R≈0 is the competent complete-queue checkpoint floor and R≈1 the stronger attainable interrupted-learning control; all quantitative judgments below are ESTIMATED because native learning and persistence costs are UNMEASURED.

Value-aware durable experience is the proposed ESTIMATED R=0.60 reference, without measured proof that complete replay persistence leaves useful additional learning.

## 2. Strongest lawful combined attack
Persist an append-only rollout journal with unique group IDs, producing policy versions, completion status and consumption offsets, and commit its frontier atomically with the learner checkpoint. Use bounded asynchronous writes and backpressure so acknowledgement means durability, not merely a queued copy. [SQLite's atomic-commit account](https://www.sqlite.org/atomiccommit.html) verifies the general transaction principle; it is not a claim that serializing large tensors through SQLite is the best implementation.

Import a mature asynchronous replay-checkpoint design where compatible. [NeMo RL's single-controller guide](https://docs.nvidia.com/nemo/rl/latest/guides/single-controller.html) explicitly groups replay, dataloader, controller and unfinished-rollout state in committed snapshots, while its [async GRPO guide](https://docs.nvidia.com/nemo/rl/latest/guides/async-grpo.html) discusses replay-buffer restoration. Layer age-aware admission and bounded queue depth onto that foundation, pricing new generation against old-group training value. Compare writing all pending token/metadata records with selective persistence; text rollouts may be cheap beside model and optimizer checkpoints.

ESTIMATED single-run R=0.78, range 0.57–0.91; ESTIMATED best-of-4=0.87; ESTIMATED pass@4 at R≥0.60=0.97; ESTIMATED upper-95% projected score=0.96. These are scenario estimates beyond a frozen complete control, not observed recovery reliability. Remaining loss comes from storage contention and choosing whether stale trajectories still repay training. The card gives no queue size, storage bandwidth or interruption regime proving that full persistence is genuinely expensive. Without that evidence, ordinary crash consistency plus queue bounds is likely to capture most useful gain.

## 3. Other routes
Complete replay persistence with atomic checkpoint metadata is the strongest single standard recipe: ESTIMATED R=0.70, range 0.47–0.86. It should be the main baseline, not weights-only restore, because the scientific extension begins after buffer persistence.

A search over checkpoint interval, queue high-water mark, age cutoff and asynchronous write batch size yields ESTIMATED R=0.75, range 0.52–0.89. All reconstruction and discarded generation work stays charged. Regenerating a frontier from a rewound dataloader can also be lawful when every sampled group is reconciled and the contract permits changed exposure; it must not masquerade as restoring the same experience.

## 4. What would lower lawful saturation
Establish realistic storage contention where complete persistence materially competes with learning, and use supported reward delays that change which pending groups matter after restart. Publish whether groups may be intentionally dropped and how exposure changes affect validity, then hold out delay/crash couplings with matching development signals. ESTIMATED revised attack R=0.48–0.64. ESTIMATED authoring cost is 10–16 person-days plus ESTIMATED 480 H100-h for a first interrupted-learning study. Artificially slowing durable storage only to defeat the baseline would need a defensible deployment motivation.

## 5. Decisive-check GPU-h re-estimate
Old card budget: ESTIMATED 12 GPU-h. New ESTIMATED 480 H100-GPU-h assumes an ESTIMATED 3B policy and necessary ESTIMATED 3B reference components, ESTIMATED 4 persistence policies×3 seeds×8 cluster-hours×4 H100s=384 for training and rollouts. Forced-crash/restart overhead and complete group-ledger replay add ESTIMATED 48; independent private-success evaluation adds ESTIMATED 48. Total ESTIMATED 384+48+48=480. Storage is a separately specified resource, not a GPU-hour proxy. The former estimate can expose a dropped buffer, but it cannot determine the learning value of selective persistence under repeated real interruptions.

## 6. Duplicate check
05B: MODERATE from its source; exact resumable training state is already central, but this task permits choosing pending experience whose learning value changes with age rather than preserving a fixed update trajectory. 04A: MODERATE because asynchronous rollout age and policy utility overlap, while forced durable restoration is a different intervention. If the new task ultimately requires exact replay of every group, its claimed distinction from 05B would narrow substantially.

## 7. Verdict
CUT. ESTIMATED best-of-4 is 0.27 above the binding threshold; ESTIMATED single-run reward exceeds its line by 0.08. Verified replay-checkpoint implementations and conventional transactions provide a strong whole-stack route, and the storage/learning tradeoff needed to escape it is currently unspecified.

## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget buffer-policy research on fresh crash/delay histories); grader noise UNMEASURED (planned: repeated fixed-policy interrupted training with full event reconciliation); score ladder UNMEASURED (planned: weights-only negative, complete queue journal, async persistence, age-aware admission and attainable interrupted-learning control).

## Screen record
id: C072
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.78
attack_single_range: 0.57-0.91
bo4_est: 0.87
pass4_est: 0.97
ub95_est: 0.96
gpuh_old: 12
gpuh_new_est: 480
duplicate_of: 05B MODERATE; 04A MODERATE
kill_reason: mature complete replay persistence likely removes useful recovery gap
souping_flag: no
