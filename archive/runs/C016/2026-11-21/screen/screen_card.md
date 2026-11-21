# C016 — Design a measurement plan that survives correlated seed noise — saturation screen
## 1. What the grader actually rewards
The measurement plan must select a genuinely useful recipe and commit accurate utility forecasts, with shared streams treated as dependence blocks. ESTIMATED R≈0 corresponds to a competent independent-confirmation floor, and ESTIMATED R≈1 to an attainable stronger design of experiments. An unchanged nominal-seed benchmark is provisionally ESTIMATED R=0.00 and the reference ESTIMATED R=0.60; the selection/forecast tradeoff and squared-error scaling need explicit frozen weights before those numbers mean operational reward.
## 2. Strongest lawful combined attack
Separate randomization components for initialization, data order, augmentations and evaluation; cross components on a small diagnostic subset, fit a hierarchical variance model, and compare recipes within genuine shared-stream blocks. Then allocate remaining runs by sequential elimination and independently confirm the selected winner using newly generated nuisance streams. [Deep Reinforcement Learning That Matters](https://arxiv.org/abs/1709.06560) verifies the experimental-variability problem. [Deep RL at the Edge of the Statistical Precipice](https://arxiv.org/abs/2108.13264) and its verified [rliable library](https://github.com/google-research/rliable) supply useful uncertainty tools, although their standard resampling must be adapted to this card's actual shared-stream units.

A frontier researcher can inspect the public RNG interface, test whether nominally independent launches share trajectories or gradients, and use paired controls to identify which coupling changes rankings. Forecasts shrink noisy recipe estimates toward a pooled prior, with uncertainty propagated over the identified blocks. Reserve confirmation budget in advance instead of spending everything on an apparently precise winner. If the task does not permit breaking or observing any component of a hidden coupling, the plan can remain conservative but cannot infer independent means from unidentifiable evidence; that would be a task-validity problem, not durable model weakness.

ESTIMATED single-run R=0.81, range 0.61–0.93; ESTIMATED oracle best-of-4=0.88; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED upper-95% projection envelope=0.98. No experimental variance estimate is implied. Most available reward should come from avoiding pseudoreplication, using proper blocking and independently confirming the winner. Remaining error is limited run budget and undiagnosed component interactions. The scientific task is sensible, but competent factorial diagnostics plus conservative estimation are already the standard response to its disclosed failure.
## 3. Other routes
- Blocked paired comparisons with a reserved independent final check: ESTIMATED R=0.67, range 0.43–0.85. This may win without explicitly modeling every covariance component.
- Search allocation fractions, elimination confidence, blocking choices and shrinkage strength against public ledger campaigns. ESTIMATED R=0.75, range 0.53–0.90. CPU simulations can tune policy before expensive continuation requests, provided synthetic trials do not claim to be measured model results.
- Predict the pooled utility mean and select a robust incumbent. ESTIMATED R=0.46, range 0.20–0.74. A surprisingly strong score would reveal that the squared-error term rewards conservative forecasts more than the task rewards useful recipe discrimination.
## 4. What would lower lawful saturation
Require choosing among paid interventions on the randomization pipeline, where breaking one correlation changes the value of another experiment and the deployment estimand remains clearly defined. Show that the complete factorial/blocking baseline still misallocates a meaningful fraction of the same run budget. Freeze which components are legally controllable, with matching dev probes. Forecast redesigned composite: ESTIMATED R=0.49, range 0.27–0.71. Estimated cost is ESTIMATED several weeks of real correlated-run assets and ESTIMATED 320 additional H100 GPU-h. Hiding coupling identities without any identifying intervention would instead make the forecast target unknowable.
## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 8 GPU-h. Revised ESTIMATED 224 H100 GPU-h assumes an ESTIMATED 1B-parameter subject, ESTIMATED 4 recipe arms, ESTIMATED 4 independently generated nuisance blocks, ESTIMATED 2 initialization seeds within each block and ESTIMATED 6 H100-hours per continuation: ESTIMATED 4×4×2×6=192. Add ESTIMATED 24 GPU-h for independent winner confirmation and ESTIMATED 8 GPU-h for grading: ESTIMATED total 224. Measurement-plan code itself is CPU work. An existing certified outcome ledger could make a selector comparison nearly GPU-free, but producing that ledger and independent confirmation is not covered by the original tiny pilot.
## 6. Duplicate check
D24 (`hidden_task_cards_v4/cards/D24.md`, previously opened): MODERATE, sharing paid diagnostic allocation and candidate selection, but C016 specifically targets causal RNG dependence plus calibrated utility forecasts on continuation recipes. Catalog T03 (`task_catalog_v3_full/packets/T03.md`, opened): MODERATE, since it is a research allocation controller rather than an independence-aware measurement plan. Neither title alone warrants calling this a STRONG duplicate.
## 7. Verdict
CUT. ESTIMATED single-run score is 0.11 over its boundary, with a best-of-four breach of ESTIMATED 0.28. The standard design-of-experiments stack directly addresses the stated pathology; no concrete dependent discovery remains after it.
## 8. Measurement status
Rollouts UNMEASURED (planned: adaptive plans with independent final recipe confirmation). Grader noise UNMEASURED (planned: variance components estimated from crossed real continuations). Score ladder UNMEASURED (planned: nominal seeds, proper blocking, reserved confirmation, adaptive factorial design and attainable stronger selector).
## Screen record
id: C016
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.81
attack_single_range: 0.61-0.93
bo4_est: 0.88
pass4_est: 0.98
ub95_est: 0.98
gpuh_old: 8
gpuh_new_est: 224
duplicate_of: D24 MODERATE; catalog-T03 MODERATE
kill_reason: blocked factorial diagnosis and independent confirmation are standard
souping_flag: no
