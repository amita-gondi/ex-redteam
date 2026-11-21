# C088 — Graceful failure when fallback itself has opportunity cost — screen audit
ANCHORED headline: CONDITIONAL, flipped from CUT; ESTIMATED single 0.45, best-of-four 0.56.
## 1. What the screen claimed
The screen's combined attack used GracefulRL, state-conditioned critics, PPO, counterfactual training branches and planner-generated demonstrations. ESTIMATED single 0.73, bo4 0.82, pass@4 0.94 and ub95 0.95 produced CUT, category TRAIN, on the theory that ordinary sequential values already price fallback. Its sources were:
- https://arxiv.org/abs/2610.20401
- https://arxiv.org/abs/1707.06347

## 2. Evidence audit
GracefulRL demonstrates selective fallback and identifies collapse under naive policy gradients; PPO establishes a general optimization algorithm. Neither proves that a researcher can combine calibrated recovery values, informative experiments and stable fallback training within this task's budget. The old inference from “is an MDP” to “is substantially solved” omits transition learning and objective integration. Grade PARTIAL. Simple fully specified workflows remain vulnerable to planning, but comparable experimental evidence is missing for the complete attack.

## 3. Research done now
- *Training Language Models to Fail Gracefully* — Daman Arora et al., 2026 — https://arxiv.org/html/2610.20401v1 — fetched — supports retaining useful action while learning fallback, while its documented collapse pathology cuts against effortless critic-plus-PPO integration.
- *Proximal Policy Optimization Algorithms* — John Schulman et al., 2017 — https://arxiv.org/abs/1707.06347 — fetched — supplies a lawful optimizer, without a demonstrated solution to state-dependent experiment/recovery choices.
- *Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning* — Hen Davidov et al., 2026 — https://proceedings.mlr.press/v306/davidov26a.html — fetched — value-based mid-reasoning abstention is an actual human-built comparator, raising the baseline above a constant fallback bonus.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — demonstrates autonomous training-strategy exploration, but not opportunity-cost estimation in research workflows.
- *GPT-6.2 System Card* — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — PostTrainBench Lite shows useful short-budget small-model adaptation; its reference-gap metric does not establish sequential fallback utility.
- *PostTrainBench* — AISA/PostTrainBench team, 2026 — https://posttrainbench.com/ — fetched — traces document method lock-in and small-model GRPO collapse followed by KL repairs, lowering confidence that objective integration is routine. No current leaderboard value is claimed from its unreadable dynamic rows.

## 4. Re-estimated attack
If the human recipe is integrated successfully, allocate ESTIMATED 0.17 to visible cost conditioning, 0.19 to short counterfactual/planner supervision, and 0.12 to avoiding universal fallback while tuning a critic. This decomposition values actual workflow improvement; fallback frequency receives no independent credit. Unresolved recovery dynamics and contradictory training pressures account for the remainder.

ESTIMATED distribution {0.25,0.51,0.72}, weights {0.25,0.57,0.18}, models fallback collapse or poor values, a competent short-horizon learner, and successful recovery calibration. ESTIMATED single = 0.48, range 0.25–0.72. ESTIMATED bo4 = 0.72−0.21×0.82^4−0.26×0.25^4 = 0.62; p=0.18 gives pass@4 = 1−0.82^4 = 0.55; ub95 = 0.72. These forecasts are materially below the old near-saturation scores; run variability comes from optimization basin, value calibration and workflow composition, not an assumed constant best-of-four premium.

## 4A. Demonstrated capability and subfield SOTA
The closest directly fetched fallback result is GracefulRL's AIME error reduction from 79.1% to 8.9%, sacrificing 3.1 percentage points of success. Its sequential Minesweeper experiment uses eight H100s, but human-designed fallback shaping does not equal learned research-recovery pricing. Davidov et al. provide a more principled stopping comparator. Neither benchmark supplies a global SOTA ordering for this card. The reference must be anchored to achieved net state utility above both value-based stopping and GracefulRL, with retained successful action measured separately; R≈1 is presently uncalibrated.

