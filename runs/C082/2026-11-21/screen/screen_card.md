# C082 — Scaling laws that choose the right regularized continuation — saturation screen
## 1. What the grader actually rewards
A plan must commit a loss forecast, choose a continuation and pay for its probes before the continuation is executed at the protected horizon. The reward mixes final loss and a proper forecast score, whose relative weight is not yet fixed. R≈0 is the competent cost-aware planning floor, R≈1 is an attainable accurately forecast high-quality continuation, and the no-op/reference positions are provisionally ESTIMATED 0.00/0.60; this forecast assumes final learning utility has the dominant weight.
## 2. Strongest lawful combined attack
Fit the coupled regularization scaling form from [the verified pretraining paper](https://arxiv.org/abs/2606.06888), alongside alternative learning-curve regressions, and retain predictive uncertainty rather than choosing by fit residual alone. Use [Freeze-Thaw Bayesian Optimization](https://arxiv.org/abs/1406.3896) to resume informative runs, reserve direct late-horizon probes for likely winners, and choose the continuation by expected terminal loss subject to total cost. Alternative predictive models may be compared or used to report uncertainty; this attack never combines model weights.

The key bypass is to purchase observations near the actual decision horizon instead of relying on distant extrapolation. With a modest set of regularizers, the budget can support direct evidence for finalists, while conservative forecasts protect the proper-score term. ESTIMATED single-run R=0.64, range 0.43–0.81; ESTIMATED oracle best-of-4=0.73; ESTIMATED pass@4 at R≥0.60=0.84; ESTIMATED projected upper-95% bound=0.89. Residual error remains where regularizer rankings cross only after all affordable probes or where corpus mechanisms change scaling direction. The card posits such transport failure, but does not supply a horizon/cost ratio that makes direct finalist continuation ineffective. Unknown forecast weighting widens uncertainty rather than proving difficulty.
## 3. Other routes
- Freeze-thaw optimization without the new scaling law is ESTIMATED R=0.56, range 0.34–0.74. It targets the actual terminal decision and can outperform a scientifically interesting but misspecified global law.
- A balanced sweep of short trajectories followed by longer replication of finalists is ESTIMATED R=0.61, range 0.40–0.79. Search loses efficiency when late ranking reversals are common, but it avoids dependence on a single parametric extrapolator.
- Submit broad calibrated predictive intervals and a safe stock continuation: ESTIMATED R=0.35, range 0.17–0.58. This could become stronger if the proper-score term overweights uncertainty calibration relative to useful final loss; the exact score must be published before implementation.
## 4. What would lower lawful saturation
Commit the forecast target, proper scoring rule, utility weights and probe budget before any policy comparison. Construct identifiable repetition/regularizer interactions with delayed but development-visible ranking reversals, and impose a scientifically motivated horizon ratio that prevents directly finishing every finalist. ESTIMATED attack could fall to R=0.43–0.57, at ESTIMATED author effort of two weeks and ESTIMATED 240 additional H100 GPU-h to establish real crossing trajectories. The author must show that an attainable controller can exploit early intervention evidence; otherwise equally good observed curves are an information limit, not research reserve. Numerical model-fitting complexity alone does not create a hard continuation decision.
## 5. Decisive-check GPU-h re-estimate
The source gives ESTIMATED 16 GPU-h. Revised ESTIMATED cost is 672 H100 GPU-h: ESTIMATED 6 continuation configurations × 2 seeds × 48 H100-hours = 576 GPU-h on 1B subjects trained for roughly ESTIMATED 3B tokens including regularizer work; ESTIMATED 12 proxy trajectories × 1 seed × 4 hours = 48 GPU-h on 125M subjects; ESTIMATED evaluation and checkpoint overhead adds 48 GPU-h. Both model sizes and runtimes are planning assumptions. Reusing actual measured trajectories between competing planners is permissible for an initial falsification, but final chosen continuations must run live. The old allocation cannot reveal long-horizon rank reversals reliably.
## 6. Duplicate check
Catalog T03 — MODERATE after opening its reusable experiment-controller specification: both choose costly learning experiments and score downstream training, but C082 restricts decisions to intervention-sensitive scaling forecasts and adds a proper forecast target. D24 — WEAK, because its inspected controller selects fixed policies from diagnostic evidence rather than financing live continuation training. These comparisons do not establish a strong duplicate.
## 7. Verdict
CUT. ESTIMATED best-of-4 is 0.13 above its kill line and ESTIMATED pass@4 exceeds its boundary by 0.34. The best lawful attack uses the scaling law as one input while buying direct finalist evidence, a route the card's current contract leaves open.
## 8. Measurement status
Rollouts UNMEASURED (planned: cost-aware continuation controllers on fresh live corpora); grader noise UNMEASURED (planned: repeated terminal training and forecast rescoring); score ladder UNMEASURED (planned: safe continuation, scaling-only, freeze-thaw and intervention-aware attainable control).
## Screen record
id: C082
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.64
attack_single_range: 0.43-0.81
bo4_est: 0.73
pass4_est: 0.84
ub95_est: 0.89
gpuh_old: 16
gpuh_new_est: 672
duplicate_of: catalog T03 MODERATE; D24 WEAK
kill_reason: direct late horizon probes plus cost aware continuation selection
souping_flag: no
