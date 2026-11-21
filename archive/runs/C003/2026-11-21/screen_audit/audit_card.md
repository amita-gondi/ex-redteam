# C003 — Repair image-caption pair selection after OCR shortcut learning — screen audit
## 1. What the screen claimed
The screen selected complementary geometry examples with matched language, balanced relations and retained examples needing text for entity identification. Its ESTIMATED single/bo4/pass@4/ub95 were 0.72/0.80/0.93/0.93, yielding CUT under DATA because complementary selection appeared to remove the OCR shortcut. It cited:
- https://arxiv.org/abs/1612.00837
- https://www.ijcai.org/proceedings/2020/151

## 2. Evidence audit
Making the V in VQA Matter — Yash Goyal, 2016, revised 2017, fetched at the first URL — establishes complementary-image balancing and exposes language-prior dependence. It does not demonstrate that balancing alone trains a spatially competent modern VLM. Overcoming Language Priors with Self-supervised Learning for Visual Question Answering — Xi Zhu, 2020, fetched at the second URL — combines generated balancing examples with an auxiliary learning objective. C003 authorizes selecting existing pairs, so its reported success cannot be transferred wholesale.

Grade: PARTIAL. Both references establish a sensible bias-removal direction, but the old attack also needs correct geometric annotations, availability of useful complementary pairs and learned transfer while preserving OCR. The original sources do not jointly validate those requirements at the proposed model scale. The IJCAI citation especially overstates what a selection-only artifact can inherit from a training-method result.

## 3. Research done now
- Sparkle: Mastering Basic Spatial Capabilities in Vision Language Models Elicits Generalization to Spatial Reasoning — Yihong Tang, 2025 — https://aclanthology.org/2025.findings-emnlp.217/ — fetched — Targeted synthetic supervision improves basic and composed spatial tasks. This raises the attack by showing data interventions can teach useful geometry, but it adds supervision rather than merely selecting a fixed pool.
- GSR-BENCH: A Benchmark for Grounded Spatial Reasoning Evaluation via Multimodal LLMs — Navid Rajabi, 2024 — https://arxiv.org/abs/2406.13246 — fetched — Separates object localization from relation understanding across multimodal models. It makes an off-the-shelf scene-graph extractor an uncertain selector, lowering confidence in automatic labeling without checks.
- SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language Models — Hongxing Li, 2026 — https://arxiv.org/abs/2610.12402 — fetched — Reports gains from programmatically generated spatial training data alongside remaining predictive-reasoning failures. The training result strengthens the data route; failures on unobserved transformations do not directly protect C003's visible static tuples.
- What If the TV Was Off? Examining Counterfactual Reasoning Abilities of Multi-modal Language Models — Letian Zhang, 2023/2024 — https://arxiv.org/abs/2310.06627 — fetched — Counterfactual questions expose robustness failures, providing negative transfer evidence. The successful arXiv fetch replaces inaccessible CVPR links; hypothetical scene edits differ from C003's observed geometric edits.

Search covered spatial selection and counterfactual training. Evidence supports targeted supervision, leaving the equal-pool selection/retention combination unresolved.

## 4. Re-estimated attack
ESTIMATED incremental credits: complementary-pair coverage 0.32, visually checked relation balance 0.19, and text/object grounding quotas 0.12, totaling 0.63. Missing pairs, geometric annotation errors and slow unlearning of OCR dependence limit transfer. Published accuracy gains do not fix this provisional reward scale.

ESTIMATED R={0.45,0.59,0.82}, masses {0.20,0.50,0.30}, describe text-only balance, competent geometry/grounding coverage and successful transfer of their joint partition. Development selection and retraining seeds cause variation. Matched renderers help; run variance is unmeasured.

The implied ESTIMATED single is 0.20×0.45+0.50×0.59+0.30×0.82=0.63, range 0.45–0.82. Conditional on the same instance family and independent restarts, ESTIMATED bo4=0.82−0.23×0.70^4−0.14×0.20^4=0.76. Here p=0.30, so ESTIMATED pass@4=1−0.70^4=0.76. With cumulative mass 0.70 below the high outcome, ESTIMATED ub95=0.82. These scenario calculations include no empirical confidence guarantee or separate stronger-tier scaling fit.

The old point falls because positive papers change supervision beyond selection; simple diagrams still permit occasional highly transferable subsets.

## 4A. Demonstrated capability and subfield SOTA
The strongest recent task-adjacent result consulted is SpaceCast-Bench (Li, 2026, fetched above): targeted data fine-tuning raises Qwen3-VL-4B's reported predictive-spatial accuracy from 34.0% to 65.7%, with external transfer checks. Sparkle supplies a closer two-dimensional training mechanism. Neither is a fixed-pool selector maintaining OCR. Set the reference target using this demonstrated possibility of learned spatial improvement, then measure the actual selector ceiling on matched diagrams; R≈1 cannot be equated with either paper's accuracy.

