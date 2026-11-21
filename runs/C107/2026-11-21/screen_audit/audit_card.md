# C107 — A tokenizer change that must pay for its own optimizer recovery — screen audit
## 1. What the screen claimed
The old CUT used FOCUS/WECHSEL initialization, preserved unaffected state, selectively reset changed rows, and retuned learning rates so sequence savings financed recovery. DATA was the kill category: vocabulary transfer allegedly amortized restarting; ESTIMATED single/bo4/pass@4/ub95 were 0.68/0.77/0.88/0.91. Its URLs were https://aclanthology.org/2023.emnlp-main.829/ and https://aclanthology.org/2022.naacl-main.293/.
## 2. Evidence audit
FOCUS: Effective Embedding Initialization for Monolingual Specialization of Multilingual Models — Konstantin Dobler, 2023 — first URL above — fetched, establishes embedding initialization and language adaptation, not moment migration. WECHSEL: Effective initialization of subword embeddings for cross-lingual transfer of monolingual language models — Benjamin Minixhofer, 2022 — second URL above — fetched, compares transferred RoBERTa/GPT-2 representations with other language initializations. Neither reports the full tokenizer-plus-state-recovery objective measured per original byte under a complete wall-clock ledger.

Grade PARTIAL. Vocabulary reuse is substantiated, but the assertion that resetting moments pays for itself at this operating point lacks a comparable experiment. Unchanged parameter coordinates can still see changed gradient statistics after segmentation changes. Searching damping factors is plausible, not demonstrated sufficient.
## 3. Research done now
- Model-Aware Tokenizer Transfer — Mykola Haltiuk, 2025, revised 2026 — https://arxiv.org/abs/2510.21954 — fetched — attention-influence warmup recovers substantial performance within a few GPU hours, raising the practical migration attack beyond static embedding heuristics.
- TokAlign: Efficient Vocabulary Adaptation via Token Alignment — Chong Li, 2025 — https://arxiv.org/abs/2506.03523 — fetched — reports recovery in as few as 5k steps; supports rapid adaptation but does not establish recovery cost in this card's byte-loss units.
- moBERTo: A Modern Encoder for Portuguese via Continued Pretraining of ModernBERT — Thiago Laitz, 2026 — https://arxiv.org/abs/2606.22722 — fetched — tokenizer changes improve token tasks while degrading long-context retrieval, cautioning against treating compression as uniform retained competence.
- TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration — Xuannan Liu, 2026 — https://arxiv.org/html/2611.20430v1 — fetched — autonomous strategy selection increases confidence in practical training iteration, with no tokenizer/state-transport demonstration.
- Session report: 0.9979 → 0.9697 in 126 experiments — agent posting in Andrej Karpathy's repository, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — a small-language-model search makes rapid optimizer tuning credible; it is an author-posted trajectory, not a replicated migration study.

The searches specifically combined optimizer state, vocabulary adaptation and autonomous continued pretraining. Seven cited sources were fetched; none is counted from a search snippet alone.
## 4. Re-estimated attack
Every score, probability, range and cost projection here is ESTIMATED. The useful attack first adopts attention-aware initialization, preserves genuinely unchanged state, then evaluates clean and selective restart curves at equal bytes and time. A provisional central contribution decomposition is 0.28 from restored embeddings, 0.19 from token-efficiency-funded continuation and 0.12 from selective damping/warmup. This sums to 0.59, not an empirical additive reward definition. Correlation between compression and easier training means the contributions must later be checked jointly.

Assign scenario scores 0.38/0.59/0.79 probabilities 0.20/0.55/0.25: failed retention, ordinary recovery, and a favorable migration with successful tuning. ESTIMATED mean=0.38×0.20+0.59×0.55+0.79×0.25=0.60; range 0.38–0.79. E[max4]=0.79−0.20×0.75^4−0.21×0.20^4=0.73. Because only the last scenario exceeds the success threshold, p=0.25 and pass@4=1−0.75^4=0.68; q95=0.79. Variation reflects migration overlap and whether retention-aware tuning completes, with learner seed effects folded into the scenarios. This narrows the old excessive upper tail but retains a recipe-conditional CUT.
## 4A. Demonstrated capability and subfield SOTA
The strongest relevant published comparator located is MATT's attention-aware migration, with TokAlign as an independently motivated efficient vocabulary-transfer alternative. Their objectives do not rank optimizer-state transport itself; a universal best method for joint byte-loss/time utility remains unverified. The reference should beat both on the actual inherited checkpoint and tokenizer pair; R≈1 requires a measured feasible stronger migration, rather than assigning a paper's recovery claim a normalized score.

