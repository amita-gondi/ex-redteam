# C042 — Pretrain conditional computation with delayed expert utility — screen audit
## 1. What the screen claimed
The previous screen proposed stable sparse training, loss-free balancing, expert warmup, rare-task replay and composition probes. It reported ESTIMATED single=0.49, bo4=0.58, pass@4=0.41 and ub95=0.73, retaining CONDITIONAL status without a populated kill category. Survival depended on selective precursor retention under a binding capacity constraint. Its cited URLs were:
- https://arxiv.org/abs/2202.08906
- https://arxiv.org/abs/2408.15664

## 2. Evidence audit
ST-MoE establishes training stability and downstream transfer, while loss-free balancing supplies model-scale evidence for removing auxiliary-gradient interference. Neither demonstrates the choice of initially unhelpful specialists whose joint benefit appears much later. Rare-task replay, useful complementarity estimation and scarce-capacity selection were not backed by matched experiments in the screen. PARTIAL is the appropriate grade: the stable-training base is supported, but the research difficulty lies beyond balancing loads.

## 3. Research done now
Every C042 score, probability allocation and future resource allowance is ESTIMATED, including numeric fields in the record.
- ST-MoE: Designing Stable and Transferable Sparse Expert Models — Barret Zoph et al., 2022 — https://arxiv.org/abs/2202.08906 — fetched — Successful large sparse transfer makes router instability an inadequate hardness argument for this task.
- Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts — Lean Wang et al., 2024 — https://arxiv.org/abs/2408.15664 — fetched — Tests extending to 3B parameters strengthen the lawful alternative to a destructive uniform auxiliary objective.
- Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation — Junzhuo Li et al., 2025 — https://aclanthology.org/2025.emnlp-main.932/ — fetched — Adaptive routing, domain-gradient separation and staged freezing preserve competence across domains. This raises the rehearsal attack, but retaining known domains is different from selecting future complementary precursors.
- Sparse Mixture-of-Experts for Compositional Generalization: Empirical Evidence and Theoretical Foundations of Optimal Sparsity — Jinze Zhao et al., 2026 — https://proceedings.mlr.press/v328/zhao26b.html — fetched — SRAVEN and SKILL-MIX results connect activation needs to composition complexity. The card must meter activated work rather than give a free increase in expert count.
- The Myth of Expert Specialization in MoEs: Why Routing Reflects Geometry, Not Necessarily Domain Expertise — Xi Wang et al., 2026 — https://arxiv.org/abs/2604.09780 — fetched — Observed routing similarity does not reliably identify semantic expertise, weakening the proposed complementarity diagnostic.
- PaperBench Science: expanding PaperBench into scientific domains — Elvis Zhang Research, Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched — The validation deficit matters when an apparent routing improvement must be shown to cause later useful composition.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — Post-training agents can select data and update policies at relevant subject sizes; no reported task has C042's delayed utility structure.

## 4. Re-estimated attack
The full attack jointly tunes load-control biases, warmup, rehearsal proportions, freezing and composition-based selection. Above a competent sparse/replay floor, assign ESTIMATED 0.10 to less destructive routing pressure, 0.19 to maintaining candidate feature diversity, and 0.16 to using early composition probes: 0.45 in total. This provisional decomposition discounts any ordinary stability repair already present in calibration. The remaining gain requires predicting which specialists justify their future storage and update opportunity cost.

Use a discrete single-run scenario distribution: scores {0.25,0.47,0.69}, probabilities {0.25,0.60,0.15}. Modes represent misleading router diagnostics, effective broad retention and successful complementarity inference. Curriculum/training seeds and probe selection jointly drive spread. Mean=0.25×0.25+0.60×0.47+0.15×0.69=0.45, range 0.25–0.69. Independent best-of-four expectation=0.69−0.22×0.85^4−0.22×0.25^4=0.57; pass@4=1−0.85^4=0.48; ub95=0.69. The old tail of 0.73 had no stated generating distribution; the new distribution exposes exactly what a successful specialist-selection branch assumes.

## 4A. Demonstrated capability and subfield SOTA
The closest current subfield reference combines Li's multi-domain preservation result with Zhao's demonstrated composition/activation tradeoff. Neither establishes an optimum for delayed expert selection at the same active and stored parameter budgets. Anchor the reference to these reproduced controls, then require an informed capacity-matched policy to demonstrate the stronger end of the reward scale. R≈1 is presently unanchored, not a claim that balancing alone reaches a known ceiling.

