# C052 — Search that allocates shared answering capacity across campaigns — screen audit
## 1. What the screen claimed
The screen combined versioned answer deduplication, correlated knowledge-gradient allocation, short posterior lookahead, batching and prefix reuse. Its ESTIMATED single/bo4/pass@4/ub95 were 0.77/0.85/0.98/0.95; CUT, category MEM, because correlated scheduling supposedly covered the central mechanism. Old cited URLs:
- https://people.orie.cornell.edu/pfrazier/pub/CorrelatedKG.pdf
- https://docs.vllm.ai/en/stable/design/prefix_caching/

## 2. Evidence audit
The correlated-normal ranking problem supplies an implementable acquisition policy, but campaign answers are discrete, semantically correlated and may unlock complementary questions. No cited experiment measures that translation. Prefix caching is real infrastructure; its saved prefill work does not reduce a token-denominated answering budget unless the task explicitly charges compute instead. Version-safe duplicate elimination remains useful, but is already required in the competent floor.

Grade: PARTIAL. Both implementation ingredients exist, yet neither establishes the claimed normalized decision gain. The unsupported bridge is calibrated joint decision value across scientific campaigns, rather than installation of a serving package.

## 3. Research done now
All entries below were opened in this session; reported experimental results are source observations, not audit measurements. All reward forecasts and proposed budgets in this file are ESTIMATED.
- The Knowledge-Gradient Policy for Correlated Normal Beliefs — Peter Frazier et al., 2009 — https://people.orie.cornell.edu/pfrazier/pub/CorrelatedKG.pdf — fetched — confirms information sharing under Gaussian beliefs; raises recipe plausibility without demonstrating campaign semantics.
- Automatic Prefix Caching — vLLM project, 2026 documentation snapshot — https://docs.vllm.ai/en/stable/design/prefix_caching/ — fetched — validates reusable prefill state; contributes no automatic reduction in counted output tokens.
- From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research — Yuyang Wu et al., 2026 — https://arxiv.org/html/2611.17041v1 — fetched — LEAD-RL improves delegation efficiency; its training intervention is different from constructing a shared-budget scheduler during an episode.
- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts — Hjalmar Wijk et al., 2024, revised 2025 — https://arxiv.org/html/2411.15114v2 — fetched — rapid optimization supports implementing queue experiments, while longer-budget human advantages weaken assumed integration reliability.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v3 — fetched — executable reproduction remains substantially harder than proposing a scheduler, lowering confidence in complete validation.

## 4. Re-estimated attack
The reward is an anchored terminal-decision gain, not a sum of independent cache savings. Conditional on a successful implementation, allocate ESTIMATED 0.18 to avoiding genuinely redundant purchases beyond the supplied floor, 0.26 to marginal-value ordering, and 0.18 to useful limited lookahead: total ESTIMATED 0.62. Incorrect dependency beliefs, answer unreliability and complementary purchases consume the remaining reserve. These allocations are hypotheses about normalized utility, not measured reward weights.

A literature-capable implementation distribution has ESTIMATED outcomes 0.39/0.62/0.78 with probabilities 0.20/0.55/0.25: incomplete dependency integration, competent policy, unusually effective lookahead. Its ESTIMATED mean is 0.20×0.39+0.55×0.62+0.25×0.78=0.61, range 0.39–0.78. ESTIMATED E[max4]=0.39+0.23(1−0.20^4)+0.16(1−0.75^4)=0.73. With ESTIMATED p=0.80, pass@4=1−0.20^4=1.00 after rounding; ESTIMATED q95=0.78. This is lower than the old forecast because caching cannot be credited twice and inference dependencies need actual calibration.

## 4A. Demonstrated capability and subfield SOTA
Subfield SOTA anchor: Wu's LEAD-RL reports a 2.49 percentage-point BrowseComp accuracy improvement and 24.5% lower critical-path cost over shared-credit training. Those metrics cannot define R=1 for simultaneous scientific campaigns. Anchor the future control to a measured implementation of coordinated allocation with the same answering service; until that exists, native decision counts and the normalized ceiling are unresolved.

Demonstrated results: LEAD-RL uses Qwen3.6-35B-A3B and Ling-3-Flash main-agent/subagent systems with an evidence-return harness. Training duration and accelerator-hours were not specified in the fetched description; it demonstrates using coordinated delegation, not unaided invention within twelve hours. Separately, PaperBench's Claude 3.5 Sonnet with BasicAgent attains 21.0% replication in twelve hours with one A10. That constrains confidence in developing and validating a new decision model, although this inherited hub is a narrower starting point than paper replication.

