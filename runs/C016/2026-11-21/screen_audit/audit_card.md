# C016 — Design a measurement plan that survives correlated seed noise — screen audit
## 1. What the screen claimed
The screen's attack crossed initialization, ordering and augmentation randomness, fitted variance components, performed sequential comparisons and reserved independent winner confirmation. It reported ESTIMATED single/bo4/pass@4/ub95 = 0.81/0.88/0.98/0.98, CUT, category EXP, because factorial diagnosis and correct blocking directly address the pathology. Its cited URLs were:
- https://arxiv.org/abs/1709.06560
- https://arxiv.org/abs/2108.13264
- https://github.com/google-research/rliable
## 2. Evidence audit
The RL papers and rliable support uncertainty estimation, without automatically identifying shared RNG components or validating adaptive selection. Resampling dependent nominal rows remains wrong.

Identification, a fixed deployment estimand and forecast validation remain separate obligations. Grade: PARTIAL. New variance-decomposition evidence strengthens nuisance randomization without measuring reward under this query budget or the unspecified forecast-loss weighting.
## 3. Research done now
- Deep Reinforcement Learning that Matters — Peter Henderson et al., 2017, revised 2019 — https://arxiv.org/abs/1709.06560 — fetched — Establishes practical variability and implementation sensitivity; strengthens the need for an explicit independent-seed control rather than supplying a finished adaptive plan.
- Deep Reinforcement Learning at the Edge of the Statistical Precipice — Rishabh Agarwal et al., 2021, revised 2022 — https://arxiv.org/abs/2108.13264 — fetched — Supports uncertainty-aware reporting but does not license treating dependent launches as independent draws.
- rliable — Google Research, 2021 project, repository accessed 2026 — https://github.com/google-research/rliable — fetched — Provides a runnable statistical toolkit; the attacker still has to supply the correct block structure and experimental units.
- Accounting for Variance in Machine Learning Benchmarks — Xavier Bouthillier et al., 2021 — https://arxiv.org/abs/2103.03098 — fetched — Demonstrates how sampling, initialization and tuning change comparisons across neural workloads, strongly raising the case for randomizing multiple nuisance factors instead of only increasing nominal seeds.
- Empirical Design in Reinforcement Learning — Andrew Patterson et al., 2024 — https://www.jmlr.org/papers/volume25/23-0183/23-0183.pdf — fetched — Gives detailed experimental guidance, including separate randomness and paired comparisons, making ordinary dependence correction a mature baseline. Its warnings about bias also argue against treating confirmation as infallible.
- When Does Pairing Seeds Reduce Variance? Evidence from a Multi-Agent Economic Simulation — Udit Sharma, 2025, revised 2026 — https://arxiv.org/abs/2512.24145 — fetched — The current fetched title differs from the search index's older title. Its paired simulation results support variance reduction only when induced correlations are favorable; it is neither frontier training evidence nor proof that seed matching always helps.

Search focused on variance components and recent paired-seed work. The three additions clarify both the power and the conditional validity of pairing.
## 4. Re-estimated attack
All forecast numbers here are ESTIMATED. Correct units and true independent confirmation plausibly recover 0.39 reward, targeted nuisance crossing adds 0.21, and conservative shrinkage/sequential allocation adds about 0.11. These marginal allocations concern selected-recipe value plus forecast calibration; exact utility weights remain an implementation blocker, so the decomposition is conditional on a scientifically balanced weighting.

Use R=0.57 with probability 0.15 when an interaction is misidentified, R=0.71 with probability 0.65 when the standard crossed plan succeeds, and R=0.80 with probability 0.20 when economical allocation yields an additional good recipe choice. Most attempts reuse a mature plan, giving less dispersion than an insight-dependent task. Remaining spread arises from which coupling is detected and finite continuation outcomes; no numeric grader variance is claimed. ESTIMATED single=0.15×0.57+0.65×0.71+0.20×0.80=0.71; range 0.57–0.80. ESTIMATED bo4=0.57×0.15^4+0.71×(0.80^4−0.15^4)+0.80×(1−0.80^4)=0.76. ESTIMATED p=0.85 implies pass@4=1−0.15^4=1.00 rounded. ESTIMATED ub95=0.80 because cumulative mass at 0.71 is 0.80.

Mean and upper tail fall because rliable alone cannot identify dependence. Reusing a standard design makes the bo4 gap small. This independent-attempt desk distribution supplies no fitted population bound.
## 4A. Demonstrated capability and subfield SOTA
Bouthillier (2021) and Patterson (2024), both fetched, anchor valid comparisons averaged over the deployment randomization distribution. No universal adaptive-design leaderboard establishes an optimum. R≈1 requires a measured continuation-based efficient-design control, not presumed perfect variance inference.

- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts — Hjalmar Wijk et al., 2024, revised 2025 — https://arxiv.org/html/2411.15114v2 — fetched. Claude 3.5 Sonnet in METR's Modular scaffold approaches human performance on scaling-law selection under the paper's thirty-two-hour aggregate comparison; underlying attempts last up to eight hours, with task-specific access bounded by six H100s. The authors identify lucky prediction as a major contributor. This directly warns that a plausible utility forecast is not demonstrated experimental identification.
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search — Yutaro Yamada et al., 2025 — https://arxiv.org/html/2504.08066v1 — fetched. Claude 3.5 Sonnet coding with GPT-4o feedback/report agents produced a workshop-accepted paper among selected submissions, with a fifteen-hour cap and one-hour experiment-node cap; total accelerator allocation is unreported. It demonstrates conducting experiment branches, not calibrated recipe choice under shared RNG blocks.

