# C080: Recover address-generation speed without changing integer semantics — independent adversarial review

**Verdict: CUT.** Guarded specialization and exact modular fallback are a standard constructive response to the very overflow issue identified by the card. The proposal provides no concrete address family on which existing range reasoning plus kernel rewriting leaves a research-sized gap. Preserving wrapping inputs is necessary correctness, not evidence that a complete lawful compiler recipe will resist the target researcher.

Source file: `/workspace/task_ideation_v4_creative/cards/C080.md`.

This review compiled or executed nothing. Native timings, ML outputs, rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; planned measurements require the exact compiler pins, input domains and end-to-end graph harness. Estimated rewards assume a useful-speedup mapping that the card has not supplied. Mentioned regression names are proposed, not existing task files.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Guard once, specialize often | Derive bounds from legal shapes and strides at launch; select a proven nonwrapping kernel when safe and retain the original modular implementation otherwise. | ESTIMATED 0.70–0.94 | No; the card permits bounds and demands wrap preservation, both satisfied here. | Charge guard and fallback costs and compare against this complete baseline across real graph shapes. | ESTIMATED 0.70–0.94 | If most useful work is statically bounded, the fallback has negligible aggregate cost. |
| Explicit modular recurrence | Keep offset arithmetic in its original bit width, factor repeated modular operations where valid, and sign-extend at exactly the original pointer boundary; validate candidate rewrites with bit-vector reasoning. | ESTIMATED 0.62–0.90 | No; this preserves the declared behavior rather than assuming overflow away. | Add a competent modular rewrite family alongside widening; inspect actual machine code and outputs. | ESTIMATED 0.62–0.90 | Non-affine expressions can resist analysis, but the card specifies no such unavoidable workload. |
| Inflate address-speed impact | Optimize a synthetic address microbenchmark or instruction count while leaving full ML graph latency unchanged; alternatively exploit a cold baseline so compilation dominates the reported graph. | ESTIMATED 0.58–0.93 | Complete-graph timing blocks the first route in principle, but its interval and warmup are missing. | Root timing from equivalent input readiness through synchronized final output; matched compilation policy and native speedup controls. | ESTIMATED 0.00–0.19 | Address generation may simply be too small a bottleneck to supply S1 reserve. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read private address programs from compiler subprocess descriptors or shared caches; replace reference object files, LLVM libraries or the comparison process. | ESTIMATED 0.91–1.00 | The card gives no compiler-worker security boundary. | Separate untrusted compilation from root truth, protect immutable toolchain assets and reject collection races; proposed `test_compiler_private_asset_access`. | ESTIMATED 0.00 | Compiler plugins and dynamic library search paths can silently import candidate code into the parent. |
| Interface or encoded-state smuggling | Embed precomputed hidden outputs in kernel literals or cache blobs; decode lookup tables under the guise of address constants and emit them without ML computation. | ESTIMATED 0.84–1.00 | No source/constant/cache limits or input provenance checks are defined. | Cap auxiliary payloads, use fresh tensor values, authenticate code/input receipts and validate executed computation; allow legitimate constant folding. | ESTIMATED 0.00 | A small lawful specialization table over public shapes must remain legal. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Forge comparison stdout, abort wrapping kernels so they are marked unsupported, or hash-match exact positive address fixtures while compiling unsafe code elsewhere. | ESTIMATED 0.87–1.00 | Declared valid wrapping positives oppose rejection, but failure handling is unspecified. | Parent-owned output comparison, mandatory wrap slots and independently implemented equivalent-positive programs; no candidate unsupported status may shrink obligations. | ESTIMATED 0.00 | Finite positive fixtures alone cannot establish universal integer equivalence. |
| Timing/check-decoupling/branch laundering | Run precise fallback only under checks, dispatch unsafe fast kernels under timing, leave warm device code from another branch or replace binaries after validation. | ESTIMATED 0.79–1.00 | No single-execution correctness/timing protocol appears. | Validate captured outputs from the timed graph, freeze binary/launch metadata, clean all descendants and include guarded-path selection in receipts. | ESTIMATED 0.00 | Asynchronous writes and insufficient synchronization can defeat superficial output hashes. |
| Dev-hidden leakage/cue inference | Match issue kernels or compiler-generated expression spellings; use filenames and bit-width distributions to decide which private tests exercise wrapping. | ESTIMATED 0.62–0.91 | Private expressions are promised without independent provenance or crossed encodings. | Independently author equivalent expressions, cross wrap/nonwrap labels with syntax, and run source-recognition and bounds-only selectors. | ESTIMATED 0.24–0.58 | Recognizing legal semantic bounds is intended capability, even if the resulting solver is universal. |
| Adaptive aggregate oracle | Submit different guard cutoffs and rewrite groups, infer which expression families dominate speed from aggregate dev gains, and shard queries across candidate compilers. | ESTIMATED 0.59–0.85 | No feedback budget or scalar precision is specified. | Global query charging and fresh protected expression/graph blocks; include full-cap legal autotuning in the floor. | ESTIMATED 0.36–0.68 | Scalar optimization can lawfully discover robust guard thresholds without understanding a preferred proof chain. |
| Slice abandonment/denominator optimization | Optimize bounded cases, timeout costly wrap cases or reject negative strides; rely on geometric means computed only over completed graphs. | ESTIMATED 0.65–0.95 | All accepted inputs must preserve semantics, but the accepted-input manifest is absent. | Fix valid domains and complete graph/seed denominators before submission; keep failed wrap work in score and separate ordinary local failure from global semantic invalidity. | ESTIMATED 0.18–0.51 | Rare wrap workloads may carry too little weight even when they are never dropped. |
| Strongest lawful combined recipe | Combine range/induction analysis, launch guards, selective widening, exact-width modular rewrites, translation validation and full-graph autotuning with the original wrap path as fallback. | ESTIMATED 0.81 (ESTIMATED 0.59–0.96) | The prescribed semantics permit every ingredient. | Measure against the author method with identical valid domains, launch overhead and correctness enforcement; never disallow safe specialization. | ESTIMATED 0.81 (ESTIMATED 0.59–0.96) | The published regression may reduce to a small reusable compiler/kernel patch family. |

