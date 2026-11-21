# C119 — Train the agent to detect its own research dead ends — screen audit
## 1. What the screen claimed
The screen combined freeze-thaw allocation, curve extrapolation, conservative offline values and paid continuation probes. Its ESTIMATED single/bo4/pass4/ub95 were 0.48/0.58/0.44/0.74; verdict CONDITIONAL, kill category none, because abandoned branches lack identifying counterfactuals. The cited URLs were https://arxiv.org/abs/1406.3896, https://ijcai.org/proceedings/2015/487 and https://arxiv.org/abs/2006.04779.

## 2. Evidence audit
Freeze-Thaw Bayesian Optimization — Kevin Swersky, 2014, first URL above, fetched — demonstrates allocating training among configurations. It does not learn whether a scientific intervention will rescue a plateau. Speeding Up Automatic Hyperparameter Optimization of Deep Neural Networks by Extrapolation of Learning Curves — Tobias Domhan, 2015, second URL, fetched — supports early termination, with roughly twofold reported HPO acceleration; extrapolating a fixed training process is weaker than anticipating a changed process. Conservative Q-Learning for Offline Reinforcement Learning — Aviral Kumar, 2020, third URL, fetched — addresses unsupported action values on control datasets, without supplying this task's missing continuation outcomes.

Grade: PARTIAL. The allocation ingredients exist, but none establishes action-conditioned campaign value under censoring. In particular, pessimism can prevent reckless continuation while also destroying the rare late-discovery utility that earns reward here.

## 3. Research done now
- TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration — Xuannan Liu, 2026 — https://arxiv.org/html/2611.20430v1 — fetched — raises confidence that a research loop can change training strategy after feedback; its externally engineered controller is not a learned stopping policy.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace/OpenAI, 2025 — https://arxiv.org/html/2504.01848v1 — fetched — lowers confidence in transferring a complete value-learning recipe into an executed research system without integration losses.
- Evaluating frontier AI R&D capabilities of language model agents against human experts — METR, 2024 — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/ — fetched — supports fast experimental iteration but documents trouble incorporating new evidence, precisely the risk when a continuation probe contradicts an early learning curve.

Search covered autonomous experiment stopping and current post-training agents; no matched autonomous continuation-policy training result was verified.

## 4. Re-estimated attack
All reward values, distribution masses and pilot allocations below are ESTIMATED forecasts, not observations. The competent floor must already include fixed patience and restart portfolios; recovering those alone cannot earn the normalized gain. Allow 0.19 expected reward from resumable uncertainty-aware allocation, 0.18 from action-conditioned outcome fitting and 0.13 from purchasing informative forks: total 0.50. These contributions describe increments in campaign utility, not independent accuracy bonuses. Their interaction is the principal extrapolation.

Recipe-availability distribution: R={0.31,0.51,0.72}, probabilities {0.25,0.56,0.19}, representing respectively censoring-biased fit, useful allocation, and discovery of a transferable intervention test. Thus single=0.25×0.31+0.56×0.51+0.19×0.72=0.50, range 0.31–0.72. Expected maximum=0.72−0.21×0.81^4−0.20×0.25^4=0.63; p=0.19, pass4=1−0.81^4=0.57. The single-run 95th percentile is 0.72. Learner seed variation is folded into these coarse outcomes; grader variance is unknown. Compared with the screen, the recipe-based upper tail is more dangerous even though its percentile is lower: repeated search selects the informative-probe insight.

## 4A. Demonstrated capability and subfield SOTA
Subfield comparator: Freeze-Thaw remains the verified pause/resume recipe here, while TrainExplorer is the strongest directly relevant current campaign system located. No common benchmark establishes a universal continuation-policy SOTA. Anchor the north star to an independently executed continuation oracle constrained to the same observations and paid interventions, with Freeze-Thaw plus restarts as floor; its attainable utility is UNMEASURED, so R≈1 cannot yet be assigned a native gain.

Demonstrated results: GLM-5.2 in TrainExplorer/Claude Code reports aggregate 39.02 in ten hours on one 80GB GPU, training 1.7B–4B subjects. That establishes strategy-changing post-training, not training the allocator. Separately, o1 with PaperBench IterativeAgent obtains 24.4% rubric credit in twelve hours on one A10; reproduction of supplied methods leaves substantial implementation gaps before counterfactual identification.

