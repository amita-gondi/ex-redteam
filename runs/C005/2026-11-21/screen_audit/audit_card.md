# C005 — Reward counterfactual experiment cancellation — screen audit
## 1. What the screen claimed
Its combined recipe predicted unfinished-run outcomes, planned over capacity-releasing graph transitions, and converted simulated continuation values into a reward used by the fixed policy trainer. The ESTIMATED single/bo4/pass@4/ub95 were 0.68/0.77/0.88/0.92. The final CUT, category TRAIN, rested on graph lookahead supplying the supposedly difficult cancellation credit. The screen linked:
- https://arxiv.org/abs/1810.01963
- https://proceedings.mlr.press/v80/falkner18a.html

## 2. Evidence audit
Learning Scheduling Algorithms for Data Processing Clusters — Hongzi Mao, 2018, later published 2019, fetched at the Decima URL — demonstrates learned dependency-aware scheduling. It neither learns counterfactual scientific value from interim evidence nor shows that reward edits alone reproduce a planner. BOHB: Robust and Efficient Hyperparameter Optimization at Scale — Stefan Falkner, 2018, fetched at the second URL — supports efficient configuration search and resource allocation, but its evaluation lacks action-dependent scientific successors and reward-only distillation.

Grade: ASSUMED. The individual scheduling and search ingredients are real. However, the decisive capability is transferring a belief-sensitive planner into the fixed learner through the allowed objective channel, on fresh causal graphs. No old source demonstrates that bridge; a working external planner would be an informative control, not automatically a valid deployed solution here.

## 3. Research done now
- In-Context Freeze-Thaw Bayesian Optimization for Hyperparameter Optimization — Herilalaina Rakotoarison, 2024 — https://proceedings.mlr.press/v235/rakotoarison24a.html — fetched — Demonstrates strong learning-curve extrapolation and incremental allocation across tuning benchmarks. It raises confidence in the partial-run predictor and practical search budget, without resolving dependent scientific opportunities.
- Cost-Sensitive Freeze-thaw Bayesian Optimization for Efficient Hyperparameter Tuning — Dong Bok Lee, 2025 — https://arxiv.org/abs/2510.21379 — fetched — Jointly prices future improvement and computational cost, including stopping the search. This directly strengthens opportunity pricing, while its configuration landscape is less causally coupled than cancellation-dependent experiment graphs.
- A Trajectory-Based Bayesian Approach to Multi-Objective Hyperparameter Optimization with Epoch-Aware Trade-Offs — Wenyu Wang, 2025 — https://proceedings.mlr.press/v286/wang25a.html — fetched — Optimizes trade-offs along predicted training trajectories with early termination. It expands the credible attack beyond a terminal-loss threshold; it supplies no trained cancellation-reward transfer result.
- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts — Hjalmar Wijk, 2024, revised 2025 — https://arxiv.org/abs/2411.15114 — fetched — Finds that strong short-budget implementation performance does not imply equally strong longer-budget research returns. This is negative context for assuming effortless planner construction and validation, not a forecast of an unavailable frontier researcher or a comparable cancellation task.

Searches targeted cost-sensitive freeze/thaw methods and experiment-scheduling reward design. Recent optimization work strengthens several components, but no consulted method establishes their complete lawful composition under C005's artifact restriction.

## 4. Re-estimated attack
ESTIMATED incremental credits: interim prediction 0.23, successor-aware pricing 0.18 and fixed-trainer shaping 0.09, totaling 0.50. Exact fully observed planning does not establish learnable partial-observation credit. Committed grader tables do not grant the attacker unseen outcomes.

ESTIMATED states {0.31,0.54,0.73}, probabilities {0.32,0.50,0.18}, represent weak transfer, ordinary opportunity-aware stopping and generalizable value shaping. Cheap graph replay supports search; policy instability and joint-belief errors cause failures. The probabilities are not rollout-fitted.

ESTIMATED single=0.32×0.31+0.50×0.54+0.18×0.73=0.50, range 0.31–0.73. Independent research restarts on a common graph block imply ESTIMATED bo4=0.73−0.19×0.82^4−0.23×0.32^4=0.64. Taking p=0.18 gives ESTIMATED pass@4=1−0.82^4=0.55. Cumulative mass at the central state is 0.82, making ESTIMATED ub95=0.73. This is a single-attempt scenario quantile; a stronger-model scaling confidence interval remains unidentified.

Unproven reward-channel transfer lowers the old point; graph replay still permits occasional strong shaping. Native reward anchors remain unknown.

## 4A. Demonstrated capability and subfield SOTA
Lee's cost-sensitive freeze/thaw BO (2025, fetched above) improves the compared cost/performance trade-offs; Decima handles scheduling dependencies. Neither teaches scientific-successor value through a reward-only interface. Their legal combination defines the native-value floor, but no published composite control anchors R≈1; reference feasibility is open.

- The AI Scientist-v2 — Yutaro Yamada, 2025 — https://arxiv.org/html/2504.08066v1 — fetched. Claude 3.5 Sonnet coding with GPT-4o feedback and agentic tree search produced a selected workshop-accepted paper. The runtime cap was fifteen hours; accelerator allocation is unspecified. Searching experimental branches is demonstrated, but transferring branch value through C005's fixed reward learner is not.
- AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure — Megan Kinniment/METR, 2026 — https://metr.org/blog/2026-11-20-q4-2026-capability-update/ — fetched. The GPT-6 Astra/Opus 5.5-era cohort's best Budget NanoGPT run saves a reported 15.7% in forty-eight hours on eight H100s. The prose does not identify that winner's model. This cautions against treating long-budget optimization as reliable twelve-hour policy-credit discovery.

