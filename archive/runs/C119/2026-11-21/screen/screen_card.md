# C119 — Train the agent to detect its own research dead ends — saturation screen
## 1. What the grader actually rewards
The continuation policy is trained, inserted into a reset researcher and judged by final private model improvement over a complete campaign. Spending less time on a branch is useful only when the saved resources produce better learning elsewhere; a plateau can be valuable if a later intervention unlocks progress. ESTIMATED R≈0 is a competent restart-and-continuation baseline, and ESTIMATED R≈1 is an attainable stronger campaign policy at the same horizon. The no-training policy and intended ESTIMATED reference near 0.60 need native improvement anchors, not historical stop/continue agreement.
## 2. Strongest lawful combined attack
Train a value model over experiment state, remaining budget, previous intervention responses and uncertainty, keeping abandoned branches explicitly censored. [Freeze-Thaw Bayesian Optimization](https://arxiv.org/abs/1406.3896) verifies the familiar strategy of pausing and resuming promising runs. [Learning-curve extrapolation](https://ijcai.org/proceedings/2015/487) verifies predictive early termination, but curve shape alone is insufficient when a new intervention changes the mechanism. The attacker would combine both with learned action-conditioned continuation values rather than simply copy old patience decisions.

[Conservative Q-Learning](https://arxiv.org/abs/2006.04779) supplies an established offline policy-learning control for avoiding unsupported optimistic values; its guarantees do not automatically transfer to these research histories. Use a charged exploration tranche to continue some apparently dead branches and randomize interventions, then fit uncertainty-aware values and train the controller on actual gains. At deployment, preserve resumable checkpoints, compare continuing with restarting, and occasionally buy an identifying probe when its expected value exceeds direct training. Tune policy conservatism and restart cost across development campaigns, including late-discovery cases.

ESTIMATED single-run R=0.48, range 0.29–0.69; ESTIMATED oracle best-of-4=0.58; ESTIMATED pass@4 at R≥0.60=0.44; ESTIMATED projected upper-95% score=0.74. The residual is the missing counterfactual: a history can support the same early curve under a dead mechanism and one needing an informative intervention. Paying to learn that distinction competes with all subsequent research. A complete value/search stack could still solve simple instances, so the tiny projected margin does not support a pass.
## 3. Other routes
Freeze-thaw allocation with probabilistic learning-curve models is the strongest single recipe. ESTIMATED R=0.36, range 0.18–0.58. It preserves promising slow starters but misses plateau-breaking interventions absent from the observed curve.

Search over patience, restart schedules, probe frequency, uncertainty bonuses and value-model features has ESTIMATED R=0.44, range 0.24–0.66. Its fitness must be completed campaign improvement, not stop-label accuracy. A broad fixed portfolio that never learns a continuation model is also lawful: ESTIMATED R=0.41, range 0.21–0.65. If independent branches are cheap, this diversification can replace sophisticated counterfactual reasoning and should be a serious baseline.
## 4. What would lower lawful saturation
Require executed, randomized continuation forks for training support, and hold out mechanisms where a specific affordable intervention separates an unidentifiable branch from a temporary plateau. Supply comparable protected dev histories and make restart/restore costs explicit. ESTIMATED combined score reduction is 0.06–0.12, to around 0.36–0.42, if those dependencies survive full search. ESTIMATED authoring is 15–25 person-days plus 480 H100-h for continued and abandoned branch counterfactuals. Do not label unrun continuations as failures or create delayed breakthroughs by arbitrary hidden timers.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 20 GPU-h. New ESTIMATED pilot is 304 H100 GPU-h. With a 4B researcher and 1B subject learners: 4 continuation policies × 2 seeds × 3 campaign mechanisms × 8 H100-h = 192; randomized continuation forks, 8 histories × 8 H100-h = 64; controller adaptation = 16; final evaluation and repeated fixed-policy campaigns = 32. ESTIMATED total 192+64+16+32=304. The earlier value could fit the policy cheaply but leaves most counterfactual labels and downstream campaign outcomes untested. This remains a mechanism pilot, not a powered tail study.
## 6. Duplicate check
T03, MODERATE: its source already submits a transferable strategy-switching research controller with freeze/rollback allocation, while this card trains a narrower continuation policy from campaign outcomes. 02B, MODERATE: its opened task trains delayed-action credit assignment; C119 specifically controls whether further research should be attempted. Shared campaign utility does not erase the different intervention, but the overlap makes generic controller success a credible bypass.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 is only 0.02 below its threshold and projected upper-95% only 0.01 below its threshold. Require real randomized continuation support and identifiable intervention-dependent plateau cases, with a full restart-portfolio control, before promoting the task.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent learned-continuation construction attempts on fresh campaigns). Grader noise UNMEASURED (planned: repeat fixed controller training, researcher execution and subject-learning seeds). Score ladder UNMEASURED (planned: patience, restart portfolio, freeze-thaw, value policy, reference and stronger same-budget continuation control).
## Screen record
id: C119
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.48
attack_single_range: 0.29-0.69
bo4_est: 0.58
pass4_est: 0.44
ub95_est: 0.74
gpuh_old: 20
gpuh_new_est: 304
duplicate_of: T03 MODERATE; 02B MODERATE
kill_reason: none
souping_flag: no
