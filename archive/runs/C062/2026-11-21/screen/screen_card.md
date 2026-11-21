# C062 — Prevent persistent NaN poisoning at graph padding transitions — saturation screen
## 1. What the grader actually rewards
Correctness extends through later requests that reuse state touched by padded graph execution; finite immediate logits do not establish safety. Useful throughput counts only exact valid completions over that extended service trace. R≈0 is the repaired competent graph/fallback floor and includes no-op public repairs; R≈1 is the attainable safe graph-execution control, with all performance forecasts and pilot costs here ESTIMATED because the baseline/control gap is UNMEASURED.

A state-safe graph redesign would target ESTIMATED R=0.60 as the author reference, but its capacity margin over guarded writes is UNMEASURED.

## 2. Strongest lawful combined attack
Audit every persistent-state write for active-lane ownership, not just the output logits. Route padded lanes to a dedicated scratch state and guard their stores using the documented semantics of [Triton masked stores](https://triton-lang.org/main/python-api/generated/triton.language.store.html). Use request-generation tags on reused slots, initialize scratch buffers deterministically, and preserve a safe eager path around unsupported transitions. This is structural prevention of contamination, rather than periodically replacing NaNs after damage has spread.

Retain graph capture for common safe shapes and tune the inventory against total state and capture memory. [NVIDIA's CUDA graph guidance](https://docs.nvidia.com/dl-cuda-graph/latest/torch-cuda-graph/best-practices.html) explains stable addresses and asynchronous execution constraints; its [memory discussion](https://docs.nvidia.com/dl-cuda-graph/latest/troubleshooting/memory-issues.html) identifies persistent graph inputs and separate pools as real costs. Those sources support a realistic graph/fallback stack, without proving speed on this proposed recurrent workload. After each poisoned-lane candidate trace, the attack reuses all affected slots and compares continued execution with an independent safe implementation.

ESTIMATED single-run R=0.80, range 0.61–0.92; ESTIMATED best-of-4=0.88; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED upper-95% projection=0.97. These are subjective estimates above fixed calibration controls. The residual is graph-memory pressure and throughput lost at rare transitions, not an unresolved mathematical barrier to safe dummy lanes. If the complete masked-state implementation is already the frozen floor, the card must demonstrate another attainable native reserve before a normalized reward forecast is meaningful.

## 3. Other routes
The published repair followed by conservative eager execution at risky state changes is the strongest single simple recipe: ESTIMATED R=0.68, range 0.46–0.85. It can saturate whenever transition frequency is low enough that safe fallback barely affects complete throughput.

Search over graph sizes, padding strategy, scratch pooling, capture memory and fallback thresholds has ESTIMATED R=0.77, range 0.56–0.91. Every search candidate must survive continued slot reuse. Checking only the trigger batch is a potential grader weakness, but the source card already demands continuation; this forecast assumes that defense is honored.

## 4. What would lower lawful saturation
Demonstrate a realistic graph-inventory frontier where isolated scratch states consume material memory and fallback loses material service capacity. Fresh instances should vary coupled request lifetimes and speculative state commits, with equal development visibility, rather than adding more padding dimensions. ESTIMATED combined reward after such a redesign is 0.53–0.69. ESTIMATED authoring is 7–11 person-days and ESTIMATED 36 H100-h for a first faithful service comparison. A design whose entire gain is the active-lane store guard should be cut after that repair, regardless of how durable the original failure was.

## 5. Decisive-check GPU-h re-estimate
Old card: ESTIMATED 8 GPU-h. New ESTIMATED 36 H100-GPU-h uses an ESTIMATED 8B hybrid/recurrent serving model on an ESTIMATED 2-H100 worker. ESTIMATED 3 arms×3 state-history seeds×1.5 cluster-hours×2 devices gives 27, with ESTIMATED 9 for graph capture, safe-reference continuation and independent repeated timing. Total ESTIMATED 27+9=36. There is no training component. A smaller recurrent fixture may find the bad write cheaply, but it does not determine whether the repaired production-size graph pool has meaningful useful-capacity headroom.

## 6. Duplicate check
06A: WEAK after reading its compressed-state source; both concern persistent inference state, but lossy representation/recovery differs from exact inactive-lane isolation. 05A: MODERATE because it already grades exact serving throughput across coupled state lifetimes, although graph-padding poisoning is not its specified intervention. The near-neighbor note's C030 comparison is internal to the creative set and is not substituted for an indexed prior-task check.

## 7. Verdict
CUT. ESTIMATED single-run reward exceeds the binding limit by 0.10; ESTIMATED best-of-4 exceeds its line by 0.28. Safe scratch isolation, guarded writes and tuned fallback form a standard combined route, and no measured graph-memory tradeoff currently establishes a difficult residual.

## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget safe-state graph implementations on fresh lifetime traces); grader noise UNMEASURED (planned: repeated complete continuations and warmed timing for fixed kernels); score ladder UNMEASURED (planned: repaired eager, narrow fallback, guarded state, tuned graph pool and stronger safe capacity control).

## Screen record
id: C062
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.80
attack_single_range: 0.61-0.92
bo4_est: 0.88
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 8
gpuh_new_est: 36
duplicate_of: 06A WEAK; 05A MODERATE
kill_reason: active-lane write isolation and fallback remove the stated mechanism
souping_flag: no
