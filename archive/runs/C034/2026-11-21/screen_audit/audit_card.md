# C034 — Decode under a metered energy envelope — screen audit
## 1. What the screen claimed
A fused inference stack, joint power/batch calibration and phase-aware Pareto lookup were forecast to capture nearly all energy-efficiency opportunity. The screen's ESTIMATED single=0.80, bo4=0.87, pass@4=0.97 and ub95=0.98 led to CUT, category SYS, because the operating-point search appeared compact. It cited:
- https://arxiv.org/abs/2208.06102
- https://ml.energy/zeus/optimize/power_limit_optimizer/
- https://arxiv.org/abs/2403.20306

## 2. Evidence audit
Zeus establishes energy-aware configuration search for training, and its optimizer is usable machinery rather than a serving result. Towards Greener LLMs directly studies inference power/performance knobs, supporting workload-aware tuning but not the screen's normalized recovery fraction. Grade: PARTIAL: static energy tuning is evidenced; successful integration of latency penalties, thermal stabilization, phase changes and full service accounting within an autonomous attempt was assumed.

## 3. Research done now
- Zeus: Understanding and Optimizing GPU Energy Consumption of DNN Training — Jie You et al., 2022 — https://arxiv.org/abs/2208.06102 — fetched — Repeated-job energy optimization makes a serious calibration floor available; training convergence and serving deadlines remain different constraints.
- Power Limit Optimizer — Zeus Project, 2026 documentation state — https://ml.energy/zeus/optimize/power_limit_optimizer/ — fetched — The documented objectives can balance energy and slowdown. They make the search straightforward to implement but do not certify end-to-end decoding utility.
- Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference — Jovan Stojkovic et al., 2024 — https://arxiv.org/abs/2403.20306 — fetched — Evaluated inference tradeoffs support jointly tuning model workload, performance limits and energy; this raises confidence in ordinary operating-point gains.
- KAIROS: Stateful, Context-Aware Power-Efficient Agentic Inference Serving — Yichao Yuan et al., 2026, revised November — https://arxiv.org/abs/2604.16682 — fetched — Context-aware frequency, concurrency and placement achieve measured power reductions while meeting performance targets. Its identified thrashing regime also cuts against the claim that lower decode frequency is universally beneficial.
- InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents — Jehyeok Yeon et al., 2026 — https://arxiv.org/html/2607.20468v1 — fetched — Autonomous server tuning improves speed, yet narrow configuration exploration can lag structured search. This supports a capable attacker without equating available knobs with reliable optimization.
- Session report: 0.9979 → 0.9697 in 126 experiments — agent posting on Andrej Karpathy's behalf, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — The claimed overnight combined-recipe training search demonstrates the short-loop pattern, but it is a self-report without energy metering or matched expert controls.

## 4. Re-estimated attack
On an unmeasured reward ladder, ESTIMATED shares 0.50 static operating point, 0.30 phase/batch adaptation and 0.20 kernel/idle accounting plausibly yield recovery fractions 0.95/0.72/0.46. Their product sum is ESTIMATED 0.50×0.95+0.30×0.72+0.20×0.46=0.78 rounded. The remaining loss concerns transition dynamics and the fact that optimizing watts can reduce completed work.

Represent a well-executed literature recipe by ESTIMATED scores 0.67/0.78/0.85 with probabilities 0.15/0.55/0.30. These capture conservative static selection, competent phase control and successful joint kernel/controller tuning; thermal trace composition and search choices drive the spread. ESTIMATED single=0.15×0.67+0.55×0.78+0.30×0.85=0.78, range 0.67–0.85; bo4=0.85−0.07×0.70^4−0.11×0.15^4=0.83. Every mode crosses the success threshold, so ESTIMATED p=1.00 and pass@4=1−0^4=1.00 within this deliberately conditional recipe model. ESTIMATED ub95=0.85. Relative to the screen, measured energy complications reduce upper-tail confidence rather than simply adding a standard best-of-four bonus.

## 4A. Demonstrated capability and subfield SOTA
KAIROS is the strongest current context-aware energy-serving result opened here. It should anchor the resource-matched controller reference alongside the best fixed operating point. Its reported power reduction cannot become this card's joules-per-completion reward without matching workloads and latency constraints. No demonstrated same-device top anchor is yet available; R≈1 must denote a later attained control, not ideal minimum power.

Agent demonstrations, with outcomes reported by their sources:
- Yeon et al.'s fetched InferenceBench evaluates Opus 4.5+Claude Code on one H100 for two hours, reporting 3.37× aggregate speedup over PyTorch. That supports short server experiments; energy curves and thermal order balancing are outside the objective.
- The fetched Karpathy discussion identifies the agent only as Claude, the scaffold as autoresearch, and the device as one H100. It claims an improved validation metric over approximately ten-and-a-half hours of experiments. That establishes neither exact model identity nor independent replication, and its five-minute training loop is cleaner than a stabilized energy trial.

