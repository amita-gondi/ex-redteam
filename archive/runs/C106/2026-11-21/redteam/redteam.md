# C106: Improve a world model by limiting its planner's evidence access — independent adversarial review

**Verdict: FIX.** Planner-induced distribution shift is real, but pessimistic modeling, short-horizon replanning and targeted real-data collection already address the disclosed failure. A credible residual could arise where useful long-horizon evidence and shared model error cannot be separated by those controls. The card supplies no dynamics family or observation contract establishing that residual, so its low attack estimate is premature.

Source: `/workspace/task_ideation_v4_creative/cards/C106.md`.

This review ran no simulator, policy, training or live boundary probe. All numerical payouts are ESTIMATED conditional judgments rather than calibrated rewards. The card names a world model, planner evidence interface, independent simulator and learning ledger, but supplies no executable paths for them; references below name those objects without inventing delivered files.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
| Short-horizon conservative MPC | Fit probabilistic dynamics from authorized real transitions; plan with uncertainty penalties and support constraints, execute only the first action and replan from fresh observations. | ESTIMATED 0.57–0.85 | No; this is a lawful evidence-limiting controller. | Give a fully tuned conservative replanning baseline equal data and total planning work; certify tasks requiring more than reactive correction. | ESTIMATED 0.57–0.85 | Short horizons can remove exploitation while preserving sufficient completion. |
| Discard the learned-model bottleneck | Train a model-free or imitation policy on permitted real trajectories; use the world model only for diagnostics or a fallback, if this is within the submitted artifact contract. | ESTIMATED 0.46–0.83 | Nothing states that successful model-free control is invalid. | Define deployment authority and compare the direct policy at equal real-data and training cost; preserve lawful alternatives. | ESTIMATED 0.46–0.83 | Requiring an idle model module would not create scientific necessity. |
| Learn the exploitable region directly | Cluster model residuals by state-action support, collect real counterexamples near the planner's selected trajectories and add a learned failure classifier or robust action shield. | ESTIMATED 0.54–0.88 | The suggested ensemble floor omits some direct residual-learning capacity. | Compare shared-error detection with a flexible residual/support predictor trained on the same corrective real batch. | ESTIMATED 0.54–0.88 | Shared ensemble bias is not automatically shared bias of an independently trained residual monitor. |
| Filesystem/mount/proc/IPC/frozen-asset access | Reach independent-simulator dynamics parameters, observation-alias truth or terminal predicates through mounts, descriptors and shared simulator IPC; alter frozen transition or success code. | ESTIMATED 0.94–1.00 | Independent success authority is stated, but process and mount separation are not. | Isolate simulator state from planner workers; typed observation broker, immutable renderer/dynamics and no inherited privileged handles. | ESTIMATED 0.00 | A simulator API may reveal state indirectly through diagnostics or debug exceptions. |
| Interface or encoded-state smuggling | Embed private dynamics tables, a pre-trained controller or uncharged trajectory data inside the evidence interface's arrays, serialized uncertainty objects or helper code. | ESTIMATED 0.84–1.00 | No interface grammar, checkpoint ingress or payload contract is defined. | Authenticate permitted learned state and charged training; bound all decoded artifacts; allow only legal observation-derived interface outputs. | ESTIMATED 0.00 | A compact hand-coded lawful controller must remain admissible if the contract permits it. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Return imagined terminal success as a real episode result, forge a completion receipt, crash hard episodes, or identify stock simulator conformance trajectories by bytes. | ESTIMATED 0.81–1.00 | Simulator-only success and real/imagined distinction oppose this, by prose only. | Trusted parent obtains real terminal receipts directly; independent behaviorally equivalent positive cases; no default success for nonexecution. | ESTIMATED 0.00 | A simulated episode can be real for grading yet accidentally use candidate-controlled success metadata. |
| Timing/check-decoupling/branch laundering | Hide simulator queries as uncharged model calibration, label real data as imagined for cost accounting, or select the best corrective batch while dropping failed exploration branches. | ESTIMATED 0.74–0.97 | Complete rollout cost and a ledger are requested without ownership rules. | Broker-owned real/imagined receipts, all-ancestor work accounting, immutable selected planner/model pair and synchronized teardown. | ESTIMATED 0.00 | Batched model evaluations and cached simulator trajectories complicate amortization. |
| Dev-hidden leakage/cue inference | Infer fresh dynamics or alias class from reset order, scene identifier, object serialization or simulator initialization latency, then dispatch a known controller. | ESTIMATED 0.62–0.92 | Freshness and comparable access do not address label-correlated packaging. | Cross reset metadata and nuisance assets with dynamics; whole-family splits; metadata-only controller and same-observation alias controls. | ESTIMATED 0.19–0.48 | Observation-identifiable dynamics should be inferable legally; secrecy cannot be the intended obstacle. |
| Adaptive aggregate oracle | Query completion for increasingly selective gates or planner penalties, infer which failure family dominates, and tune to protected development rather than learning useful dynamics. | ESTIMATED 0.56–0.87 | No cap or precision policy is supplied for development simulator feedback. | Charge all real interactions and aggregate queries globally; untouched final dynamics; baseline full-budget adaptive tuning. | ESTIMATED 0.50–0.80 | Cheap development resets may make family search an effective valid method. |
| Slice abandonment/denominator optimization | Avoid contact-rich or aliased episodes, terminate conservatively and excel on easy motion tasks; exclude failures from reported completion or rollout cost averages. | ESTIMATED 0.50–0.89 | Completion is the correct target, but episode indexing and coverage floors are missing. | Fixed episode/dynamics strata, local timeouts as failures, per-family completion floors and explicit no-op/safe-stop controls. | ESTIMATED 0.20–0.59 | Overconservatism can still maximize a poorly weighted completion/cost tradeoff. |
| Strongest lawful combined recipe | Combine probabilistic ensemble MPC, support and residual-based gating, short adaptive horizons, targeted real counterexamples and direct-policy fallback; jointly tune to real completion per full cost. | ESTIMATED 0.65 (ESTIMATED 0.40–0.90) | The written defenses regulate truth and cost, not this valid controller. | Show an observable long-horizon/shared-error interaction surviving the entire conservative-control stack. | ESTIMATED 0.65 (ESTIMATED 0.40–0.90) | The ordinary stack may already perform every useful function of the proposed redesign. |

