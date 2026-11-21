# C067 — Versioned prefix caches for asynchronous learning — saturation screen
## 1. What the grader actually rewards
The scorer measures private policy success per complete GPU time while binding every reused prefix state to its actual producing weights and rollout event. A cache hit is valuable only if the resulting legal updates improve learning; relabeling stale state as current is invalid. R≈0 is the competent reset/versioning floor and R≈1 the attainable asynchronous-learning control, with all numerical scores and costs below ESTIMATED and the native success/time anchors UNMEASURED.

The reference policy for exact selective reuse nominally targets ESTIMATED R=0.60; its learning benefit over tuned full flushing is UNMEASURED.

## 2. Strongest lawful combined attack
Key each cache block by effective producing model version as well as prefix and relevant configuration. [vLLM's prefix-cache design](https://docs.vllm.ai/en/stable/design/prefix_caching/) already uses extra identity information such as adapter IDs; extending the key to a weight epoch is straightforward. Group requests by legitimate epoch, amortize synchronization over useful rollout batches, and prefill popular prefixes only after a version switch when the expected reuse repays the rebuild.

For localized updates, compute an architectural dependency closure: a change upstream of a cached layer invalidates its derived keys/values, while provably unchanged subgraphs can retain state. Do not approximate dense changed-weight caches as exact. Retain correctly labeled older-policy rollouts only if the objective permits them, with version-aware importance handling inspired by [IMPALA](https://arxiv.org/abs/1802.01561); that source establishes an off-policy actor/learner method, not permission to alter this task's frozen objective. Tune epoch length, rollout age and prefix grouping jointly, comparing complete flush as a serious control.

ESTIMATED single-run R=0.70, range 0.48–0.86; ESTIMATED best-of-4=0.80; ESTIMATED pass@4 at R≥0.60=0.91; ESTIMATED upper-95% projection=0.93. The forecast is for a tuned transfer implementation beyond frozen calibration, not a result after placing that implementation at the floor. The residual is learning lost while amortizing policy updates and rebuild work that exact dependencies cannot avoid. Dense updates usually invalidate far more state than the phrase “localized weight update” suggests. That can make selective reuse physically unhelpful, in which case a sophisticated cache policy does not create scientific reserve.

## 3. Other routes
Full flushing with tuned synchronization and request batching has ESTIMATED R=0.60, range 0.36–0.79. It directly addresses correctness and may win if most updates change every cached layer.

A bounded scheduling sweep over update interval, shared-prefix grouping, prefill regeneration and permitted rollout age has ESTIMATED R=0.67, range 0.44–0.84. A dependency-only selective cache, without learning-aware scheduling, has ESTIMATED R=0.52, range 0.29–0.73. None of these methods can legally reuse old activations under new producing weights merely because token strings match.

## 4. What would lower lawful saturation
Freeze the allowed update locality and objective semantics, demonstrate genuinely reusable exact subgraphs, and create held-out interactions where reuse value trades off with measurable later learning. Match development prefix families and update frequencies. ESTIMATED resulting attack R=0.46–0.61; retention would still require margin checks. ESTIMATED preparation is 10–15 person-days and ESTIMATED 432 H100-h for a reduced asynchronous campaign comparison. If dense updates eliminate all reuse, cut rather than scoring a reference with an unachievable state-sharing advantage.

## 5. Decisive-check GPU-h re-estimate
Old card budget: ESTIMATED 14 GPU-h. New ESTIMATED 432 H100-GPU-h assumes an ESTIMATED 1B policy/learner and an ESTIMATED 1B reference model, ESTIMATED 4 cache/schedule arms×3 seeds×8 cluster-hours×4 H100s=384. Independent policy-success evaluation, fresh-prefix rebuild accounting and cold epoch transitions add ESTIMATED 48, totaling ESTIMATED 432. Rollout and update work share that allocation; no remote teacher is assumed free. The old allowance can show a cache invalidation failure, but not determine whether a selective policy improves sample efficiency after charging synchronization and regeneration.

## 6. Duplicate check
04A: MODERATE after reading its source. Policy-version consistency, cache boundaries and useful asynchronous learning are already central there, but this dense-policy intervention focuses prefix-state reuse rather than MoE routing/replay consistency. 05A: MODERATE because exact prefix reuse contributes to serving capacity, while it does not grade policy improvement through weight updates. The dense versus MoE distinction alone would be weak novelty; the exact reuse/learning tradeoff must carry it.

## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds the binding threshold by 0.20, and ESTIMATED pass@4 exceeds its threshold by 0.41. The single-run point touches rather than exceeds its strict line, but that does not rescue the card from repeated-search saturation. Standard version keys and ordinary asynchronous scheduling cover much of the stated mechanism.

## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget cache/schedule research on fresh update histories); grader noise UNMEASURED (planned: replay fixed policies with separate rollout and learner seeds); score ladder UNMEASURED (planned: reset-only, epoch grouping, exact dependency reuse, permitted stale-rollout correction and attainable learning control).

## Screen record
id: C067
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.70
attack_single_range: 0.48-0.86
bo4_est: 0.80
pass4_est: 0.91
ub95_est: 0.93
gpuh_old: 14
gpuh_new_est: 432
duplicate_of: 04A MODERATE; 05A MODERATE
kill_reason: version-correct caching plus synchronization search likely exceeds tail limits
souping_flag: no
