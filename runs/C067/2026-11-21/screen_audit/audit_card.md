# C067 — Versioned prefix caches for asynchronous learning — screen audit
## 1. What the screen claimed
The screen combined model-epoch cache keys, prefix grouping, architectural dependency closure, synchronization tuning and objective-permitted stale-rollout correction. It assigned CUT/SYS with ESTIMATED single 0.70, best-of-four 0.80, pass@4 0.91 and upper-95% 0.93, attributing most reserve to conventional scheduling. The source URLs were:
- https://docs.vllm.ai/en/stable/design/prefix_caching/
- https://arxiv.org/abs/1802.01561

## 2. Evidence audit
vLLM's keying scheme supports identity-safe prefix lookup, but a key alone neither certifies unchanged activations nor improves post-update learning. IMPALA demonstrates asynchronous off-policy learning in Atari/DeepMind Lab, a substantial objective and model mismatch for language-policy prefix reuse. Exact dependency closure is sound when subgraphs are unchanged; the existence of useful such subgraphs under this card's updates is not demonstrated. Grade: PARTIAL, with both the reusable-state premise and normalized learning benefit still open.

## 3. Research done now
Search focused on asynchronous language RL, post-refit cache invalidation and measured current agent systems. All cited pages were fetched; ESTIMATED labels apply to this audit's forecasts rather than to attributed published results.
- Automatic Prefix Caching — vLLM project, 2026 documentation snapshot — https://docs.vllm.ai/en/stable/design/prefix_caching/ — fetched — extra block identities support epoch separation; they do not make old-weight KV tensors current.
- IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures — Lasse Espeholt et al., 2018 — https://arxiv.org/abs/1802.01561 — fetched — proves a particular actor/learner correction works, not that V-trace can replace the card's frozen learning objective.
- AReaL: A Large-Scale Asynchronous Reinforcement Learning System for Language Reasoning — Wei Fu et al., 2025, revised 2026 — https://arxiv.org/abs/2505.24298 — fetched — reports up to 2.77× training acceleration with matched/improved quality, strengthening the async tuning route on language models.
- Train with Async GRPO — NVIDIA NeMo-RL, 2026 snapshot — https://docs.nvidia.com/nemo/rl/latest/guides/async-grpo.html — fetched — documents explicit post-update cache recomputation and backend-specific pause behavior; conventional repairs are more substantial than a version counter.
- COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning — Zicheng Hu et al., 2026 — https://arxiv.org/abs/2610.09597 — fetched — advantage staleness can defeat policy-ratio correction alone, lowering confidence in the screen's simple combined recipe.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — independently demonstrates strong agent-built asynchronous RL and prefix-cached serving, but not their combined cache lifecycle through updates.

## 4. Re-estimated attack
A legal full-flush system with tuned update cadence plausibly captures ESTIMATED 0.31 of the provisional reward; batching by prefix/version contributes ESTIMATED 0.16; exact reuse of genuinely unaffected subgraphs adds ESTIMATED 0.11 where available. This estimates success per total device-time. Higher cache-hit rate does not itself count, and changing the learner to COPC or IMPALA is legal only if objective freedom is expressly granted. Standard importance ratios cannot repair an incorrectly labeled cache.

An ESTIMATED mixture places probabilities {0.25,0.55,0.20} on R={0.34,0.61,0.76}. It captures three structural outcomes: dense updates leave no reusable state, epoch scheduling works, or selective reuse also helps. ESTIMATED single=0.0850+0.3355+0.1520=0.57, range 0.34–0.76. ESTIMATED best-of-four=0.76−0.15×0.80^4−0.27×0.25^4=0.70; p=0.75 implies pass@4=1−0.25^4=1.00; upper-95%=0.76. This is lower than the screen's mean because exact reuse is not generally available after dense updates; repeated attempts still cut the recipe scenario.

## 4A. Demonstrated capability and subfield SOTA
AReaL supplies the closest system-scale quality/throughput reference, while COPC is a newer strong correction comparator: it reports stronger tool-math/search learning and a 1.7× step-time advantage over synchronous PPO. These metrics do not rank exact cache policies on this card. Anchor the floor to a tuned current reset-capable async stack and measure success/time against an independently feasible exact-reuse control. Neither headline speedup supplies R≈1, and a workload with no reusable subgraph cannot justify that reference.

