# C057 — Search across a corpus whose experiments have different resource contracts — screen audit
## 1. What the screen claimed
The screen proposed typed extraction of resource contracts, conservative feasibility filtering, deployment-specific Pareto frontiers and BOHB/cost-aware pilot allocation. Its ESTIMATED single/bo4/pass@4/ub95 were 0.82/0.89/0.99/0.98; CUT, category EXP, because those steps appeared to directly repair the inherited failure. Old URLs:
- https://proceedings.mlr.press/v80/falkner18a.html
- https://arxiv.org/abs/2211.02732

## 2. Evidence audit
BOHB supports efficient hyperparameter search with resource allocation, not extracting complete preparation and memory dependencies from papers. Multi-fidelity cost-aware BO depends on useful relationships between information sources; it does not establish that unrelated literature results preserve ranking after deployment adaptation. Neither citation demonstrates producing a corpus that causes a different fixed researcher to choose and execute the right recipe.

Grade: PARTIAL. Feasibility rejection is well motivated and likely accessible. The load-bearing claim that it recovers nearly all normalized utility is unsupported without measuring the feasible candidates' learning quality and the corpus-to-agent transfer. The screen also gave pilot execution capabilities to a data artifact without freezing how those receipts become available.

## 3. Research done now
Numerical forecasts and proposed experiment costs are ESTIMATED; source benchmark results are historical observations with different denominators.
- BOHB: Robust and Efficient Hyperparameter Optimization at Scale — Stefan Falkner et al., 2018 — https://proceedings.mlr.press/v80/falkner18a.html — fetched — makes multi-fidelity recipe trials credible, but does not solve cross-report contract interpretation.
- Multi-Fidelity Cost-Aware Bayesian Optimization — Zahra Zanjani Foumani et al., 2022 preprint, 2023 publication — https://arxiv.org/abs/2211.02732 — fetched — supports cost-sensitive information allocation; correlation assumptions may fail after batch or precision changes.
- TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — demonstrates complete bounded training campaigns and strategy changes, raising the credible feasibility-and-selection attack.
- PaperBench Science: expanding PaperBench into scientific domains — Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched — frequent validation failures after substantial implementation progress lower confidence in extrapolated scientific recipes.
- AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure — Megan Kinniment et al., METR, 2026 — https://metr.org/blog/2026-11-20-q4-2026-capability-update/ — fetched — resource-rich optimization is demonstrably useful, but long runs do not automatically close the best-human gap or validate a curated corpus.

## 4. Re-estimated attack
The strongest lawful construction retains uncertainty in source contracts, estimates full persistent and transient costs, and presents executable feasible variants to the fixed agent. When the data-artifact contract permits acquiring real pilots, charge those pilots to corpus preparation. Otherwise the attack must use supplied receipts rather than silently adding another controller.

A successful combined recipe plausibly recovers ESTIMATED 0.26 through eliminating impossible methods, 0.23 through choosing among feasible Pareto candidates and 0.21 through validating a scaled variant: total ESTIMATED 0.70. These are proposed increments in normalized downstream gain, not extraction accuracy. Failed adaptation and unmodeled setup costs remain substantial. Typed extraction and simple capacity checks already included in the floor reduce the marginal opportunity.

Use ESTIMATED outcomes 0.47/0.70/0.83 with probabilities 0.13/0.69/0.18. Contract checks are mostly mechanical once the recipe is integrated, making the competent mode dominant; cross-scale learning transfer creates the upper tail. ESTIMATED single=0.13×0.47+0.69×0.70+0.18×0.83=0.69, range 0.47–0.83; ESTIMATED bo4=0.47+0.23(1−0.13^4)+0.13(1−0.82^4)=0.77. With ESTIMATED p=0.87, pass@4=1−0.13^4=1.00; ESTIMATED ub95=0.83. This remains below the old mean because paper extraction does not guarantee executable learning quality.

## 4A. Demonstrated capability and subfield SOTA
The nearest measured bounded-training comparator is TrainExplorer/GLM-5.2: its weighted post-training aggregate is 39.02 against 31.70 for the same model in Claude Code, with official instruct models at 51.14 under a different development budget. This is relevant SOTA among the fetched agentic recipe-selection comparisons, not a best corpus-curation score. A north-star control must demonstrate successful adaptation within C057's envelope; importing official instruct quality as R=1 would violate the resource contract.

