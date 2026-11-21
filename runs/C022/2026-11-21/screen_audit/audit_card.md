# C022 — A research search tool that learns from failed reproductions — screen audit
## 1. What the screen claimed
The proposed attack combined hybrid retrieval, structured experimental conditions, contradiction queries and campaign-level tuning. It assigned ESTIMATED single/bo4/pass@4/ub95 of 0.79/0.86/0.97/0.96 and CUT, category MEM: condition-aware retrieval supposedly supplies the evidence missing from positive-only search. Its bibliography contained:

- https://arxiv.org/abs/2104.08663
- https://aclanthology.org/2020.emnlp-main.609/

## 2. Evidence audit
BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models — Nandan Thakur, 2021, fetched — supports diverse-domain retrieval comparisons, not extracting causal applicability from failed ML runs. Fact or Fiction: Verifying Scientific Claims — David Wadden, 2020, fetched — evaluates scientific support/refutation, but identifying a refuting abstract does not establish which implementation condition repairs a training recipe. Neither reports the reset researcher's final training utility under an equal experiment allowance.

Grade: PARTIAL. Corpus indexing and support/refutation retrieval are demonstrated components. Condition transfer, recipe modification and cost-effective execution carry most of the scientific burden and were extrapolated. Newer evidence strengthens structured retrieval, while still leaving the downstream objective unresolved.

## 3. Research done now
- Language agents achieve superhuman synthesis of scientific knowledge — Michael D. Skarlinski, 2024 — https://arxiv.org/abs/2409.13740 — fetched — PaperQA2 explicitly evaluates contradiction discovery, making the negative-evidence route materially stronger than a generic citation-search analogy. Biology literature synthesis remains different from selecting a profitable ML intervention.
- OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs — Akari Asai, 2024 — https://arxiv.org/abs/2411.14199 — fetched — Retrieval plus feedback improves citation-grounded answers across scientific fields. This raises confidence that a replacement search tool can package useful conditions, but its correctness endpoint cannot be substituted for training gains.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace, 2025 — https://arxiv.org/abs/2504.01848 — fetched — Research implementations remain incomplete even with source papers available. This weakens the leap from retrieving a condition to obtaining the intended experimental result; the tested agents and rubric are not this task's frozen actor or reward.
- What Makes AI Research Replicable? Executable Knowledge Graphs as Scientific Knowledge Representations — Yujie Luo, 2025, revised 2026 — https://arxiv.org/abs/2510.17795 — fetched — Integrating code and technical details improves PaperBench replication across agent frameworks. This is closer support for executable condition extraction than either original citation, though not a demonstration on private failed-reproduction ledgers.

## 4. Re-estimated attack
The fixed researcher mediates tool utility. On unresolved reward anchors, ESTIMATED recovery of failure notes supplies 0.24, code/config-linked conditions add 0.19, and dependency queries plus campaign selection add 0.15. Total ESTIMATED 0.58 leaves causal ambiguity and execution capability unresolved.

Model an ESTIMATED mixture: probability 0.60 of R=0.49 when relevant evidence is found but transfer remains incomplete, probability 0.40 of R=0.71 when a condition comparison effectively specifies the repair. This spread reflects whether the corpus contains an actionable dependency chain, search implementation choices and training-selection variance. It does not attribute unknown variance to a deterministic outer scorer. ESTIMATED single=0.60×0.49+0.40×0.71=0.58, range 0.49–0.71. ESTIMATED bo4=0.49×0.60^4+0.71×(1−0.60^4)=0.68. Since p=0.40, ESTIMATED pass@4=1−0.60^4=0.87. ESTIMATED ub95=0.71 because the lower mode's cumulative probability is only 0.60.

The lower mean reflects incomplete recipe execution; retries help when a useful condition is explicit. Shared corpus difficulty requires block-level measurement. This percentile cannot substitute for a stronger-tier prediction bound.

## 4A. Demonstrated capability and subfield SOTA
Subfield SOTA found here splits between PaperQA2's contradiction discovery and xKG's executable research knowledge; no common downstream-training leaderboard ranks them. The north star should be training utility from correctly applied failure conditions, with these systems as public controls. Their published metrics cannot define R≈1 for a private experiment ledger.

PaperQA2/ContraCrow's GPT-4-Turbo orchestrator finds contradictions, with expert validation reported for 70% (Skarlinski, 2024; fetched https://arxiv.org/html/2409.13740v2). WikiCrow articles take approximately eight minutes through APIs; contradiction runtime and GPU use are unspecified. xKG+o3-mini/PaperCoder reports 53.21% rubric completion; its BasicAgent/IterativeAgent variants have one-hour limits (Luo, 2025/2026; fetched https://arxiv.org/html/2510.17795v3). This is PaperBench Code-Dev, without executed training replication or a training-compute ledger. Its irrelevant-code ablation can harm outcomes. These published observations establish useful evidence assembly, leaving applicability and profitable training unshown.

