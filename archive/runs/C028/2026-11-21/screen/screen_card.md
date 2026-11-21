# C028 — Adapt the scaffold's own compute governor — saturation screen
## 1. What the grader actually rewards
The governor earns utility through the best reproducible trained result achieved by the same research agent within a complete campaign budget. Forecasting, restarts and unsuccessful continuation all consume that budget; a noisy maximum cannot substitute for independent confirmation. ESTIMATED R≈0 is the competent fixed-allocation floor and ESTIMATED R≈1 the attainable campaign outcome, with the author reference provisionally near ESTIMATED R=0.60 and the premature-stop starter near ESTIMATED R=0.00.
## 2. Strongest lawful combined attack
Replace recent-gain patience with a portfolio that reserves long uninterrupted allocations while pruning clearly dominated branches. [Hyperband](https://jmlr.org/papers/v18/16-558.html) supplies budget diversification; [Freeze-Thaw Bayesian Optimization](https://arxiv.org/abs/1406.3896) supplies continuation forecasts. Use these as components, with a conservative uncertainty floor because an apparent plateau can precede a delayed scientific payoff. Charge the prediction model and checkpoint restoration, and select the final recipe through replicated legal development results.

The researcher can directly edit the governor to keep a baseline branch alive until the campaign deadline, explore alternative experiment families, and occasionally resume uncertain branches. Features should describe what experiment changed and whether an unresolved prerequisite remains, rather than extrapolating only validation loss. Jointly tune allocation fractions and continuation thresholds using completed permitted histories. This is a compact adaptive optimization controller, not a need for new subject-model inference machinery.

ESTIMATED single-run R=0.76, range ESTIMATED 0.52–0.90; ESTIMATED best-of-4=0.83; ESTIMATED pass@4 at R≥0.60=0.95; ESTIMATED projected upper-95% bound=0.96. Relative to the provisional endpoint, removing premature termination recovers most easy gain and portfolio allocation captures much of the remaining experiment-selection gain. The unresolved fraction concerns genuinely unprecedented prerequisites with no early value signal. It would be incorrect to assume the stronger researcher shares present agents' tendency to quit early.
## 3. Other routes
A fixed long-horizon continuation policy is surprisingly strong here: ESTIMATED R=0.64, range ESTIMATED 0.40–0.82. It removes the stated defect while avoiding forecast overhead, although it wastes budget on dead branches.

A search over patience windows, geometrically spaced restarts and protected long-run fractions gives ESTIMATED R=0.70, range ESTIMATED 0.46–0.87. These are inexpensive configuration decisions compared with training, so full-budget development search is plausible. The final comparison must preserve all failed campaigns and rerun chosen recipes; selecting the largest noisy metric without replication is not the lawful attack being credited.
## 4. What would lower lawful saturation
Make continuation contingent on acquiring a costly, informative observation whose availability changes subsequent experiment choices. Require matched early trajectories with different, development-identifiable responses to diagnostic actions; mere random delayed breakthroughs are an information deficit rather than a research challenge. ESTIMATED composite reward might become R=0.46–0.59. Constructing those live campaigns costs ESTIMATED three author-weeks and ESTIMATED 144 H100 GPU-h of response validation. This change would also need a narrower scientific distinction from the existing autonomous-controller task, because its present mechanism already includes delayed reversals and strategy switching.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 10 GPU-h. New ESTIMATED 88 H100 GPU-h comprises an ESTIMATED 0.3B training subject, ESTIMATED four governor arms, ESTIMATED three independent campaign seeds, and ESTIMATED six H100-hours per complete campaign: ESTIMATED 4×3×6=72. Reserve ESTIMATED 16 GPU-h for independent final-recipe verification and interruption recovery checks. The inference-only governor is small; the expensive part is re-executing the agent's chosen experiments. A static trace replay cannot measure counterfactual evidence acquisition, so the old allowance is inadequate.
## 6. Duplicate check
Catalog T03: STRONG. Its source explicitly submits a reusable research controller, grades new live ML projects under complete costs, and includes contextual multi-fidelity allocation, delayed reversals and rollback. Calling the submitted controller a self-edited governor does not change intervention or target. V3 03B: WEAK; its inspected contract trains subject-policy inference-budget allocation rather than the researcher's campaign continuation.
## 7. Verdict
CUT for duplicate T03, independently reinforced by saturation. The ESTIMATED best-of-four excess is 0.23 and the single-run forecast exceeds its line by ESTIMATED 0.06. No additional scientific construct in this card separates it from the existing controller contract.
## 8. Measurement status
Rollouts UNMEASURED (planned: live campaigns with identical initial histories). Grader noise UNMEASURED (planned: independent replay of selected training recipes). Score ladder UNMEASURED (planned: patience starter, always-continue, portfolio governor, response-aware controller).
## Screen record
id: C028
verdict: CUT
binding_line: duplicate
attack_single_est: 0.76
attack_single_range: 0.52-0.90
bo4_est: 0.83
pass4_est: 0.95
ub95_est: 0.96
gpuh_old: 10
gpuh_new_est: 88
duplicate_of: T03 STRONG; 03B WEAK
kill_reason: same campaign-allocation intervention and outcome as T03
souping_flag: no
