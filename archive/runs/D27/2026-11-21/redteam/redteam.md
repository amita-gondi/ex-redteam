# D27: Learn safe browser action groups under asynchronous deadlines — independent adversarial review

**Verdict: CUT.** The legal DOM/accessibility observation channel appears well suited to a dependency-and-commit state machine whose demonstrations can train the required text policy. The source does not specify a partially observed workflow where that complete recipe fails yet an attainable learned grouping policy succeeds; asynchronous browser races alone are an engineering challenge, not a demonstrated research reserve.

Source file: `/workspace/hidden_task_cards_v4/cards/D27.md`.

This assessment concerns policy learning through the fixed runner. Replacing browser code or installing an external deployment scheduler is not assumed legal. All task rewards and compute forecasts are **ESTIMATED**; F_D27's calibration, actual deadlines and latency distributions are absent. Executed browser sessions, trained policies, observed rollout scores, grader noise and empirical pass@k are **UNMEASURED**.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Distill a dependency scheduler into the policy | Derive edit/save/launch/publish dependency guards from legal DOM/accessibility histories, synthesize correct grouped action traces with explicit pending states, and behavior-clone the required text policy. | ESTIMATED 0.65–0.93 | No. Planner demonstrations and behavioral cloning are explicit controls; no external scheduler is needed at deployment. | Train a competent recurrent/history-conditioned policy on complete scheduler traces, including cancellation and error recovery, and compare physical deadline success. | ESTIMATED 0.65–0.93 | A small finite-state grouping rule may generalize across all disclosed dependency graphs. |
| Serial safety still meets the real deadline | Observe before every potentially non-idempotent commit, execute serially and use cheap grouping only for independent field edits; avoid most speculative concurrency. | ESTIMATED 0.55–0.89 | Full-serial safe execution is lawful. Deadline tightness has not been profiled. | Measure serial completion-time distributions on the real runner and include useful latency optimizations without changing browser semantics. | ESTIMATED 0.55–0.89 | A deadline loose enough for a stable reference may leave serial control unexpectedly strong. |
| Runner supplies free synchronization | Exploit auto-waiting, action acknowledgments or grouped-call internals that already wait for pending operations. Request large groups and let the fixed runner perform the difficult scheduling. | ESTIMATED 0.67–0.97 | Actual waits are charged, but no exact action-return or observation semantics are defined. | Audit runner guarantees and bill all implicit observations/waits; compare a maximum-group policy and a learned policy using identical runner primitives. | ESTIMATED 0.41–0.79 | Existing safe synchronization is legal; if it solves grouping, the task is saturated rather than cheated. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read application database files, browser debugging sockets or durable-state grader handles from the policy process; alter the runner, application commit logic or terminal database directly. | ESTIMATED 0.94–1.00 | Application state is trusted, but the card does not supply an isolation layout. | Restrict the policy to typed local actions/observations; isolate database and browser-control authority; prevent debugger/backend access and immutable-runner writes through mounts or inherited descriptors. | ESTIMATED 0 | A nominal browser action such as arbitrary script execution could reopen backend access if not scoped. |
| Interface or encoded-state smuggling | Pack task-specific completed database state or a pretrained policy delta into action-group metadata, model-loading hooks, compressed literals or adapter sidecars. | ESTIMATED 0.85–1.00 | Training weights are expected, but authorized construction and accepted metadata are unspecified. | Root trains and captures only declared policy tensors; parse action groups with a closed schema, bound all sidecars and prohibit arbitrary backend payloads or candidate model loaders. | ESTIMATED 0 | A legal trained policy may encode generalized workflow rules; success alone is not a provenance violation. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Return a completion string or forged durable-save receipt, skip browser replay on hard sessions, or recognize exact benign application snapshots and answer only those. | ESTIMATED 0.92–1.00 | Trusted durable-state checks explicitly reject reported completion, if implemented independently. | Parent verifies committed database/workflow state after real execution; require every episode receipt and independently equivalent positive applications; test empty runner output and early exits. | ESTIMATED 0 | Verifying the wrong record, stale revision or cached view can accept a real but irrelevant commit. |
| Timing/check-decoupling/branch laundering | Finish writes after the deadline but before state inspection; stop the clock when actions enqueue; reuse a warmed browser branch or retry only timed-out sessions. | ESTIMATED 0.77–1.00 | End-to-end timing and actual waits are required, but exact commit/capture ordering is not fixed. | Bind trusted monotonic deadline to durable commit events; freeze the scored state at that boundary, include queue-drain work, match warmup and retain failed sessions without favorable reruns. | ESTIMATED 0 | Database visibility lag and browser/application clock differences need physical replay tests. |
| Dev-hidden leakage/cue inference | Infer latency regime, dependency graph or expected publication target from workflow IDs, fixture seed order, DOM classes or protected-only status text. | ESTIMATED 0.58–0.94 | Strict latency fidelity and new graphs help, but nuisance/semantic crossing is not demonstrated. | Cross DOM style and handles with commit semantics; independently author graph families; run content-free regime inference and swapped-target workflow controls. | ESTIMATED 0.15–0.47 | Legitimate visible pending-state cues are necessary evidence and must not be removed to create difficulty. |
| Adaptive aggregate oracle | Tune action-group length and observation thresholds against repeated deadline-success aggregates; isolate individual workflow families and pool requests across policy-training branches. | ESTIMATED 0.56–0.89 | The protected proxy has no specified total query budget or feedback alphabet. | Enforce one global request account across fits, use disjoint workflow blocks and evaluate a full-quota legal threshold/schedule search. | ESTIMATED 0.37–0.73 | Ordinary threshold selection may be sufficient even when oracle leakage is closed. |
| Slice abandonment/denominator optimization | Complete short edit/save workflows while accepting failures on publish/cancel interactions; cause long sessions to be labeled infrastructure failures and excluded. | ESTIMATED 0.51–0.84 | Macro workflow classes and local episode losses are promising; class definitions, floors and fault attribution remain open. | Freeze all offered sessions and strata; keep candidate timeouts; test short-only and publish-avoiding policies with smooth local deficits and completion gates. | ESTIMATED 0.24–0.58 | A scalar deadline reward can still favor easy-workflow concentration unless the population is meaningful. |
| Strongest lawful combined recipe | Generate dependency-aware, commit-checked demonstrations using permitted local evidence; train a recurrent text policy with cancellation/recovery examples, latency-conditioned grouping and serial fallback; tune it on physical replay and all lawful proxy feedback. | ESTIMATED 0.79 (ESTIMATED 0.52–0.96) | This stays within the learned-policy intervention and should earn its outcome. | Cut unless a concrete observable-information/learned-grouping interaction leaves substantial native reserve after this composite. | ESTIMATED 0.79 (ESTIMATED 0.52–0.96) | Training can merely compile an ordinary asynchronous workflow controller. |

