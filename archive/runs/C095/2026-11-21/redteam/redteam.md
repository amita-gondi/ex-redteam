# C095: Find an optimizer coordinate system beyond standard recipe sweeps — independent adversarial review

**Verdict: CUT.** Rotating an adaptive optimizer into a learned curvature basis is already a published recipe, and the card does not instantiate a domain-reuse phenomenon that survives it. Its state-budget caveat has no numerical contract or feasible stronger control. The proposal currently names a research aspiration rather than a defensible unsolved task distribution.

Source file: `/workspace/task_ideation_v4_creative/cards/C095.md`.

All optimizer and reward comparisons here are ESTIMATED conditional judgments. Training curves, rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; planned measurement would compare complete optimizers on paired domain-reuse streams with identical persistent bytes and full auxiliary work. No source optimizer, learner, benchmark or task package was executed. Future component/test labels are proposals only.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| SOAP already supplies the coordinates | Estimate structured gradient moments, rotate into their eigenbasis, run adaptive moments there and refresh the basis at a charged tuned cadence. | ESTIMATED 0.67–0.92 | No; coordinate reparameterization is the intended legal intervention. | Include a faithful SOAP family, with state-matched blocking when necessary, before asserting a coordinate insight. | ESTIMATED 0.67–0.92 | The entire reference may be a special case of existing rotated adaptive optimization. |
| Reset contaminated moments | Detect domain-return transitions from lawful probes; compare keep, reset and decay of optimizer memory while tuning ordinary learning schedules. | ESTIMATED 0.55–0.83 | No transition law shows why generic state hygiene is inadequate. | Give all methods the same observable probes and compare a fully tuned reset/decay family. | ESTIMATED 0.55–0.83 | A moment-state problem can be mislabeled as a representation problem. |
| Extra model hiding in the transform | Retain learned coordinate matrices or low-rank factors as an additional prediction path, or use function-changing nonlinear “reparameterization” to increase effective capacity. | ESTIMATED 0.72–1.00 | Fixed capacity is stated but functional equivalence and state ownership are undefined. | Require an invertible coordinate map with explicit canonical model reconstruction and total state/compute inventory; independently check round trips. | ESTIMATED 0.00 | Legitimate optimizer state also stores useful history; capacity must be defined by deployed function rather than raw tensor count alone. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read private future-domain probes from trainer queues or descriptors; modify fixed initialization, held-out loss code or reference optimizer state. | ESTIMATED 0.89–1.00 | No trusted trainer and transform-worker separation is specified. | Root owns original model and evaluation streams; isolate transform workers and shared buffers; proposed `test_coordinate_asset_access` attempts mount/proc/IPC reads and frozen writes. | ESTIMATED 0.00 | Optimizer access to model tensors must not imply access to evaluation truth or parent memory. |
| Interface or encoded-state smuggling | Encode fitted target-domain tensors or labels in basis initialization constants, checkpoint metadata or procedural coordinate maps; install them as supposedly equivalent state. | ESTIMATED 0.83–1.00 | The source warns about capacity but not arbitrary state injection. | Bind initialization/training lineage, bound auxiliary channels and require data-derived optimizer transitions with no unreceipted parameter replacement. | ESTIMATED 0.00 | A compact legal preconditioning algorithm is powerful and cannot be excluded because it resembles a learned transform. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Return fabricated post-reuse loss, skip a failing reuse stream or recognize canonical equivalence fixtures from their exact matrices. | ESTIMATED 0.85–1.00 | Equivalent-parameterization comparisons are promised, not independently specified. | Parent evaluates canonical weights on every stream; use independently generated equivalent maps and all-positive checks; missing training work never counts as convergence. | ESTIMATED 0.00 | Equivalence at initialization does not guarantee the optimizer follows the claimed recurrence later. |
| Timing/check-decoupling/branch laundering | Exclude eigendecomposition, basis transfer or temporary dense covariance from the FLOP ledger; train in an expensive hidden basis and submit a cheap equivalent endpoint. | ESTIMATED 0.76–0.98 | Fixed bytes/FLOPs is a principle without a lifetime accounting boundary. | Count all decompositions, conversions, scratch peaks, moment transport and search branches; capture state and receipts from the actual trained path. | ESTIMATED 0.00 | Peak temporary state and persistent bytes are distinct resources, both needing declared treatment. |
| Dev-hidden leakage/cue inference | Infer future reused domain from corpus order or probe filenames and hardcode a basis schedule; recognize a public synthetic curvature generator. | ESTIMATED 0.58–0.89 | Fresh relations are promised while observation-to-future correlations remain unspecified. | Independently author reuse relations; cross serialization and transition markers; compare metadata-only, static-basis and universal-generator controllers. | ESTIMATED 0.26–0.59 | Inference from legitimate curvature probes is intended research, and may make a simple controller sufficient. |
| Adaptive aggregate oracle | Sweep ranks, block partitions and refresh triggers, difference protected loss responses and coordinate search jobs under separate state handles. | ESTIMATED 0.59–0.86 | The dev observable-probe promise sets no scoring-channel limit. | One episode-wide feedback ledger, fresh evaluation blocks and complete selection cost; measure full-cap legal optimizer search. | ESTIMATED 0.35–0.67 | Low-dimensional joint search can discover an adequate basis schedule without the proposed diagnosis. |
| Slice abandonment/denominator optimization | Optimize latest-domain loss while forgetting reused features; omit failed return streams or average losses per batch instead of fixed valid-token/domain weights. | ESTIMATED 0.64–0.93 | Private loss after reuse is useful but the retention population and weights are missing. | Freeze acquisition/return-domain cells and token denominators; report native losses and deliberate newest-domain specialization under smooth non-regression penalties. | ESTIMATED 0.23–0.56 | Mild floors can leave profitable forgetting; harsh floors can erase learning signal. |
| Strongest lawful combined recipe | Search SOAP/Shampoo-style structured coordinates and Muon/AdamW alternatives; tune rank/block allocation, basis cadence, moment reset/transport and schedules at equal total bytes and matrix work. | ESTIMATED 0.80 (ESTIMATED 0.53–0.95) | These are lawful optimizer alternatives within the proposed intervention. | Benchmark the best compatible single method against a concrete causal reference; security work supplies no capability reduction. | ESTIMATED 0.80 (ESTIMATED 0.53–0.95) | Known coordinate adaptation may absorb every useful effect in the still-undefined learner. |