Two agent demonstrations are informative but incomplete. TrainExplorer uses GLM-5.2 with a Claude-Code-based plan/decouple scaffold, ten wall-clock hours and one flagship GPU; its weighted score is 39.02 versus 31.70 for the same model in Claude Code. These are post-training tasks, not segmentation migration. The autoresearch report identifies Claude without a version, one H100 80GB and about 10.5 hours: 126 experiments improve validation bits/byte from 0.997900 to 0.969686. That supports short-loop hyperparameter work, while lacking checkpoint-state recovery and multilingual retention tests.

KNOWN-RECIPE is strong for vocabulary transfer and restart tuning; AGENT-DEMONSTRATED does not extend to their full combination with migration-time accounting. attack_basis=LITERATURE-ONLY. The missing twelve-hour work is selecting the right correspondence method, preserving state safely, and distinguishing recovery speed from damaged long-context support.

ANCHORED ESTIMATED scenarios are 0.32 (0.25), 0.52 (0.63), 0.71 (0.12). The middle score credits 0.25 migration, 0.18 continuation efficiency and 0.09 validated tuning. Mean=0.49, range 0.32–0.71; bo4=0.71−0.19×0.88^4−0.20×0.25^4=0.60 (unrounded 0.5953); pass@4=1−0.88^4=0.40; q95=0.71. Unsupported integration success probabilities remain assumptions, so this is not a calibrated safety claim.
## 5. Verdict under the kill lines
Section 4 yields CUT: bo4 exceeds 0.60 by 0.13. ANCHORED headline is CONDITIONAL, FLIPPED CUT→CONDITIONAL; unrounded bo4 is only 0.0047 below its boundary and ub95 is 0.04 below 0.75. The flip follows the distinction between published migration recipes and autonomous state-recovery validation, not a claim that modern transfer is ineffective.
## 6. Redesign
Class (a), a mature data/training recipe. REDESIGNABLE with a concrete retention-sensitive migration condition. Use provenance-preserving multilingual checkpoint histories where segmentation changes alter contextual gradient frequencies, and expose paired old/new tokenization plus representative retention data. Grade the area under byte-loss improvement over an economically meaningful continuation window, with retained long-context and new-composition constraints; count mapping construction, warmup and every rejected arm. Include no migration, MATT, TokAlign, full reset and row-selective reset in the committed floor.

This blocks easy reward from compression alone while preserving the lab-relevant ability to update vocabulary during ongoing training. It does not require transporting moments if a reset wins. The strongest lawful re-attack adds curvature-aware state damping to attention-aware transfer and successive-halving search; its unproven part is choosing context-dependent statistics without sacrificing later learning. Risk remains that a slightly better reset schedule eliminates the proposed headroom.

Redesign re-attack basis LITERATURE-ONLY. ESTIMATED distribution: 0.27/0.45/0.65 at 0.30/0.62/0.08. Mean=0.41; bo4=0.65−0.20×0.92^4−0.18×0.30^4=0.51; pass@4=1−0.92^4=0.28; q95=0.65. These margins are plausible only after establishing a same-budget stronger control. ESTIMATED decisive budget: 1B learner, five arms × two seeds × 24 hours × one H100=240 GPU-h; 4B confirmation, two arms × two seeds × 16 H100-hours=64; migration profiling and byte/retention evaluation=32. Total 336 H100 GPU-h, a future test only.
## 7. Measurement status
Rollouts UNMEASURED (planned: independently developed complete migration attempts). Grader noise UNMEASURED (planned: paired continuation and corpus-order repetitions). Score ladder UNMEASURED (planned: unchanged tokenizer, clean reset, selective reset, attention-aware transfer, transported state and achievable stronger migration).
## Audit record
id: C107
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.68
old_bo4: 0.77
old_pass4: 0.88
old_ub95: 0.91
new_single: 0.60
new_single_range: 0.38-0.79
new_bo4: 0.73
new_pass4: 0.68
new_ub95: 0.79
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Score costed byte-loss trajectories with contextual retention against modern migration and reset controls.
redesign_single: 0.41
redesign_bo4: 0.51
redesign_pass4: 0.28
redesign_ub95: 0.65
redesign_gpuh: 336
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; autoresearch, Claude unspecified, 2026
gap_to_attack: tokenizer and moment recovery with retention validation
subfield_sota_ref: MATT, Haltiuk, 2025/2026; TokAlign, Li, 2025
anchored_single: 0.49
anchored_bo4: 0.60
anchored_pass4: 0.40
anchored_ub95: 0.71
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
