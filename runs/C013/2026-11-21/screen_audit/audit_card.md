# C013 — Build an evaluator that prices research reversibility — screen audit
## 1. What the screen claimed
The old screen proposed a state inventory, cold-restoration probes, hazard estimation and terminal-quality prediction, then rejected the evaluator task as standard experimental design (EXP). Its ESTIMATED single/bo4/pass@4/ub95 were 0.74/0.82/0.94/0.95, with CUT because actual cold continuations directly test the desired recoverability. It cited these implementation and checkpointing sources:
- https://docs.pytorch.org/docs/stable/distributed.checkpoint.html
- https://www.usenix.org/conference/fast21/presentation/mohan
## 2. Evidence audit
Distributed Checkpoint and CheckFreq support building recovery probes. Neither evaluates recipe selection by later model quality: restoring state does not show that a short continuation predicts long-horizon loss after another interruption.

Probe allocation, hazard inference and learning-curve extrapolation carry the unsupported portion. Grade: PARTIAL. Undefined probe opportunity cost makes direct testing a vulnerability; API documentation does not demonstrate the complete selector.
## 3. Research done now
- Distributed Checkpoint — PyTorch, 2026 documentation as accessed — https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html — fetched — The screen URL redirects here; persistence and resharding help construct cold tests but do not rank scientific value automatically.
- CheckFreq: Frequent, Fine-Grained DNN Checkpointing — Jayashree Mohan et al., 2021 — https://www.usenix.org/conference/fast21/presentation/mohan — fetched — A concrete checkpointing system makes instrumentation feasible, raising confidence in the routine state-audit portion.
- DataStates-LLM: Lazy Asynchronous Checkpointing for Large Language Models — Avinash Maurya et al., 2024 — https://arxiv.org/abs/2406.10707 — fetched — Demonstrates large-model asynchronous state capture, strengthening the baseline's realism while exposing overlap and consistency concerns beyond checkpoint file existence.
- Check-N-Run: a Checkpointing System for Training Deep Learning Recommendation Models — Assaf Eisenman et al., 2022 — https://www.usenix.org/conference/nsdi22/presentation/eisenman — fetched — Production recovery engineering supports measuring actual continuations; recommendation-state compression results cannot establish a selector's quality on arbitrary research graphs.
- ByteCheckpoint: A Unified Checkpointing System for Large Foundation Model Development — Borui Wan et al., 2025 — https://www.usenix.org/system/files/nsdi25-wan-borui.pdf — fetched — Cross-stage, cross-parallelism checkpoint handling strengthens a sophisticated cold-restart attack. Its demonstrated state-management objective differs from forecasting resumed learning, a useful limit on the saturation claim.

Searches targeted current training-recovery systems and exact restart state. None of these papers was found to report the complete recipe-ranking capability at this card's objective, so the new systems results are component support only.
## 4. Re-estimated attack
The following quantities are ESTIMATED, including the normalized score decomposition. State inventory and immediate cold tests recover about 0.34 by eliminating non-resuming recipes. Phase-stratified probes add 0.20 through detection of sampler/scheduler dependencies. A charged learning-curve predictor and conservative selector add 0.11; interactions prevent summing independent headline speedups. Remaining loss comes from delayed divergence and probe transfer across recovery graphs.

Model full attempts as R=0.43 with probability 0.20, R=0.67 with probability 0.60, and R=0.82 with probability 0.20. These correspond to late-failure mismatch, successful routine diagnosis, and well-allocated longer probes. Variation comes mainly from experiment placement rather than kernel randomness; training-seed variation is included in the scenario uncertainty, with grader noise still unknown. ESTIMATED single=0.20×0.43+0.60×0.67+0.20×0.82=0.65, range 0.43–0.82. ESTIMATED bo4=0.43×0.20^4+0.67×(0.80^4−0.20^4)+0.82×(1−0.80^4)=0.76. ESTIMATED p=0.80 gives pass@4=1−0.20^4=1.00 rounded. ESTIMATED ub95=0.82, since the CDF at 0.67 is 0.80.

Missing long-run validation lowers the old mean/tail, while direct cold testing preserves repeated success. Attempts are conditionally independent; shared graph difficulty needs separate blocks. This percentile is no measured scaling projection.
## 4A. Demonstrated capability and subfield SOTA
ByteCheckpoint (Wan, 2025, fetched) is the closest current industrial recovery anchor: it demonstrates efficient checkpoint resharding across training configurations. DataStates-LLM supplies another large-scale checkpoint frontier. Their native target is reliable useful training after restoration, which should anchor this task's attainable control; neither supplies a SOTA recipe-value selector or numeric R≈1 anchor. Until recovered loss and total restart cost are measured jointly, the reference remains a target capability, not a calibrated score.

- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-used-to-assess-high-ai-self-improvement-capabilities — fetched: Astra's evaluation agent earns reported 81.85% rubric credit for research debugging, including experiment failures. Per-task runtime, hardware and full scaffold are unreported there. Diagnosis is relevant to state inventories; autonomous cold recovery and later-quality ranking are not established.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched: o1 with IterativeAgent obtains reported 24.4% replication credit using twelve hours and a single A10. Execution and persistence are part of reproducing experiments, but this is no test of ranking recoverable learning value under interruptions.