KNOWN-RECIPE: inference power and phase tuning. AGENT-DEMONSTRATED: adjacent short-loop optimization, not trusted energy/SLO validation. Accordingly attack_basis=LITERATURE-ONLY and the anchored decision rests on assumption. A twelve-hour researcher must instrument the trusted meter, distinguish cap effects from thermal drift, choose jointly feasible settings and validate mixed traffic; these steps are material but simpler than inventing a new energy algorithm.

ANCHORED ESTIMATED distribution is 0.53/0.59/0.67 with probabilities 0.20/0.60/0.20, representing static-only tuning, sound calibration and effective phase control. ESTIMATED single=0.20×0.53+0.60×0.59+0.20×0.67=0.59, range 0.53–0.67; bo4=0.67−0.08×0.80^4−0.06×0.20^4=0.64. ESTIMATED p=0.20, pass@4=1−0.80^4=0.59, ub95=0.67. The modest spread reflects a compact search with thermal validation risk, rather than a rare conceptual breakthrough.

## 5. Verdict under the kill lines
The recipe-only estimate is CUT at ESTIMATED bo4=0.83. The ANCHORED result remains CUT, UNCHANGED: ESTIMATED bo4 exceeds 0.60 by 0.04 and pass@4 exceeds 0.50 by 0.09. This is an assumption-dependent, near-line kill rather than a demonstrated autonomous energy solve. KAIROS strengthens the attainable human recipe while InferenceBench tempers expectations of exhaustive search; measurements near either boundary would require HOLD and planned expansion.

## 6. Redesign
Cause (b): directly searchable operating settings. REDESIGNABLE as cumulative energy allocation across stateful agent sessions with application deadlines and observable thermal history. Provide the device response curves, live counters, context-growth features and representative demand transitions. Count trusted whole-device energy, including idle periods and switching, and reward completed equivalent-quality workflows under a cumulative envelope. Keep a feasible completion target and adequate reserve; neither hidden temperature behavior nor an impossible power budget is acceptable.

Strongest re-attack: KAIROS-style context control plus a calibrated model-predictive controller, dynamic batching, fused kernels and sequential operating-point search. Put these in the floor. The additional question is when to spend energy now to avoid later context-induced thrashing and deadline loss. A memoryless phase table cannot represent that coupling, although a standard optimal controller may still solve it. Establishing a stronger attained policy is therefore essential before calling this resistant R&D.

Re-attack basis=LITERATURE-ONLY. ESTIMATED scores 0.24/0.44/0.61 with probabilities 0.40/0.50/0.10 reflect failed coupling models, a useful predictive controller and occasional strong dynamic allocation. ESTIMATED mean=0.40×0.24+0.50×0.44+0.10×0.61=0.38, range 0.24–0.61; bo4=0.61−0.17×0.90^4−0.20×0.40^4=0.49; pass@4=1−0.90^4=0.34; ub95=0.61. Risk: KAIROS already captures nearly all history dependence, making the proposed extra capability illusory.

Pilot GPU-h ESTIMATED: an 8B decoder on one H100, six controller arms, three traffic seeds, 1.50 stabilized hours per arm gives 6×3×1.50×1=27.00. Add ESTIMATED 6.00 for output checking and 9.00 for order-balanced thermal repeats: total 42.00 H100 GPU-h. No experiment or energy measurement was performed during this audit.

## 7. Measurement status
Rollouts UNMEASURED (planned matched static, context-aware and predictive policies). Grader noise UNMEASURED (planned external-meter repeatability and thermal counterbalancing). Score ladder UNMEASURED (planned joules/completion and deadline curves for fixed optimum, combined floor and attainable stronger controller).

## Audit record
id: C034
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.80
old_bo4: 0.87
old_pass4: 0.97
old_ub95: 0.98
new_single: 0.78
new_single_range: 0.67-0.85
new_bo4: 0.83
new_pass4: 1.00
new_ub95: 0.85
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Allocate cumulative energy across observable context and thermal histories with feasible workflow deadlines.
redesign_single: 0.38
redesign_bo4: 0.49
redesign_pass4: 0.34
redesign_ub95: 0.61
redesign_gpuh: 42
attack_basis: LITERATURE-ONLY
demonstrated_ref: InferenceBench, Opus 4.5 plus Claude Code, 2026; autoresearch discussion 43, Claude version unspecified, 2026
gap_to_attack: metered thermal-stable energy optimization has no matched autonomous demonstration
subfield_sota_ref: KAIROS context-aware power reduction under performance targets, Yuan et al., 2026
anchored_single: 0.59
anchored_bo4: 0.64
anchored_pass4: 0.59
anchored_ub95: 0.67
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