- MLE-bench — Chan Jun Shern, 2024 — https://arxiv.org/html/2410.07095v1 — fetched. AIDE/o1-preview's reported 16.9% medal rate uses one A10 and twenty-four hours. It supports autonomous data preparation and model comparison; no result establishes image-pair balancing with simultaneous text-grounding retention in half that time.
- PaperBench — Giulio Starace, 2025 — https://arxiv.org/html/2504.01848v1 — fetched. o1/IterativeAgent reaches reported 24.4% reproduction credit with twelve hours on one A10. It demonstrates partial integration, but complete spatial selection plus retraining/retention validation exceeds what that aggregate establishes.

Basis LITERATURE-ONLY: complementary-data design is KNOWN-RECIPE; the end-to-end selector is not AGENT-DEMONSTRATED. The agent must determine available pair support, trust geometric labels selectively and validate learned retention, rather than import synthetic-supervision results unchanged.

ANCHORED ESTIMATED R={0.33,0.52,0.69}, masses {0.32,0.56,0.12}. These reflect incomplete spatial annotation, useful selection and successful transfer auditing. Single=0.32×0.33+0.56×0.52+0.12×0.69=0.48, range 0.33–0.69; bo4=0.69−0.17×0.88^4−0.19×0.32^4=0.59; pass@4=1−0.88^4=0.40; ub95=0.69 because CDF before it is 0.88. Research integration causes the spread; blockwise independence and reward conversion are assumptions.

## 5. Verdict under the kill lines
The recipe-only evidence estimate in section 4 is CUT, ESTIMATED bo4 0.16 above its line. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL, with ESTIMATED bo4 0.01 below the boundary and ub95 0.06 below its limit. Spatial supervision has demonstrated gains, but neither fetched agent evaluation demonstrates this selection-only transfer. The judgment rests on assumption; surviving requires the role-binding revision and native ceiling check below.

## 6. Redesign
The anchored survival condition below has LITERATURE-ONLY re-attack support for binding-aware acquisition.
Cause (a), specifically mature bias-aware data selection. Start with a corpus already balanced for text-only predictability and individual spatial relations. Give the selector an existing pool of diagrams where printed aliases identify entities through legends, and geometry determines relations among the bound entities. Cross alias resolution, distractor structure and relation composition independently. Keep every required legend readable; provide analogous crossings in development. Evaluate held-out role-binding compositions with tuple accuracy, OCR and object identity under equal selected tokens and training work.

Selection must jointly teach textual binding and geometry. Relation quotas, caption balancing and OCR confidence cannot identify which combinations repair the learner's binding error. The strongest legal alternative uses OCR, layout parsing, entity-link graphs, error-conditioned subset selection and low-fidelity continuation search. That recipe still earns substantial reward; it falls short if examples helpful for one binding stage interfere with another and the best subset depends on joint learning effects. A reference must demonstrate this interaction rather than assuming unfamiliar aliases create hardness.

ESTIMATED redesign states {0.27,0.46,0.66}, masses {0.40,0.52,0.08}, represent marginal quotas, binding-aware selection and transferable interaction discovery. Single=0.40×0.27+0.52×0.46+0.08×0.66=0.40; bo4=0.66−0.20×0.92^4−0.19×0.40^4=0.51; pass@4=1−0.92^4=0.28; ub95=0.66. REDESIGNABLE, with 0.09 bo4 margin. A canonical-graph parser remains a decisive shortcut control.

Decisive-check GPU-h ESTIMATED: a 3B VLM, five selectors, three training seeds, sixteen H100-hours per continuation, and thirty-six H100-hours for pool feature extraction and tuple/OCR/identity evaluation gives 5×3×16+36=276. This comparison tests the interaction hypothesis at useful model scale; a later saturation panel needs its own budget. The redesign remains acquisition research of interest to multimodal pretraining teams, rather than a general puzzle-solving benchmark.

## 7. Measurement status
Rollouts UNMEASURED (planned selection-code attacks with fixed source-pool access). Grader noise UNMEASURED (planned paired VLM retraining across label-preserving geometric edits). Score ladder UNMEASURED (planned OCR ranking, complementary quotas, canonical-graph selection, binding-aware reference and stronger corpus control).

## Audit record
id: C003
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 8
old_single: 0.72
old_bo4: 0.80
old_pass4: 0.93
old_ub95: 0.93
new_single: 0.63
new_single_range: 0.45-0.82
new_bo4: 0.76
new_pass4: 0.76
new_ub95: 0.82
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Select training pairs for interacting text-to-entity binding and geometric composition after marginal bias balancing is supplied.
redesign_single: 0.40
redesign_bo4: 0.51
redesign_pass4: 0.28
redesign_ub95: 0.66
redesign_gpuh: 276
attack_basis: LITERATURE-ONLY
demonstrated_ref: MLE-bench, o1-preview AIDE, 2024; PaperBench, o1 IterativeAgent, 2025
gap_to_attack: Validate geometry-selective training without losing legitimate text grounding
subfield_sota_ref: Spatial-data fine-tuning of Qwen3-VL-4B, Li SpaceCast-Bench, 2026
anchored_single: 0.48
anchored_bo4: 0.59
anchored_pass4: 0.40
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
