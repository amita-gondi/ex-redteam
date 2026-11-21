# C002 — Learn a curriculum from optimizer blind spots — screen audit
## 1. What the screen claimed
The proposed attack inferred prerequisites from compiler failures, scheduled by learning progress, rehearsed common syntax and probed acquisition transitions. The screen's ESTIMATED single/bo4/pass@4/ub95 were 0.53/0.63/0.54/0.79. Although its author wrote CONDITIONAL, the final TSV and reconciliation say CUT, category RECON: the suggested history-crossed revision had not been incorporated and the forecasts crossed kill lines. The old URLs were:
- https://proceedings.mlr.press/v70/graves17a
- https://arxiv.org/abs/1707.00183

## 2. Evidence audit
Automated Curriculum Learning for Neural Networks — Alex Graves, 2017, fetched through https://proceedings.mlr.press/v70/graves17a.html — supports progress-driven bandit scheduling on LSTM curricula. Teacher-Student Curriculum Learning — Tambet Matiisen, 2017, fetched at the old arXiv URL — supports both progress targeting and revisiting deteriorating skills on arithmetic and navigation. Neither extracts prerequisite graphs from compiler traces or resolves optimizer-history barriers in a code pretraining learner.

Grade: PARTIAL. Adaptive scheduling and forgetting-aware rehearsal are demonstrated ingredients. The assertion that short continuations distinguish representational absence from temporarily unhelpful optimizer state is unverified on a comparable model, work budget and executable-coverage metric. A compiler's dependency graph describes language semantics; it need not describe the learner's acquisition path.

## 3. Research done now
- Curriculum Learning for Small Code Language Models — Marwa Naïr, 2024 — https://arxiv.org/abs/2407.10194 — fetched — Finds more benefit for code execution than completion, supporting a schedule attack on this objective. Its very small GPT learners are not evidence of reliable billion-parameter syntax acquisition.
- Beyond Random Sampling: Efficient Language Model Pretraining via Curriculum Learning — Yang Zhang, 2025, revised 2026 — https://arxiv.org/abs/2506.11300 — fetched — Broad pretraining experiments support warmup curricula and efficient ordering. This strengthens the conventional schedule floor, without testing absent syntax gradients or history-specific reversals.
- Accelerating Large Language Model Pretraining via LFR Pedagogy: Learn, Focus, and Review — Neha Prakriya, 2025 — https://aclanthology.org/2025.conll-1.18/ — fetched — Demonstrates dynamic emphasis on difficult and forgettable data during pretraining. It makes rehearsal plus progress selection a serious combined attack rather than two speculative independent tricks.
- What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning — Yaning Jia, 2025 — https://arxiv.org/abs/2510.19099 — fetched — Shows curriculum direction depends on model and task. This lowers confidence that compiler-topological ordering alone transfers, though mathematics post-training is only an analogue of the proposed code setting.

Searches covered execution curricula and progress-sensitive sampling; no source implements the complete recipe on fresh compiler semantics.

## 4. Re-estimated attack
ESTIMATED incremental credits: prerequisite ordering 0.22, progress allocation 0.16, charged rehearsal/transition probes 0.12, totaling 0.50. A short probe can miss the benefit of longer precursor exposure; diagnosis competes with useful continuation work. Native anchors remain unmeasured.

ESTIMATED R={0.36,0.53,0.67}, masses {0.30,0.56,0.14}, represent mistimed prerequisites, useful adaptation and transferable transition diagnosis. Research-path variation dominates; acquisition and retention also depend on learner seed. These are judgmental masses, not published success rates.

ESTIMATED single=0.30×0.36+0.56×0.53+0.14×0.67=0.50, with range 0.36–0.67. Independence of researcher restarts conditional on a fixed construct block gives ESTIMATED bo4=0.67−0.14×0.86^4−0.17×0.30^4=0.59. Since only the top state reaches 0.60, p=0.14 and ESTIMATED pass@4=1−0.86^4=0.45. The lower states contain cumulative probability 0.86; hence ESTIMATED ub95=0.67. This percentile summarizes the stated scenarios and does not certify an extrapolation to an unavailable researcher.

The old tail falls because curriculum speedups do not establish transition diagnosis or justify a separate projection bonus.

## 4A. Demonstrated capability and subfield SOTA
SOTA for the nearest large-scale curriculum objective is Zhang's Beyond Random Sampling (2025/2026, fetched above): its strongest reported warmup ordering gives sustained downstream improvement, while Naïr's code-execution evidence concerns much smaller learners. Neither establishes optimizer-blind-spot recovery. Anchor the floor to a tuned progress/review and warmup portfolio, and require a same-token adaptive reference to beat that portfolio on executed constructs. A published numerical R≈1 mapping does not exist.

- Session report: 0.9979 → 0.9697 in 126 experiments — agent posting in Andrej Karpathy's autoresearch, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched. Claude, version unspecified, reports interacting training improvements over approximately ten and a half hours on one H100. This supports rapid schedule/optimizer searches, but is a self-report about a short validation loop, not rare-syntax transfer.
- RE-Bench — Hjalmar Wijk, 2024/2025 — https://arxiv.org/html/2411.15114v2 — fetched. METR-scaffolded o1-preview/Claude 3.5 Sonnet achieve about four times average expert score at two hours, but lose at thirty-two aggregate hours. Allocations reach six H100s. This establishes implementation/search, not curriculum-transition diagnosis.

