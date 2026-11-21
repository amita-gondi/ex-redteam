# C047 — Continue pretraining after a causal feature is deliberately removed — screen audit
## 1. What the screen claimed
The screen first tried all-layer feature readouts, then combined counterfactual examples, balanced sampling, visual-layer unfreezing, auxiliary relation losses and ordinary-image replay. It forecast ESTIMATED single=0.64, bo4=0.74, pass@4=0.81 and ub95=0.92, producing CUT, category TRAIN, because feature recovery might need only a strong established recipe. Sources cited:
- https://arxiv.org/abs/2210.11369
- https://arxiv.org/abs/2409.14637

## 2. Evidence audit
The feature-learning paper demonstrates that spurious classifiers can retain useful core representations. All-layer reweighting strengthens the cheap readout test, but neither establishes recovery of compositional image-text relations from a checkpoint lacking those features. The screen also assumes a suitable legal counterfactual corpus and successful retention-aware full recovery. Grade PARTIAL: the retained-feature branch is credible; its prevalence and the relearning branch were not demonstrated on a comparable VLM setup.

## 3. Research done now
All new reward values and allocation probabilities are ESTIMATED. Source benchmark outcomes are cited external results, and C047 itself remains unmeasured.
- On Feature Learning in the Presence of Spurious Correlations — Pavel Izmailov et al., 2022 — https://arxiv.org/abs/2210.11369 — fetched — Strong core-feature readouts despite shortcut reliance make watermark removal alone insufficient evidence of representational damage.
- Not Only the Last-Layer Features for Spurious Correlations: All Layer Deep Feature Reweighting — Humza Wajid Hameed et al., 2024 — https://arxiv.org/abs/2409.14637 — fetched — Features missing from the last layer can remain elsewhere, requiring a broader baseline than a failed final-layer probe.
- RaVL: Discovering and Mitigating Spurious Correlations in Fine-Tuned Vision-Language Models — Maya Varma et al., 2024 — https://proceedings.neurips.cc/paper_files/paper/2024/hash/95c6ae3f3393786203a4b6dcb9df1036-Abstract-Conference.html — fetched — Region-aware discovery and mitigation across many VLM configurations raise confidence in a targeted visual recovery floor, with classification rather than relational-generation evidence.
- Escaping the SpuriVerse: Can Large Vision-Language Models Generalize Beyond Seen Spurious Correlations? — Yiwei Yang et al., 2025 — https://arxiv.org/abs/2506.18322 — fetched — Synthetic counterfactual fine-tuning substantially improves shortcut-sensitive VQA. This is direct evidence against assuming that diverse shortcut failures require a novel recovery mechanism.
- Diagnosing the Sources of Compositional Failure in Vision-Language Models: A Controlled Analysis — Mona Gandhi et al., 2026 — https://arxiv.org/abs/2609.31456 — fetched — Primitive recognition, binding and relation load contribute separately. This lowers confidence that one generic relation loss addresses every residual failure.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern et al., 2024 — https://arxiv.org/html/2410.07095v1 — fetched — Familiar data/training recipes can be selected autonomously, but empirical recovery and validation failures remain common.
- PaperBench Science: expanding PaperBench into scientific domains — Elvis Zhang Research, Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched — Modern agents often execute an experiment without completing its scientific validation; a feature-loss claim needs that missing step.

## 4. Re-estimated attack
Run balanced all-layer probes before expensive updates. Where core visual information survives, retrain the readout; otherwise search counterfactual support, progressive unfreezing and retention replay jointly. On the provisional post-floor reward scale, credit ESTIMATED 0.16 to finding accessible features, 0.27 to counterfactual relearning and 0.14 to controlling ordinary-skill interference: 0.57. These increments cannot be identified from the cited benchmark accuracies; they are a task-specific decomposition contingent on the checkpoint family.

Literature-conditioned distribution: R={0.32,0.57,0.78}, probability={0.20,0.55,0.25}. The upper branch starts with recoverable core features and informative annotations; the low branch needs deeper relational relearning. Starting checkpoint, corpus design choices and optimizer seeds produce substantially more variance than an ordinary fixed readout fit. ESTIMATED mean=0.20×0.32+0.55×0.57+0.25×0.78=0.57, range 0.32–0.78; bo4=0.78−0.21×0.75^4−0.25×0.20^4=0.71; pass@4=1−0.75^4=0.68; ub95=0.78. This reduces the old point and tail because known-feature recovery and absent-feature reconstruction are distinct hypotheses.

## 4A. Demonstrated capability and subfield SOTA
Closest recovery anchor: SpuriVerse reports counterfactual fine-tuning reaching 78.40% accuracy, versus at most 37.1% among the evaluated unadapted closed models. RaVL reports an 8.2% improvement in worst-group image classification accuracy over its comparison, with broad VLM coverage. These are strong human-designed mitigation results, not proof of causal-feature reconstruction with general-skill retention. Anchor C047's reference to reproduced balanced/counterfactual and region-aware controls under identical exposure. No fetched source supplies a matched constrained R≈1 endpoint; the normalized reference remains open.

