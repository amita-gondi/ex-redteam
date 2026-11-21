# C106 — Improve a world model by limiting its planner's evidence access — screen audit
## 1. What the screen claimed
The screen combined ensemble disagreement, pessimistic planning, short horizons and targeted real interactions, retaining CONDITIONAL with no kill category. Its forecasts were ESTIMATED single/bo4/pass@4/ub95 = 0.44/0.54/0.31/0.71; shared observation aliases and a cheap model-free bypass were unresolved. Cited URLs were https://arxiv.org/abs/2005.13239 and https://arxiv.org/abs/2005.05951.
## 2. Evidence audit
MOPO — Tianhe Yu, 2020 — https://arxiv.org/abs/2005.13239 — fetched, supports uncertainty-penalized offline policy learning. MOReL — Rahul Kidambi, 2020, revised 2021 — https://arxiv.org/abs/2005.05951 — fetched, demonstrates pessimistic offline dynamics optimization. Neither tests the card's active acquisition/interface co-adaptation or an autonomous research agent implementing it. Bootstrap diversity also supplies no guarantee against a common missing latent variable.

Grade: PARTIAL. The pessimistic-control component has experimental precedent; targeted disambiguation and economical retraining remain extrapolations. The earlier claim that the combined loop closes ordinary exploitation is stronger than its citations establish.
## 3. Research done now
- Mastering Diverse Domains through World Models — Danijar Hafner, 2023, revised 2024 — https://arxiv.org/abs/2301.04104 — fetched — DreamerV3's broad control results strengthen the direct-controller comparator, without establishing this sensing intervention.
- Planners Exploit Deterministic Error: Dithered Low-Bit World Models — Yong Hwi Song, 2026 — https://arxiv.org/abs/2611.11780 — fetched — planning collapses despite similar one-step errors; this weakens residual-only gating as a sufficient attack.
- Beyond Policy Alignment: Closing the Planning-Learning Loop for Robot Control with Learned World Models — Kowndinya Boyalakuntla, 2026 — https://arxiv.org/abs/2609.39751 — fetched — PL-MPC couples critic supervision and terminal estimates, raising the floor beyond an isolated uncertainty penalty.
- PaperBench Science: expanding PaperBench into scientific domains — Elvis Zhang Research/Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched — scientific validation remains a bottleneck, lowering confidence in automatic sensing-loop integration.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace/OpenAI, 2025 — https://arxiv.org/html/2504.01848v1 — fetched — research reproduction provides an autonomy comparator rather than proof of robotic research success.

Search covered recent world-model exploitation, Dreamer and TD-MPC variants; the Nature landing page failed to fetch and is not counted. Five new sources and both old sources were successfully opened.
## 4. Re-estimated attack
All reward contributions, scenario probabilities and derived quantities below are ESTIMATED, not measurements. Conditional on competent implementation, pessimistic planning contributes about 0.22 reward above a provisional combined floor, horizon/replanning selection 0.14, and acquired-data correction 0.15: a central 0.51. These are nonoverlapping utility hypotheses, not measured reward terms. Unresolved aliasing, acquisition cost and learning feedback leave substantial utility unrecovered; committing actual native-utility anchors may change every normalized number.

Use a discrete scenario distribution: R=0.29 with probability 0.28 for overconservative gating; 0.51 with probability 0.60 for ordinary correction; 0.73 with probability 0.12 for successful latent diagnosis. Variation comes mainly from finding the right sensing intervention, then learner seeds, rather than additive grader noise. ESTIMATED single = 0.29×0.28+0.51×0.60+0.73×0.12=0.47, range 0.29–0.73. For independent attempts, E[max4]=0.73−0.22×0.88^4−0.22×0.28^4=0.60 before rounded threshold comparisons (unrounded 0.5967). With p=0.12, pass@4=1−0.88^4=0.40; single-run q95=0.73. The screen's bo4 gap was too narrow for an identification-dependent attack, even though its mean was similar.
## 4A. Demonstrated capability and subfield SOTA
Subfield comparator: Hafner's DreamerV3 reports one configuration across more than 150 tasks, including Minecraft diamonds without human curricula. PL-MPC is a newer directly relevant planning-learning comparator, and Song's paper identifies a remaining exploitation mechanism. No common leaderboard certifies their ordering on latent-alias acquisition. R≈1 must therefore be anchored to a same-budget, independently replayed stronger controller using those baselines, not a claimed universal optimum; that calibration is absent.