KNOWN-RECIPE: resumable BO and conservative value fitting. AGENT-DEMONSTRATED: bounded execution and strategy exploration, without a verified learned censored-history controller. attack_basis=LITERATURE-ONLY. In twelve hours the attacker must generate informative forks, distinguish intervention effects from seed variance and validate transfer to different plateau mechanisms.

ANCHORED distribution uses R={0.26,0.48,0.68}, masses {0.25,0.61,0.14}. A routine scheduling improvement contributes about 0.24, supported intervention fitting another 0.16, and selective probing about 0.05 in expectation. ESTIMATED single=0.45, range 0.26–0.68; bo4=0.68−0.20×0.86^4−0.22×0.25^4=0.57; pass4=1−0.86^4=0.45; ub95=0.68. Those masses are explicit judgment under incomplete evidence, not fitted success frequencies; the verdict rests on assumption.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT, bo4 exceeds by ESTIMATED 0.03 and pass4 by 0.07. Headline ANCHORED verdict: CONDITIONAL, UNCHANGED from CONDITIONAL; bo4 sits ESTIMATED 0.03 below its line. TrainExplorer supports an effective research loop but does not validate the learned continuation treatment. Require real fork support and a measured gain over the complete restart control.

## 6. Redesign
Cause (b): standard sequential allocation may optimize an underspecified campaign grader. Make the condition concrete: supply randomized continued/stopped branch histories with observable intervention responses, then assess new causal plateau mechanisms for which a paid diagnostic changes which branch deserves continuation. Keep checkpoints, legal interventions and their costs equally accessible. The researcher learns continuation value; merely pausing bad curves cannot exploit the intervention response.

Strongest re-attack combines Freeze-Thaw, conservative fitted values, restart diversification and an uncertainty-driven fork selector. With the recipe installed in the floor, residual expected contributions are ESTIMATED 0.17 for response modeling, 0.14 for transfer and 0.09 for allocation. Model R={0.23,0.43,0.62} with masses {0.25,0.66,0.09}: single=0.40; bo4=0.62−0.19×0.91^4−0.20×0.25^4=0.49; pass4=1−0.91^4=0.31; ub95=0.62. Basis LITERATURE-ONLY; risk remains that one generic probe resolves every family. REDESIGNABLE, contingent on measured feasibility and a nontrivial oracle reserve.

Decisive check ESTIMATED 240 H100 GPU-h: 4 policies×2 seeds×3 mechanisms×6 hours×1 H100=144 for 1B subjects; 8 randomized fork pairs×4 H100-hours=32; 4B reset-researcher inference=32; independent replay/evaluation=32. No jobs were run; this pilot can falsify the mechanism, not certify score tails.

## 7. Measurement status
Rollouts UNMEASURED (planned independent policy-construction attempts with all branches charged). Grader noise UNMEASURED (planned fixed-policy learner/researcher repeats). Score ladder UNMEASURED (planned restart, Freeze-Thaw, fitted-value, intervention-policy and constrained-oracle comparisons).

## Audit record
id: C119
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.48
old_bo4: 0.58
old_pass4: 0.44
old_ub95: 0.74
new_single: 0.50
new_single_range: 0.31-0.72
new_bo4: 0.63
new_pass4: 0.57
new_ub95: 0.72
new_verdict: CUT
binding_line: bo4>0.60
flip: CONDITIONAL->CUT
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Identify plateau mechanisms through paid intervention-response forks and compare learned continuation against full resumable allocation.
redesign_single: 0.40
redesign_bo4: 0.49
redesign_pass4: 0.31
redesign_ub95: 0.62
redesign_gpuh: 240
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer GLM-5.2 2026; PaperBench o1 IterativeAgent 2025
gap_to_attack: learned continuation under censored intervention outcomes
subfield_sota_ref: Freeze-Thaw Swersky 2014; TrainExplorer Liu 2026
anchored_single: 0.45
anchored_bo4: 0.57
anchored_pass4: 0.45
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
