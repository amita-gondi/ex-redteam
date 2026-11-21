# C126 — A reusable kernel tool library judged by the next research project — screen audit
## 1. What the screen claimed
The screen combined CUTLASS/Triton portfolios, guard extraction, call-site tests and complete-graph profiling, including direct compiler replacement. Its ESTIMATED single/bo4/pass4/ub95=0.80/0.88/0.98/0.97 produced CUT, category SYS: standard guarded reuse addresses hidden shape and precision assumptions. URLs: https://docs.nvidia.com/cutlass/latest/index.html; https://docs.nvidia.com/cutlass/latest/media/docs/cpp/profiler.html; https://triton-lang.org/main/python-api/generated/triton.autotune.html; https://docs.pytorch.org/docs/main/user_guide/torch_compiler/compile/programming_model.reducing_guard_overhead.html.

## 2. Evidence audit
Welcome to CUTLASS and CUTLASS Profiler — NVIDIA, 2026 documentation snapshots — both fetched, establish mature implementations and verification/search facilities for supported operations. triton.autotune — Triton project, 2026 retrieved documentation — fetched, confirms keyed configuration tuning and input-state restoration options; the correct key still has to encode relevant assumptions. Reducing Guard Overhead — PyTorch, 2026 retrieved main documentation — fetched, concerns reuse under captured conditions, not discovering numerical preconditions for scientific equivalence. These living documents do not state a single original publication year.

Grade: PARTIAL. Strong implementations support the portfolio route, but no old citation measures an agent extracting a reusable library and improving its next research project after charging construction. In particular, local numerical tolerance and whole-graph error sensitivity are different validity claims.

## 3. Research done now
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng/PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — directly raises the plausibility of profiled kernel search, while its evaluation does not measure reusable-library transfer between reset projects.
- CudaForge: An Agent Framework with Hardware Feedback for CUDA Kernel Optimization — Zijian Zhang, 2025 — https://arxiv.org/html/2511.01884v1 — fetched — provides model, hardware and per-kernel timing for autonomous optimization, substantially stronger evidence than library documentation.
- CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation — Weinan Dai, 2026 — https://arxiv.org/abs/2602.24286 — fetched — reports strong compiled-baseline faster rates from a human-engineered trained system. It raises the primitive-generation ceiling without demonstrating twelve-hour discovery of a reusable abstraction. The HTML endpoint returned no readable body, so only the abstract's claims are used.

Search emphasized kernel-agent timing, numerical verification and contemporary compiled comparisons. None verified the entire library-construction/downstream-consumption experiment.

## 4. Re-estimated attack
The numerical models below are ESTIMATED, including all probability weights. Conditional on successful integration, allocate 0.27 reward to guarded portfolio dispatch, 0.22 to feedback-guided retuning and 0.15 to graph-level composition and validation. Mean contribution=0.64. Safe fallbacks retain correctness but can erase speedup; they cannot be counted as capturing performance reward merely because every graph runs.

Use R={0.48,0.66,0.79}, probabilities {0.23,0.59,0.18}. These represent conservative fallback, useful retuning and discovery of reusable fusion. Single=0.23×0.48+0.59×0.66+0.18×0.79=0.64, range 0.48–0.79. Bo4=0.79−0.13×0.82^4−0.18×0.23^4=0.73. With p=0.77, pass4=1−0.23^4=1.00 rounded; ub95=0.79. Most run variation is choosing the abstraction and allocating validation effort; mature dispatch itself should be nearly deterministic. This is substantially below the old point estimate because kernel correctness, graph speed and amortized construction cost are separate hurdles.

## 4A. Demonstrated capability and subfield SOTA
Strongest reported comparator located: CUDA Agent's faster-than-torch.compile rates are 100%/100%/92% on KernelBench levels. These are task rates, not speedup magnitudes and not transferable-library utility. Anchor the floor to compiled graphs plus guarded vendor libraries, and the stronger endpoint to independently measured same-budget whole-graph savings. The inherited 1B–4B workloads have no native timing anchors yet; assigning R≈1 from isolated-kernel rates would be invalid.

