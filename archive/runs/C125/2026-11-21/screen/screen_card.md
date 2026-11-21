# C125 — An agent that learns to make its uncertainty actionable — saturation screen
## 1. What the grader actually rewards
Only the uncertainty-to-action rule changes: estimates and available measurements remain fixed. The chosen experiments must improve private final training utility, with numerical forecasts committed before results and scored properly. ESTIMATED R≈0 is a competent decision-value policy over those fixed beliefs, and ESTIMATED R≈1 is an attainable stronger same-budget allocation; the intended ESTIMATED reference near 0.60 lacks measured utility anchors. Because forecast quality is fixed across policies, its contribution must not provide unconditional positive reward that disguises a small action-improvement range.
## 2. Strongest lawful combined attack
For each candidate measurement, simulate permitted outcomes under the fixed uncertainty representation, update beliefs according to the published interface, and compute the expected improvement in the best terminal recipe after paying measurement cost. [The knowledge-gradient policy](https://optimallearning.princeton.edu/Papers/FrazierPowellDayanik_KnowledgeGradientSICON.pdf) verifies this established information-collection objective. [BoTorch's knowledge-gradient implementation](https://archive.botorch.org/tutorials/one_shot_kg) provides a practical route where the exposed posterior supports it. This respects the fixed-estimator restriction; it does not retrain or recalibrate an uncertainty ensemble.

Use decision sensitivity to ignore uncertainty directions that cannot change the winning action, then add short multi-step lookahead for complementary measurements. Compare stopping now, direct training and each probe on the same expected terminal utility scale. Search action-rule parameters on development campaigns and commit forecasts through a deterministic interface before requesting outcomes. If beliefs are only marginal confidence intervals, evaluate robust utility across admitted joint models rather than pretending independence. A strong researcher can implement the complete policy or enumerate a small measurement tree without training another model.

ESTIMATED single-run R=0.90, range 0.73–0.98; ESTIMATED oracle best-of-4=0.95; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% score=0.99. The residual is posterior misspecification and long complementary measurement sequences. But the card fixes uncertainty estimates and interventions, removing much of the research that could resolve those issues. Decision relevance is precisely what expected decision value computes; disagreement about irrelevant quantities is a weakness of entropy-only acquisition, not of the strongest lawful attack.
## 3. Other routes
One-step cost-aware knowledge gradient is the strongest single standard recipe. ESTIMATED R=0.78, range 0.56–0.93. It can change the favorite recipe when a cheap informative measurement justifies doing so, while stopping when uncertainty has no action consequence.

A sweep over lookahead depth, cost thresholds, posterior sampling count and robust utility penalties has ESTIMATED R=0.86, range 0.65–0.97. Finite measurement menus may permit exhaustive dynamic programming within the researcher budget. A lawful simple route tests only the closest competing recipes, allocating the rest to the current best: ESTIMATED R=0.72, range 0.47–0.91. It can be sufficient when the fixed uncertainty already identifies the relevant ambiguity and the starter merely ignores it.
## 4. What would lower lawful saturation
Reopen the intervention to acquiring or learning an action-relevant causal uncertainty model from real training probes, with intervention-dependent response changes that cannot be read from fixed estimates. This substantially changes the current fixed-belief task. ESTIMATED attack reduction could be 0.23–0.33, to about 0.57–0.67, which still needs repeated-search screening. ESTIMATED authoring is 15–25 person-days and 400 H100-h for matched response histories and identifiability checks. Adding a proper-score term or wider numerical intervals alone does not create that learning problem.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 12 GPU-h. New ESTIMATED end-to-end pilot is 96 H100 GPU-h: 3 action policies × 2 seeds × 3 ambiguous 1B projects × 4 H100-h for chosen experiments and final continuation = 72; independent native-utility evaluation and fixed-forecast checks = 16; fixed 4B agent integration = 8. ESTIMATED total 72+16+8=96. There is no policy-model training in this configuration because the submitted artifact is an action configuration. A CPU-only finite-tree calculation should precede this pilot and may already reject the premise. The old allowance omitted the real learning outcomes of selected measurements.
## 6. Duplicate check
T15, MODERATE: its source chooses costly decision-changing evidence with finite-horizon planning, but its artifact is a trained elicitation policy rather than fixed-belief scientific action rules. T14, MODERATE: it combines proper forecasts with cost-sensitive terminal choices, while C125 also schedules experiments. D24, MODERATE: paid testing and selection overlap, but its policies are fixed deployment candidates rather than newly trained research outcomes.
## 7. Verdict
CUT. ESTIMATED single-run reward exceeds its threshold by 0.20 and ESTIMATED best-of-4 by 0.35. Fixed beliefs and a disclosed measurement menu expose a standard value-of-information optimization problem; the author's entropy-based failure mode does not defeat decision-focused acquisition.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent action-rule construction and full ambiguous-project campaigns). Grader noise UNMEASURED (planned: fixed-policy training seeds and repeated forecast commitment checks). Score ladder UNMEASURED (planned: favorite-recipe policy, nearest-competitor tests, knowledge gradient, multi-step planning, reference and stronger allocation).
## Screen record
id: C125
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.90
attack_single_range: 0.73-0.98
bo4_est: 0.95
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 12
gpuh_new_est: 96
duplicate_of: T15 MODERATE; T14 MODERATE; D24 MODERATE
kill_reason: fixed belief decision value planning directly optimizes measurement actions
souping_flag: no
