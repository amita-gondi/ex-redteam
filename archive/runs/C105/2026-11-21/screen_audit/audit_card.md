# C105 — Train a verifier, then make the learner harder for it honestly — screen audit
## 1. What the screen claimed
CodeRL-style critic training and AlphaCodium-style test-centered generation supplied execution labels, refreshed negatives and diverse correct positives, with exact execution routing when affordable. The screen CUT under TRAIN with ESTIMATED single 0.76, bo4 0.84, pass@4 0.96 and ub95 0.95 because no binding verification bottleneck had been specified. It cited:
- https://arxiv.org/abs/2207.01780
- https://arxiv.org/abs/2401.08500

## 2. Evidence audit
CodeRL demonstrates critic-assisted code learning and AlphaCodium improves test-centered generation. Neither establishes that a frontier researcher will train both models, generate balanced execution-labeled data and retain unfamiliar correct solution modes in this budget. AlphaCodium's inference scaffold cannot be counted directly as improvement in the final trained learner.

Grade: PARTIAL. The literature now contains much closer co-evolution recipes than the screen used, strengthening the scientific baseline. However, available executions label sampled behavior, not universal semantic correctness, and an execution-backed bank does not automatically solve the honest-positive generalization problem.

## 3. Research done now
- *CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning* — Hung Le et al., 2022 — https://arxiv.org/abs/2207.01780 — fetched — Validates learned critics and execution feedback; it does not demonstrate autonomous construction of the complete adaptive pair.
- *Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering* — Tal Ridnik et al., 2024 — https://arxiv.org/abs/2401.08500 — fetched — Raises confidence in training-data generation through tests, while inference-time orchestration remains different from trained capability.
- *Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning* — Yinjie Wang et al., 2025 — https://arxiv.org/abs/2506.03136 — fetched — CURE directly co-trains the relevant abilities and reports improved code accuracy, materially strengthening the known recipe beyond a static verifier.
- *Scaling Agentic Verifier for Competitive Coding* — Zeyao Ma et al., 2026 — https://proceedings.mlr.press/v306/ma26av.html — fetched — Discriminative input generation supports adaptive tests; this is a purpose-built training pipeline rather than demonstrated researcher discovery during one task.
- *Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents* — Xing Zhang et al., 2026 — https://arxiv.org/html/2607.12790v1 — fetched — Co-evolution can preserve oracle-driven gains, but reported metric gaming and detector repair undermine unconditional trust in the learned checker.
- *Singularity-Bench: Can Agents Build Agents?* — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — A timed coding-RL engineering task demonstrates relevant agent competence; its trusted fixed rewards omit the verifier-construction obligation.

## 4. Re-estimated attack
ESTIMATED gain contributions are 0.24 from reliable execution labels, 0.23 from CURE-like joint updates and 0.18 from diverse-positive replay, hard-negative refresh and routing. Single=0.65. These increments describe a plausible sequential improvement over the inherited static-verifier learner; exact reward weights and competent-floor placement are still unspecified. The literature directly supports co-training, but the last allocation assumes data coverage and tuning successfully transfer.

ESTIMATED outcomes are probability 0.15 at R=0.32 when training produces a brittle checker, 0.65 at 0.66 for effective standard co-training, and 0.20 at 0.84 for robust execution-backed refinement. Mean=0.15×0.32+0.65×0.66+0.20×0.84=0.65, range 0.32–0.84. Bo4=0.32+0.34(1−0.15⁴)+0.18(1−0.80⁴)=0.77; pass@4=1−0.15⁴=1.00 because p=0.85; ub95=0.84. Spread reflects whether the evolving positive distribution is covered, plus learner/verifier training interactions. It is not modeled as a universal noise offset. Compared with the screen, the mean and tails fall while the explicit conventional-success branch still produces a strong recipe-level CUT. Actual seed variability and audit error rates remain unknown.

## 4A. Demonstrated capability and subfield SOTA
CURE's reported ReasonFlux-Coder-7B/14B results improve code generation by 5.3% and best-of-N accuracy by 9.0% over the study's starting models. These are source-reported gains, not C105 rewards. The newer agentic-verifier work provides a stronger input-generation comparator, but there is no verified universal champion across correctness, honest rejection and complete training cost. A valid R≈1 must come from a stronger same-budget learner that also accepts independently correct algorithm families; published coding accuracy alone cannot anchor it.

