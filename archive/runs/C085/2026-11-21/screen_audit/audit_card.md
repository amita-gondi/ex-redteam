# C085 — Diffusion draft lengths under shared verifier contention — screen audit
ANCHORED headline: CUT; ESTIMATED best-of-four 0.61 narrowly breaches its line.
## 1. What the screen claimed
The old attack married LibraSpec confidence estimates to batch-conditioned speculation, an online verifier cost surface and deadline-weighted token allocation. It assigned ESTIMATED single 0.79, bo4 0.87, pass@4 0.98 and ub95 0.96, yielding CUT, category SYS: shared-load adaptation was already known. Its cited URLs were:
- https://arxiv.org/abs/2608.08721
- https://docs.vllm.ai/en/stable/features/speculative_decoding/dynamic_speculative_decoding/
- https://docs.vllm.ai/projects/ascend/en/v0.27.1rc/user_guide/feature_guide/speculative_decoding.html

## 2. Evidence audit
LibraSpec directly supports confidence-driven length optimization, while both documentation pages expose practical dynamic speculation controls. Neither documents the claimed deadline-sensitive service controller on fresh contention graphs. Nevertheless, newly fetched D-cut is much closer than the old citations: it allocates verification work across requests using confidence and measured runtime costs. Grade PARTIAL, because a comparable human system exists but end-to-end autonomous deadline optimization remains unverified.

## 3. Research done now
- *LibraSpec: Dynamic Diffusion-Based Speculative Decoding via Marginal-Gain-Driven Optimization* — Zexun Lin et al., 2026 — https://arxiv.org/html/2608.08721v1 — fetched — supplies the diffusion confidence/marginal-cost component, raising the attack beyond an acceptance-only heuristic.
- *D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding* — Tianyu Liu et al., 2026 — https://arxiv.org/html/2607.14647v1 — fetched — cross-request pruning and runtime cost modeling directly address the proposed externality; this strongly weakens the novelty argument.
- *Reciprocal Guidance: Orchestrating Draft and Verify Budgets for Advancing the Diffusion-AR Self-Speculation Frontier* — Linye Wei et al., 2026 — https://arxiv.org/html/2609.34388v1 — fetched — adapts request-specific blocks across load regimes, further raising the known-recipe baseline, although it uses a shared backbone.
- *SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding* — Kunjun Li et al., 2026 — https://arxiv.org/html/2611.02501v1 — fetched — includes agent-developed batching mechanisms and measured short campaigns; unlike the card, its clients maintain fixed in-flight concurrency.
- *GPT-6.2 System Card* — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — demonstrates quick training-code optimization, providing positive but indirect evidence for carrying out the profile-and-search loop.

Both old vLLM pages were fetched in this session. They are living documentation inspected in 2026, with publication dates unspecified. Sources are counted as distinct works, not separate abstract/HTML addresses: three old, four additional, seven fetched total.

## 4. Re-estimated attack
Conditional on a competent implementation, ESTIMATED normalized gains comprise 0.19 from replacing isolated costs with measured batch costs, 0.23 from cross-request verification allocation, and 0.15 from deadline weighting and overload fallback. The residual is joint acceptance/deadline prediction under state changes. These fractions are forecasts of score capture, not a claimed decomposition reported by D-cut.

ESTIMATED outcomes {0.34,0.57,0.73} with probabilities {0.15,0.65,0.20} represent incomplete integration, useful batch coordination and a strong deadline policy. ESTIMATED single = 0.57, range 0.34–0.73. The discrete expected maximum is ESTIMATED bo4 = 0.73−0.16×0.80^4−0.23×0.15^4 = 0.66. ESTIMATED p=0.20 gives pass@4 = 1−0.80^4 = 0.59; ub95 = 0.73. This is substantially below every old point because the old controller's discovery and validation were treated as free. The larger bo4 spread reflects occasional successful integration, rather than a uniform increment.

## 4A. Demonstrated capability and subfield SOTA
The closest verified human/system frontier is D-cut's dense/MoE high-concurrency comparison: reported average speedup rises from 1.26× to 1.65×, with runtime-dependent budget allocation. RecGuide reports up to 1.8× over vanilla self-speculation across concurrency levels. These comparisons do not establish a common global winner. R≈1 should be anchored to an independently executed coordinated service control under the card's exact deadline metric; no such normalized anchor is measured.

