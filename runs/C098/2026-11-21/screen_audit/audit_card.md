# C098 — Report and repair censored training failures — screen audit
## 1. What the screen claimed
The screen proposed reconstructing launches, optimizing complete-population delivered utility with SMAC3, modeling failure separately from conditional quality and confirming configurations across independent failure groups. Its ESTIMATED single/bo4/pass@4/ub95 were 0.82/0.89/0.99/0.97; it CUT under EXP because ordinary failure-aware selection directly addresses a success-only leaderboard. Sources cited:
- https://automl.github.io/SMAC3/latest/api/smac/scenario/
- https://automl.github.io/SMAC3/latest/3_getting_started/

## 2. Evidence audit
SMAC3 supports crash costs, trial budgets and algorithm configuration, so its relevance is concrete. However, API capabilities do not demonstrate reconstructing partially missing launches, learning correlated causes or producing a calibrated and more useful training recipe. The old forecast implicitly treated all those integration steps as completed.

Grade: PARTIAL. Once the launch denominator is trusted, observed failure utility needs no counterfactual successful-loss imputation. That is a valid simplification, but it does not establish enough learning headroom or enough independent evidence to award the old near-certain success probability.

## 3. Research done now
- *Scenario* — AutoML/SMAC3, 2026 documentation snapshot — https://automl.github.io/SMAC3/latest/api/smac/scenario/ — fetched — Explicit failed-trial costs make crash-aware optimization a supported mechanism; correlated-failure calibration is not a reported capability result.
- *Getting Started* — AutoML/SMAC3, 2026 documentation snapshot — https://automl.github.io/SMAC3/latest/3_getting_started/ — fetched — Supplies the configuration interface, reducing implementation uncertainty without proving scientific improvement on failed training campaigns.
- *Can LLMs Beat Classical Hyperparameter Optimization Algorithms? A Study on autoresearch* — Fabio Ferreira et al., 2026 — https://arxiv.org/html/2603.24647v1 — fetched — Actually evaluates searches with OOM penalties. The positive hybrid-search result raises this attack; its restricted search space and longer budget limit transfer.
- *Session report: 0.9979 → 0.9697 in 126 experiments* — Claude agent/Andrej Karpathy repository, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — Retained failed and discarded trials demonstrate practical short-loop experimentation, but not a reliability-calibrated final policy under shared causes.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — Autonomous planning and controlled training changes improve a benchmark aggregate; the paper does not demonstrate discovery of correlated failure mechanisms.

## 4. Re-estimated attack
The ESTIMATED literature-composition gain budget is 0.12 from denominator correction, 0.35 from selecting reliable productive settings, 0.18 from memory/precision/restart repairs and 0.10 from calibrated final reporting: single 0.75. These allocations require a weak inherited success-only incumbent; denominator repair earns no direct scientific reward. Calibration's weight is unspecified, so the allocation is conditional on a useful-learning-dominated score rather than a reward for merely reporting failures.

Use probability 0.10 at R=0.45 when conservative choices sacrifice learning, 0.60 at 0.73 for successful complete-ledger tuning and 0.30 at 0.89 for effective causal repair. ESTIMATED mean=0.10×0.45+0.60×0.73+0.30×0.89=0.75, range 0.45–0.89. E[max4]=0.45+0.28(1−0.10⁴)+0.16(1−0.70⁴)=0.85. Since p=0.90, pass@4=1−0.10⁴=1.00; ub95=0.89. Spread reflects which failure groups are diagnosed and whether safe settings retain quality; no measured noise estimate is embedded. These values lower the old mean and tail substantially, while leaving the recipe-level CUT intact.

## 4A. Demonstrated capability and subfield SOTA
The closest field comparator located is Ferreira et al.'s hybrid Centaur search, which beats its pure LLM and classical competitors on the autoresearch study. Its OOM-aware objective is genuinely relevant. It is not a universal reliability-search record, and the card supplies no matched delivered-utility ceiling. R≈1 must be anchored by an actually productive repair control under the same failure process, not the best successful run with failures removed.

Two demonstrations constrain autonomy. Ferreira et al. run Qwen3.5-backed search, including a CMA-ES hybrid, for 24 hours with three seeds on a roughly 50M optimizee; model and training share a GPU, with training VRAM capped at 80 GB. This is actual infeasibility-aware search, but twice the wall budget and much smaller training than a frontier-relevant campaign. The Claude autoresearch report records 126 trials, including one crash, in about 10.5 hours on one H100; version and independent replication are unspecified. It shows usable experimentation, not failure-probability calibration. TrainExplorer supplies corroborating training agency, without closing that gap.