KNOWN-RECIPE evidence is strong for indexing conditions and code. AGENT-DEMONSTRATED support ends before the required final-training benefit, so attack_basis=LITERATURE-ONLY. Within twelve hours the attacker must integrate the evidence tool, establish applicability across failure regimes and leave enough budget to train; no fetched result demonstrates that whole chain.

ANCHORED ESTIMATED R=0.29/0.48/0.63 with probabilities 0.37/0.55/0.08 represents retrieval-only progress, usable partial transfer and a rare fully actionable condition. ESTIMATED single=0.37×0.29+0.55×0.48+0.08×0.63=0.42, range 0.29–0.63. ESTIMATED bo4=0.29×0.37^4+0.48×(0.92^4−0.37^4)+0.63×(1−0.92^4)=0.52; pass@4=1−0.92^4=0.28; ub95=0.63. Independent-attempt assumptions and unmeasured utility anchors remain material; this is not an observed ceiling.

## 5. Verdict under the kill lines
The section 4 evidence re-estimate is CUT, binding on pass4 with an ESTIMATED 0.37 breach. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL, with bo4 the nearest ESTIMATED line at 0.08 clearance. The correction is xKG's Code-Dev endpoint and the absence of demonstrated failure-ledger-to-training transfer. Require executed same-budget campaigns, frozen native anchors and a concrete applicability test; otherwise the favorable anchored margins rest on assumption.

## 6. Redesign
Given the ANCHORED condition, the following sketch specifies the missing applicability experiment. Its re-attack basis is LITERATURE-ONLY; the causal training selector has not been demonstrated by the cited retrieval agents.
Cause (a): a mature retrieval/data stack repairs the stated omission. REDESIGNABLE. Build genuine failure ledgers with observationally similar symptoms produced by distinct, documented interactions among data ordering, optimization and implementation. No individual note should contain a universal fix. The tool must maintain competing condition graphs, request a discriminating training probe through the same charged API available to every baseline, and return an executable recipe decision to the reset agent.

Reward final held-out training utility after all retrieval, code extraction, diagnostic runs and final fitting costs. Supply full provenance, negative findings and useful dev examples; withhold only ordinary final evaluation outcomes. Include PaperQA2-style contradiction retrieval, exhaustive context where feasible, xKG-style executable dependencies and tuned hybrid search in the floor. This targets a frontier lab's need to decide which apparently contradictory experimental result applies to its current run.

The strongest re-attack combines those tools with active causal experiment selection. ESTIMATED R=0.34 with probability 0.78 and R=0.57 with probability 0.22: basic evidence organization earns the lower outcome; correct cross-note diagnosis occasionally unlocks the extra 0.23. Arithmetic gives ESTIMATED single=0.78×0.34+0.22×0.57=0.39; bo4=0.34×0.78^4+0.57×(1−0.78^4)=0.48; pass@4=0.00 because neither outcome reaches 0.60; ub95=0.57. These forecasts imply plausible screen passage, conditional on demonstrating the claimed residual diagnostic gap. A generic graph compiler that consistently predicts the correct probe would eliminate it.

Decisive pilot ESTIMATED 264 H100 GPU-h: 1B training subjects, four evidence/diagnostic arms, three campaign seeds, one H100 for 16 hours gives 192; an 8B frozen actor and indexing cost 24; independent final evaluation adds 48. Thus 192+24+48=264. This is a later falsification pilot, not work executed in this audit or a complete saturation panel.

## 7. Measurement status
Rollouts UNMEASURED (planned: tools built independently then used by identical reset actors). Grader noise UNMEASURED (planned: repeat fixed-tool campaigns and pair training seeds). Score ladder UNMEASURED (planned: positive-only index, failure retrieval, executable evidence graph, active diagnostic and attainable control).

## Audit record
id: C022
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.79
old_bo4: 0.86
old_pass4: 0.97
old_ub95: 0.96
new_single: 0.58
new_single_range: 0.49-0.71
new_bo4: 0.68
new_pass4: 0.87
new_ub95: 0.71
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Turn conflicting reproduction evidence into a charged active diagnosis problem scored by subsequent training utility.
redesign_single: 0.39
redesign_bo4: 0.48
redesign_pass4: 0.00
redesign_ub95: 0.57
redesign_gpuh: 264
attack_basis: LITERATURE-ONLY
demonstrated_ref: PaperQA2/ContraCrow, GPT-4-Turbo, 2024; xKG/PaperCoder and IterativeAgent, o3-mini, 2025/2026
gap_to_attack: code and evidence retrieval are not realized training utility
subfield_sota_ref: contradiction retrieval PaperQA2 2024; executable research knowledge xKG 2025/2026
anchored_single: 0.42
anchored_bo4: 0.52
anchored_pass4: 0.28
anchored_ub95: 0.63
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