## Published recipe shortcut — web checked

- [SOAP: Improving and Stabilizing Shampoo using Adam](https://arxiv.org/abs/2409.11321): the opened primary abstract explicitly describes Adam in the preconditioner's eigenbasis and continuing moment updates while the basis changes slowly.
- [Shampoo: Preconditioned Stochastic Tensor Optimization](https://arxiv.org/abs/1802.09568): the primary abstract establishes structured tensor-dimension preconditioners as an existing way to reduce full curvature storage.
- [Muon official repository](https://github.com/KellerJordan/Muon): the opened project README supplies an orthogonalized-update alternative and explicitly separates hidden-weight optimization from ordinary handling of other parameter classes.

Primary abstract/README verification establishes these mechanisms. No optimizer code was installed, no paper result was reproduced and no compatibility with the card's unspecified model was established. The strongest composite is a searched family of compatible choices, not a claim that simultaneously applying every preconditioner helps. Its scenario score is **ESTIMATED 0.80 (ESTIMATED 0.53–0.95)**.

This prior art is particularly close. The card's argument that standard methods share mistaken coordinate assumptions omits a method whose central construction changes those coordinates. Blocking or reducing refresh frequency to fit the task budget is a fair adaptation only if the reference pays for the same mathematical work and storage. If no useful published configuration fits, that needs an explicit byte/FLOP witness rather than a verbal assertion.

## Saturation against the hypothetical 10T researcher / 12h

A competent research solver can recognize SOAP, implement a known family, profile its matrix work and jointly tune block size, refresh and reset. It can use observable gradient/probe data to detect nonstationarity without receiving private future labels. The proposed domain transitions could genuinely require a new transport rule, but no concrete law, inherited failure or admissible reference is supplied to support that possibility.

My conditional saturation estimates are **ESTIMATED single-run maximum 0.93 versus >0.70**, **ESTIMATED oracle best-of-4 mean 0.88 versus >0.60**, **ESTIMATED pass@4 0.95 versus >0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.99 versus ≥0.75**. They likely breach all absolute gates. These forecasts are neither measured scores nor fitted confidence bounds. Their basis is direct overlap between the desired intervention and an available complete optimizer, with uncertainty captured by the broad recipe range.

S1 lacks any executable reference and stronger same-deployment control; no native headroom has been measured. S7 has no achievable loss/compute ceiling bracket. A severe state cap could make both the baseline and reference physically incapable of tracking changing directions, rather than creating a learnable advantage. A loose theoretical optimum or extra-state oracle cannot establish attainability under that cap. Both gates remain OPEN and cannot be counted as independent observed failures.

Plan budget sweeps separately over researcher tokens, serial search, concurrent subject runs and subject training work. Grade repeatability must include basis nondeterminism, eigenvalue degeneracy and whole retraining variance. Pre/post-coordinate function checks need canonical tensor precision rather than comparing only parameter metadata. All are UNMEASURED, with matched domain-stream restarts and fresh-container repeat grades as the planned measurements. An overlap with a binding cutoff would remain HOLD.

## Revised estimate versus the source card

The source assigns **ESTIMATED 0.38** to strong AdamW/Muon updates, low-rank preconditioning and condition-triggered refresh. I assign **ESTIMATED 0.80 (ESTIMATED 0.53–0.95)** after explicitly including SOAP and tuning reset/transport as part of the baseline. That combination is not automatically weaker than a proposed author transform. The source does not quantify either its storage disadvantage or the reference's attainable benefit.

I also reject using current Sol/Astra or Opus weaknesses as evidence against the hypothetical solver. Those reports contain caveats and known-recipe strengths; early stopping, conservative experiments and weak testing are removed from this threat model. The complete-recipe calibration packets warn against optimistic component-by-component scoring, but C095's estimate comes from unusually direct algorithmic overlap rather than their numerical band.

## Boilerplate and missing build content

This is the least instantiated mechanism among the reviewed optimizer proposals: **ESTIMATED 45–55%** of its prose is general optimizer/research framing and **ESTIMATED 45–55%** supplies the domain-reuse/coordinate concept. **Mostly boilerplate for build purposes:** a builder cannot reconstruct the mathematical learner or resource law from it. That judgment concerns missing semantics, not a measured text-overlap score.

Missing items include model architecture, natural domain reuse process, legal parameter group definitions, function-preserving map class, inversion guarantees, state byte cap, scratch budget, compute prices, probe visibility, schedule authority and canonical checkpoint semantics. It also lacks an inherited stalled project and evidence that the stall survives healthy standard training. Comparing equivalent initial parameterizations diagnoses sensitivity; it does not by itself prove why later improvement occurs or exclude additional effective work. A causal experiment must isolate coordinate choice from moments, regularization, numerical precision and exposure.

## Duplicate check

The checked T08 FIX packet studies changing protected subspaces, adaptive-step projection and moment transport under tool-contract updates. C095 reuses some optimizer mathematics but changes the task to unconstrained domain-reuse loss. T02 also includes standard optimizer and history-conditioned search. These are important neighboring mechanisms, yet neither checked packet establishes an exact duplicate of the proposed coordinate artifact. The source's W09 comparison is unverified; the referenced candidate file was outside this review's inspected material. No duplicate id is recorded.

## Verdict, required fixes and cheapest decisive check

**CUT** the current proposal because no specified residual distinguishes it from direct application of published coordinate-adaptive optimization. A new version would need an authentic stalled learner, a concrete observable curvature/reuse interaction, exact resource semantics and a reference whose advantage remains after SOAP, structured Shampoo, Muon/AdamW and state-reset controls. Banning these methods would invalidate rather than rescue the task.

Cheapest decisive check is CPU mathematical mapping: express the proposed transform and moment recurrence, then test whether it is already a legal SOAP/structured-preconditioning configuration under the intended state cap. **ESTIMATED 0 H100-hours**. At present there is no proposed recurrence to distinguish, so this audit exposes the missing content before an unjustified training reservation. Once that gap exists, a real transition-learning pilot must be costed from actual parameter shapes, tokens and auxiliary decompositions rather than the card's unsupported allowance.

An eventual implementation needs R2 live attacks and executable tests for hidden predictor capacity, procedural parameter injection, forged loss receipts, skipped return domains and uncharged decompositions. Root-owned initial state, private evaluation text, bounded artifact parsing, trusted library paths, per-seed deadlines, deterministic positive equivalence fixtures and a portable offline lifecycle are still absent. Full delivery reconciliation must retain failed branches and all actual model/optimizer state. These are necessary integrity gates and do not weaken the lawful optimizer.

## Verdict record
id: C095
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.80 (0.53–0.95)
combined_recipe_attack: ESTIMATED 0.80 (0.53–0.95)
best_of_4: ESTIMATED 0.88
pass_at_4: ESTIMATED 0.95
single_run_max: ESTIMATED 0.93
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: instantiate stalled learner and resource law; SOAP and structured optimizer floor; concrete residual transport mechanism
main_kill_reason: published rotated adaptive optimization directly covers the proposed intervention
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
