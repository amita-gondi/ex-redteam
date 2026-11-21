# C069 — Finite policy losses without deleting informative extremes — screen audit
## 1. What the screen claimed
Stable log-space arithmetic, bounded updates, GSPO/DAPO alternatives, adaptive KL, policy refresh and coverage-aware replay formed the old combined attack. The screen gave CUT/TRAIN with ESTIMATED single 0.62, best-of-four 0.72, pass@4 0.78 and upper-95% 0.88, because no tail mechanism was specified that defeated that stack. Its URLs were:
- https://docs.pytorch.org/docs/stable/generated/torch.logsumexp.html
- https://arxiv.org/abs/2507.18071
- https://papers.nips.cc/paper_files/paper/2025/file/a4277440d50f1f15d2cb4c14f7e0c0d2-Paper-Conference.pdf

## 2. Evidence audit
GSPO and DAPO demonstrate actual language-model RL gains; logsumexp establishes only an arithmetic primitive. None measures success/coverage recovery on the card's proposed informative extremes at its fixed rollout allowance. The screen correctly distinguished overflow prevention from estimator quality, then assumed the latter was adequately solved by composition. Grade: PARTIAL, because stable training is evidenced but selective retention of rare useful trajectories remains a different claim.

## 3. Research done now
Research searched sequence-weighted, smooth-gated and contemporary off-policy losses. Every entry was fetched; all card-level numeric forecasts are ESTIMATED.
- torch.logsumexp — PyTorch, 2026 version 2.15 documentation — https://docs.pytorch.org/docs/2.15/generated/torch.logsumexp.html — fetched — the original stable URL redirects; stabilized reduction helps avoid overflow without identifying useful tails.
- Group Sequence Policy Optimization — Chujie Zheng et al., 2025 — https://arxiv.org/abs/2507.18071 — fetched — demonstrated Qwen-family stability supports a powerful sequence-level control, but sequence clipping can discard localized valid signal.
- DAPO: An Open-Source LLM Reinforcement Learning System at Scale — Qiying Yu et al., 2025 — https://papers.nips.cc/paper_files/paper/2025/file/a4277440d50f1f15d2cb4c14f7e0c0d2-Paper-Conference.pdf — fetched — reports 50 AIME-2024 points on Qwen2.5-32B, establishing an empirical combined recipe rather than just guard placement.
- Soft Adaptive Policy Optimization — Chang Gao et al., 2025 — https://arxiv.org/abs/2511.20347 — fetched — smooth token gates explicitly preserve signal that hard sequence clipping loses; this strengthens the attack beyond the earlier screen.
- VESPO: Variational Sequence-Level Soft Policy Optimization for Stable Off-Policy LLM Training — Guobin Shen et al., 2026 — https://arxiv.org/abs/2602.10693 — fetched — reports stable dense/MoE training at severe staleness with a bounded reshaping kernel, while emphasizing that unmodified importance sampling has a variance problem.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — leading autonomous RL systems use logprob correction and validation, yet weaker systems make many ineffective updates; stability is not universal.
- GPT-6.2 System Card, PostTrainBench Lite — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — provides a small-model training-search anchor but does not evaluate informative-tail coverage.

## 4. Re-estimated attack
Above a repaired stable implementation, ESTIMATED 0.23 could come from selecting token, sequence or smooth-gated weighting; ESTIMATED 0.17 from refresh/KL/group-size control; ESTIMATED 0.16 from replay and coverage-based selection. Those increments concern downstream success with mandatory coverage. Arithmetic finiteness earns no separate improvement. Replacing an estimator is permitted here because the submission is a loss, but its objective and finite-group semantics must be declared rather than silently changed during evaluation.

An ESTIMATED recipe distribution R={0.33,0.59,0.77}, probabilities {0.25,0.50,0.25}, gives single=0.0825+0.2950+0.1925=0.57, range 0.33–0.77. The spread represents whether validation identifies a loss that retains rare skills rather than simply reducing variance. ESTIMATED best-of-four=0.77−0.18×0.75^4−0.26×0.25^4=0.71. Only the high mode passes, so ESTIMATED p=0.25, pass@4=1−0.75^4=0.68 and upper-95%=0.77. The old mean and tail both decrease, despite stronger contemporary algorithms, because the card-specific coverage claim has no comparable experiment.

## 4A. Demonstrated capability and subfield SOTA
Among fetched same-subfield results, VESPO is the newest strong matched off-policy comparator, reporting gains over recent reshaping baselines in math/code; SAPO supplies a production-used smooth-gating alternative. Neither establishes a universal best loss across tail regimes. The attainable reference must be measured against a joint VESPO/SAPO/GSPO/DAPO search under identical rollout accounting. R≈1 for signal-preserving coverage is therefore not publicly anchored; finite loss values cannot serve as its proxy.

