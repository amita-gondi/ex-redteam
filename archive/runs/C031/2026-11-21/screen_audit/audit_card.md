# C031 — Optimize inference under live vocabulary constraints — screen audit
## 1. What the screen claimed
The screen combined XGrammar-2 dispatch/JIT/cache reuse, llguidance background parsing, versioned mask deltas and fused sampling. Its ESTIMATED single/bo4/pass@4/ub95 were 0.85/0.91/0.99/0.99, producing CUT, category SYS, because dynamic grammar compilation allegedly removed the main obstacle. Its cited URLs were:
- https://arxiv.org/abs/2601.04426
- https://github.com/guidance-ai/llguidance/blob/main/parser/README.md

## 2. Evidence audit
XGrammar-2 actually evaluates changing tool sets and tag-triggered grammar dispatch, including end-to-end generation; this is meaningful comparable support for ordinary dynamic structure. Its shared-schema experiments do not establish efficient maintenance when an external observation invalidates relationships inside many previously reusable fragments. llguidance documents overlapping mask calculation with logits, but documentation is neither a measured delta-transfer implementation nor evidence that dependency-changing observations leave that overlap available. Grade: PARTIAL; the engine replacement is demonstrated, whereas the most important extension to this card's observation semantics remains extrapolation.

## 3. Research done now
- XGrammar-2: Dynamic and Efficient Structured Generation Engine for Agentic LLMs — Linzhang Li et al., 2026 — https://arxiv.org/abs/2601.04426 — fetched, including full-text evaluation — Strong evidence against a static-engine baseline: dynamic tool grammars benefit from substructure reuse. Its dispatch semantics differ from arbitrary externally revised predicates, lowering confidence in the screen's near-complete recovery claim.
- llguidance parser README — guidance-ai, 2026 living documentation, accessed this session — https://github.com/guidance-ai/llguidance/blob/main/parser/README.md — fetched, with raw-file body checked — Advises background mask computation and exposes token commitment. This makes overlap implementable, raising the attack, while leaving observation arrival on the critical path unresolved.
- Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation — Luca Beurer-Kellner et al., 2024 — https://arxiv.org/abs/2403.06988 — fetched — DOMINO establishes efficient subword-aligned CFG decoding. It supports a good correctness/performance floor here, without testing destructive live revisions.
- XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models — Yixin Dong et al., 2024, revised 2025 — https://arxiv.org/abs/2411.15100 — fetched — Context-sensitive token checks and CPU/GPU overlap are already engineered, so rebuilding these pieces should not earn research credit. This raises confidence in integration gains, rather than in semantic incrementalization.
- SynCode: LLM Generation with Grammar Augmentation — Shubham Ugare et al., 2024 — https://arxiv.org/abs/2403.01632 — fetched — Its offline DFA mask store and CFG guarantees identify an important boundary: syntax validity is well supported; changing nonlocal semantic legality is not demonstrated. This cuts against treating all token constraints as solved grammar caching.

## 4. Re-estimated attack
With native anchors UNMEASURED, use ESTIMATED gain shares 0.45 grammar/mask execution, 0.30 observation recomputation and 0.25 transfer/scheduling. ESTIMATED recovered fractions 0.95/0.65/0.45 yield 0.45×0.95+0.30×0.65+0.25×0.45=0.74 rounded. Observation-triggered invalidation remains on the critical path.

The ESTIMATED distribution has R=0.49/0.72/0.83 with probabilities 0.15/0.40/0.45: broad correctness rebuilds, competent integration and effective overlap/cache reuse. ESTIMATED mean=0.15×0.49+0.40×0.72+0.45×0.83=0.74. These are search/workload outcomes, with independent restarts assumed within the workload family.

ESTIMATED single=0.74, range 0.49–0.83; bo4=0.49×0.15^4+0.72×(0.55^4−0.15^4)+0.83×(1−0.55^4)=0.82. ESTIMATED p=0.85 gives pass@4=1−0.15^4=1.00 rounded, not certainty. ESTIMATED ub95=0.83 because cumulative mass below that mode is 0.55; this percentile is not a fitted S4 confidence interval. Mean, maximum and upper-tail estimates decrease from the screen; pass@4 increases after replacing its unexplained probability with this explicit distribution.

## 4A. Demonstrated capability and subfield SOTA
Subfield SOTA consulted: Li et al.'s fetched 2026 XGrammar-2 dynamic-tool evaluation. Use that configuration as the public reference. An attainable faster control for arbitrary observation-revised predicates is absent; R≈1 remains unanchored. Section 4 concerns recipe potential.

Two fetched agent comparisons delimit that transfer. KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — reports correct generated kernels throughout KernelBench and an L1 average above torch.compile on H100. The inspected report leaves the generating model and total search hours unspecified. It demonstrates local hardware-guided optimization, not live semantic-mask integration.

