# C012: Recover learnability after curriculum-induced gradient starvation — independent adversarial review

**Verdict: CUT.** The proposed obstacle is already the target of plasticity-restoration methods, while the proposed strongest attack omits representation recycling and selective reinitialization. Nothing specified separates this environment from a competent joint search over known recovery techniques, balanced temporal training and an affordable restart.

Source file: `/workspace/task_ideation_v4_creative/cards/C012.md`.

All payout and resource figures in this report are ESTIMATED planning scenarios. The inherited learner, dataset and scoring program were not executed. Since the card contains no executable artifact paths, references to the starvation checkpoint, fixed clip pool, temporal probes and scene evaluator identify described assets only. A security weakness below is a conditional implementation risk, not a discovered exploit in shipped code.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Recycle the starved temporal representation | Measure activation utility on legal long clips; reinitialize inactive temporal units and their moments, preserve the spatial backbone, then resume balanced training. | ESTIMATED 0.71–0.92 | No: changing trainable representations is expressly the task. | Compare competent neuron recycling, partial temporal reset and continual-backprop-style renewal to the reference. | ESTIMATED 0.71–0.92 | The intended representation intervention may simply reproduce this recipe. |
| Recover from an earlier state or fresh temporal head | Keep useful spatial features, replace the temporal head, or restart from a legal ancestor; allocate the fixed exposure budget to long-delay learning first. | ESTIMATED 0.65–0.90 | No initial-state or reset law is specified. | Declare legal initialization choices; run exposure-matched head reset and full/partial restart without deliberately poor tuning. | ESTIMATED 0.61–0.88 | A restrictive checkpoint rule cannot be added after a lawful restart wins. |
| Teach time directly from existing clips | Generate frame-order, offset and masked-future targets from the fixed pool; rebalance delay groups and jointly train auxiliary temporal objectives. | ESTIMATED 0.63–0.86 | The no-new-clips rule permits new targets and subsequences. | Account actual decoded frame/clip exposures; evaluate generic temporal supervision plus recovery methods jointly. | ESTIMATED 0.60–0.85 | Clip count alone says little about usable temporal supervision. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read private scene scripts or answer buffers through evaluator mounts/descriptors; mutate the shared starvation checkpoint to a better ancestor. | ESTIMATED 0.94–1.00 | Only private answers in probes are explicitly prohibited. | Evaluator-only scene truth, immutable checkpoint copies and independent process/IPC domains; test descriptor and library writes. | ESTIMATED 0.00 | Scene-rendering helpers can unintentionally expose script state. |
| Interface or encoded-state smuggling | Embed pretrained temporal tensors or scene answer maps inside the training recipe, numeric schedules or auxiliary-target callbacks. | ESTIMATED 0.88–1.00 | No submission language, aggregate cap or provenance boundary exists. | Trusted data-derived targets and tensor mutations; cap all source/config channels, including compressed and procedural payloads. | ESTIMATED 0.00 | An ordinary lawful reset must remain distinguishable from imported trained state. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Print temporal-probe success without training, return cached evaluation results, or recognize public successful scenes by script hashes. | ESTIMATED 1.00 | A deterministic grader can still trust an untrusted result channel. | Parent independently renders and grades the frozen learner; require executed clip-update receipts and behaviorally independent positive fixtures. | ESTIMATED 0.00 | If the parent imports candidate helpers, forged probe output can regain authority. |
| Timing/check-decoupling/branch laundering | Count clips for a cheap recovery branch but submit weights from a richer branch; leave auxiliary feature training alive after the meter stops. | ESTIMATED 0.86–1.00 | Exposure counting is promised without a state-bound execution ledger. | Bind all parameter ancestry and replay decoding to the committed artifact; terminate descendants and charge unsuccessful search. | ESTIMATED 0.00 | Shared backbone feature caches may conceal uncounted clip passes. |
| Dev-hidden leakage/cue inference | Predict event order from scene-generation ordering, object texture or answer phrasing; identify changed delay mechanisms from metadata. | ESTIMATED 0.74–0.98 | Matching temporal statistics does not balance semantic or rendering shortcuts. | Counterfactual scenes with identical nuisances and reversed causal/order truth; independent script families and no-video control. | ESTIMATED 0.20–0.48 | A small script grammar may be easy to infer from pixels legitimately. |
| Adaptive aggregate oracle | Sweep reset layers and temporal-loss mixtures against repeatedly queried event-order scores; isolate hidden delay strata by paired changes. | ESTIMATED 0.70–0.91 | No query accounting is present. | Protected representative development service with global quotas and untouched final scripts; measure full lawful tuning. | ESTIMATED 0.52–0.79 | Choosing reset extent is a low-dimensional search likely to transfer. |
| Slice abandonment/denominator optimization | Recover common short order questions, ignore delayed causes, and exploit short accuracy being merely a separate diagnostic. | ESTIMATED 0.62–0.89 | Separate tracking is not a scored non-regression requirement. | Fixed scene obligations, explicit short/long/cause utility and calibrated local deficits; retain all skipped outputs. | ESTIMATED 0.30–0.61 | An easy order slice can dominate even a balanced-looking scalar. |
| Strongest lawful combined recipe | Search balanced long-delay exposure, direct temporal auxiliary targets, selective temporal resets, moment renewal, shrink-and-perturb and neuron recycling; select among compatible recovery/restart arms. | ESTIMATED 0.76 (ESTIMATED 0.56–0.94) | No; this is legal representation and training research using the fixed pool. | Run this combined plasticity floor before building an elaborate causal reference. | ESTIMATED 0.76 (ESTIMATED 0.56–0.94) | Closing answer leakage cannot remove the ordinary recovery route. |

