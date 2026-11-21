# C127 — A curriculum flywheel that learns from cross-project interference — screen audit
## 1. What the screen claimed
The proposed attack mixed output-consistent replay, interference-based retrieval, gradient retention and generated contrastive bridge episodes, with joint retraining as an alternative. Old ESTIMATED single/bo4/pass4/ub95 were 0.45/0.56/0.34/0.73; CONDITIONAL, category none, because cross-project causal abstractions might exceed replay. Cited URLs: https://arxiv.org/abs/2004.07211, https://arxiv.org/abs/1908.04742 and https://arxiv.org/abs/1706.08840.

## 2. Evidence audit
Dark Experience for General Continual Learning: a Strong, Simple Baseline — Pietro Buzzega, 2020 — fetched at the first URL, supports rehearsal and logit consistency on continual-learning datasets. Online Continual Learning with Maximally Interfered Retrieval — Rahaf Aljundi, 2019 — fetched at the second, selects examples damaged by a prospective update. Gradient Episodic Memory for Continual Learning — David Lopez-Paz, 2017 — fetched at the third, constrains forgetting on image-classification sequences. None concerns generating data that teaches a research agent when apparently similar training interventions have opposite effects.

Grade: ASSUMED. Retention methods have evidence, but the load-bearing bridge generator and transfer to new executed research projects do not. Preserving old predictions can even reinforce the wrong unconditional heuristic; the references establish a floor, not the claimed causal abstraction improvement.

## 3. Research done now
- AgentCL: Toward Rigorous Evaluation of Continual Learning in Language Agents — Yiheng Shu, 2026 — https://arxiv.org/html/2606.02461v2 — fetched — dependency-controlled streams distinguish memory behavior that naive streams miss. This lowers confidence that generic replay results predict conditional research transfer.
- Agent Lightning: Train ANY AI Agents with Reinforcement Learning — Xufang Luo/Microsoft Research, 2025 — https://arxiv.org/html/2508.03680v1 — fetched — supplies a concrete parametric agent-training framework across SQL, retrieval and tool math, raising implementation feasibility without establishing a cross-project research curriculum.
- TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration — Liu et al. (BUPT/Alibaba), 2026 — https://arxiv.org/html/2611.20430v1 — fetched — supports autonomous training experimentation; the trained subjects solve benchmarks rather than becoming interference-resistant researchers.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — OpenAI, 2025 — https://arxiv.org/html/2504.01848v1 — fetched — demonstrates the remaining execution burden after receiving a known method, limiting claims that generated research episodes automatically become effective supervision.

Search covered continual research-agent training, curriculum interference and current controlled agent streams. No comparable autonomous bridge-curriculum discovery result was verified.

## 4. Re-estimated attack
All prospective values and distribution weights are ESTIMATED. Beyond a competent replay floor, allow 0.12 for targeted retention, 0.13 for conditioned bridge examples and 0.17 for joint exposure/sequence search: expected 0.42. Joint all-project retraining remains fully lawful when prior data is available; it is included in the upper outcome, not excluded through an artificial sequential constraint. Its feasibility depends on lifetime token and generation costs that the original card leaves unmeasured.

Distribution R={0.24,0.46,0.68}, probabilities {0.30,0.57,0.13}. Outcomes reflect preserved tool behavior without transfer, useful conditional examples, and a successful joint-corpus or bridge solution. Mean=0.30×0.24+0.57×0.46+0.13×0.68=0.42, range 0.24–0.68. Bo4=0.68−0.22×0.87^4−0.22×0.30^4=0.55; p=0.13, pass4=1−0.87^4=0.43; ub95=0.68. Curriculum selection, discovering a discriminating condition and learner seed interference produce the spread. The old pass4 was too low relative to a meaningful successful-curriculum mode, while its upper percentile lacked a stated distribution.