Basis ASSUMED: KNOWN-RECIPE planning does not establish the permitted artifact. AGENT-DEMONSTRATED reward transfer is absent; shaping must be learned and validated without deploying the external planner.

ANCHORED ESTIMATED outcomes {0.20,0.42,0.67}, masses {0.43,0.49,0.08}, separate transfer failure, useful shaping and a discovered general credit representation. Single=0.43×0.20+0.49×0.42+0.08×0.67=0.35, range 0.20–0.67; bo4=0.67−0.25×0.92^4−0.22×0.43^4=0.48; pass@4=1−0.92^4=0.28; ub95=0.67 because the lower CDF is 0.92. Conditional independence and probabilities are subjective; no benchmark rate was inserted as C005's success probability.

## 5. Verdict under the kill lines
The section 4 estimate is CUT, with ESTIMATED bo4 0.04 over its threshold. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL. Its ESTIMATED margins are single 0.35, bo4 0.12, pass@4 0.22 and ub95 0.08. The absent reward-channel result prevents an evidence-based saturation claim, while unanchored utility and synthetic-only shape prevent PASS-SCREEN. The assumption-dependent condition is a real-campaign reward artifact with a feasible same-budget reference, described below.

## 6. Redesign
The anchored condition requires reward-only feasibility on real ML work. The following campaign revision's re-attack basis remains ASSUMED.
Cause (c): small graph semantics can expose successor values; objective search compounds this. Replace synthetic tables with real continuation campaigns where cancellation changes both capacity and available checkpoint evidence/initialization. Shared learning regimes should include plateaus valuable for later adaptation despite weak immediate accuracy. Disclose scheduling, retention and reservation rules, with causally matched development campaigns.

Grade downstream quality at fixed H100 allocation, charging abandoned reservations, probes and policy execution. Only the reward definition is submitted; shaped return earns nothing independently. Frontier labs need cancellation decisions that preserve scientifically valuable partial artifacts.

Re-attack with freeze/thaw predictions, joint successor beliefs, checkpoint-value estimation, Monte Carlo lookahead and potential search. Capacity accounting remains straightforward; predicting later adaptation value and teaching it through reward remain uncertain. Equal-budget continuations must establish that residual beyond final-loss extrapolation or reject the redesign.

ESTIMATED redesign distribution {0.22,0.42,0.64}, masses {0.43,0.50,0.07}, represents stopping-only, artifact-aware and transferable-credit methods. Single=0.43×0.22+0.50×0.42+0.07×0.64=0.35; bo4=0.64−0.22×0.93^4−0.20×0.43^4=0.47; pass@4=1−0.93^4=0.25; ub95=0.64. REDESIGNABLE. Risks are an ordinary joint surrogate solving it or successor value proving unaffordable to estimate.

Decisive pilot GPU-h ESTIMATED: train a 100M graph policy under four reward arms, three seeds and three H100-hours per run (4×3×3=36). Then compare four cancellation policies, three campaign seeds, each with an eight-H100-hour aggregate budget for a 1B subject learner (4×3×8=96), plus twelve H100-hours for terminal evaluation: 36+96+12=144. All campaign experiments share that aggregate allocation; it is not an uncharged per-branch allowance.

## 7. Measurement status
Rollouts UNMEASURED (planned reward-only attacks followed by fixed-trainer cancellation policies). Grader noise UNMEASURED (planned repeated campaign and policy seeds with paired reservation histories). Score ladder UNMEASURED (planned native completed-work value for no cancellation, predictive stopping, graph planning, artifact-aware shaping and stronger feasible credit).

## Audit record
id: C005
old_verdict: CUT
evidence_grade: ASSUMED
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 8
old_single: 0.68
old_bo4: 0.77
old_pass4: 0.88
old_ub95: 0.92
new_single: 0.50
new_single_range: 0.31-0.73
new_bo4: 0.64
new_pass4: 0.55
new_ub95: 0.73
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: c
redesign_status: REDESIGNABLE
redesign_oneline: Learn cancellation credit for real continuation campaigns where checkpoint evidence changes successor learning value as well as capacity.
redesign_single: 0.35
redesign_bo4: 0.47
redesign_pass4: 0.25
redesign_ub95: 0.64
redesign_gpuh: 144
attack_basis: ASSUMED
demonstrated_ref: AI Scientist-v2, Claude 3.5 Sonnet with GPT-4o tree-search feedback, 2025; Budget NanoGPT, METR frontier cohort winner unspecified, 2026
gap_to_attack: Turn external belief-sensitive planning into a generalizable reward-only trained cancellation policy
subfield_sota_ref: Cost-sensitive stopping trade-offs, Lee freeze-thaw BO, 2025; reward-only scientific successor control unavailable
anchored_single: 0.35
anchored_bo4: 0.48
anchored_pass4: 0.28
anchored_ub95: 0.67
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: ASSUMED
souping_flag: no
