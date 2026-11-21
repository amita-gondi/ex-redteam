# C105 — Train a verifier, then make the learner harder for it honestly — saturation screen
## 1. What the grader actually rewards
The final coding learner earns utility through programs that pass private exact tests, while independent correct implementations expose verifier false rejection. Verifier accuracy matters only insofar as its mistakes and training feedback affect that useful outcome under the stated audits. ESTIMATED R≈0 means a complete execution-backed training baseline is unimproved; ESTIMATED R≈1 means matching a stronger feasible learner while preserving honest-solution acceptance. Raw learner success and audit weights are unspecified, so the intended ESTIMATED reference R≈0.60 remains an anchor to establish.
## 2. Strongest lawful combined attack
Build a growing execution-labeled program bank with compiler outcomes, failing inputs, passing diverse implementations and reduced counterexamples. [CodeRL](https://arxiv.org/abs/2207.01780) verifies the mature combination of code policy training, unit-test feedback and a learned critic. [AlphaCodium](https://arxiv.org/abs/2401.08500) verifies a test-centered iterative generation route. The attacker can use such generation during data construction, with every execution and teacher call charged, then train the final learner and verifier on those checked records.

Refresh the verifier on the learner's current high-confidence errors, deliberately include unfamiliar correct algorithm families, and reserve exact execution for uncertain or novel programs. Retain earlier honest positives so refreshing does not become blanket rejection. Calibrate acceptance by algorithm and program length, use execution failures as hard negatives, and select update ratios by exact development learner success. A learner that generates more correct code reduces verifier pressure as well; there is no need to solve a separate abstract coadaptation problem when execution provides the label.

ESTIMATED single-run R=0.76, range 0.56–0.90; ESTIMATED oracle best-of-4=0.84; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED projected upper-95% score=0.95. Residual difficulty comes from incomplete generated tests, expensive semantic equivalence and novel correct solution modes absent from the bank. The card has not fixed a verification budget or semantic class that makes those limitations binding. A refreshed execution-labeled bank is therefore likely to recover most of the promised gain.
## 3. Other routes
CodeRL-style critic-assisted policy training is the strongest single established recipe. ESTIMATED R=0.62, range 0.42–0.80. It attacks the downstream endpoint directly and could outperform a more elaborate verifier whose labels are weak.

Sweep learner/verifier update frequency, hard-negative ratio, diverse-positive replay and execution routing, selecting exclusively on held-out exact success plus false-rejection audits. ESTIMATED R=0.71, range 0.50–0.88. This search learns a useful refresh policy without identifying the alleged mutual blind spot. If full execution of every training candidate is affordable, replacing most learned-verifier decisions with exact checks is a lawful route with ESTIMATED R=0.82, range 0.63–0.94. It should be measured before paying for a sophisticated verifier.
## 4. What would lower lawful saturation
Specify task semantics for which available development tests are genuinely incomplete and verification consumes a material fraction of the training budget. Independently construct correct algorithm variants that require new discriminating tests, then preserve those semantics in hidden projects. ESTIMATED attack reward could fall by 0.15–0.23 to around 0.53–0.61, still near or above the repeated-search gate. ESTIMATED authoring cost is 12–20 person-days and 180 H100-h for program-bank and learner pilots. An opaque hidden-only test shift is not a valid substitute for a predictive development slice, and forbidding execution would remove a lawful scientific control.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 18 GPU-h. A useful pilot needs ESTIMATED 192 H100 GPU-h. Assume a 4B coding learner and 1B verifier: 4 paired training arms × 2 seeds × 12 H100-h learner continuation = 96; verifier training and refresh, 4 × 2 × 4 H100-h = 32; fresh code generation and private exact-success evaluation = 40; independent correct-solution audits and repeated fixed-artifact grades = 24. ESTIMATED total 96+32+40+24=192. CPU test execution is separately bounded but does not become fictitious GPU time. The previous number could support a static verifier comparison, not repeated coadaptation with consequential learner training.
## 6. Duplicate check
07B, MODERATE: the source trains an evidence evaluator under independent optimization and honest-positive controls, whereas C105 also updates the coding learner and scores its final capability. D17, MODERATE: it grades downstream teaching utility, but its submitted aggregation changes over fixed evaluators rather than jointly training verifier weights and policy. These overlaps are substantial without sharing the complete intervention.
## 7. Verdict
CUT. ESTIMATED single-run score is 0.06 over its limit; ESTIMATED best-of-4 is 0.24 over. Execution-backed labeling and diversity replay are adequate candidate explanations for nearly all current headroom, and the card does not establish a verification bottleneck that survives their combination.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget learner/verifier training attempts). Grader noise UNMEASURED (planned: retrain frozen paired recipes and repeat exact program evaluation). Score ladder UNMEASURED (planned: unchanged learner, execution-only labels, static critic, refreshed critic, reference and stronger checked learner).
## Screen record
id: C105
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.76
attack_single_range: 0.56-0.90
bo4_est: 0.84
pass4_est: 0.96
ub95_est: 0.95
gpuh_old: 18
gpuh_new_est: 192
duplicate_of: 07B MODERATE; D17 MODERATE
kill_reason: refreshed execution labels likely close useful verifier learner gap
souping_flag: no
