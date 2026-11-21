# C013 — Build an evaluator that prices research reversibility — saturation screen
## 1. What the grader actually rewards
The evaluator selects a recipe, and that selection earns the quality actually recovered after a trusted interruption and cold restart. Predicting restart duration or identifying a checkpoint defect is useful only insofar as it selects a better resumed learning trajectory. ESTIMATED R≈0 matches the competent recovery-ranking floor, ESTIMATED R≈1 reaches a feasible stronger selector, no-op final-loss ranking is provisionally ESTIMATED R=0.00, and the intended reference ESTIMATED R=0.60 remains an unmeasured anchor.
## 2. Strongest lawful combined attack
Inventory each recipe's model, optimizer, scheduler, sampler, RNG and data-lineage dependencies, then run bounded cold-restoration probes at multiple interruption phases. [PyTorch Distributed Checkpoint](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html) verifies available model/optimizer persistence and resharding facilities; [CheckFreq](https://www.usenix.org/conference/fast21/presentation/mohan) verifies fine-grained checkpoint profiling and resumable data iteration. The attacker uses these as a checklist and instrumentation basis, not as permission to edit the candidate recipes themselves.

Combine structural state-dependency checks with empirical short continuations after killing all original processes and dropping author caches. Rank by predicted terminal quality at the remaining budget, charging save latency, lost work, reconstruction and any learning divergence. A survival or hazard model can estimate interruption exposure, while a regression model estimates resumed quality conditional on the observed state gaps. Search the placement of probes to maximize ranking discrimination, reserving expensive checks for recipe pairs whose uninterrupted quality is similar. This directly catches the supposedly difficult case where state appears present but relies on an inaccessible assumption: a genuine cold continuation exercises that assumption.

ESTIMATED single-run R=0.74, range 0.51–0.89; ESTIMATED oracle best-of-4=0.82; ESTIMATED pass@4 at R≥0.60=0.94; ESTIMATED upper-95% projection envelope=0.95. They are planning estimates with no fitted survival or score data. The main gain is selecting a slightly worse uninterrupted recipe that actually resumes, which routine fault injection should expose. Residual uncertainty comes from hidden interruption mechanisms not represented by the probes and from long-horizon optimizer divergence. Because dev offers equivalent recovery access, an automated probe battery is a strong lawful competitor rather than a weak baseline.
## 3. Other routes
- Rank on one full cold restart plus checkpoint-age-adjusted learning value. ESTIMATED R=0.60, range 0.36–0.81. It misses phase-specific and correlated failures but directly measures the target behavior.
- Sweep interruption phases, state components to test, short continuation lengths and hazard/quality weights. ESTIMATED R=0.69, range 0.44–0.87. Efficient allocation across close recipe pairs can outperform an elaborate learned predictor.
- Choose a robustly checkpointed recipe with a modest uninterrupted-loss penalty whenever its restoration test passes. ESTIMATED R=0.52, range 0.27–0.77. This conservative selection shortcut is especially effective if catastrophic non-recovery dominates the metric.
## 4. What would lower lawful saturation
Give the evaluator a real paid probe budget and recipes with compositional dependencies where a cheap successful restart does not certify later recoverability. Make the same dependency evidence available in dev, and independently demonstrate a legal adaptive probe strategy that predicts which longer continuation will fail. Price probe opportunity cost in final recovered quality. Forecast composite after revision: ESTIMATED R=0.48, range 0.26–0.70, for ESTIMATED several weeks of realistic interrupted-training authoring and ESTIMATED 216 extra H100 GPU-h. New fault names alone will not defeat a cold-execution checker; the dependency must change probe value without hiding necessary information.
## 5. Decisive-check GPU-h re-estimate
The original allowance is ESTIMATED 8 GPU-h. Revised ESTIMATED 180 H100 GPU-h uses an ESTIMATED 1B-parameter training workload with ESTIMATED 4 candidate recipes, ESTIMATED 3 seeds and ESTIMATED 3 interruption placements; each trusted continuation consumes ESTIMATED 4 H100-hours: ESTIMATED 4×3×3×4=144. Share these outcomes across ESTIMATED 3 evaluator arms rather than rerunning identical recipes unnecessarily. Add ESTIMATED 24 GPU-h for probe training/continuations and ESTIMATED 12 GPU-h for independent evaluation, yielding ESTIMATED 180. The old value might expose one missing state component, but cannot establish selection value over interruption distributions.
## 6. Duplicate check
v3 07B (`task_design_v3_codex/07_measurement_and_reward.md`, task opened): WEAK, because that evaluator scores scientific evidence rather than selecting recoverable training recipes. v3 05B (`task_design_v3_codex/05_exact_systems.md`, source opened): MODERATE; resumable state is a shared target, but its submitted intervention accelerates the training graph while preserving state, whereas C013 changes an evaluator selecting among fixed recipes. The artifact/target pairing therefore differs.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds the gate by 0.22 and the single-run forecast by ESTIMATED 0.04. A dependency inventory plus cold continuation battery seems able to capture the disclosed reversibility advantage without an additional research insight.
## 8. Measurement status
Rollouts UNMEASURED (planned: cost-accounted adaptive recovery evaluators). Grader noise UNMEASURED (planned: repeated interruption/continuation seeds from identical durable states). Score ladder UNMEASURED (planned: uninterrupted-loss ranking, checkpoint-age ranking, cold-probe ranking, adaptive probes and stronger selector).
## Screen record
id: C013
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.74
attack_single_range: 0.51-0.89
bo4_est: 0.82
pass4_est: 0.94
ub95_est: 0.95
gpuh_old: 8
gpuh_new_est: 180
duplicate_of: v3-07B WEAK; v3-05B MODERATE
kill_reason: cold fault-injection probes directly measure useful recovery
souping_flag: no