KNOWN-RECIPE includes Gaussian information allocation and exact caching. AGENT-DEMONSTRATED does not cover fitting campaign-level posteriors, valuing complements and validating terminal utility under the shared token cap. Therefore attack_basis=LITERATURE-ONLY; transfer to the stipulated frontier attacker is explicitly an assumption.

For the ANCHORED distribution, the crucial uncertainty is whether the agent obtains a useful shared-decision model at all. Use two ESTIMATED modes: 0.34 with probability 0.62 for ordinary queue improvements without trustworthy joint value, and 0.65 with probability 0.38 when a usable graph model is integrated. The latter remains plausible because the original workload supplies no instantiated complementarity barrier; it is not inferred from a benchmark success percentage. ESTIMATED single=0.62×0.34+0.38×0.65=0.46, range 0.34–0.65. ESTIMATED bo4=0.34+0.31(1−0.62^4)=0.60, unrounded 0.6042; ESTIMATED pass@4=1−0.62^4=0.85; ESTIMATED ub95=0.65. This bimodality gives substantial repeated-attempt risk despite a modest mean. Restarts are assumed independent conditional on campaign difficulty; grader variation is UNMEASURED.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT through ESTIMATED bo4=0.73 and the other tails. Headline ANCHORED verdict: CUT, UNCHANGED. ESTIMATED pass@4=0.85 exceeds its line by 0.35; bo4 also narrowly breaches before rounding. LEAD-RL's scope and PaperBench's validation gap lower the expected single score, but the ordinary original graph workload still permits a plausible successful-integration mode. The verdict depends on that unmeasured mode probability, not demonstrated saturation.

## 6. Redesign
Cause class (b): acquisition and policy search can optimize an ordinary graph workload. Specify the condition concretely: use independently authored campaigns with observable evidence versions, shared intermediate findings, complementary purchases and disclosed cancellation costs. Publish matching development interactions and retain all final decisions in the denominator. Put caching, greedy value/token, correlated Gaussian acquisition and shallow lookahead together in the measured floor. Require a bounded executable allocation control to beat that floor on native decision value before freezing normalization.

The strongest re-attack uses that combined floor plus learned complement detectors and posterior rollout search. The intended residual is learning which evidence interactions actually transfer between campaigns, not concealing a graph needed by the researcher. ESTIMATED outcomes 0.26/0.45/0.64 with probabilities 0.29/0.62/0.09 distinguish failed transfer, useful local complements and reliable joint planning. ESTIMATED single=0.29×0.26+0.62×0.45+0.09×0.64=0.41; bo4=0.26+0.19(1−0.29^4)+0.19(1−0.91^4)=0.51; pass@4=1−0.91^4=0.31; ub95=0.64. Basis remains LITERATURE-ONLY. REDESIGNABLE, conditional on demonstrated native reserve; an unexpectedly strong exact planner remains the main risk.

Decisive-check budget ESTIMATED: an 8B answering model on one H100, four allocation arms × three independent graph/answer seeds × two hours =24 H100-GPU-h; eight hours of replay/calibration overhead gives 32. This is a future falsification pilot, not twelve-hour frontier certification.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent full-budget scheduler attempts on fresh campaign graphs). Grader noise UNMEASURED (planned: fixed-policy service repeats separating answer randomness from scoring determinism). Score ladder UNMEASURED (planned: uncoupled queue, cache, joint recipe, complement-aware reference and stronger constrained control).

## Audit record
id: C052
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.77
old_bo4: 0.85
old_pass4: 0.98
old_ub95: 0.95
new_single: 0.61
new_single_range: 0.39-0.78
new_bo4: 0.73
new_pass4: 1.00
new_ub95: 0.78
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Calibrate complementary shared evidence against a combined allocation floor and a feasible bounded control.
redesign_single: 0.41
redesign_bo4: 0.51
redesign_pass4: 0.31
redesign_ub95: 0.64
redesign_gpuh: 32
attack_basis: LITERATURE-ONLY
demonstrated_ref: LEAD-RL, Qwen3.6-35B-A3B and Ling-3-Flash, 2026; PaperBench, Claude 3.5 Sonnet BasicAgent, 2025
gap_to_attack: unaided joint campaign utility calibration within twelve hours
subfield_sota_ref: coordinated delegation accuracy-cost improvement, Wu et al., 2026
anchored_single: 0.46
anchored_bo4: 0.60
anchored_pass4: 0.85
anchored_ub95: 0.65
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
