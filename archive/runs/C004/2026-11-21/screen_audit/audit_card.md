# C004 — Make audio event harvesting hear quiet precursors — screen audit
## 1. What the screen claimed
The earlier attack used a ring buffer, novelty/disagreement/exploration triggers, embedding diversity, lagged associations and threshold calibration. Its ESTIMATED single/bo4/pass@4/ub95 were 0.64/0.72/0.80/0.89; CUT, category DATA, reflected retrospective precursor recovery plus conventional active acquisition. The cited pages were:
- https://arxiv.org/abs/2002.05033
- https://arxiv.org/abs/2505.20956

## 2. Evidence audit
Active Learning for Sound Event Detection — Shuyang Zhao, 2020, fetched at the first URL — supports change-point segmentation and mismatch/diversity acquisition, including benefits from recording context. It selects annotations from already available audio, rather than deciding which waveforms survive a recording cap. Hybrid Disagreement-Diversity Active Learning for Bioacoustic Sound Event Detection — Shiqi Zhang, 2025, fetched at the second URL — directly supports the committee/diversity combination on sparse sounds, but still addresses annotation efficiency rather than discovering future-failure precursors.

Grade: PARTIAL. Useful acoustic sample acquisition has genuine task-adjacent evidence, including rare events. The unsupported bridge is that event-triggered lookback captures the right delayed predictive evidence economically enough to improve a fresh detector under the specified full-stream penalties. A software buffer is straightforward to implement, but that fact is not SOTA evidence of downstream scientific value.

## 3. Research done now
- Online Active Learning For Sound Event Detection — Mark Lindsey, 2023 — https://arxiv.org/abs/2309.14460 — fetched — Tests online acquisition with changing class distributions and identifies weaknesses in existing approaches. It strengthens the case for an adaptive collector while warning that static uncertainty/diversity is insufficient under drift.
- Stream-based Active Learning for Anomalous Sound Detection in Machine Condition Monitoring — Tuan Vu Ho, 2024 — https://www.isca-archive.org/interspeech_2024/ho24_interspeech.html — fetched — Improves machine monitoring with low-budget stream selection. This is closer to the industrial use case, but updates a scoring backend rather than training the proposed precursor detector from newly retained clips.
- Explainable Unsupervised Sound Anomaly Detection via Sparse Feature Decomposition — Francesco Paissan, 2026 — https://www.merl.com/publications/docs/TR2026-166.pdf — fetched — Links anomaly scores to acoustic features on a machine-sound benchmark. It supports useful pretrained representations, yet describes rarity and nuisance sensitivity that lower confidence in novelty as predictive-value estimation.
- Patch-Based Contrastive Learning with Latent Space Clustering for Unsupervised Sound Anomaly Detection — Abhivanth Sivaprakash, 2025 — https://dcase.community/documents/challenge2025/technical_reports/DCASE2025_Vijayyan_37_t2.pdf — fetched — Reports localized spectrogram representations under machine-domain shift. It raises the plausibility of detecting weak local changes, without establishing that those changes predict future failures or that the collector can identify them before labels arrive.

Queries distinguished streaming sound acquisition from ordinary anomaly classification. None of the newly opened sources demonstrates the complete delayed-precursor harvesting objective, so their benchmark outcomes are not converted into C004 scores.

## 4. Re-estimated attack
ESTIMATED credits: lookback/exploration 0.24, motif diversity 0.20, and lag/context priorities with threshold calibration 0.12, totaling 0.56. A terminal event need not identify its faint cause, so buffering receives less credit than previously. Live triggers cannot use future annotations.

ESTIMATED scores {0.34,0.57,0.76}, masses {0.25,0.50,0.25}, represent benign-novelty waste, useful clips with incomplete context and effective lag-conditioned triggering. Research paths, rare-event composition and detector seeds vary. Grader variance is unknown; lawful bounded waveform buffering is assumed.

ESTIMATED single=0.25×0.34+0.50×0.57+0.25×0.76=0.56, range 0.34–0.76. With independent restart choices within an instance block, ESTIMATED bo4=0.76−0.19×0.75^4−0.23×0.25^4=0.70. Only the high state passes, giving p=0.25 and ESTIMATED pass@4=1−0.75^4=0.68. The cumulative probability at 0.57 is 0.75, so ESTIMATED ub95=0.76. This tail is a subjective single-run percentile, not a confidence limit on a measured projection.

Annotation efficiency weakly predicts precursor discovery, lowering the old point. Occasional lag-rule discovery creates a larger selection gain.

## 4A. Demonstrated capability and subfield SOTA
The most comparable strong acoustic acquisition result opened is Zhang's MFFT BioSED study (2025): reported warm-start mAP is 71% against 75% with full supervision using 2.3% annotation. That anchors a strong disagreement/diversity floor, not a precursor-harvesting ceiling: annotation fraction differs from recorded-minute cost. Ho's stream study corroborates practical acquisition gains. No source supplies the card's early-evidence capture optimum, so a reference requires equal-minute native full-stream utility before assigning R≈1.

