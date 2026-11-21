# C108 — Teach an agent to create adversaries before choosing its data — saturation screen
## 1. What the grader actually rewards
Generated adversaries must obey environment invariants, and their data must improve a newly trained agent against independent adaptive opponents without destroying ordinary competence. Validity is an admission condition, not a separate source of reward. ESTIMATED R≈0 means no improvement over a competent diverse-adversary training corpus, while ESTIMATED R≈1 means attainable robust downstream utility at the same total generation and learning cost. The unchanged inherited agent should score at or below that floor; the proposed ESTIMATED reference around 0.60 requires actual native-success anchors.
## 2. Strongest lawful combined attack
Begin with executable opponent families and mutate their action policies, preconditions and timing, preserving validity through trusted checks. [PAIRED](https://arxiv.org/abs/2012.02096) verifies adversarial environment generation driven by relative solvability rather than impossible worst cases. [ACCEL](https://arxiv.org/abs/2203.01302) verifies evolutionary editing and regret-guided curriculum construction. These are not turnkey code-tool adversaries, but their combination gives a familiar design for finding learnable weaknesses and continually moving beyond mastered examples.

The attacker would cluster valid failures by intervention response, not wording, and test transfer by training a cheap learner on one cluster and evaluating disjoint opponent implementations. Keep examples that repair more than their own generating template, maintain ordinary positive replay, and refresh opponents against the current learner. [Replay-Guided Adversarial Environment Design](https://arxiv.org/abs/2110.02439) verifies another mature replay-based ingredient. Development selection can jointly choose mutation operators, curriculum mixture and robust-training strength. Generated invalid trials and failed transfer experiments remain charged.

ESTIMATED single-run R=0.72, range 0.50–0.88; ESTIMATED oracle best-of-4=0.81; ESTIMATED pass@4 at R≥0.60=0.94; ESTIMATED projected upper-95% score=0.93. The remaining gap is discovering an adversarial mechanism absent from every mutation grammar or model prior. Independent opponents can reveal that gap, but their independence alone does not make them hard. The card does not define a missing mechanism that this competent portfolio cannot produce, and diversity/repair-transfer selection directly addresses its stated shallow-adversary problem.
## 3. Other routes
Regret-guided adversarial generation with ordinary positive replay is the strongest single recipe. ESTIMATED R=0.56, range 0.34–0.76. It filters impossible or already solved examples but can concentrate on a narrow high-regret family.

An evolutionary search over valid attack programs, using robust learner improvement as a slow fitness signal and failure novelty as a cheap proxy, has ESTIMATED R=0.66, range 0.43–0.85. This is feasible when inherited attack programs make mutations inexpensive; completely new opponent training would consume much more of the horizon. A static public-style adversary portfolio followed by balanced robust training is another lawful baseline, ESTIMATED R=0.60, range 0.38–0.80. If it matches the adaptive generator, the prerequisite generation stage has no demonstrated scientific value.
## 4. What would lower lawful saturation
Define new opponent families whose useful training examples require composing individually harmless actions, and ensure the composition's value changes after the learner is updated. Hold out causal opponent implementations, provide related development interactions and preserve honest task support throughout. ESTIMATED score reduction is 0.13–0.21, to approximately 0.51–0.59, which may still violate oracle selection. ESTIMATED preparation is 14–24 person-days and 240 H100-h for independently executed opponent and learner histories. A larger list of exploit names or cosmetic code variants would not provide this change.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 18 GPU-h. New ESTIMATED value is 216 H100 GPU-h. Assume a 4B tool agent: 4 corpus-generation strategies × 2 learner seeds × 12 H100-h continuation = 96; generation and transfer-filtering with a 1B proxy, 4 arms × 8 H100-h = 32; independent adaptive-opponent evaluation, 4 × 2 × 8 H100-h = 64; repeated ordinary-competence and validity audits add 24. ESTIMATED total 96+32+64+24=216. The old pilot could compare static corpora but omitted much of the adaptive generation and opponent search being claimed.
## 6. Duplicate check
T17, MODERATE: its opened contract removes learned exploits through policy training, while this artifact creates and curates adversarial training data before downstream learning. D04, MODERATE: it generates certified training worlds and curricula, but not adaptive adversaries against a code-tool agent. D07, WEAK: it controls shortcut onset online rather than producing the training corpus. The different artifact prevents a STRONG duplicate finding here.
## 7. Verdict
CUT. ESTIMATED single-run reward crosses its limit by 0.02, and ESTIMATED best-of-4 crosses by 0.21. Validity checks and transfer-based corpus selection are useful engineering, but the complete known-method stack already supplies the intended competence-before-curation sequence.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent adversary-generation and corpus-selection attempts). Grader noise UNMEASURED (planned: repeat fixed-corpus learner training and adaptive-opponent searches). Score ladder UNMEASURED (planned: inherited agent, static attack library, regret generation, transfer-filtered generation, reference and stronger robust learner).
## Screen record
id: C108
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.72
attack_single_range: 0.50-0.88
bo4_est: 0.81
pass4_est: 0.94
ub95_est: 0.93
gpuh_old: 18
gpuh_new_est: 216
duplicate_of: T17 MODERATE; D04 MODERATE; D07 WEAK
kill_reason: validated adversarial curriculum and transfer filtering recover intended gains
souping_flag: no
