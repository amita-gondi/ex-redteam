# C037 — Co-schedule draft training and target inference — screen audit
## 1. What the screen claimed
Online distillation, replay, break-even refresh selection and load-aware update windows formed the old attack. Its ESTIMATED single=0.51, bo4=0.59, pass@4=0.46 and ub95=0.74 produced CONDITIONAL, with no kill category recorded; persistence-dependent refresh value was required. The screen cited:
- https://arxiv.org/abs/2310.07177
- https://research.google/pubs/distillspec-improving-speculative-decoding-via-knowledge-distillation/

## 2. Evidence audit
Online Speculative Decoding demonstrates query-adaptive draft learning, and DistillSpec demonstrates better draft alignment. Neither cited experiment shows that an autonomous controller chooses profitable refreshes when training, data generation and exact target serving compete for the same pool under drifting demand. Grade: PARTIAL, because draft improvement is comparable while economic scheduling is the unverified load-bearing component. Calling acceptance-rate improvement a service improvement would ignore the card's actual denominator.

## 3. Research done now
- Online Speculative Decoding — Xiaoxuan Liu et al., 2023, revised 2024 — https://arxiv.org/abs/2310.07177 — fetched — Online target-feedback distillation increases acceptance and lowers latency on the authors' workloads. It raises the adaptive-draft floor without pricing this task's displaced serving work.
- DistillSpec: Improving speculative decoding via knowledge distillation — Google Research, 2024 — https://research.google/pubs/distillspec-improving-speculative-decoding-via-knowledge-distillation/ — fetched — A strong aligned draft is available through standard training. This makes a weak frozen-draft reference inappropriate, but supplies no persistence predictor.
- verl-SpeCo v0.2.0: Faster Standalone Training and Broader Online Co-Training — PeiXiang Tan et al./verl, 2026 — https://verl-project.github.io/posts/2026-11-16-verl-speco-v0-2-0/ — fetched — Implemented idle-window scheduling, drafter freezing and co-training reduce overhead in measured training/rollout settings. This materially raises the combined baseline, while an RL main loop differs from an external target-service queue.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — Small-model post-training and training-speed results establish real autonomous learning-pipeline ability. They do not demonstrate deciding whether an update repays shared serving contention.
- Session report: 0.9979 → 0.9697 in 126 experiments — Claude agent account via Andrej Karpathy, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — The reported overnight training loop supports meaningful cadence/loss exploration inside the budget. Its stationary validation target omits drift duration and target-request opportunity cost.

## 4. Re-estimated attack
Assume the floor already includes ordinary online distillation. ESTIMATED residual opportunity consists of 0.35 choosing/withholding refresh, 0.40 scheduling contention and synchronization, and 0.25 adapting speculative length/replay. ESTIMATED recovery fractions 0.35/0.70/0.50 yield 0.35×0.35+0.40×0.70+0.25×0.50=0.53. verl-SpeCo strengthens contention handling; uncertain future regime lifetime remains unrecovered.

ESTIMATED recipe outcomes 0.30/0.54/0.72 have probabilities 0.20/0.60/0.20: mispriced refreshes, sensible break-even control and successful persistence-sensitive adaptation. ESTIMATED single=0.20×0.30+0.60×0.54+0.20×0.72=0.53, range 0.30–0.72. ESTIMATED bo4=0.72−0.18×0.80^4−0.24×0.20^4=0.65; pass@4=1−0.80^4=0.59 with p=0.20; ub95=0.72. Learner seed, policy-selection mistakes and demand persistence produce this broad distribution, not an assumed constant uplift. Its mean is only slightly above the screen, but the explicit successful-mode probability makes repeated search more dangerous than the old offsets implied.

## 4A. Demonstrated capability and subfield SOTA
The current subfield anchor consulted is verl-SpeCo's idle-time/freeze-aware online co-training, combined with the exact-verification semantics of Online Speculative Decoding. Reference service should start from that integrated recipe. The strongest demonstrated configuration is not a proven optimum under request drift; R≈1 needs an attained shared-pool schedule that beats this floor on net completions. Separate spare-GPU draft training cannot supply a legal ceiling.

The fetched 2026 OpenAI card reports GPT-6.2 Astra closing 74.79% of the instruction-reference gap in PostTrainBench Lite, with five hours and one H100. Its internal agent harness selects data and training settings on small pretrained models. This demonstrates draft-scale training competence, while shared-pool economic control was not tested. The fetched 2026 autoresearch discussion reports Claude, version unspecified, improving its training metric through an approximately ten-and-a-half-hour H100 session. Its scaffold continuously edits, evaluates and retains candidates; the result is self-reported and its losses are not a service-value metric.