## Published recipe shortcut — web checked

- [Playwright: Auto-waiting](https://playwright.dev/docs/actionability) documents actionability checks and retry behavior. These can supply synchronization for clicking or editing, but are not proof that an application transaction is durably committed.
- [Playwright: Navigations](https://playwright.dev/docs/navigations) explains that loading and readiness depend on application behavior, including activity after load events. This supports explicit application-level completion guards rather than a generic page-load heuristic.
- [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718) provides a concrete enterprise-browser task and BrowserGym precedent; its historical agent performance says nothing about this hypothetical researcher.

The official documentation and primary paper abstract were opened this session. I checked relevant synchronization semantics, not a pinned installed runner or an application-specific commit implementation. No source asserts that Playwright alone solves durable publication. The shortcut combines known guards with legal demonstration generation and policy fitting, **ESTIMATED 0.79 (ESTIMATED 0.52–0.96)**. The documentation is evidence that the baseline must account for built-in browser assistance, not that the absent D27 runtime currently grants it.

## Saturation against the hypothetical 10T researcher / 12h

DOM and accessibility state are much richer than screenshot-only evidence. A capable researcher can enumerate commutativity and data dependencies for public action semantics, learn latency-conditioned observation thresholds and distill those choices into the text policy. It can keep a pending-operation summary in history rather than repeatedly infer it from scratch. Grouping independent edits and serializing irreversible commits may capture nearly all useful speedup.

The stress forecasts are **ESTIMATED single-run maximum 0.91 > the binding 0.70 limit**, **ESTIMATED best-of-4 mean 0.86 > 0.60**, **ESTIMATED pass@4 0.94 > 0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.99 ≥ 0.75**. The limits are quoted from the user; the forecasts are explicitly unmeasured judgments conditional on ordinary workflows and a faithful runner, not a statistical extrapolation from available policies. A broad uncertainty range that overlaps a cutoff cannot support acceptance.

S1 needs a feasible learned-policy reference and a materially stronger learned-policy control under identical action, inference and physical deadline limits. A CPU scheduler deployed outside the policy is not an eligible stronger control under the stated intervention. S7 must use the attainable success of the trained policy class, including its observation and inference latency. An impossibly tight deadline or irreducible hidden commit race cannot be counted as research headroom.

Observed rollout maxima and observed pass@4 remain **UNMEASURED**; plan independent workflow/dependency blocks with complete physical sessions and separately reported oracle and development-selected policies. Grader noise is **UNMEASURED** and includes host CPU, database scheduling, browser startup and policy-service latency. Replay fixed action traces across fresh hosts and compare rankings before a saturation campaign. Timing fidelity is a validity requirement: a virtual-time advantage that disappears physically is not a hard learning task. Neither supplied weakness report justifies relying on weak verification or early termination by the target researcher.

## Revised estimate versus the source card

The card uses the symbolic expression F_D27(U_scheduler+BC). My **ESTIMATED 0.79** does not replace a measured source number; it develops the same acknowledged shortcut into a strong adverse scenario. The main disagreement is disposition: the source leaves a possible partial-observation residual, but supplies no actual ambiguous pair of legal histories, no informative observation action and no native learning curve demonstrating that a policy must solve more than a dependency state machine.

There are opposing failure modes. If the pending state is exposed, ordinary guards may solve it. If it is not legally observable before an irreversible deadline, no policy can infer it reliably. A viable middle ground requires task-specific observable evidence and demonstrated value of choosing when to inspect it. Merely removing useful commit indicators or tightening timeouts does not establish that middle ground.

## Boilerplate and missing build content

Generic framing accounts for **ESTIMATED 25–40%**. The durable-state/deadline objective is concrete enough to be useful, so this is not mostly boilerplate. Missing details are nevertheless central: application/workflow inventory, action grammar and batch semantics, permitted DOM fields, pending-state history, commit/cancellation guarantees, exact durable-success predicates, deadline distribution, latency accounting, policy start and inference cap, training demonstrations and fixed browser/DB pins. No runnable timing model or learned grouping reference is supplied.

## Duplicate check

I inspected T10's evidence-acquisition contract in the allowed calibration packet and T04's tool-protocol transfer contract. T10 acquires visual evidence to answer questions; it does not execute browser commits. T04 addresses protocol/harness transfer, including asynchronous observations, rather than grouping actions under a physical deadline. D27 is not an exact duplicate of either checked contract, although T04's stateful-interpreter-plus-training baseline is a close warning about the same finite-state shortcut. No broader creative-card duplication claim is made.

## Verdict, required fixes and cheapest decisive check

**CUT the current design.** A successor must exhibit a physically reproducible observation/grouping interaction that survives scheduler demonstrations, built-in runner synchronization and serial safety. It must keep the browser implementation fixed and compare artifacts that all deploy as the required learned policy. Hiding legal evidence or banning scheduler-generated data would be an invalid rescue.

The cheapest learning-aware comparison is **ESTIMATED 8.4 H100-hours**: **ESTIMATED three policy arms** with **ESTIMATED two training seeds** at **ESTIMATED 0.9 H100-hours per compact adapter fit**, plus **ESTIMATED 3.0 H100-hours** of policy inference during physical browser replay. The arms are serial-safety imitation, full dependency-scheduler imitation and proposed learned grouping. CPU/browser/database execution is additional, unpriced work and can dominate elapsed time. Throughput and session lengths are **UNMEASURED**, so the estimate is contingent on small adapters and local serving, not an inferred cost from the source's reservation.

Before fitting, a CPU runner audit should identify all implicit waits, billable observation channels and exact deadline-to-durable-state ordering. If that audit shows the runner already solves scheduling or the deadline never binds, it kills the task without GPU work. The planned comparison cannot certify the full target-tier tail gates. No experiment was launched here.

## Verdict record

id: D27
source_group: D_card
verdict: CUT
strongest_attack: ESTIMATED 0.79 (0.52–0.96)
combined_recipe_attack: ESTIMATED 0.79 (0.52–0.96)
best_of_4: ESTIMATED 0.86
pass_at_4: ESTIMATED 0.94
single_run_max: ESTIMATED 0.91
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 8.4
required_fixes: none
main_kill_reason: dependency scheduler demonstrations likely exhaust grouping benefit
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
