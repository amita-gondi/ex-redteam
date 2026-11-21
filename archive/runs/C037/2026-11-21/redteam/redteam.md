# C037: Co-schedule draft training and target inference — independent adversarial review

**Verdict: CUT.** Online draft adaptation and feedback-driven speculation control are established methods, and a cost-aware refresh threshold joins them naturally. The card offers no specified delayed interaction that defeats that complete controller; merely observing that periodic retraining can be wasteful does not create a durable research obstacle.

Source file: `/workspace/task_ideation_v4_creative/cards/C037.md`.

The assessment used the proposal and checked literature only. There is no supplied serving executable, update-config filename or resource-meter implementation to audit. References to the target server, draft updater, shared-pool supervisor and prompt replayer denote the proposed processes. Reward estimates are ESTIMATED conditional scenarios because the card never defines its reward anchors.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Profile the refresh break-even point | Estimate accepted-token gain, remaining demand and update cost from legal telemetry; update only when projected saved target work exceeds training/synchronization cost. | ESTIMATED 0.74–0.93 | No: this addresses the exact economic failure attributed to periodic refresh. | Strong online cost-model and receding-horizon controller with tuned uncertainty margin, not just periodic scheduling. | ESTIMATED 0.74–0.93 | A small threshold table may cover every drift regime. |
| Reuse verification data for cheap adaptation | Cache admitted target verification distributions or generated tokens, distill on recent rejected draft regions, and pause micro-updates during measured contention. | ESTIMATED 0.66–0.88 | Data generation is charged, but already-performed useful target work may be legally reused. | Count capture/storage and backward work; include on-policy selective distillation from already-metered verification. | ESTIMATED 0.63–0.86 | The card may overestimate the extra teacher cost of online adaptation. |
| Win by disabling adaptation or speculation | Use target-only serving during bad acceptance, retain a competent frozen draft otherwise, and stop retraining when the horizon is short. | ESTIMATED 0.61–0.86 | No-op and mode-switch baselines are absent. | Full-budget best frozen, target-only and adaptive-speculation controls with unchanged outputs and service obligations. | ESTIMATED 0.58–0.84 | If these reach reference, the online training problem contributes no reserve. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read the private future prompt trace via replayer descriptors or scheduler shared memory; alter fixed target weights or trusted verification kernels. | ESTIMATED 0.97–1.00 | Shared-pool metering does not isolate future inputs or the target. | Causal prompt broker, immutable target/runtime, separate trace namespace and live descriptor/IPC mutation tests. | ESTIMATED 0.00 | A monitoring endpoint may expose future arrival or family labels. |
| Interface or encoded-state smuggling | Put a pretrained future-domain draft or lookup outputs in refresh configs, compressed constants or checkpoint sidecars; load them as an apparent online update. | ESTIMATED 0.87–1.00 | No artifact grammar or state provenance is provided. | Trusted draft initialization/update lineage, aggregate source/config bounds and no unreceipted state imports. | ESTIMATED 0.00 | Efficient legal draft architecture/config changes must remain admitted when the contract allows them. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Declare target verification completed from acceptance counters; skip verifier calls; recognize copy-like positive prompts or sibling output hashes. | ESTIMATED 1.00 | Charging verification is not proof that verified outputs exist. | Parent captures actual target-corrected tokens and completion; independently authored positive requests and fake-counter/abort regressions. | ESTIMATED 0.00 | Correctness only on a separate slow test path cannot validate timed service. |
| Timing/check-decoupling/branch laundering | Launch draft updates off-pool or before start, time serving alone, defer device synchronization, or swap a validated draft for another warmed branch. | ESTIMATED 0.91–1.00 | The card explicitly requires one resource meter; enforcement remains unwritten. | Supervisor accounts every device/process and ancestor from initialization through synchronized completion; freeze the exact timed config and state. | ESTIMATED 0.00 | Shared contexts or overlapping jobs can evade naive sums of per-process event times. |
| Dev-hidden leakage/cue inference | Detect drift boundaries from trace ordering, filename, timestamps or protected-only prompt tags and refresh just before the private transition. | ESTIMATED 0.76–0.98 | Matching contention and delay distributions does not remove boundary cues. | Cross trace packaging and family transitions; hold out whole prompt provenance and test metadata-only schedules. | ESTIMATED 0.19–0.47 | A legitimate content classifier may still identify drift immediately. |
| Adaptive aggregate oracle | Tune refresh periods, update sizes and speculation length against repeated private throughput aggregates; infer the remaining service horizon by perturbation. | ESTIMATED 0.70–0.92 | Query quotas and trace reuse are unspecified. | Protected dev with global call accounting, final trace independence and complete legal adaptive scheduler baseline. | ESTIMATED 0.51–0.80 | The scheduling surface may be low-dimensional enough for cheap search. |
| Slice abandonment/denominator optimization | Admit short requests only, truncate difficult generations, starve the shifted family or count allocated/active GPU time selectively. | ESTIMATED 0.71–0.97 | Exact outputs are required but offered-load, timeout and denominator semantics are missing. | Fixed offered prompt/output obligations, request-family floors and all-pool time from one authoritative clock; failed slots remain present. | ESTIMATED 0.30–0.63 | Good throughput scheduling can still trade long requests away without a native service-quality constraint. |
| Strongest lawful combined recipe | Couple on-policy draft distillation and recent-data sampling to a profiled net-savings refresh controller; adapt speculation length and use target-only/frozen fallbacks when updates do not repay. | ESTIMATED 0.78 (ESTIMATED 0.58–0.95) | This is allowed scheduling and training configuration. | Execute the complete compatible controller at the full reservation before investing in reference decomposition. | ESTIMATED 0.78 (ESTIMATED 0.58–0.95) | Isolation and honest GPU accounting do not invalidate a good cost model. |

