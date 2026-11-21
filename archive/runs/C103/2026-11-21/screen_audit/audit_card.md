# C103 — First build a privacy attack, then train a deletion method — screen audit
## 1. What the screen claimed
LiRA, extraction/relearning probes and robust unlearning formed the old evaluator/deletion loop. ESTIMATED single 0.46, bo4 0.56, pass@4 0.38 and ub95 0.72 supported CONDITIONAL, with no TSV kill category; complete retraining or clean-ancestor replay was an unresolved legal shortcut. The cited URLs were:
- https://arxiv.org/abs/2112.03570
- https://arxiv.org/abs/2408.10682
- https://proceedings.mlr.press/v267/fan25e.html

## 2. Evidence audit
LiRA supports powerful membership inference, not proof of relational counterfactual equivalence. The adversarial and relearning-resilient unlearning papers demonstrate useful attack/defense methods, but do not show an autonomous researcher constructing a calibrated evaluator and achieving this joint privacy/utility target within the card's budget. The distinction between confidential influence and legitimately re-derived knowledge remains load-bearing.

Grade: PARTIAL. There is genuine domain evidence for both sides of the loop, unlike a purely imagined attack. However, neither an attack-bank union nor low extraction accuracy establishes matching independently retrained behavior, and unresolved retraining economics prevent interpreting a low forecast as safe.

## 3. Research done now
- *Membership Inference Attacks From First Principles* — Nicholas Carlini et al., 2021, revised 2022 — https://arxiv.org/abs/2112.03570 — fetched — Strengthens probe calibration at low false-positive rates; membership detection does not identify all retained relational influence.
- *Towards Robust Knowledge Unlearning: An Adversarial Framework for Assessing and Improving Unlearning Robustness in Large Language Models* — Hongbang Yuan et al., 2024 — https://arxiv.org/abs/2408.10682 — fetched — Establishes adversarial recovery and defense as a practical floor, without a matching counterfactual-relations result.
- *Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond* — Chongyu Fan et al., 2025 — https://proceedings.mlr.press/v267/fan25e.html — fetched — Smoothing improves resistance on WMDP/MUSE; raises the robust control while leaving broad deletion equivalence open.
- *Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents* — Junkai Lin et al., 2026 — https://arxiv.org/html/2610.17659v1 — fetched — Memory/tool channels and retention losses complicate deletion. The agents are subjects of unlearning, not autonomous unlearning researchers.
- *Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness* — Haoting Qian et al., 2026 — https://arxiv.org/html/2608.04519v1 — fetched — Directly tests indirect reasoning and recovery, weakening confidence that ordinary probe success is sufficient.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — Provides a budget-comparable training-agent comparator; its objectives do not validate privacy evaluators.
- *PaperBench Science: expanding PaperBench into scientific domains* — Elvis Zhang Research/Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched — Incomplete scientific validation despite substantial execution cautions against assuming a working attack bank is a validated deletion instrument.

## 4. Re-estimated attack
Condition on a training history for which full clean replay does not fit the declared allowance. ESTIMATED sequential contributions are 0.12 from replacing the weak probe, 0.21 from robust deletion plus retained replay and 0.11 from strength/layer/early-stop selection: single 0.44. Evidence is strongest for detecting some hidden recovery and improving an existing defense; it is weakest for matching the retained-data counterfactual.

The ESTIMATED distribution has probability 0.20 at 0.24 when attacks remain weak or utility collapses, 0.65 at 0.44 for competent robust deletion, and 0.15 at 0.68 for successful evaluator-guided refinement. Single=0.44, range 0.24–0.68; bo4=0.24+0.20(1−0.20⁴)+0.24(1−0.85⁴)=0.55; pass@4=1−0.85⁴=0.48; ub95=0.68. The principal spread is discovering a probe that changes a useful deletion choice, followed by training stability. This slightly lowers the old mean/bo4 but raises repeated-run success under an explicit upper branch. Grader uncertainty and retraining-seed variance remain unknown.

Clean replay is a separate workload regime, not run-to-run luck. If a legal clean ancestor and retained replay fit, the above distribution is inapplicable: retraining is a direct counterfactual construction and the workload should CUT after measurement. No unsupported probability is assigned to which resource regime exists.

## 4A. Demonstrated capability and subfield SOTA
Fan et al.'s smoothness-enhanced methods are the strongest robust-deletion recipe family verified here; the newer multi-hop and agent-unlearning benchmarks expose dimensions they do not certify. No common privacy/utility ordering establishes a universal 2026 champion. The defensible north star is independently retrained retained-data behavior, with stochastic retraining variability measured, plus a feasible same-deployment-budget stronger deletion control. Its attainment is currently unverified.

