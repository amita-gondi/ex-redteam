# C109 — Fix calibration, then optimize a scheduler whose decisions change calibration — saturation screen
## 1. What the grader actually rewards
Completed jobs must deliver actual model improvement, with all pool resources charged and postponed or abandoned jobs kept in the forecast audit. Better utilization or wider forecast intervals cannot substitute for learning utility. ESTIMATED R≈0 is a competent exploration-aware scheduler's native improvement floor; ESTIMATED R≈1 is an attainable stronger allocation at the same queue and compute limits. A scheduler doing no useful work should remain at ESTIMATED R≈0, while the intended ESTIMATED reference near 0.60 has no measured native anchor.
## 2. Strongest lawful combined attack
Model runtime as a censored duration distribution rather than treating abandoned jobs as fast failures or missing rows. Retain elapsed-time lower bounds, queue features, selection probabilities and actual improvement at each completed checkpoint. Force a small randomized exploration tranche to obtain coverage, estimate selection correction only where overlap exists, and update runtime and utility predictions together. This is a standard decision-feedback treatment, not a privacy or grader exploit.

Use [BOHB](https://proceedings.mlr.press/v80/falkner18a.html) for cost-efficient candidate allocation and [ASHA](https://arxiv.org/abs/1810.05934) for asynchronous budgeted continuation. Their published mechanisms do not solve informative censoring by themselves; the attack adds the logged censoring model and completion audits explicitly. Compare optimistic and conservative utility-per-time rankings, periodically finish uncertain jobs to identify their tails, and reserve enough resources to prevent starvation. Fit time-varying predictors on recent observations, testing whether queue composition or model scale changes calibration. A competent researcher can tune the exploration/continuation tradeoff against real development improvement across complete queues.

ESTIMATED single-run R=0.66, range 0.44–0.83; ESTIMATED oracle best-of-4=0.75; ESTIMATED pass@4 at R≥0.60=0.86; ESTIMATED projected upper-95% score=0.90. The residual is counterfactual information about expensive uncompleted jobs and shared-resource interference that changes durations after admission. Those are real limitations. However, the card does not specify a narrow exploration budget, adversarial overlap failure or intervention-dependent utility that defeats periodic randomized completion. Most stated pathology is addressed directly by this combined scheduler.
## 3. Other routes
The strongest single recipe is asynchronous multi-fidelity allocation with a fixed random exploration reserve and explicit accounting for incomplete runs. ESTIMATED R=0.52, range 0.31–0.73. It can recover useful expensive jobs even with only crude runtime estimates.

A policy search over admission priority, exploration fraction, completion floor, forecast window and stopping threshold has ESTIMATED R=0.62, range 0.39–0.81. Complete-queue replay can cheaply prune policies only if it faithfully models resource interactions; otherwise final choices require real queues. A lawful static robust allocation with no runtime learning has ESTIMATED R=0.45, range 0.24–0.68. It is important because a small forecast penalty could make avoiding the endogenous predictor the best approach.
## 4. What would lower lawful saturation
Create live queues where an exploratory training job reveals which later jobs share a bottleneck and which yield useful learning, with informative partial progress and priced completion. Keep representative interference patterns in protected development queues and score downstream improvement primarily, reporting calibration separately or with justified weight. ESTIMATED attack reduction is 0.14–0.22, to roughly 0.44–0.52. ESTIMATED cost is 10–18 person-days and 320 H100-h for live shared-resource histories. Making long jobs intrinsically unobservable would be an identifiability failure, not a useful harder setting.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 16 GPU-h. New ESTIMATED cost is 224 H100 GPU-h: 4 scheduler arms × 2 queue seeds × 2 H100s × 12 hours = 192 H100-h, plus 32 H100-h for independent checkpoint utility evaluation and repeated forecast-audit grades. Assume mixed 300M–1B training jobs, with the allocation sized to permit contention rather than an idle large model reservation. ESTIMATED total 192+32=224. This is a narrow scheduler comparison, not a full frontier tail study. The old allowance can profile a few jobs but cannot reveal policy-induced selection over multiple real queues.
## 6. Duplicate check
05B, WEAK: its opened task accelerates exact distributed training while preserving updates and resume state, rather than learning which jobs to expose and complete. T03, MODERATE: its contextual experiment controller already allocates multi-fidelity research effort and evaluates live learning gains; C109 isolates censored runtime calibration within resource scheduling. The changed causal treatment is meaningful enough to avoid STRONG duplication.
## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds its threshold by 0.15 and pass@4 by 0.36. Censoring-aware forecasts, explicit exploration and ordinary asynchronous continuation form the complete lawful baseline that the current design has not moved beyond.
## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget independent scheduler construction on fresh live queues). Grader noise UNMEASURED (planned: repeat fixed policies under queue/learner seeds and matched host contention). Score ladder UNMEASURED (planned: static allocation, ASHA control, corrected forecasting, joint scheduler, reference and attainable stronger queue policy).
## Screen record
id: C109
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.66
attack_single_range: 0.44-0.83
bo4_est: 0.75
pass4_est: 0.86
ub95_est: 0.90
gpuh_old: 16
gpuh_new_est: 224
duplicate_of: 05B WEAK; T03 MODERATE
kill_reason: censoring correction exploration and multi fidelity allocation form a sufficient stack
souping_flag: no
