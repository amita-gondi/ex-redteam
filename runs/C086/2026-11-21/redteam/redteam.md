# C086: Research world models graded only by executed improvements — independent adversarial review

**Verdict: CUT.** The proposed catch is ordinary model-based optimization under surrogate error, and the card itself permits an execution-grounded optimizer to bypass proposal training. A learned proposer can imitate that optimizer while satisfying the weights artifact requirement. No concrete project distribution establishes transferable scientific behavior beyond competent uncertainty-aware search and full-cost validation.

Source file: `/workspace/task_ideation_v4_creative/cards/C086.md`.

This is a review of a proposal rather than a delivered agent. Reward and cost values are ESTIMATED assumptions. Rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; measuring them requires frozen project families, training budgets and reset semantics. Neither a surrogate nor a downstream training run was executed. Proposed receipt and test names below describe missing build work.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Ignore the research surrogate | Allocate true short runs using successive halving and a model-based sampler; promote promising candidates and select on actual validation gains rather than predicted scores. | ESTIMATED 0.64–0.89 | The source explicitly acknowledges this lawful bypass. | Include direct-execution search with its saved surrogate-training budget reallocated to experiments. | ESTIMATED 0.64–0.89 | The task may have no reason to train a research world model at all. |
| Generic optimism repair | Fit ensembles to true receipts, sample disagreement and random exploration regions, and impose conservative acquisition outside observed proposal support. | ESTIMATED 0.60–0.87 | No; the source names most of these ingredients without establishing their ceiling. | Jointly tune acquisition, refresh allocation and exploration under the complete budget, then compare with the proposed strategy. | ESTIMATED 0.60–0.87 | Shared model misspecification is possible but not a demonstrated residual research mechanism. |
| Distill search into the mandatory proposer | Generate legal successful search trajectories on training projects and fine-tune the proposal policy to emit their standard optimizer/data recipes; keep a generic search controller at reset. | ESTIMATED 0.65–0.91 | Training the proposal agent does not require that its behavior be scientifically novel. | Compare a distilled generic optimizer with the reference at matched training and deployment cost; no provenance-based rejection of successful legal recipes. | ESTIMATED 0.65–0.91 | If projects share ordinary hyperparameter sensitivities, distillation transfers broadly. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read hidden project validation text from trainer descriptors or surrogate caches; alter initial subject checkpoints, true-execution runner or trusted receipt store. | ESTIMATED 0.90–1.00 | Separate prediction/receipt channels are requested but their processes are unspecified. | Root-owned execution service outside proposer namespace; immutable project assets and opaque job handles; proposed `test_project_truth_and_receipts` probes mount, proc and IPC paths. | ESTIMATED 0.00 | A helper allowed to launch arbitrary experiments may accidentally inherit evaluator authority. |
| Interface or encoded-state smuggling | Put private project solutions or externally trained proposal deltas into refresh configuration, proposal text attachments or numeric surrogate features; load them at reset. | ESTIMATED 0.83–1.00 | No distinction between authorized proposer weights and arbitrary auxiliary state is defined. | Authenticate learned-state lineage and account every persistent byte; bound auxiliary payloads and prevent proposal code from loading substitute subject states. | ESTIMATED 0.00 | A legal algorithm encoded in weights is the intended artifact; size scans cannot distinguish knowledge from illicit provenance. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Label a surrogate prediction as a completed experiment, reuse another proposal's receipt, skip a failed run, or recognize canonical healthy projects by manifest hashes. | ESTIMATED 0.88–1.00 | Typed prediction versus execution channels directly address the first route, by specification only. | Parent authenticates job/config/state lineage and recomputes gains; independent equivalent project positives and failed-run fixtures must all traverse real execution. | ESTIMATED 0.00 | Correctly typed receipts can still describe the wrong experiment unless provenance is bound. |
| Timing/check-decoupling/branch laundering | Spend free research before reset, keep optimizer or model caches across projects, hide losing trials, or execute a different proposal after selecting a cheap validated one. | ESTIMATED 0.77–1.00 | Comprehensive charging is promised without reset or ancestry implementation. | Charge proposal generation, all surrogate fits and true runs; cold-reset all state; freeze selected recipe and link every ancestor to the same ledger. | ESTIMATED 0.00 | “Reset” may leave useful nonweight memory or remote worker state that changes the scientific estimand. |
| Dev-hidden leakage/cue inference | Recognize model-family names, inherited project logs or architecture filenames and emit the corresponding public recipe; memorize repeated project mechanisms. | ESTIMATED 0.61–0.90 | Fresh architecture/data mechanisms are stated but not independently authored. | Whole-project provenance splits, anonymized nuisance metadata and crossed task families; compare source-recognition-only and generic-recipe proposers. | ESTIMATED 0.28–0.61 | Reading legitimate architecture code is permitted; a universal optimizer remains a lawful win. |
| Adaptive aggregate oracle | Use final-gain dev calls as extra true validation, difference proposal bundles to isolate profitable mechanisms and share query quotas across proposer training branches. | ESTIMATED 0.60–0.88 | Real-execution dev parity could create a powerful additional experiment channel. | Put dev and true training services under one metered episode account; predeclare precision, refresh and selection rules; hold out fresh projects for adaptive winners. | ESTIMATED 0.35–0.69 | A lawful extra evaluation is still valuable; quota closure does not reduce all adaptive search gains. |
| Slice abandonment/denominator optimization | Propose only low-cost optimizer changes on easy families, time out architecture edits and report gain only over projects with completed true validations. | ESTIMATED 0.63–0.92 | No reset-project denominator or minimum coverage is described. | Commit all project slots and cost; preserve unsuccessful changes and no-op outcomes; macro report data, architecture and optimization families. | ESTIMATED 0.24–0.57 | A strong common-family specialist may remain optimal under the eventual weights. |
| Strongest lawful combined recipe | Combine trained proposal priors with Bayesian/multi-fidelity true-run search, ensemble uncertainty, explicit exploratory refresh and conservative acquisition; compare direct search and use all legal dev selection. | ESTIMATED 0.78 (ESTIMATED 0.51–0.94) | Every ingredient fits the stated research loop. | Run this full controller, including a no-surrogate arm, before attributing transfer to a new refresh strategy. | ESTIMATED 0.78 (ESTIMATED 0.51–0.94) | The intended chain can collapse into a standard budgeted optimization controller. |

