# C113 — An agent that upgrades its numerical debugging instrument — saturation screen
## 1. What the grader actually rewards
The debugger must help reset research agents choose repairs that improve actual training on private numerical incidents, after diagnostic reads and experiments are charged. Reporting more tensor differences is useless unless it changes a repair and its downstream learning outcome. ESTIMATED R≈0 means no gain beyond competent scale-aware comparison and selective replay; ESTIMATED R≈1 means attainable incident recovery under the same access and cost limits. The planned ESTIMATED reference R≈0.60 remains unanchored, and an agent applying a generic stable repair without debugging must also be scored.
## 2. Strongest lawful combined attack
Replace global tolerance checks with per-operation error summaries, magnitude distributions, signed cancellation indicators, update-to-parameter ratios and first-divergence localization. [Herbgrind](https://arxiv.org/abs/1705.10416) verifies high-precision shadow analysis and numerical root-cause tracing; [NSan](https://arxiv.org/abs/2102.12782) verifies a practical numerical sanitizer. They are methodological precedents, not drop-in instrumentation for arbitrary GPU tensor programs. For actual CUDA execution, [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/) supplies complementary memory/race checks, not a floating-point accuracy oracle.

The combined instrument would capture bounded real-path tensors, bisect the earliest update divergence, and replay only the implicated reduction or nonlinear operation with wider arithmetic. Preserve the original dispatch and inputs for the primary reproduction, comparing a separate mathematical reference without pretending it follows the same kernel path. Perturb scales and reduction order locally to separate cancellation from indexing, masking and stale-state bugs. Feed the reset agent concrete counterexamples and run small repair interventions before paying for longer continuation. This familiar workflow directly handles the starter comparator's blind spots while respecting the read budget.

ESTIMATED single-run R=0.61, range 0.39–0.81; ESTIMATED oracle best-of-4=0.71; ESTIMATED pass@4 at R≥0.60=0.77; ESTIMATED projected upper-95% score=0.88. A real residual remains when instrumentation changes scheduling or only a long low-precision trajectory triggers the error. Yet bounded capture and actual-path differential testing address much of that risk, and the card does not commit to a family requiring a new diagnostic principle rather than a better comparator implementation.
## 3. Other routes
The strongest single recipe is magnitude-aware tensor comparison plus selective high-precision replay around the earliest mismatch. ESTIMATED R=0.49, range 0.29–0.71. It should catch cancellation and reduction defects without a complete dynamic analysis system.

Search over capture points, tolerance functions, sampled tensor coordinates and perturbation amplitudes can optimize downstream repair yield. ESTIMATED R=0.57, range 0.34–0.79, with all diagnostic reads and agent attempts included. A generic stable-implementation replacement is a lawful bypass: ESTIMATED R=0.64, range 0.35–0.88 if incidents lie in a few known loss/reduction operators. The debugger must beat that route on useful learning, rather than receive credit for explaining a repair the agent could have applied immediately.
## 4. What would lower lawful saturation
Select actual incidents where errors emerge only through interactions of scale, dispatch and optimizer state, and where replacing every suspect operation with a slow stable version loses the fixed training budget. Preserve a valid local reproduction obtainable through bounded paid captures. ESTIMATED attack reduction is 0.10–0.18, to approximately 0.43–0.51. ESTIMATED authoring cost is 10–17 person-days and 160 H100-h for independent low-precision histories and replay validation. A hidden hand-authored bug catalogue would make fault identification enumerable and should not be mistaken for this stronger setting.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 12 GPU-h. New ESTIMATED pilot is 112 H100 GPU-h. Assume a 1B subject learner and fixed 4B diagnostic agent: 4 debugger arms × 2 independent incident mechanisms × 2 seeds × 4 H100-h repair continuation = 64; actual-path capture and selective arithmetic replay = 16; reset-agent inference = 16; independent final learning and repeat-grade checks = 16. ESTIMATED total 64+16+16+16=112. CPU analysis is extra elapsed work, not GPU utilization. The old value may suffice for a kernel-level mismatch reproduction, but not for the required debugger-to-repair-to-learning chain.
## 6. Duplicate check
D13, MODERATE: its source requires incident repair and causal certificates from a trained investigator, whereas C113 submits a reusable numerical instrument to a reset agent. 04B, WEAK: its opened context co-designs numerical precision and recovery for the learner, not the diagnostic tool. 05B, WEAK: exact update verification is shared infrastructure, but its submission optimizes execution throughput.
## 7. Verdict
CUT. ESTIMATED oracle best-of-4 is 0.11 over its line and pass@4 is 0.27 over. The instrument is concrete and useful, but the proposed numerical failure families are already natural targets for selective shadow replay and divergence localization.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent debugger-building attempts followed by reset-agent repairs). Grader noise UNMEASURED (planned: replay fixed captures, repeat agent decisions and retrain selected repairs). Score ladder UNMEASURED (planned: starter comparator, mature comparator, selective replay, generic stable repair, reference debugger and stronger recovery control).
## Screen record
id: C113
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.61
attack_single_range: 0.39-0.81
bo4_est: 0.71
pass4_est: 0.77
ub95_est: 0.88
gpuh_old: 12
gpuh_new_est: 112
duplicate_of: D13 MODERATE; 04B WEAK; 05B WEAK
kill_reason: selective shadow replay and divergence localization cover stated incidents
souping_flag: no
