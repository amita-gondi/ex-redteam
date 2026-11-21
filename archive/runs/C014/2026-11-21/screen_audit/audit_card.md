# C014 — Replace confidence scores with executable falsifiers — screen audit
## 1. What the screen claimed
The screen combined property-based state sequences, independent arithmetic, gradient checks, metamorphic tests and paired learning trials to accept worthwhile training patches. It forecast ESTIMATED single/bo4/pass@4/ub95 = 0.77/0.84/0.96/0.96 and CUT, category EXP, on the premise that numerical testing plus continuations covers the target. Its URLs were:
- https://hypothesis.readthedocs.io/en/latest/stateful.html
- https://www.flux.utah.edu/paper/yang-pldi11/
## 2. Evidence audit
Hypothesis and Csmith establish test-generation feasibility. Neither measures the opportunity cost of rejecting beneficial training patches or connects counterexamples to downstream learning value.

Independent implementations can agree on an unhelpful objective. Short paired trials may help, but final-horizon ranking remains unsupported. Grade: ASSUMED for scientific selection, despite working software-testing components.
## 3. Research done now
- Stateful tests — Hypothesis project, 2026 documentation accessed — https://hypothesis.readthedocs.io/en/latest/stateful.html — fetched — Supports generating trainer/checkpoint operation sequences and shrinking failures; raises confidence in routine state-defect detection only.
- Finding and Understanding Bugs in C Compilers — Xuejun Yang et al., 2011 — https://www.flux.utah.edu/paper/yang-pldi11/ — fetched — Confirms cross-implementation testing can expose defects, but C compiler equivalence offers no evidence for which training loss is scientifically useful.
- Large Language Models are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models — Yinlin Deng et al., 2023 — https://arxiv.org/abs/2212.14834 — fetched — TitanFuzz reaches real deep-learning library bugs, directly strengthening the neural-code falsification component beyond the old compiler analogy. Library bug discovery still differs from gain-aware patch acceptance.
- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts — Hjalmar Wijk et al., 2024, revised 2025 — https://arxiv.org/abs/2411.15114 — fetched — Reports fast agent engineering progress alongside weaker returns at longer budgets; it argues against equating a familiar testing recipe with reliable multi-hour scientific judgment. It supplies no score conversion for this card.
- RExBench: Can coding agents autonomously implement AI research extensions? — Nicholas Edwards et al., 2025, revised 2026 — https://arxiv.org/abs/2506.22598 — fetched — Research-extension failures show that valid-looking code and paper knowledge leave substantive implementation gaps, lowering confidence in a nearly automatic patch selector. Different agents and tasks preclude using its reported success as this attack's probability.

Searches covered DL fuzzing, learning-curve selection and research-agent benchmarks. The new evidence strengthens numerical testing while cutting against the old near-complete scientific-selection claim.
## 4. Re-estimated attack
All allocations in this section are ESTIMATED hypotheses. Independent numerical/state checks plausibly capture 0.30 of score by excluding harmful implementations. Assumption-targeted generated tests add 0.14 for batch, precision and restart dependencies. Paired continuation selection contributes about 0.12 net of rejecting valid alternatives. The expected total is near 0.56; the uncertain remainder consists of valid but misleading learning objectives, long-horizon reversals and lost improvements.

Use R=0.37/0.58/0.76 with probabilities 0.25/0.55/0.20. The middle case represents good testing but imperfect scientific ranking; the high case occurs when the candidate family is dominated by detectable implementation mistakes or early-predictable gains. Low outcomes reflect common-mode objective errors. This is research-path variability plus seed-sensitive patch ranking, not an assertion about measured scorer randomness. ESTIMATED single=0.25×0.37+0.55×0.58+0.20×0.76=0.56, range 0.37–0.76. ESTIMATED bo4=0.37×0.25^4+0.58×(0.80^4−0.25^4)+0.76×(1−0.80^4)=0.69. ESTIMATED p=0.20, so pass@4=1−0.80^4=0.59. ESTIMATED ub95=0.76 because the two lower scenarios have cumulative probability 0.80.

The lower single estimate enters the old empty boundary band; repeated selector discovery still triggers CUT. Arithmetic assumes independent restarts conditional on patch family. S4 scaling remains unfitted.
## 4A. Demonstrated capability and subfield SOTA
The verified domain anchor is TitanFuzz (Deng, 2023, fetched), which discovers actual DL-library defects with model-generated programs. It supports the counterexample-generation frontier. No fetched work demonstrates a best-in-subfield selector that values accepting and rejecting training interventions by final learning gain, so the north star cannot honestly receive a literature-derived R≈1 value. Anchor the competent test floor to TitanFuzz-like executable coverage, then measure scientific selection separately.

- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched; its o1+SimpleJudge obtains reported F1=0.84 on JudgeEval, with judging runtime/accelerator budget unspecified. Checking predefined rubric requirements differs from synthesizing experiments that predict useful patch gains.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-used-to-assess-high-ai-self-improvement-capabilities — fetched; the Astra research-debugging agent achieves reported 81.85% average rubric credit. Detailed scaffold, elapsed budget and device allocation are not supplied. Root-cause diagnosis raises confidence in falsification, while the opportunity cost of rejecting valid rewrites remains untested.

