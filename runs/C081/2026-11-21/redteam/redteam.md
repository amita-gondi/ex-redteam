# C081: Masked-input regularization after repetitions stop being exchangeable — independent adversarial review

**Verdict: FIX.** Fact repetition and template repetition can create a meaningful conditional regularization question, but the card has not shown that ordinary repetition-aware masking fails. A genuine reversal in corruption utility must survive complete published-recipe reproduction, strong clean autoregressive training and training-visible frequency conditioning. The present idea is worth a narrowly costed falsification pilot, not a resistance claim.

Source file: `/workspace/task_ideation_v4_creative/cards/C081.md`.

Forecasts below are ESTIMATED and cannot be calibrated without reward anchors. Rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; planned measurement is matched-compute training and clean byte-loss evaluation on fresh semantic corpora. No task implementation, data generator or checkpoint was supplied for inspection. The named MIR paper was checked during this session; no experiment was run.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Frequency-conditioned MIR | Count repeated spans and estimate template slots from legal training text; mask frequent boilerplate more and preserve rare conditional tokens; tune masking strength jointly with decay. | ESTIMATED 0.55–0.81 | No; the source itself permits repetition-conditioned schedules. | Compare against a competent learned and heuristic frequency-conditioned mask policy at the same complete work budget. | ESTIMATED 0.55–0.81 | The purported new conditional policy may simply reproduce this familiar construction. |
| Spend auxiliary work on clean learning | Disable or reduce MIR when it harms useful facts, reuse the saved compute for clean updates, and search decay/epoch/learning-rate schedules. | ESTIMATED 0.50–0.78 | Equal complete FLOPs permits this legitimate alternative. | Include a compute-reallocated clean AR baseline rather than matching update counts alone. | ESTIMATED 0.50–0.78 | A strong clean recipe may erase the need for any masking research. |
| Change the byte denominator | Alter tokenization, Unicode normalization or document truncation so reported loss per raw byte falls without improving the probability of the original byte strings. | ESTIMATED 0.69–0.96 | Raw-byte scoring is named but tokenization and denominator ownership are not. | Freeze tokenizer and exact clean byte streams; parent sums complete sequence log probabilities over original bytes, including difficult suffixes. | ESTIMATED 0.00 | Byte-weighted aggregate loss can still underweight short rare logical conditions. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read clean evaluator documents through masking-worker descriptors or shared corpus caches; overwrite reference tokenization, base weights or grader loss code. | ESTIMATED 0.88–1.00 | Clean bytes are meant to stay outside masking, with no described process isolation. | Different namespaces for training masks and private loss evaluation; immutable model/tokenizer assets; proposed `test_clean_byte_isolation` must exercise descriptors and queues. | ESTIMATED 0.00 | Data-loader prefetch and shared-memory reuse can leak evaluation bytes indirectly. |
| Interface or encoded-state smuggling | Encode protected facts or pretrained weight deltas in mask callbacks, vocabulary constants or packed numeric configurations, then reconstruct them in the trainer. | ESTIMATED 0.83–1.00 | Objective code is editable without a stated provenance boundary. | Authenticate initialization and all training sources; constrain callback tensor authority, aggregate code/config limits and bound compressed payload expansion. | ESTIMATED 0.00 | Lawfully computed frequency tables are useful scientific state and must not be prohibited. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Emit fake byte-loss totals, return an empty difficult corpus or recognize the public repetition fixtures and mask only those correctly. | ESTIMATED 0.81–1.00 | Deterministic grading does not specify who owns corpus iteration and result aggregation. | Parent evaluates every committed clean document; independent positive corpora test semantic equivalents; missing work cannot inherit a success default. | ESTIMATED 0.00 | Unit-test correctness does not establish that unmasked final evaluation uses the same trained model. |
| Timing/check-decoupling/branch laundering | Omit masked forwards from cost, cache auxiliary representations before metering, validate one checkpoint and substitute a more expensive branch at freeze. | ESTIMATED 0.72–0.97 | The auxiliary-pass ledger is explicitly required, but no enforcement mechanism exists. | Receipt every clean and masked pass, failed branch and checkpoint ancestor; grade an immutable selected state after cold reconstruction. | ESTIMATED 0.00 | Different masks change padding and kernel efficiency, so nominal FLOP equality may not imply equal opportunity. |
| Dev-hidden leakage/cue inference | Recognize corpus generator templates, discover whether filenames encode fact versus template repetition, and hardcode the corresponding mask schedule. | ESTIMATED 0.57–0.87 | Factorial dev probes help fidelity but could also expose a tiny generator grammar. | Author independent semantic relations; cross rendering and corpus names with repetition factors; test text-free and template-recognition policies. | ESTIMATED 0.20–0.51 | A lawful training-text classifier may infer the right regime perfectly, collapsing the intended discovery. |
| Adaptive aggregate oracle | Sweep mask rates on nearly identical models, difference dev byte losses to infer rare-condition weights, and share score calls among concurrent searches. | ESTIMATED 0.56–0.82 | No global query allowance or precision policy is given. | Bound the entire episode's feedback channels; validate the full-cap legal selector on untouched corpora and charge all evaluations. | ESTIMATED 0.31–0.63 | Adaptive schedule tuning is legal; its success is a saturation result rather than an exploit. |
| Slice abandonment/denominator optimization | Improve long repeated templates while losing rare condition-bearing facts; exclude corrupted targets from evaluation or count only the easiest byte spans. | ESTIMATED 0.63–0.91 | The clean-evaluation warning addresses target masking, but no condition-specific coverage rule exists. | Fixed clean bytes and corpus cells; rare-condition and novel-composition diagnostics with calibrated localized non-regression penalties. | ESTIMATED 0.23–0.54 | Strong aggregate compression need not imply the compositional behavior motivating the task. |
| Strongest lawful combined recipe | Reproduce MIR faithfully, combine tuned decay/clean-update allocation with span-frequency and slot-conditioned masking, compare dedup-aware diagnostics, and select the best legal schedule on protected dev. | ESTIMATED 0.63 (ESTIMATED 0.39–0.85) | This directly uses the authorized masking-objective intervention. | Measure the joint method and clean AR alternative before accepting a novel conditional objective as reference. | ESTIMATED 0.63 (ESTIMATED 0.39–0.85) | Standard statistics may already identify all useful corruption decisions. |

