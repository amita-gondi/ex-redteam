# C063 — Make MTP gradients correct and cheap across sequence shards — screen audit
## 1. What the screen claimed
The screen proposed exact forward halo exchange, its backward adjoint, transfer coalescing, overlap and selective embedding recomputation. Its ESTIMATED single/best-of-four/pass@4/upper-95% were 0.76/0.85/0.95/0.95, giving CUT, category SYS: public dependency indices allegedly expose almost all communication reserve. It cited these URLs:
- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/multi_token_prediction.html
- https://docs.nvidia.com/megatron-core/developer-guide/nightly/apidocs/core/core.transformer.multi_token_prediction.html

## 2. Evidence audit
The first documentation page specifies the depth-dependent objective; the second now explicitly lists boundary exchange and precomputed-embedding rolling. These are strong implementation leads, but neither supplies a measured loss/time comparison of corrected full gather against exact halos across the card's sequence layouts. Forward indices also do not establish a performant distributed backward or demonstrate agent validation of training trajectories. Grade: PARTIAL, because the communication recipe exists while its normalized payoff and autonomous integration remain extrapolations.

## 3. Research done now
The search covered MTP sequence-parallel gradient transport and current autonomous training optimization. Every listed source was opened; source statistics below are reported results, while all reward forecasts are ESTIMATED.
- Multi-Token Prediction (MTP) — NVIDIA, 2026 documentation snapshot — https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/multi_token_prediction.html — fetched — sequential prediction depths clarify which shifted embeddings require ancestry; this supports repair, not its speedup.
- core.transformer.multi_token_prediction — NVIDIA, 2026 snapshot — https://docs.nvidia.com/megatron-core/developer-guide/nightly/apidocs/core/core.transformer.multi_token_prediction.html — fetched — adjacent-rank exchange and packed rolls make the old synthesis route more concrete, raising implementation plausibility.
- DeepSeek-V3 Technical Report — DeepSeek-AI, 2024, revised 2025 — https://arxiv.org/abs/2412.19437 — fetched — production MTP training establishes a meaningful research target; its large MoE training result does not isolate embedding-halo benefit.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — autonomous distributed pretraining can reach mature baselines, increasing the threat from complete replacements; the benchmark does not test MTP gradient equivalence.
- GPT-6.2 System Card, research engineering assessments — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — measured training-time improvement supports empirical tuning, but the single-device task omits cross-rank ancestry.
- AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure — Megan Kinniment et al./METR, 2026 — https://metr.org/blog/2026-11-20-q4-2026-capability-update/ — fetched — record-level training optimization remains harder than competent improvements, reducing confidence that a public operator yields near-ceiling reward.

## 4. Re-estimated attack
First assess the recipe assuming competent integration. In provisional reward units, exact selective transport plausibly captures ESTIMATED 0.37, coalescing and asynchronous interior work another ESTIMATED 0.18, and profile-guided recomputation ESTIMATED 0.09. These are contributions to one quality-per-total-time utility, not separately graded bonuses. Corrected gathering itself belongs in the floor; gradient parity is a validity constraint. Unhidden topology and packed-document metadata help, while horizons spanning many shards leave unavoidable traffic.

An ESTIMATED three-outcome distribution assigns probability 0.20 to R=0.40, 0.55 to R=0.65, and 0.25 to R=0.79. The low outcome represents backward synchronization costs defeating the predicted forward gain; the high outcome needs both halo correctness and effective overlap. ESTIMATED single=0.20×0.40+0.55×0.65+0.25×0.79=0.64, range 0.40–0.79. ESTIMATED best-of-four=0.79−0.14×0.75^4−0.25×0.20^4=0.75; p=0.80, so ESTIMATED pass@4=1−0.20^4=1.00; ESTIMATED upper-95%=0.79. This replaces the screen's unsupported high mean with implementation-dependent spread, while retaining a recipe-level CUT.

## 4A. Demonstrated capability and subfield SOTA
Subfield anchor: DeepSeek-V3 reports MTP within a 671B-total/37B-active model trained on 14.8T tokens. That is a demonstrated large-scale MTP system, not a measured optimum for this communication problem. NVIDIA's current boundary operators are the closest public implementation reference. Neither fixes the card's R≈1 loss/time anchor; native corrected-gather, production-roll and stronger-control curves must establish it before release.