The learning ingredients are KNOWN-RECIPE, and substantial small-model experimentation is AGENT-DEMONSTRATED. The combined train/serve valuation remains LITERATURE-ONLY as attack_basis. Twelve hours must include trustworthy interference measurement and forecasting whether a newly observed regime persists, not just producing a better draft. The anchored verdict consequently relies on a transfer assumption, with current model weakness anecdotes carrying no quantitative weight.

ANCHORED ESTIMATED distribution is R=0.43/0.53/0.68, probabilities 0.25/0.65/0.10. This assumes a stronger model can usually integrate familiar learning and serving pieces, but profitable anticipatory refresh remains uncommon. ESTIMATED mean=0.25×0.43+0.65×0.53+0.10×0.68=0.52, range 0.43–0.68. ESTIMATED bo4=0.68−0.15×0.90^4−0.10×0.25^4=0.58; p=0.10 gives pass@4=1−0.90^4=0.34; ub95=0.68. Restarts are assumed independent conditional on the drift family; correlated learner failures would reduce the oracle-selection gain.

## 5. Verdict under the kill lines
Section 4's recipe-tail verdict is CUT at ESTIMATED bo4=0.65. The ANCHORED verdict is CONDITIONAL, UNCHANGED from the old screen, binding at ESTIMATED bo4 only 0.02 below 0.60. New co-training evidence removes claims that idle-window scheduling itself is a protected insight; actual agent evidence still does not establish reliable amortization under drifting service demand. Retention requires the persistence/update-benefit condition below and a full-cost floor including the newer co-training controls.

## 6. Redesign
Cause (a): familiar draft adaptation plus serving scheduling. REDESIGNABLE by specifying the old condition causally: construct realistic prompt-family histories with visible features predicting both regime persistence and which draft errors are learnable. Cross persistent and transient shifts with approaching service peaks, while preserving those relationships in development. Supply update-progress and queue telemetry, genuine frozen/no-update alternatives, and all draft refresh costs. Exact target output verification stays mandatory.

The strongest attack combines online distillation, replay-recency tuning, adaptive speculation length, verl-SpeCo-style freeze/idle scheduling and a conservative break-even controller. It loses when identical initial acceptance drops have different observable future demand and learning response, requiring jointly calibrated forecasts. Information remains available to all methods; the task must not become guessing unobservable future traffic. Demonstrate a legal predictor/controller with better net service than generic periodic and model-predictive scheduling before building a full environment.

Re-attack basis=LITERATURE-ONLY. ESTIMATED values 0.28/0.45/0.63, probabilities 0.35/0.56/0.09, give mean=0.35×0.28+0.56×0.45+0.09×0.63=0.41, range 0.28–0.63. ESTIMATED bo4=0.63−0.18×0.91^4−0.17×0.35^4=0.50; pass@4=1−0.91^4=0.31; ub95=0.63. The successful tail corresponds to learning a transferable update-payoff model. Residual risks are a simple refresh threshold solving every regime or draft training never amortizing at all; either invalidates the research premise.

Decisive measurement ESTIMATED: an 8B target and 0.5B draft share two H100s; five controllers over three drift/training seeds at two hours each require 5×3×2×2=60.00 GPU-h. Target-only references and seed/interference replay add ESTIMATED 8.00+4.00, totaling 72.00 H100 GPU-h. This proposed test is not a rollout performed here.

## 7. Measurement status
Rollouts UNMEASURED (planned fully metered shared-pool scheduling). Grader noise UNMEASURED (planned paired draft-update seeds and repeated contention traces). Score ladder UNMEASURED (planned strong frozen, periodic, current co-training controller and attained forecast-based schedule).

## Audit record
id: C037
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.51
old_bo4: 0.59
old_pass4: 0.46
old_ub95: 0.74
new_single: 0.53
new_single_range: 0.30-0.72
new_bo4: 0.65
new_pass4: 0.59
new_ub95: 0.72
new_verdict: CUT
binding_line: bo4>0.60
flip: CONDITIONAL->CUT
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Disclose predictive persistence and learnability features so draft refresh must repay future shared-pool service displacement.
redesign_single: 0.41
redesign_bo4: 0.50
redesign_pass4: 0.31
redesign_ub95: 0.63
redesign_gpuh: 72
attack_basis: LITERATURE-ONLY
demonstrated_ref: PostTrainBench Lite, GPT-6.2 Astra plus internal agent harness, 2026; autoresearch, Claude unspecified, 2026
gap_to_attack: profitable online learning under request-service contention is not demonstrated
subfield_sota_ref: verl-SpeCo idle-window and drafter-freeze co-training, Tan et al., 2026
anchored_single: 0.52
anchored_bo4: 0.58
anchored_pass4: 0.34
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