KNOWN-RECIPE factorial diagnosis is stronger than the agents' demonstrated statistical identification. attack_basis=LITERATURE-ONLY. A twelve-hour attempt must discover the shared randomization, adapt the design without selection bias and confirm the winner; the closest studies do not validate that chain. The resulting verdict rests on assumed transfer rather than on a benchmark success percentage.

ANCHORED ESTIMATED distribution: R=0.27/0.49/0.68, probabilities 0.27/0.60/0.13, representing false identification, competent partial blocking and successful adaptive confirmation. ESTIMATED single=0.27×0.27+0.60×0.49+0.13×0.68=0.46, range 0.27–0.68; bo4=0.27×0.27^4+0.49×(0.87^4−0.27^4)+0.68×(1−0.87^4)=0.57; pass@4=1−0.87^4=0.43; ub95=0.68. The high branch remains possible because the method is standard, while its frequency no longer presumes autonomous statistical success.
## 5. Verdict under the kill lines
Section 4's evidence-only stress case gives CUT. The ANCHORED decision is CONDITIONAL, FLIPPED CUT→CONDITIONAL: ESTIMATED bo4 clears by 0.03 and pass@4 by 0.07. The scaling-law experiment's luck-sensitive outcomes and AI Scientist's lack of calibrated dependence tests weaken the automatic-solve premise. The condition is an identified deployment estimand plus an executable, paid intervention study as specified below.
## 6. Redesign
Potential cause (b) is standard experimental design. Retention requires this REDESIGNABLE paid-intervention contract. Re-attack basis=LITERATURE-ONLY, with forecasts stressing successful transport-adjusted design beyond demonstrated agent capability.

Supply coupled curriculum, augmentation and initialization campaigns with a published deployment estimand. Offer paid interventions: independent augmentation, paired ordering or upstream curriculum reruns. Effects may vary by recipe; distribution-changing interventions require estimable adjustments to deployment-average learning utility. Expose dependency APIs, receipts and dev interaction examples.

The floor combines factorial diagnostics, hierarchical inference, elimination and confirmation. The re-attack adds value-of-information search with transport adjustments. Resistance needs recipe/curriculum interactions that change useful interventions after observations, making exhaustive crossing expensive. A successful same-budget adaptive control must establish feasible trustworthy training comparisons without hidden independence rules.

ESTIMATED revised outcomes 0.33/0.51/0.68 have probabilities 0.35/0.53/0.12 for incorrect adjustment, useful partial diagnosis and effective adaptive design. ESTIMATED single=0.35×0.33+0.53×0.51+0.12×0.68=0.47; bo4=0.33×0.35^4+0.51×(0.88^4−0.35^4)+0.68×(1−0.88^4)=0.58; pass@4=1−0.88^4=0.40; ub95=0.68. This is CONDITIONAL with bo4 only 0.02 below its kill line. A generic optimal-design solver is the leading residual risk, and narrower budgets alone cannot rescue the concept.

ESTIMATED pilot: 1B subject, 4 recipes × 4 nuisance blocks × 2 initialization seeds × 6 hours × 1 H100=192 GPU-h; independent confirmation adds 24 and evaluation 8, totaling 224 H100 GPU-h. Ledger replays may screen plans on CPU after these outcomes exist, but cannot establish GPU learning utility without the underlying continuations.
## 7. Measurement status
Rollouts UNMEASURED (planned adaptive plans with separately held confirmation blocks). Grader noise UNMEASURED (planned crossed nuisance-component study rather than nominal-seed resampling). Score ladder UNMEASURED (planned incumbent, paired comparisons, complete factorial stack and independently feasible adaptive design).
All reward estimates and planned resource totals in this record are ESTIMATED.
## Audit record
id: C016
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.81
old_bo4: 0.88
old_pass4: 0.98
old_ub95: 0.98
new_single: 0.71
new_single_range: 0.57-0.80
new_bo4: 0.76
new_pass4: 1.00
new_ub95: 0.80
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Optimize paid scientific randomization interventions and transport-adjusted utility forecasts over observable curriculum interactions.
redesign_single: 0.47
redesign_bo4: 0.58
redesign_pass4: 0.40
redesign_ub95: 0.68
redesign_gpuh: 224
attack_basis: LITERATURE-ONLY
demonstrated_ref: RE-Bench scaling law, Claude 3.5 Sonnet Modular, 2024/2025; AI Scientist-v2, Claude 3.5 Sonnet plus GPT-4o, 2025
gap_to_attack: identifying shared RNG components and calibrating adaptive utility forecasts
subfield_sota_ref: nuisance-aware neural comparisons, Bouthillier, 2021; empirical RL design, Patterson, 2024
anchored_single: 0.46
anchored_bo4: 0.57
anchored_pass4: 0.43
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
