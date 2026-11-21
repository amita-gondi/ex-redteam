# C101 — Explore a training loss surface when every initial run fails — saturation screen
## 1. What the grader actually rewards
The precursor objective must train a code learner that completes private long synthesis programs under independent terminal tests and covers new composition mechanisms. R≈0 is the competent curriculum/demonstration floor; R≈1 is an attainable improvement in complete executable solutions, not merely higher partial-test reward. The inherited all-failure policy is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; an initially empty success buffer does not establish that no useful supervision can be generated lawfully.
## 2. Strongest lawful combined attack
Use legal training specifications to synthesize verified short programs and progressively compose them. Combine the abstraction-learning and neural-search ideas demonstrated by [DreamCoder](https://arxiv.org/abs/2006.08381), counterexample-driven refinement from the verified [CEGIS course reference](https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm), and verifier-filtered self-training following [STaR](https://arxiv.org/abs/2203.14465). Distill complete legal training solutions, add execution traces for intermediate states, and continue RL on the harder composition frontier with replay that preserves precursor skills.

The strongest attack does not wait for a lucky full solution from the stalled initial learner. It obtains training-only demonstrations from bounded symbolic search or backward construction, validates them, and amortizes them into the model. No hidden test programs or labels are available to that process. ESTIMATED single-run R=0.64, range 0.38–0.83; ESTIMATED oracle best-of-4=0.75; ESTIMATED pass@4 at R≥0.60=0.84; ESTIMATED projected upper-95% bound=0.92. The remaining gap is genuine transfer to new semantic compositions and avoidance of intermediate signals that teach unextendable prefixes. That could make a good research task, but it is already the core intervention of v3 02A, and the card does not rule out standard training-only synthesis as its saturation route.
## 3. Other routes
- Prerequisite curriculum with verifier-filtered complete demonstrations is ESTIMATED R=0.55, range 0.31–0.77. It replaces uniform entropy with concrete successful learning targets without needing a novel dense reward.
- Search auxiliary execution losses, curriculum depth, replay mixture and counterexample schedules under a fixed total generation/training allowance: ESTIMATED R=0.60, range 0.35–0.81. Confirmation must use full held-out synthesis, since partial-test progress is exactly the misleading proxy at issue.
- Terminal-only broad sampling with entropy tuning is ESTIMATED R=0.18, range 0.00–0.39. This intentionally weak isolated control diagnoses sparse signal, but cannot represent the full lawful attack when program construction and demonstrations are permitted.
## 4. What would lower lawful saturation
Specify a distinct precursor artifact or information constraint that changes the research intervention beyond v3 02A, and demonstrate a transfer mechanism that survives legal symbolic demonstration plus curriculum. Keep new language semantics observable through matching development tasks, and require evidence that a proposed precursor changes full-solution learnability rather than only prefix scores. ESTIMATED attack might fall to R=0.39–0.54 after a substantive redesign. ESTIMATED author effort is several weeks and ESTIMATED extra validation 256 H100 GPU-h. Raising synthesis length or withholding terminal successes is insufficient when backward-generated correct training programs remain cheap.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 18 GPU-h. New ESTIMATED total: 512 H100 GPU-h. Assume an ESTIMATED 7B learner with a separate small learned precursor head: ESTIMATED 4 objective/curriculum arms × 2 seeds × 4 H100s × 12 hours = 384 GPU-h. Demonstration generation, filtering and auxiliary model work add ESTIMATED 80 GPU-h; independent long-program execution and coverage evaluation add ESTIMATED 48 GPU-h. Symbolic search CPU time is separate and must be charged in the task's full cost ledger. The old allowance neglects the training needed to escape the empty-success regime and the competing demonstration baseline, which is likely more informative than another sampling-only run.
## 6. Duplicate check
v3 02A — STRONG after opening its objective/intermediate-supervision specification. Both inherit a learner beyond its successful frontier, submit learning signals and transfer schedules, and grade new unhinted executable compositions. Restricting the modality to long code synthesis does not change that intervention/target identity. D18 — MODERATE: its inspected support generator constructs missing reachable training states under a fixed learner objective, whereas C101 changes the signal itself. Excluded historical parameter-combination methods are not used in this comparison or attack.
## 7. Verdict
CUT for strong duplicate. ESTIMATED best-of-4 is also 0.15 above its threshold, and the ESTIMATED projected upper bound is 0.17 above its cutoff. A synthesis-specific instance could enrich v3 02A, but the current card adds no separate scientific treatment beyond precursor supervision and compositional transfer.
## 8. Measurement status
Rollouts UNMEASURED (planned: symbolic-demonstration, curriculum and precursor-objective searches); grader noise UNMEASURED (planned: training-seed and independent synthesis-family replication); score ladder UNMEASURED (planned: terminal-only learner, partial-test learner, demonstration curriculum and attainable precursor control).
## Screen record
id: C101
verdict: CUT
binding_line: duplicate
attack_single_est: 0.64
attack_single_range: 0.38-0.83
bo4_est: 0.75
pass4_est: 0.84
ub95_est: 0.92
gpuh_old: 18
gpuh_new_est: 512
duplicate_of: v3 02A STRONG; D18 MODERATE
kill_reason: precursor objective and new executable composition target duplicate 02A
souping_flag: no
