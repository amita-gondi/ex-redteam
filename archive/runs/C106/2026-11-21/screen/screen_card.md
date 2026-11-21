# C106 — Improve a world model by limiting its planner's evidence access — saturation screen
## 1. What the grader actually rewards
The endpoint is successful closed-loop control in an independent simulator, after charging real data acquisition and imagined planning. An interface that hides every risky prediction loses completion reward when those predictions are needed to act. ESTIMATED R≈0 represents the complete conservative model-based control floor and ESTIMATED R≈1 an attainable stronger controller using the same observations and interaction budget. A no-action controller should lie at ESTIMATED R≈0; an intended ESTIMATED reference near 0.60 needs an independently demonstrated feasible control ceiling.
## 2. Strongest lawful combined attack
Train diverse dynamics predictors with bootstrap histories and different observation abstractions, then constrain planning by support distance, disagreement and validation error. [MOPO](https://arxiv.org/abs/2005.13239) verifies uncertainty-penalized model-based optimization; [MOReL](https://arxiv.org/abs/2005.05951) verifies pessimistic treatment of unsupported transitions. Their relevance is a conservative baseline, not a guarantee that disagreement detects every error. Use short-horizon replanning and compare the return ordering of candidate actions across predictors before exposing their evidence to the planner.

When proposed actions depend on uncertain evidence, spend real interaction on the disagreement frontier, retrain the predictors and relax the evidence gate where errors shrink. Also test randomized representation perturbations and held-out trajectory residuals, which can expose confident consensus mistakes missed by bootstrap variance. Keep a supported fallback controller so uncertainty does not cause complete paralysis. All real episodes, candidate action searches and retraining count toward the same budget. This closes the basic model-exploitation loop without needing a novel world-model objective.

ESTIMATED single-run R=0.44, range 0.25–0.66; ESTIMATED oracle best-of-4=0.54; ESTIMATED pass@4 at R≥0.60=0.31; ESTIMATED projected upper-95% score=0.71. The remaining obstacle is decision-relevant aliasing: every predictor may fit the observed history while recommending the wrong contact action, and the next observation must be actively selected to distinguish those histories. Generic pessimism can remove the only route to completion. That is a substantive residual, but the current prose does not establish that enough tasks require such an identification step.
## 3. Other routes
MOPO-style uncertainty penalization with fixed real-data coverage is the strongest isolated recipe. ESTIMATED R=0.31, range 0.16–0.52. It should prevent obvious optimistic exploitation, while sharing the abstraction errors of its model family.

A sweep over gate thresholds, rollout horizon, ensemble diversity and real-data acquisition frequency would be a strong no-diagnosis competitor. ESTIMATED R=0.40, range 0.22–0.63. The outer researcher can select by true development completion rather than imagined value. A direct model-free controller trained on the allowed simulator interactions is also lawful if the artifact interface permits it: ESTIMATED R=0.48, range 0.20–0.76. Cheap simulator access could make this bypass decisive, so it must be priced and tested explicitly.
## 4. What would lower lawful saturation
Require tasks where useful actions cross an apparently unsupported region, with an affordable sensing action that resolves a shared latent alias and changes which model evidence is safe to use. Include matched dev examples, fixed real-interaction pricing and a direct-controller control at the same cap. ESTIMATED attack reduction is 0.07–0.13, placing the combined route around 0.31–0.37. ESTIMATED cost is 12–22 person-days of dynamics/observation design and 180 H100-h for feasibility and conservative-control pilots. Do not hide the identifying observation or reward safety alone: either would lower utility without establishing research reserve.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 22 GPU-h. New ESTIMATED requirement is 144 H100 GPU-h. Assume a 200M observation/world-model stack and smaller control policy: 4 evidence/training arms × 3 seeds × 6 H100-h = 72; independent simulator acquisition and closed-loop evaluation for those 12 models × 3 H100-h = 36; a direct model-free route at 3 seeds × 8 H100-h = 24; repeated fixed-controller grading adds 12. ESTIMATED total 72+36+24+12=144. Simulator CPU-hours need their own ledger. The earlier allowance might screen immediate gating gains but does not cover acquired-data feedback or the direct-controller bypass.
## 6. Duplicate check
T13, WEAK: its opened contract learns actionable representations from passive video through a fixed bridge, rather than regulating model evidence in planning. D32, WEAK: it allocates robot annotations under a frozen learner, while C106 changes both the planner interface and the learned dynamics. D22, WEAK: induced-failure training resembles the feedback loop, but its teacher-to-student transfer target is different.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 is 0.06 below its line, but projected upper-95% score is only 0.04 below the projection kill. Require identifiable shared-alias tasks, paid sensing and the matched direct-controller comparison; inexpensive direct simulation training would invalidate this forecast.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent complete interface/world-model optimization attempts). Grader noise UNMEASURED (planned: repeated simulator seeds and retraining of fixed evidence policies). Score ladder UNMEASURED (planned: no-action, ungated planning, pessimistic planning, active correction, model-free control and attainable stronger control).
## Screen record
id: C106
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.44
attack_single_range: 0.25-0.66
bo4_est: 0.54
pass4_est: 0.31
ub95_est: 0.71
gpuh_old: 22
gpuh_new_est: 144
duplicate_of: T13 WEAK; D32 WEAK; D22 WEAK
kill_reason: none
souping_flag: no
