# C121 — An agent that builds its own small falsifiable research benchmark — saturation screen
## 1. What the grader actually rewards
Reset researchers use the submitted small benchmark to choose patches, and the selected patches must improve independently executed ML projects. Test count and mutation coverage are diagnostic only; benchmark execution competes with the research it is meant to improve. ESTIMATED R≈0 is the patch utility obtained with a competent representative benchmark, and ESTIMATED R≈1 is attainable stronger selection under the same full campaign cost. The original tiny self-test and intended ESTIMATED reference R≈0.60 need native selected-patch utility measurements before any reward-scale claim is credible.
## 2. Strongest lawful combined attack
Build a compact suite from real workload strata, covering complete updates, checkpoint transitions and end-to-end timing rather than isolated toy operations. [Airspeed Velocity](https://github.com/airspeed-velocity/asv) verifies mature benchmark and regression infrastructure; its [timing guidance](https://asv.readthedocs.io/en/stable/tuning.html) supports careful treatment of measurement variation. [Hypothesis](https://github.com/hypothesisWorks/hypothesis/) verifies property-based input generation and counterexample reduction, useful for unusual valid patches as well as faults. These tools provide infrastructure, not evidence of any score on private ML projects.

The attacker would create independently equivalent correct implementations and representative bad patches, measure how candidate probes rank them, and select a small probe set maximizing decision value per execution cost. Keep a final full training-step check for high-ranked patches and spend additional time only when confidence intervals overlap. Include real learning continuation for changes whose benefit is not determined by immediate exactness or throughput. Tune the suite against held-out development patch mechanisms, then freeze it before private project evaluation. This attacks the selection endpoint directly and avoids mistaking mutation score for scientific value.

ESTIMATED single-run R=0.74, range 0.52–0.89; ESTIMATED oracle best-of-4=0.82; ESTIMATED pass@4 at R≥0.60=0.95; ESTIMATED projected upper-95% score=0.94. Rank reversals across scale and delayed learning interactions leave residual risk. However, a representative mini-campaign with sequential promotion already handles more than mutation coverage, and the card does not specify which expensive private interaction remains unpredictable from its legal probes. A weak tiny starter is a large source of easily recoverable reward.
## 3. Other routes
A representative end-to-end benchmark with matched warmup and repeated timing is the strongest single recipe. ESTIMATED R=0.61, range 0.39–0.80. It can select good patches without a learned diagnostic model or elaborate mutation search.

Search over workload cases, probe durations, correctness checks and confidence-based promotion has ESTIMATED R=0.69, range 0.46–0.86. Optimize selected-patch improvement on full development projects rather than benchmark accuracy against a finite fault list. A lawful alternative spends nearly all diagnostic time directly testing the leading patches on the target development project: ESTIMATED R=0.66, range 0.41–0.85. A reusable small benchmark is valuable only if it beats that allocation after its construction cost is included.
## 4. What would lower lawful saturation
Choose project families with validated scale/horizon reversals and require an affordable diagnostic intervention that predicts the direction of those reversals across unfamiliar patch mechanisms. Keep equivalent unusual patches positive and make development workloads match deployment concurrency and state. ESTIMATED score reduction is 0.13–0.21, to around 0.53–0.61, leaving tail risk unresolved. ESTIMATED authoring effort is 12–20 person-days and 300 H100-h for real patch-outcome histories. Simply shrinking benchmark time until every method guesses would destroy identifiability and useful weak-agent signal.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 12 GPU-h. New ESTIMATED total is 128 H100 GPU-h. Assume a fixed 4B researcher and 1B training projects: 4 benchmark policies × 2 campaign seeds × 3 held-out projects × 3 H100-h for selected-patch execution = 72; independent full-outcome controls for 6 patch/project contrasts × 6 H100-h = 36; benchmark timing, agent inference and repeated grades = 20. ESTIMATED sum 72+36+20=128. Pure kernel timings may be much cheaper, but the card's training/system endpoint requires meaningful continuation for training patches. The old estimate mostly covers the instrument, not its downstream decisions.
## 6. Duplicate check
D24, MODERATE: its source submits a reusable paid diagnostic controller and grades selected fixed-policy deployment utility, while this card installs a self-benchmark in researchers who choose executable ML patches. T03, MODERATE: it already chooses research experiments, but the submitted artifact here is the diagnostic benchmark rather than the full controller. Neither comparison warrants STRONG duplication without equating policy selection with newly executed patch research.
## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds its line by 0.22, and the single-run estimate exceeds its line by 0.04. Representative complete checks plus sequential patch promotion can plausibly capture most gains over the inherited tiny self-test.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent benchmark-design attempts followed by reset research campaigns). Grader noise UNMEASURED (planned: repeated warm timings, agent selections and selected-patch training seeds). Score ladder UNMEASURED (planned: original self-test, representative suite, property-based suite, sequential promotion, reference and stronger attainable selection control).
## Screen record
id: C121
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.74
attack_single_range: 0.52-0.89
bo4_est: 0.82
pass4_est: 0.95
ub95_est: 0.94
gpuh_old: 12
gpuh_new_est: 128
duplicate_of: D24 MODERATE; T03 MODERATE
kill_reason: representative complete checks and sequential promotion solve weak self benchmark
souping_flag: no
