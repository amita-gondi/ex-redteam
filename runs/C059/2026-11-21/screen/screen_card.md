# C059 — Grammar staging after the public fix is already applied — saturation screen
## 1. What the grader actually rewards
This is exact structured-generation goodput after the competent allocation repair, including host mask construction and transfer time in the request interval. Grammar validity alone is insufficient: the timed outputs must satisfy the promised exact decoding semantics, with failed requests retained. R≈0 is the repaired competent engine floor, including buffer reuse; R≈1 is the attainable faster engine under the same workload, and every performance or budget number below is ESTIMATED because those anchors are UNMEASURED.

The custom mask-update reference carries an ESTIMATED R=0.60 design target; its throughput advantage after mature dynamic-engine replacement is unknown.

## 2. Strongest lawful combined attack
Begin with whole-backend replacement rather than polishing the reported staging call. [XGrammar](https://arxiv.org/abs/2411.15100) combines prechecked token classes, persistent parsing state and overlap with model execution. More directly, [XGrammar 2](https://arxiv.org/abs/2601.04426) addresses dynamic structured generation with dispatch semantics, compilation and cross-grammar reuse. Those verified public methods weaken the claim that changing schemas necessarily leaves an unfamiliar residual after allocation repair.

Attach parser state and mask-buffer ownership to stable request identities, not transient batch positions. Maintain generation counters when slots are recycled, stage mask deltas only when profitable, and overlap host parsing with previous GPU work using explicit dependencies. Compare delta updates with full reusable pinned-buffer copies across actual vocabulary sizes and churn. The attacker tunes complete throughput after matched warmup and validates the exact timed tokens; a fast but semantically stale mask is a failure.

ESTIMATED single-run R=0.86, range 0.71–0.95; ESTIMATED best-of-4=0.92; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% bound=0.99. Public engine results are not measurements of this card, and these forecasts assume a frozen calibration baseline predating stronger workload-specific integration. If the imported engine already defines the floor, an independently demonstrated native reserve is required instead. The residual is irregular parser work and synchronization at state changes, but ordinary identity-safe scheduling directly handles batch reordering. The [reported staging regression](https://github.com/vllm-project/vllm/issues/49013) was verified to exist; its reported measurements are not independently reproduced here.

## 3. Other routes
An unmodified mature dynamic grammar backend with reusable staging is the strongest single recipe: ESTIMATED R=0.77, range 0.57–0.92. The reward must be measured against that control before attributing gains to a custom delta representation.

Autotune full versus delta masks, staging chunk size, parser-thread allocation and overlap depth under exact output checks. ESTIMATED R=0.83, range 0.64–0.94. A shape-specific fast path remains lawful when it generalizes across fresh schema contents; its brevity does not justify exclusion. Host synchronization must remain inside the complete cost ledger.

## 4. What would lower lawful saturation
Use independently authored dynamic grammars with request cancellation, schema mutation and slot reuse that create genuinely coupled parser-state lifetimes. Preserve the same disclosed semantics in development, permit complete backend replacement, and compare against the latest compatible dynamic engine. ESTIMATED revised attack R=0.59–0.75, so even this extension is likely unsafe. ESTIMATED work is 5–8 person-days plus ESTIMATED 24 H100-h for correctness and throughput pilots. If full-mask staging is already near the constrained ceiling, cut the task rather than widening normalization around a negligible difference.

## 5. Decisive-check GPU-h re-estimate
Old card amount: ESTIMATED 5 GPU-h. New ESTIMATED 24 H100-GPU-h assumes an ESTIMATED 8B serving model, ESTIMATED 4 backends/configurations×3 workload seeds×1.5 device-hours =18, with ESTIMATED 6 for parser compilation, disjoint warmup, independent token verification and repeated timing. Total ESTIMATED 18+6=24 on H100. No model training is involved. A CPU parser microbenchmark is a useful preliminary falsifier, but the old budget is optimistic for end-to-end comparisons under dynamic batches and repeated matched timing.

## 6. Duplicate check
05A: MODERATE after reading its serving-system source. It permits whole-engine replacement and grades exact useful serving capacity, but its named coupling is sessions/adapters/model shapes rather than grammar-state transitions. 05B: WEAK in the same inspected file because exact execution and state semantics overlap, while distributed training updates are a different target. This is a narrow specialization, not a demonstrated STRONG duplicate.

## 7. Verdict
CUT. The ESTIMATED single-run estimate exceeds its binding limit by 0.16; repeated-search and projection estimates are also far above their lines. A verified public dynamic grammar engine attacks the proposed extension itself, beyond the simpler buffer-allocation repair.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent engine-integration attempts under the full research budget); grader noise UNMEASURED (planned: repeated warmed complete-request timing with fixed artifacts); score ladder UNMEASURED (planned: repaired staging, mature dynamic backend, identity-safe scheduling, delta tuning and attainable exact control).

## Screen record
id: C059
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.86
attack_single_range: 0.71-0.95
bo4_est: 0.92
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 5
gpuh_new_est: 24
duplicate_of: 05A MODERATE; 05B WEAK
kill_reason: mature dynamic grammar replacement already targets the residual
souping_flag: no
