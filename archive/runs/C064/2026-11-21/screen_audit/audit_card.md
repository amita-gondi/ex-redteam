# C064 — Router regularization invariant to token packing — screen audit
## 1. What the screen claimed
The old attack combined valid-token normalization, global or sequence regularization, loss-free expert biases, capacity control and timescale tuning. It forecast ESTIMATED single 0.47, best-of-four 0.56, pass@4 0.32 and upper-95% 0.70, retaining CONDITIONAL status until rare specialization survived those controls; the TSV has no kill category for this survivor. Its two citations were:
- https://arxiv.org/abs/2408.15664
- https://docs.nvidia.com/megatron-core/developer-guide/latest/apidocs/core/core.transformer.transformer_config.html

## 2. Evidence audit
Loss-free balancing has actual model-training evidence, including improved quality and balance, rather than merely an optimizer argument. Configuration documentation establishes that normalization and balancing alternatives are available, but measures neither packing invariance nor compositional rare-domain retention. Most importantly, the screen's claim that future rare-expert utility resists ordinary tuning was also unmeasured. Grade: PARTIAL: neither the attack's complete success nor the proposed residual is established on comparable histories.

## 3. Research done now
I searched for routing specialization, population balance and contemporary autonomous pretraining results, then fetched the following. Reward and probability quantities in this audit are ESTIMATED; paper results are attributed reports.
- Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts — Lean Wang et al., 2024 — https://arxiv.org/abs/2408.15664 — fetched — validation reaches 3B-parameter models and 200B tokens; this raises confidence in bias-based balancing but says little about later compositional demand.
- core.transformer.transformer_config — NVIDIA, 2026 documentation snapshot — https://docs.nvidia.com/megatron-core/developer-guide/latest/apidocs/core/core.transformer.transformer_config.html — fetched — available router controls support a broad lawful baseline, without quantifying scientific headroom.
- Advancing Expert Specialization for Better MoE — Hongcan Guo et al., 2025, revised 2026 — https://arxiv.org/abs/2505.22323 — fetched — orthogonality and variance objectives improve specialization; this weakens the assumption that correcting normalization leaves only unexplored techniques.
- ϕ-Balancing for Mixture-of-Experts Training — Lizhang Chen et al., 2026 — https://l-z-chen.github.io/img_pdf/MoE_ICML2026.pdf — fetched — an EMA-based population objective outperforms Switch-style and loss-free baselines in reported experiments, expanding the combined attack beyond the screen's menu.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — successful autonomous pretraining supports implementation of routing alternatives, but does not isolate preservation of uncommon experts under changing mixtures.
- GPT-6.2 System Card, training evaluations — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — real model-training improvements strengthen short-loop tuning; its dense-training evidence cannot settle sparse specialization.

## 4. Re-estimated attack
Normalization repair earns no residual utility above the stipulated competent floor. I allocate ESTIMATED 0.24 of reward-scale improvement to choosing an appropriate loss-free/population controller, ESTIMATED 0.12 to joint capacity and timescale selection, and ESTIMATED 0.07 to specialization-aware validation. These increments describe plausible held-out loss recovery, not a fabricated weighted grader. Interaction can negate them: suppressing rare traffic may improve average balance while damaging a later composite skill.

Use an ESTIMATED discrete approximation R={0.25,0.46,0.64}, probabilities {0.25,0.60,0.15}. The spread represents controller transfer and training seed sensitivity, rather than numerical noise in counting tokens. ESTIMATED single=0.25×0.25+0.60×0.46+0.15×0.64=0.43, range 0.25–0.64. For independent attempts, ESTIMATED best-of-four=0.64−0.18×0.85^4−0.21×0.25^4=0.55. Only the high outcome passes: ESTIMATED p=0.15 and pass@4=1−0.85^4=0.48; upper-95%=0.64. Relative to the old estimates, the mean decreases slightly, but pass@4 rises because the explicit high-mode probability is larger than the old unexplained tail implied. This evidence-level result is CONDITIONAL, chiefly on pass@4's ESTIMATED 0.02 clearance.