## Published recipe shortcut — web checked

- [The Dormant Neuron Phenomenon in Deep Reinforcement Learning](https://arxiv.org/abs/2302.12902) describes ReDo and restored network expressivity through neuron recycling. It establishes a reset-based baseline family; video compatibility is not demonstrated by that abstract.
- [Loss of plasticity in deep continual learning](https://www.nature.com/articles/s41586-024-07711-7) studies the persistence problem itself and discusses continual backpropagation as a remedy. The proposed task cannot infer novelty from uniform replay failing.
- [On Warm-Starting Neural Network Training](https://arxiv.org/abs/1910.08475) supplies shrink-and-perturb as a warm-start intervention, another natural search arm at the inherited checkpoint.

Primary search results returned these titles and mechanism descriptions in this session; verification is at abstract/search-summary depth. I did not reproduce the methods or verify a video-model port. The lawful attack uses the strongest compatible arm, with shared balanced sampling and temporal supervision, rather than assuming every reset rule helps simultaneously. Its conditional score is ESTIMATED 0.76, range ESTIMATED 0.56–0.94. No paper's benchmark score has been carried into that number.

## Saturation against the hypothetical 10T researcher / 12h

The supplied checkpoint localizes the intervention: inspect which temporal layers have little useful activity, reset candidate subsets, and measure fresh delayed-relation acquisition. A capable researcher can make that diagnostic and implement multiple published recovery methods quickly. The card does not supply an interaction that defeats them. It instead asks for precisely the distinction these controls address: replay exposure versus restored plasticity. Demonstrating that representation intervention beats uniform replay would therefore validate the phenomenon while leaving the research task saturated.

Expected tail stress values are single-run maximum ESTIMATED 0.91 and oracle best-of-4 mean ESTIMATED 0.84. Both exceed the source bar's respective >0.70 and >0.60 cutoffs. Success-at-threshold planning gives pass@4 ESTIMATED 0.93, above the binding >0.50 line at R>=0.60. The projected upper-95% endpoint under stronger research or expanded compute is ESTIMATED 0.98, also beyond the binding >=0.75 line. This endpoint is a subjective saturation scenario; there are no curve fits or empirical confidence intervals behind it.

S1 lacks an actual same-budget stronger control, native reserve or midrange reference. S7 cannot be calculated without a demonstrated attainable lower ceiling bound. If recovered performance is already near the best learnable performance on the fixed clips, a normalized ceiling-relative statistic would strengthen the cut case. An unattainably difficult new relation does not supply usable headroom. Delay range matching helps the proxy, but changed hidden mechanisms must still be represented by predictive legal training evidence.

Observed rollout rewards: UNMEASURED; planned collection is independently restarted recovery searches over fresh script blocks. Grader noise: UNMEASURED; planned test is repeated end-to-end grading of fixed artifacts, including renderer and training variation. Observed run count and observed pass@k: UNMEASURED; future tail studies must preserve failures and distinguish dev-selected recovery from retrospective oracle selection. A larger video learner would test scale transfer, not establish resistance against a larger researcher. Weak verification or premature stopping in current-model reports is irrelevant to this attack.

## Revised estimate versus the source card

The designer's source ESTIMATED attack is 0.46 for replay, delay balancing and auxiliary temporal prediction. My ESTIMATED 0.76 composite adds the most direct answer to vanished features: renew the affected representation and its optimizer state, keeping useful features where possible. The card offers no evidence that those legal actions are expensive, inaccessible or harmful enough to prevent success. Its exposure-matched pilot is sensible, but it must include these controls; “feature recovery” cannot be treated as uniquely authored insight when a published mechanism already supplies it.

## Boilerplate and missing build content

I estimate generic material at ESTIMATED 0.15–0.30 of the card and specific material at ESTIMATED 0.70–0.85. It is not mostly boilerplate, but the specific text describes a hypothesis rather than a build. Absent are the learner architecture, inherited training history, legal reset/init operations, actual starvation checkpoint, exact frame/exposure accounting, auxiliary-label authority, scene ontology, deterministic terminal predicates, reward aggregation and reference implementation. “New delayed relation” also needs a protocol separating old-task memorization from later acquisition at equal pretraining and probe cost. Probe training cannot become free extra data.

The project history matters scientifically. A deliberately dead temporal head or broken normalization state could manufacture a recovery effect that disappears when a basic implementation bug is fixed. Establish a naturally arising starvation trajectory and compare it with a healthy same-data learner before interpreting a gap as plasticity research. Maintain native short-event performance during that comparison; a restored head that forgets useful skills has not necessarily improved the promised outcome.

## Duplicate check

T11 was checked through its FIX packet: it concerns counterfactual visual evidence, event ordering and supervised/GRPO support. C012 shares its temporal evaluation surface but adds an inherited loss of trainability. That is a potential new mechanism rather than an exact duplicate, although both can collapse to direct temporal supervision. I did not read other creative or D cards for a comprehensive duplicate determination. Format exemplar text is not evidence for semantic overlap.

## Verdict, required fixes and cheapest decisive check

CUT the proposal as specified. Its difficulty argument excludes important standard controls from consideration without identifying a residual mechanism beyond them. A new submission would need a concrete, feasible interference between restoring long-delay plasticity and preserving short-event competence that survives selective resets, continual renewal, direct temporal targets and affordable restart. Forbidding those legal actions would not be a repair.

The cheapest decisive empirical screen is a matched recovery study, proposed at ESTIMATED 21 H100-hours: compact video learner, competing balanced replay, selective temporal reset, recycling, shrink-and-perturb and reference arms, followed by new-relation acquisition and short-event retention evaluation. This is an early rejection pilot, not the full bar panel or a precision guarantee. It requires actual architecture/throughput profiling; the source card's ESTIMATED 16 GPU-h omits much of this control set. No experiment has been run or authorized here.

If reconsidered, the delivery must still isolate scene truth and base assets, retrain from authentic data-derived recipes, cap decoded payloads, bind exposures to weights, and reject spoofed/skipped work. Portable container lifecycle, trusted library resolution, symmetric warmup, per-seed deadlines, fixed denominators, independent equivalent-positive banks, private decontamination and archived per-item records remain mandatory. These protect measurement validity; none changes the legal plasticity recipe's score. A live adversarial transcript and executable `tests/test_anticheat.py` would be future evidence, not something this desk review provides.

## Verdict record

id: C012
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.76 (ESTIMATED 0.56–0.94)
combined_recipe_attack: ESTIMATED 0.76 (ESTIMATED 0.56–0.94)
best_of_4: ESTIMATED 0.84
pass_at_4: ESTIMATED 0.93
single_run_max: ESTIMATED 0.91
upper95_projected: ESTIMATED 0.98
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 21
required_fixes: none
main_kill_reason: published plasticity restoration covers proposed intervention
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
