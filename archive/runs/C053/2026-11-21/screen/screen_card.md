# C053 — Search for absent evidence without inventing a negative result — saturation screen
## 1. What the grader actually rewards
The policy must acquire evidence about missing reports, commit probabilities for their causes, and select a training recipe whose continuation actually succeeds. R≈0 is utility no better than the calibrated missing-data recipe floor, including the inherited absence-as-failure policy; R≈1 reaches a stronger feasible control on both probabilistic assessment and downstream decisions. The aggregation between those targets is unspecified, so every numerical score and resource allocation in this review is ESTIMATED, with anchors UNMEASURED.

For the adaptive-replication reference, ESTIMATED R=0.60 is only a nominal placement until proper-score and continuation anchors exist.

## 2. Strongest lawful combined attack
Start by separating query failure, unavailable report, and an observed negative result in a typed ledger. Fit alternative publication-selection models to permitted metadata and acquired outcomes, retain a posterior over explanations, then purchase replications or metadata probes by expected reduction in recipe regret. [Manski's partial-identification treatment](https://www.sciencedirect.com/science/article/pii/S0888613X04001124) supplies the relevant warning: missing observations alone do not justify point identification. The attack should carry bounds or posterior uncertainty instead of converting missingness into fabricated negative labels.

For probe allocation, adapt [correlated knowledge gradient](https://people.orie.cornell.edu/pfrazier/pub/CorrelatedKG.pdf) to the effect of a report on competing recipe choices, with cost-sensitive stopping. Fit selection and outcome models jointly using authorized replicated cases and test model misspecification on held-out development mechanisms. The paper is an allocation ingredient, not proof that publication mechanisms are Gaussian or identifiable.

ESTIMATED single-run R=0.50, range 0.31–0.65; ESTIMATED oracle best-of-4=0.58; ESTIMATED pass@4 at R≥0.60=0.40; ESTIMATED upper-95% projected score=0.72. These refer to a stronger adaptive implementation above frozen calibration controls and are not statistical confidence statements. The residual is economically meaningful: different selection laws can fit the same early ledger yet prescribe different replication purchases. However, if they remain indistinguishable after every legal probe, neither the reference nor an attacker can infer the hidden state; that part must not count as attainable headroom.

## 3. Other routes
A single parametric selection model plus a fixed replication quota is the strongest simple recipe, with ESTIMATED R=0.39, range 0.20–0.57. It should resolve straightforward publication bias but will select the wrong follow-up when missingness depends on an unmodeled interaction.

Search over selection-model families, pessimism strength, replication fraction and stopping thresholds yields ESTIMATED R=0.47, range 0.27–0.64. Entire missingness families must be held out from selection. A constant prior forecast can also score well on the probability component if classes are imbalanced, so it belongs in the floor rather than being rejected as insufficiently elaborate.

## 4. What would lower lawful saturation
Require a public probe-availability contract and an independently checked nonanticipatory reference: each decision-relevant pair of missingness mechanisms must be distinguishable through an affordable permitted probe sequence. Freeze a proper probability score and a scientifically justified recipe-utility aggregation, with prior-only forecasting and replicate-everything controls included. Then hold out combinations of selection mechanisms and outcome dependence, while preserving matched development examples. ESTIMATED attack after these repairs is 0.44–0.56, provided reference reserve exists. ESTIMATED cost: 10–15 person-days of mechanism and identifiability work plus ESTIMATED 48 H100-h for a pilot. Removing unknowable cases may raise all methods' native performance; that is a necessary correction, not evidence of greater difficulty.

## 5. Decisive-check GPU-h re-estimate
Old card: ESTIMATED 5 GPU-h. A useful continuation check needs ESTIMATED 48 H100-GPU-h: ESTIMATED 3 policies, ESTIMATED 3 private mechanism blocks with one paired learner seed per block, and ESTIMATED 4 device-hours each with an ESTIMATED 1B learner give 3×3×4=36. An ESTIMATED 8B evidence assistant and fresh probability/continuation grading add ESTIMATED 12, giving ESTIMATED 36+12=48. The small learner tests the sign of recipe selection, not frontier-scale training. Mechanism enumeration and posterior fitting are CPU work. The old amount could test ledger handling, but not whether acquired evidence improves actual learning.

## 6. Duplicate check
T14: MODERATE after reading its packet; supported reporting and cost-sensitive deferral overlap with this target, but T14 trains a reporter rather than intervening on a publication process. T15: MODERATE from its source; sequential information acquisition is shared, while the hidden object here is informative missingness in scientific reports. The present causal process is narrower and distinct enough to avoid a STRONG duplicate finding.

## 7. Verdict
CONDITIONAL. The ESTIMATED best-of-4 margin below its kill line is only 0.02, and the ESTIMATED projection margin is 0.03. Retention requires the exact probe-identifiability contract, proper-score aggregation, and same-budget nonanticipatory reference described above; otherwise hidden-state scoring is scientifically unresolved. This is a desk hold for redesign, not a measured pass.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent probe-policy searches on fresh selection mechanisms); grader noise UNMEASURED (planned: repeated fixed policies with separately replayed continuations); score ladder UNMEASURED (planned: prior-only, missing-at-random, selection-model, adaptive replication and attainable reference).

## Screen record
id: C053
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.50
attack_single_range: 0.31-0.65
bo4_est: 0.58
pass4_est: 0.40
ub95_est: 0.72
gpuh_old: 5
gpuh_new_est: 48
duplicate_of: T14 MODERATE; T15 MODERATE
kill_reason: near best-of-four boundary and probe identifiability unresolved
souping_flag: no
