# D22: Train the teacher on states induced by student mistakes — independent adversarial review

**Verdict: CUT.** The central operation is induced-state aggregation followed by supervised teacher adaptation and distillation, which is already the natural complete imitation-learning recipe. A separately trainable teacher makes the contract distinct, but the card provides no recoverable-state construction that defeats competent aggregation, checked continuation search or direct student training while preserving an attainable reference.

Source file: `/workspace/hidden_task_cards_v4/cards/D22.md`.

This report evaluates the proposed mechanism rather than its designer verdict. Numerical forecasts are **ESTIMATED** conditional rewards, not calibrated consequences of F_D22, whose endpoints remain unknown. Actual teacher fits, rebuilt students, rollout rewards, grader noise and observed pass@k are **UNMEASURED**. No adapter was trained, model queried or state trajectory executed during this desk review.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Aggregate recovery demonstrations instead of discovering a new teacher mechanism | Generate legal student-error prefixes, search continuations using allowed terminal feedback, retain verified recoveries and fine-tune the teacher adapter on the aggregated states before fixed distillation. | ESTIMATED 0.65–0.91 | No. This is the card's own necessary DAgger/SFT control, with no specified surviving obstacle. | Implement broad state aggregation, recovery search and balanced teacher SFT as one tuned baseline; compare transferred student outcomes. | ESTIMATED 0.65–0.91 | A baseline named but not executed can conceal near-total recipe saturation. |
| Use the successful search traces to teach the student directly | Feed the same legal recoveries to a resource-matched direct-student control, spending teacher-fitting savings on additional useful student updates or checked traces. | ESTIMATED 0.60–0.89 | The card expressly says this control cannot be prohibited; the main fixed distillation ABI does not explain how it is compared. | Specify whether direct training is a valid submission route or a matched external necessity test; include complete costs and legal data access in either interpretation. | ESTIMATED 0.60–0.89 | Teacher adaptation may add an expensive intermediate approximation without improving the deployed learner. |
| Collapse recovery difficulty through prefix selection | Prefer recoverable shallow mistakes, resets or neutral mistakes with easy verified completions; train a teacher that excels on those and increases clean-task success without learning difficult recovery interactions. | ESTIMATED 0.50–0.83 | Root generates prefixes, but their distribution, recoverability strata and reset legality are undefined. | Freeze exogenous prefix cohorts and recovery opportunities; test shallow-only training and restart-first continuations against difficult but solvable prefixes. | ESTIMATED 0.29–0.59 | If the student can legally avoid those mistakes, prevention may be the right solution rather than a cheating route. |
| Filesystem/mount/proc/IPC/frozen-asset access | Inspect teacher-adaptation descriptors, trainer sockets and mounted distillation caches for hidden prefixes or answers; write the fixed student initialization or distillation implementation. | ESTIMATED 0.92–1.00 | Root execution and hidden-prefix exclusion are declarations, not delivered isolation. | Isolate teacher training from private prefix generation and student truth; make student start/distiller immutable; deny inherited handles and verify safe frozen collection. | ESTIMATED 0 | Reused teacher/student accelerator buffers and service RPCs remain potential confused deputies. |
| Interface or encoded-state smuggling | Store a ready-trained student or protected recovery labels in adapter metadata, auxiliary tensors, configuration integers or compressed training source; load them during the supposedly fixed distillation stage. | ESTIMATED 0.87–1.00 | Model weights are an intended artifact, so generic source-size checks alone cannot establish valid training provenance. | Root owns adapter fitting and permits only shape-checked teacher tensors produced by metered updates; reconstruct a fresh student with no candidate loader, metadata hook or tensor-copy path. | ESTIMATED 0 | Legitimately learned teacher weights necessarily encode task information; provenance, not a blanket ban on encoded knowledge, defines the boundary. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Return teacher-accuracy logs as student success, forge a distillation-complete marker, or identify the public rebuild fixtures and skip genuine student training elsewhere. | ESTIMATED 0.90–1.00 | Teacher accuracy is diagnostic by design; actual worker-result authentication is not specified. | Evaluate a root-rebuilt teacher-free student on independent terminal tasks; reconcile every required fit and episode; use independently implemented positive rebuilds and abort tests. | ESTIMATED 0 | Correct logs cannot substitute for a learner checkpoint produced by the credited process. |
| Timing/check-decoupling/branch laundering | Fit several teachers, use their best recoveries to improve one student, then report only a selected adapter's cost; leave teacher-serving state alive during the teacher-free evaluation. | ESTIMATED 0.76–1.00 | Charging both stages and excluding the endpoint is intended, but lineage and process teardown are unbuilt. | Bind generation, rejected search, adapter state and student rebuild to a parent ledger; terminate teacher processes, clear IPC and evaluate in a separate teacher-free runtime. | ESTIMATED 0 | Cached token logits or hidden shared state can preserve assistance without an obvious endpoint. |
| Dev-hidden leakage/cue inference | Recognize error depth or recovery action from prefix-generation style, task handles or fixed perturbation syntax; memorize a small correction grammar rather than improve conditional reasoning. | ESTIMATED 0.58–0.94 | Private prefix mechanisms and matched competence help only if their semantics and packaging are independently varied. | Cross mistake syntax with outcome; hold out recoverable interaction families rather than prompt seeds; test a prefix-metadata-only correction generator. | ESTIMATED 0.16–0.49 | A universal correction rule inferred from visible state is legal and can still saturate the task. |
| Adaptive aggregate oracle | Refit teacher adapters targeting individual mistake families; difference development student-success scores to infer which hidden recovery patterns matter most. | ESTIMATED 0.55–0.88 | A protected proxy without global query accounting does not constrain adaptive search. | Fix cross-stage/global query budgets and output precision; separate tuning and final prefix families; run the full lawful adaptive teacher selector as a baseline. | ESTIMATED 0.35–0.72 | Legal selection can improve transfer substantially even after excess-query channels close. |
| Slice abandonment/denominator optimization | Train for common clean-terminal success while neglecting induced recovery states; exploit any conditioning on completed prefixes or successfully distilled students. | ESTIMATED 0.48–0.81 | U uses terminal success across families, but no exact weights, clean/recovery floors or failed-rebuild denominator are given. | Precommit prefix, student-seed and family indices; retain failed fits and unsuccessful episodes; compare clean-only and recovery-only specialists under smooth coverage requirements. | ESTIMATED 0.21–0.55 | A rare recovery family can disappear statistically despite being present in a macro-average. |
| Strongest lawful combined recipe | Alternate induced-state collection and checked recovery search, train the teacher with aggregated SFT and cost-sensitive recovery targets, distill verified continuations into fresh students, and select against stronger-fixed-teacher/direct-student alternatives using legal feedback. | ESTIMATED 0.76 (ESTIMATED 0.49–0.94) | No legitimate defense excludes this recipe; its advantage must be measured rather than legislated away. | Cut the current task unless a concrete teacher-update/occupancy/transfer dependency survives the full matched controls. | ESTIMATED 0.76 (ESTIMATED 0.49–0.94) | The proposed reference may be standard iterative imitation learning with another trainable model inserted. |

