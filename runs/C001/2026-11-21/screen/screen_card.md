# C001 — Preserve negative evidence during scientific corpus deduplication — saturation screen
## 1. What the grader actually rewards
The submitted corpus earns credit only through the learner it trains: lower outcome-conditioned log loss on matched successful and failed interventions, with ordinary scientific language retained. On the contract's provisional scale, ESTIMATED R≈0 means matching the competent curation floor, while ESTIMATED R≈1 means reaching an independently attainable stronger corpus control. Neither anchor exists yet; an unchanged crawl pipeline would plausibly receive ESTIMATED R=0.00, and the intended reference is provisionally ESTIMATED R=0.60 rather than a measured baseline.
## 2. Strongest lawful combined attack
Start with [SemDeDup](https://arxiv.org/abs/2303.09540) for candidate duplicate neighborhoods, then change its deletion rule: extract intervention, population, dose, context, outcome direction and uncertainty from each candidate. Preserve documents whenever any consequential tuple differs, including failed replications; remove only redundant descriptions within each tuple. Add a conservative disagreement bucket instead of resolving uncertain contradictions by majority vote. [DataComp-LM](https://arxiv.org/abs/2406.11794) supplies a verified precedent for controlled filtering experiments and ordinary quality filtering, although neither paper establishes performance on this proposed task.

The frontier researcher can inspect representative extraction failures, create local consistency checks, cap exposure per tuple and tune the negative/positive balance using admitted dev loss. This combines semantic deduplication, information extraction, stratified sampling and exposure search. It attacks the actual error directly: the original pipeline mistakes similar wording for equivalent experimental evidence. It does not require discovering hidden interventions or rewriting the learner.

Forecasts are ESTIMATED single-run R=0.78, range 0.61–0.90; ESTIMATED oracle best-of-4 mean=0.84; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% planning bound=0.96. The bound is a subjective stress envelope, not a fitted confidence interval. In reward units, the attack likely obtains most attainable gain from restoring deleted contrasts, leaving unresolved reporting ambiguity and learner sensitivity to exposure. These residuals seem too small to protect a benchmark whose central deletion mistake is visible in the task statement. Reclassifying this stack as the floor afterward would change the task, not establish current headroom.
## 3. Other routes
- A single conservative recipe keeps every member of a contradictory cluster and otherwise uses lexical deduplication: ESTIMATED R=0.67, range 0.43–0.82. It wastes tokens, but strongly favors the loss term the grader actually evaluates.
- Search varies cluster radius, contradiction-confidence threshold, per-condition cap and failure sampling weight, with early elimination on paired dev loss: ESTIMATED R=0.73, range 0.52–0.87. Cheap corpus transformations permit substantial exploration before expensive retraining.
- A lawful negative-heavy corpus might exploit the matched-pair evaluation prevalence. ESTIMATED R=0.48, range 0.20–0.72; ordinary-text retention and matched conditional questions should limit this, but the mixture must be frozen explicitly.
## 4. What would lower lawful saturation
Use reports where the same outcome polarity has different evidential value depending on cross-report causal conditions, with ambiguous wording represented equally in positive and negative documents. Require calibration across independently authored condition combinations, and score transfer after a disclosed follow-up adaptation stage. Merely adding more duplicates will not help. This could lower the composite to ESTIMATED R=0.49, range 0.28–0.70, at ESTIMATED authoring effort of several researcher-weeks and ESTIMATED 240 additional H100 GPU-h for anchor and transfer comparisons. Preserve legally extractable conditions; withholding necessary context would turn curation into guessing.
## 5. Decisive-check GPU-h re-estimate
Old card allowance: ESTIMATED 6 GPU-h. New ESTIMATED 156 H100 GPU-h: a continued-pretraining subject of ESTIMATED 1B parameters, ESTIMATED 4 arms (inherited pipeline, conservative retention, complete attack, independent reference), ESTIMATED 3 seeds each, ESTIMATED 12 H100-hours per run, plus ESTIMATED 12 GPU-h for outcome/ordinary-text evaluation: ESTIMATED 4×3×12+12=156. Assume ESTIMATED billions of exposed tokens across each continuation, with throughput verified before committing the budget. The former allowance could screen extraction quality, but cannot compare learned conditional likelihoods reliably. This is a falsification pilot; researcher-tail certification would cost considerably more.
## 6. Duplicate check
v3 01A, source opened at `task_design_v3_codex/01_data_distribution.md`: WEAK, because both curate corpora but its intervention is stage-dependent source allocation and its target includes post-adaptation capability. FIX T02, source inspected at `fix_packets_v4/T02/packet.md`: WEAK, since optimizer/retention-aware continued pretraining is broader than preserving contradictory reports during deduplication. Neither is the same intervention and grader target.
## 7. Verdict
CUT. The binding best-of-four estimate exceeds its kill line by ESTIMATED 0.24; single-run and projection estimates also breach their respective boundaries. This is a plausible data-engineering task, but the disclosed information-loss mechanism invites a compact, competent repair with little demonstrated residual research difficulty.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget curation attempts on fresh intervention families). Grader noise UNMEASURED (planned: paired learner seeds and repeated fixed-artifact evaluation). Score ladder UNMEASURED (planned: unchanged pipeline, contradiction retention, full composite, reference and stronger control in native log-loss units).
## Screen record
id: C001
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.78
attack_single_range: 0.61-0.90
bo4_est: 0.84
pass4_est: 0.98
ub95_est: 0.96
gpuh_old: 6
gpuh_new_est: 156
duplicate_of: v3-01A WEAK; FIX-T02 WEAK
kill_reason: tuple-preserving curation recovers the principal reward
souping_flag: no
