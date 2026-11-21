# C084 — Approximate speculation with a real downstream regret contract — screen audit
ANCHORED headline: CONDITIONAL; ESTIMATED single 0.44 and best-of-four 0.55.
## 1. What the screen claimed
The screen combined exact speculation, ASD mismatch acceptance, syntax-sensitive exemptions and load-adaptive draft lengths, selected using executed development tasks. Its ESTIMATED single/bo4/pass@4/ub95 were 0.49/0.59/0.36/0.74; verdict CONDITIONAL, with no populated kill category, because the exact-decoder floor and executable quality tradeoff were unfinished. It cited these URLs:
- https://proceedings.mlr.press/v202/leviathan23a.html
- https://huggingface.co/ynFeng/approximate-speculative-decoding/tree/main
- https://docs.vllm.ai/en/stable/features/speculative_decoding/dynamic_speculative_decoding/

## 2. Evidence audit
Exact speculative verification has direct algorithmic and experimental support; dynamic draft sizing is an implemented serving feature. The checkpoint listing verifies an artifact, rather than demonstrating that token-type exemptions protect downstream program semantics. ASD itself explicitly distinguishes its regret ledger from a quality guarantee. Grade: PARTIAL. The weakest bridge is recognizing consequential low-regret mismatches before execution, followed by showing that selective approximation still beats a fully tuned exact stack.

## 3. Research done now
All seven distinct works listed or discussed here were fetched; mirror formats of the same paper count once.
- *Fast Inference from Transformers via Speculative Decoding* — Yaniv Leviathan et al., 2023 — https://proceedings.mlr.press/v202/leviathan23a.html — fetched — establishes the exact alternative that must enter this task's competent floor.
- *Approximate Speculative Decoding* — Yuannuo Feng et al., 2026 — https://arxiv.org/html/2608.03447v3 — fetched — reports matched strict-verifier throughput gains and small, variable task-quality changes. This raises the plausibility of useful approximation but supplies no branch-sensitivity guarantee.
- *SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding* — Kunjun Li et al., 2026 — https://arxiv.org/html/2611.02501v1 — fetched — demonstrates agents improving lossless speculation, strengthening the exact bypass and the baseline required here.
- *AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines* — Li Chen, 2026 — https://arxiv.org/html/2609.18123v1 — fetched — its engine flag searches use a deterministic proposer. They support an available tuning recipe, not autonomous semantic-risk discovery.
- *GPT-6.2 System Card* — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — bounded NanoGPT optimization demonstrates short empirical loops; transferring that competence to approximation safety remains conjectural.

The old Hugging Face listing and vLLM documentation were also opened. The documentation's inspected version is dated 2026 for this audit; its original publication year is unspecified. The listing is a 2026 ASD artifact, not an independent result.

## 4. Re-estimated attack
First consider recipe execution without discounting autonomous integration. ESTIMATED reward contributions are 0.15 from recovering safe approximation opportunities, 0.20 from development-selected regret budgets, and 0.18 from exemptions plus adaptive speculation. These are a provisional allocation of normalized improvement, not measured additive ablations. They leave semantic dependence and approximation overhead unresolved.

Represent the ESTIMATED run distribution by rewards {0.33,0.53,0.71}, with probabilities {0.20,0.60,0.20}: an overconservative verifier, a useful selective verifier, or a policy that generalizes well. Variation is mainly discovery and workload transfer; grader variance is unknown. ESTIMATED single = 0.20×0.33+0.60×0.53+0.20×0.71 = 0.53, range 0.33–0.71. ESTIMATED bo4 = 0.71−0.18×0.80^4−0.20×0.20^4 = 0.64. With p=0.20, ESTIMATED pass@4 = 1−0.80^4 = 0.59; ESTIMATED single-distribution 95th percentile = 0.71. Unlike the old fixed-looking uplift, this tail alone kills the recipe forecast.

## 4A. Demonstrated capability and subfield SOTA
Subfield comparator: Feng et al.'s ASD reports a 7.78% average throughput improvement over matched strict speculation across seven Qwen3-14B/DSpark tasks. This is the closest fetched approximate-verification reference, not a proved global frontier. R≈1 must correspond to a separately attained executable-utility improvement above a strong exact floor; the original card provides no measured anchor. Exact and approximate speedups on different models cannot define that denominator.

