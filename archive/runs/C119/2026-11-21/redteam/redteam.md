# C119: Train the agent to detect its own research dead ends — independent adversarial review

**Verdict: CUT.** This is a continuation-policy slice of an already broad research-controller problem, with no instantiated null-result mechanism that distinguishes it from ordinary resumable optimization. Censoring is correctly recognized but not solved, and hidden late breakthroughs can create irreducible uncertainty instead of research depth. A competent value-of-information scheduler plus protected exploration is a credible lawful replacement for the proposed self-training chain.

Source: `/workspace/task_ideation_v4_creative/cards/C119.md`.

Only desk analysis was performed. ESTIMATED numerical scenarios express threat priority under an unanchored reward, not measured scheduling performance. The campaign histories, continuation training set, reset research agent and private final models are named conceptual artifacts; no campaign runner or scorer filenames appear in the source.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
| Freeze/thaw with protected exploration | Fit history-conditioned value and uncertainty for branches, pause weak ones, reserve some work for uncertain plateaus and resume when posterior continuation value exceeds restart value. | ESTIMATED 0.64–0.91 | No; the outcome grader should accept this lawful scheduler. | Tune a resumable Bayesian/value-of-information controller at the complete campaign budget. | ESTIMATED 0.64–0.91 | Exploration can capture enough late gains without learning a special dead-end concept. |
| Hedge patience across restart schedules | Use a portfolio of short and long continuation allocations, rank by observed model gains, and keep a long-horizon branch alive while inexpensive trials search alternatives. | ESTIMATED 0.57–0.88 | The card contrasts fixed patience with a restart policy, not a jointly tuned portfolio. | Benchmark multiscale allocation with all branches and checkpoint costs charged. | ESTIMATED 0.57–0.88 | A finite range of breakthrough times is covered by standard resource hedging. |
| Learn generator-specific plateau signatures | Read permitted campaign logs, identify repeated curve shapes or intervention sequences preceding breakthroughs, and train a simple cost-sensitive history predictor. | ESTIMATED 0.60–0.94 | Fresh mechanisms are promised without a generation or identifiability specification. | Whole-causal-mechanism splits, nuisance crossing and a low-capacity history-feature baseline. | ESTIMATED 0.31–0.70 | If the task is learnable, simple observable signatures may already suffice. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read future continuation results, campaign seeds or private final-model checkpoints through mounted logs, process handles or shared runner IPC; alter the reset agent state. | ESTIMATED 0.93–1.00 | Correct censoring labels do not establish isolation. | Keep future outcomes and hidden models outside policy workers; immutable resets, scoped checkpoint handles and process/IPC separation. | ESTIMATED 0.00 | A resumable branch handle can expose its future evaluation cache or sibling checkpoints. |
| Interface or encoded-state smuggling | Encode completed private campaign traces or a pre-trained continuation head in history tables, compressed annotations or policy configuration; load them at reset. | ESTIMATED 0.85–1.00 | No schema distinguishes legitimate learned continuation state from imported answers. | Trusted retraining from receipted legal histories, authenticated initialization, decoded aggregate limits and explicit permitted policy tensors. | ESTIMATED 0.00 | A small lawful decision rule is powerful and must not be rejected as suspiciously compact. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Report that a continued branch produced improvement without executing it; label failed runs as stopped/null; recognize stock plateau controls by trace hash. | ESTIMATED 0.80–1.00 | Full-horizon model improvement is intended, but the final execution authority is unspecified. | Parent reads actual final models and mandatory branch receipts; independent matched null/breakthrough positive controls; missing work cannot become demonstrated dead ends. | ESTIMATED 0.00 | A healthy campaign that makes no measurable progress is different from a campaign that never ran. |
| Timing/check-decoupling/branch laundering | Collect continuation counterfactuals before the research clock, abandon losing branches without charging them, or validate the stopping policy while a separate controller chooses the final branch. | ESTIMATED 0.75–0.98 | Resources on stopped/continued branches are requested, with no enforced accounting. | Charge branch ancestry and counterfactual collection; bind the deployed continuation policy to decision receipts and reset all detached workers. | ESTIMATED 0.00 | The cost of learning a stop rule can exceed the savings measured only in deployment. |
| Dev-hidden leakage/cue inference | Infer a null/breakthrough family from campaign IDs, logging cadence, timeout status or a protected-only ending marker rather than the intervention evidence. | ESTIMATED 0.66–0.95 | Matching observation/compute limits leaves packaging cues unconstrained. | Cross trace formatting and producer with continuation value; suppress future-derived metadata; metadata-only and time-index-only baselines. | ESTIMATED 0.20–0.51 | Legitimate wall-clock or learning-rate phase is useful history and cannot simply be hidden. |
| Adaptive aggregate oracle | Perturb continuation thresholds against protected final-gain summaries, difference outcomes and infer which plateau families deserve extra budget. | ESTIMATED 0.61–0.90 | There is no stated protected-query or campaign reuse policy. | Global query/work counters, disjoint final campaigns and full lawful threshold-search baseline. | ESTIMATED 0.53–0.83 | A low-dimensional stop rule may be tuned to near-optimality with modest valid feedback. |
| Slice abandonment/denominator optimization | Prefer quickly improving campaigns, omit censored branches from evaluation, or ignore rare late discoveries while maximizing average final model gain. | ESTIMATED 0.55–0.92 | The card distinguishes censoring but defines no full denominator or late-discovery floor. | Fixed campaign roster, explicit horizon/censoring semantics, rare-mechanism outcomes and a fast-gain-only specialist control. | ESTIMATED 0.26–0.64 | Forcing late-discovery coverage can also reward waste unless its native utility is independently justified. |
| Strongest lawful combined recipe | Use cost-aware history-conditioned value prediction, freeze/thaw allocation, multiscale restarts, uncertainty-preserving exploration and randomized continuation audits; tune the whole portfolio against legal final-gain feedback. | ESTIMATED 0.76 (ESTIMATED 0.50–0.95) | It satisfies the card's scientific objective without imitating historical stop decisions. | Demonstrate a fresh observable intervention mechanism that defeats the complete scheduler while a feasible reference learns it. | ESTIMATED 0.76 (ESTIMATED 0.50–0.95) | This may already be the strongest practical implementation of the proposed policy. |

