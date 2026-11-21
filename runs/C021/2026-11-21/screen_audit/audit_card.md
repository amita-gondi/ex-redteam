# C021 — Design experiments that expose architecture–data complementarity — screen audit
## 1. What the screen claimed
The screen proposed direct joint testing of the disclosed losing edits, factorial screening, conditional Bayesian optimization and budget-reserved continuations. Its ESTIMATED single/bo4/pass@4/ub95 were 0.65/0.75/0.84/0.92; verdict CUT, category EXP, because the problem statement points toward the joint experiment. The cited URLs were:

- https://arxiv.org/abs/2109.09831
- https://proceedings.mlr.press/v80/falkner18a.html
- https://arxiv.org/abs/2407.01492

## 2. Evidence audit
SMAC3 — Marius Lindauer, 2021, fetched — supports conditional configuration search, without demonstrating discovery of architecture/data transitions under this campaign's cost accounting. BOHB — Stefan Falkner, 2018, fetched — establishes a practical multi-fidelity optimizer, but cheap rankings are a prerequisite rather than a guaranteed property here. RegMix — Qian Liu, 2024, fetched — actually transfers data-mixture selection from small language models to larger training; that is relevant capability evidence for the data component, not for jointly changing representation and architecture.

Grade: PARTIAL. The strongest part of the attack is the unusually informative task description, which needs no claim about frontier scientific discovery. The extrapolated part is preserving that advantage through delayed joint learning and final-budget allocation. No opened source demonstrates that entire combination on comparable coupled interventions.

## 3. Research done now
- Improving Multi-fidelity Optimization with a Recurring Learning Rate for Hyperparameter Tuning — HyunJae Lee, 2022 — https://arxiv.org/abs/2209.12499 — fetched — Documents slow starters defeating early termination and supplies a repair. It lowers confidence in naive BOHB here while strengthening a learning-rate-aware adversary; its image experiments do not settle language-model architecture reversals.
- DataComp-LM: In search of the next generation of training sets for language models — Jeffrey Li, 2024 — https://arxiv.org/abs/2406.11794 — fetched — Controlled dataset experiments show that consequential data interventions can be evaluated at meaningful language-model scales. This raises feasibility of the attack's data probes, without showing the proposed architecture interaction is identifiable cheaply.
- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts — Hjalmar Wijk, 2024 — https://arxiv.org/abs/2411.15114 — fetched — Agents can implement and test ML optimizations quickly, yet the reported longer-budget comparison favors human research. That argues against treating correct factorial implementation as guaranteed successful scientific allocation.

Counts refer to distinct cited works; HTML and abstract versions share an entry.

## 4. Re-estimated attack
All reward forecasts and distribution assumptions below are ESTIMATED; reward anchors remain unmeasured. This is an attack on the provisional scale, not evidence that a known floor can receive positive reward after calibration. Directly testing the named pair plausibly recovers 0.36 of reward; surrogate-guided neighborhood exploration adds 0.17; preserving a final continuation and checking slow starters adds 0.10 in expectation. Their combined 0.63 leaves the unresolved transfer and training-budget opportunity cost.

Use an ESTIMATED two-regime distribution: probability 0.32 at R=0.43 when proxies misrank the pair, and probability 0.68 at R=0.73 when the joint test transfers. These are conditional outcome representatives, not measured modes. Search decisions and proxy fidelity dominate variation. ESTIMATED single=0.32×0.43+0.68×0.73=0.63, range 0.43–0.73. Independent attempts give ESTIMATED bo4=0.43×0.32^4+0.73×(1−0.32^4)=0.73. With p=0.68, ESTIMATED pass@4=1−(1−0.68)^4=0.99. The single-run CDF reaches 0.95 at 0.73, so ESTIMATED ub95=0.73.

Repeated-search success rises despite a lower mean because the disclosed joint test creates a reliable opportunity. Block-conditioned measurement must check independence; the percentile is not a fitted projection.

## 4A. Demonstrated capability and subfield SOTA
The closest subfield SOTA located is RegMix's transfer of mixture rankings to substantially larger language-model training, improving downstream results relative to human selection (Liu, 2024; fetched above). It anchors a competent data-selection control, without establishing an architecture/data-interaction ceiling. A native loss reference and R≈1 remain unanchored until matched joint-training controls exist.

