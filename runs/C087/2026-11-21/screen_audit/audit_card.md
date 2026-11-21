# C087 — Prior-support diagnostics that unlock genuinely new RL behavior — screen audit
ANCHORED headline: CONDITIONAL; ESTIMATED best-of-four 0.56 leaves limited clearance.
## 1. What the screen claimed
The screen proposed support sampling, entropy/prompt interventions, STaR-like self-training, precursor curricula and lawful symbolic demonstrations. Its ESTIMATED single/bo4/pass@4/ub95 were 0.47/0.57/0.29/0.72, giving CONDITIONAL with an empty kill-category cell: discovery needed observable transfer and a matched diagnostic ablation. It referenced:
- https://arxiv.org/abs/2608.24949
- https://arxiv.org/abs/2203.14465

## 2. Evidence audit
The prior-support paper experimentally separates initialization, prompt distribution and reward density; STaR supports bootstrapping from successful rationales. Neither demonstrates an agent constructing a diagnostic that selects the right precursor intervention and improves fresh executable mechanism coverage. Moreover, dense rewards overcoming low initial support contradict a blanket inference that a missed base rollout identifies a missing capability. Grade PARTIAL: available training ingredients are credible, but their causal use by the submitted evaluator is unestablished.

## 3. Research done now
- *Demystifying Reinforcement Learning Post-Training of Language Models* — Donovan Clay et al., 2026 — https://arxiv.org/html/2608.24949v1 — fetched — its controlled sandbox shows reward granularity can change low-support learning, so support counts alone cannot prescribe this card's intervention.
- *STaR: Bootstrapping Reasoning With Reasoning* — Eric Zelikman et al., 2022 — https://arxiv.org/abs/2203.14465 — fetched — supplies the self-training component, without testing an instrument that distinguishes composition deficits from rare complete paths.
- *Curriculum Reinforcement Learning Can Incentivize Reasoning Capacity in LLMs Beyond the Base Model* — Pengxiang Cai et al., 2026 — https://arxiv.org/html/2606.22317v1 — fetched — boundary sampling plus teacher guidance is a particularly close human-built bypass, raising the curriculum floor.
- *Primitives and Paths: Predicting What Post-Training Can Do from What the Base Model Already Has* — Anqi Qu, 2026 — https://arxiv.org/html/2611.11260v1 — fetched — distinguishes primitive availability from complete-path support; it makes the diagnostic problem more specific and weakens a one-axis novelty claim.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — autonomous strategy changes are demonstrated, but instrument construction and novelty attribution are outside its reported target.
- *PaperBench: Evaluating AI's Ability to Replicate AI Research* — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched — partial reproduction results caution against assuming that reading the diagnostic literature guarantees a validated scientific implementation.

## 4. Re-estimated attack
The recipe can plausibly capture ESTIMATED 0.16 through avoiding wasted all-failure updates, 0.18 through teacher/symbolic precursor demonstrations, and 0.12 through replay and entropy selection. Support estimation itself deserves no novelty credit. Remaining value requires choosing between primitive acquisition, composition supervision and ordinary sharpening under the same total rollout budget.

For a recipe-capable implementation use ESTIMATED rewards {0.27,0.48,0.68}, probabilities {0.25,0.60,0.15}. The modes encode an uninformative support audit, useful curriculum, or a fortunate diagnostic/training match. ESTIMATED single = 0.46, range 0.27–0.68; bo4 = 0.68−0.20×0.85^4−0.21×0.25^4 = 0.57; pass@4 = 1−0.85^4 = 0.48; ub95 = 0.68. Training seeds and which precursor diagnosis is found create the spread; scorer determinism does not remove either. The old pass@4 was too low for this explicit upper-tail mass, despite similar means.

## 4A. Demonstrated capability and subfield SOTA
The strongest directly relevant fetched curriculum result is Cai et al.'s boundary-aware RL: mean pass@256 improves by 9.8 percentage points over base models across their reported model settings. That is empirical support expansion with teacher guidance, not proof of mathematically absent support or universal mechanism discovery. The card's north star should be a feasible control that improves new-composition execution after charging support probes and teacher data. No published result supplies this card's normalized R≈1 anchor.

