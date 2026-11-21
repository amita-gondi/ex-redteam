# D28: Teach screenshot-only actions with training-only transition feedback — independent adversarial review

**Verdict: FIX.** Privileged training feedback could improve visual control without a runtime DOM channel, but the card conflates correct delayed-event bookkeeping with a harder feedback-learning claim. A bounded redesign can retain the latter by starting from correct version binding, restricting feedback to training updates and demonstrating student-occupancy-dependent value beyond complete privileged imitation and terminal-credit baselines.

Source file: `/workspace/hidden_task_cards_v4/cards/D28.md`.

No visual policy, feedback callback or application was executed. All proposed rewards are **ESTIMATED** scenarios on an eventual frozen reward scale; missing F_D28 anchors preclude calibrated predictions. Actual learning gains, observed rollout scores, grader noise and observed pass@k are **UNMEASURED**. The analysis distinguishes what a training teacher may legally see from what the deployed screenshot actor may receive.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Replace token feedback with privileged recovery imitation | Use legal DOM/transition evidence to generate verified training actions after induced visual-policy mistakes; behavior-clone those recoveries and fine-tune with exact terminal success. | ESTIMATED 0.54–0.85 | No. Teacher distillation is a lawful complete comparator and can bypass the proposed token-credit mechanism. | Match successful-state exposure, teacher generation and update work between full recovery imitation and feedback learning. | ESTIMATED 0.54–0.85 | The teacher may already supply every useful action distinction. |
| Correct provenance, then use ordinary trajectory returns | Join each delayed transition to the original episode/action/version; compute conventional terminal returns or off-policy-corrected advantages instead of learning special token feedback. | ESTIMATED 0.51–0.82 | Trusted version binding is specified, but the inherited failure could make this hygiene supply most apparent headroom. | Ship correct joins as the common starter; compare synchronous, correctly bound asynchronous and stale diagnostic arms with equal work. | ESTIMATED 0.40–0.73 | Actor staleness and event misattribution are different problems; solving one does not prove a novel solution to the other. |
| Teacher gives actions impossible to identify visually | Exploit an apparent reference trained on privileged pending-state distinctions that no screenshot history distinguishes; achieve high teacher accuracy while claiming transferable feedback value. | ESTIMATED 0.49–0.89 | The card requires history-based identifiability but supplies no observational-collision audit. | Pair identical screenshot/action histories with differing DOM states and check for a common successful continuation or a legal informative observation before action. Reject impossible instances. | ESTIMATED 0 | Perfect privileged labels can still be inconsistent targets for a partially observed actor. |
| Filesystem/mount/proc/IPC/frozen-asset access | From the deployed actor, open DOM snapshots, browser debug sockets, training transition logs or application database descriptors left in mounts/IPC; alter fixed screenshot capture or terminal truth. | ESTIMATED 0.94–1.00 | Screenshot-only deployment and absent runtime layers are explicit intentions, not a verified namespace. | Rebuild evaluation in a separate runtime with screenshot/action-only IPC; exclude DOM/log assets, debugger handles and writable capture code; probe inherited FDs and frozen assets. | ESTIMATED 0 | Browser accessibility helpers and stale shared-memory buffers may reveal privileged state indirectly. |
| Interface or encoded-state smuggling | Encode a runtime planner in the token-feedback callback, stash DOM summaries in recurrent state during evaluation, or install arbitrary learner deltas through numeric feedback fields and compressed rule literals. | ESTIMATED 0.86–1.00 | Runtime planners are expressly invalid; feedback grammar, call phases and tensor authority remain unspecified. | Execute feedback only in trusted training; admit bounded action/version-linked targets or losses, no inference callback or parameter-address writes; reconstruct learner state from metered legal updates. | ESTIMATED 0 | Powerful lawful reward/advantage functions must remain expressible; simplistic source scans cannot establish this boundary. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Substitute token accuracy for durable success, print application-complete markers, skip late episodes or recognize fixed positive screenshot fixtures by bytes. | ESTIMATED 0.90–1.00 | Token metrics have no outer weight, which helps; executed-state receipts and equivalent-positive tests are not built. | Parent reads durable application outcomes after actual policy execution; require all scheduled episode/version receipts and independently rendered positive workflows; test worker deletion and forged stdout. | ESTIMATED 0 | A cached screenshot or UI toast can look successful before the durable write occurs. |
| Timing/check-decoupling/branch laundering | Bind feedback to a cheap older policy while training a newer branch, reuse uncharged teacher trajectories, or let a DOM-serving training process survive into screenshot evaluation. | ESTIMATED 0.76–1.00 | Version receipts and teacher-cost accounting are proposed but not fully defined. | Bind action, behavior probabilities, transition, update and final learner to one immutable lineage; charge rejected trajectories; kill training services and cold-load the committed actor in evaluation. | ESTIMATED 0 | Delayed valid receipts arriving after a branch switch need precise ownership and charging rules. |
| Dev-hidden leakage/cue inference | Memorize layout families, task IDs, delay patterns or renderer artifacts that identify the next action independently of visual workflow semantics. | ESTIMATED 0.57–0.92 | New layouts and compositions are useful, but independent construction and nuisance crossing remain untested. | Cross layout/rendering with transition graphs; hold out workflow compositions and content ancestry; test screenshot-style-only and task-text-only policies. | ESTIMATED 0.15–0.46 | Correct OCR and layout parsing are legitimate transferable skills, even if they make the task easier. |
| Adaptive aggregate oracle | Tune feedback rules that target one delayed-action family at a time, difference protected terminal-success scores and coordinate selector queries across training branches. | ESTIMATED 0.54–0.88 | Protected proxy matching is specified without a global precision/query contract. | Add a cross-branch root ledger, fresh proxy workflow blocks and fixed response cadence; include the strongest permitted feedback-rule selector in the recipe floor. | ESTIMATED 0.34–0.69 | Lawful query-driven search can find a compact general credit rule without the proposed diagnosis. |
| Slice abandonment/denominator optimization | Train strongly on ordinary immediate workflows, ignore asynchronous or late commits, and exploit any denominator based on received feedback rather than offered episodes. | ESTIMATED 0.47–0.82 | Failed/late episodes remain included in prose, but explicit asynchronous strata and release-time denominators are missing. | Preindex all offered episodes and update receipts; freeze ordinary/asynchronous coverage requirements; evaluate immediate-only and wait-heavy specialist policies. | ESTIMATED 0.22–0.55 | Waiting can be a valid safe strategy unless real observation and deadline costs make it uncompetitive. |
| Strongest lawful combined recipe | Combine visual grounding pretraining, history-conditioned privileged recovery imitation, induced-state aggregation, correct version/behavior-policy accounting and tuned terminal-credit RL, selecting feedback variants using all legal proxy calls. | ESTIMATED 0.63 (ESTIMATED 0.38–0.87) | The composite respects training-only privilege and screenshot-only deployment. | Retain only if a precisely defined feedback intervention adds native success beyond this complete baseline and leaves an attainable stronger control. | ESTIMATED 0.63 (ESTIMATED 0.38–0.87) | Standard visual imitation plus off-policy engineering could absorb the entire reference benefit. |