RE-Bench (Wijk, 2024, fetched https://arxiv.org/html/2411.15114v2) tests o1-preview/AIDE and Claude 3.5 Sonnet/Modular: the best agents report fourfold average expert score at two aggregate hours, with humans ahead at longer budgets. The scaling task supplies six H100s; it does not require diagnosing complementarity. The autoresearch session (agent posting for Andrej Karpathy, 2026, fetched https://github.com/karpathy/autoresearch/discussions/43) reports Claude improving validation bits/byte from 0.997900 to 0.969686 across 126 trials in approximately 10.5 hours on an H100. Its model variant and independent transfer validation are absent. These attributed results are not audit measurements.

KNOWN-RECIPE: factorial and multi-fidelity search exist. AGENT-DEMONSTRATED: rapid empirical optimization exists, but matched-budget selection of delayed complementarity is unshown. Thus attack_basis=LITERATURE-ONLY for the complete route, whose reliability rests on assumption.

ANCHORED ESTIMATED outcomes R=0.34/0.51/0.64 have probabilities 0.30/0.64/0.06. Direct joint testing supplies the low outcome; ordinary neighborhood selection earns the middle; delayed proxy transfer gives the rare upper outcome. ESTIMATED single=0.30×0.34+0.64×0.51+0.06×0.64=0.47, range 0.34–0.64. ESTIMATED bo4=0.34×0.30^4+0.51×(0.94^4−0.30^4)+0.64×(1−0.94^4)=0.54; pass@4=1−0.94^4=0.22; ub95=0.64. Independent restarts are assumed. Unresolved loss anchors and delayed-transfer feasibility prevent clear passage.

## 5. Verdict under the kill lines
Section 4 yields CUT, with ESTIMATED bo4 over by 0.13. The headline ANCHORED verdict is CONDITIONAL: FLIPPED CUT→CONDITIONAL. Its closest ESTIMATED line is bo4, clearing by 0.06, but normalization and delayed-transfer feasibility remain unmeasured. A known search method and a short-loop agent result do not demonstrate reliable joint-mechanism discovery. Require matched loss anchors and a direct joint/factorial-search comparison against the diagnostic control.

## 6. Redesign
The ANCHORED verdict still requires an explicit feasibility condition. The re-attack below has LITERATURE-ONLY basis: no consulted agent result validates this cross-mechanism diagnostic under the target budget.
Kill cause (b): standard experimental design can exploit a named reversal. REDESIGNABLE. Replace the named pair with an inherited language-pretraining campaign containing competing, documented explanations for a representation bottleneck: tokenization fragmentation, context mixing and positional inductive bias. Supply the full code, data statistics and comparable dev families. Permit any architecture/data program, but score its final loss at equal complete compute, including diagnosis and failed probes. Require transfer to independently authored compositions where the same superficial pair improves one family and harms another for observable mechanistic reasons.

Include factorial search, SMAC3, RegMix-style proxies, recurring-learning-rate probes and reserved continuations in the measured floor. The research opportunity must be a diagnostic that predicts which representation intervention transfers, established by ablation against identical search without that diagnostic. This remains useful frontier pretraining R&D. It neither conceals valid observations nor makes exhaustive search impossible by fiat; matched resources must support the stronger control and useful ordinary baselines.

The strongest redesigned attack combines conditional surrogates with gradient/representation diagnostics and long probes. ESTIMATED outcomes are R=0.31 with probability 0.72 and R=0.55 with probability 0.28: base recipe captures 0.31 and occasionally correct mechanistic selection adds 0.24. Thus ESTIMATED single=0.38; bo4=0.31×0.72^4+0.55×(1−0.72^4)=0.49; pass@4=1−1^4=0.00; ub95=0.55. These bounded modes are a falsifiable feasibility hypothesis, with residual risk that a universal diagnostic lifts the successful mode above the pass threshold.

Decisive-check cost ESTIMATED 480 H100 GPU-h: a 1B learner, four complete-search/diagnostic arms, three seeds, one H100 for 32 hours per campaign gives 4×3×1×32=384; independent continuations and loss evaluation add 96. Before interpreting normalized scores, freeze measured loss anchors and demonstrate the stronger attainable control. If ordinary pairwise search matches it, abandon this redesign.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent full-budget planners on fresh interaction families). Grader noise UNMEASURED (planned: repeat identical programs with paired learner seeds). Score ladder UNMEASURED (planned: isolated edits, disclosed joint test, full interaction search, diagnostic ablation and stronger continuation control).

## Audit record
id: C021
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.65
old_bo4: 0.75
old_pass4: 0.84
old_ub95: 0.92
new_single: 0.63
new_single_range: 0.43-0.73
new_bo4: 0.73
new_pass4: 0.99
new_ub95: 0.73
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Require transferable representation diagnosis across observable architecture/data mechanisms beyond complete interaction search.
redesign_single: 0.38
redesign_bo4: 0.49
redesign_pass4: 0.00
redesign_ub95: 0.55
redesign_gpuh: 480
attack_basis: LITERATURE-ONLY
demonstrated_ref: RE-Bench, Claude 3.5 Sonnet/o1-preview, 2024; autoresearch, Claude variant undisclosed, 2026
gap_to_attack: delayed architecture/data interaction transfer within the full campaign budget
subfield_sota_ref: cross-scale mixture ranking, RegMix Liu, 2024
anchored_single: 0.47
anchored_bo4: 0.54
anchored_pass4: 0.22
anchored_ub95: 0.64
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