Evaluating frontier AI R&D capabilities of language model agents against human experts — METR, 2024 — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/ — fetched — reports o1-preview in METR's scaffold beating the best human prefix-sum kernel, using GPU-equipped task computers and experiments across aggregated budgets up to 32 hours; that winning run's exact compute is not identified here. This is evidence for bitset/kernel iteration, while external-observation state consistency remains untested. These are source-reported outcomes, not this audit's measurements.

KNOWN-RECIPE covers grammar execution; AGENT-DEMONSTRATED covers neighboring kernels. attack_basis=LITERATURE-ONLY: twelve-hour backend selection, invalidation correctness and transfer integration remain untested together. The anchored verdict assumes transfer across that gap.

ANCHORED ESTIMATED distribution: R=0.33/0.54/0.68 with probabilities 0.28/0.60/0.12, reflecting stalled integration, a sound ordinary backend and a rare successful live pipeline. ESTIMATED single=0.28×0.33+0.60×0.54+0.12×0.68=0.50, range 0.33–0.68. ESTIMATED bo4=0.68−0.14×0.88^4−0.21×0.28^4=0.59. ESTIMATED pass@4=1−0.88^4=0.40, since p=0.12; ESTIMATED ub95=0.68. This distribution widens the integration-risk contribution rather than applying an across-card discount.

## 5. Verdict under the kill lines
Section 4's recipe-capability verdict is CUT: ESTIMATED bo4=0.82 exceeds its line by 0.22. The headline ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL, with ESTIMATED bo4=0.59 only 0.01 below the binding line. The fetched kernel demonstrations do not show reliable integration of the semantic pipeline the screen priced as nearly certain. Retention requires an executable XGrammar-2 combined floor, full observation-consistency checks and a stronger same-budget control establishing native reserve; no claim of measured saturation resistance follows.

## 6. Redesign
Cause (a), mature grammar serving. REDESIGNABLE under a concrete condition: execute semantic constraints whose observations revise shared permissions, cardinality dependencies and cross-field references during concurrent generation. Supply dependency graphs, predicate semantics, realistic histories and an exact slow checker, including local and broad revisions in development. Score valid responses per complete service time, charging compilation and predicate work under disclosed memory/latency limits.

XGrammar-2 dispatch, llguidance overlap, dirty-bit propagation, sparse/dense fallback and fused sampling remain the strongest lawful recipe. Put that whole combination into the floor. A grammar cache cannot itself update a token mask whose allowed identifiers depend on changed shared relations; a useful improvement must jointly choose incremental indexes, recomputation granularity and request scheduling. This is valuable frontier agent infrastructure rather than larger arbitrary automata. An independently implemented dependency-aware control must first show affordable native reserve; otherwise abandon this redesign.

ESTIMATED re-attack modes are 0.28/0.47/0.64 with probabilities 0.40/0.50/0.10: ordinary incremental indexes help often, but discovering an effective shared representation is rarer. ESTIMATED mean=0.40×0.28+0.50×0.47+0.10×0.64=0.41, range 0.28–0.64. ESTIMATED bo4=0.64−0.17×0.90^4−0.19×0.40^4=0.52; p=0.10 yields pass@4=1−0.90^4=0.34; ub95=0.64. Re-attack basis is LITERATURE-ONLY, including extrapolation from known indexes, not a demonstrated agent solve. These would clear the absolute margins. Residual risk is that standard incremental-view maintenance plus a better profiler reaches the strong mode much more frequently, or semantic work contributes too little end-to-end latency. Keep feasibility CONDITIONAL until those controls and the native reserve are measured.

Decisive-check GPU-h ESTIMATED: a frozen 8B subject on one H100, five arms, three independently authored trace seeds, 0.75 hour per execution gives 5×3×0.75×1=11.25 H100 GPU-h. Add ESTIMATED 3.75 GPU-h for full checker replay and 3.00 for timing/peak-state replication: total 18.00. This is a falsification pilot, not the full saturation panel; no compute was executed here.

## 7. Measurement status
Rollouts UNMEASURED (planned dynamic-backend and semantic-index controls on fresh histories). Grader noise UNMEASURED (planned independent host scheduling and warmed timing repeats). Score ladder UNMEASURED (planned full-mask, combined public stack and feasible dependency-aware control, with frozen native anchors).

## Audit record
id: C031
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.85
old_bo4: 0.91
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.74
new_single_range: 0.49-0.83
new_bo4: 0.82
new_pass4: 1.00
new_ub95: 0.83
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Execute disclosed live relational constraints with exact shared-dependency invalidation above a combined dynamic-grammar floor.
redesign_single: 0.41
redesign_bo4: 0.52
redesign_pass4: 0.34
redesign_ub95: 0.64
redesign_gpuh: 18
attack_basis: LITERATURE-ONLY
demonstrated_ref: KernelAgent, model unspecified, 2026; RE-Bench, o1-preview, 2024
gap_to_attack: observation-consistent grammar and transfer integration lacks a matched agent trial
subfield_sota_ref: XGrammar-2 dynamic tool generation, Li et al., 2026
anchored_single: 0.50
anchored_bo4: 0.59
anchored_pass4: 0.40
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