Agent demonstration one: KernelAgent's profiler-guided scaffold reports 1.56× over default torch.compile on a hundred level-one tasks using H100 measurements. Backbone and complete search time are unspecified, blocking a twelve-hour comparability claim. Demonstration two: OpenAI-o3 in CudaForge's coder/judge loop reports 97.6% correctness and 1.68× over its PyTorch baselines, about 26.5 minutes per kernel on one RTX6000. Its baseline and workload differ, and it optimizes supplied operations rather than teaching a reset researcher a reusable library.

KNOWN-RECIPE includes guards, autotuning and profiling. AGENT-DEMONSTRATED kernel optimization is strong; autonomous amortized library extraction with end-to-end numerical transfer is not established. For the complete attack, attack_basis=LITERATURE-ONLY. The missing twelve-hour work is creating useful reusable boundaries, testing them under changed contracts and recovering enough downstream runtime to repay library construction.

ANCHORED allowances are 0.22 mature reuse, 0.17 tuning and 0.10 transferable composition. Distribution R={0.27,0.52,0.68}, masses {0.22,0.64,0.14}, yields single=0.49, range 0.27–0.68; bo4=0.68−0.16×0.86^4−0.25×0.22^4=0.59; pass4=1−0.86^4=0.45; ub95=0.68. Library integration failures widen the downside despite fast per-kernel search. Forecast transfer masses remain assumptions; no claim is made that contemporary agents are weak at kernels.

## 5. Verdict under the kill lines
Section 4 CUT; headline ANCHORED CONDITIONAL, FLIPPED CUT→CONDITIONAL. Bo4 has ESTIMATED 0.01 margin, requiring a direct all-in library-versus-compiler comparison. CudaForge establishes affordable autonomous search, but the absence of a demonstrated reusable-artifact transfer result removes support for the old high attack reward. Promotion requires incremental reusable abstraction gain after the strongest direct compiler and kernel-agent controls.

## 6. Redesign
Cause (a): mature kernel stacks solve ordinary validity-aware reuse. Share guarded vendor kernels, direct compilation and profiler-guided search as the floor. Require a reusable scheduling/numerical abstraction across real graph families with coupled resource use—for example deciding when a reduction can remain resident across a following operation without violating the graph's disclosed error budget. Hold out operation compositions, retain matched development examples and test the abstraction on several graphs. This is useful compiler/kernel R&D, with all lawful fallback routes available.

Strongest re-attack combines vendor dispatch, agent-generated kernels, autotuning and graph profiling. It must now generalize a cross-operation decision, rather than retune an inherited tile size. ESTIMATED modes {0.21,0.42,0.64}, probabilities {0.25,0.66,0.09}, imply single=0.39; bo4=0.64−0.22×0.91^4−0.21×0.25^4=0.49; pass4=1−0.91^4=0.31; ub95=0.64. Basis LITERATURE-ONLY for this wider transfer. REDESIGNABLE; a compiler pass already implementing the chosen abstraction is the chief residual risk and must enter the floor.

Pilot ESTIMATED 64 H100 GPU-h: 1B–4B graph workloads, 4 strategies×2 reset seeds×3 hours×1 H100=24; extraction and tuning=16; independent adversarial-value graph replay/timing=16; fixed 4B researcher inference=8. This tests same-device transfer; distributed variants need separate costing.

## 7. Measurement status
Rollouts UNMEASURED (planned independent library construction and reset graph optimization). Grader noise UNMEASURED (planned repeated warmed whole-graph timings). Score ladder UNMEASURED (planned guarded vendor floor, direct compiler, kernel-agent search, reusable abstraction and feasible stronger library).

## Audit record
id: C126
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 4
sources_new_count: 3
sources_fetched_count: 7
old_single: 0.80
old_bo4: 0.88
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.64
new_single_range: 0.48-0.79
new_bo4: 0.73
new_pass4: 1.00
new_ub95: 0.79
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Reward reusable cross-operation scheduling and numerical contracts beyond shared guarded libraries and direct kernel search.
redesign_single: 0.39
redesign_bo4: 0.49
redesign_pass4: 0.31
redesign_ub95: 0.64
redesign_gpuh: 64
attack_basis: LITERATURE-ONLY
demonstrated_ref: KernelAgent backbone unspecified 2026; CudaForge OpenAI-o3 2025
gap_to_attack: all-in reusable library transfer to reset end-to-end graph research
subfield_sota_ref: CUDA Agent compiled-baseline faster rates Dai 2026
anchored_single: 0.49
anchored_bo4: 0.59
anchored_pass4: 0.45
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
