# C099 — Recheck a curriculum proxy when the learner changes — saturation screen
## 1. What the grader actually rewards
Diagnostic examples earn value only through the next curriculum they select and the resulting private final capability after continued training. R≈0 is the competent current-learner curriculum floor, while R≈1 is an attainable diagnostic policy that selects substantially better learning opportunities across stages. The static inherited ranking is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; agreement with a refreshed difficulty label is not itself scientific utility.
## 2. Strongest lawful combined attack
Combine current-policy rescoring and staleness-aware sampling from [Prioritized Level Replay](https://arxiv.org/abs/2010.03934) with progress-driven generation from [ALP-GMM](https://arxiv.org/abs/1910.07224). Add forgetting indicators, gradient-change summaries and short paired continuation probes to distinguish high current error from high learnability. When several candidate contrasts disagree, spend legal diagnostic budget on examples that separate their predicted curriculum choices, then update the progress model. This attack actively generates new diagnostic contrasts where permitted, rather than merely rescoring the old bank.

The standard stack should eliminate stale rankings and recover broad changes in difficulty. Its harder residual is recognizing that the representation transition changes which contrast is informative: examples can have similar loss and short-run progress while differing in the prerequisite they unlock later. Fresh stage transitions and the supplied protected development transitions make that a learnable measurement-design question rather than a hidden rule change. ESTIMATED single-run R=0.42, range 0.22–0.58; ESTIMATED oracle best-of-4=0.52; ESTIMATED pass@4 at R≥0.60=0.16; ESTIMATED projected upper-95% bound=0.68. These are conditional desk forecasts assuming the promised proxy-rebuilding mechanism genuinely changes subsequent learning utility beyond periodic refresh and lookahead.
## 3. Other routes
- Periodic current-learner rescoring with prioritized replay is ESTIMATED R=0.31, range 0.12–0.51. It handles staleness but cannot create a missing contrast if the old examples alias different learning needs.
- Search refresh intervals, progress windows, uncertainty weights and diagnostic-generator parameters with short continuation confirmation: ESTIMATED R=0.39, range 0.18–0.57. It can find a good general policy, though short probes may miss prerequisite-dependent delayed gains.
- Directly allocate small training branches to each proposed curriculum and select by measured next-stage progress: ESTIMATED R=0.37, range 0.15–0.59. This is the important measurement-design bypass; its cost competes with final learning and it may choose the wrong horizon when gains reverse later.
## 4. What would lower lawful saturation
Use independently authored stage transitions with causal contrasts that separate delayed prerequisite value from immediate difficulty, and include full periodic refresh, generated contrasts and short-branch lookahead in the floor. Development must expose the same transition process and lawful diagnostic actions. ESTIMATED attack could fall to R=0.32–0.44, at ESTIMATED author effort of several weeks and ESTIMATED 192 H100 GPU-h of real stage-history calibration. Reject artificial transitions whose effect is only a hidden label flip. The attainable reference needs to exploit evidence available before allocating the continuation, with an ablation showing that rebuilt diagnostics actually change useful learning.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 12 GPU-h. New ESTIMATED total: 480 H100 GPU-h, assuming an ESTIMATED 3B learner and ESTIMATED 125M diagnostic proxies. ESTIMATED 4 diagnostic/curriculum strategies × 2 seeds × 2 H100s × 18 hours = 288 GPU-h; diagnostic construction and short continuation branches add ESTIMATED 96 GPU-h; protected final training/evaluation and representation-transition checks add ESTIMATED 96 GPU-h. The old figure omits the learner trajectory on both sides of a stage change and the extra branches needed to measure diagnostic usefulness. Scoring an existing difficulty table on CPU would not constitute the decisive experiment.
## 6. Duplicate check
v3 01A — MODERATE after opening its stage-aware corpus specification: it reweights a fixed source pool across learning stages, whereas C099 submits actively rebuilt diagnostic data that determines later curricula. D26 — MODERATE: its inspected selector uses versioned gradient sketches for future rollout allocation, but it does not rebuild diagnostic contrasts as the learner representation changes. The new diagnostic-data intervention remains distinguishable from both parents.
## 7. Verdict
PASS-SCREEN. ESTIMATED margins are 0.28 for the single-run point, 0.08 for best-of-4, 0.34 for pass@4 and 0.07 for the projected upper bound. This is a priority for a falsification pilot, with the promised causal proxy-change mechanism still awaiting implementation and measurement.
## 8. Measurement status
Rollouts UNMEASURED (planned: regenerated-diagnostic policies versus refresh/lookahead controls); grader noise UNMEASURED (planned: stage-history and continued-training replication); score ladder UNMEASURED (planned: static proxy, periodic scoring, generated contrasts, proposed diagnostic reference and attainable control).
## Screen record
id: C099
verdict: PASS-SCREEN
binding_line: none
attack_single_est: 0.42
attack_single_range: 0.22-0.58
bo4_est: 0.52
pass4_est: 0.16
ub95_est: 0.68
gpuh_old: 12
gpuh_new_est: 480
duplicate_of: v3 01A MODERATE; D26 MODERATE
kill_reason: none
souping_flag: no
