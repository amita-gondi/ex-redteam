# C008 — Grade latent visual decisions before training the policy — saturation screen
## 1. What the grader actually rewards
Reward-decomposition code matters only if training with it increases closed-loop scene completion; causal probes distinguish perception improvements from actuator improvements and ignored task requirements. ESTIMATED R≈0 is the competent auxiliary-supervision floor, while ESTIMATED R≈1 is a feasible stronger decomposition under matching information and training work. An unchanged distance reward is provisionally ESTIMATED R=0.00 and a successful reference ESTIMATED R=0.60; probe attribution must not award points independently of completion.
## 2. Strongest lawful combined attack
Train a simulator-state expert, expose its decisions only during authorized training, and turn action agreement plus object-role consistency into dense reward components for the pixel policy. [Learning by Cheating](https://proceedings.mlr.press/v100/chen20a.html) verifies a privileged-state teacher transferring to a sensorimotor student. [Distilling Policy Distillation](https://proceedings.mlr.press/v89/czarnecki19a.html) verifies concrete policy-transfer choices. Use paired identity interventions to gate the perceptual reward, paired actuator changes to calibrate control advantage, and on-policy correction examples to cover states produced by the learner.

The submission is still a reward harness. It can compare trusted train-time quantities and emit approved training signals, but cannot place simulator identities in the deployed observation or write completion receipts. A strong researcher would jointly tune the distillation-to-terminal-reward schedule, role-conditioned shaping and intervention sampling. An accurate perception head is insufficient, so the attack measures whether action logits change appropriately on identity swaps and lets that causal response control its shaping weight. This is materially stronger than independent auxiliary classification plus distance reward.

ESTIMATED single-run R=0.50, range 0.28–0.69; ESTIMATED oracle best-of-4=0.59; ESTIMATED pass@4 at R≥0.60=0.42; ESTIMATED upper-95% projection envelope=0.76. The envelope expresses design uncertainty rather than a fitted interval. The attack should recover familiar object targeting and smooth actuator adaptation, but transferring a state expert is not equivalent to selecting a reward that teaches new object-action causal relationships. Where identity and control errors induce the same action failure, sparse public intervention evidence may not identify which shaping gradient helps the finite student. Conversely, if the expert's supervision transfers directly, saturation could be substantially higher than this point estimate.
## 3. Other routes
- Privileged-teacher action distillation used as the sole dense training signal: ESTIMATED R=0.39, range 0.19–0.62. It supplies correct local targets but can fail on student-induced ambiguity and new role/control combinations.
- Sweep auxiliary-head weights, potential shaping, teacher annealing and identity/control probe allocation using the actual closed-loop dev endpoint. ESTIMATED R=0.46, range 0.24–0.67. This route must be charged for intervention collection and retraining, not just reward-function arithmetic.
- A terminal-only reward with standard exploration is a legitimate bypass: ESTIMATED R=0.26, range 0.08–0.51. A high result would show the proposed diagnostic decomposition is unnecessary.
## 4. What would lower lawful saturation
Require held-out compositions where the same perceptual error can require different control corrections, while independent train-time interventions reveal the distinction. Freeze a protected dev generator with those interactions and include a full privileged-teacher transfer control before choosing reward anchors. Demonstrate that a causally chosen decomposition teaches behavior beyond that control at equal examples. Forecast after this specific revision: ESTIMATED single R=0.40, best-of-four=0.49, pass@4=0.22 and upper envelope=0.66. Cost is ESTIMATED several researcher-weeks and ESTIMATED 120 extra H100 GPU-h for crossed teacher/decomposition experiments. Merely withholding valid simulator supervision would weaken the legal baseline instead of strengthening the task.
## 5. Decisive-check GPU-h re-estimate
Original allowance: ESTIMATED 12 GPU-h. Revised ESTIMATED 108 H100 GPU-h includes an ESTIMATED 100M-parameter vision-control student, ESTIMATED 4 reward arms, ESTIMATED 3 seeds and ESTIMATED 6 H100-hours per student run, plus ESTIMATED 12 GPU-h for privileged-teacher training and ESTIMATED 24 GPU-h for counterfactual closed-loop evaluation: ESTIMATED 4×3×6+12+24=108. Simulator rendering may impose substantial CPU wall time even with low GPU utilization. The old pilot can validate attribution probes, but cannot establish that the selected reward actually trains the policy better across seeds. No part of this proposed budget is spent here.
## 6. Duplicate check
Catalog T19 (`task_catalog_v3_full/packets/T19.md`, opened): WEAK, because its evaluator ranks compositional visual-temporal evidence rather than teaching a control policy through perception/control interventions. D14 (`hidden_task_cards_v4/cards/D14.md`, opened): MODERATE; both value diagnoses through later policy corrections, but C008 submits an executable reward decomposition grounded in simulator interventions rather than a trained diagnostic message channel.
## 7. Verdict
CONDITIONAL. The ESTIMATED upper envelope crosses its kill boundary by 0.01 and best-of-four has only ESTIMATED 0.01 clearance. Require the interaction-crossed generator and demonstrated privileged-teacher residual described above. Current forecasts cannot support PASS-SCREEN; direct transfer could eliminate the hypothesized diagnostic advantage.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent reward-harness searches including teacher transfer). Grader noise UNMEASURED (planned: repeated policy seeds and fixed-policy causal probe replays). Score ladder UNMEASURED (planned: distance shaping, perception auxiliaries, teacher reward, causal decomposition and stronger attainable control).
## Screen record
id: C008
verdict: CONDITIONAL
binding_line: ub95>=0.75
attack_single_est: 0.50
attack_single_range: 0.28-0.69
bo4_est: 0.59
pass4_est: 0.42
ub95_est: 0.76
gpuh_old: 12
gpuh_new_est: 108
duplicate_of: catalog-T19 WEAK; D14 MODERATE
kill_reason: require teacher-resistant causal perception-control compositions
souping_flag: no

## Screening-lead reconciliation (added after batch review, 2026-11-21 PT)
The author verdict above is CONDITIONAL, but this card's own ESTIMATED numbers cross a kill line (upper-95% 0.76 ≥ 0.75). The bar says over a line is CUT, so the final screen verdict is **CUT (bar-applied)**. The card may come back as a CONDITIONAL candidate only after the redesign described in section 7 and a fresh screen.