Demonstration one: TrainExplorer runs planning, data preparation, training and evaluation within ten hours on one 80GB flagship GPU per configuration. It demonstrates selecting feasible learning changes from a real budget, but its autonomous scaffold directly controls experiments; C057 modifies only evidence consumed by a frozen agent. Demonstration two: PaperBench Science's GPT-6 Astra reaches 59.08% partial credit but 13.98% full reproduction over scientific tasks with varying limits. Its reported hardware/scaffold detail does not establish a matched twelve-hour budget; the relevant lesson is the gap between executing most of a workflow and validating its claim.

KNOWN-RECIPE comprises contract extraction plus feasibility-driven search. No inspected AGENT-DEMONSTRATED result shows unaided evidence-corpus construction delivering cross-contract recipe transfer through the specified fixed agent. attack_basis=LITERATURE-ONLY for that entire causal chain. The remaining twelve-hour work is resolving undocumented dependencies, choosing valid adaptations and checking that a downstream agent uses the caveats correctly.

ANCHORED ESTIMATED distribution: outcomes 0.41/0.56/0.70, probabilities 0.17/0.56/0.27. The basic corpus remains useful even when adaptation fails, while the upper state requires a feasible recipe that survives actual validation. ESTIMATED mean=0.17×0.41+0.56×0.56+0.27×0.70=0.57, range 0.41–0.70. ESTIMATED bo4=0.41+0.15(1−0.17^4)+0.14(1−0.73^4)=0.66; ESTIMATED pass@4=1−0.73^4=0.72; ESTIMATED ub95=0.70. Spread follows adaptation failure versus successful validation; it is not a borrowed training-noise estimate. Anchor and independence assumptions remain explicit.

## 5. Verdict under the kill lines
Evidence verdict CUT; headline ANCHORED verdict CUT, UNCHANGED. Binding ESTIMATED pass@4=0.72 exceeds its line by 0.22, while ESTIMATED bo4=0.66 exceeds its line by 0.06. The single-run point no longer breaches 0.70. Current training-agent results make successful execution credible often enough to retain a tail-based cut, but assigning its frequency to corpus-mediated transfer remains an assumption. This is a weaker and more specific claim than near-certain saturation.

## 6. Redesign
Class (b): ordinary feasibility and staged selection search optimize the original objective. REDESIGNABLE. Supply complete truthful resource contracts and legal initial receipts, then require adaptation where memory-saving changes alter optimization dynamics: checkpointing changes feasible batch, batch changes noise, and the resulting data schedule changes which method wins. Keep this a corpus artifact by permitting structured executable adaptation instructions, not live arbitrary control. Publish analogous development transfers and score actual chosen training outcomes under a common full-cost ledger.

The strongest re-attack combines contract extraction, capacity estimation, BOHB and pilot-informed adaptation. Put that combination in the floor. Its residual must be predicting coupled learning changes across deployments, which a frontier lab would value independently of report formatting. ESTIMATED redesign states 0.28/0.49/0.67 at probabilities 0.22/0.65/0.13 give single=0.22×0.28+0.65×0.49+0.13×0.67=0.47; bo4=0.28+0.21(1−0.22^4)+0.18(1−0.87^4)=0.57; pass@4=1−0.87^4=0.43; ub95=0.67. Re-attack basis LITERATURE-ONLY; this is CONDITIONAL near bo4, with the concrete coupling and measured control required. A robust conservative recipe winning across contracts would erase the proposed headroom.

ESTIMATED decisive compute: 1B learners, four corpus/selection arms × three workload/learner seeds × sixteen hours on one H100=192 H100-GPU-h; an 8B fixed research agent and ingestion add 24, with quality/memory repeats adding 24. Total ESTIMATED 240 H100-GPU-h; a larger subject-scale follow-up remains separately unpriced.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent curations with executed selected recipes). Grader noise UNMEASURED (planned: fixed-corpus agent repetitions and paired recipe seeds). Score ladder UNMEASURED (planned: summaries, typed contracts, feasibility checks, executed pilots and coupled adaptation reference).

## Audit record
id: C057
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.82
old_bo4: 0.89
old_pass4: 0.99
old_ub95: 0.98
new_single: 0.69
new_single_range: 0.47-0.83
new_bo4: 0.77
new_pass4: 1.00
new_ub95: 0.83
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Test resource-induced learning-dynamics adaptations after complete contract and feasibility baselines.
redesign_single: 0.47
redesign_bo4: 0.57
redesign_pass4: 0.43
redesign_ub95: 0.67
redesign_gpuh: 240
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; PaperBench Science, GPT-6 Astra, 2026
gap_to_attack: curated evidence causes valid cross-contract adaptation by a fixed agent
subfield_sota_ref: bounded post-training aggregate 39.02, TrainExplorer Liu et al., 2026
anchored_single: 0.57
anchored_bo4: 0.66
anchored_pass4: 0.72
anchored_ub95: 0.70
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
