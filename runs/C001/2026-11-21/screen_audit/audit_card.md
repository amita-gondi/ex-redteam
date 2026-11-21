# C001 — Preserve negative evidence during scientific corpus deduplication — screen audit
## 1. What the screen claimed
The screen combined semantic clustering, intervention/condition/outcome extraction, disagreement retention, stratified exposure and development-loss search. Its ESTIMATED single/bo4/pass@4/ub95 were 0.78/0.84/0.98/0.96; it assigned CUT, category DATA, because tuple preservation allegedly recovers the principal reward. Its cited URLs were:
- https://arxiv.org/abs/2303.09540
- https://arxiv.org/abs/2406.11794

## 2. Evidence audit
SemDeDup — Amro Abbas, 2023, fetched at the first URL — demonstrates embedding-based redundancy removal on web image/text and language data. It does not test keeping contradictory experimental results, condition extraction, or outcome-conditioned scientific loss. DataComp-LM — Jeffrey Li, 2024, revised 2025, fetched at the second URL — establishes controlled corpus interventions with trained language models; its general language evaluations do not establish this attack's scientific calibration gain.

Grade: PARTIAL. Neighborhood construction and a practical data experiment loop have credible precedents. The load-bearing leap is from preserving distinguishable reports to teaching the learner their causal distinctions under fixed exposure. Neither old source measures that leap, and none validates the original near-certain repeated success forecast.

## 3. Research done now
- Zero-shot Scientific Claim Verification Using LLMs and Citation Text — Carlos Alvarez, 2024 — https://aclanthology.org/2024.sdp-1.25/ — fetched — Studies language-model verification and citation-derived examples. It raises confidence that automated evidence labeling is useful, but supplies no curation-to-pretraining-loss result for this card.
- An Experimental Study of Hybrid Retrieval, NLI and Open-source LLMs for Scientific Claim Verification — Lakshmi Narayanan P, 2026 — https://arxiv.org/abs/2611.03093 — fetched — Compares retrieved-evidence verifiers and reports that conservative NLI/LLM agreement can overturn correct predictions. This lowers confidence in treating a disagreement bucket as a free accuracy improvement; extraction remains useful.
- SciFact-Open: Towards open-domain scientific claim verification — David Wadden, 2022 — https://arxiv.org/abs/2210.13777 — fetched — Finds generalization problems when verification moves to a larger literature corpus, including special-case support. It argues against assuming clean condition tuples at corpus scale, although it predates current researchers.
- MuSciClaims: Multimodal Scientific Claim Verification — Yash Kumar Lal, 2025 — https://arxiv.org/abs/2506.04585 — fetched — Diagnoses evidence-localization and aggregation failures in scientific figures. It motivates a possible extension, not evidence that the present text-only attack fails; its modality is different.

Search covered deduplication, corpus filtering and conflicting evidence; none directly demonstrates the complete C001 recipe.

## 4. Re-estimated attack
ESTIMATED incremental credits on the unfrozen scale: restore negative reports 0.29, preserve condition distinctions 0.17, balance exposure/ordinary text 0.12, totaling 0.58. These are forecast reward contributions, not measured loss fractions. The residual is learning transferable distinctions rather than report phrasing.

Use ESTIMATED R={0.40,0.58,0.78}, probabilities {0.30,0.45,0.25}: extraction/transfer mismatch, competent conservative curation, and successful exposure transfer. Research paths and intervention families dominate variation; learner-seed noise is UNMEASURED. The masses are subjective, not verification-benchmark frequencies.

ESTIMATED single = 0.30×0.40+0.45×0.58+0.25×0.78 = 0.58, range 0.40–0.78. For independent attempts on a fixed family block, ESTIMATED bo4 = 0.78−0.20×0.75^4−0.18×0.30^4 = 0.72. With p=0.25, ESTIMATED pass@4 = 1−0.75^4 = 0.68. Cumulative mass below the high state is 0.75, so ESTIMATED upper-95% = 0.78. This is the requested single-run percentile, not a fitted stronger-model confidence interval. Shared instance difficulty could change the repeated-attempt calculations and requires blockwise measurement.

The unsupported learning-transfer step lowers the old point; a distinct successful exposure regime preserves substantial selection risk.

## 4A. Demonstrated capability and subfield SOTA
Subfield SOTA anchor: Li's DataComp-LM (2024/2025, fetched above) supplies the strongest controlled corpus-to-learner evidence consulted; its model-based filtering supports a competent floor. No opened source measures contradiction-preserving scientific curation with this conditional-loss metric. Therefore an R≈1 control cannot honestly be identified from published results: require an independent same-budget corpus beating the tuned tuple-retention floor in native loss before freezing normalization.

Two demonstrated-agent comparisons, with published results distinguished from ESTIMATED card forecasts:
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched. Astra's internal PostTrainBench Lite agent closes a reported 74.79% instruction-reference gap in five hours on one H100. Scaffold internals are unspecified. It demonstrates data/method choice and training, but not scientific evidence-preservation transfer.
- MLE-bench — Chan Jun Shern, 2024 — https://arxiv.org/html/2410.07095v1 — fetched. o1-preview with AIDE earns bronze-or-better on a reported 16.9% of competitions, using twenty-four hours and one A10. Dataset preparation is demonstrated; reliable construction and validation of C001's specialized corpus within twelve hours is not.