## Published recipe shortcut — web checked

- [Freeze-Thaw Bayesian Optimization](https://arxiv.org/abs/1406.3896): the primary abstract explicitly addresses choosing between pausing, starting and resuming model training using partial histories and information-theoretic selection.
- [Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization](https://jmlr.org/papers/v18/16-558.html): the primary publication page describes adaptive resource allocation and early stopping, establishing a multi-budget baseline rather than fixed patience.
- [BOHB: Robust and Efficient Hyperparameter Optimization at Scale](https://arxiv.org/abs/1807.01774): the primary abstract combines model-based configuration selection with bandit allocation and strong anytime behavior.

Verification depth is primary publication-page/abstract text from this session. No optimizer ran, and these methods' original training-curve assumptions do not prove success on intervention-changing scientific campaigns. The proposed attack extends the history features and preserves exploratory continuation rather than falsely asserting that smooth curve extrapolation solves every null result. Its combined forecast is ESTIMATED 0.76 (ESTIMATED 0.50–0.95).

## Saturation against the hypothetical 10T researcher / 12h

The continuation scheduler faces these binding thresholds: a single valid run >0.70 kills, as do oracle best-of-four mean >0.60, pass@4 >0.50 at R≥0.60, and projected upper-95% ≥0.75. They are copied requirements, not forecasts. S1 specifies reference [0.50,0.65], same-budget stronger control ≥reference+0.20 and reachable ≥0.75; S7 imposes the analogous tests on Q=(R−r_floor)/(C_L−r_floor), with a legitimately attainable ceiling rather than clairvoyance.

The strongest target can distinguish an unpromising training curve from an untested intervention. It can estimate continuation value using the available project state and spend a controlled exploration allocation on branches that look identical so far. Thus the right known-method baseline is not a rule that stops whenever recent improvement vanishes. A researcher with reliable memory and the full horizon can implement and tune a branch portfolio directly.

There is also an information-theoretic trap. If two histories are legally indistinguishable until after the stop decision but have different hidden breakthrough times, no continuation policy can identify the better branch beforehand. The achievable ceiling then depends on exploration economics, not on whether an agent acquires scientific taste. If legal histories do distinguish them, the task must show why an expressive ordinary value predictor fails. The card identifies neither a concrete distinction nor a successful reference exploiting it.

My single-run maximum forecast is ESTIMATED 0.94; best-of-four oracle mean ESTIMATED 0.86; pass@4 ESTIMATED 0.94; stronger-tier/expanded-compute upper-95% scenario ESTIMATED 0.99. Each likely exceeds its binding saturation boundary. These forecasts are not observations, fitted confidence statements or guaranteed successes. The projected upper-95% is an ESTIMATED planning envelope; empirical projection and its uncertainty remain UNMEASURED. Repeated-search success could correlate strongly across mechanisms, so no independent-trial formula was used to create the pass forecast.

S1 is OPEN without a budget-feasible reference, stronger same-contract control and native campaign-gain reserve. S7 is OPEN without an achievable ceiling that accounts for unavoidable indistinguishable histories. A clairvoyant continuation oracle is a diagnostic upper comparator, never a legal attainable control. All rollout scores, observed runs, grader noise and observed pass@k are UNMEASURED. Measure independent campaigns with matched reset states, randomized logged continuation audits and executed final improvements. Later full-budget researcher restarts must retain timeouts and count all selector costs, with development selection separate from the retrospective oracle. The weakness reports' early stopping is the symptom this task addresses, not evidence that an optimized target policy cannot solve it.

## Revised estimate versus the source card

The designer's ESTIMATED 0.39 notes that missing continuation counterfactuals can teach premature stopping. My ESTIMATED 0.76 (ESTIMATED 0.50–0.95) assumes the attacker recognizes that statistical issue and collects some randomized continuations or uses conservative uncertainty-aware scheduling. Correcting censored labels is ordinary experimental design. If counterfactual collection is too expensive for every learner, that constraint applies to the reference as well and cannot support an unmeasured low baseline.

## Boilerplate and missing build content

ESTIMATED 35–50% is generic self-improvement motivation, matching language or compliance guidance. As a construction document it is mostly boilerplate: it has no campaign generator, research action space, history schema, censoring probabilities, logging policy, checkpoint/resume semantics, final utility function, policy model, resource limits or executable reference. It does not specify whether a null result concerns low statistical power, a wrong hypothesis, an optimizer plateau or a missing prerequisite; those mechanisms imply different optimal next actions.

The proposed cheapest test itself requires running abandoned branches far enough to observe their counterfactual value. Those outcomes cannot be assigned from historical stop decisions. A realistic build would need that data collection and its selection bias included in the resource and statistical plan, rather than assuming a training corpus of correct continuation values already exists.

## Duplicate check

Catalog T03's inspected task definition already trains a transferable research controller on experiment choice, strategy switching, delayed response reversals and irreversible allocation. C119 narrows that controller to stopping/continuation and adds no independently specified environment mechanism. It is therefore a near-duplicate of checked T03, rather than a distinct resistant task. C122 is a sibling selection-component proposal, but critic ranking and continuation allocation are different interfaces. No D-card comparison is claimed.

## Verdict, required fixes and cheapest decisive check

CUT as a standalone task proposal. Censoring-aware continuation could be a useful component or difficulty axis inside T03, but the current card's novelty is a policy label over standard resource allocation. A durable redesign would need observable intervention-dependent continuation value and independent evidence that both direct Bayesian scheduling and learned history predictors leave native reserve. That is new task construction, not a security patch.

The cheapest decisive check uses CPU reasoning over proposed campaign histories: identify whether the information needed for an optimal continuation is legally present, and whether a generic cost-aware scheduler already expresses the reference. ESTIMATED accelerator requirement is 0 H100-hours. A trace-only replay could be diagnostic only when traces are actually complete, externally authored and independent of the logged stop policy; no such trace bank is supplied. Actual experiments on live model-training campaigns would require profiling the unspecified subjects before a defensible GPU budget can be given. I do not adopt the card's pilot allowance as a measurement.

If developed elsewhere, the shared delivery gates still require a root-owned branch ledger, safe checkpoint handles, trusted final-model evaluation, finite per-branch/seed deadlines, all-positive independent controls, no skipped-work credit, private decontamination and a portable exact-version archive. Independent live cheating sessions and regressions are future requirements and were not replaced by this desk exercise. No rollout, training or money-spending action occurred.

## Verdict record

id: C119
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.76 (0.50–0.95)
combined_recipe_attack: ESTIMATED 0.76 (0.50–0.95)
best_of_4: ESTIMATED 0.86
pass_at_4: ESTIMATED 0.94
single_run_max: ESTIMATED 0.94
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: none; fold into controller task or define a new observable mechanism
main_kill_reason: standard resumable allocation subsumes the stopping-policy proposal
duplicate_of: T03
souping_flag: none
urls_cited: ESTIMATED 3