Agent result one: GLM-5.2 with TrainExplorer's literature-planning and decoupled training scaffold reaches its reported 39.02 weighted score in ten hours per configuration on one 80GB flagship GPU. It can train candidate policies but has not demonstrated the card's recovery-value objective. Agent result two: GPT-6.2 Astra in OpenAI's unnamed PostTrainBench Lite setup closes 74.79% of the base-to-instruct performance gap, averaged across tasks/attempts, with five hours and one H100. That demonstrates substantial adaptation at relevant subject sizes, while providing no abstention-cost trajectory or critic validation.

KNOWN-RECIPE covers value-based stopping, safe fallback shaping and bounded planning. The integrated objective discovery remains beyond the verified AGENT-DEMONSTRATED scope. attack_basis=LITERATURE-ONLY. In twelve hours an agent must estimate recovery transitions, create informative training branches and avoid both fallback collapse and reckless intervention. The forecast rests on this transfer assumption.

Use anchored ESTIMATED rewards {0.25,0.48,0.68} with masses {0.25,0.62,0.13}. ESTIMATED single = 0.45, range 0.25–0.68; bo4 = 0.68−0.20×0.87^4−0.23×0.25^4 = 0.56; pass@4 = 1−0.87^4 = 0.43; ub95 = 0.68. The upper branch requires correct value integration rather than merely successful fine-tuning.

## 5. Verdict under the kill lines
The evidence re-estimate is CUT through bo4 and pass@4. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; bo4 is ESTIMATED 0.04 below its threshold. Direct evidence of collapse and the absence of a comparable autonomous recovery-value result drive the flip. It is not evidence that state-dependent costs inherently defeat a planner.

## 6. Redesign
Class (c): disclosed small workflow semantics may permit exact planner supervision; class (a) training recipes compound it. REDESIGNABLE. Make the inherited floor a cost-conditioned GracefulRL/value-stopping policy with legal planner trajectories. Use actual ML experiment/recovery workflows where interventions share learned latent causes: two cheap diagnostics can be redundant, while an apparently weak test can resolve whether a costly recovery is safe.

Supply costs, available recovery actions, representative transition histories and equivalent development probes. Reward only realized downstream model utility after all diagnostic and recovery costs, subject to successful-action retention. The hard part becomes learning reusable belief updates over causal experiment outcomes, rather than changing a fallback constant. Show a feasible reference on those same dynamics before release.

The re-attack combines Bayesian transition fitting, short-horizon planning, demonstrations and anti-collapse training. Its full scope is LITERATURE-ONLY. ESTIMATED outcomes {0.21,0.42,0.64}, weights {0.35,0.58,0.07}, imply single 0.36, bo4 = 0.64−0.22×0.93^4−0.21×0.35^4 = 0.47, pass@4 = 1−0.93^4 = 0.25, ub95 0.64. Residual danger is that a compact sufficient statistic reduces everything to a cheap planner.

ESTIMATED decisive check: 3B policy and small critic, four controls × two seeds × twelve hours × two H100 = 192 GPU-h; training-branch generation 32 GPU-h and independent utility/retention evaluation 32 GPU-h bring the total to 256 H100 GPU-h. CPU planning gets a separate ledger.

## 7. Measurement status
Rollouts UNMEASURED (planned fallback/critic/planner arms). Grader noise UNMEASURED (planned seeded workflow and utility replication). Score ladder UNMEASURED (planned fixed fallback, value stopping, joint learner and feasible stronger control).

Treat the following score and training-budget entries as ESTIMATED scenarios.

## Audit record
id: C088
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.73
old_bo4: 0.82
old_pass4: 0.94
old_ub95: 0.95
new_single: 0.48
new_single_range: 0.25-0.72
new_bo4: 0.62
new_pass4: 0.55
new_ub95: 0.72
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: c
redesign_status: REDESIGNABLE
redesign_oneline: Learn causal recovery beliefs above an inherited cost-sensitive fallback and planning floor.
redesign_single: 0.36
redesign_bo4: 0.47
redesign_pass4: 0.25
redesign_ub95: 0.64
redesign_gpuh: 256
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; PostTrainBench Lite, GPT-6.2 Astra, 2026
gap_to_attack: recovery-value learning and anti-collapse integration unshown
subfield_sota_ref: GracefulRL success-error frontier, Arora, 2026
anchored_single: 0.45
anchored_bo4: 0.56
anchored_pass4: 0.43
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