Two agent results matter. SpecPilot uses Opus 5.5 in Claude Code with isolated promotion and token-forcing checks. Its first Qwen3.8-27B/H100 round took 11.7 hours and 28.3 GPU-h; later rounds cost another 19.3 hours. This demonstrates exact-stack engineering inside approximately the allotted wall time, while the full final result exceeds it. It does not demonstrate selective semantic approximation. OpenAI's GPT-6.2 Astra evaluation, in an unnamed scaffold, saved 42.87% of NanoGPT baseline time after two hours on one H100. That establishes empirical optimization capacity, with no demonstrated downstream-regret classifier.

KNOWN-RECIPE applies to exact verification and ASD. The combined branch-aware approximate controller is not AGENT-DEMONSTRATED; attack_basis=LITERATURE-ONLY. Within twelve hours the attacker must implement compatible cache semantics, gather executable counterfactuals, and validate an unseen-dependency risk policy. The anchored verdict therefore rests on assumption.

Use ESTIMATED outcomes {0.27,0.48,0.66}, probabilities {0.30,0.58,0.12}. The lower branch includes integration or conservative-policy shortfalls; the upper branch requires successful semantic transfer. ESTIMATED anchored single = 0.44, range 0.27–0.66; bo4 = 0.66−0.18×0.88^4−0.21×0.30^4 = 0.55; pass@4 = 1−0.88^4 = 0.40; ub95 = 0.66. These are forecasts, not inferred frequencies from the cited benchmarks.

## 5. Verdict under the kill lines
Section 4 is CUT through bo4 and pass@4. The ANCHORED verdict is CONDITIONAL, UNCHANGED against the old screen: bo4 clears its line by only ESTIMATED 0.05 before rounding. Demonstrated lossless engineering raises baseline requirements, while the lack of agent evidence for semantic-risk integration prevents treating the whole recipe as already solved.

## 6. Redesign
Class (a): mature exact-serving bypass, compounded by an underspecified score scale. REDESIGNABLE. Commit the floor as tuned exact tree verification with load adaptation; score additional useful completions per serving second subject to disclosed executable-quality constraints. Supply development programs with explicit causal dependencies and matched private compositions where sensitivity moves between identifiers, literals and control flow. Measure a feasible reference before release; if approximation cannot outperform exact serving, reject this task for absent scientific reserve.

The strongest re-attack is ASD budget tuning plus learned sensitivity estimates and an exact fallback. It cannot obtain incremental reward from exact engineering already included in the floor; deciding where approximation is worthwhile still requires causal transfer. Basis: LITERATURE-ONLY. ESTIMATED redesigned outcomes {0.24,0.43,0.61}, weights {0.35,0.59,0.06}, give single 0.37, bo4 = 0.61−0.18×0.94^4−0.19×0.35^4 = 0.47, pass@4 = 1−0.94^4 = 0.22, ub95 0.61. Residual risk is a cheap sensitivity predictor generalizing universally.

ESTIMATED decisive check: a frozen 14B target and compatible draft on two H100s per arm; four policies × three workload seeds × two hours × two H100 = 48 GPU-h, plus 12 GPU-h for independent execution/timing audits = 60 H100 GPU-h. This is a future falsification pilot, not a certified saturation study.

## 7. Measurement status
Rollouts UNMEASURED (planned exact-floor and selective-verifier attempts). Grader noise UNMEASURED (planned repeated serving/execution pairs). Score ladder UNMEASURED (planned strict, ASD, sensitivity-aware and independently stronger controls).

Reward and proposed compute entries below are ESTIMATED; citation counts describe consulted works.

## Audit record
id: C084
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.49
old_bo4: 0.59
old_pass4: 0.36
old_ub95: 0.74
new_single: 0.53
new_single_range: 0.33-0.71
new_bo4: 0.64
new_pass4: 0.59
new_ub95: 0.71
new_verdict: CUT
binding_line: bo4>0.60
flip: CONDITIONAL->CUT
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Freeze a strong exact floor and reward validated semantic approximation on causal program families.
redesign_single: 0.37
redesign_bo4: 0.47
redesign_pass4: 0.22
redesign_ub95: 0.61
redesign_gpuh: 60
attack_basis: LITERATURE-ONLY
demonstrated_ref: SpecPilot, Opus 5.5 Claude Code, 2026; NanoGPT, GPT-6.2 Astra, 2026
gap_to_attack: no demonstrated semantic-risk controller
subfield_sota_ref: ASD matched strict-verifier comparison, Feng, 2026
anchored_single: 0.44
anchored_bo4: 0.55
anchored_pass4: 0.40
anchored_ub95: 0.66
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