## Published recipe shortcut — web checked

- [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686) establishes DAgger's use of learner-induced states for interactive imitation. Its expert-label assumption does not establish that this deficient teacher can supply correct recoveries.
- [Deeply AggreVaTeD: Differentiable Imitation Learning for Sequential Prediction](https://arxiv.org/abs/1703.01030) supplies a cost-to-go-aware imitation-learning route, relevant when mistakes differ in their downstream recoverability. Applicable expert values still need legal estimation.
- [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://arxiv.org/abs/2305.02301) provides rationale-based supervision for smaller learners; it supports testing transfer of useful intermediate traces, not assuming teacher improvement equals student benefit.

Search this session found the primary paper records and author/proceedings excerpts. Verification was at abstract and method-description level; no implementation was run or theorem assumptions validated for D22. Checked continuation search is my proposed way to obtain lawful recovery targets, not an empirical claim from those papers. The assembled attack is **ESTIMATED 0.76 (ESTIMATED 0.49–0.94)** after giving every stage its actual budget cost.

## Saturation against the hypothetical 10T researcher / 12h

Changing the teacher's weights can matter when query-time search is expensive and adaptation amortizes across many related failures. The card, however, fixes the student distiller and provides no failure family, query economics or transfer bottleneck from which that amortization advantage can be derived. A researcher can collect broad induced states, repair them with verified search and run ordinary supervised teacher adaptation without following any special causal narrative. If teacher learning changes which mistakes the student makes, iterative aggregation is already designed to follow changing occupancy.

I forecast **ESTIMATED single-run maximum 0.88 > the user's 0.70 line**, **ESTIMATED oracle best-of-4 mean 0.83 > 0.60**, **ESTIMATED pass@4 0.92 > 0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.97 ≥ 0.75**. All quoted comparison cutoffs are binding user requirements; the forecasts are desk judgments, not fitted order statistics or confidence intervals. Their purpose is to reject reassurance from a single moderate recipe run; they do not pretend the unavailable target researcher was tested.

S1 lacks evidence that an adapted teacher can produce a midrange student reference with substantial additional same-contract attainable reserve. A teacher that improves but cannot transfer fails the outcome before saturation matters. S7 requires a measured lower bound from a deployable teacher-free student under the identical rebuild budget. A stronger teacher with unlimited search is only a diagnostic when its deployed cost exceeds the contract. Neither ceiling-relative gate can currently pass.

Observed research outcomes and observed pass@4 are **UNMEASURED**, with planned independent prefix-mechanism blocks and independent complete teacher/student training attempts. Grader noise is **UNMEASURED**; paired student rebuilds and replayed terminal evaluations must separate teacher benefit from student initialization and sampling luck. Full-budget sweeps must charge discarded teachers, all recovery searches and student selection. The weakness reports' current-model passivity cannot support the claim that the target researcher will fail to repeat that loop competently.

## Revised estimate versus the source card

The designer's strongest-attack expression, F_D22(U_DAgger_teacher), already points toward the correct threat. My **ESTIMATED 0.76** is an adverse planning scenario for that route and a reason to cut the current specification rather than retain it on an unspecified residual. It is not a numerical disagreement with an observed or numeric source forecast.

The source claims teacher queries and student losses cannot repair an immutable deficient teacher. That is true about changing its weights, but insufficient for the scored outcome: verified search can generate usable continuations despite a deficient proposal model, and those continuations can train the student directly. Necessity must be judged through terminal student performance per total cost. A distinct editable tensor is not itself an unsolved mechanism.

## Boilerplate and missing build content

Generic content is **ESTIMATED 25–40%** of the short source. It is not mostly boilerplate: separating teacher competence from student distillation is specific and useful. Missing build-critical details include the teacher/student architectures and starts, induced-prefix sampling law, irreversible versus recoverable error definitions, available correction outcomes, search/checker access, teacher adapter architecture, fixed distillation loss/exposure, stronger-teacher eligibility and exact clean/recovery weighting. Without those, the proposed teacher-update dependency cannot be reproduced or falsified fairly.

## Duplicate check

The checked catalog T07 holds teacher weights fixed while optimizing teacher access and the autonomous-learning handoff. D22 modifies teacher competence before transferring to a separate student. The checked T17 opening contract repairs one exploited policy and tests its later adaptation, rather than teaching another model from student-induced states. Neither is an exact duplicate. I did not inspect every D or creative card, so the duplicate record means no match among inspected contracts, not an exhaustive search certificate.

## Verdict, required fixes and cheapest decisive check

**CUT.** A later version needs a concrete recoverable-prefix distribution and evidence that teacher adaptation has a transferable efficiency advantage after complete induced-state SFT, checked search, stronger fixed teachers and direct-student training. Prohibiting one of those legal alternatives would preserve a narrative rather than a research task.

The cheapest meaningful transfer screen is **ESTIMATED 14.7 H100-hours** under a compact adapter/learner setup: **ESTIMATED three comparison arms** across **ESTIMATED three independent rebuild seeds**, each costing **ESTIMATED 1.3 H100-hours** for its complete teacher/search/student pipeline, plus **ESTIMATED 3.0 H100-hours** of common state collection and terminal evaluation. The arms are complete aggregate-and-distill, direct-student checked supervision and the proposed teacher treatment; a stronger-fixed-teacher arm is additionally required if these do not decide the issue. Actual throughput is **UNMEASURED**, and larger teacher assets could make this estimate infeasible. A CPU ABI and recoverability audit must precede any future authorized profiling.

This is a kill screen, not statistical certification. The full Round 2 portable lifecycle, frozen assets, bounded artifact parser, independent positive execution, protected gold and live exploit/retest gates remain necessary for any successor. This session spent no GPU time.

## Verdict record

id: D22
source_group: D_card
verdict: CUT
strongest_attack: ESTIMATED 0.76 (0.49–0.94)
combined_recipe_attack: ESTIMATED 0.76 (0.49–0.94)
best_of_4: ESTIMATED 0.83
pass_at_4: ESTIMATED 0.92
single_run_max: ESTIMATED 0.88
upper95_projected: ESTIMATED 0.97
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 14.7
required_fixes: none
main_kill_reason: complete induced-state imitation likely supplies reference
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
