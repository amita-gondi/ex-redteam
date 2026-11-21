# C058 — Search whose stopping policy is judged after a hidden-but-disclosed refresh — saturation screen
## 1. What the grader actually rewards
The scaffold must revise actual research decisions after new evidence arrives, then choose recipes whose private continuations are useful; obsolete commitments remain scored until explicitly updated. Calling a refresh endpoint or flagging possible drift earns no independent credit. R≈0 is the fixed competent revisit-policy floor and R≈1 the stronger same-budget decision control, with no-op early stopping at or below the floor; all numerical forecasts in this screen are ESTIMATED because the utility anchors are UNMEASURED.

Hazard-aware reopening is the intended reference at nominal ESTIMATED R=0.60, with its final refreshed-decision utility still UNMEASURED.

## 2. Strongest lawful combined attack
Store an explicit graph from evidence versions to claims and from claims to recipe choices. At each disclosed refresh, retrieve the delta, invalidate affected descendants, and rank reopenings by expected terminal regret reduction divided by total search and rerun cost. Maintain a hazard model for evidence arrivals using [Bayesian online changepoint detection](https://arxiv.org/abs/0710.3742) as a standard statistical component, while allowing a small new report to trigger revision through a semantic dependency rather than its size.

Apply [correlated knowledge-gradient allocation](https://people.orie.cornell.edu/pfrazier/pub/CorrelatedKG.pdf) to prioritize checks that affect several decisions. Keep cheap hash/version checks separate from costly semantic rereading, reserve a final revision tranche, and compare hazard-aware scheduling with simply reopening every affected branch. These are adaptations of verified methods, not results for this environment. The attack removes the assumption that confidence in an old conclusion makes a revision hard to notice: provenance gives an independent trigger.

ESTIMATED single-run R=0.76, range 0.58–0.90; ESTIMATED best-of-4=0.84; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED upper-95% projection=0.95. They concern improvement beyond previously committed controls, not a method simultaneously placed at reward zero. The residual consists of costly semantic dependency discovery and refreshes whose importance becomes clear only after another experiment. A cheap metadata delta followed by targeted rereading should nevertheless recover most conventional refresh cases. Unannounced hidden-only obligations would be a contract flaw rather than a legitimate residual.

## 3. Other routes
Versioned dependency invalidation followed by a fixed-priority revisit queue is the strongest simple recipe: ESTIMATED R=0.68, range 0.48–0.84. It uses no sophisticated hazard inference and directly repairs stale conclusions when reports explicitly revise known experiments.

A sweep over reserved refresh budget, maximum evidence age, reopen threshold and lookahead depth gives ESTIMATED R=0.72, range 0.53–0.87. A particularly strong lawful endpoint is deferring expensive final commitment until the last disclosed refresh when intermediate decisions carry little value; that control must be tested rather than dismissed as unscientific waiting.

## 4. What would lower lawful saturation
Commit intermediate decision value and irreversible experiment costs so that waiting until the end is suboptimal. Introduce supported, semantically indirect evidence dependencies with different observable arrival hazards, and hold out causal dependency compositions. Give development the same refresh rules and opportunities. ESTIMATED combined R after redesign is 0.48–0.63, with ESTIMATED 8–12 person-days of authoring and ESTIMATED 96 H100-h for an initial learning-continuation comparison. More refreshes without changing the value of reopening would mostly enlarge an ordinary invalidation workload.

## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 7 GPU-h. New ESTIMATED 96 H100-GPU-h comprises an ESTIMATED 8B search actor and ESTIMATED 1B continuation learner, ESTIMATED 4 revisit policies×3 campaign seeds×6 H100-h per full refreshed campaign =72, plus ESTIMATED 24 for arrival replay, independent continuation evaluation and cold-start checks. Total ESTIMATED 72+24=96. No actor pretraining is required; the learner budget is a reduced recipe-comparison pilot. The former number could replay text arrivals, but it would not determine whether revised research choices improve actual downstream learning after all reopen costs.

## 6. Duplicate check
T05: MODERATE, after inspection of its revision-safe memory packet; versioned facts and invalidation are shared, but this card submits a revisit/stopping configuration and grades research recipe utility. T03: MODERATE because its live research controller already switches strategy after contradictory evidence, although exogenous report refreshes and stopping economics are a more specific setting here. No exact same-intervention match is strong enough for a duplicate cut.

## 7. Verdict
CUT. ESTIMATED best-of-4 is 0.24 above its binding line; ESTIMATED single-run reward, pass@4 and upper projection cross their thresholds as well. Provenance-driven invalidation plus budgeted reopening addresses the central failure without needing a new scientific mechanism.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget revisit-policy construction across fresh refresh campaigns); grader noise UNMEASURED (planned: fixed-policy replays with independent actor and continuation randomness); score ladder UNMEASURED (planned: never reopen, periodic refresh, dependency invalidation, hazard allocation and attainable nonanticipatory control).

## Screen record
id: C058
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.76
attack_single_range: 0.58-0.90
bo4_est: 0.84
pass4_est: 0.96
ub95_est: 0.95
gpuh_old: 7
gpuh_new_est: 96
duplicate_of: T05 MODERATE; T03 MODERATE
kill_reason: evidence invalidation and cost-aware revisits likely exhaust headroom
souping_flag: no