Two fetched agent results constrain transfer. Pipeline Lab's GPT-6 Astra reaches 59.08% partial credit and 13.98% full reproduction on scientific workflows; the starting reference gives 4–24-hour task limits, but the opened report does not specify hardware or scaffold. It demonstrates execution better than reliable validation, without an active robot-learning result. Starace's o1/IterativeAgent reaches 24.4% rubric credit with twelve hours and one A10; that is closer in time, but reconstructing supplied research differs from discovering informative actions under shared model error.

KNOWN-RECIPE covers conservative model-based RL; AGENT-DEMONSTRATED does not cover this full feedback loop. Basis: LITERATURE-ONLY. In twelve hours the agent must establish latent observability, choose paid sensing and validate subsequent control gains; no matching autonomous trajectory was verified.

ANCHORED ESTIMATED distribution: 0.25 (0.30), 0.46 (0.60), 0.71 (0.10). The central case comprises 0.21 conservative control, 0.13 interface tuning and 0.12 reliable acquisition. Mean=0.42, range 0.25–0.71; bo4=0.71−0.25×0.90^4−0.21×0.30^4=0.54; pass@4=1−0.90^4=0.34; q95=0.71. These probabilities express judgment under missing integration evidence; the verdict rests on assumption.
## 5. Verdict under the kill lines
Evidence re-estimate: CONDITIONAL, with unrounded bo4 only 0.0033 below its line. Headline ANCHORED verdict: CONDITIONAL, UNCHANGED; ub95 has 0.04 margin and bo4 approximately 0.06. The new exploitation evidence preserves concern about gating while reproduction results do not justify declaring the complete attack solved. This is a design hold, not a measured pass.
## 6. Redesign
Cause class (a): model-based RL stack plus standard acquisition. REDESIGNABLE. Specify contact tasks with a shared visual alias resolved by a lawful, useful probe; publish representative probe costs and dev examples. Changing contact dynamics must alter which evidence is trustworthy. Grade completion and total interaction/planning expenditure, retaining the no-gate and direct model-free controllers. The condition adds identifiable scientific structure, not inaccessible truth or arbitrary uncertainty.

The strongest re-attack combines PL-MPC-style updates, ensemble support filtering, belief-state sensing and direct policy learning. Conservative rejection now loses productive actions, while disagreement alone misses the shared alias. A sensing-aware reference must demonstrate affordable recovery before this change is accepted. Residual risk: recurrent policy learning may amortize the entire identification step.

Redesign basis LITERATURE-ONLY. ESTIMATED scenarios 0.23/0.42/0.63 with probabilities 0.32/0.60/0.08 yield mean 0.38; bo4=0.63−0.21×0.92^4−0.19×0.32^4=0.48; pass@4=1−0.92^4=0.28; q95=0.63. This plausibly clears the lines but requires the pilot. ESTIMATED decisive check: a 200M world model, four interface arms × three seeds × six hours × one H100=72 GPU-h; direct policy three seeds × eight H100-hours=24; acquisition/evaluation 36 and fixed-policy repeats 12, total 144 H100 GPU-h. No GPU work occurred.
## 7. Measurement status
Rollouts UNMEASURED (planned: complete independent sensing/interface campaigns). Grader noise UNMEASURED (planned: replay fixed controllers over paired simulator seeds). Score ladder UNMEASURED (planned: ungated, pessimistic, active-sensing, model-free and stronger feasible controls, with raw completion/cost anchors).
## Audit record
id: C106
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.44
old_bo4: 0.54
old_pass4: 0.31
old_ub95: 0.71
new_single: 0.47
new_single_range: 0.29-0.73
new_bo4: 0.60
new_pass4: 0.40
new_ub95: 0.73
new_verdict: CONDITIONAL
binding_line: none
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Require affordable alias-resolving actions and validate against a direct recurrent controller.
redesign_single: 0.38
redesign_bo4: 0.48
redesign_pass4: 0.28
redesign_ub95: 0.63
redesign_gpuh: 144
attack_basis: LITERATURE-ONLY
demonstrated_ref: PaperBench Science, GPT-6 Astra, 2026; PaperBench, o1 IterativeAgent, 2025
gap_to_attack: autonomous paid-sensing and world-model feedback integration
subfield_sota_ref: DreamerV3, Hafner, 2023/2024; PL-MPC, Boyalakuntla, 2026
anchored_single: 0.42
anchored_bo4: 0.54
anchored_pass4: 0.34
anchored_ub95: 0.71
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