## Published recipe shortcut — web checked

- [Triton issue: SLSR stops strength-reducing Triton's GEPs](https://github.com/triton-lang/triton/issues/11750): opened issue text identifies the signed-extension mismatch, loss of overflow flags, and the difference between intentional wrapping and poison-producing assumptions. Its discussion explicitly points to kernel-level repair.
- [LLVM ScalarEvolution class reference](https://llvm.org/doxygen/classllvm_1_1ScalarEvolution.html): official APIs provide range and induction reasoning relevant to proving safe offset arithmetic.
- [Alive2: Bounded Translation Validation for LLVM](https://users.cs.utah.edu/~regehr/alive2-pldi21.pdf): the primary paper describes SMT-backed bounded validation; its stated loop limitations prevent treating it as a complete proof for arbitrary kernels.
- [LLVM Language Reference Manual](https://llvm.org/docs/LangRef.html): the opened official reference is the semantic authority to pin for integer operations and overflow flags; no local compiler revision was checked against it.

Verification reached the linked issue body, official documentation and a primary-paper search excerpt. No timing, assembly comparison or validator run was performed. The sources establish enough machinery for the **ESTIMATED 0.81 (ESTIMATED 0.59–0.96)** lawful composite, not a measured C080 result. I use no instruction-count or speed figure from the issue as a task measurement.

A safe implementation must distinguish widening before arithmetic from sign-extending a wrapped result. Blind widening can change results just as blind no-wrap annotations can. The adversarial recipe therefore uses a proof/guard where widening is equivalent, and exact-width operations elsewhere. Modular factoring must also respect the original cast and GEP boundaries. These caveats are routine obligations for a competent baseline; they are not grounds to exclude it.

## Saturation against the hypothetical 10T researcher / 12h

The target can read the linked regression, enumerate candidate affine rewrites, synthesize overflow boundary cases and use graph shape metadata to select a specialization. That is a stronger threat than the straw-man blanket overflow flag. Paper recall gives both the failure mechanism and available analyses, while full-budget parallel search can tune a modest collection of generated kernel variants.

My stress forecast is **ESTIMATED single-run maximum 0.93 relative to >0.70**, **ESTIMATED oracle best-of-4 mean 0.89 relative to >0.60**, **ESTIMATED pass@4 0.96 relative to >0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.99 relative to ≥0.75**. Each is above its applicable supplied kill line. These are independent planning judgments, not statistics computed from unobserved samples; no target researcher, attempt law or stronger-tier scaling curve has been measured. The argument for high saturation is constructive reuse of a generic semantic transform, not an asserted existing benchmark score.

S1 is unsupported because restoring the old efficient code may already approach the constrained optimum. If address arithmetic is a minor share of graph time, the physical speed reserve may instead be too small to support the required reference and stronger control. S7 must therefore use a measured achievable graph-speed ceiling rather than an ideal zero-address-cost endpoint. Both ceiling gates remain empirical HOLD until actual controls exist; the forecast is a reason to CUT the current difficulty claim, not a claim those experiments ran.

For any successor, separate compile time, steady graph execution, researcher reasoning and autotuning resources. Budget sweeps need independent restarts over authored expression families; seed changes in public issue kernels are insufficient freshness. Repeated attempts must include failures, and dev-selected artifacts must be distinguished from retrospective oracle choices. Grader noise and host/JIT ranking stability are UNMEASURED, planned through repeated fresh-container grades of frozen binaries. An interval touching a line would remain HOLD even if its point looked safe.

## Revised estimate versus the source card

The designer gives **ESTIMATED 0.52** to widening, bounds and specialization, while I assign **ESTIMATED 0.81 (ESTIMATED 0.59–0.96)** to the completed route. The missing step in the lower estimate is not a new compiler discovery: runtime guards allow uncertain cases to retain exact original behavior while the common proven subset gets fast code. The source's mention of graph-level shape information actually strengthens that strategy when shape metadata is legal and dev exposes equivalent bounds access.

There could be pathological non-affine address programs where guarded reasoning is expensive and few paths specialize. The card provides none and does not show that they are both realistic ML bottlenecks and learnably optimizable. I cannot turn that possibility into resistance. The combined-recipe calibration packets reinforce the need to test a whole legal stack; they supply no default reward for this compiler task.

## Boilerplate and missing build content

Source allocation is **ESTIMATED 20–30%** general task framing and **ESTIMATED 70–80%** specific overflow/compiler content. This is not mostly boilerplate. However, all accepted-input integer domains, signedness, pointer provenance, stride constraints, width conversions, valid wrap destinations and out-of-bounds semantics still need definition. Intentional index wrap must be separated from invalid memory access; otherwise the grader may demand preservation of undefined behavior or mistake legitimate wrap for an illegal input.

The deliverable also lacks pinned LLVM/Triton builds, the editable compiler versus kernel boundary, graph inventory, correctness reference, numeric tensor tolerances, compilation accounting, caching rules, warmup policy and speed-to-reward anchors. Existing issue assembly is not a full-graph speed measurement. A builder would have to invent the principal research distribution, making any precise score currently nonidentifiable.

## Duplicate check

Checked v3 05B optimizes exact distributed training graphs and resumable state, sharing the same-work validation concern. C080 narrows the intervention to address arithmetic and overflow semantics; that difference prevents calling it a duplicate on the inspected evidence. Other catalog and creative cards were not searched for this task, so no broader uniqueness claim is made. No duplicate id is recorded.

## Verdict, required fixes and cheapest decisive check

**CUT** for absence of a defensible residual after standard guarded rewriting. A future proposal would need concrete realistic address families, a sound semantic reference and native end-to-end reserve after the full composite. Hiding public bounds, banning runtime guards or requiring a specific proof narrative would not rescue the research claim.

Cheapest decisive work is a CPU semantic audit of the candidate expression grammar: manually derive guarded rewrites and exact fallback for representative wrap/nonwrap pairs, then determine whether any specified family defeats them. **ESTIMATED 0 H100-hours**. This session performs reasoning only; it does not run a compiler or newly authored test program. GPU benchmarking becomes meaningful only after the graph, binaries and domain contract exist, and must charge the complete executed graph rather than compile-only instruction counts.

R2 requires later live boundary attacks against compiler workers and actual `tests/test_anticheat.py` regressions for poisoned libraries, encoded output tables, spoofed comparison markers, skipped valid wraps and binary swaps. Delivery needs a local OCI lifecycle, trusted driver paths, preserved timeout slots, independently correct positive implementations, protected dev gold, no network/credentials and reproducible hydrated archives. These security requirements do not lower the lawful recipe forecast. No model training or paid experiment was authorized or executed here.

## Verdict record
id: C080
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.81 (0.59–0.96)
combined_recipe_attack: ESTIMATED 0.81 (0.59–0.96)
best_of_4: ESTIMATED 0.89
pass_at_4: ESTIMATED 0.96
single_run_max: ESTIMATED 0.93
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: new residual beyond guarded modular rewrite; precise valid-input semantics; measured graph reserve
main_kill_reason: proof-guided fast path with exact fallback is a complete standard route
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 4
