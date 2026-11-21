# C110 — A benchmark generator that must survive its own learner's progress — saturation screen
## 1. What the grader actually rewards
The generator is useful only when training on its output improves a learner on independently authored causal programs. Difficulty labels, reference-solving volume and impressive generated examples have no direct value, while their costs reduce the available learning budget. ESTIMATED R≈0 is no improvement over a competent adaptive generator with prerequisite replay; ESTIMATED R≈1 is the attainable same-cost transfer control. An unchanged inherited generator is an essential native baseline, and the planned ESTIMATED reference near 0.60 is not yet calibrated.
## 2. Strongest lawful combined attack
Install a generator that tracks learning potential rather than raw task size or failure rate. [Prioritized Level Replay](https://arxiv.org/abs/2010.03934) already selects generated levels using their estimated future learning value, and [ACCEL](https://arxiv.org/abs/2203.01302) edits useful levels as the learner changes. Those methods explicitly accommodate a learner whose competence changes which tasks matter. Their existence weakens the premise that progress invalidating a static filter is itself an unusual research obstacle.

For this card, the attacker would represent each executable program by causal operators and prerequisite structure, retain a broad reservoir, and compare fresh performance with recent learning progress. Mutate programs near the current frontier, preserve simpler bridges and periodically retest previously mastered families. Use checked reference solutions for labels and a small disjoint transfer probe to distinguish true abstraction progress from memorizing a generator family. Tune generator edit frequencies, replay mixtures and prerequisite floors against final transfer after complete learner transitions. Reference solving and discarded candidates stay in the cost ledger.

ESTIMATED single-run R=0.63, range 0.40–0.82; ESTIMATED oracle best-of-4=0.73; ESTIMATED pass@4 at R≥0.60=0.82; ESTIMATED projected upper-95% score=0.89. The residual is a mismatch between local progress and long-term transfer: a temporarily mastered prerequisite may still be needed to teach a future abstraction. Generic regret and replay can miss that delayed value. Yet the card has not instantiated such a mismatch; the known stack already changes its sampling objective after learning, rather than endlessly increasing superficial complexity.
## 3. Other routes
Prioritized replay with a fixed procedural grammar is the strongest single standard baseline. ESTIMATED R=0.48, range 0.27–0.70. It responds to changing competence without editing the grammar and may be enough if the inherited pool already covers useful support.

Evolutionary generator search can optimize mutations, semantic operator balance and replay age over short complete training cycles. ESTIMATED R=0.58, range 0.34–0.79. This is not an oracle search on hidden programs: development learner transfer supplies its fitness. A broad static curriculum built by backward prerequisite enumeration is a lawful alternative, ESTIMATED R=0.50, range 0.26–0.75. If its coverage matches adaptive generation, the self-modification story adds cost without improving the scientific endpoint.
## 4. What would lower lawful saturation
Define private task families where acquiring a reusable abstraction reverses the teaching value of different causal decompositions, and show that local learning-progress rankings disagree with delayed transfer. Expose an affordable protected development transfer probe and preserve equal reference-solving budgets. ESTIMATED score reduction is 0.15–0.23, to approximately 0.40–0.48. ESTIMATED preparation is 12–20 person-days plus 280 H100-h to obtain real before/after learner checkpoints and audit the reversal. More program length or extra operators without changed instructional value is insufficient.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 20 GPU-h. New ESTIMATED pilot is 256 H100 GPU-h. Assume 1B causal-program learners: 4 generator arms × 3 seeds × 16 H100-h spanning an abstraction transition = 192; generator/reference-model inference = 24; independent transfer and retention evaluation = 24; paired longer continuation of selected controls = 16. ESTIMATED total 192+24+24+16=256. The old estimate could test a short curriculum segment, but an uninformative pre-transition result cannot decide the claimed change in generator usefulness. These costs assume inherited pretrained learners rather than training a capable language model from scratch.
## 6. Duplicate check
D04, MODERATE: its source already submits a certified world factory and curriculum and grades independent learning, but its repair-world semantics differ from a self-modified causal-program generator. D18, MODERATE: it constructs reachable support under a fixed schedule, whereas C110 changes generation in response to learning. T07, WEAK: adaptive learning allocation overlaps, but the submitted intervention is teacher access rather than generated task structure.
## 7. Verdict
CUT. ESTIMATED best-of-4 is 0.13 above its kill line and pass@4 is 0.32 above. The promised adaptation to learner progress is already part of mature replay and environment-editing recipes; a specific delayed-transfer reversal is needed for re-entry.
## 8. Measurement status
Rollouts UNMEASURED (planned: full generator-editing attempts replayed through complete learner transitions). Grader noise UNMEASURED (planned: fixed-generator retraining seeds and independently drawn causal programs). Score ladder UNMEASURED (planned: static coverage, replay-only, edited curriculum, delayed-transfer reference and same-budget stronger generator).
## Screen record
id: C110
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.63
attack_single_range: 0.40-0.82
bo4_est: 0.73
pass4_est: 0.82
ub95_est: 0.89
gpuh_old: 20
gpuh_new_est: 256
duplicate_of: D04 MODERATE; D18 MODERATE; T07 WEAK
kill_reason: mature learner conditioned generation already follows competence changes
souping_flag: no
