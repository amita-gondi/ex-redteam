# C010: Train through delayed simulator corrections — independent adversarial review

**Verdict: FIX.** Retroactive contact supervision could create a meaningful retention problem, but the card only argues against fixed-window replay. A bounded redesign must distinguish forgotten information from information that a compact simulator checkpoint, diverse coreset, or fresh corrected training can recover.

Source file: `/workspace/task_ideation_v4_creative/cards/C010.md`.

This is a CPU desk assessment. Reward forecasts below are ESTIMATED scenarios conditional on a sensible midrange reference, not fitted scores; the reward equation and anchors do not exist in the card. No training, rollout, simulator execution, or live exploit was performed. The card supplies no runtime filenames: “chronology service,” “submitted buffer,” and “policy trainer” below refer to its described processes, not inspected implementations.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Regenerate rather than retain observations | Save legal simulator reset state, action sequence and RNG state; regenerate discarded sensor windows when a correction arrives; relabel and retrain. | ESTIMATED 0.78 | No: stored observations are mentioned, reconstruction state is not defined. | Count every persistent reconstruction byte and replay compute; test a checkpoint/action codec at the same total budget. | ESTIMATED 0.55–0.85 | Procedural regeneration remains lawful if the simulator exposes it. |
| Hedge delay with multiscale diverse replay | Retain event boundaries and rare-contact representatives, reserve a reservoir for old trajectories, and choose variable burn-in lengths after correction. | ESTIMATED 0.64–0.84 | The criticism concerns FIFO and uniform relabeling, not this combined retention policy. | Strong diversity-plus-priority baseline with growing windows; demonstrate a residual benefit from dependency information. | ESTIMATED 0.54–0.81 | A heavy-tailed retention schedule can cover long delays cheaply. |
| Discard corrupted supervision and relearn | Learn control from physical transitions and terminal success; downweight provisional contact labels, then spend later updates on corrected examples or newly sampled geometry. | ESTIMATED 0.58–0.83 | No causal necessity for contact labels is established. | Contact-free and late-training controls with identical interaction/update allowances and geometry coverage. | ESTIMATED 0.50–0.80 | Contact prediction may be an unnecessary auxiliary objective. |
| Filesystem/mount/proc/IPC/frozen-asset access | Inspect chronology-service descriptors, mounts and shared-memory handles for pending corrections; try altering the initial policy or simulator contact table. | ESTIMATED 0.95–1.00 | Chronological delivery is required, but isolation is unspecified. | Keep future correction truth outside the solver namespace; root-owned service, immutable initial state, safe buffer snapshot and live access probes. | ESTIMATED 0.00 | A service RPC returning future state can bypass file permissions. |
| Interface or encoded-state smuggling | Pack old observations into trainer constants, optimizer state, recurrent caches or compressed buffer metadata while reporting a small submitted buffer. | ESTIMATED 0.85–1.00 | Counting replay bytes does not enumerate all retention channels. | Canonical accounting of source, caches, tensors and reconstructible state; trusted update authority and bounded decoded-input tests. | ESTIMATED 0.00 | Learned policy information is legitimate; distinguish it from an undeclared replay store. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Return fabricated completion receipts, skip expensive corrected retraining, or identify successful simulator fixtures from visible trajectory hashes. | ESTIMATED 1.00 | Determinism does not authenticate execution. | Parent drives new episodes and computes terminal truth; require independent equivalent positives and reject missing trainer work. | ESTIMATED 0.00 | Shared fixture ancestry could make an apparently independent bank recognizable. |
| Timing/check-decoupling/branch laundering | Train a future-corrected branch before its committed arrival, validate a chronological branch and swap in the former, or carry a detached learner across resets. | ESTIMATED 0.90–1.00 | The chronology requirement addresses intent, not lineage binding. | Service timestamps every read/update, snapshots the exact final policy, charges branches and terminates descendants between attempts. | ESTIMATED 0.00 | Host arrival time and logical simulator time need one authoritative ordering. |
| Dev-hidden leakage/cue inference | Infer contact revision type from delay bucket, trajectory identifier, geometry export order or correction-message length instead of revisiting evidence. | ESTIMATED 0.70–0.96 | Shared delay/storage distributions are useful but do not remove joint cues. | Cross delay, cause and encoding; private geometry-family splits and metadata-only correction predictors. | ESTIMATED 0.15–0.45 | A legitimate observable warning can make retention allocation easy. |
| Adaptive aggregate oracle | Submit buffer variants differing in one geometry class, difference completion/storage aggregates, and tune retention toward the reused evaluation bank. | ESTIMATED 0.65–0.90 | No feedback quota, precision or bank-reset rule is given. | Root-global query budget; protected dev gold, independent final geometries and full-cap adaptive retention baseline. | ESTIMATED 0.40–0.70 | Lawful tuning may generalize; rounded feedback alone does not guarantee privacy. |
| Slice abandonment/denominator optimization | Keep recent easy grasps, omit episodes needing distant corrections, or report only completed training phases to improve completion per byte. | ESTIMATED 0.60–0.88 | Completion is named without weighting, penalty or denominator rules. | Fixed offered episodes; correction-distance/cause strata, local failures and smooth retention-sensitive deficits; run recent-only specialist. | ESTIMATED 0.25–0.58 | A storage penalty can still make abandonment rational under honest accounting. |
| Strongest lawful combined recipe | Jointly tune prioritized relabeling, gradient/diversity coresets, multiscale recurrent replay, uncertainty-based retention, compression and permitted regeneration; compare to delayed-label-agnostic control training. | ESTIMATED 0.67 (ESTIMATED 0.47–0.87) | No: none of these methods is excluded by the scientific contract. | Execute this whole policy against dependency-aware retention at matched bytes, interactions and useful compute. | ESTIMATED 0.67 (ESTIMATED 0.47–0.87) | Security changes leave this algorithmic challenge intact. |