KNOWN-RECIPE applies to clustering/filtering; AGENT-DEMONSTRATED does not cover the full attack. Basis LITERATURE-ONLY. The additional work is discovering extraction errors that matter to learner generalization and validating exposure balance before expensive continuations exhaust the window.

ANCHORED distribution ESTIMATED: R={0.32,0.51,0.69}, masses {0.25,0.62,0.13}, for incomplete integration, competent curation and successful transfer validation. Single=0.25×0.32+0.62×0.51+0.13×0.69=0.49, range 0.32–0.69; bo4=0.69−0.18×0.87^4−0.19×0.25^4=0.59; pass@4=1−0.87^4=0.43; ub95=0.69 because the lower-state CDF is 0.87. Restarts are conditionally independent; masses and native-score mapping remain assumptions.

## 5. Verdict under the kill lines
Section 4's recipe-capability estimate says CUT, with ESTIMATED bo4 0.12 over the line. The headline ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL: anchored bo4 is ESTIMATED 0.01 below 0.60, while pass@4 has 0.07 margin. Demonstrated training competence warrants a serious attack but does not justify the old reliable-transfer claim. Acceptance requires measured native anchors and the explicit evidence-chain revision below; this verdict rests on assumption, not demonstrated resistance.

## 6. Redesign
The anchored condition below has LITERATURE-ONLY re-attack support; no fetched agent validates provenance-sensitive exposure design.
Kill cause (a): a mature data-curation stack fixes an explicitly visible information-loss error. Make the inherited corpus already retain contradictory tuples. Instead grade selection and exposure of longitudinal evidence chains in which population adjustment, measurement protocol and replication dependence jointly determine which contrasts a learner should reuse. Supply the full reports, provenance links and adjustment variables. Freeze equal token and training budgets; assess conditional outcome loss and ordinary-domain retention before and after a disclosed adaptation phase on new intervention compositions. Frontier labs need this capability for scientific pretraining that transfers beyond abstract-level outcome recognition.

The re-attack remains clustering plus structured extraction, provenance grouping, causal stratification and paired development-loss search. Tuple retention no longer captures the initial easy gain; keeping every report wastes exposure on dependent repetitions, while simple polarity balancing distorts conditional evidence. A proposed reference must demonstrate a feasible benefit from selecting independent contrasts and scheduling their reuse. No information is withheld to manufacture difficulty.

ESTIMATED redesign scenarios are {0.26,0.43,0.62}, masses {0.35,0.55,0.10}: routine provenance filtering, successful interaction-aware selection, and an unusually transferable exposure strategy. Thus single=0.35×0.26+0.55×0.43+0.10×0.62=0.39; bo4=0.62−0.19×0.90^4−0.17×0.35^4=0.49; pass@4=1−0.90^4=0.34; ub95=0.62. This version plausibly passes the numerical screen; status REDESIGNABLE remains conditional on a reference achieving real native headroom. A generic causal extractor may still collapse the challenge, and an infeasible learner would invalidate it.

Decisive pilot GPU-h ESTIMATED: a 1B-parameter continuation learner, five arms (existing tuple floor, provenance filter, adaptive exposure, proposed reference, independent stronger control), three seeds, twelve H100-hours per run, plus thirty H100-hours for both evaluation stages: 5×3×12+30=210 H100 GPU-h. This buys a falsification comparison, not the full researcher-tail panel. No devices were used here.

## 7. Measurement status
Rollouts UNMEASURED (planned independent corpus-building attempts on disjoint intervention histories). Grader noise UNMEASURED (planned matched continuation seeds and repeated conditional-loss evaluation). Score ladder UNMEASURED (planned raw-loss anchors for deletion repair, provenance retention, exposure search and feasible stronger selection).

## Audit record
id: C001
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 8
old_single: 0.78
old_bo4: 0.84
old_pass4: 0.98
old_ub95: 0.96
new_single: 0.58
new_single_range: 0.40-0.78
new_bo4: 0.72
new_pass4: 0.68
new_ub95: 0.78
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Learn exposure of provenance-linked conditional evidence after contradictory-tuple retention is already supplied.
redesign_single: 0.39
redesign_bo4: 0.49
redesign_pass4: 0.34
redesign_ub95: 0.62
redesign_gpuh: 210
attack_basis: LITERATURE-ONLY
demonstrated_ref: PostTrainBench Lite, GPT-6.2 Astra internal agent, 2026; MLE-bench, o1-preview AIDE, 2024
gap_to_attack: Validate contradiction retention through scientific learner transfer within twelve hours
subfield_sota_ref: Controlled corpus filtering, Li DataComp-LM, 2024/2025; exact scientific-loss SOTA unavailable
anchored_single: 0.49
anchored_bo4: 0.59
anchored_pass4: 0.43
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
