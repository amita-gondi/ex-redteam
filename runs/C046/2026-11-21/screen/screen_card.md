# C046 — Pretrain a model that can change its own activation budget — saturation screen
## 1. What the grader actually rewards
The trained model must maintain useful sequence likelihood while allowed layer depth changes during generation, with every executed layer and state-conversion step charged. Static shallow quality is insufficient if deeper continuation consumes incompatible or absent historical state. ESTIMATED R≈0 denotes competent elastic-depth training and ESTIMATED R≈1 a stronger feasible transition-aware model; independent-depth distillation is provisionally ESTIMATED R=0.00, reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Use layer dropout, shared early-exit prediction heads and depth-conditioned teacher losses, then train on actual token-level depth transitions. [LayerSkip](https://arxiv.org/abs/2404.16710) establishes joint layer-dropout/early-exit training. [CALM](https://arxiv.org/abs/2207.07061) directly addresses per-timestep compute changes and missing historical representations, so the transition problem is not untouched by standard methods.

Combine representation alignment with explicit missing-state policy: copy/project lower-depth states where validated, reconstruct necessary deeper history only when the metered availability contract permits it, and train against the resulting mixed-depth cache distribution. Include abrupt shallow-to-deep transitions and transitions after difficult tokens in the curriculum. Tune dropout, depth sampling, alignment weight and limited backfill jointly against complete-sequence loss/FLOPs. The attacker need not use full-depth self-speculative verification when that would violate the active budget; the transferable pieces are elastic training and explicit cache-state handling.

ESTIMATED single-run R=0.68, range ESTIMATED 0.41–0.86; ESTIMATED best-of-4=0.77; ESTIMATED pass@4 at R≥0.60=0.87; ESTIMATED projected upper-95% bound=0.93. On the provisional scale, established elastic-depth training captures static compatibility and much ordinary switching gain, while transition exposure reduces the remaining distribution mismatch. Residual failures arise when long shallow histories omit information needed by resumed deep computation and cheap reconstruction cannot recover it. That can be a physical information bottleneck affecting all methods rather than exclusive scientific headroom.
## 3. Other routes
Layer-dropout training with shared exits alone scores ESTIMATED R=0.53, range ESTIMATED 0.28–0.75. It aligns intermediate predictions but does not fully match deployed cache histories.

A sweep over depth schedules, cache-state projection and reconstruction thresholds reaches ESTIMATED R=0.61, range ESTIMATED 0.35–0.81. Since abrupt switches are disclosed, a researcher can deliberately generate many transition examples rather than hope random adjacent-depth sampling covers them. A conservative shallow-history model that avoids expensive deeper reuse is another lawful route, ESTIMATED R=0.40, range ESTIMATED 0.17–0.66, potentially strong if the utility grants little value to deeper recovery.
## 4. What would lower lawful saturation
Start from a complete CALM/LayerSkip-style baseline trained on the exact switching interface, then demonstrate a recoverable long-history incompatibility with substantial same-budget reserve. Include transitions where copying and cheap projection both fail but a legal representation-learning control succeeds. ESTIMATED combined R could become 0.45–0.57. ESTIMATED cost is five model-research weeks and ESTIMATED 320 H100 GPU-h for causal state-recovery checks. More severe depth limits alone risk reducing the attainable ceiling rather than increasing research difficulty.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 16 GPU-h. Revised ESTIMATED 304 H100 GPU-h assumes an ESTIMATED 1B subject, ESTIMATED four elastic-training arms, ESTIMATED two independent seeds and ESTIMATED 30 H100-hours per continued-training run: ESTIMATED 4×2×30=240. Transition-trace evaluation and cache-state interventions add ESTIMATED 48 GPU-h, while full-depth teacher targets add ESTIMATED 16 GPU-h. A single H100 is assumed per run, with all auxiliary work included. The old estimate may compare short transition losses but cannot establish stable mixed-depth training or the full quality/compute frontier.
## 6. Duplicate check
03B: MODERATE, after reading its budget-conditioned student contract, but C046 changes activated layer depth and historical state compatibility instead of reasoning/tool expenditure. 06A: WEAK from its inspected attention-compression contract. 04B: WEAK after reading its changing-precision learning target; it edits arithmetic policy rather than depth-conditioned historical representations. The transition representation is a distinct mechanism.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds its line by 0.17 and pass@4 by 0.37. Existing adaptive-depth methods already address the central missing-state issue, making a stronger combined training stack likely to breach repeated-search gates.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete variable-depth training and mixed-history evaluation). Grader noise UNMEASURED (planned: repeated learner and switch-trace seeds). Score ladder UNMEASURED (planned: isolated exits, elastic training, transition stack and attainable recovery model).
## Screen record
id: C046
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.68
attack_single_range: 0.41-0.86
bo4_est: 0.77
pass4_est: 0.87
ub95_est: 0.93
gpuh_old: 16
gpuh_new_est: 304
duplicate_of: 03B MODERATE; 06A WEAK
kill_reason: elastic-depth training and missing-state handling are established
souping_flag: no