## Published recipe shortcut — web checked

- [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952) establishes selective reuse of important transitions; it supports a serious relabel-and-reprioritize baseline, not correction propagation by itself.
- [Hindsight Experience Replay](https://arxiv.org/abs/1707.01495) demonstrates off-policy relabeling for robot manipulation. Its changed-goal setting differs from revised contact truth, so compatibility requires explicit testing.
- [GCR: Gradient Coreset Based Replay Buffer Selection For Continual Learning](https://arxiv.org/abs/2111.11210) selects small memories to approximate historical gradients; it challenges the assumption that retaining a fixed local window is the strongest ordinary option.

Verification reached primary abstract pages opened during this session. I did not inspect executable ports or paper appendices, and no cited result measures this task. Variable-window retention and checkpoint reconstruction are adversary-designed engineering additions, not claims made by these papers. The strongest compatible search over those options is ESTIMATED 0.67, with ESTIMATED scenario range 0.47–0.87. These alternatives should compete when their objectives conflict; adding every loss indiscriminately would weaken the attack.

## Saturation against the hypothetical 10T researcher / 12h

The researcher can read the simulator interface, calculate storage economics and construct a retention codec before spending its training allocation. A surprising correction delay is not necessarily hard: an exponentially spaced history, a rare-event reservoir or replay from actions can cover much more history than a fixed burn-in window. Conversely, if old pixels contain genuinely unpredictable task-relevant information, then retaining them has a real opportunity cost. That is the promising mechanism, provided legal observations before deletion contain evidence useful for deciding what to save.

My full-budget tail scenario is single-run maximum ESTIMATED 0.82, oracle best-of-4 mean ESTIMATED 0.74, pass@4 ESTIMATED 0.84 at the binding success threshold R>=0.60, and stronger-tier/extra-compute upper-95% projection ESTIMATED 0.93. These forecasts exceed respectively the binding >0.70, >0.60, >0.50 and >=0.75 kill lines. “Upper-95%” here is an ESTIMATED conservative planning endpoint, not a fitted confidence bound. The forecasts assume moderately correlated attempts over retention architectures; they are not derived by pretending attempts are independent Bernoulli draws.

S1 is OPEN: neither executable reference nor stronger same-budget control demonstrates the required reference band and reserve. S7 is OPEN because an achievable constrained ceiling has not been bracketed; a low storage-limited ceiling would tighten the test, not establish resistance. Rollout scores, observed runs, observed pass@k and grader noise are UNMEASURED. Planned measurement: fresh geometry/correction blocks, independently restarted full-budget recipe searches, repeated grading of frozen policies, and separate oracle versus legal-dev selection. Budget sweeps must distinguish researcher reasoning from simulator interaction and subject updates. Present-model early stopping supplies no protection.

The FIX judgement concerns a narrower, testable retention mechanism, not confidence that these forecasts will fall after implementation. If diverse replay or regeneration matches the reference, retire this version. Making correction causes unknowable until after irreversible deletion would manufacture an information deficit rather than research depth.

## Revised estimate versus the source card

The card gives source ESTIMATED 0.44 for prioritized relabeling plus recurrent burn-in. I raise the lawful composite to ESTIMATED 0.67 because the adversary can select nonlocal evidence before deletion, vary its window length, and question the need to use provisional contact labels at all. The card's observation that a correction can reach beyond a fixed window does not establish that necessary history is expensive to summarize or regenerate. My greater concern is lawful algorithmic coverage; a stolen future correction has a separate conditional exploit payout and is excluded from the combined estimate.

## Boilerplate and missing build content

ESTIMATED generic framing fraction: 0.20–0.35; ESTIMATED task-specific fraction: 0.65–0.80. This is a compact idea with distinctive timing/storage semantics, not mostly boilerplate. It is nevertheless insufficient to build faithfully. Missing are contact revision semantics, whether corrections change rewards or just auxiliary labels, robot/observation specification, reset/replay access, total interaction and update budgets, initial checkpoints, retention ledger, arrival-time API, score equation, episode weights, reference algorithm and legal stronger control. The claimed unseen-geometry test also needs a defensible train/dev/final geometry split and transfer-sensitive terminal predicates.

## Duplicate check

The checked FIX packet T13 concerns passive-video grounding and bridge-supported action learning. C010 instead changes supervision after learning and meters historical evidence, so I do not find a near-duplicate of that checked mechanism. T08's checked contract-change problem shares continual adaptation, but its changed obligations and fixed replay differ from retroactive contact correction. No broad catalog or D-card search was performed; the structural exemplars were used only for format. Duplicate status is therefore limited to these actual comparisons.

## Verdict, required fixes and cheapest decisive check

FIX, with required changes:

1. Define the complete legal retention/reconstruction boundary and chronological state machine, including reset seeds, model caches and persistent non-buffer objects.
2. Construct identifiable correction families where selecting sufficient old evidence competes for storage; demonstrate gain beyond contact-free relearning and competent multiscale/cohort replay.
3. Freeze native completion and storage units, fixed strata, smooth penalties, independent calibration anchors and a stronger feasible control before reward normalization.
4. Deliver portable privilege separation, network-none execution, trusted results, per-seed deadlines and negative exploit controls. Test chronology, encoded stores, fake receipts, descriptor access and checkpoint swaps through the real loader. Match warmup shapes and library paths; retain failures and prune nonselected checkpoints. Require protected representative dev content, independent all-positive fixtures, decontamination and exact-archive reconciliation.

The cheapest immediate check is a CPU dependency/reconstruction audit: can a legal reset snapshot and action log reproduce discarded observations under each correction law? Its cost is ESTIMATED 0 H100-hours. Passing that audit warrants a later paired learning pilot, proposed at ESTIMATED 18 H100-hours for competing retention policies and correction-free controls on the same compact robot learner. This differs from the card's source ESTIMATED 14 GPU-h because regeneration and label-agnostic controls add actual training work; subject size and simulator throughput must be pinned before that contingent budget is credible. Nothing was launched. The CPU test can reject the claimed storage mechanism but cannot certify saturation resistance.

## Verdict record

id: C010
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.67 (ESTIMATED 0.47–0.87)
combined_recipe_attack: ESTIMATED 0.67 (ESTIMATED 0.47–0.87)
best_of_4: ESTIMATED 0.74
pass_at_4: ESTIMATED 0.84
single_run_max: ESTIMATED 0.82
upper95_projected: ESTIMATED 0.93
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: account reconstructible memory; identifiable correction dependencies; combined replay controls; frozen native reward; chronological isolated trainer
main_kill_reason: diverse replay and reconstruction may remove retention research
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
