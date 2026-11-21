# C103 — First build a privacy attack, then train a deletion method — saturation screen
## 1. What the grader actually rewards
Deletion succeeds only when the resulting model approaches an independently retrained counterfactual while keeping retained capabilities. The evaluator must also recognize recoverable influence in deliberately incomplete deletions, so making every attack fail is not sufficient. ESTIMATED R≈0 denotes weak-probe deletion with no improvement over a competent attack-calibrated floor; ESTIMATED R≈1 denotes attainable counterfactual agreement and retained utility under the same resource allowance. The card supplies neither distance weights nor measured anchors, leaving the intended ESTIMATED reference R≈0.60 provisional.
## 2. Strongest lawful combined attack
First build a calibrated suite rather than a single membership classifier. [LiRA](https://arxiv.org/abs/2112.03570) establishes likelihood-ratio membership inference using reference behavior, which can distinguish ordinary high loss from genuine membership evidence. Combine that with prompted extraction, paraphrases of confidential relationships and small clean continuation tests. Fit thresholds on independent retained and retrained controls, and record attack power against intentionally partial deletion before accepting a negative result.

Then optimize deletion against the suite while preserving retained examples through supervised replay and output-distribution constraints. [Towards Robust Knowledge Unlearning](https://arxiv.org/abs/2408.10682) verifies an adversarial attack/defense route that recovers latent knowledge and trains against that recovery. [Unlearning Resilient to Relearning Attacks](https://proceedings.mlr.press/v267/fan25e.html) supplies another relevant robust-optimization control. A capable researcher would alternate attack discovery with deletion updates and select by counterfactual development distance, never by attack success alone. These sources verify ingredients; none demonstrates this card's fresh relational target is solved.

ESTIMATED single-run R=0.46, range 0.28–0.65; ESTIMATED oracle best-of-4=0.56; ESTIMATED pass@4 at R≥0.60=0.38; ESTIMATED projected upper-95% score=0.72. The difficult remainder is indirect influence supported by retained relationships: deletion must match what retraining would infer, rather than erase every inference related to a confidential fact. A larger attack bank cannot identify that distinction automatically. However, if full lawful retraining fits the deployment budget, the attacker can submit that procedure and the score could approach ESTIMATED R=0.95; its cost must be resolved before accepting the lower forecast.
## 3. Other routes
A single adversarial unlearning recipe, calibrated on direct extraction and utility, is the strongest immediate baseline. ESTIMATED R=0.35, range 0.18–0.56. It should remove obvious recoverable associations but may damage facts that counterfactual retraining legitimately reconstructs.

An explicit sweep over forgetting strength, retained replay ratio, affected layers and early stopping is stronger than tuning a privacy threshold. ESTIMATED R=0.43, range 0.24–0.64, provided every candidate is charged and development relationships are separate. A lawful shortcut is to reset to an available clean ancestor and replay only retained updates; ESTIMATED R=0.75, range 0.45–0.96 if such an ancestor and sufficient replay budget are exposed. The current card does not specify their availability, so this remains a material conditional branch.
## 4. What would lower lawful saturation
Freeze a relational counterfactual benchmark containing both removable memorization and legitimately re-derivable facts, with independent attacks and clean relearning after deletion. Require equal utility tolerances across deletion and retraining controls, and establish through timing that complete retraining or clean-ancestor replay cannot fit the existing cap; change the workload economics openly if necessary. ESTIMATED robust-stack score after these requirements is 0.38–0.46, a reduction of 0.04–0.10 from an easier direct-fact implementation. ESTIMATED preparation is 10–18 person-days and 240 H100-h for paired counterfactual histories. Retaining a feasible stronger same-budget method is essential; simply increasing model size is not a hardness argument.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 20 GPU-h. New ESTIMATED budget is 176 H100 GPU-h: 4 deletion arms × 2 seeds × 6 H100-h on a 4B subject = 48; 2 independent counterfactual histories × 2 seeds × 20 H100-h for 1B controlled retraining = 80; attack/reference-model calibration on ESTIMATED 4 small models × 6 H100-h = 24; extraction, relearning and retained-utility evaluation = 24. ESTIMATED total 48+80+24+24=176. This economical pilot uses controlled histories; a general multi-billion-token pretraining counterfactual would cost substantially more. The old estimate covers a probe-separation check, not a useful complete deletion comparison.
## 6. Duplicate check
T17, MODERATE: the opened packet removes exploit behavior and tests its reconstruction under clean learning, whereas this task targets confidential influence relative to retraining. 07B, WEAK: its evaluator is trained against independent evidence truth, without the privacy counterfactual or deletion intervention. Neither shares both the intervention and grader target.
## 7. Verdict
CONDITIONAL. The ESTIMATED projected bound sits only 0.03 below its kill threshold and best-of-4 only 0.04 below its boundary. Require the relational counterfactual/relearning design and a measured cost audit of clean replay and retraining before promotion; if either shortcut fits, CUT the current workload.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent evaluator-plus-deletion development attempts). Grader noise UNMEASURED (planned: repeat counterfactual retraining and attack calibration across seeds). Score ladder UNMEASURED (planned: original model, weak deletion, robust deletion, clean replay, reference and independent retraining in native distance and retained capability).
## Screen record
id: C103
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.46
attack_single_range: 0.28-0.65
bo4_est: 0.56
pass4_est: 0.38
ub95_est: 0.72
gpuh_old: 20
gpuh_new_est: 176
duplicate_of: T17 MODERATE; 07B WEAK
kill_reason: none
souping_flag: no
