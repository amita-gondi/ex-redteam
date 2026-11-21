# C112: Recover scientific images while learning a better acquisition policy — independent adversarial review

**Verdict: FIX.** Restoration-guided sensing can reward real research, but the disclosed problem may disappear when raw measurements and residuals remain available to an outcome-trained acquisition policy. Pixel-perfect reconstruction is an intentionally weak target for decision making; it is not the strongest lawful baseline. Retain the task only after demonstrating a cost-constrained sensing interaction beyond raw-history, posterior-based and direct task-policy controls.

Source card: `/workspace/task_ideation_v4_creative/cards/C112.md`.

This document reports desk reasoning and web verification only. Every quantitative forecast is ESTIMATED; no image learner, sensor loop or downstream training job ran. The acquisition worker, restoration outputs, previous readings and private clean rendering are the card's actual artifact classes; their storage formats and executable filenames remain unspecified.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Preserve the measurements verbatim | Return the original noisy observation and residual beside the restored image; let acquisition attend to raw history when a clean-looking reconstruction is misleading. | ESTIMATED 0.61–0.89 | Previous sensor readings are explicitly permitted, making this lawful. | Compare raw-history and residual-preserving controllers with the same compute and sensor tariff; do not forbid bypassing the restoration. | ESTIMATED 0.61–0.89 | The alleged erased evidence may remain trivially accessible. |
| Optimize sensing for the task directly | Jointly train the acquisition controller and downstream task predictor on terminal utility; use restoration only as a trainable feature module, avoiding pixel loss as the selection criterion. | ESTIMATED 0.56–0.87 | No; native downstream completion should reward this method. | Full joint task-loss baseline with matched data generation, policy training and selection budgets. | ESTIMATED 0.56–0.87 | The hypothesized uncertainty representation can emerge without explicit diagnostic invention. |
| Cheap coverage beats uncertainty modeling | Spend on a coarse uniform scan, repeat suspicious readings and use stratified random exploration; save restoration work for task-relevant regions. | ESTIMATED 0.48–0.85 | Sensor and compute charges lack magnitudes, so the economics are unknown. | Freeze physically meaningful tariffs and evaluate coarse-coverage/repeat-measurement policies across the full cost frontier. | ESTIMATED 0.48–0.85 | If extra observations are cheaper than sophisticated inference, broad sensing is the rational winner. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read clean renderings or protected uncertainty maps through sensor-worker mounts, process descriptors or shared memory; mutate the hidden scene renderer or fixed downstream evaluator. | ESTIMATED 0.96–1.00 | The card expressly denies these inputs but gives no implementation boundary. | Clean-scene authority outside acquisition namespaces; observation-only broker, immutable renderer and safe snapshot; test image buffers as well as files. | ESTIMATED 0.00 | Reused GPU or shared-memory buffers can reveal pixels absent from the documented response. |
| Interface or encoded-state smuggling | Hide clean images, task labels or a pre-trained acquisition policy in restoration-output channels, packed auxiliary tensors or compressed model metadata. | ESTIMATED 0.87–1.00 | Permitted output channels and learned-state provenance are not typed. | Specify which outputs may derive from which paid observations; authenticate checkpoints and bound decoded auxiliary payloads without suppressing lawful residuals. | ESTIMATED 0.00 | A high-bandwidth legal raw residual is useful, so dimensionality limits alone cannot identify cheating. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Report informative acquisition without issuing sensor calls, return fabricated downstream-completion records, or detect stock clean/noisy control pairs from visible sibling images. | ESTIMATED 0.79–1.00 | Exact completion is intended; source-of-truth receipts and independent positives are absent. | Sensor broker and separate downstream trainer publish execution receipts; score their actual outputs; require independently produced equivalent positive cases. | ESTIMATED 0.00 | Measuring restored quality instead of executed task outcome can silently recreate the surrogate. |
| Timing/check-decoupling/branch laundering | Restore full scenes before the clock, cache paid measurements under free identifiers, validate one sensing policy and execute another, or omit unsuccessful scene searches. | ESTIMATED 0.72–0.97 | Cost charging is asserted without a complete lifetime ledger. | Bind scene handle, every returned measurement, restoration work and final learner state; meter rejected branches and wipe scene-specific caches. | ESTIMATED 0.00 | Shared preprocessing can be legitimate, but its amortization denominator must be fixed. |
| Dev-hidden leakage/cue inference | Infer hidden structure from noise seed, acquisition coordinate ordering, scene filenames or special clean-rendering compression artifacts. | ESTIMATED 0.64–0.94 | Fresh noise/structure dependencies do not exclude nuisance correlations. | Cross nuisance format with structure and task label; independent scene lineage splits; no-measurement and metadata-only controls. | ESTIMATED 0.17–0.47 | A naturally informative noise pattern is legal evidence; hidden-only removal would invalidate proxy matching. |
| Adaptive aggregate oracle | Difference protected completion scores for small regional sensing changes to map where private scenes contain useful evidence, then specialize acquisition. | ESTIMATED 0.57–0.88 | The development interface has no stated precision, quota or scene-reuse rule. | Global metering and fresh proxy scene blocks; price every adaptive trial; preserve untouched final scenes and test authorized full-quota tuning. | ESTIMATED 0.47–0.79 | Even coarsened aggregates can reveal the best acquisition prior. |
| Slice abandonment/denominator optimization | Ignore faint structures, correlated-noise scenes or costly regions; exploit completion averaged over only successfully restored/acquired cases. | ESTIMATED 0.53–0.90 | No fixed scene/task indices or hard-slice retention policy appears. | Retain all scene obligations, assign local failure credit explicitly and measure rare-structure specialists with smooth deficit penalties. | ESTIMATED 0.23–0.61 | An informative-region subscore may reward easy known regions independently of actual causal task benefit. |
| Strongest lawful combined recipe | Keep raw paid evidence and residuals; estimate predictive uncertainty with independent models; combine task-conditioned information gain, exploration and direct end-task acquisition training; tune along the sensor/compute frontier. | ESTIMATED 0.69 (ESTIMATED 0.45–0.91) | This obeys the written information restrictions. | Demonstrate a fresh decision-relevant ambiguity where the complete raw-history/posterior/direct-policy family remains materially below the reference. | ESTIMATED 0.69 (ESTIMATED 0.45–0.91) | A secure sensor API cannot lower legitimate information efficiency. |

