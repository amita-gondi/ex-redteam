# C089 — Escape proxy-reward traps before training locks them in — saturation screen
## 1. What the grader actually rewards
The curriculum is valuable only if its trained policy completes private text-state tasks according to trusted intended-outcome rules rather than maximizing the proxy. R≈0 is the complete generic exploration and demonstration floor, and R≈1 is an attainable transferable policy that avoids traps while retaining ordinary completion. The unmodified proxy learner is provisionally ESTIMATED R=0.00, the target reference ESTIMATED R=0.60; reducing proxy exploitation without doing useful work must not score well.
## 2. Strongest lawful combined attack
The verified [AI Safety Gridworlds study](https://arxiv.org/abs/2606.15385) supports failures of entropy, prompting and finer credit on its environments. It does not establish failure of planner-generated safe demonstrations plus curriculum. Reproduce those mitigations through the official code identified in the paper, then construct legal escape trajectories from training transition rules, start with reachable safe precursors, and aggregate corrections on states the learner actually visits. [DAgger's implementation documentation](https://imitation.readthedocs.io/en/latest/algorithms/dagger.html) gives a concrete framework for the latter component. Combine safe replay, ordinary-task replay, staged exposure to proxy temptation and development selection by true authorized training outcomes.

The researcher should distinguish an exploration failure from an objective that positively prefers the trap. Demonstrating a safe route is insufficient if later proxy-only optimization promptly erases it; therefore the combined baseline must retain authorized safe supervision throughout its permitted curriculum. ESTIMATED single-run R=0.61, range 0.39–0.80; ESTIMATED best-of-4=0.72; ESTIMATED pass@4 at R≥0.60=0.80; ESTIMATED projected upper-95% bound=0.89. Remaining reward lies in transferring escape precursors across causal mechanisms and resisting interference from newly competent local behavior. This is substantive uncertainty, but the small discrete state language makes systematic training trajectories considerably stronger than entropy-only controls.
## 3. Other routes
- Counterexample replay with ordinary completion examples is ESTIMATED R=0.51, range 0.29–0.72. It directly teaches the intended distinction, although fixed examples may miss states induced by the adapting learner.
- Search curriculum ordering, safe/proxy replay ratio, entropy schedule and precursor difficulty: ESTIMATED R=0.57, range 0.35–0.77. Fresh executable development audits make it possible to reject schedules that only conceal failure temporarily.
- Entropy and credit refinement alone are ESTIMATED R=0.22, range 0.05–0.43. The source study justifies treating this isolated recipe as weak, but not using it as the complete lawful floor.
## 4. What would lower lawful saturation
Specify exactly which intended-goal labels and executable training branches are authorized. Include a floor that combines training-only planning, visited-state correction and persistent safe replay, then author fresh causal traps where precursors interfere with useful behavior rather than merely requiring an unseen action. ESTIMATED combined reward could drop to 0.40–0.56. ESTIMATED cost is two author-weeks and 192 H100 GPU-h for real lock-in and escape trajectories. Hiding the true rule would make safety unidentifiable; forbidding demonstrations after they solve the task would suppress a lawful baseline. Demonstrate a stronger same-budget curriculum before asserting remaining reserve.
## 5. Decisive-check GPU-h re-estimate
Old card value: ESTIMATED 16 GPU-h. New ESTIMATED total: 320 H100 GPU-h. Use an ESTIMATED 3B text-action policy: ESTIMATED 4 mitigation/curriculum arms × 3 seeds × 2 H100s × 10 hours = 240 GPU-h, plus ESTIMATED 48 GPU-h to generate and verify correction trajectories and ESTIMATED 32 GPU-h for protected ordinary/trap evaluation. These runs must extend past the apparent lock-in point; a short episode is not equivalent to learning lock-in. The original allowance may reproduce a toy trap but lacks the independent training and transfer comparisons needed to distinguish recipe failure from distribution mismatch.
## 6. Duplicate check
FIX T17 and catalog T17 — WEAK to MODERATE: both inspected sources repair an already contaminated policy offline and test retained capability, whereas this curriculum acts before lock-in. D07 — MODERATE after inspecting its online onset/control description: preventing exploit acquisition and scoring useful learning overlap strongly, but D07 submits an adaptive intervention controller while C089 submits escape training data/curriculum. The intervention difference prevents an automatic strong-duplicate cut.
## 7. Verdict
CUT on ESTIMATED best-of-4=0.72, exceeding the threshold by 0.12; ESTIMATED pass@4 also exceeds its line by 0.30. The paper's negative mitigation results should motivate the pilot, not stand in for testing a stronger lawful demonstration-and-curriculum stack.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete safe-demonstration curricula on fresh causal traps); grader noise UNMEASURED (planned: independent training and environment-seed grades); score ladder UNMEASURED (planned: proxy learner, entropy floor, correction replay, escape reference and attainable transfer control).
## Screen record
id: C089
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.61
attack_single_range: 0.39-0.80
bo4_est: 0.72
pass4_est: 0.80
ub95_est: 0.89
gpuh_old: 16
gpuh_new_est: 320
duplicate_of: FIX T17 WEAK; catalog T17 MODERATE; D07 MODERATE
kill_reason: safe planner trajectories and visited state correction exceed entropy only controls
souping_flag: no