OpenAI's GPT-6.2 Astra obtained 74.79% gap closure on PostTrainBench Lite using five hours and one H100, with its internal agent scaffold not fully disclosed. That shows practical update-policy selection, but the tasks use dense 1.7B–4B base models and immediate benchmark feedback. Pipeline Lab's GPT-6 Astra configuration obtained 59.08% partial and 13.98% full reproduction on science tasks with four-to-twenty-four-hour budgets, median seven; per-task hardware and detailed scaffold compute are not reported on the fetched page. Its weak closure of scientific validation cautions against inferring delayed complementarity from a routing plot. Neither score is a C042 success frequency.

This is KNOWN-RECIPE sparse preservation, not AGENT-DEMONSTRATED delayed expert selection: attack_basis=LITERATURE-ONLY. Twelve hours must cover causal probes, scarce-capacity decisions and a complete delayed-outcome replay, a combination absent from the retrieved agent results.

ANCHORED outcomes {0.23,0.44,0.66} receive probabilities {0.25,0.61,0.14}. ESTIMATED single=0.42, range 0.23–0.66; bo4=0.66−0.22×0.86^4−0.21×0.25^4=0.54; pass@4=1−0.86^4=0.45; ub95=0.66. Lower successful-selection credit reflects the diagnostic gap. Verdict rests on assumption, especially the unverified retention bottleneck.

## 5. Verdict under the kill lines
Both the section-4 forecast and ANCHORED assessment are CONDITIONAL; UNCHANGED versus the old verdict. Anchored bo4 is 0.06 below its line, pass@4 is approximately 0.05 below its line before rounding, and the percentile is 0.09 below its limit. Current preservation methods strengthen the baseline while the specialization evidence weakens simplistic expert-selection claims. These near margins do not resolve whether preserve-all rehearsal succeeds.

## 6. Redesign
Class (a), mature sparse-training stack; REDESIGNABLE through a concrete condition. Construct observable curricula with interchangeable early specialists competing for finite update capacity, followed by compositions whose useful precursor differs across semantic families. Give dev the same causal diagnostic access as evaluation, including legal short composition probes. Validate that the whole combination of loss-free balancing, adaptive rehearsal, domain-aware freezing and probe search cannot keep every precursor, while a capacity-matched informed learner achieves the stronger control. This changes the learning decision rather than concealing the relevant future mechanism.

The best re-attack learns a predictive influence model and spends probes to identify high-value specialists. It falls short only if the validated interaction demands generalization beyond marginal routing statistics; uniform retention must remain legal. The capability is valuable for allocating large sparse-model training compute. Risk remains that ordinary replay plus staged freezing solves all families; that would remove the proposed research headroom.

Re-attack basis LITERATURE-ONLY. ESTIMATED distribution {0.21,0.39,0.56} with masses {0.20,0.65,0.15}: single=0.38, bo4=0.56−0.17×0.85^4−0.18×0.20^4=0.47, pass@4=0.00, ub95=0.56. Decisive pilot ESTIMATED 368 H100 GPU-h: 1.2B total/0.3B active subject, four policies × three curriculum seeds × twenty-four hours × one H100=288, plus 48 evaluation and 32 capacity-probe GPU-h. No GPU work was launched.

## 7. Measurement status
Rollouts UNMEASURED (planned full precursor/composition training with preserved all-state budgets). Grader noise UNMEASURED (planned independent router seeds and fixed composition evaluation). Score ladder UNMEASURED (planned stable MoE, combined preservation stack, causal selector and informed feasible control).

## Audit record
id: C042
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.49
old_bo4: 0.58
old_pass4: 0.41
old_ub95: 0.73
new_single: 0.45
new_single_range: 0.25-0.69
new_bo4: 0.57
new_pass4: 0.48
new_ub95: 0.69
new_verdict: CONDITIONAL
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Validate probe-identifiable complementary precursors that compete under a feasible fixed retention capacity.
redesign_single: 0.38
redesign_bo4: 0.47
redesign_pass4: 0.00
redesign_ub95: 0.56
redesign_gpuh: 368
attack_basis: LITERATURE-ONLY
demonstrated_ref: PostTrainBench Lite, GPT-6.2 Astra, 2026; PaperBench Science, GPT-6 Astra, 2026
gap_to_attack: No autonomous delayed complementary-expert selection result
subfield_sota_ref: DES-MoE, Li, 2025; compositional sparsity, Zhao, 2026
anchored_single: 0.42
anchored_bo4: 0.54
anchored_pass4: 0.45
anchored_ub95: 0.66
anchored_verdict: CONDITIONAL
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