## Published recipe shortcut — web checked

- [Language Models Learn to Improve Language Models](https://arxiv.org/abs/2610.23344): the primary paper page was opened to verify the cited proposal-learning work exists; detailed implementation and transfer claims were not independently reproduced.
- [Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization](https://arxiv.org/abs/1603.06560): primary search material establishes a standard resource-allocation route over real partial evaluations.
- [BOHB: Robust and Efficient Hyperparameter Optimization at Scale](https://proceedings.mlr.press/v80/falkner18a.html): the primary proceedings abstract directly combines model-based configuration selection with budget allocation.
- [Scalable Global Optimization via Local Bayesian Optimization](https://arxiv.org/abs/1910.01739): the primary abstract supplies local-model trust-region search as another way to manage unreliable global surrogates.

These are mechanism-level checks from a primary page or primary search excerpts. I did not inspect LM2LM training code, assert that continuous BO directly optimizes arbitrary patches, or import any paper's reported score. Structured legal recipe choices can be searched directly; free-form code proposals need an explicit candidate representation and executable validation. The adversarial combination is a controller over compatible alternatives, with **ESTIMATED reward 0.78 (ESTIMATED 0.51–0.94)**.

Exploratory true evaluations are not a new defense unavailable to standard optimization. A competent baseline should challenge optimistic regions deliberately and abandon a bad surrogate when true experiments are cheaper. Its policy training cost must be counted, but the reference bears equivalent proposal-learning and refresh costs. Forcing the baseline to retain a demonstrably harmful world model would manufacture the intended advantage.

## Saturation against the hypothetical 10T researcher / 12h

Assume the stronger researcher can synthesize valid experiments, preserve all logs and run a practical search controller without waiting for a complete causal explanation of every gain. The card provides no project where that shortcut is insufficient. Fresh model names or architecture implementations might alter response surfaces, but Bayesian exploration and true-run selection are designed to cope with unknown surfaces.

Working forecasts are **ESTIMATED single-run maximum 0.91 versus >0.70**, **ESTIMATED oracle best-of-4 mean 0.86 versus >0.60**, **ESTIMATED pass@4 0.94 versus >0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.99 versus ≥0.75**. These likely breach the respective supplied lines. No sample law, scaling fit or empirical confidence interval underlies those planning values. A much lower outcome remains in the recipe range if true runs are extremely expensive or the learned transfer problem is substantially richer than ordinary recipe search.

S1 is OPEN because there are no native gains for a reference, stronger control or useful reserve. S7 is OPEN because no same-budget achievable ceiling is bracketed. A true-run cap that makes every method ineffective is not evidence of resistance; a learned proposer needs legal training evidence sufficient to generalize within the same cap. The correct denominator is actual achievable downstream improvement, not predicted surrogate gain or theoretical perfect training loss.

Observed repeated-search and grade-noise measurements remain UNMEASURED. Plan independent fresh-project restarts across research budgets, separate proposer-training work from researcher inference and subject-model experiments, and measure both legal dev selection and retrospective best-of-four. Conditional stronger-tier projections must carry family-transfer and anchor uncertainty; unresolved intervals stay HOLD. The supplied weakness reports' failures to iterate or verify cannot be used as hardness, especially for a task whose baseline is automated iteration.

## Revised estimate versus the source card

The source's **ESTIMATED 0.39** already includes ensembles, Bayesian acquisition and low-confidence true runs. My **ESTIMATED 0.78 (ESTIMATED 0.51–0.94)** disagrees because it completes that recipe with multi-fidelity allocation, model distrust, direct-search fallback and legal distillation into the required artifact. There is no specified reason this controller must repeatedly lose to the author method on real project gains.

Policy-induced shared blind spots are a hypothesis, not a measured replication result; the card appropriately says so. They could motivate future research, but they do not justify assigning the full conventional optimizer a low score. Security fixes can stop a forecast masquerading as execution, yet cannot lower the gain of actual validated conventional proposals. The calibration packets support precisely that separation without providing a numerical prior for this card.

## Boilerplate and missing build content

The source contains **ESTIMATED 35–45%** generic agentic optimization language and **ESTIMATED 55–65%** content specific to proposal learning and surrogate refresh. It is not mostly boilerplate by that editorial fraction, but it omits nearly every implementation choice affecting feasibility. Missing items include inherited project assets, actual edit grammar, proposer architecture and initialization, surrogate feature/state schema, true-run fidelity choices, uncertainty calibration and reset procedure.

The reward also lacks a definition of “training gains,” reference endpoints, per-project scaling, acceptance of regressions, actual serving/training costs and all-job denominators. The budget might be spent mainly training the proposer, mainly optimizing each new subject or mainly grading. Those are different tasks. A causal transfer study must compare trained versus untrained proposal priors while keeping online controller, execution opportunity and model capacity matched, including a generic optimizer with reliable memory. No such construction is in the card.

## Duplicate check

The checked T02 FIX packet already includes model-assisted multi-fidelity recipe search, although its deployed artifact is a continuation method rather than a proposal agent. C086 therefore overlaps its baseline machinery, not necessarily its scientific endpoint. The source's comparison to T03 remains unverified because that packet was not opened. No checked D card matches the learned proposal/refresh artifact, and no duplicate id is established from the limited inspected scope.

## Verdict, required fixes and cheapest decisive check

**CUT** this open-ended research-surrogate proposal until it names a project family with a demonstrated residual beyond ordinary execution-grounded optimization. This is larger than a grader correction: the principal scientific distribution and reference have yet to be designed. A future version may retain the idea if it demonstrates transferable proposal skill after matched-cost direct-search and distilled-search controls.

Cheapest decisive check is a CPU allocation/contract audit: enumerate the proposed legal recipe and fidelity interface, show whether a no-surrogate controller can spend all freed training/refresh budget on the same true tests, and determine what extra legal information proposal training adds at reset. **ESTIMATED 0 H100-hours**. This can expose an unnecessary learned artifact before costly training. It cannot provide measured transfer evidence, and no quantitative training pilot is defensible until actual subject sizes and run prices are fixed.

For an eventual package, R2 requires separate trust domains for predictions and actual job results, immutable starting models, encoded-state controls and live receipt-forgery/skip tests. Per-project timeouts, all-branch charging, independent healthy project controls, protected development data, environment-configurable legitimate services and local OCI startup must work in the delivered configuration. No keys may enter the solver, and final archive metrics must reconcile with complete failed-run records. These are unexecuted release requirements, not reasons to revise the lawful forecast downward.

## Verdict record
id: C086
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.78 (0.51–0.94)
combined_recipe_attack: ESTIMATED 0.78 (0.51–0.94)
best_of_4: ESTIMATED 0.86
pass_at_4: ESTIMATED 0.94
single_run_max: ESTIMATED 0.91
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: concrete residual beyond execution-grounded optimization; matched direct-search control; authenticated complete experiment ledger
main_kill_reason: standard optimizer can bypass or be distilled into the proposer
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 4