## 4A. Demonstrated capability and subfield SOTA
The strongest newly fetched same-subfield comparator is Chen et al.'s population-balancing method, with Guo et al.'s specialization objectives as an independent quality-oriented competitor. They report improvements on their own pretraining/fine-tuning suites; no common leaderboard establishes a universal router winner. The reference must therefore be the best complete combined control measured on identical valid-token streams, including these methods. R≈1 remains UNMEASURED: a fixed reference of 0.60 cannot be justified from expert-count uniformity.

For the first agent anchor, Opus 5.5+Claude Code beat or matched the Singularity-Bench pretraining baseline with twelve hours and four GB300s, implementing a stack competitive with Megatron/OLMo training. This makes discovering a runnable router variant credible; it leaves multi-history rare-skill retention untested. For the second, GPT-6.2 Astra's tool-enabled NanoGPT trials achieved a reported 42.87% mean baseline-time saving in two hours on one H100. That demonstrates experimentally improving training efficiency, but not an agent selecting a sparse-router objective by delayed compositional loss. OpenAI discloses the task environment rather than a complete reproducible scaffold specification.

KNOWN-RECIPE covers token counts, biases, population statistics and extra specialization losses. AGENT-DEMONSTRATED covers ordinary training-stack construction, not their joint generalization under heterogeneous packing. attack_basis=LITERATURE-ONLY. Within twelve hours the agent must distinguish fast balancing proxies from genuinely retained expertise, fit several complete training runs and select a schedule that transfers.

An anchored ESTIMATED R distribution puts probabilities {0.32,0.62,0.06} on {0.22,0.41,0.63}. ESTIMATED single=0.0704+0.2542+0.0378=0.36, range 0.22–0.63. ESTIMATED best-of-four=0.63−0.22×0.94^4−0.19×0.32^4=0.46; pass@4=1−0.94^4=0.22; upper-95%=0.63. The rare upper mode reflects finding a broadly transferable recipe, not merely winning a seed. No benchmark calibrates its probability, so this is explicitly assumption-dependent.

## 5. Verdict under the kill lines
The section 4 recipe forecast remains CONDITIONAL. The ANCHORED forecast is PASS-SCREEN, FLIPPED CONDITIONAL→PASS-SCREEN: mean, best-of-four, pass@4 and upper-tail margins are ESTIMATED 0.34, 0.14, 0.28 and 0.12 respectively. The reason is the missing demonstrated bridge from capable pretraining agents to delayed expert specialization, despite stronger known human methods. This is a research-priority judgment; absent measured native reserve it does not certify an executable task.

## 6. Redesign
NOT-NEEDED under the anchored kill lines. Preserve the published packing-invariant objective and grade actual compositional loss at equal active FLOPs; absorb population balancing and specialization-loss combinations into the baseline before claiming a reference gain. The principal risk is that one such published combination solves all mixtures, which would reverse the anchored verdict when measured. Neither a ban on loss-free routing nor hidden normalization rules would be an acceptable response.

## 7. Measurement status
Rollouts UNMEASURED (planned independent router searches with fixed compute and fresh mixtures); grader noise UNMEASURED (planned paired-seed endpoint loss and rare-slice uncertainty); score ladder UNMEASURED (planned token-correct global loss, loss-free bias, population balancing, specialization losses and attainable joint control).

## Audit record
id: C064
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.47
old_bo4: 0.56
old_pass4: 0.32
old_ub95: 0.70
new_single: 0.43
new_single_range: 0.25-0.64
new_bo4: 0.55
new_pass4: 0.48
new_ub95: 0.64
new_verdict: CONDITIONAL
binding_line: none
flip: none
kill_cause_class: na
redesign_status: NOT-NEEDED
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench pretraining, Opus 5.5+Claude Code, 2026; NanoGPT, GPT-6.2 Astra, 2026
gap_to_attack: delayed rare-expert retention across packing histories
subfield_sota_ref: population ϕ-balancing, Chen et al., 2026; specialization objectives, Guo et al., 2025/2026
anchored_single: 0.36
anchored_bo4: 0.46
anchored_pass4: 0.22
anchored_ub95: 0.63
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CONDITIONAL->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