For demonstrated agents, Opus 5.5+Claude Code constructs asynchronous GRPO in Singularity-Bench over twelve hours on four GB300s, using truncated importance weights and a held-out checkpoint selector, reaching 0.533 versus Miles' 0.539. That directly supports integrating a conventional stable learner. It does not test new rare-reward mechanisms or guarantee informative extreme updates survive. GPT-6.2 Astra's tool-enabled PostTrainBench Lite closes a reported 74.79% of the base-to-instruct gap with five hours on one H100 across 1.7B–4B models. This supports empirical post-training search at relevant scale, but the aggregate spans ordinary benchmarks and does not establish robust tail-estimator discovery. Complete scaffold details are not available on the vendor page.

The numerical and estimator components are KNOWN-RECIPE; rare-signal preservation at fixed rollout cost is not AGENT-DEMONSTRATED. attack_basis=LITERATURE-ONLY for the strongest full attack. In twelve hours the agent must collect enough diagnostic rare events, distinguish genuine learning signal from excessive variance and validate coverage before exhausting its rollout ledger.

Anchored ESTIMATED outcomes {0.28,0.48,0.68}, probabilities {0.30,0.58,0.12}, yield single=0.0840+0.2784+0.0816=0.44, range 0.28–0.68; best-of-four=0.68−0.20×0.88^4−0.20×0.30^4=0.56; pass@4=1−0.88^4=0.40; upper-95%=0.68. The favorable mode requires actual coverage transfer; its probability is an ESTIMATED assumption, not a measured literature success frequency.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT, mainly best-of-four ESTIMATED 0.11 above the line. ANCHORED: CONDITIONAL, FLIPPED CUT→CONDITIONAL, with best-of-four only ESTIMATED 0.04 below 0.60. Fetched smooth-loss methods strengthen the human recipe, whereas agent results demonstrate ordinary RL construction without this coverage capability. An unmeasured reference or upper-tail fit remains a release hold rather than evidence of resistance.

## 6. Redesign
Cause (b), REDESIGNABLE. Define clean, executable-reward tool tasks where new skills create rare successful prefixes, while changing action-branching structure generates large but unhelpful importance ratios. Publish causal trace features and representative histories; vary their compositions independently of ratio magnitude. There is no reward corruption or added observation noise. Permit the submitted learner to allocate groups and adapt its weighting using authorized history, and score exact skill coverage at fixed total generations. Include smooth weighting, sequence estimators, refresh and coverage replay in the floor.

The strongest re-attack adds a history-conditioned selector to those losses. It must infer which extremes precede reusable skill growth rather than apply one global gate, a LITERATURE-ONLY capability on fetched evidence. ESTIMATED R={0.23,0.42,0.61}, probabilities {0.41,0.52,0.07}, yields single=0.36, best-of-four=0.61−0.19×0.93^4−0.19×0.41^4=0.46, pass@4=1−0.93^4=0.25, upper-95%=0.61. The risk is a simple trace-conditioned gate solving all regimes; test that competitor and inspect overlap with T18 before building. ESTIMATED check: 3B policy with 3B frozen reference/value component as needed, four estimators × three seeds × ten hours × four H100s=480; probes and independent coverage evaluation add 96, totaling 576 H100-h. Reference feasibility must precede this pilot.

## 7. Measurement status
Rollouts UNMEASURED (planned autonomous estimator searches under charged generation); grader noise UNMEASURED (planned independent training/rollout seed decomposition); score ladder UNMEASURED (planned stable arithmetic, GSPO, SAPO, VESPO, replay/refresh combination and history-aware control).

## Audit record
id: C069
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.62
old_bo4: 0.72
old_pass4: 0.78
old_ub95: 0.88
new_single: 0.57
new_single_range: 0.33-0.77
new_bo4: 0.71
new_pass4: 0.68
new_ub95: 0.77
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Select useful rare updates from disclosed causal histories with clean verifiers after modern smooth losses enter the floor.
redesign_single: 0.36
redesign_bo4: 0.46
redesign_pass4: 0.25
redesign_ub95: 0.61
redesign_gpuh: 576
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench GRPO, Opus 5.5+Claude Code, 2026; PostTrainBench Lite, GPT-6.2 Astra, 2026
gap_to_attack: fixed-budget rare-skill coverage from informative extreme ratios
subfield_sota_ref: VESPO, Shen et al., 2026; SAPO, Gao et al., 2025
anchored_single: 0.44
anchored_bo4: 0.56
anchored_pass4: 0.40
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
