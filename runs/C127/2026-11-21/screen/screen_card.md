# C127 — A curriculum flywheel that learns from cross-project interference — saturation screen
## 1. What the grader actually rewards
The self-trained researcher must produce useful model or system improvements on fresh old/new projects after learning through the submitted sequence. Replaying familiar tool actions is insufficient if the agent fails to transfer the underlying intervention, and all lifetime generation and training costs count. ESTIMATED R≈0 is a competent continual-learning corpus/replay floor; ESTIMATED R≈1 is an attainable stronger cross-project research policy at equal cost. An unchanged researcher and a jointly trained all-project control need native scores before the intended ESTIMATED reference near 0.60 is meaningful.
## 2. Strongest lawful combined attack
Build a mechanism-stratified episode store that preserves project conditions, intervention code, diagnostic predictions and actual outcomes. [Dark Experience Replay](https://arxiv.org/abs/2004.07211) verifies rehearsal combined with output-consistency regularization, while [Maximally Interfered Retrieval](https://arxiv.org/abs/1908.04742) verifies selecting replay likely to suffer from an upcoming update. Apply these as strong learning controls, not as evidence that scientific abstraction transfer has been solved. Keep the researcher as one evolving model and train on legal development episodes only.

The attacker would run cheap candidate updates, identify project pairs with negative transfer, and generate contrastive bridge episodes where similar telemetry calls for different actions under a changed condition. Replay both the original observations and the discriminating intervention, retaining old useful methods without teaching unconditional avoidance of new ones. [Gradient Episodic Memory](https://arxiv.org/abs/1706.08840) provides another established gradient-retention control to compare where its cost is affordable. Sweep sequence order, bridge frequency and replay balance against full development research campaigns, including a joint retraining arm when all prior legal data remains available.

ESTIMATED single-run R=0.45, range 0.26–0.68; ESTIMATED oracle best-of-4=0.56; ESTIMATED pass@4 at R≥0.60=0.34; ESTIMATED projected upper-95% score=0.73. The remaining gap is not ordinary action forgetting: old and new trajectories can both look successful while encoding incompatible causal heuristics, and a fresh project demands the correct conditional abstraction. Bridge generation must identify that distinction and teach it to a smaller research agent. The card's proposed interference relationships make this plausible, but no asset or executed learning history establishes how much of reward depends on it.
## 3. Other routes
Balanced replay with output-consistency regularization is the strongest single baseline. ESTIMATED R=0.32, range 0.16–0.54. It preserves familiar competence but may stabilize the very unconditional heuristic that later projects require the agent to revise.

Sequence and corpus search over replay capacity, project weights, contrast-pair construction and learning rate has ESTIMATED R=0.41, range 0.22–0.64. Its evaluation must include fresh campaigns, since training loss can improve while scientific decisions degrade. A lawful joint all-project retraining route has ESTIMATED R=0.59, range 0.34–0.81 if historical data is cheap and fully available. This branch could immediately CUT the workload economics; any low forecast must therefore survive that control rather than rely on a needless sequential training constraint.
## 4. What would lower lawful saturation
Require real intervention-response interference with valid conditional solutions, independently held-out research projects, and a disclosed lifetime exposure budget under which joint retraining is a serious but nontrivial control. Verify that bridge examples improve executed research beyond matched ordinary replay and examples of the same code without conditions. ESTIMATED attack reduction is 0.06–0.12, to approximately 0.33–0.39. ESTIMATED authoring effort is 18–30 person-days and 480 H100-h for cross-project training histories and downstream evidence. Arbitrarily contradictory labels on indistinguishable histories would make the task infeasible, not harder.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 22 GPU-h. New ESTIMATED requirement is 400 H100 GPU-h. For a 4B research agent, use 4 curriculum/replay arms × 2 seeds × 3 stages × 8 H100-h = 192; bridge-data generation and interference probes = 48; reset evaluation on 1B subject projects, 4 × 2 × 4 projects × 4 H100-h = 128; independent final outcome checks = 32. ESTIMATED total 192+48+128+32=400. This is modest continued adaptation, not training the researcher from scratch. The earlier budget could fit a short continual fine-tune but omits most downstream AI-R&D evaluation and generated support.
## 6. Duplicate check
FIX T08, MODERATE: its source changes the update rule over fixed versioned contract data, whereas C127 generates a curriculum for a research agent and grades its later discoveries. D21, MODERATE: it co-adapts scaffold and policy under replay-version changes, while C127's scientific treatment is the cross-project training distribution. 01B, WEAK: acquisition responds to learner change, but its learner is not a self-trained researcher evaluated on fresh AI-R&D campaigns.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 has only 0.04 margin and the projected bound only 0.02. Require demonstrated conditional causal interference, matched bridge/replay controls and the joint-retraining comparison; cheap joint exposure or mere action rehearsal would move the verdict to CUT.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent curriculum-flywheel construction and lifetime-cost campaigns). Grader noise UNMEASURED (planned: repeat researcher adaptation and reset downstream project executions). Score ladder UNMEASURED (planned: unchanged researcher, balanced replay, interference replay, bridge curriculum, joint retraining, reference and stronger transferable researcher).
## Screen record
id: C127
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.45
attack_single_range: 0.26-0.68
bo4_est: 0.56
pass4_est: 0.34
ub95_est: 0.73
gpuh_old: 22
gpuh_new_est: 400
duplicate_of: FIX T08 MODERATE; D21 MODERATE; 01B WEAK
kill_reason: none
souping_flag: no
