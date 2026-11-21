# C080 — Recover address-generation speed without changing integer semantics — saturation screen
## 1. What the grader actually rewards
The grader values faster complete ML graphs while retaining the declared behavior of both bounded and intentionally wrapping address arithmetic. R≈0 is the semantics-preserving competent compiler floor, whereas R≈1 denotes an independently demonstrated fast implementation that accepts every legal input. The unmodified regression is ESTIMATED R=0.00 and the desired reference is ESTIMATED R=0.60; the missing native timing anchors make this a conditional reward forecast, not a claim that instruction-count recovery equals normalized gain.
## 2. Strongest lawful combined attack
Use the [verified regression report](https://github.com/triton-lang/triton/issues/11750) to locate lost strength reduction, but do not apply global nonwrapping flags. Combine [LLVM ScalarEvolution](https://llvm.org/doxygen/ScalarEvolution_8cpp_source.html) range information with [Z3 bit-vector reasoning](https://microsoft.github.io/z3guide/docs/theories/Bitvectors/) to prove safe local transformations. Generate a guarded fast specialization when runtime shapes establish a nonoverflow range, retain exact modular arithmetic otherwise, and profile both paths on complete graphs. Widening intermediate arithmetic is permitted only after proving equivalence to the original wrap semantics; widening alone is not a general repair.

The strongest route amortizes proof and compilation across repeated shapes, propagates bounds from graph inputs, and searches alternative pointer factorizations under exact equivalence checks. It can handle ordinary affine kernels very effectively. Its unresolved part is finding profitable cross-operation bounds and preserving speed when legal wraps are frequent enough that the fallback dominates. ESTIMATED single-run R=0.48, range 0.28–0.65; ESTIMATED best-of-4=0.58; ESTIMATED pass@4 at R≥0.60=0.32; ESTIMATED projected upper-95% bound=0.73. These uncertainty quantities are desk estimates. They assume the workload genuinely weights wrap-sensitive interactions; a bank dominated by ordinary affine offsets could instead saturate above the single-run cutoff.
## 3. Other routes
- Stock range analysis plus local kernel rewrites is ESTIMATED R=0.38, range 0.19–0.58. This is the strongest isolated conventional recipe because the source defect has an explicit semantic explanation and a kernel-side repair route.
- Enumerate width, factoring, tile and guarded-specialization alternatives, rejecting inequivalent candidates with a bit-vector checker: ESTIMATED R=0.46, range 0.25–0.64. Compilation and proof time consume the same research allowance; unrestricted brute-force expression search is not free.
- Specialize only on observed development dimensions and use a correct generic fallback elsewhere: ESTIMATED R=0.31, range 0.12–0.55. This remains lawful but should transfer poorly when fresh legal bounds change which factoring is safe.
## 4. What would lower lawful saturation
Require private graph families with correlated shape bounds and valid wrapping paths that contribute material useful work, then publish a predictive development generator for those mechanisms. Freeze the combined guarded-analysis compiler in the floor and meter specialization creation as well as execution. The required change is specifically this mechanism-balanced generator and accounting contract; adding random expressions is insufficient. ESTIMATED attack would move to R=0.39–0.51, with ESTIMATED best-of-4 near 0.52. ESTIMATED implementation effort is two compiler engineer-weeks and ESTIMATED extra calibration is 24 H100 GPU-h. If no attainable control beats that floor materially, retire the task rather than shrinking the reward denominator.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 8 GPU-h. New ESTIMATED total: 20 H100 GPU-h, using fixed kernels and an ESTIMATED 1B frozen training graph without convergence training. Allocate ESTIMATED 4 transformation strategies × 3 program-bank seeds × 1 H100-hour = 12 GPU-h; add ESTIMATED 4 GPU-h for exact graph-output replay and ESTIMATED 4 GPU-h for warmup and timed repetitions. Proof solving is CPU work, estimated separately as several workstation-days, not relabeled GPU time. The original allowance is reasonable for a reproduction but too small to compare full semantics-preserving strategies across mechanism families.
## 6. Duplicate check
v3 05B — MODERATE. Its opened source permits complete graph optimization while preserving updates and resumable state; C080 instead focuses the artifact on integer-address compilation and its accepted-input semantics. Exact training throughput overlaps, but neither checkpoint state nor distributed scheduling is the new causal bottleneck.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 is only 0.02 below its cutoff and the ESTIMATED upper bound is only 0.02 below its boundary. Require the mechanism-balanced wrapping/shape generator, identical development semantics, and fully charged guarded specialization described above before further promotion. Present uncertainty cannot support PASS-SCREEN.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent proof-guided compiler attempts); grader noise UNMEASURED (planned: repeated exact graph timings on fixed compiled artifacts); score ladder UNMEASURED (planned: regressed compiler, legal local repair, guarded solver and stronger graph-bound control).
## Screen record
id: C080
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.48
attack_single_range: 0.28-0.65
bo4_est: 0.58
pass4_est: 0.32
ub95_est: 0.73
gpuh_old: 8
gpuh_new_est: 20
duplicate_of: v3 05B MODERATE
kill_reason: narrow best of four and projection margins require balanced wrap mechanisms
souping_flag: no