Agent evidence is indirect in two different ways. On MLE-bench, o1-preview with AIDE reached medal performance on 16.9% of tasks using twenty-four hours and an A10; it demonstrates training-pipeline selection, with longer time and no requirement to distinguish feature loss from readout bias. In Pipeline Lab's native scientific environments, GPT-6 Astra reached 13.98% complete reproduction, despite 59.08% partial credit, at task limits of four to twenty-four hours. The fetched account does not disclose each configuration's full scaffold or hardware ledger. Its relevance is causal verification after an apparently successful run, not VLM fine-tuning accuracy.

This attack has a KNOWN-RECIPE but no AGENT-DEMONSTRATED matched recovery campaign: attack_basis=LITERATURE-ONLY. The agent must locate the failure, construct legal support, select trainable layers and demonstrate retained ordinary capability within twelve hours. In particular, none of the agent results demonstrates an unaided diagnosis of absent relational representation.

ANCHORED scenarios R={0.28,0.49,0.67}, weights={0.20,0.66,0.14}: ESTIMATED single=0.47, range 0.28–0.67; bo4=0.67−0.18×0.86^4−0.21×0.20^4=0.57; pass@4=1−0.86^4=0.45; ub95=0.67. The probabilities explicitly assume a modest chance of validating the complete recovery; they are not borrowed from medal or reproduction rates. Verdict rests on assumption.

## 5. Verdict under the kill lines
Section 4 remains CUT. The ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL, with bo4 only 0.03 under its line and pass@4 approximately 0.05 under. SpuriVerse keeps a substantial recovery attack on the table; the absence of autonomous representation-diagnosis evidence prevents assigning the old high reliability. The condition is a demonstrated recovery problem after the full readout/counterfactual baseline, specified next.

## 6. Redesign
Cause (a), mature debiasing and fine-tuning stack; REDESIGNABLE. Assemble inherited checkpoint families with selective primitive deficits verified by several probes and direct visual interventions, rather than equating low answers with missing features. Allow a fixed pool of annotated decompositions, paired visual interventions and ordinary images. Reward improved learning of new causal relations after a recovery phase, with identical recovery bytes, optimization work and frozen downstream adaptation across methods.

Put all-layer readouts, region-aware losses, broad counterfactual tuning, full visual unfreezing and retention replay into the combined floor. A recovery policy must choose which primitive-support bridge improves subsequent composition learning, rather than merely erase a watermark readout. The best re-attack uses active curriculum selection plus layer-sensitive training; its remaining challenge is transferring from accessible primitive assays to new relation combinations. This is a useful frontier VLM data-design capability. A failed probe alone cannot certify lost information, and any universal clean-tuning solution invalidates the redesign.

Redesign basis LITERATURE-ONLY. ESTIMATED R={0.22,0.41,0.59}, masses={0.20,0.65,0.15}: single=0.40; bo4=0.59−0.18×0.85^4−0.19×0.20^4=0.50; pass@4=0.00; ub95=0.59. Pilot ESTIMATED 208 H100 GPU-h assumes available 3B VLM checkpoints: four recovery arms × two starting seeds × twenty hours × one H100=160, plus 32 intervention/retention evaluation and 16 probe GPU-h. Creating shortcut checkpoints is additional work and must be costed before scheduling the pilot.

## 7. Measurement status
Rollouts UNMEASURED (planned matched-exposure recovery with independent shortcut checkpoints). Grader noise UNMEASURED (planned paired renders, starting seeds and recovery repeats). Score ladder UNMEASURED (planned all-layer readout, complete recovery floor, bridge selector and stronger feasible learner).

## Audit record
id: C047
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.64
old_bo4: 0.74
old_pass4: 0.81
old_ub95: 0.92
new_single: 0.57
new_single_range: 0.32-0.78
new_bo4: 0.71
new_pass4: 0.68
new_ub95: 0.78
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Score transferable primitive-support recovery beyond complete counterfactual tuning and all-layer readout controls.
redesign_single: 0.40
redesign_bo4: 0.50
redesign_pass4: 0.00
redesign_ub95: 0.59
redesign_gpuh: 208
attack_basis: LITERATURE-ONLY
demonstrated_ref: MLE-bench, o1-preview AIDE, 2024; PaperBench Science, GPT-6 Astra, 2026
gap_to_attack: No demonstrated absent-feature diagnosis and retained-skill VLM recovery
subfield_sota_ref: SpuriVerse fine-tuning, Yang, 2025; RaVL, Varma, 2024
anchored_single: 0.47
anchored_bo4: 0.57
anchored_pass4: 0.45
anchored_ub95: 0.67
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