KNOWN-RECIPE therefore has strong support; the complete reliability intervention is not AGENT-DEMONSTRATED within a comparable envelope. attack_basis=LITERATURE-ONLY. An agent must reconcile the ledger, identify shared causes and confirm delivered-quality improvements without treating correlated launches as independent.

ANCHORED ESTIMATED probabilities are 0.15 at 0.27, 0.65 at 0.51 and 0.20 at 0.72. Single=0.52, range 0.27–0.72; bo4=0.27+0.24(1−0.15⁴)+0.21(1−0.80⁴)=0.63; pass@4=1−0.80⁴=0.59; ub95=0.72. The successful branch is plausible because failure-penalized optimization is demonstrated, but its probability and reward transfer are assumptions. This is a tail-driven kill forecast, not evidence that agents routinely attain a high mean.

## 5. Verdict under the kill lines
Both section 4 and the ANCHORED assessment say CUT, UNCHANGED. The anchored binding line is bo4, exceeded by ESTIMATED 0.03; pass@4 also exceeds its line by 0.09. These are weaker grounds than the screen claimed and rest on transfer assumptions. The explicit failed-trial search result nevertheless makes a consequential lucky integration credible enough that the simple leaderboard-repair task needs redesign.

## 6. Redesign
Class (b): ordinary configuration search can optimize the current grader. REDESIGNABLE. Supply a complete immutable launch ledger from the outset and put grouped SMAC/Centaur selection in the floor. Change the intervention to an adaptive training-and-recovery policy facing observable precursor signals: memory pressure, gradient instability and data-dependent checkpoint cost interact with batch allocation. Score delivered private learning over actual launches with a disclosed calibration term. Dev must contain the same causal interactions, while held-out histories vary their composition; do not invent missing observability or random crashes to create difficulty.

The attack combining crash penalties, conservative settings and fixed restarts now faces a meaningful tradeoff: safe settings lose useful learning, while aggressive settings require timely recovery. A stronger legal precursor-aware policy must demonstrate reserve before shipping. Reliable frontier training is the scientific target. The strongest re-attack adds a failure classifier and contextual controller to SMAC; its basis remains LITERATURE-ONLY, with misspecified shared-cause models the principal residual risk.

For the redesign, ESTIMATED masses 0.30 at 0.20, 0.60 at 0.40 and 0.10 at 0.65 imply single 0.37; bo4=0.20+0.20(1−0.30⁴)+0.25(1−0.90⁴)=0.48; pass@4=0.34; ub95=0.65. Planned decisive cost is ESTIMATED 4 policy arms×3 independent failure-history seeds×6 hours×2 H100 for a 1B learner=144 GPU-h, plus 48 for recovery replay and protected-quality checks: 192 H100 GPU-h. This tests common failure interactions, not rare-event certification.

## 7. Measurement status
Rollouts UNMEASURED (planned complete-ledger and adaptive-recovery attacks). Grader noise UNMEASURED (planned failure-group resampling and paired training repeats). Score ladder UNMEASURED (planned success-only incumbent, grouped optimizer, contextual repair and attainable reliable control).

## Audit record
id: C098
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.82
old_bo4: 0.89
old_pass4: 0.99
old_ub95: 0.97
new_single: 0.75
new_single_range: 0.45-0.89
new_bo4: 0.85
new_pass4: 1.00
new_ub95: 0.89
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Start from complete grouped selection and reward precursor-aware recovery that improves delivered learning under observable interacting failures.
redesign_single: 0.37
redesign_bo4: 0.48
redesign_pass4: 0.34
redesign_ub95: 0.65
redesign_gpuh: 192
attack_basis: LITERATURE-ONLY
demonstrated_ref: autoresearch HPO, Qwen3.5+Centaur, 2026; autoresearch session, Claude version unspecified, 2026
gap_to_attack: grouped failure-cause calibration and causal repairs within twelve hours
subfield_sota_ref: Centaur autoresearch comparison with OOM penalties, Ferreira et al., 2026
anchored_single: 0.52
anchored_bo4: 0.63
anchored_pass4: 0.59
anchored_ub95: 0.72
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