## Published recipe shortcut — web checked

- [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://arxiv.org/abs/1805.12114): the primary abstract describes PETS, combining probabilistic ensembles with trajectory sampling for uncertainty-aware control.
- [MOPO: Model-based Offline Policy Optimization](https://arxiv.org/abs/2005.13239): the returned primary result establishes a model-based offline policy-optimization baseline relevant to controlling distribution-shift exploitation.
- [MOReL: Model-Based Offline Reinforcement Learning](https://arxiv.org/abs/2005.05951): the primary abstract explicitly constructs a pessimistic decision process from offline data, making evidence restriction an established algorithmic direction.

Verification was limited to primary abstracts and search-returned paper descriptions. These are not reproduced implementations, and offline guarantees do not directly transfer to the card's active-data, partially observed robot setting. The combined attack joins compatible control ideas while allowing independent model-free and residual-monitor alternatives rather than pretending every paper is a single plug-in. Strongest composite reward remains ESTIMATED 0.65 (ESTIMATED 0.40–0.90).

## Saturation against the hypothetical 10T researcher / 12h

The prompt fixes the controller's comparisons at single-run R>0.70, oracle best-of-four mean >0.60, pass@4 >0.50 at R≥0.60, and projected upper-95% ≥0.75. These constants are acceptance requirements rather than estimated rewards. S1 asks for reference [0.50,0.65], a same-envelope control ≥reference+0.20 and attainable ≥0.75. S7 also tests Q=(R−r_floor)/(C_L−r_floor) against the absolute gate values, with uncertainty in the legal ceiling retained.

The important question is whether the solver must retain uncertain evidence to complete a task, rather than merely gate unsupported trajectories. A fully observed stabilization or short manipulation benchmark would likely be solved by ordinary replanning. Conversely, aliasing that makes successful actions indistinguishable from failure under all legal histories is an observability defect, not a research challenge. The missing middle is an identifiable history-dependent planning problem with useful information that cannot be discarded cheaply.

The target researcher can replace the evidence representation and the planner jointly, fit residual predictors, and allocate all permitted real queries efficiently. Its persistence is assumed. Current reports of under-used budgets, limited verification and weak novel research do not justify discounting published conservative-control machinery. The allowed calibration packets likewise caution that complete recipes can approach a reference without following the author's decomposition.

Desk tail forecasts are single-run maximum ESTIMATED 0.87, oracle best-of-four mean ESTIMATED 0.76, pass@4 ESTIMATED 0.83, and stronger-tier/expanded-compute upper-95% scenario ESTIMATED 0.97. Each is above its corresponding binding bar boundary; likely breach labels are single, bo4, pass4 and upper95. The projected figure is a risk envelope awaiting a fitted interval, not an empirically calculated upper bound. Different planner restarts share task difficulty, so the pass estimate is not computed by asserting independent repeated successes.

S1 remains unresolved until the same deployment envelope supports a midrange reference and demonstrably stronger controller. S7 is also OPEN: the legal achievable ceiling cannot be inferred from a state-oracle planner or unlimited real simulator access. All rollout rewards, observed runs, grading variability and observed pass@k are UNMEASURED. Measure native completion, real query use, imagined work and catastrophe frequency on fresh dynamics blocks; replay identical policies for grader variance and execute independent full-budget researcher attempts only in a later authorized study. Separate subject-training, serial planning and researcher inference in budget sweeps.

## Revised estimate versus the source card

The source's ESTIMATED 0.36 accounts for ensembles, support-aware planning and targeted data, then invokes shared abstractions as an obstacle. My ESTIMATED 0.65 (ESTIMATED 0.40–0.90) is higher because shared bias can be countered by independently learned residual classifiers, direct observations and shorter planning horizons. None requires recognizing the designer's particular abstraction error. The card offers no executed counterexample showing that these additions lose needed task information.

## Boilerplate and missing build content

ESTIMATED 25–40% is reusable framing or compliance text. For construction it is mostly boilerplate: there is no robot embodiment, simulator/version, sensor model, dynamics distribution, real-query tariff, model architecture, evidence schema, action latency, reward mapping or reference controller. “Actual uncertainty limits” is not a formal interface property without defining what the planner sees and can reconstruct.

The independent simulator must check true closed-loop outcomes while the learning ledger records provenance of every transition. It cannot rely on a label supplied by the model. The task also needs a natural inherited failure trace and rights-cleared training assets; merely tagging it with an accepted pretraining shape does not demonstrate that world-model learning dominates integration work.

## Duplicate check

The inspected T13 calibration material uses supported closed-loop recovery and model-based/direct-controller bypasses, but its core is grounding passive video into actions. That is related control machinery rather than an established duplicate of planner evidence restriction. C112 in the assigned set also changes an intermediate representation to influence data acquisition; its sensor uncertainty problem is different. The source's unavailable W10 neighbor was not inspected and is unverified; no D or other creative neighbor is asserted.

## Verdict, required fixes and cheapest decisive check

Retain FIX only with these bounded requirements:

1. Commit a dynamics/alias family with a legal successful history-dependent controller and explicit observability evidence.
2. Define evidence authority, action and rollout costs, fixed completion denominators and a native ceiling under identical real-data limits.
3. Compare evidence redesign against fully tuned conservative MPC, direct-policy replacement and residual-guided real collection. Keep all successful legal alternatives eligible.
4. Build broker-owned provenance, separate terminal authority, immutable state capture, decoded-state checks and independent healthy positive controls. The later delivery must pass live cheat sessions, portable startup/library tests, actual-shape warmup, bounded retries, decontamination and bundle reconciliation.

Begin with CPU analysis of whether the proposed aliases admit different required actions under identical legal histories, with ESTIMATED 0 H100-hours. For an observable candidate, the cheapest decisive learned-dynamics comparison is ESTIMATED 14 H100-hours: ESTIMATED three controller/data-collection arms across ESTIMATED two seeds at ESTIMATED two device-hours, plus ESTIMATED two device-hours for independent rollout scoring; simulator CPU work is additional but uses no accelerator. This is a small-model kill screen, not the card's unprofiled robotics-scale training claim. The uncertainty mechanism, not an arbitrary restriction on MPC, must explain any surviving gap.

## Verdict record

id: C106
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.65 (0.40–0.90)
combined_recipe_attack: ESTIMATED 0.65 (0.40–0.90)
best_of_4: ESTIMATED 0.76
pass_at_4: ESTIMATED 0.83
single_run_max: ESTIMATED 0.87
upper95_projected: ESTIMATED 0.97
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 14
required_fixes: observable dynamics family; real-cost evidence ABI; complete conservative/direct control comparison; trusted simulator ledger
main_kill_reason: ordinary conservative control may remove all planner exploitation
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
