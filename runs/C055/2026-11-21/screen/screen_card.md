# C055 — Search with local surrogate models that must know when to retire — saturation screen
## 1. What the grader actually rewards
Submitted lifecycle code is installed into a reset research agent; reward comes from its best independently validated training result after charging surrogate maintenance and real experiments. Prediction accuracy, confident uncertainty estimates, and the act of retiring a model earn nothing directly. R≈0 is the competent frozen optimizer floor, including the unchanged lifecycle, and R≈1 is the same-budget attainable training control; numerical forecasts below are ESTIMATED pending those native anchors.

Its retirement-aware reference is assigned a nominal ESTIMATED R=0.60 comparison point, not an observed improvement over existing adaptive controllers.

## 2. Strongest lawful combined attack
Replace the lifecycle with local trust-region surrogates, success/failure-based region resizing, scheduled exploration outside the preferred region, and model reset on persistent predictive-residual changes. [TuRBO](https://arxiv.org/abs/1910.01739) already provides local Bayesian models with global allocation across regions. Add [Bayesian online changepoint detection](https://arxiv.org/abs/0710.3742) on independently obtained experiment residuals, keeping a small audit stream whose selection does not depend on surrogate optimism.

The crucial combination is deliberate external checking: a confidently wrong ensemble cannot veto the scheduled real probes. When a region fails calibration, discard its fitted surrogate state, refit on a recent window, and compare the resulting acquisition policy with model-free exploration. Tune audit spending, reset sensitivity and local-region lifetime jointly against final executed training quality. This is legal scaffold replacement under the card's submission channel, and the source does not impose a restriction that would prevent it.

ESTIMATED single-run R=0.74, range 0.55–0.87; ESTIMATED best-of-4=0.82; ESTIMATED pass@4 at R≥0.60=0.95; ESTIMATED upper-95% projection=0.94. These subjective numbers concern a transferred complete policy beating a committed calibration floor; they cannot also be its measured score after that identical policy enters the floor. The unresolved remainder is an experiment landscape with useful basins that sparse audits rarely sample. If the reference also cannot locate those basins through legal observations, that is inaccessible utility rather than resistance to standard methods.

## 3. Other routes
TuRBO with its ordinary restart logic and no separate change detector has ESTIMATED R=0.62, range 0.41–0.79. Its local safeguards already address a substantial part of surrogate overconfidence; a fixed surrogate with greedy acquisition is too weak a comparison.

A model-free successive-elimination search over actual recipe outcomes, retaining an incumbent and reserving budget for final confirmation, has ESTIMATED R=0.66, range 0.45–0.82. A development sweep can choose whether surrogate fitting pays at all. That bypass is particularly dangerous when real experiments are cheap relative to fitting and when the recipe space is small.

## 4. What would lower lawful saturation
To re-enter, define action-induced regime changes where trusting, auditing or retiring a surrogate changes the future experimental distribution, with meaningful costs for losing transferable past data. Hold out those causal couplings and expose predictive development cases. ESTIMATED residual attack would be 0.46–0.63, with ESTIMATED 12–18 person-days of authoring and ESTIMATED 288 H100-h for a learning-outcome pilot. Generic drift, periodic refresh and disagreement thresholds alone do not change the task relative to existing adaptive-controller designs. The revised artifact should also be narrower than unrestricted research-controller replacement so its scientific distinction is reviewable.

## 5. Decisive-check GPU-h re-estimate
Old budget: ESTIMATED 12 GPU-h. New ESTIMATED 288 H100-GPU-h assumes ESTIMATED 1B training subjects, ESTIMATED 4 controller arms, ESTIMATED 3 independent mechanism histories with one shared training-seed schedule per history, and ESTIMATED 20 H100-h of executed recipe experiments per arm/history: 4×3×20=240. Independent incumbent confirmation and repeated downstream grading add ESTIMATED 48, totaling ESTIMATED 288. CPU surrogate fitting is separately accounted as wall time, not relabeled GPU training. This is still only a reduced-model falsification comparison. The old allowance cannot support repeated campaigns in which several genuinely trained recipes expose and correct surrogate bias.

## 6. Duplicate check
T03: STRONG. Its source packet already submits a reusable controller, fits an ensemble response model, updates that model after contradictory experiments, switches strategy, and grades final live-training outcomes; its combined baseline explicitly includes change detection and rollback. The title's claim that the older task fixes the surrogate is contradicted by that source. T20 is WEAK because it shares research-agent scaffolding but lacks the surrogate-controlled learning campaign target.

## 7. Verdict
CUT, binding reason duplicate. C055's unrestricted lifecycle code changes the same controller component and is judged by the same downstream training target as T03, without an instantiated additional coupling. Independently, ESTIMATED best-of-4 is above its saturation line by 0.22; changing the title to emphasize self-modification does not remove that attack.

## 8. Measurement status
Rollouts UNMEASURED (planned: reset controllers across independent mechanism histories); grader noise UNMEASURED (planned: repeated incumbent confirmation with fixed lifecycle artifacts); score ladder UNMEASURED (planned: frozen surrogate, periodic refresh, trust-region restart, audit/change detector and attainable training control).

## Screen record
id: C055
verdict: CUT
binding_line: duplicate
attack_single_est: 0.74
attack_single_range: 0.55-0.87
bo4_est: 0.82
pass4_est: 0.95
ub95_est: 0.94
gpuh_old: 12
gpuh_new_est: 288
duplicate_of: T03 STRONG; T20 WEAK
kill_reason: existing adaptive controller already updates and retires response models
souping_flag: no