## Published recipe shortcut — web checked

- [Online Speculative Decoding](https://arxiv.org/abs/2310.07177) explicitly updates drafts on observed queries using distillation, directly covering adaptation to changing serving inputs.
- [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://arxiv.org/abs/2310.08461) supplies draft/target alignment as a known training intervention; its use still needs the task's full teacher and update costs.
- [TurboSpec: Closed-loop Speculation Control System for Optimizing LLM Serving Goodput](https://arxiv.org/abs/2406.14066) profiles the execution environment and adjusts speculation through feedback, supporting the serving-side control component.

The first and third primary abstracts were opened; DistillSpec was found as a primary paper result in this session. No code compatibility or hardware performance was verified. Combining a refresh economics rule with these components is my attack construction, not an asserted turnkey published system. Its strongest-lawful reward forecast is ESTIMATED 0.78, with ESTIMATED scenario range 0.58–0.95; no external latency gains enter that forecast.

## Saturation against the hypothetical 10T researcher / 12h

A strong researcher would separate the effect of an update on acceptance from its net effect on completed service. For each recent prompt cluster, it can measure accepted draft lengths, draft/target costs and queued work, then allocate a small update only when the likely savings repay the opportunity cost. Drift detection, a cooldown period and uncertainty-aware threshold tuning are ordinary engineering. The card's one-transition pilot is especially friendly to a threshold solution: it does not yet force a long sequence of investments whose value changes after earlier update choices.

The full-budget saturation scenario gives single-run maximum ESTIMATED 0.93, oracle best-of-4 mean ESTIMATED 0.86, and pass@4 ESTIMATED 0.95 at the binding R>=0.60 success threshold. Compare those with the source hard kills >0.70, >0.60 and >0.50 respectively: each is likely exceeded. The projected upper-95% endpoint for stronger-tier or expanded-compute research is ESTIMATED 0.99, above the binding >=0.75 line. It is an explicitly ESTIMATED risk endpoint, not a fitted statistical projection or target-model measurement.

S1 is OPEN without a same-envelope stronger schedule and independently demonstrated throughput reserve. Even a perfect draft has finite speedup once verification, batching and shared training resources dominate; that physical roof must be measured rather than assumed. S7 is OPEN until the achievable reward ceiling is bracketed. A tiny room for scheduling improvement cannot be inflated into research headroom by narrowing the reward scale. All proposed controls must serve the same target model and correct sampling contract.

Rollout rewards, observed run counts and observed pass@k are UNMEASURED. Planned evaluation uses independent full-budget controller searches on fresh prompt-family sequences, preserving every failed branch and reporting legal-dev-selected and hidden-oracle winners separately. Grader noise is UNMEASURED; measure frozen schedules repeatedly with real-shape warmup, matched clocks and host variation. Separate outer researcher tokens, serial search time, concurrent trials and subject GPU work in any sweep. The supplied weakness reports' early-stopping anecdotes do not slow a hypothetical researcher that profiles correctly and persists throughout its budget.

## Revised estimate versus the source card

The designer gives source ESTIMATED 0.44 to periodic distillation plus speculation tuning and peak avoidance. I raise the estimate to ESTIMATED 0.78 because the lawful controller need not be periodic: it can explicitly estimate the marginal value of refreshing, keep a frozen option and switch speculation off when the workload is unfavorable. The source's stated failure case—training when contention makes the draft economically worthless—is precisely what an ordinary net-benefit policy is built to avoid. No identified data constraint, delayed identifiability problem or nonlocal investment effect defeats that route.

This comparison does not assume free target labels. The strongest attack reuses target work already required to verify real requests where legally available, and charges any extra distribution capture, storage, backward pass and synchronization. If access to dense teacher distributions is unavailable, token-based on-policy adaptation remains an alternative arm. The control's competence must be assessed under the actual telemetry contract, not an artificially rich simulator or a deliberately weak periodic baseline.

## Boilerplate and missing build content

The source is ESTIMATED 0.75–0.88 mechanism-specific, leaving ESTIMATED 0.12–0.25 generic framing. It is not mostly boilerplate, but it does not yet define a runnable systems experiment. Missing are target/draft models, initial alignment, pool topology, concurrency and admission actions, workload arrival law, drift support, telemetry delay, legal update objectives, synchronization protocol, output-equivalence rule, GPU-time denominator and complete reward formula. The phrase “total GPU time” needs a decision about idle reserved capacity and overlap, not just a sum of worker-reported runtimes.

A deterministic prompt trace is not a deterministic elapsed-time grader. Cold compilation, communication and host scheduling can alter both the apparent baseline and the opportunity to update. At minimum the build needs matched warmup and baseline calibration per hardware configuration. It also needs finite storage/retention for all refresh branches and a reset that prevents old draft state from crossing attempts. Otherwise the task can produce strong-looking but incomparable scores without any malicious candidate behavior.

## Duplicate check

The checked v3 `03_knowledge_transfer.md` specifies 03B, a budget-conditioned student trading reasoning and coverage. C037 instead modifies a draft while a separate fixed target serves and verifies. They share distillation economics but differ in artifact, objective and time-coupled resource competition. I find no verified duplicate in that comparison. C020, reviewed earlier in this assigned session, optimizes cache admission rather than draft training; its throughput-accounting risks are adjacent but its scientific mechanism is distinct. No other card comparisons are claimed.

## Verdict, required fixes and cheapest decisive check

CUT because the stated residual is an ordinary online control problem already encompassed by a competent combined recipe. A re-entry would need concrete admissible telemetry and a reproducible sequence where training changes later service value in a way a cost-aware adaptive controller cannot cheaply learn. Hiding drift until after an irreversible decision or banning conditional refresh would not establish a scientific reserve.

The lowest-cost decisive screen is a CPU calculation, ESTIMATED 0 H100-hours, using legal per-stage service/update profiles to compare frozen, target-only, periodic and net-benefit schedules. It should distinguish a causal controller from a clairvoyant future-trace optimum and expose cases where no update repays before the horizon. That can reject the proposed scheduling depth without training any draft. If real profiles are unavailable, no honest numeric GPU conclusion follows from an invented simulator. A later profiling and replay pilot is provisionally ESTIMATED 9 H100-hours for the compact fixed target/draft pair and transition set, charging distillation and verification; this is an estimated rejection screen rather than certification. The source's ESTIMATED 12 GPU-h is not treated as measured cost.

Any future implementation must enforce the shared pool at the supervisor, freeze target weights, isolate future prompts, cap state/config payloads and bind timed tokens to correctness checks. Negative controls must try hidden workers, forged counters, skipped verification, asynchronous timing and checkpoint swaps, alongside independently implemented successful fixtures. Require portable network-none execution, trusted dynamic libraries, per-seed timeouts, protected dev gold, fixed request denominators, private decontamination and full per-request archive records. None of this was executed in this CPU review, and none reduces the legal combined estimate.

## Verdict record

id: C037
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.78 (ESTIMATED 0.58–0.95)
combined_recipe_attack: ESTIMATED 0.78 (ESTIMATED 0.58–0.95)
best_of_4: ESTIMATED 0.86
pass_at_4: ESTIMATED 0.95
single_run_max: ESTIMATED 0.93
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: none
main_kill_reason: cost-aware online distillation and speculation control
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
