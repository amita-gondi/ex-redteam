# C126 — A reusable kernel tool library judged by the next research project — saturation screen
## 1. What the grader actually rewards
The library must help a reset researcher deliver correct end-to-end speedups on new ML graphs, including the cost of constructing, validating and tuning its reusable entries. A fast primitive is worthless when its actual call site violates a shape, precision or semantic precondition. ESTIMATED R≈0 is a mature guarded-library baseline and ESTIMATED R≈1 is attainable stronger graph performance at the same complete research cost. The copied-snippet starter and intended ESTIMATED reference near 0.60 have no measured native runtime anchors.
## 2. Strongest lawful combined attack
Use a mature kernel portfolio with explicit contracts, rather than infer validity from one successful launch configuration. [CUTLASS](https://docs.nvidia.com/cutlass/latest/index.html) verifies established template/DSL abstractions for high-performance matrix operations, and its [profiler](https://docs.nvidia.com/cutlass/latest/media/docs/cpp/profiler.html) supplies an existing search and verification component. [Triton autotuning](https://triton-lang.org/main/python-api/generated/triton.autotune.html) verifies keyed configuration search with mechanisms for restoring mutated inputs during trials. Those details matter when reusing kernels whose tuning changes state.

Annotate each entry with supported strides, alignment, aliasing, reduction semantics, accumulation precision and admissible value regimes. [PyTorch's guard documentation](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/compile/programming_model.reducing_guard_overhead.html) verifies conditional reuse based on captured assumptions. Add independent randomized and adversarial-value checks at the new call site, fall back when preconditions fail, and retune only the performance-sensitive remaining dimensions. The reset agent can compose verified primitives and profile the entire graph, discarding locally faster substitutions that lose globally. Construction and failed tuning are charged; no hidden task identity is needed in dispatch.

ESTIMATED single-run R=0.80, range 0.59–0.93; ESTIMATED oracle best-of-4=0.88; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% score=0.97. Numerical preconditions depending on downstream sensitivity can remain difficult, and graph-wide fusion may require new abstractions. However, the card's named failure—carrying hidden shape and precision assumptions—is directly addressed by guarded contracts and call-site differential tests. Fresh shape relationships alone do not establish that the mature portfolio lacks the necessary abstraction.
## 3. Other routes
A guarded CUTLASS/Triton portfolio with safe fallback is the strongest single standard recipe. ESTIMATED R=0.67, range 0.44–0.85. It trades some specialization for reliable transfer and can avoid much downstream debugging.

Autotune dispatch and fusion choices across development graphs, selecting by complete warm runtime after exactness checks. ESTIMATED R=0.76, range 0.53–0.91. Cache keys must cover actual semantic assumptions, and every trial remains paid. A lawful alternative avoids the custom library and asks the existing compiler to optimize each new graph directly: ESTIMATED R=0.71, range 0.46–0.89. If compilation and validation are cheap relative to library construction, reusable extraction may not improve the full scientific budget at all.
## 4. What would lower lawful saturation
Hold out a graph interaction that requires a new reusable communication or numerical abstraction, with representative development evidence and a demonstrated benefit across more than one graph. Keep existing guarded libraries fully legal and measure the additional gain over direct compilation. ESTIMATED score reduction is 0.15–0.23, to approximately 0.57–0.65, still near repeated-search kills. ESTIMATED preparation is 12–22 person-days and 120 H100-h for graph-family and precondition validation. Adding uncommon sizes without a changed abstraction mostly gives autotuners more cases, not deeper research.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 16 GPU-h. New ESTIMATED cost is 48 H100 GPU-h: 4 library strategies × 2 independent reset campaigns × 3 H100-h testing fixed 1B–4B graph workloads = 24; library extraction/calibration benchmarks = 8; independent graph correctness and repeated warm timings = 8; fixed 4B researcher inference = 8. ESTIMATED total 24+8+8+8=48. No subject-model training is required for this microbenchmark-oriented pilot. The old estimate was closer than on training cards, but omitted repeated downstream campaigns and all-in construction cost. Larger distributed graphs would need a separately priced topology study.
## 6. Duplicate check
05B, MODERATE: the opened source optimizes one exact training graph family and resumable state, whereas C126 submits a reusable inventory consumed by reset researchers on later graphs. T03, WEAK: it supplies a transferable researcher controller but not kernel abstractions or a graph-speed target. T21, WEAK: resource-aware deployment is shared context, but its intervention changes model compression and recovery rather than reusable kernels.
## 7. Verdict
CUT. ESTIMATED single-run score exceeds its limit by 0.10 and best-of-4 by 0.28. Mature templates, guarded reuse and complete-graph validation form a direct solution to the currently specified library-transfer bottleneck.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent library construction and reset graph-optimization campaigns). Grader noise UNMEASURED (planned: repeated matched-host warm graph timings and researcher restarts). Score ladder UNMEASURED (planned: copied snippets, guarded portfolio, autotuned portfolio, direct compiler, reference and stronger feasible reusable library).
## Screen record
id: C126
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.80
attack_single_range: 0.59-0.93
bo4_est: 0.88
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 16
gpuh_new_est: 48
duplicate_of: 05B MODERATE; T03 WEAK; T21 WEAK
kill_reason: guarded mature kernel portfolios cover stated reuse assumptions
souping_flag: no