TrainExplorer runs GLM-5.2 in a planning/decoupled-execution scaffold derived from Claude Code, with ten hours and one 80GB flagship GPU per configuration. Its weighted PostTrainBench result is 39.02, against 31.70 for the same model in Claude Code. This demonstrates selecting and training useful alternatives, while leaving support diagnostics untested. PaperBench's o1-high/IterativeAgent obtains 24.4% reproduction rubric credit with twelve hours and an A10; even with a supplied paper, complete integration is far from assured. Its objective is reproduction, not automatically choosing informative causal probes.

The attack is KNOWN-RECIPE at the curriculum level; AGENT-DEMONSTRATED applies only to adjacent post-training, not the complete diagnostic loop. attack_basis=LITERATURE-ONLY. Twelve-hour novelty attribution and matched-budget transfer validation are assumptions, especially because sampling and training compete for the same compute.

ESTIMATED anchored states {0.28,0.49,0.67}, weights {0.24,0.64,0.12}, reflect cheap useful curriculum more often than an effective new instrument. ESTIMATED single = 0.46, range 0.28–0.67; bo4 = 0.67−0.18×0.88^4−0.21×0.24^4 = 0.56; pass@4 = 1−0.88^4 = 0.40; ub95 = 0.67. The scientific validity of this extrapolation remains assumption-dependent.

## 5. Verdict under the kill lines
Both the recipe re-estimate and ANCHORED result are CONDITIONAL. The anchored verdict is UNCHANGED; bo4's ESTIMATED clearance is 0.04. The new boundary-curriculum and primitive/path work strengthen the lawful alternatives but do not demonstrate an unaided causal evaluator. The condition is a precise transfer-and-ablation contract, rather than an unsupported “new capability” label.

## 6. Redesign
Class (b): a diagnostic can otherwise win by ordinary curriculum selection or sampling artifacts. REDESIGNABLE. Define mechanism families through executable causal programs and score actual held-out compositional success. Give all methods identical precursor-generation and teacher access. Inherit boundary-aware curriculum, verifier-filtered demonstrations and entropy/replay tuning as the combined floor; require the submitted diagnostic to choose among interventions for matched checkpoints with different primitive-versus-path deficits.

Publish the intervention interface and representative evidence on dev. Cross training checkpoints and causal compositions so neither a task label nor zero observed successes reveals the answer. Compare with a shuffled-diagnostic ablation under the same sampling ledger. This is useful frontier R&D: deciding whether to spend scarce training compute on new primitives, bridges or exploration.

The strongest redesign attack uses primitive probes, boundary sampling and teacher-guided bridging, then tunes their allocation. Basis LITERATURE-ONLY: no fetched agent demonstration validates that combined triage process. ESTIMATED distribution {0.23,0.43,0.63}, weights {0.30,0.62,0.08}, gives single 0.39, bo4 = 0.63−0.20×0.92^4−0.20×0.30^4 = 0.49, pass@4 = 1−0.92^4 = 0.28, ub95 0.63. A universal teacher curriculum is the principal residual risk and must remain legal.

ESTIMATED pilot: 7B subjects, four training arms × two seeds × eight hours × four H100 = 256 GPU-h; support probing 64 GPU-h plus independent causal-transfer evaluation 32 GPU-h gives 352 H100 GPU-h. The budget is proposed future work, not compute consumed here.

## 7. Measurement status
Rollouts UNMEASURED (planned checkpoint/intervention comparisons). Grader noise UNMEASURED (planned repeated semantic execution and seed checks). Score ladder UNMEASURED (planned sampling, curriculum, diagnostic ablation and stronger transfer controls).

All reward forecasts and future accelerator allocations in this record are ESTIMATED.

## Audit record
id: C087
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.47
old_bo4: 0.57
old_pass4: 0.29
old_ub95: 0.72
new_single: 0.46
new_single_range: 0.27-0.68
new_bo4: 0.57
new_pass4: 0.48
new_ub95: 0.68
new_verdict: CONDITIONAL
binding_line: pass4>0.50
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Measure causal transfer beyond a shared teacher-curriculum floor using matched diagnostic ablations.
redesign_single: 0.39
redesign_bo4: 0.49
redesign_pass4: 0.28
redesign_ub95: 0.63
redesign_gpuh: 352
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; PaperBench, o1 IterativeAgent, 2025
gap_to_attack: autonomous primitive-versus-path diagnosis unvalidated
subfield_sota_ref: boundary-aware Curriculum RL, Cai, 2026
anchored_single: 0.46
anchored_bo4: 0.56
anchored_pass4: 0.40
anchored_ub95: 0.67
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