TrainExplorer/GLM-5.2 achieves 39.02 aggregate in ten hours on one 80 GB flagship GPU. That demonstrates bounded post-training integration, but no privacy-probe calibration or counterfactual validation. PaperBench Science reports GPT-6 Astra at 59.08% partial and 13.98% full reproduction across tasks lasting four to twenty-four hours; scaffold and hardware are unspecified in the fetched report. Its validation gap matters because C103 needs evidence that a negative attack result is meaningful, not merely successful execution. Neither is a demonstrated unlearning-research attack. The 2026 agent-unlearning paper likewise cannot supply that missing autonomous result.

KNOWN-RECIPE is supported for attacks and robust updates; the complete loop is not AGENT-DEMONSTRATED here. attack_basis=LITERATURE-ONLY. An agent still must find independently useful attacks, preserve legitimate inferences and validate the joint utility/deletion tradeoff within twelve hours.

Under the non-replay regime, ANCHORED ESTIMATED masses 0.25 at 0.16, 0.65 at 0.37 and 0.10 at 0.64 give single 0.34, range 0.16–0.64; bo4=0.16+0.21(1−0.25⁴)+0.27(1−0.90⁴)=0.46; pass@4=0.34; ub95=0.64. Those margins would pass numerically, but transfer and resource assumptions remain decisive.

## 5. Verdict under the kill lines
Section 4 is CONDITIONAL, especially pass@4's ESTIMATED 0.02 clearance. The ANCHORED verdict remains CONDITIONAL, UNCHANGED: the non-replay forecast is below every line, but lawful counterfactual replay has not been costed out. This condition, rather than generic difficulty of unlearning, is the binding unresolved gate. New multi-hop evidence lowers confidence in easy robust deletion without resolving the shortcut.

## 6. Redesign
Class (a): complete retraining is a mature, potentially decisive replacement. REDESIGNABLE. Freeze the initial ancestor, retained-data access, complete cost ledger and the actual deletion allowance. Use a long training history where measured clean replay exceeds that allowance, while a legal stronger deletion control remains feasible. Include disclosed relational cases that are removable memorization and others re-derivable from retained evidence; counterfactuals decide which. Preserve full development access to equivalent relations, independent attacks and clean relearning checks. This changes the workload economics transparently rather than prohibiting a valid method.

LiRA plus extraction, smoothness-based unlearning and replay tuning now must distinguish harmful influence from valid reconstruction; suppression alone cannot win. The strongest re-attack adds relational attack generation and selected-layer updates. Its basis is LITERATURE-ONLY, with undiscovered cheap exact replay or weak independent attacks the main risks. Frontier labs need this deletion/retention capability, but the task survives only if the paired controls demonstrate it is feasible.

ESTIMATED redesign probabilities 0.30 at 0.14, 0.63 at 0.34, 0.07 at 0.61 imply single 0.30; bo4=0.14+0.20(1−0.30⁴)+0.27(1−0.93⁴)=0.41; pass@4=0.25; ub95=0.61. Decisive compute: ESTIMATED 4 deletion arms×2 seeds×4 H100-hours on 4B subjects=32; 2 controlled 1B histories×2 seeds×16 H100-hours=64; attack calibration 24 and retained/counterfactual evaluation 8: total 128 H100 GPU-h. This is a controlled-history falsification pilot, not full pretraining deletion certification.

## 7. Measurement status
Rollouts UNMEASURED (planned evaluator/deletion attacks plus a timed legal replay control). Grader noise UNMEASURED (planned independent retraining and probe-calibration seeds). Score ladder UNMEASURED (planned weak deletion, robust public methods, feasible reference and retained-data retraining with native utility distances).

## Audit record
id: C103
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.46
old_bo4: 0.56
old_pass4: 0.38
old_ub95: 0.72
new_single: 0.44
new_single_range: 0.24-0.68
new_bo4: 0.55
new_pass4: 0.48
new_ub95: 0.68
new_verdict: CONDITIONAL
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Fix replay economics and require independently validated relational deletion with a feasible retained-utility control.
redesign_single: 0.30
redesign_bo4: 0.41
redesign_pass4: 0.25
redesign_ub95: 0.61
redesign_gpuh: 128
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; PaperBench Science, GPT-6 Astra, 2026
gap_to_attack: autonomous privacy evaluator construction and counterfactual relational deletion
subfield_sota_ref: smoothness-enhanced robust unlearning, Fan et al., 2025; multi-hop comparator, Qian et al., 2026
anchored_single: 0.34
anchored_bo4: 0.46
anchored_pass4: 0.34
anchored_ub95: 0.64
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
