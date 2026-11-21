# D11: Learn when a streaming visual assistant should respond or wait — independent adversarial review

**Verdict: CUT.** The stated failure modes decompose into causal event recognition, confidence-based delay and a responded-event ledger. No specified visual ambiguity requires a new learning mechanism beyond that complete standard system, and making event identity unavailable until after the deadline would lower feasibility rather than establish research depth.

Source file: `/workspace/hidden_task_cards_v4/cards/D11.md`.

The report treats complete sessions as the scientific unit. All rewards, costs and extrapolation values are ESTIMATED desk scenarios, conditional on the source's unresolved anchors and observation contract. There are no measured detections, session scores or security grades. The event clock, renderer and learner are proposed components without source code in this card.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Detector plus responded-event automaton | Train a causal temporal detector; maintain separate pending, confirmed and answered states keyed by visible object/event tracks; emit once when confirmation crosses the legal response threshold. | ESTIMATED 0.70–0.94 | No; this is the complete control explicitly contemplated by the source. | Run causal detection with identity tracking, hysteresis and legal-window calibration jointly, including overlapping events. | ESTIMATED 0.70–0.94 | Repetition and premature response errors may disappear without any special wait-policy research. |
| Fixed-delay or posterior-threshold stopping | Estimate event-specific response hazard from legal prefixes; choose a calibrated delay or confidence threshold that minimizes premature and missed-window costs. | ESTIMATED 0.62–0.88 | Published windows constrain decisions but do not establish that optimal stopping is difficult. | Compare fixed delays, sequential posterior thresholds and a learned end-to-end policy under identical causal inputs. | ESTIMATED 0.62–0.88 | Wide windows can make threshold choice nearly irrelevant; narrow windows can make everyone information-limited. |
| Direct timing demonstrations | Generate legal training-session prefixes and exact valid actions from train-only event annotations; imitate wait/respond and suppress already-served identities; refine on induced errors. | ESTIMATED 0.67–0.93 | No restriction blocks causal demonstration training, and none should. | Give this teacher the same trace and fitting budget; match prefix coverage before attributing gains to restraint learning. | ESTIMATED 0.67–0.93 | A small finite event grammar may be exhaustively teachable. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read future-frame buffers, event-annotation descriptors or renderer shared memory; patch a detector backbone or clock library through writable mounts. | ESTIMATED 0.93–1.00 | The policy is denied hidden state in prose, without a concrete memory/process boundary. | Stream only revealed frames through an isolated worker, keep full-session annotations and clock authority separate, freeze assets and inspect inherited handles. | ESTIMATED 0.00 | Decoder prefetch and shared buffers can expose future pixels without exposing an explicit annotation file. |
| Interface or encoded-state smuggling | Hide event schedules in submitted weight metadata, compressed configuration or recurrence initialization; replay precomputed responses indexed by session identifier. | ESTIMATED 0.86–1.00 | A trained-weight artifact is implied, but its legal provenance and recurrent reset are undefined. | Trusted reconstruction from legal traces, bounded handoff parsing and fresh zeroed per-session memory; deny schedule/timestamp overrides. | ESTIMATED 0.00 | Legal temporal memory inferred from observed prefixes is necessary and must not be rejected as a payload. |
| Spoofed verdict / skipped execution / benign-bank fingerprint | Claim valid response timestamps without emitting responses, abort during quiet intervals or identify correct-session fixtures by matching inherited video bytes. | ESTIMATED 0.88–1.00 | Trusted time and exact event identities would help only if actual emissions are recorded independently. | Parent timestamps real outputs, reconciles every opportunity and uses independent equivalent timing-positive sessions; skipped work yields no response credit. | ESTIMATED 0.00 | A permanently silent or dead policy must not earn safety points for absence of duplicates. |
| Timing / check-decoupling / branch laundering | Buffer the whole clip before starting its clock, backdate outputs, use a causal detector for checks and an offline future-aware smoother for credited sessions, or retain a warmed hidden-state process. | ESTIMATED 0.82–1.00 | A trusted event clock addresses claims, but stream release and compute deadlines remain unspecified. | Bind frame release, inference completion and credited response in one causal event ledger; clear workers and charge all useful preprocessing. | ESTIMATED 0.00 | Offline replay can accidentally turn simulated event time into free compute or free lookahead. |
| Dev-hidden leakage / cue inference | Infer event onset from scene cuts, rendering overlays, frame counters or clean/failed clip encodings; use composition seed metadata to preselect a response schedule. | ESTIMATED 0.69–0.96 | Shared packaging and new causal compositions are intended, not demonstrated. | Cross appearance/cuts with timing truth, remove scheduling sidecars and compare blank-frame/metadata-only predictors on independent sessions. | ESTIMATED 0.13–0.36 | Natural visible precursors are legitimate evidence; nuisance cues must be tested by counterfactual interventions. |
| Adaptive aggregate oracle | Sweep response thresholds and cooldowns against a reused composition bank, difference premature/duplicate summaries and reconstruct its timing distribution. | ESTIMATED 0.61–0.89 | The protected proxy has no stated query price, precision or release policy. | Freeze aggregate information limits globally and test the best legal threshold optimizer on untouched compositions. | ESTIMATED 0.25–0.53 | A low-dimensional threshold family can generalize well from very little legal feedback. |
| Slice abandonment / denominator optimization | Respond only to isolated easy events, ignore overlaps, or create long silence so scoring averages over observed responses instead of offered opportunities. | ESTIMATED 0.47–0.83 | The card explicitly retains quiet and overlap strata, but the opportunity/cost formula is absent. | Root owns opportunity identities and quiet-interval accounting; measure always-wait, immediate-response and easy-only policies with smooth local penalties. | ESTIMATED 0.17–0.45 | Quiet-interval mass can dominate an incorrectly weighted utility even with complete session denominators. |
| Strongest lawful combined recipe | Train causal visual event/identity features with prefix demonstrations; maintain a pending/answered automaton; use sequential confidence and calibrated cooldown/window thresholds with full legal dev selection. | ESTIMATED 0.79 (ESTIMATED 0.56–0.96) | This implements the disclosed outcome and is entirely lawful. | Measure full-session native gain against it before any claim of stacked timing insights. | ESTIMATED 0.79 (ESTIMATED 0.56–0.96) | Standard temporal recognition and control may already reach the constrained ceiling. |