Two fetched agent results constrain transfer. Opus 5.5 with Claude Code matches or exceeds Singularity-Bench's pretraining reference during twelve hours on four GB300s; that reference uses FP8 OLMo-2-1B training in Megatron. It demonstrates selecting and implementing a distributed training stack, but not constructing exact MTP backward halos. Separately, GPT-6.2 Astra in OpenAI's tool-enabled NanoGPT evaluation saved a reported 42.87% of baseline training time with two development hours and one H100. Its optimizer/hyperparameter search is relevant to validating useful speed, yet single-device target-quality training does not certify this multi-rank operator. The public card does not fully specify the agent scaffold internals.

KNOWN-RECIPE: explicit exchange plus adjoint and overlap. AGENT-DEMONSTRATED: adjacent distributed training optimization, without this combined exact-gradient result. Hence attack_basis=LITERATURE-ONLY. The missing twelve-hour achievement is integrating transport, packed masks and backward accumulation, then demonstrating improved learning per complete elapsed time.

The anchored ESTIMATED distribution is R={0.29,0.49,0.66} with probabilities {0.30,0.57,0.13}. Its components represent parity-only progress, a valid useful halo implementation, and successful end-to-end tuning. ESTIMATED single=0.087+0.2793+0.0858=0.45, range 0.29–0.66; best-of-four=0.66−0.17×0.87^4−0.20×0.30^4=0.56; pass@4=1−0.87^4=0.43; upper-95%=0.66. These probabilities are judgmental; the anchored verdict rests on assumption, not an observed failure rate.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT, with best-of-four ESTIMATED 0.75 exceeding 0.60 by 0.15. ANCHORED: CONDITIONAL, FLIPPED CUT→CONDITIONAL; best-of-four is only ESTIMATED 0.04 below its line, while single, pass@4 and upper tail have larger margins. Demonstrated distributed training prevents dismissing the attack, but no fetched result supports the screen's near-certain exact-halo success.

## 6. Redesign
Cause class (a): mature communication primitives. REDESIGNABLE. Make horizon selection part of the disclosed scientific task: allocate auxiliary prediction depths across documented sequence regimes under a common training FLOP ledger, with exact ancestry retained for every selected target. Score held-out next-token loss per total training time relative to a floor combining correct halos, recomputation and a development-tuned fixed horizon schedule. Match development and hidden horizon regimes; reveal all objective semantics. This adds a real allocation problem that a frontier pretraining team would value, without concealing dependencies or manufacturing latency pressure.

The strongest re-attack combines current boundary transport with short-run allocation search. Its basis remains LITERATURE-ONLY: public MTP training does not demonstrate autonomous selection of transferable schedules. An ESTIMATED distribution {0.24,0.43,0.62} with probabilities {0.38,0.54,0.08} gives single=0.37, best-of-four=0.62−0.19×0.92^4−0.19×0.38^4=0.48, pass@4=1−0.92^4=0.28, and upper-95%=0.62. Residual risk is one universal fixed schedule; test it explicitly before claiming headroom. Decisive-check cost ESTIMATED: a 1B decoder, four allocation/transport arms × three seeds × six hours × four H100s=288 H100-h, plus 48 H100-h for gradient probes/evaluation, totaling 336 H100-h. No GPU work was run.

## 7. Measurement status
Rollouts UNMEASURED (planned full-budget fresh packed-MTP attempts); grader noise UNMEASURED (planned paired repeated training trajectories); score ladder UNMEASURED (planned corrected gather, production roll, exact halos, recomputation and adaptive-depth control).

## Audit record
id: C063
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.76
old_bo4: 0.85
old_pass4: 0.95
old_ub95: 0.95
new_single: 0.64
new_single_range: 0.40-0.79
new_bo4: 0.75
new_pass4: 1.00
new_ub95: 0.79
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Learn transferable MTP horizon allocation after exact communication is included in the floor.
redesign_single: 0.37
redesign_bo4: 0.48
redesign_pass4: 0.28
redesign_ub95: 0.62
redesign_gpuh: 336
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench, Opus 5.5+Claude Code, 2026; NanoGPT, GPT-6.2 Astra, 2026
gap_to_attack: exact distributed MTP backward and learning-time validation
subfield_sota_ref: DeepSeek-V3 MTP, DeepSeek-AI, 2024/2025
anchored_single: 0.45
anchored_bo4: 0.56
anchored_pass4: 0.43
anchored_ub95: 0.66
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
