# C004 — Make audio event harvesting hear quiet precursors — saturation screen
## 1. What the grader actually rewards
The collector must spend a limited recording allowance on clips that improve a subsequently trained detector, not merely capture more quiet sound. False alarms and missed event intervals are counted over the complete stream, and overlapping clips consume recording minutes repeatedly. ESTIMATED R≈0 corresponds to the established harvesting floor and ESTIMATED R≈1 to an attainable best constrained collector; inherited loudness gating is tentatively ESTIMATED R=0.00, with a reference target of ESTIMATED R=0.60 pending calibration.
## 2. Strongest lawful combined attack
Use an always-running, bounded ring buffer of recent audio and a mixture of capture triggers: low-amplitude spectral change, acoustic novelty, model disagreement and uniform random exploration. Retain a pre-event window when an observable acoustic event occurs, charging every retained sample and overlapping window. This buffer route is lawful only if transient processing is permitted by the recording contract; without that permission, the collector must reserve its quota prospectively and the forecast falls. The card currently limits captured minutes, not transient buffering, so this is a serious interface question rather than an illegal future-label oracle.

Fit an embedding-based diversity selector and update capture priorities from labels available on past captures. [Active Learning for Sound Event Detection](https://arxiv.org/abs/2002.05033) verifies the relevance of active acquisition; [Hybrid Disagreement-Diversity Active Learning for Bioacoustic Sound Event Detection](https://arxiv.org/abs/2505.20956) verifies a concrete disagreement/diversity combination. Add lagged association estimates between captured weak sounds and subsequently observed failures, without reading future annotations at collection time. A final threshold calibration on legal dev streams controls the false-alarm penalty. Detector training remains fixed if the editable artifact is only the collector.

ESTIMATED single-run R=0.64, range 0.40–0.82; ESTIMATED oracle best-of-4=0.72; ESTIMATED pass@4 at R≥0.60=0.80; ESTIMATED upper-95% projection=0.89. These are scenario estimates, not statistical findings. Buffering and exploration should recover much of the missing precursor exposure, while diversity prevents spending the entire cap on stationary quiet background. The unresolved share is learning which quiet motifs matter when delays vary and failures are rare. That is a real acquisition problem, but the current budget semantics allow a strong conventional remedy before novel research is needed.
## 3. Other routes
- Spectral novelty with a uniform exploration reserve is the best single conventional collector: ESTIMATED R=0.46, range 0.24–0.68. It avoids pure loudness bias but cannot distinguish informative novelty from benign acoustic change.
- Sweep lookback length, onset thresholds, diversity radius and random-capture fraction on matched-duration dev streams. ESTIMATED R=0.58, range 0.35–0.78. Most candidate collectors can be replayed cheaply before detector retraining, so search should be included in the floor.
- Trigger on a loud downstream event and retain only its preceding buffer. ESTIMATED R=0.61, range 0.30–0.85 if retrospective retention is admitted; this can undercut the intended discovery challenge without accessing any protected labels.
## 4. What would lower lawful saturation
Define a prospective recording contract: samples not admitted when they arrive cannot later enter the training corpus, even if transient features are computed. Charge retained history and prohibit retrospective promotion of discarded waveforms. Include acoustically similar quiet distractors whose predictive value depends on earlier observable context, with matching dev evidence. Forecast the revised stack at ESTIMATED R=0.44, range 0.24–0.64. Authoring and auditing these streams costs ESTIMATED several weeks; an additional ESTIMATED 72 H100 GPU-h would compare prospective and retrospective controls. A blanket ban on all memory would be unjustified because causal feature state is part of a legitimate collector.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 8 GPU-h. New ESTIMATED 42 H100 GPU-h comprises an ESTIMATED 100M-parameter acoustic detector, ESTIMATED 4 collection arms, ESTIMATED 3 seeds, ESTIMATED 3 H100-hours per training run, and ESTIMATED 6 GPU-h for embedding passes and full-stream evaluation: ESTIMATED 4×3×3+6=42. Stream collection replay itself can be CPU work. This is much smaller than language-model pretraining, but the old envelope still omits diversity-feature computation, retention semantics and detector-seed replication. If an audio foundation model must be trained rather than supplied frozen, this budget must be replaced.
## 6. Duplicate check
v3 01B (`task_design_v3_codex/01_data_distribution.md`, acquisition section opened): WEAK; both acquire useful learning data, but this card controls streaming audio retention with future precursor value rather than experience selection across learner changes. The card's W06 reference is outside the supplied existing-task index and is not treated as a verified duplicate. No indexed task shares both this collector intervention and its full-stream event metric.
## 7. Verdict
CUT. ESTIMATED best-of-four is above the line by 0.12, and ESTIMATED pass@4 exceeds its boundary by 0.30. Retrospective buffering plus ordinary active acquisition is a credible combined route; clarifying prospective retention is necessary before reconsideration.
## 8. Measurement status
Rollouts UNMEASURED (planned: budget-accounted collectors with and without lookback). Grader noise UNMEASURED (planned: repeated detector seeds and independent stream blocks). Score ladder UNMEASURED (planned: loudness, random capture, novelty, combined acquisition and stronger feasible collector at identical retained minutes).
## Screen record
id: C004
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.64
attack_single_range: 0.40-0.82
bo4_est: 0.72
pass4_est: 0.80
ub95_est: 0.89
gpuh_old: 8
gpuh_new_est: 42
duplicate_of: v3-01B WEAK
kill_reason: buffered acquisition and diversity threaten the recording challenge
souping_flag: no
