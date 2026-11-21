# C050 — Search by commissioning discriminating micro-experiments — saturation screen
## 1. What the grader actually rewards
The plan must select a recipe whose independent continuation learns well after charging archive search and executed micro-experiments. Resolving a causal ambiguity earns nothing unless it changes a consequential recipe decision or avoids wasted training. ESTIMATED R≈0 is a competent cost-aware experiment-selection floor and ESTIMATED R≈1 the attainable net learning result; retrieval-only selection is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Use retrieval to initialize a posterior over recipe responses, then choose experiments by expected improvement in the final decision rather than generic hypothesis information gain. [Frazier's Bayesian optimization tutorial](https://arxiv.org/abs/1807.02811) describes the knowledge-gradient acquisition function and its decision-theoretic basis. [Budget-aware planning over iterative learners](https://proceedings.mlr.press/v206/belakaria23a.html) explicitly combines partial learning responses, cost and nonmyopic allocation. These are directly relevant corrections to the card's concern that a cheap experiment may distinguish predictions without improving recipe selection.

Combine a small causal-model portfolio with response-surface Bayesian optimization, conservative multi-fidelity promotion and explicit stop-versus-measure comparison. Search archived runs only while their expected decision value exceeds that of a new controlled intervention. Retain a direct outcome-search branch so the controller need not identify the author's preferred explanation. Execute the final recipe independently, with all exploratory training charged and no accidental checkpoint reuse. A frontier researcher can synthesize this compact controller from established methods and tune it on the disclosed experiment API.

ESTIMATED single-run R=0.74, range ESTIMATED 0.47–0.90; ESTIMATED best-of-4=0.83; ESTIMATED pass@4 at R≥0.60=0.94; ESTIMATED projected upper-95% bound=0.96. The forecast credits buying measurements that change the best recipe, not merely reducing posterior entropy. Residual loss comes from misspecified intervention models and micro-run rankings that reverse at full continuation. Those can create a real research challenge, but the present card neither instantiates such a mechanism nor separates it from the existing autonomous-controller contract.
## 3. Other routes
Cost-aware knowledge-gradient selection is the strongest single recipe: ESTIMATED R=0.64, range ESTIMATED 0.36–0.84. It directly values improved decisions, although limited lookahead may miss an expensive enabling experiment.

A bounded search over micro-experiment families, promotion thresholds and retrieval stopping rules reaches ESTIMATED R=0.69, range ESTIMATED 0.41–0.87. Small candidate action spaces may even admit exhaustive decision-tree search within the target allowance. A direct multi-fidelity recipe tournament gives ESTIMATED R=0.60, range ESTIMATED 0.31–0.82; it can win without any causal explanation if cheap continuations predict the final ranking. That bypass is legitimate and must enter the floor.
## 4. What would lower lawful saturation
Specify a new scientific mechanism where informative interventions change which later measurements are feasible, and cheap learning curves alias despite matched archive evidence. Supply development-observable clues and an attainable controller that exploits the dependency. ESTIMATED attack R could decline to 0.45–0.58. ESTIMATED cost is five experimental-design weeks and ESTIMATED 288 H100 GPU-h of live intervention validation. This would still need a clear distinction from T03's existing intervention-aware controller, which already includes probe equivalence, delayed reversals and irreversible allocation.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 10 GPU-h. New ESTIMATED 120 H100 GPU-h assumes an ESTIMATED 0.3B training subject, ESTIMATED four plan arms and ESTIMATED three independent ambiguous-archive blocks. Each arm/block receives ESTIMATED four micro-runs at ESTIMATED one H100-hour plus an independent ESTIMATED four-hour final continuation: ESTIMATED 4×3×(4×1+4)=96 GPU-h. Add ESTIMATED 16 GPU-h for repeated final recipe verification and ESTIMATED 8 GPU-h for proxy/grader overhead. Existing archive generation is assumed sunk and verified; creating it is extra. The original estimate barely covers one contrast and cannot compare complete policies.
## 6. Duplicate check
Catalog T03: STRONG. Its read source submits a reusable controller choosing informative live experiments, uses an intervention-aware contextual optimizer, and grades newly executed ML projects after complete research costs. Retrieval as an optional evidence action does not change the intervention or grader target. D10: WEAK, after reading its overseer-evidence contract, which buys safety inspections rather than training experiments.
## 7. Verdict
CUT for duplicate T03. Independently, ESTIMATED best-of-four exceeds its gate by 0.23 and single-run by 0.04. Decision-value experimental design directly addresses the proposed plateau and makes saturation plausible without exploiting the grader.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete search/measurement plans on fresh ambiguous projects). Grader noise UNMEASURED (planned: repeated independent final continuations). Score ladder UNMEASURED (planned: retrieval-only, recipe tournament, knowledge-gradient controller and stronger intervention planner).
## Screen record
id: C050
verdict: CUT
binding_line: duplicate
attack_single_est: 0.74
attack_single_range: 0.47-0.90
bo4_est: 0.83
pass4_est: 0.94
ub95_est: 0.96
gpuh_old: 10
gpuh_new_est: 120
duplicate_of: T03 STRONG; D10 WEAK
kill_reason: informative live-experiment selection already covered by T03
souping_flag: no