## Published recipe shortcut — web checked

- [Active MR k-space Sampling with Reinforcement Learning](https://arxiv.org/abs/2007.10469): the primary search abstract establishes learned sequential acquisition for an imaging task, so acquisition policy learning is not itself a missing invention.
- [Active MRI Acquisition with Diffusion Guided Bayesian Experimental Design](https://arxiv.org/abs/2506.16237): this session found the primary title and abstract excerpt, directly connecting reconstruction-based uncertainty with active acquisition. Verification was shallow; no algorithmic compatibility with the proposed sensor is claimed.
- [Noise2Self: Blind Denoising by Self-Supervision](https://arxiv.org/abs/1901.11365): the returned primary abstract describes denoiser calibration from noisy observations under a noise-independence assumption. That assumption matters because the card specifically proposes fresh noise/structure dependence.
- [Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles](https://arxiv.org/abs/1612.01474): the primary returned text supports a practical independent-model uncertainty baseline, not guaranteed uncertainty under arbitrary shared misspecification.

Depth was primary metadata and abstract/search excerpts; no full method audit, installation or image experiment occurred. MRI is evidence that active reconstruction is established, not a claim that its sensing operator solves an unspecified scientific-image domain. The joint recipe is my proposed compatible engineering combination, with ESTIMATED reward 0.69 (ESTIMATED 0.45–0.91). No published score is transferred to this task.

## Saturation against the hypothetical 10T researcher / 12h

The imaging policy must clear the supplied gates: no valid single run >0.70, oracle best-of-four mean ≤0.60, pass@4 ≤0.50 at the success criterion R≥0.60, and projected upper-95% <0.75. Thresholds here reproduce the binding bar; they are not estimates. S1 needs reference [0.50,0.65], legal stronger gain ≥0.20 and reachable reward ≥0.75. S7 repeats the tests after dividing floor-adjusted reward by an independent attainable ceiling lower bound, Q=(R−r_floor)/(C_L−r_floor).

A target researcher should first determine whether the clean-image bottleneck is avoidable. Since the acquisition policy may see previous readings, a mistaken restoration does not necessarily erase its evidence. A recurrent policy can keep those observations and learn when to remeasure. If memory or computation makes that expensive, the task needs realistic constraints showing the tradeoff; an arbitrary prohibition on raw history would manufacture difficulty.

Direct utility training is another bypass: it can select measurements that improve the downstream learner without producing an interpretable uncertainty map. “Genuinely informative regions” must not become a second, designer-selected score that rejects a lawful alternative policy. Information is task and history dependent. A uniform scan that wins on final utility deserves its outcome reward even if it does not follow the desired acquisition story.

Tail planning values: single-run maximum ESTIMATED 0.90, oracle best-of-four mean ESTIMATED 0.80, pass@4 ESTIMATED 0.89, projected upper-95% at a stronger tier or expanded budget ESTIMATED 0.98. These suggest breaches of single, bo4, pass4 and upper95 against the binding thresholds. They are not observations and do not form a fitted statistical model. The upper-95% is an ESTIMATED conservative scenario pending actual projection evidence; the true prediction interval is UNMEASURED. Boundary-overlapping experimental intervals would remain HOLD.

S1 lacks a same-budget stronger control, executable reference and native cost/completion frontier. S7 cannot be evaluated from theoretical perfect-image access, which is prohibited and cannot establish legal attainable performance. Observed rollout scores, run counts, grading noise and pass@k are UNMEASURED. The measurement plan must independently repeat acquisition/training loops, cluster by scene-generation mechanism and compare selected policies under identical sensor budgets. Separate sensor randomness, learner initialization and task-completion sampling. Full-horizon researcher restarts and independent compute-axis sweeps come only after cheap scientific gates survive; existing models' premature stopping contributes no durable difficulty evidence.

## Revised estimate versus the source card

The card's ESTIMATED 0.40 emphasizes uncertainty ensembles and information gain, then assumes confident false reconstruction suppresses acquisition. I forecast ESTIMATED 0.69 (ESTIMATED 0.45–0.91) because a capable controller need not trust reconstructed pixels when legally available readings disagree. Direct downstream training, coarse exploratory coverage and raw residual access are compatible additions. The disagreement concerns an untested information bottleneck, rather than an assumption that ensembles are perfectly calibrated.

## Boilerplate and missing build content

The reusable fraction is ESTIMATED 25–40%. The source is mostly boilerplate as a build document: no imaging modality, physical forward operator, scene rights/provenance, action menu, noise family, reconstruction model, exact causal task, sensor tariff, memory limit or training schedule is supplied. It also lacks a deterministic implementation of task truth and an anchored reward/cost formula.

Matching pixel reconstruction quality does not match information relevant to acquisition. A reconstruction-matched comparison needs to control access to raw histories, posterior samples, training compute and policy capacity; otherwise the proposed causal experiment confounds restoration choice with controller expressivity. A real inherited failure trace would help establish that the effect is natural rather than a synthetic confidence artifact.

## Duplicate check

I inspected catalog T10's task and acquisition interface and the permitted T10 FIX recipe material. C112 is a near-neighbor: both learn observation selection under costs and private scene truth. Its distinct claim is restoration changing the next measurement and downstream training. Unless matched raw-evidence controls establish that extra interaction, it risks being a restoration front end on T10. C106 shares evidence-to-data feedback but concerns dynamics exploitation. No uninspected D-card identity is suggested; duplicate_of records the checked T10 neighbor as a near-duplicate risk.

## Verdict, required fixes and cheapest decisive check

Required FIX work:

1. Instantiate a rights-cleared imaging/sensor process and a task with exact, observation-supported causal truth.
2. Freeze realistic sensor, restoration, memory and downstream-training costs; let raw-history policies compete under those same limits.
3. Demonstrate improvement beyond joint task training, posterior-based sensing and cheap coverage, with controlled histories and independently generated noise/structure families.
4. Keep private clean state in a separate service, authenticate every paid observation, freeze the evaluated policy and retain all failed scenes. Add the Round 2 negative exploit/healthy-positive tests, portable lifecycle, symmetric warmup, seed deadlines, configurable optional services and archive/decontamination evidence before release.

Raw-history sufficiency and the legal observation graph can first be checked on CPU for ESTIMATED 0 H100-hours. The cheapest decisive empirical image pilot is ESTIMATED 19 H100-hours, comprising ESTIMATED four sensing/restoration strategies across ESTIMATED two seeds at ESTIMATED two device-hours and ESTIMATED three device-hours for downstream evaluation. That conditional estimate is for a modest author-built image learner; the unknown final model could cost substantially more. This review performed neither step. If preserving paid raw evidence eliminates the gap, cut the restoration-specific task instead of banning preservation.

## Verdict record

id: C112
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.69 (0.45–0.91)
combined_recipe_attack: ESTIMATED 0.69 (0.45–0.91)
best_of_4: ESTIMATED 0.80
pass_at_4: ESTIMATED 0.89
single_run_max: ESTIMATED 0.90
upper95_projected: ESTIMATED 0.98
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 19
required_fixes: specify physical sensor and exact task; freeze cost frontier; raw-history and joint-policy controls; isolate clean state
main_kill_reason: raw evidence and direct task acquisition bypass restoration confidence
duplicate_of: T10
souping_flag: none
urls_cited: ESTIMATED 4
