# C098 — Report and repair censored training failures — saturation screen
## 1. What the grader actually rewards
The final recipe is judged by delivered private learning utility over a fixed launch population, including crashes and timeouts, and by failure-probability calibration against retained outcomes. R≈0 is a competent reliability-aware optimizer and R≈1 is an attainable more reliable, useful recipe. The success-only campaign is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; reconstructing missing log rows is necessary accounting but is not itself improved learning.
## 2. Strongest lawful combined attack
Reconcile scheduler launch records, checkpoint manifests and typed exits into one append-only population, then optimize expected delivered utility directly. Use the explicit failed-trial cost, instance features and runtime cutoff supported by verified [SMAC3 scenarios](https://automl.github.io/SMAC3/latest/api/smac/scenario/) and the [algorithm-configuration interface](https://automl.github.io/SMAC3/latest/3_getting_started/). Fit separate failure and conditional-quality models, group repetitions by shared host/data failure cause, and confirm finalists on independent groups. Add conservative resource settings and validated restart handling when the interface permits actual repairs.

An important simplification is that a timed-out run's delivered utility is already observed under the contract, often zero; its hypothetical loss if allowed unlimited time need not be imputed to select the best delivered recipe. Survival modeling is useful for runtime decisions, not a requirement to manufacture successful scores for failed launches. ESTIMATED single-run R=0.82, range 0.63–0.94; ESTIMATED best-of-4=0.89; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% bound=0.97. Residual reward is uncertainty about novel correlated failure mechanisms and quality/reliability tradeoffs. Without a specified causal repair interaction, standard failure-aware configuration search addresses the stated leaderboard defect directly.
## 3. Other routes
- Choose the recipe with the best empirical complete-population utility, using grouped independent confirmations: ESTIMATED R=0.72, range 0.49–0.89. This can work without a sophisticated censoring model when sufficient launch history already exists.
- Sweep learning rate, batch size, precision-safe settings, memory headroom and allowed recovery rules with failed trials charged: ESTIMATED R=0.79, range 0.57–0.93. Search should select useful reliable progress, not simply the lowest successful loss.
- Use a conservative stock recipe and report its failure probability honestly: ESTIMATED R=0.53, range 0.28–0.76. This becomes dangerous if reliability dominates learning gain or the inherited campaign contains obvious overaggressive settings.
## 4. What would lower lawful saturation
Introduce a concrete intervention-dependent failure mechanism that changes which training evidence is worth acquiring, with recoverable precursor signals and matched development support. Freeze complete-ledger SMAC-style selection and conservative restart controls in the floor, while fixing the relative weights of delivery and calibration. ESTIMATED attack could fall to R=0.43–0.59, at ESTIMATED effort of two engineer-weeks and ESTIMATED additional 192 H100 GPU-h for actual correlated-failure campaigns. Missing records alone do not qualify: if launches cannot be reconstructed independently, the grader lacks its population rather than becoming a harder scientific task.
## 5. Decisive-check GPU-h re-estimate
Old allocation: ESTIMATED 10 GPU-h. New ESTIMATED total: 432 H100 GPU-h, using ESTIMATED 1B training subjects. ESTIMATED 4 recipe-selection strategies × 3 independent failure-group seeds × 24 H100-hours = 288 GPU-h; controlled failure/recovery repetitions add ESTIMATED 96 GPU-h and final quality/calibration evaluation adds ESTIMATED 48 GPU-h. Crash runtime is charged even when it yields no checkpoint. The earlier allowance omits independent correlated-failure groups and enough training to measure delivered progress; repeated log parsing cannot replace these outcomes. This pilot still would not certify very rare failure probabilities with narrow confidence intervals.
## 6. Duplicate check
Catalog T14 — WEAK after opening its supported-reporting specification: it learns evidence-bound claims and terminal decisions, whereas C098 selects training configurations under failure. Catalog T03 — MODERATE because its inspected controller chooses costly learning experiments and handles failed work, though this card focuses the intervention on failure modeling and reliable delivery. The source comparison does not justify a strong duplicate solely because both require honest ledgers.
## 7. Verdict
CUT. ESTIMATED single-run reward exceeds the boundary by 0.12, ESTIMATED best-of-4 by 0.29 and ESTIMATED pass@4 by 0.49. The strongest lawful attack makes the launch population explicit and optimizes observed delivered utility with mature configuration-search machinery.
## 8. Measurement status
Rollouts UNMEASURED (planned: failure-aware configuration searches and actual repairs); grader noise UNMEASURED (planned: independent failure-group and training-seed campaigns); score ladder UNMEASURED (planned: successful-only selection, conservative stock, complete-ledger selection and attainable repair-aware control).
## Screen record
id: C098
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.82
attack_single_range: 0.63-0.94
bo4_est: 0.89
pass4_est: 0.99
ub95_est: 0.97
gpuh_old: 10
gpuh_new_est: 432
duplicate_of: catalog T14 WEAK; catalog T03 MODERATE
kill_reason: complete population expected utility is directly handled by failure aware search
souping_flag: no