## 4A. Demonstrated capability and subfield SOTA
Subfield comparator: Agent Lightning establishes practical agent weight training, and AgentCL provides a current dependency-sensitive memory evaluation. The latter is nonparametric and the former does not establish lifelong scientific transfer. No verified best human or system result matches this exact objective; therefore R≈1 cannot honestly be anchored to a published number. Planned native anchors are a lifetime-cost-matched joint corpus, an independently designed bridge curriculum and a stronger feasible conditional researcher, all UNMEASURED.

Two demonstrated results bound nearby capabilities. GLM-5.2/TrainExplorer on Claude Code reports 39.02 aggregate from ten-hour, single-80GB-GPU post-training of 1.7B–4B models. That establishes building learners, not training the experimenter. PaperBench's o1/IterativeAgent reaches 24.4% rubric credit in twelve hours with one A10; it executes supplied research methods rather than learning to retain them across parameter updates. Their outcomes cannot be multiplied to predict a self-training flywheel.

KNOWN-RECIPE: replay and retention. AGENT-DEMONSTRATED: bounded post-training and partial research execution. The complete attack's bridge-generation/causal-transfer capability is ASSUMED, so attack_basis=ASSUMED. In twelve hours the agent must locate genuine negative transfer, collect response contrasts, train the smaller researcher and establish that fresh-project improvements repay all earlier generation costs.

ANCHORED expected increments are 0.10 interference-aware replay, 0.09 bridge generation and 0.15 joint/sequence search. Use R={0.17,0.38,0.63}, masses {0.28,0.64,0.08}. Single=0.34, range 0.17–0.63; bo4=0.63−0.25×0.92^4−0.21×0.28^4=0.45; pass4=1−0.92^4=0.28; ub95=0.63. The successful outcome includes cheap joint retraining when it works. Its probability is an explicit forecast, not a measured rate; this verdict rests on assumption, particularly about headroom above joint exposure.

## 5. Verdict under the kill lines
Evidence re-estimate CONDITIONAL, with ESTIMATED bo4 only 0.05 below the line before rounding. ANCHORED PASS-SCREEN, FLIPPED CONDITIONAL→PASS-SCREEN: margins are ESTIMATED 0.36 single, 0.15 bo4, 0.22 pass4 and 0.12 ub95. The evidence gap is larger than the old discussion acknowledged: classification replay does not demonstrate curriculum construction for scientific reasoning, and current controlled-stream work cautions against that transfer. This is a screening hypothesis awaiting native calibration, not evidence that a future researcher has failed.

## 6. Redesign
NOT-NEEDED. Fresh interference relationships and independent old/new projects already target the unsupported capability, provided training sees lawful discriminating conditions rather than contradictory indistinguishable labels. Measure joint all-project training at identical lifetime exposure before asserting research reserve; if it reaches the stronger control, replace or cut the task instead of forbidding it. The proposed curriculum should earn value through executed novel projects, with matched replay and no-condition bridge ablations separating retention from causal transfer.

## 7. Measurement status
Rollouts UNMEASURED (planned independent curriculum generation and lifetime adaptation attempts). Grader noise UNMEASURED (planned repeated researcher-training seeds and fresh subject-model campaigns). Score ladder UNMEASURED (planned balanced replay, interference replay, conditioned bridges, joint retraining and independently attainable stronger research policy).

## Audit record
id: C127
old_verdict: CONDITIONAL
evidence_grade: ASSUMED
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.45
old_bo4: 0.56
old_pass4: 0.34
old_ub95: 0.73
new_single: 0.42
new_single_range: 0.24-0.68
new_bo4: 0.55
new_pass4: 0.43
new_ub95: 0.68
new_verdict: CONDITIONAL
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
attack_basis: ASSUMED
demonstrated_ref: TrainExplorer GLM-5.2 2026; PaperBench o1 IterativeAgent 2025
gap_to_attack: generating causal bridge curricula that improve a continually trained researcher
subfield_sota_ref: Agent Lightning Luo 2025; controlled AgentCL streams Shu 2026; matched SOTA unverified
anchored_single: 0.34
anchored_bo4: 0.45
anchored_pass4: 0.28
anchored_ub95: 0.63
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CONDITIONAL->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
