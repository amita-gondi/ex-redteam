# C019 — Autotune without teaching the model the tuner workload — saturation screen
## 1. What the grader actually rewards
The tuning policy chooses kernels, but reward comes from verified multimodal completions divided by serving time plus amortized tuning cost. A kernel that wins hot-buffer timings and loses under actual request residency therefore hurts utility. ESTIMATED R≈0 is the competent repaired representative-tuning floor, ESTIMATED R≈1 the stronger attainable end-to-end tuner; unchanged hot-cache tuning is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60, with the amortization horizon still unfrozen.
## 2. Strongest lawful combined attack
The cited [SGLang issue](https://github.com/sgl-project/sglang/issues/50057) exists: its reported title concerns an empty blockwise search space and weights resident in cache during timing. That verifies the lead, not a locally reproduced defect or its current fix status. Start after the public feasibility correction, then measure candidates under rotating weight buffers, multiple reuse distances and representative complete requests. [NVIDIA CompileIQ benchmarking guidance](https://nvidia.github.io/CompileIQ/v1.1/benchmarking.html) verifies cold-cache measurement tooling; [TVM MetaSchedule](https://tvm.apache.org/docs/deep_dive/tensor_ir/tutorials/meta_schedule.html) verifies a mature measured-search framework.

Combine those tools with randomized candidate order, disjoint process starts, explicit allocator snapshots and a configuration cache keyed by shapes plus relevant residency regime. Allocate tuning effort by deployment frequency and potential regret, not equal repetitions for every tile. For promising candidates, restore a controlled request prelude and validate the winner in untouched end-to-end traffic. Treat probe-induced residency as a measurement confound: alternate candidates on the same restored prelude, and let a low-overhead online policy select among a small verified set. All feature collection, compilation and retuning are amortized at the same horizon as serving.

ESTIMATED single-run R=0.73, range 0.49–0.88; ESTIMATED oracle best-of-4=0.81; ESTIMATED pass@4 at R≥0.60=0.94; ESTIMATED upper-95% projection envelope=0.94. These forecasts are not cache measurements. Representative replay and proper blocking should remove most of the known misselection, and a conditional dispatch cache handles recurring image-token regimes. Residual difficulty lies in allocator transitions whose state cannot be restored cheaply and workload changes that invalidate previous measurements. The present card does not yet show that these effects defeat disciplined replay tuning rather than merely naive hot-cache benchmarking.
## 3. Other routes
- Full-request replay tuning with one deployment-wide kernel choice: ESTIMATED R=0.58, range 0.34–0.79. It avoids unrealistic microbenchmarks but compromises across residency regimes.
- Search tile choices jointly with cache-key features, probe frequency and tuning horizon; use multi-fidelity elimination followed by independent traffic confirmation. ESTIMATED R=0.68, range 0.44–0.85. Many rejected candidates need no long serving trial.
- Disable expensive tuning and select a robust library default. ESTIMATED R=0.43, range 0.16–0.73, strongly dependent on the amortization horizon. If this wins because the horizon is tiny, the environment rewards avoiding a bad tuner rather than researching measurement policy.
## 4. What would lower lawful saturation
Freeze realistic amortization horizons and create observable state-transition graphs where probing one candidate changes later kernel value. Supply equivalent dev transitions and include restored-prelude replay as the floor. Require the submitted policy to decide when enough evidence exists to stop perturbing deployment state. Forecast after that change: ESTIMATED R=0.45, range 0.24–0.67. Cost is ESTIMATED several weeks of allocator/residency workload authoring and ESTIMATED 48 extra H100 GPU-h. Replacing hot-cache timings with cold-cache timings alone is a standard repair and should not be presented as the remaining insight.
## 5. Decisive-check GPU-h re-estimate
Old card allowance: ESTIMATED 5 GPU-h. Revised ESTIMATED 32 H100 GPU-h assumes an ESTIMATED 3B-parameter VLM on ESTIMATED 1 H100, ESTIMATED 4 tuner policies, ESTIMATED 3 independent traffic/residency seeds per policy and ESTIMATED 2 cold process repetitions per seed, each ESTIMATED 0.75 GPU-h: ESTIMATED 4×3×2×0.75=18. Add ESTIMATED 8 GPU-h for legal search/compilation and ESTIMATED 6 GPU-h for correctness and amortization checks: ESTIMATED total 32. There is no subject-model training. The original value is plausible for a local hot/cold diagnostic but thin for end-to-end winner selection across distinct residency transitions.
## 6. Duplicate check
v3 05A (`task_design_v3_codex/05_exact_systems.md`, source previously opened): WEAK; it optimizes serving execution directly, whereas C019 submits the tuning/measurement policy and its dispatch cache. D24 (`hidden_task_cards_v4/cards/D24.md`, source opened): WEAK, because paid testing and selection are similar but its candidates are fixed policies, not kernels whose measurement changes accelerator residency. No indexed STRONG duplicate is identified.
## 7. Verdict
CUT. The ESTIMATED best-of-four breach is 0.21, and the single-run breach ESTIMATED 0.03. The verified public timing pitfall gives the attacker a concrete repair, while representative replay plus conditional dispatch is a credible complete saturation stack.
## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget measurement policies after the public feasibility repair). Grader noise UNMEASURED (planned: restored preludes, randomized order and cold-start replications). Score ladder UNMEASURED (planned: hot-cache, cold-cache, full replay, conditional replay and attainable adaptive tuner).
## Screen record
id: C019
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.73
attack_single_range: 0.49-0.88
bo4_est: 0.81
pass4_est: 0.94
ub95_est: 0.94
gpuh_old: 5
gpuh_new_est: 32
duplicate_of: v3-05A WEAK; D24 WEAK
kill_reason: repaired representative replay tuning likely selects near-best kernels
souping_flag: no