KNOWN-RECIPE testing is extensive, including TitanFuzz's Codex/InCoder-based generation; AGENT-DEMONSTRATED scientific patch selection is not. attack_basis=LITERATURE-ONLY. Twelve-hour integration must connect numerical falsifiers to causal learning benefit, price continued experiments and preserve mathematically legitimate alternatives. None of these reported percentages is a completion probability for that chain.

ANCHORED ESTIMATED outcomes are 0.28/0.47/0.68 with probabilities 0.30/0.57/0.13: good code tests can still fail scientific ranking, ordinary empirical selection partly transfers, and a successful causal checker occasionally emerges. ESTIMATED single=0.30×0.28+0.57×0.47+0.13×0.68=0.44, range 0.28–0.68; bo4=0.28×0.30^4+0.47×(0.87^4−0.30^4)+0.68×(1−0.87^4)=0.56; pass@4=1−0.87^4=0.43; ub95=0.68. The headline verdict rests on assumption because no comparable-budget result measures the complete selector.
## 5. Verdict under the kill lines
Section 4 yields a recipe-conditioned CUT. The ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL, with ESTIMATED bo4 margin 0.04 and pass@4 margin 0.07. JudgeEval and research debugging show checking competence, but provide no direct bridge to long-run learning selection. Retention requires the concrete gain-aware contract and native outcome controls below.
## 6. Redesign
Potential cause (b) is standard patch search. The REDESIGNABLE condition below targets gain-aware falsification. Re-attack basis=LITERATURE-ONLY: the stress estimate assumes causal selection integration beyond demonstrated diagnosis.

Use independently implemented reweighting, optimizer-state and auxiliary-objective interventions with public assumptions and intended benefits. Give the checker statistics, gradients, source and small executable learning probes. Charge tests against downstream training. Score accepted interventions' final learning value and the independently established opportunity cost of missed valid gains.

Dev must show horizon reversals and predictive observables; hidden uses new causal combinations. An affordable legal control must demonstrate that targeted interventions predict the reversals. This tests whether correct-looking training improvements work for the intended reason.

The strongest redesigned attack is TitanFuzz-style generation plus differential/gradient tests, paired multi-fidelity training and patch-claim-conditioned causal probes. Standard tests remain in the floor. Its limitation is allocating experiments that distinguish objective misspecification from useful approximation while preserving valid rewrites; exhaustive final-horizon trials consume real useful training time. Residual risk is a generic multi-fidelity optimizer matching the bespoke checker, which would erase this proposed distinction.

For that re-attack, ESTIMATED outcomes 0.28/0.46/0.65 receive probabilities 0.45/0.48/0.07. ESTIMATED mean=0.45×0.28+0.48×0.46+0.07×0.65=0.39; bo4=0.28×0.45^4+0.46×(0.93^4−0.45^4)+0.65×(1−0.93^4)=0.50; pass@4=1−0.93^4=0.25; ub95=0.65. Low outcomes arise from wrong experiment selection; successful assumption probes form the small upper branch. This plausibly passes the desk thresholds if feasible reserve is measured.

ESTIMATED decisive cost uses a 1B trainer, 8 patch arms × 3 seeds × 6 hours × 1 H100=144 GPU-h; checker probes cost 36 and independent final evaluation 12, giving 192 H100 GPU-h. This only screens whether the useful scientific reversals exist; larger subjects are required if the mechanism disappears at this scale.
## 7. Measurement status
Rollouts UNMEASURED (planned isolated checkers with direct-trial and complete fuzzing baselines). Grader noise UNMEASURED (planned paired final-horizon training and valid-rewrite replays). Score ladder UNMEASURED (planned numerical checks, assumption tests, empirical selection and independent attainable scientific control).
Forecast fields, including the resource proposal, are ESTIMATED throughout this record.
## Audit record
id: C014
old_verdict: CUT
evidence_grade: ASSUMED
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.77
old_bo4: 0.84
old_pass4: 0.96
old_ub95: 0.96
new_single: 0.56
new_single_range: 0.37-0.76
new_bo4: 0.69
new_pass4: 0.59
new_ub95: 0.76
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Price claim-conditioned learning falsifiers against useful final training across valid interventions with predictable horizon reversals.
redesign_single: 0.39
redesign_bo4: 0.50
redesign_pass4: 0.25
redesign_ub95: 0.65
redesign_gpuh: 192
attack_basis: LITERATURE-ONLY
demonstrated_ref: JudgeEval, o1 SimpleJudge, 2025; Research Debugging, GPT-6.2 Astra, 2026
gap_to_attack: gain-aware acceptance of scientifically different training patches
subfield_sota_ref: executable DL-library fuzzing, TitanFuzz, 2023; scientific selection optimum unverified
anchored_single: 0.44
anchored_bo4: 0.56
anchored_pass4: 0.43
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