- MLGym — Deepak Nathani, 2025 — https://arxiv.org/html/2502.14499v1 — fetched. Claude 3.5 Sonnet/SWE-Agent attains reported CIFAR-10 accuracy 0.895 from a 0.497 starter, with one GPU, approximately four hours and a fifty-action limit. It demonstrates classifier experimentation, not selecting rare predictive audio before its value is known.
- PaperBench Science — Elvis Zhang Research/Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched. GPT-6 Astra with the authors' launcher achieves reported 13.98% full and 59.08% partial reproduction under four-to-twenty-four-hour limits. Hardware and detailed scaffold are unreported there. Its validation failures matter to establishing causal precursor value, although the tasks are not audio acquisition.

KNOWN-RECIPE buffering and active labeling are supported; an AGENT-DEMONSTRATED complete collector is absent. Basis LITERATURE-ONLY. Integrating delayed labels, choosing benign controls and verifying future warning improvements remain beyond the demonstrated supervised loop.

ANCHORED ESTIMATED states {0.27,0.48,0.68}, probabilities {0.34,0.55,0.11}, correspond to uninformative capture, competent acoustic coverage and successful lag discovery. Single=0.34×0.27+0.55×0.48+0.11×0.68=0.43, range 0.27–0.68; bo4=0.68−0.20×0.89^4−0.21×0.34^4=0.55; pass@4=1−0.89^4=0.37; ub95=0.68, with 0.89 cumulative mass below it. Stream difficulty is conditioned on; scenario probabilities are assumptions, not observed audio-agent frequencies.

## 5. Verdict under the kill lines
Section 4's combined-recipe forecast is CUT, with ESTIMATED bo4 0.10 above 0.60. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; ESTIMATED bo4 has about 0.05 margin and ub95 0.07. Demonstrated classifier tuning cannot establish reliable precursor discovery under a different resource denominator. This assumption-dependent survival requires the context-controlled warning design and a feasible collector/reference comparison below.

## 6. Redesign
The anchored condition requires contextual warning, with LITERATURE-ONLY support for its acquisition/validation re-attack.
Cause (a): standard buffered acquisition and data diversity exploit the disclosed collector failure. Shift the useful outcome to early warning learned from context-dependent precursors, with evaluation before the terminal event. Supply operating context and longitudinal sound history; reuse the same quiet motifs in benign and failure trajectories so acoustic novelty alone is insufficient. Match observable contexts and precursor combinations between development and held-out machines. Keep downstream detector training fixed and meter its full-stream early-warning false-alarm/miss utility.

Allow ring buffers and retrospective selection; charge both transient and archived waveforms under an allowance derived from real stream rates. Failure lookbacks remain valuable but cannot alone distinguish acoustically similar harmless motifs. Predictive contextual transfer supplies the research target.

Re-attack with frozen embeddings, buffer triggers, matched case-control capture, contextual hazard estimation and diverse replay. It falls short only if interaction-aware benign controls improve warning beyond tuned failure-history collection. Simple contextual regression solving everything, or uninformative precursors defeating every learner, would reject this hypothesis.

ESTIMATED re-attack states {0.24,0.44,0.63}, masses {0.45,0.47,0.08}, express context-blind capture, hazard-aware acquisition and interaction discovery. Single=0.45×0.24+0.47×0.44+0.08×0.63=0.37; bo4=0.63−0.19×0.92^4−0.20×0.45^4=0.49; pass@4=1−0.92^4=0.28; ub95=0.63. REDESIGNABLE for acoustic reliability R&D, without claiming measured resistance.

GPU-h ESTIMATED for a decisive pilot: a 100M detector, five collectors, four seeds, four H100-hours per training run, plus twelve H100-hours for embedding extraction and continuous-stream warning evaluation: 5×4×4+12=92. Collection replay itself can run on CPUs; no replay or training was executed during this audit.

## 7. Measurement status
Rollouts UNMEASURED (planned complete collectors with auditable transient and archived audio costs). Grader noise UNMEASURED (planned detector-seed replication across independent soundscapes). Score ladder UNMEASURED (planned native warning utility for loudness, buffered diversity, contextual case-control and stronger acquisition policies).

## Audit record
id: C004
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 8
old_single: 0.64
old_bo4: 0.72
old_pass4: 0.80
old_ub95: 0.89
new_single: 0.56
new_single_range: 0.34-0.76
new_bo4: 0.70
new_pass4: 0.68
new_ub95: 0.76
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Reward context-dependent early-warning data acquisition with matched benign controls while retaining costed lawful buffering.
redesign_single: 0.37
redesign_bo4: 0.49
redesign_pass4: 0.28
redesign_ub95: 0.63
redesign_gpuh: 92
attack_basis: LITERATURE-ONLY
demonstrated_ref: MLGym, Claude 3.5 Sonnet SWE-Agent, 2025; PaperBench Science, GPT-6 Astra author launcher, 2026
gap_to_attack: Discover delayed predictive acquisition value rather than optimize a supplied labeled dataset
subfield_sota_ref: Sparse-event annotation efficiency, Zhang MFFT BioSED, 2025; waveform-budget optimum unknown
anchored_single: 0.43
anchored_bo4: 0.55
anchored_pass4: 0.37
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