SpecPilot's Opus 5.5/Claude Code system produced a Qwen3.5-4B batched deployment in 9.7 hours, charging 20.2 H100 GPU-h and promoting two changes. Its hardware isolation and held-out checks make this concrete integration evidence. Fixed-concurrency decoding is still easier to validate than deadline-qualified service completions under changing arrivals. Separately, GPT-6.2 Astra in OpenAI's unnamed NanoGPT scaffold achieved its reported 42.87% time saving with two development hours and one H100. That result supports fast profiling/tuning, but neither diffusion correctness nor queue externalities were evaluated.

Thus the coordinated literature recipe is KNOWN-RECIPE; the whole deadline-sensitive attack is not AGENT-DEMONSTRATED. attack_basis=LITERATURE-ONLY, with assumption-dependent transfer. An unaided agent must port confidence semantics, preserve exact sequence verification, estimate queue costs and independently confirm deadlines within twelve hours.

The anchored ESTIMATED distribution is {0.32,0.55,0.70}, weights {0.18,0.70,0.12}. Most runs achieve substantial ordinary coordination; only the upper branch validates effective deadline allocation. ESTIMATED single = 0.53, range 0.32–0.70; bo4 = 0.70−0.15×0.88^4−0.23×0.18^4 = 0.61; pass@4 = 1−0.88^4 = 0.40; ub95 = 0.70. These probability masses are explicit forecasts, not benchmark-derived success rates.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT, bo4 exceeds 0.60 by ESTIMATED 0.06. ANCHORED verdict: CUT, UNCHANGED, but the binding bo4 excess is only ESTIMATED 0.01. D-cut and RecGuide show that the central coordination idea is implemented; SpecPilot supports bounded integration capacity. They do not support the old near-certain saturation forecast, so the retained cut is narrow and assumption-dependent.

## 6. Redesign
Class (a), with a secondary class-(b) configuration-search route. REDESIGNABLE. Install a D-cut-style cross-request cost controller as the inherited floor. Expose prefix-cache state, future-known request DAG constraints, confidence histories and deadline slack equally on dev and evaluation. Let the submitted policy coordinate draft lengths with admission and cache retention when completing one request releases dependent requests; score exact, deadline-qualified useful completions under a fixed resource ledger.

This requires anticipatory joint decisions: LibraSpec supplies local marginal gains, D-cut optimizes a current batch, and a short-horizon deadline rule can sacrifice future cache reuse or block downstream critical paths. Provide realistic dependency traces and a feasible offline-derived deployed policy as the stronger control, rather than concealing scheduler information. A frontier serving team could use this capability directly.

The re-attack combines D-cut, deadline-aware receding-horizon planning and measured cache-value estimates. Its basis remains LITERATURE-ONLY. ESTIMATED rewards {0.22,0.42,0.62}, probabilities {0.30,0.63,0.07}, yield single 0.37, bo4 = 0.62−0.20×0.93^4−0.20×0.30^4 = 0.47, pass@4 = 1−0.93^4 = 0.25, ub95 0.62. A small exact dynamic program exploiting a low-dimensional dependency graph is the main residual bypass; test it as a lawful floor.

ESTIMATED decisive budget: frozen 8B verifier plus compatible diffusion draft on one H100, five policies × four workload seeds × three hours = 60 GPU-h; add 12 GPU-h for exact-output and deadline replay = 72 H100 GPU-h. No training is assumed in that pilot.

## 7. Measurement status
Rollouts UNMEASURED (planned independent controller integrations). Grader noise UNMEASURED (planned repeated wall-time and queue replay). Score ladder UNMEASURED (planned isolated LibraSpec through coordinated dependency-aware controls).

The record's performance and pilot-cost values are ESTIMATED, not observed serving results.

## Audit record
id: C085
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.79
old_bo4: 0.87
old_pass4: 0.98
old_ub95: 0.96
new_single: 0.57
new_single_range: 0.34-0.73
new_bo4: 0.66
new_pass4: 0.59
new_ub95: 0.73
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Start above cross-request pruning and optimize disclosed cache and request-DAG consequences jointly.
redesign_single: 0.37
redesign_bo4: 0.47
redesign_pass4: 0.25
redesign_ub95: 0.62
redesign_gpuh: 72
attack_basis: LITERATURE-ONLY
demonstrated_ref: SpecPilot, Opus 5.5 Claude Code, 2026; NanoGPT, GPT-6.2 Astra, 2026
gap_to_attack: changing-arrival deadline coordination unshown
subfield_sota_ref: D-cut high-concurrency runtime allocation, Liu, 2026
anchored_single: 0.53
anchored_bo4: 0.61
anchored_pass4: 0.40
anchored_ub95: 0.70
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