## Published recipe shortcut — web checked

- [OadTR: Online Action Detection with Transformers](https://arxiv.org/abs/2106.11149): the primary abstract describes recognizing current actions using historical information and predicted future context; it supplies a causal detection architecture lead, not access to actual future frames.
- [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation](https://arxiv.org/abs/1903.01945): establishes temporal refinement and smoothing against oversegmentation. Its offline receptive field must be made causal or treated as a diagnostic, never silently admitted to D11 deployment.
- [Bayesian Online Changepoint Detection](https://arxiv.org/abs/0710.3742): describes online inference of run length and changes, supporting a standard evidence-accumulation baseline for event onset and reset.

I checked primary search abstracts and associated primary publisher results during this session. No detector implementation, latency or causal receptive field was executed or audited. The proposed composite is my engineering inference from these mechanisms; no paper establishes its D11 score. Its working reward forecast is ESTIMATED 0.79, range ESTIMATED 0.56–0.96. A faithful online baseline must prevent future leakage while still retaining all historical observations allowed to the reference.

## Saturation against the hypothetical 10T researcher / 12h

The proposal's observed-frame competence premise already supplies a strong perception starting point. A researcher can label causal prefixes, calibrate uncertainty and maintain explicit response state. Keeping a response ledger does not require learning post-response restraint through trial and error. Overlapping events require concurrent identities, which are a familiar tracking problem rather than evidence that these modules form dependent research discoveries.

Waiting can be valuable when later evidence disambiguates an event, but that alone establishes a sequential decision problem, not a durable recipe gap. The author needs prefix-equivalent event pairs where different later evidence changes the correct action while enough legal time remains for a common causal policy. If the correct response is already determined by a cheap detector, standard thresholds win; if it is not determined before the window closes, all policies share an information ceiling. The current card gives no intermediate construction or reference witness.

Full-budget risk estimates are single-run maximum ESTIMATED 0.94 against the binding 0.70 line, oracle best-of-4 mean ESTIMATED 0.88 against 0.60, and pass@4 ESTIMATED 0.92 against 0.50 at reward at least the binding 0.60 threshold. Projected upper-95% is ESTIMATED 0.99 against 0.75. I expect all absolute gates to be threatened. These tail forecasts express a scenario rather than inferred statistical parameters, and no actual kill is observed.

S1 lacks a midrange executable timing reference and a stronger same-deployment causal control with demonstrated reserve. S7 is unassessed because the usable observation/latency ceiling is unknown. A nominal score gap caused by invisible events or physically missed deadlines cannot establish that reserve. Current assistants' weak long-horizon verification or tendency to stop early, as reported in the allowed weakness files, cannot be counted against a full-budget target researcher.

Rollout scores: UNMEASURED; future evaluations must replay complete independently authored sessions. Grader noise: UNMEASURED; test clock determinism separately from decoder/runtime and training variation. Observed runs: UNMEASURED; keep missed deadlines, worker faults and all threshold-search branches. pass@k observed: UNMEASURED; use independent research attempts per composition block and report deployable dev selection alongside oracle selection. Any later scaling fit must distinguish extra researcher reasoning from extra subject inference per frame.

## Revised estimate versus the source card

`F_D11(U_detector+FSM)` is the card's symbolic estimate, so there is no source numeric point for an arithmetic comparison. My ESTIMATED 0.79 assigns high risk to exactly that route after adding causal identity tracking, demonstration-trained waiting and confidence calibration. The source's conditional retention rests on evidence accumulation exceeding detection plus state; as written it does not show why.

The card's proposed pilot includes detector training, but a baseline using isolated-frame predictions alone would not test its strongest acknowledged shortcut. It needs temporal context, event-keyed state and jointly tuned delays. As in the supplied FIX calibration material, measuring individual familiar components weakly is not a substitute for a complete known-method system.

## Boilerplate and missing build content

My editorial split is ESTIMATED 35–45% generic safeguards and ESTIMATED 55–65% streaming-specific material. It is not mostly boilerplate, yet an implementer cannot infer event ontology, visual source rights, precise response matching, overlap identities, duplicate attribution, quiet-interval weight or response costs. Also absent are observation frequency, frame release semantics, whether inference blocks delivery, hardware timing rules, actor policy size, fitting recipe and frozen anchor values. The event clock and renderer in this review are roles named by the proposal, not discovered executable filenames.

The exact grader must specify how a response covering several events is matched, whether incorrect extra content invalidates a response and how recurring visually identical events receive new identities. Otherwise a response containing every possible answer, or one response spanning multiple windows, can game matching. The GDM timing lesson requires actual shape-appropriate warmup and meaningful latency effects, while structural isolation must deny future-frame queues. Portable execution, strict parsing, finite timeouts, independent positive probes, immutable submission capture and complete per-session exports all remain future requirements. No judge should decide whether a response seemed appropriately restrained.

## Duplicate check

I read catalog T10's active crop/revisit definition and the v3 file heading identifying 02B as delayed irreversible-tool credit. D11's fixed incoming stream and proactive response windows differ from both. There is therefore no exact duplicate established among those inspected neighbors; the risk is saturation by published temporal-control methods, not a proven copied contract. The duplicate review does not certify unexamined D or creative cards.

## Verdict, required fixes and cheapest decisive check

CUT this formulation. Reconsider only after providing an observation-matched ambiguity family, exact causal timing semantics and an executable reference with native advantage over a competent temporal-detector/automaton/demonstration composite. Narrower windows, longer recordings and bans on response ledgers are not acceptable fixes.

The earliest decisive experiment is CPU replay over legal detector-score traces, with explicit event identities and release times, comparing a grid of thresholds/delays plus concurrent event ledgers against the proposed wait-policy actions. It costs ESTIMATED 0 H100-hours and tests whether the distinctive response mechanism is simply bookkeeping. Ground-truth event labels may define scorer truth and diagnostic upper bounds, but must not be supplied to the deployable controller. If that audit leaves a substantive perceptual ambiguity, a later separately priced causal-detector fitting pilot would be necessary; it is not implicitly included in this CPU check. No training or replay experiment actually ran here.

## Verdict record

id: D11
source_group: D_card
verdict: CUT
strongest_attack: ESTIMATED 0.79 (ESTIMATED 0.56–0.96)
combined_recipe_attack: ESTIMATED 0.79 (ESTIMATED 0.56–0.96)
best_of_4: ESTIMATED 0.88
pass_at_4: ESTIMATED 0.92
single_run_max: ESTIMATED 0.94
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: new causal ambiguity witness; complete temporal detector and automaton floor; exact stream and matching semantics
main_kill_reason: standard event detection and response bookkeeping exhaust the mechanism
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