KNOWN-RECIPE state capture and cold probing are real; AGENT-DEMONSTRATED long-horizon recovery selection is missing. attack_basis=LITERATURE-ONLY. The extra work is designing informative interruption probes, validating all cold dependencies and forecasting resumed loss before the twelve-hour window closes. The anchored judgment therefore rests on an integration assumption.

ANCHORED ESTIMATED R=0.30/0.48/0.70 with probabilities 0.32/0.56/0.12, representing incomplete cold diagnosis, working but short-sighted selection and successful long-horizon discrimination. ESTIMATED single=0.32×0.30+0.56×0.48+0.12×0.70=0.45, range 0.30–0.70; bo4=0.30×0.32^4+0.48×(0.88^4−0.32^4)+0.70×(1−0.88^4)=0.57; pass@4=1−0.88^4=0.40; ub95=0.70. The larger integration failure mass replaces section 4's assumption that direct tests generally expose the decisive scientific dependency.
## 5. Verdict under the kill lines
Evidence re-estimate: CUT under section 4's recipe-success assumption. ANCHORED headline: CONDITIONAL, FLIPPED CUT→CONDITIONAL. ESTIMATED bo4 clears by 0.03 and ub95 by 0.05; no numeric kill is established by the new forecast. Research-debugging evidence is encouraging but lacks cold-recovery selection outcomes, so the required condition is a charged-probe pilot with a measured ByteCheckpoint-class native frontier.
## 6. Redesign
Potential cause (b) is underpriced testing. The anchored condition requires this REDESIGNABLE charged-probe contract; re-attack basis=LITERATURE-ONLY, with forecast stress assuming competent implementation.

Supply real recipes with asynchronous data preparation, optimizer schedules and transport dependencies, observable traces and migration code. Dev represents resource-layout and data-stage interruptions. The evaluator purchases cold probes before selecting a recipe, charging them against final training time; recovered held-out loss is the utility. Allow several short or fewer long tests. Exhaustive author continuations and a feasible adaptive control must show affordable distinguishing evidence.

The strongest attack combines dependency parsing, ordinary cold tests, ByteCheckpoint-aware load probes, multi-fidelity curve fitting and Bayesian value-of-information allocation. It stops being nearly free to test every recipe to completion. The unsolved part is learning which state transition makes a cheap continuation unrepresentative while pricing that uncertainty against useful training. This remains useful research infrastructure for frontier jobs. Its major residual risk is that one successful restart plus a static conservative penalty orders every recipe correctly; that is a decisive rejection criterion.

ESTIMATED redesign outcomes are 0.32/0.50/0.69 with probabilities 0.40/0.50/0.10 for misleading short probes, useful partial ranking and an effective adaptive schedule. ESTIMATED single=0.40×0.32+0.50×0.50+0.10×0.69=0.45; bo4=0.32×0.40^4+0.50×(0.90^4−0.40^4)+0.69×(1−0.90^4)=0.56; pass@4=1−0.90^4=0.34; ub95=0.69. This is CONDITIONAL, with bo4 clearance only 0.04, requiring the concrete charged-probe contract rather than an unexplained tightening of limits.

ESTIMATED pilot uses a 1B learner: 4 recipes × 3 seeds × 3 interruption phases × 4 hours × 1 H100=144 GPU-h. Evaluator probe campaigns add ESTIMATED 24 and evaluation adds 12, totaling 180 H100 GPU-h. Stored author outcomes may compare selectors offline, but each selector is charged the probes it requests.
## 7. Measurement status
Rollouts UNMEASURED (planned independent adaptive evaluators on fresh recovery graphs). Grader noise UNMEASURED (planned repeated cold restarts from identical durable snapshots). Score ladder UNMEASURED (planned final-loss ranking through full cold-probe selection and a feasible recovery-aware control).
All score entries and proposed GPU-hours below are ESTIMATED; source counts are audit facts.
## Audit record
id: C013
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.74
old_bo4: 0.82
old_pass4: 0.94
old_ub95: 0.95
new_single: 0.65
new_single_range: 0.43-0.82
new_bo4: 0.76
new_pass4: 1.00
new_ub95: 0.82
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Charge adaptive cold probes against final useful training and evaluate selection across disclosed state-transition mechanisms.
redesign_single: 0.45
redesign_bo4: 0.56
redesign_pass4: 0.34
redesign_ub95: 0.69
redesign_gpuh: 180
attack_basis: LITERATURE-ONLY
demonstrated_ref: Research Debugging, GPT-6.2 Astra, 2026; PaperBench, o1 IterativeAgent, 2025
gap_to_attack: cold interruption probes that predict resumed model value
subfield_sota_ref: large-foundation-model checkpoint resharding, ByteCheckpoint, 2025
anchored_single: 0.45
anchored_bo4: 0.57
anchored_pass4: 0.40
anchored_ub95: 0.70
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