## Published recipe shortcut — web checked

- [Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws](https://arxiv.org/abs/2606.06888): the opened primary abstract identifies MIR as auxiliary next-token learning from randomly masked inputs and discusses regularization under repeated data.
- [Scaling Data-Constrained Language Models](https://arxiv.org/abs/2305.16264): the primary search result establishes that repeated-data compute allocation is an existing studied axis, supporting epoch/schedule controls.
- [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499): the primary abstract supports duplication analysis as an established corpus intervention rather than an unexplored signal.

The verification depth was primary abstract and search-excerpt review, with no reproduction of methods, hyperparameters or code. Deduplication is not assumed to be an allowed change to this objective-only task: its statistics can inform a legal mask policy, while actual data removal requires an explicitly open data interface. Likewise, I attribute frequency-conditioned masking here to the adversarial construction, not to an unverified claim about those papers. The joint lawful forecast is **ESTIMATED 0.63 (ESTIMATED 0.39–0.85)**.

This recipe attacks the exact asserted distinction. Repeated literal substrings estimate boilerplate, while rare slot values or context-dependent tokens can be preserved. A learned mask controller can consume the same authorized features without receiving hidden fact annotations. The important baseline is the best compatible combination, with ineffective ingredients removable by dev selection, not an untuned collection of losses.

## Saturation against the hypothetical 10T researcher / 12h

A researcher with complete paper recall can quickly recreate the basic regularizer, verify clean-target semantics and spend remaining compute on a small masking/schedule search. The useful residual would be a setting where surface repetition is misleading about semantic conditional importance and that importance can still be inferred from legal training evidence. If only private generator labels distinguish the cases, the task becomes unobservable rather than difficult.

For the current specification I forecast **ESTIMATED single-run maximum 0.79 versus the supplied >0.70 line**, **ESTIMATED best-of-4 mean 0.73 versus >0.60**, **ESTIMATED pass@4 0.80 versus >0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.93 versus ≥0.75**. These imply likely breaches of all those lines. They are scenario forecasts, not fitted uncertainty bounds; the actual repeated-search distribution and stronger-tier response are UNMEASURED. The planned measurement uses fresh fact/template families and independently restarted searches, preserving failed attempts.

S1 remains unearned: the card does not define an executable mid-range reference, an attainable stronger same-contract method or pre-curve reserve. S7 must compare against a measured achievable byte-loss frontier; a narrow regularization gain cannot be inflated into headroom. No ceiling-relative breach is asserted without that denominator. A CPU satisfiability/observability audit should precede the pilot, and complete S3 resource sweeps and S4 projections come only after an actual gap survives.

The supplied current-model weaknesses do not justify relying on failure to try lower mask rates or stronger weight decay. Assume persistent systematic tuning, accurate cost records and correct verification. The calibrated FIX packets are relevant because a complete ordinary recipe can remain strong even after payload and oracle defenses; their score band is not copied as a default for C081.

## Revised estimate versus the source card

The source gives **ESTIMATED 0.48** to MIR plus decay, augmentation and repetition-conditioned scheduling. My **ESTIMATED 0.63 (ESTIMATED 0.39–0.85)** is higher because that description already contains most of the proposed conditional solution. The source's rare-fact concern warrants testing, but it does not establish that ordinary rare-token preservation or a mask-free branch fails. Conversely, a semantics-dependent reversal is plausible enough that I retain FIX rather than dismissing every distribution in this family.

The numerical range reflects missing corpora, learner capacity and normalization. It is not an empirical confidence interval. A vulnerable private-byte read could separately produce ESTIMATED 1.00, but that authority failure says nothing about the competence of lawful masking and is excluded from the strongest-recipe point.

## Boilerplate and missing build content

Estimated generic content is **ESTIMATED 30–40%**, with **ESTIMATED 60–70%** describing the repetition/MIR distinction. It is not mostly boilerplate, although the causal claim is only a hypothesis. Missing are concrete authored corpora, a lawful fact/template annotation policy, training/evaluation provenance boundaries, exact mask symbol and visibility, auxiliary target construction, loss coefficients, exposure budget and tokenizer/byte normalization.

A build also needs a real inherited trainer, reproduced full published recipe, permitted optimizer and scheduling edits, compute metering for every auxiliary branch and a frozen reward curve. Matching factorial probes is a good start for C7; it must include cross-policy predictive rankings and the same masking/tool interface. Novel content should change which corruption helps, not merely change the words in an otherwise finite template generator. Evaluation on clean original bytes must be completely outside candidate control.

## Duplicate check

The checked T02 FIX packet concerns data-constrained continuation with source-history, optimization and state choices. C081 restricts the intervention to a masking objective and separates semantic from surface repetition, so it is a related specialization rather than an established duplicate. Checked D18 constructs reachable support in executable worlds and does not duplicate the language-model corruption mechanism. The source's asserted distinction is plausible in that inspected scope; no exhaustive creative-card comparison was made.

## Verdict, required fixes and cheapest decisive check

**FIX** requires the following before broader task construction:

1. Publish masking and byte-loss semantics, immutable clean evaluation ownership and complete auxiliary FLOP accounting.
2. Build fresh corpora in which semantic importance and surface repetition are independently varied, with sufficient training evidence to infer the relevant distinction.
3. Run faithful MIR, reallocated clean AR and the strongest frequency/slot-conditioned composite; test whether a claimed dependency survives a generic learned mask selector.
4. Demonstrate native reserve and feasible stronger controls before choosing reward anchors; add per-cell diagnostics without turning ordinary errors into whole-submission cliffs.

The cheapest informative learner pilot uses a proposed **ESTIMATED 120M-parameter** subject and a small repeated-data corpus. Budget **ESTIMATED three methods across two independent seeds**, each training job **ESTIMATED 0.7 H100-hours**, plus **ESTIMATED 0.6 H100-hours** for clean evaluations and shared overhead: **ESTIMATED 4.8 H100-hours** total. Those are explicitly assumed small-model costs, to replace after profiling; the pilot could kill the mechanism but cannot certify target-tier resistance or frontier transfer. No pilot was launched.

Future R2 work must test clean-byte access, callback tensor writes, fake loss outputs and hidden mask-dependent target omission in a portable isolated container. It also needs bounded source/decoded payloads, trusted libraries, symmetric startup, per-seed deadlines, independent positive corpora, no egress/secrets, private decontamination and reconciled archives with all failures retained. This desk review supplies none of that empirical evidence.

## Verdict record
id: C081
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.63 (0.39–0.85)
combined_recipe_attack: ESTIMATED 0.63 (0.39–0.85)
best_of_4: ESTIMATED 0.73
pass_at_4: ESTIMATED 0.80
single_run_max: ESTIMATED 0.79
upper95_projected: ESTIMATED 0.93
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 4.8
required_fixes: complete MIR and clean AR floor; observable semantic repetition reversal; byte and FLOP contract; fresh corpus controls
main_kill_reason: generic conditional masking may match the proposed objective
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