Double Ratchet uses Opus 4.7 throughout its skill/metric loops and reports retaining 106% of oracle-driven improvement on MBPP+ after one hundred skill rounds. Full elapsed time and compute are unspecified, and the documented detector repair's unaided status is unverified. Its artifacts are metrics and skills, rather than a trained coding learner/verifier pair. Singularity-Bench's Opus 5.5+Claude Code codes and trains a coding-RL system for twelve hours on four GB300s, reporting resolve rate 0.533. That demonstrates substantial autonomous RL integration, while its fixed verifier and repository-resolution objective leave C105's adaptive false-rejection constraint untested.

KNOWN-RECIPE includes genuine coder/tester co-evolution. The entire twelve-hour integration is not AGENT-DEMONSTRATED; attack_basis=LITERATURE-ONLY. The remaining autonomous obligation is maintaining useful verifier discrimination while the learner discovers correct algorithms outside its training bank, and confirming the final learner actually improves.

ANCHORED ESTIMATED masses are 0.25 at 0.20, 0.63 at 0.46 and 0.12 at 0.69. Single=0.42, range 0.20–0.69; bo4=0.20+0.26(1−0.25⁴)+0.23(1−0.88⁴)=0.55; pass@4=1−0.88⁴=0.40; ub95=0.69. This retains meaningful success probability in light of both close human recipes and actual RL-engineering demonstrations. The mapping to rewards remains an explicit assumption, not a calibrated benchmark conversion.

## 5. Verdict under the kill lines
Section 4 says CUT, primarily through ESTIMATED bo4 0.77. The headline ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL: unrounded bo4 is approximately 0.55, within 0.05 of its boundary. CURE strengthens the baseline, but neither its human-designed recipe nor the fetched agent runs demonstrates the complete learner/verifier research attack. The undefined verification cost and positive-audit weighting must be resolved before accepting either saturation or resistance.

## 6. Redesign
Class (a): execution-backed training can replace a weak learned checker. REDESIGNABLE. Instantiate code families with meaningful verification costs, such as tensor programs whose long-sequence reductions and shape-dependent behavior require substantial execution. Publish reference semantics, representative input regimes and independent correct implementations; dev must exhibit the same semantic interactions as evaluation. Charge execution and test generation, and allow exact checking whenever affordable. First measure the complete CURE/input-generation/replay floor against a feasible stronger pair; retain only regimes where selective verification saves real training work without sacrificing honest positives.

The combined execution-labeling, generic co-training and diversity replay recipe now must acquire discriminating tests for new solution modes rather than cheaply exhaust all candidates. It remains free to use symbolic checks, metamorphic tests and full execution. The strongest re-attack combines those with uncertainty routing; its basis is LITERATURE-ONLY. A cheap complete checker or simple positive family classifier could still erase the gap. Frontier labs would value reliable verifier-guided code training, provided the stronger control demonstrates attainability rather than an artificially starved verification budget.

ESTIMATED redesign probabilities 0.30 at 0.17, 0.60 at 0.38 and 0.10 at 0.63 give single 0.34; bo4=0.17+0.21(1−0.30⁴)+0.25(1−0.90⁴)=0.46; pass@4=0.34; ub95=0.63. Pilot cost is ESTIMATED 4 arms×2 seeds×8 one-H100 hours for a 4B learner=64, plus 4×2×2 hours for a 1B verifier=16, plus 16 generation and 16 independent evaluation hours: 112 H100 GPU-h. CPU execution is separately metered, never relabeled GPU time.

## 7. Measurement status
Rollouts UNMEASURED (planned independent joint-training attacks with exact-execution controls). Grader noise UNMEASURED (planned repeated paired training and independently authored honest-positive banks). Score ladder UNMEASURED (planned execution-only, static critic, co-evolved pair, reference and stronger checked learner).

## Audit record
id: C105
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.76
old_bo4: 0.84
old_pass4: 0.96
old_ub95: 0.95
new_single: 0.65
new_single_range: 0.32-0.84
new_bo4: 0.77
new_pass4: 1.00
new_ub95: 0.84
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Make discriminating verification consequential under real execution costs while preserving observable semantics and independently correct solutions.
redesign_single: 0.34
redesign_bo4: 0.46
redesign_pass4: 0.34
redesign_ub95: 0.63
redesign_gpuh: 112
attack_basis: LITERATURE-ONLY
demonstrated_ref: Double Ratchet, Opus 4.7, 2026; Singularity-Bench coding RL, Opus 5.5+Claude Code, 2026
gap_to_attack: budget-matched trained verifier and learner with robust honest-positive acceptance
subfield_sota_ref: ReasonFlux-Coder/CURE, Wang et al., 2025; agentic verifier, Ma et al., 2026
anchored_single: 0.42
anchored_bo4: 0.55
anchored_pass4: 0.40
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
