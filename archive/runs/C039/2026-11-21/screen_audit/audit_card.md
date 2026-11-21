# C039 — Pretrain from revisable scientific records — screen audit
## 1. What the screen claimed
The old attack extracted assertion lineage and validity conditions, then used qualified exposure, revision deduplication and balanced replay. ESTIMATED single/bo4/pass@4/ub95=0.67/0.76/0.85/0.92 yielded CUT/DATA because temporal processing was expected to recover most revision utility. Its cited URLs were:
- https://arxiv.org/abs/2106.15110
- https://arxiv.org/abs/2204.14211

## 2. Evidence audit
Time-Aware Language Models supports timestamp-conditioned learning, while TemporalWiki supports training on revision differences. Neither demonstrates extracting which scientific intervention conditions preserve an old conclusion, nor shows that exposure-only policies teach those dependencies efficiently. Grade: PARTIAL: temporal retention/update machinery is established, but the screen moved from dated facts and aggregate perplexity to condition-sensitive scientific conclusions without comparable evidence. Synthetic contrastive rewrites are also not automatically legal in an exposure-policy artifact.

## 3. Research done now
- Time-Aware Language Models as Temporal Knowledge Bases — Bhuwan Dhingra et al., 2021, revised 2022 — https://arxiv.org/abs/2106.15110 — fetched — Timestamp modeling helps changing factual knowledge; this supports explicit-date cases, not recovering unexpressed experimental qualifiers.
- TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving Language Models — Joel Jang et al., 2022 — https://arxiv.org/abs/2204.14211 — fetched — Difference-based updates reduce redundant exposure while retaining knowledge in the evaluated encyclopedia setting. That raises the corpus-processing baseline but does not establish scientific validity judgments.
- TiC-LM: A Web-Scale Benchmark for Time-Continual LLM Pretraining — Jeffrey Li et al., 2025 — https://arxiv.org/abs/2504.02107 — fetched — Replay plus learning-rate schedules approaches retraining loss with less compute, and the best replay mix varies by domain. This strengthens the recipe while warning against a universal history ratio.
- ScienceMeter: Tracking Scientific Knowledge Updates in Language Models — Yike Wang et al., 2025, revised 2026 — https://arxiv.org/abs/2505.24302 — fetched — Its scientific preservation/acquisition/projection evaluation shows incomplete simultaneous updating across tested approaches. This directly lowers confidence in transferring generic temporal perplexity success to scientific revision learning.
- Understanding Data Temporality Impact on Large Language Models Pre-training — Romain Fabre et al., 2026 — https://proceedings.mlr.press/v306/fabre26a.html — fetched — Temporally ordered pretraining improves freshness/temporal precision at substantial model scale. It raises the ordering attack, but chronology remains different from conditional validity.
- Web Search Is Not Enough: LLMs Fail to Account for Paper Retraction Status — Huy Hoang Ha et al., 2026 — https://aclanthology.org/2026.findings-emnlp.2070/ — fetched — Retrieved retraction information improves status identification yet does not reliably prevent unqualified citation recommendations. This is negative evidence for automatic scientific-status integration, not a direct training-policy benchmark.

## 4. Re-estimated attack
ESTIMATED gain shares are 0.30 explicit lineage/date handling, 0.35 selecting informative revision spans and 0.35 learning scientific condition dependence. ESTIMATED recoveries 0.90/0.70/0.14 yield 0.30×0.90+0.35×0.70+0.35×0.14=0.56. The small final fraction reflects the source gap and limited artifact channel, not an assertion that scientific reasoning is intrinsically impossible. All exposure weights, schedules and held-out conclusion contrasts still require executable anchors.

Use ESTIMATED recipe scores 0.34/0.58/0.75 at probabilities 0.25/0.50/0.25. Corpus extraction quality, whether temporal cues suffice, and learner interference create these modes. ESTIMATED single=0.25×0.34+0.50×0.58+0.25×0.75=0.56, range 0.34–0.75; bo4=0.75−0.17×0.75^4−0.24×0.25^4=0.70; pass@4=1−0.75^4=0.68 from p=0.25; ub95=0.75. These tails still imply CUT for a fully integrated recipe, but lower the old figures because the missing scientific-conditioning capability now carries explicit cost and failure risk.

## 4A. Demonstrated capability and subfield SOTA
Fabre et al.'s fetched 2026 temporally ordered pretraining and TiC-LM's replay/meta-schedule results anchor the strongest ordinary reference. ScienceMeter supplies the closer scientific objective and shows that update, preservation and projection cannot be collapsed into aggregate language loss. No opened result reaches an exact scientific-condition exposure-policy ceiling; R≈1 therefore remains an unmeasured, required attainable control rather than invented perfect revision understanding.

- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — Astra's internal agent reportedly closes 74.79% of the reference gap in five-hour, single-H100 PostTrainBench Lite runs. This supports exposure/training experimentation, while paired historical scientific likelihood is absent.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — OpenAI research team, 2024 — https://arxiv.org/html/2410.07095v1 — fetched — o1-preview+AIDE obtains medals under a twenty-four-hour, one-A10 budget. Data-pipeline selection is real; its predictive competitions do not demonstrate revision-condition extraction or exposure-only learner control.

