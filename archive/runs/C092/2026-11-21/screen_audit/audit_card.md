# C092 — Entropy-robust control for an actual GPU training scheduler — screen audit
ANCHORED headline: PASS-SCREEN, flipped from CUT; ESTIMATED best-of-four 0.53.
## 1. What the screen claimed
The old attack bypassed continuous-time theorem transfer with Pollux goodput allocation, Gavel rounds, stale-state filtering, lease-aware planning and a residual learned controller. ESTIMATED single 0.68, bo4 0.78, pass@4 0.90 and ub95 0.92 led to CUT, category EXP, because discrete scheduling appeared to handle the central obstacle. The screen linked:
- https://arxiv.org/abs/2008.12260
- https://github.com/stanford-futuredata/gavel

## 2. Evidence audit
Pollux and Gavel demonstrate useful cluster allocation, but statistical goodput or throughput is not the sum of independently evaluated model improvements under delayed leases. The additional learning-value estimator, delay model and residual-policy training were never demonstrated together. Fetching the continuous-time paper confirms queueing experiments, without a real GPU training-value evaluation. Grade PARTIAL: mature resource-allocation components exist, but the decisive objective and autonomous integration remain unsupported.

## 3. Research done now
- *Pollux: Co-adaptive Cluster Scheduling for Goodput-Optimized Deep Learning* — Aurick Qiao et al., 2020 preprint, 2021 OSDI version — https://arxiv.org/abs/2008.12260 — fetched — makes statistical efficiency part of allocation, raising the baseline above GPU utilization while leaving private learning-value estimation unresolved.
- *Gavel* — Stanford Future Data group, 2020 system, repository inspected 2026 — https://github.com/stanford-futuredata/gavel — fetched — supplies heterogeneous round scheduling; lease mechanics are implementable without transporting a continuous-time robustness theorem.
- *Entropy Regularization Improves Policy Robustness in Continuous-Time Reinforcement Learning* — Jialun Cao et al., 2026 — https://arxiv.org/html/2607.03168v1 — fetched — studies continuous-time robust sets and queueing control, not delayed checkpoint-derived training utility, lowering confidence in direct theorem transfer.
- *Sia: Heterogeneity-aware, goodput-optimized ML-cluster scheduling* — Suhas Jayaram Subramanya et al., 2023 — https://www.pdl.cmu.edu/PDL-FTP/BigLearning/sia_sosp23-final.pdf — fetched — jointly handles adaptive jobs and heterogeneous devices with profiled models, improving the known scheduler comparator beyond Pollux/Gavel alone.
- *Singularity-Bench: Can Agents Build Agents?* — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — demonstrates autonomous interference-aware inference orchestration, positive evidence for engineering a scheduler but with a different value objective.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — demonstrates empirical training choices, without demonstrating allocation across dependent training jobs with delayed telemetry.

## 4. Re-estimated attack
ESTIMATED reward capture comprises 0.18 from avoiding allocation/restart waste, 0.17 from fitting ordinary progress curves and 0.15 from lease-aware filtering and residual tuning. This forecasts normalized model utility; it does not equate training throughput to quality gain. Irreversible leases selected before informative checkpoints, dependency-changing returns and poorly estimated learning curves remain outside the demonstrated components.

ESTIMATED run outcomes {0.28,0.52,0.73}, weights {0.25,0.57,0.18}, represent safe but low-value allocations, useful progress-aware scheduling and a well-calibrated value model. ESTIMATED single = 0.50, range 0.28–0.73; bo4 = 0.73−0.21×0.82^4−0.24×0.25^4 = 0.63; pass@4 = 1−0.82^4 = 0.55; ub95 = 0.73. Queue composition, learner seeds and whether early probes identify the right learning curve create the spread. The old forecasts skipped these integration failures and overstated repeat-search reliability.

