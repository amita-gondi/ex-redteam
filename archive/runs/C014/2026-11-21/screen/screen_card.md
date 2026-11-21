# C014 — Replace confidence scores with executable falsifiers — saturation screen
## 1. What the grader actually rewards
A checker earns value by accepting training patches that yield real learning gains and rejecting harmful ones without discarding independently valid improvements. Test counts, small counterexamples and mutation coverage have no direct reward. ESTIMATED R≈0 matches the competent patch-selection floor and ESTIMATED R≈1 reaches an attainable stronger selection policy; inherited self-confidence is provisionally ESTIMATED R=0.00, while the intended reference is ESTIMATED R=0.60 before loss and opportunity-cost anchors are measured.
## 2. Strongest lawful combined attack
Use [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html) to generate and shrink multi-step trainer/checkpoint sequences. Combine independent scalar implementations, finite-difference gradient checks, metamorphic invariants and differential numerical tests, following the cross-implementation principle exemplified by [Csmith](https://www.flux.utah.edu/paper/yang-pldi11/). Csmith itself tests C compilers, not learning improvements; its relevance is a verified testing method, not an imported performance guarantee.

Read each patch's mathematical claim and derive tests that vary the assumptions it relies on: batch partition, sequence length, dtype, accumulation order, resumed state and optimizer configuration. Run candidate code in disposable workers and compare typed results outside the worker. Then spend the saved budget on short paired learning continuations for patches that pass semantic checks, using native gain rather than correctness alone to rank them. Do not reject a valid alternative rewrite merely because it differs numerically from the starter when its declared tolerance and mathematical contract permit it. Tune acceptance using uncertainty in real training gain, with separate tests for rejecting useful changes.

ESTIMATED single-run R=0.77, range 0.53–0.91; ESTIMATED best-of-4 mean=0.84; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED upper-95% projection envelope=0.96. These are hand-derived scenarios. The stack catches broad numerical/state defects, and the paired continuations address the remaining “correct but useless” patches. Its residual is scientific common-mode error: independently written implementations may optimize the wrong objective, or short continuations may misrank long-term learning. The task does not yet specify a patch family where that residual systematically survives both assumption-targeted tests and real continuation selection.
## 3. Other routes
- An independent reference trainer plus metamorphic checks is the strongest single standard recipe: ESTIMATED R=0.61, range 0.36–0.81. It catches semantic deviations but may overreject legitimate approximate or mathematically different improvements.
- Search generator distributions, test budgets, numerical tolerances and continuation lengths, optimizing held-out selected-patch gain. ESTIMATED R=0.71, range 0.47–0.88. Mutation testing can guide this search, but mutation score cannot stand in for the outer utility.
- Skip elaborate falsification and allocate the checker budget to successive paired training trials of every candidate. ESTIMATED R=0.68, range 0.40–0.89 when candidate pools are small. Direct outcome measurement is a lawful bypass the task must price explicitly.
## 4. What would lower lawful saturation
Use genuine intervention families whose errors appear only through compositional learning assumptions, while preserving valid rewrites and a fixed affordable probe budget. Include patches with indistinguishable short learning curves but different predictable long-horizon behavior, and give the checker legal evidence for distinguishing them. Freeze the rejection opportunity-cost weight in native model value. Forecast redesigned composite: ESTIMATED R=0.47, range 0.25–0.70. Cost is ESTIMATED several weeks to build scientifically meaningful patch families plus ESTIMATED 360 H100 GPU-h to establish their paired long-run outcomes. Randomly injected bugs would primarily reward mature software testing.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 6 GPU-h. Revised ESTIMATED 192 H100 GPU-h uses an ESTIMATED 1B-parameter learner and ESTIMATED 8 candidate patches, ESTIMATED 3 seeds and ESTIMATED 6 H100-hours per trusted continuation: ESTIMATED 8×3×6=144. Share certified patch outcomes across checker arms. Reserve ESTIMATED 36 GPU-h for short probes and ESTIMATED 12 GPU-h for independent replay: ESTIMATED total 192. Most falsifier execution is CPU work, but its reward is learned improvement, requiring accelerator-backed patch outcomes. The former budget can compare test coverage, which is expressly not the grader's endpoint.
## 6. Duplicate check
Catalog T14 (`task_catalog_v3_full/packets/T14.md`, previously opened): WEAK, since supported reporting and terminal publication differ from executable patch falsification. D24 (`hidden_task_cards_v4/cards/D24.md`, opened): MODERATE; both submit a reusable diagnostic instrument evaluated by its selections, but D24 selects fixed policies through behavioral probes rather than training-code changes with subsequent learning. C014's outcome target and admissible counterexamples are materially different.
## 7. Verdict
CUT. ESTIMATED best-of-four is 0.24 above its kill line, and single-run is ESTIMATED 0.07 above. The mature falsification/continuation stack is too close to a full solution for the current general patch-selection specification.
## 8. Measurement status
Rollouts UNMEASURED (planned: isolated full-budget falsifier construction and direct-trial bypass). Grader noise UNMEASURED (planned: paired patch training seeds and fixed-artifact replay). Score ladder UNMEASURED (planned: assistant self-tests, independent reference, property-based battery, paired continuations and stronger selection control).
## Screen record
id: C014
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.77
attack_single_range: 0.53-0.91
bo4_est: 0.84
pass4_est: 0.96
ub95_est: 0.96
gpuh_old: 6
gpuh_new_est: 192
duplicate_of: catalog-T14 WEAK; D24 MODERATE
kill_reason: independent numerical tests plus paired learning trials cover the target
souping_flag: no
