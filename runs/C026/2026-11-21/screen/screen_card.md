# C026 — A self-auditing scaffold that chooses when to distrust its tests — saturation screen
## 1. What the grader actually rewards
The submitted acceptance policy is useful only when a reset researcher deploys training patches that improve independently measured model quality; unnecessary rejection loses opportunities too. ESTIMATED R≈0 denotes no improvement over the competent acceptance floor, whereas ESTIMATED R≈1 requires the attainable same-budget selection utility, including missed improvements and validation costs. The unchanged harness plausibly sits near ESTIMATED R=0.00; the intended reference targets ESTIMATED R=0.60, but neither anchor exists as a measurement.
## 2. Strongest lawful combined attack
Build a contract-aware differential runner, use mutation and metamorphic checks to expose shared blind spots, then reserve actual miniature training comparisons for disagreements that could change deployment. [DeepXplore](https://arxiv.org/abs/1705.06640) verifies that differential testing is an established approach; it does not establish that majority agreement is scientific truth. Independently implement the loss/update calculation and cross changes in semantics with changes in code style, so an obsolete runner cannot veto a deliberately changed objective merely because it disagrees.

Use [Optuna sampling and pruning](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html?highlight=hyperband) to tune audit thresholds, runner diversity and escalation spend on allowed development campaigns. A frontier researcher can write this small controller directly and allocate its full budget to consequential uncertainties. This combination attacks both false acceptance and excessive caution; simply buying more copies of the same test is weaker.

ESTIMATED single-run R=0.72, range ESTIMATED 0.48–0.87; ESTIMATED oracle best-of-4=0.80; ESTIMATED pass@4 at R≥0.60=0.92; ESTIMATED projected upper-95% bound=0.94. These are subjective planning quantities, not sampled statistics. On the provisional scale, assume the stack recovers roughly ESTIMATED 0.72 of attainable selection gain: routine semantic faults are cheaply eliminated, leaving expensive objective changes and correlated numerical mistakes. The residual requires deciding whether disagreement signals progress or a bad measurement, which may need longer training than miniature checks can afford.
## 3. Other routes
An independent reference implementation with fixed disagreement escalation is the strongest simple recipe: ESTIMATED R=0.61, range ESTIMATED 0.39–0.77. Its weakness is paying equal attention to harmless differences and deployment-changing uncertainty.

Budgeted enumeration of acceptance thresholds and audit allocation rules, followed by a protected-dev selector, reaches ESTIMATED R=0.67, range ESTIMATED 0.42–0.83. Early pruning must retain slow valid patches; optimizing mutation coverage alone would select an attractive but irrelevant diagnostic. A lawful conservative fallback that accepts only independently verified gains could reach ESTIMATED R=0.44, range ESTIMATED 0.23–0.62, depending on the missed-opportunity charge.
## 4. What would lower lawful saturation
Introduce private objective revisions whose validity is observable through independent scientific experiments but not through a permanent reference implementation. Couple the audit budget across sequential proposals, and include useful patches whose short-run ranking reverses at the deployed horizon. This could reduce the composite to ESTIMATED R=0.48–0.60, at ESTIMATED authoring effort of three researcher-weeks and ESTIMATED 96 additional H100 GPU-h to validate reversals. This changes the mechanism rather than hiding the specification. It still needs a competent miniature-training selector in the floor; complexity alone cannot establish reserve.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 8 GPU-h. New ESTIMATED 64 H100 GPU-h: use an ESTIMATED 0.3B subject model, ESTIMATED four harness arms, ESTIMATED two campaign seeds per arm, and ESTIMATED six patch decisions per campaign, each requiring ESTIMATED one H100-hour for independent training/evaluation. Arithmetic: ESTIMATED 4×2×6×1=48 GPU-h, plus ESTIMATED 16 GPU-h for rejected-patch counterfactuals and runner replays. This narrow falsification pilot excludes frontier inference charges and full certification. The original allowance cannot pay for both accepted and missed patch outcomes across several controllers.
## 6. Duplicate check
07A: MODERATE, after reading its measurement-repair contract; both validate downstream learning, but C026 modifies commissioning policy rather than the reward ecosystem itself. D24: WEAK, after reading its source; paid diagnostics select fixed policies there, while this harness governs new training patches. Neither has the same intervention and grader target together.
## 7. Verdict
CUT. The binding best-of-four forecast exceeds its line by ESTIMATED 0.20; the single-run, pass probability and projected-bound forecasts also breach their gates. The proposed redesign is a new calibration candidate, not grounds to pass the present card.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent reset campaigns per harness). Grader noise UNMEASURED (planned: replay fixed selections with fresh training seeds). Score ladder UNMEASURED (planned: unchanged acceptance, differential runner, full audit stack and attainable selection control).
## Screen record
id: C026
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.72
attack_single_range: 0.48-0.87
bo4_est: 0.80
pass4_est: 0.92
ub95_est: 0.94
gpuh_old: 8
gpuh_new_est: 64
duplicate_of: 07A MODERATE; D24 WEAK
kill_reason: differential audit stack recovers patch selection
souping_flag: no