Basis LITERATURE-ONLY: a KNOWN-RECIPE sampler exists, but AGENT-DEMONSTRATED history-conditioned syntax scheduling does not. The twelve-hour gap is diagnosing and validating a support transition whose observation may itself take a long continuation.

ANCHORED, ESTIMATED states {0.28,0.45,0.64}, masses {0.36,0.54,0.10}, represent progress-only, useful precursor scheduling and successful history diagnosis. Single=0.36×0.28+0.54×0.45+0.10×0.64=0.41, range 0.28–0.64; bo4=0.64−0.19×0.90^4−0.17×0.36^4=0.51; pass@4=1−0.90^4=0.34; ub95=0.64, with CDF 0.90 below it. Independence is conditional on construct family; parameter choices and normalization are assumed.

## 5. Verdict under the kill lines
The section 4 evidence re-estimate is CONDITIONAL near bo4. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; ESTIMATED bo4 has 0.09 numerical margin, pass@4 0.16, single 0.29 and ub95 0.11. The condition now rests on unmeasured reference headroom and the history-crossing intervention, not an asserted numeric kill. Autoresearch proves short-loop integration is possible; it does not demonstrate this slower acquisition mechanism. The headline judgment therefore rests on assumption.

## 6. Redesign
The anchored condition requires the history-crossed sampler below. Its re-attack basis remains LITERATURE-ONLY.
Cause (c): compiler-visible prerequisites can leak a nearly sufficient static plan. Construct paired training histories with the same current error signature but different acquired internal features: one benefits from continued precursor exposure while the other requires retiring that exposure and rehearsing a sibling construct. All previous training data, optimizer traces and compiler semantics remain available. Freeze the learner and optimizer; permit a schedule policy to use authorized history and charged probes. Evaluate newly composed constructs plus common-syntax retention, using the same observable regimes in development and hidden instances.

Paired continuations must demonstrate an adaptive sampler switching correctly at equal delivered tokens. Without a feasible reference, stop building. The practical target is code pretraining across capability transitions.

The strongest re-attack combines compiler planning, LFR-style progress/review, history features, change-point detection and successive-halving probes. A semantic graph cannot choose the exposure sign, while undirected probing spends training on the wrong regime. Its unresolved challenge is finding a history statistic that predicts which intervention pays before the full continuation. This is an explicitly testable hypothesis, not demonstrated resistance.

ESTIMATED redesigned outcomes {0.25,0.41,0.61}, weights {0.38,0.53,0.09}, encode static-plan failure, useful but imperfect adaptation and discovery of that statistic. Single=0.38×0.25+0.53×0.41+0.09×0.61=0.37; bo4=0.61−0.20×0.91^4−0.16×0.38^4=0.47; pass@4=1−0.91^4=0.31; ub95=0.61. REDESIGNABLE, subject to affordable history/reference validation. A simple gradient-ratio threshold is a serious residual shortcut and must be an explicit control.

Pilot GPU-h ESTIMATED: 1B code learner, four policies, two histories, three seeds, eight H100-hours per continuation, plus twenty-four for execution/retention evaluation: 4×2×3×8+24=216. The continuation must span the transition; this excludes full researcher certification.

## 7. Measurement status
Rollouts UNMEASURED (planned schedule-only research attempts with a delivered-token ledger). Grader noise UNMEASURED (planned matched-seed acquisition curves around each history's transition). Score ladder UNMEASURED (planned executable coverage for random, prerequisite, progress/review, history-aware and stronger feasible policies).

## Audit record
id: C002
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 8
old_single: 0.53
old_bo4: 0.63
old_pass4: 0.54
old_ub95: 0.79
new_single: 0.50
new_single_range: 0.36-0.67
new_bo4: 0.59
new_pass4: 0.45
new_ub95: 0.67
new_verdict: CONDITIONAL
binding_line: bo4>0.60
flip: CUT->CONDITIONAL
kill_cause_class: c
redesign_status: REDESIGNABLE
redesign_oneline: Require observable training-history distinctions to determine opposite curriculum transitions under identical current compiler errors.
redesign_single: 0.37
redesign_bo4: 0.47
redesign_pass4: 0.31
redesign_ub95: 0.61
redesign_gpuh: 216
attack_basis: LITERATURE-ONLY
demonstrated_ref: autoresearch, Claude unspecified version, 2026; RE-Bench, o1-preview and Claude 3.5 Sonnet METR scaffold, 2024/2025
gap_to_attack: Diagnose long-continuation optimizer support transitions rather than tune a fast validation loop
subfield_sota_ref: Pretraining warmup curriculum gains, Zhang Beyond Random Sampling, 2025/2026
anchored_single: 0.41
anchored_bo4: 0.51
anchored_pass4: 0.34
anchored_ub95: 0.64
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