## 4A. Demonstrated capability and subfield SOTA
The strongest directly matched fetched scheduling comparator is Sia's joint heterogeneity/resource-adaptivity formulation. On its evaluated cluster workloads it reports substantial completion-time and GPU-hour savings over prior schedulers. Those are achieved system results, but they do not establish SOTA for causal job dependencies or final model-value allocation. Newer scheduling search results did not yield a verified result on this exact metric. Anchor R≈1 to a same-lease, real-training control measured by independent checkpoints; that anchor is UNMEASURED, and a simulator optimum cannot substitute for it.

Two agent results separate plausible pieces. Opus 5.5 in Singularity-Bench's Claude Code setup builds a cluster-serverless scheduler in four hours on sixteen GB300s, a 64 GPU-h development envelope, excluding final verification. It achieves mean service utility 0.5101 against Dynamo/KAI's 0.4599 through measured interference and placement decisions. It does not learn training-return curves. TrainExplorer's GLM-5.2 planner/executor reaches its reported weighted post-training score of 39.02 with ten hours and one 80GB flagship GPU per configuration. It makes useful training choices for one assigned task, rather than pricing coupled jobs or discrete stale observations.

Both scheduling and training are separately AGENT-DEMONSTRATED, but their conjunction here is only KNOWN-RECIPE plus extrapolation. attack_basis=LITERATURE-ONLY. Twelve-hour integration must identify true marginal learning utility, model observability delay, train the residual controller and validate it on real queues. The headline therefore rests on assumption.

Anchored ESTIMATED distribution {0.23,0.46,0.66}, masses {0.25,0.64,0.11}, discounts unshown learning-value integration. ESTIMATED single = 0.42, range 0.23–0.66; bo4 = 0.66−0.20×0.89^4−0.23×0.25^4 = 0.53; pass@4 = 1−0.89^4 = 0.37; ub95 = 0.66. These scenario weights are not empirically calibrated by the two unrelated benchmark scores.

## 5. Verdict under the kill lines
Recipe re-estimate: CUT through bo4 and pass@4. ANCHORED verdict: PASS-SCREEN, FLIPPED CUT→PASS-SCREEN, with ESTIMATED margins of 0.28 single, 0.07 bo4, 0.13 pass@4 and 0.09 ub95. The critical evidence change is that the demonstrated cluster agent optimizes inference service while the training agent optimizes isolated tasks; neither establishes autonomous learning-value scheduling. Passing this desk screen does not establish reference feasibility or certify the task for deployment.

## 6. Redesign
NOT-NEEDED: the anchored distribution falls below every specified line by more than the requested screening margin. Keep the original real-training and checkpoint-derived utility contract, with equivalent development delays and leases. Pollux/Gavel/Sia-style controls, direct discrete planners and residual training must all be lawful. The next decisive test should determine whether ordinary useful-progress prediction already prices the private jobs; if it does, this PASS-SCREEN forecast is falsified. If the claimed job dependencies are merely independent learning curves with fresh numeric parameters, the card likely reduces to mature scheduling and needs a new audit.

## 7. Measurement status
Rollouts UNMEASURED (planned real multi-job scheduler campaigns). Grader noise UNMEASURED (planned job-seed, checkpoint and telemetry-delay repeats). Score ladder UNMEASURED (planned inherited, progress-aware, lease-aware, residual and independently attainable value-aware controls).

Each performance value below is ESTIMATED; source counts reflect fetched or listed works.

## Audit record
id: C092
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.68
old_bo4: 0.78
old_pass4: 0.90
old_ub95: 0.92
new_single: 0.50
new_single_range: 0.28-0.73
new_bo4: 0.63
new_pass4: 0.55
new_ub95: 0.73
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: na
redesign_status: NOT-NEEDED
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench cluster-serverless, Opus 5.5 Claude Code, 2026; TrainExplorer, GLM-5.2, 2026
gap_to_attack: real training-value allocation under stale leases unshown
subfield_sota_ref: Sia joint goodput scheduler, Subramanya, 2023; exact utility SOTA unverified
anchored_single: 0.42
anchored_bo4: 0.53
anchored_pass4: 0.37
anchored_ub95: 0.66
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CUT->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