## Published recipe shortcut — web checked

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935) establishes screenshot-based GUI action grounding and automatically curated grounding supervision. It motivates a strong visual-training floor.
- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://arxiv.org/abs/2411.17465) provides visual/action-history modeling and curated GUI instruction data as another complete baseline family. Its grounding performance is not a durable-workflow score for D28.
- [IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures](https://arxiv.org/abs/1802.01561) supplies off-policy correction for actor/learner lag. It does not repair a transition joined to the wrong action, so both provenance correctness and policy-lag treatment must be implemented separately.

This session searched the primary records, opened the GUI abstract pages and read primary IMPALA search/proceedings excerpts. Verification establishes method availability and scope, not pinned-code compatibility, faithful reproductions or D28 results. No pretrained asset was downloaded. The lawful composite's conditional estimate is **ESTIMATED 0.63 (ESTIMATED 0.38–0.87)**; the reported GUI literature does not justify deriving that number from published benchmark scores.

## Saturation against the hypothetical 10T researcher / 12h

A stronger researcher can repair timestamp/version joins immediately, preserve exact behavior-policy receipts, synthesize successful training recoveries and compare sparse terminal learning with dense token targets. Those repairs should be available to every baseline. The plausible remaining problem is selecting feedback whose benefit persists as the visual policy changes the states it visits. That effect could be genuine, but ordinary induced-state imitation follows changing occupancy too. It must be tested as a complete alternative, not weakened to clean demonstrations only.

The working forecasts are **ESTIMATED single-run maximum 0.76 > 0.70**, **ESTIMATED oracle best-of-4 mean 0.70 > 0.60**, **ESTIMATED pass@4 0.77 > 0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.93 ≥ 0.75**, against the fixed user saturation lines. These are not measured order statistics, estimated confidence limits from data or an available-model scaling fit. The broad combined range means uncertainty overlaps the dangerous region even if the point forecast is optimistic about the recipe. Correct sandboxing cannot push these lawful outcomes down.

S1 is open: the card has no independent same-observation stronger controller, no learner learning curve and no native reserve after corrected bookkeeping. Extra DOM at deployment cannot establish attainable screenshot-only headroom. S7 requires a constrained learner ceiling that includes legal screenshot history, inference budget and feedback-training work. Observationally identical histories that require opposite irreversible actions lower that ceiling; they do not create algorithmic reserve.

Empirical pass@4, full-budget rollout scores and projection fits are **UNMEASURED**. Plan independent workflow-composition blocks and complete independent researcher attempts, with legal-development selection separated from hidden retrospective selection and all teacher/rollout work charged. Grader noise is **UNMEASURED**; quantify both training randomness and application timing using fixed-rule rebuilds and repeated durable-state evaluation. The supplied weakness reports motivate checking these failures, but current agents' weak verification is not evidence that a target researcher cannot implement ordinary visual imitation and sound asynchronous learning.

## Revised estimate versus the source card

The card's strongest attack is the symbolic F_D28(U_privileged_BC+RL). My **ESTIMATED 0.63** gives that concern a conditional planning magnitude and adds ordinary actor-lag correction and induced-state recovery supervision. It is not comparable to a nonexistent measured source point. The source acknowledges correct version handling as a potential complete fix; therefore the version defect should be repaired before claiming research depth.

I retain FIX rather than CUT because the editable feedback mechanism and strict screenshot actor can express a bounded, experimentally falsifiable learning question. That retention is narrow: if complete privileged imitation reaches the reference, the correct action is to cut the distribution, not forbid demonstrations. Likewise, simply increasing telemetry delay cannot turn bookkeeping into a stacked scientific dependency.

## Boilerplate and missing build content

The generic proportion is **ESTIMATED 25–40%**. This is not mostly boilerplate: the training/deployment information split, version-linked transitions and durable application objective identify a useful intervention. Missing are the token-feedback grammar, permitted privileged fields, action/token boundary mapping, behavior-probability capture, exact stale-event semantics, learner architecture and initializer, application/renderer pins, delayed-feedback distribution and reward slice definitions. No executable teacher, feedback reference or independent transition joiner is provided. Without that contract, a callback could be either a legitimate loss function or an unauthorized planner.

## Duplicate check

The inspected T12 opening problem learns vector programs from terminal raster error; it shares delayed credit terminology but lacks GUI application transitions and privileged DOM training evidence. The checked D27 source trains grouping under browser deadlines using DOM/accessibility observations; D28 deploys screenshots and changes training feedback. These are distinct artifacts and information contracts, so duplicate_of is none among checked neighbors. A complete creative-card and v3 inventory check was not performed; no claim of universal uniqueness follows from this local comparison.

## Verdict, required fixes and cheapest decisive check

**FIX**, limited to the following required work:

1. Make correct action/episode/version attribution and behavior-policy accounting common starter infrastructure; remove gains from misjoined outcomes from the research claim.
2. Define a training-only feedback ABI with trusted update ownership, and deploy the rebuilt actor in an independently clean screenshot/action-only runtime.
3. Admit only history-identifiable workflow obligations, with counterfactual screenshot-history collision tests and a legal informative continuation when needed.
4. Establish feedback usefulness beyond complete privileged recovery imitation and terminal-credit learning at matched successful-state exposure, including a changed-occupancy interaction on fresh workflows.
5. Freeze durable-success denominators, coverage requirements, proxy-query controls and the same-contract attainable ceiling before empirical certification.

The cheapest informative learner screen is **ESTIMATED 18.6 H100-hours**. Budget **ESTIMATED four training arms** across **ESTIMATED three seeds**, **ESTIMATED 1.2 H100-hours per compact visual-adapter continuation**, plus **ESTIMATED 4.2 H100-hours** for screenshot-policy inference and paired application tests. Compare complete privileged imitation, correctly bound terminal-credit RL, proposed token feedback and a stale-binding diagnostic. A CPU history-collision/ABI audit should eliminate impossible or leaky instances first. Actual model throughput and browser evaluation rates are **UNMEASURED**, so those assumptions must be profiled before any separately authorized experiment.

A surviving pilot would still need the binding native-margin, decomposition, full-budget tail and projection studies. Round 2's independent all-positive execution, bounded state channels, per-seed deadlines, root-owned immutable collection and retained failures remain future gates; none was certified by this desk review.

## Verdict record

id: D28
source_group: D_card
verdict: FIX
strongest_attack: ESTIMATED 0.63 (0.38–0.87)
combined_recipe_attack: ESTIMATED 0.63 (0.38–0.87)
best_of_4: ESTIMATED 0.70
pass_at_4: ESTIMATED 0.77
single_run_max: ESTIMATED 0.76
upper95_projected: ESTIMATED 0.93
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 18.6
required_fixes: corrected starter provenance; training-only feedback ABI; history identifiability; complete imitation floor; outcome and ceiling anchors
main_kill_reason: privileged recovery imitation may subsume feedback learning
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