Agent demonstration one is Opus 5.5 with Claude Code constructing asynchronous GRPO on four GB300s in twelve hours, with three rollout GPUs, a single trainer, verified partial weight pushes and reported score 0.533 versus Miles' 0.539. This directly supports scheduling and weight synchronization, but the paper does not certify this card's cache receipts. Demonstration two is GPT-6.1 Sol with Codex building a prefix-cached serving engine within twelve hours on four GB300s: reported income 9.70 versus SGLang's 8.18, with recurrent-state caching as well as attention state. The weights are fixed in that serving task, so its cache correctness result does not establish validity across learner updates.

The ingredients are KNOWN-RECIPE and each adjacent subsystem is AGENT-DEMONSTRATED; their exact composition under this objective is not. Thus attack_basis=LITERATURE-ONLY. Required twelve-hour work includes finding actual dependency closure, integrating refit/pause/recompute semantics and validating downstream policy gains rather than cached-serving throughput.

For the anchored ESTIMATED distribution, R={0.42,0.52,0.68} has probabilities {0.26,0.61,0.13}. ESTIMATED single=0.1092+0.3172+0.0884=0.51, range 0.42–0.68. ESTIMATED best-of-four=0.68−0.16×0.87^4−0.10×0.26^4=0.59; pass@4=1−0.87^4=0.43; upper-95%=0.68. Outcome variability chiefly reflects useful transfer of a valid epoch schedule, with learner randomness secondary. Probability assignments remain assumptions.

## 5. Verdict under the kill lines
Section 4 yields CUT. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL, because best-of-four has only ESTIMATED 0.01 clearance; upper-95% is ESTIMATED 0.07 below its boundary. The fetched agent evidence strongly supports both engineering halves but does not show them integrated across changing weights. This is a concrete evidence gap, not a claim that current agents cannot implement cache invalidation.

## 6. Redesign
Kill cause (a), REDESIGNABLE. Specify a conditional-update policy architecture whose published layer dependencies permit exact reuse below unchanged blocks. Let the researcher choose update block subsets and synchronization boundaries using visible training statistics, at a fixed trainable-capacity and total-FLOP ledger. Grade policy success per total GPU time across prefix families requiring different adaptation depths. Supply a development counterpart for every depth regime. Include full flushing, a globally frozen prefix encoder, version batching and ordinary partial-training schedules in the floor.

That makes the learning cost of freezing reusable layers real: epoch keying plus dependency closure establishes legality but cannot decide which adaptation to forgo. The strongest re-attack is short-horizon search over freeze/cadence schedules using the current async stack. Basis LITERATURE-ONLY; no fetched agent result demonstrates transferable joint layer-adaptation/cache selection. ESTIMATED {0.26,0.44,0.65} with probabilities {0.40,0.51,0.09} yields single=0.39; best-of-four=0.65−0.21×0.91^4−0.18×0.40^4=0.50; pass@4=1−0.91^4=0.31; upper-95%=0.65. A universal partial-training schedule remains the main risk. ESTIMATED check: 1B policy, four coupled schedules × three seeds × eight hours × four H100s=384, plus 48 H100-h for fresh-prefix scoring and exact-state checks=432 H100-h. An exact slower control must fit before proceeding.

## 7. Measurement status
Rollouts UNMEASURED (planned joint cache/synchronization agents); grader noise UNMEASURED (planned paired rollout and learner seeds with total-cost replay); score ladder UNMEASURED (planned reset, version batching, dependency reuse, partial-update schedule and joint control).

## Audit record
id: C067
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.70
old_bo4: 0.80
old_pass4: 0.91
old_ub95: 0.93
new_single: 0.57
new_single_range: 0.34-0.76
new_bo4: 0.70
new_pass4: 1.00
new_ub95: 0.76
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Couple exact reusable layers to adaptation-depth choices with full-flush and fixed-freezing controls.
redesign_single: 0.39
redesign_bo4: 0.50
redesign_pass4: 0.31
redesign_ub95: 0.65
redesign_gpuh: 432
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench async RL, Opus 5.5+Claude Code, 2026; Singularity-Bench serving, GPT-6.1 Sol+Codex, 2026
gap_to_attack: exact cache reuse through policy refits with learning benefit
subfield_sota_ref: AReaL, Fu et al., 2025/2026; COPC, Hu et al., 2026
anchored_single: 0.51
anchored_bo4: 0.59
anchored_pass4: 0.43
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