These source-reported agent outcomes establish neighboring automation, not successful execution of this attack. KNOWN-RECIPE covers chronology, differences and replay. AGENT-DEMONSTRATED coverage stops before teaching preserved conditional scientific claims under current corrections. attack_basis=LITERATURE-ONLY, with assumption-dependent verdict. The research agent must identify usable original spans, choose a token-neutral schedule and validate semantic likelihood differences within twelve hours; full multi-day pretraining cannot be silently treated as another cheap trial.

ANCHORED ESTIMATED scores 0.31/0.49/0.67 have probabilities 0.25/0.65/0.10. These encode a weak semantic pipeline, useful temporal training and occasional successful condition learning. ESTIMATED mean=0.25×0.31+0.65×0.49+0.10×0.67=0.46, range 0.31–0.67. ESTIMATED bo4=0.67−0.18×0.90^4−0.18×0.25^4=0.55; pass@4=1−0.90^4=0.34; ub95=0.67. The unrounded bo4 margin is slightly less than the requested comfortable margin, and native anchor uncertainty is additional.

## 5. Verdict under the kill lines
Section 4: CUT through ESTIMATED bo4=0.70 and ub95=0.75. ANCHORED: CONDITIONAL, FLIPPED CUT→CONDITIONAL. The binding estimated bo4 margin is 0.05 at displayed precision, so this is not a clear PASS-SCREEN. Scientific-update failures and the absence of a matched agent demonstration drove the flip; broad continual-pretraining success prevents claiming a protected research gap. Retention requires conclusion-sensitive scoring and verified native headroom after temporal ordering/replay.

## 6. Redesign
Cause (c): visible dates and version wording can shortcut the scientific distinction. REDESIGNABLE by pairing real revision histories where older results remain correct under original experimental conditions while later evidence narrows a generalization. Preserve timestamps and provenance; make condition information explicit in the legal corpus. Counterbalance dates, phrasing and source prestige so chronology cannot identify the preferred conclusion by itself. Score likelihood differences between scientifically opposed, minimally changed conclusions under their supplied conditions, retaining both historical and current weights.

The lawful combined attack remains timestamp qualification, revision-span selection, ordered replay and mixture search. It no longer captures most score merely by learning newest-version wording: the same date can support different answers as intervention conditions change. No synthetic labels or rewritten conclusions may be injected unless the artifact contract explicitly permits them. An attainable condition-aware exposure control must first show a learning advantage at equal tokens, and semantic questions need independent scientific validation.

Re-attack basis=LITERATURE-ONLY. ESTIMATED states 0.21/0.40/0.64 with probabilities 0.40/0.54/0.06 give single=0.40×0.21+0.54×0.40+0.06×0.64=0.34, range 0.21–0.64; bo4=0.64−0.24×0.94^4−0.19×0.40^4=0.45; pass@4=1−0.94^4=0.22; ub95=0.64. Strong semantic extraction could make the upper state more common, and residual language-pattern shortcuts remain a serious risk. This remains useful scientific-model pretraining R&D if the stronger control is learnable rather than merely an oracle.

Decisive-check GPU-h ESTIMATED: continue a 1.3B model on five exposure policies, three training seeds and eight H100-hours per run, one H100 each: 5×3×8×1=120.00. Paired likelihood evaluation adds ESTIMATED 18.00; proxy-to-full-horizon calibration adds 12.00; total 150.00 H100 GPU-h. This is a proposed falsification tranche, not a claim that any token throughput was measured.

## 7. Measurement status
Rollouts UNMEASURED (planned token-matched exposure policies on independent scientific histories). Grader noise UNMEASURED (planned learner-seed replication and stable conditional-likelihood evaluation). Score ladder UNMEASURED (planned chronological replay floor, qualified-span policy and demonstrated stronger semantic exposure).

## Audit record
id: C039
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 8
old_single: 0.67
old_bo4: 0.76
old_pass4: 0.85
old_ub95: 0.92
new_single: 0.56
new_single_range: 0.34-0.75
new_bo4: 0.70
new_pass4: 0.68
new_ub95: 0.75
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: c
redesign_status: REDESIGNABLE
redesign_oneline: Train from legally available condition-bearing revision spans and score counterbalanced scientific conclusion contrasts.
redesign_single: 0.34
redesign_bo4: 0.45
redesign_pass4: 0.22
redesign_ub95: 0.64
redesign_gpuh: 150
attack_basis: LITERATURE-ONLY
demonstrated_ref: PostTrainBench Lite, GPT-6.2 Astra plus internal agent scaffold, 2026; MLE-bench, o1-preview plus AIDE, 2024
gap_to_attack: exposure-only conditional scientific revision learning is untested
subfield_sota_ref: temporal pretraining ordering, Fabre et al., 2026; scientific-update frontier, ScienceMeter, Wang et al., 2025 revised 2026
anchored_single: 0.46
anchored_bo4: 0.55
anchored_pass4: 0.34
anchored_ub95: 0.67
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
