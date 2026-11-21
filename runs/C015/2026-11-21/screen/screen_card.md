# C015 — Learn a grader whose abstention triggers useful data collection — saturation screen
## 1. What the grader actually rewards
The error predictor is an acquisition component: it purchases transcript minutes, changes ASR training data, and is scored by the resulting private-speech word error rate. Confidence calibration receives no independent credit, and selecting many short clips does not evade duration accounting. ESTIMATED R≈0 is a competent duration-aware acquisition floor and ESTIMATED R≈1 an attainable stronger acquisition learner; unchanged static calibration is provisionally ESTIMATED R=0.00, with reference ESTIMATED R=0.60 and raw WER anchors still absent.
## 2. Strongest lawful combined attack
Estimate expected ASR error reduction from disagreement, acoustic diversity and approximate gradient features, normalize acquisition value by utterance duration, and refresh scores after each learner update. [Active Learning for Speech Recognition: the Power of Gradients](https://arxiv.org/abs/1612.03226) verifies an expected-gradient acquisition route for ASR. [BatchBALD](https://arxiv.org/abs/1906.08158) verifies joint batch selection that accounts for redundant information; its classification results are not ASR measurements.

Train the submitted error predictor on purchased transcripts and legal history, using disagreement and expected-improvement labels from charged short continuations where affordable. Include random exploration and embedding-cluster coverage to reach confidently wrong accents that a single acoustic model would omit. After each ASR refresh, rescore the remaining pool, recalibrate duration-conditioned error estimates and revise cluster quotas. The acquisition policy therefore adapts to its own induced data shift rather than merely correcting a static score. A full acoustic ensemble is only a train-time analysis/control if the deployment artifact is one predictor's weights; distill the combined acquisition ranking and charge that cost.

ESTIMATED single-run R=0.58, range 0.35–0.79; ESTIMATED oracle best-of-4=0.68; ESTIMATED pass@4 at R≥0.60=0.72; ESTIMATED upper-95% projection envelope=0.85. They are desk forecasts. The expected native gain is a substantial share of the WER reduction available from replacing static uncertainty selection with iterative, diverse, cost-sensitive acquisition. Shared confident blind spots and delayed changes in which speech patterns are learnable remain a gap. However, refreshing acquisition after updating the learner is an ordinary active-learning loop, so endogenous drift alone does not establish that the combined stack will miss the useful second batch.
## 3. Other routes
- Duration-aware disagreement sampling with refresh after every batch: ESTIMATED R=0.44, range 0.22–0.67. It handles changing error order but can repeatedly buy redundant hard accents.
- Search disagreement/diversity/exploration weights, batch sizes, refresh frequency and duration normalization using complete acquisition campaigns. ESTIMATED R=0.54, range 0.30–0.76. The winning campaign must be rerun from a clean ASR initialization to avoid carrying paid-label advantages across trials.
- Uniform accent/noise-cluster coverage followed by error-based refinement is a lawful low-complexity bypass: ESTIMATED R=0.40, range 0.18–0.66. Clusters must derive from observable audio, not protected accent labels or transcripts.
## 4. What would lower lawful saturation
Author acquisition campaigns where learning one observed speech mechanism changes the value of another in a way that current uncertainty and acoustic diversity fail to predict. Preserve a random exploration channel and show the interaction on protected dev campaigns. Grade the complete multi-refresh WER curve or final WER under a genuinely binding minute cap, with transcript reuse charged consistently. Forecast revised stack: ESTIMATED R=0.41, range 0.22–0.62. Cost is ESTIMATED a month of speech-family curation plus ESTIMATED 216 H100 GPU-h of interaction pilots. Merely changing held-out accents could introduce unsupported distribution shift without a discoverable acquisition advantage.
## 5. Decisive-check GPU-h re-estimate
Old card estimate: ESTIMATED 10 GPU-h. New ESTIMATED 162 H100 GPU-h uses an ESTIMATED 300M-parameter ASR learner and ESTIMATED 30M-parameter acquisition predictor. ESTIMATED 4 policy arms×3 seeds×3 refresh stages×3 H100-hours per ASR update costs ESTIMATED 108 GPU-h; predictor training/ensemble feature scoring adds ESTIMATED 30 GPU-h, and WER evaluation adds ESTIMATED 24 GPU-h: ESTIMATED total 162. These figures assume a provided acoustic checkpoint and finite audio pool. The former pilot can compare first-batch selection, but omits the repeated data-distribution changes that motivate the card.
## 6. Duplicate check
v3 01B (`task_design_v3_codex/01_data_distribution.md`, acquisition contract previously opened): MODERATE, sharing learner-dependent acquisition but selecting RL experience rather than purchased speech transcripts through a trained error predictor. D26 (`hidden_task_cards_v4/cards/D26.md`, opened): WEAK, as future gradient geometry is related but its intervention includes versioned RL sketches and rollout allocation. The different acquisition interface and WER endpoint prevent a STRONG duplicate conclusion.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds its line by 0.08, pass@4 by ESTIMATED 0.22, and the projection by ESTIMATED 0.10. The iterative active-learning composite already includes the main distribution-refresh behavior offered as the source of difficulty.
## 8. Measurement status
Rollouts UNMEASURED (planned: full minute-accounted acquisition campaigns from reset learner states). Grader noise UNMEASURED (planned: ASR seeds and speech-speaker clustered WER intervals). Score ladder UNMEASURED (planned: static uncertainty, duration-aware disagreement, diverse iterative acquisition, learned lookahead and attainable stronger acquisition).
## Screen record
id: C015
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.58
attack_single_range: 0.35-0.79
bo4_est: 0.68
pass4_est: 0.72
ub95_est: 0.85
gpuh_old: 10
gpuh_new_est: 162
duplicate_of: v3-01B MODERATE; D26 WEAK
kill_reason: iterative cost-aware diverse acquisition addresses induced drift
souping_flag: no
