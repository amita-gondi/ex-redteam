# C006 — Train set-valued scientific predictions — saturation screen
## 1. What the grader actually rewards
The model predicts a winner set before trusted continuations reveal outcomes; the grader penalizes both missing genuine winners and including unnecessary recipes, then checks the selected recipe's realized utility. ESTIMATED R≈0 is the calibrated competent-ranker floor and ESTIMATED R≈1 is an achievable stronger set predictor under the same evidence limits. No-op overcommitment is tentatively ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60, but the promised “proper set score” lacks a concrete formula and tie definition.
## 2. Strongest lawful combined attack
Train a heteroscedastic recipe-performance predictor on legal tables and histories, preserving covariance between recipes that share a run or data source. Convert its predictive outcome distribution into winner probabilities, then choose the set minimizing the actual inclusion/exclusion score. Calibrate on held-out pools rather than individual rows. [Classification with Valid and Adaptive Coverage](https://arxiv.org/abs/2006.02544) verifies adaptive conformal set construction. Its marginal coverage guarantee does not imply correct coverage after mechanism shift or for a multi-winner target; those require pool-level calibration and explicit loss modeling.

Distill the complete calibrated decision rule into the submitted model, including typed recipe IDs and evidence-conditioned set boundaries. If the interface permits a wrapper, the same rule can run directly; the conservative forecast assumes the weights-only channel named by the card and charges distillation. Select the terminal recipe by posterior expected utility, retaining correlations when assessing ties. Search regularization, noise grouping and decision thresholds against the disclosed scoring rule. This is a coherent pipeline for the exact reward, not temperature scaling alone.

ESTIMATED single-run R=0.76, range 0.52–0.89; ESTIMATED oracle best-of-4=0.83; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED projected upper-95% envelope=0.95. All are provisional judgments. Most reward comes from learning recipe outcome uncertainty and making the Bayes set decision; calibration adds the useful boundary adjustment. Remaining errors concern genuinely new mechanisms and imperfect approximation of correlated ties. The card mentions experiments that separate hypotheses, but its grader does not require the predictor to acquire those experiments, so active experiment design cannot be credited as an unimplemented obstacle.
## 3. Other routes
- Conformalize the inherited ranker with pooled residuals, then include recipes whose intervals overlap the best. ESTIMATED R=0.62, range 0.38–0.81. This may overinclude under shared noise but is already materially stronger than confidence rescaling.
- Sweep interval widths, pool-conditioned calibration strata, tie tolerance and set-size penalty using legal dev pools; distill the selected rule if required. ESTIMATED R=0.70, range 0.47–0.86. The scorer's precise definition is decisive because different “proper” scores favor different actions.
- Always return a small fixed top-ranked set. ESTIMATED R=0.34, range 0.10–0.62. If this scores strongly, the tie prevalence and unnecessary-inclusion charge do not support the claimed scientific distinction.
## 4. What would lower lawful saturation
Specify an explicit continuation-distribution estimand and a set score eliciting that estimand, with shared-run correlation and observable mechanism information. To require scientific discrimination, add a metered choice of diagnostic experiment before the final set, then reward the selected continuation after charging that diagnostic. That is a substantive interface expansion. ESTIMATED composite after this change is R=0.48, range 0.26–0.70, with ESTIMATED several weeks of score design and experiment-family authoring plus ESTIMATED 192 H100 GPU-h for diagnostic/continuation anchor studies. Simply raising tie noise could make every method equally uncertain and would not create research headroom.
## 5. Decisive-check GPU-h re-estimate
The card quotes ESTIMATED 7 GPU-h. Revised ESTIMATED 144 H100 GPU-h: ESTIMATED 1B-parameter table/text predictor, ESTIMATED 4 model or calibration arms, ESTIMATED 3 seeds and ESTIMATED 4 H100-hours per fine-tune gives ESTIMATED 48 GPU-h; ESTIMATED 4 recipe families×3 continuation seeds×7 H100-hours adds ESTIMATED 84 GPU-h; independent evaluation adds ESTIMATED 12 GPU-h. Total ESTIMATED 48+84+12=144. Reuse continuation labels across predictor arms where scientifically valid. The old value might cover fitting a wrapper against already certified labels, but does not pay for the trusted continuations that define winners.
## 6. Duplicate check
Catalog T14 (`task_catalog_v3_full/packets/T14.md`, opened): WEAK. It learns supported claims and publish/defer decisions, whereas this target is a distribution-derived set of winning recipes and its actual downstream choice. v3 07B is a more general evaluator neighbor, but no same-intervention duplicate claim is made without a matched contract. Set-valued output is distinct enough to retain an idea, though not enough to resist the attack.
## 7. Verdict
CUT. The binding ESTIMATED best-of-four exceeds the specified line by 0.23; the single-run estimate is also over by ESTIMATED 0.06. Absent active evidence acquisition, calibrated prediction plus score-aware decisions closely implements the proposed reference behavior.
## 8. Measurement status
Rollouts UNMEASURED (planned: weights-only calibrated predictors and full lawful search). Grader noise UNMEASURED (planned: repeated continuation runs clustered by recipe pool). Score ladder UNMEASURED (planned: singleton, all-recipes, fixed top set, conformal rule, distilled joint predictor and attainable control).
## Screen record
id: C006
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.76
attack_single_range: 0.52-0.89
bo4_est: 0.83
pass4_est: 0.96
ub95_est: 0.95
gpuh_old: 7
gpuh_new_est: 144
duplicate_of: catalog-T14 WEAK
kill_reason: calibrated Bayes set decisions directly optimize the proposed grader
souping_flag: no
