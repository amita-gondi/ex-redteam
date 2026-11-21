# C078 — Rotary KV appends that remain correct after repeated reuse — saturation screen
## 1. What the grader actually rewards
Credit comes from complete append/read service throughput with delayed decoded outputs matching immutable reference keys and with copying charged. A damaged write that only fails for a later owner loses its affected completion credit. On the provisional scale, ESTIMATED R≈0 is the repaired competent service floor, the no-op is ESTIMATED R=0.00, the intended reference is ESTIMATED R=0.60, and R≈1 represents an attainable exact lifecycle implementation rather than merely passing a rotary test.
## 2. Strongest lawful combined attack
The actual defect is unusually actionable: [the verified upstream report](https://github.com/Dao-AILab/flash-attention/issues/3014) identifies stores extending past the logical head dimension for certain padded non-interleaved rotary layouts. Repair the store predicates, compare all neighboring cache entries after writes, and retain the normal fast path when ownership is exclusive. Combine this with reference-counted pages and copy-on-write only for shared writable ranges, using [vLLM prefix caching](https://docs.vllm.ai/en/stable/features/automatic_prefix_caching/) as a mature reuse baseline. The prefix-cache documentation verifies reuse capability; selective ownership bookkeeping is the proposed implementation, not a claimed upstream fix for this particular defect.

A strong agent need not snapshot every cache to solve this. It can separate a local out-of-bounds store from genuine aliasing, validate the corrected append, and dispatch by publicly available dimension/layout metadata. There is no training problem or hidden semantic inference in that route. ESTIMATED single-run R=0.83, range 0.68–0.95; ESTIMATED best-of-4=0.90; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% bound=0.98. Remaining loss would arise from partial-page sharing, ownership transitions and launch fragmentation. The card does not demonstrate that those costs remain substantial after a bounded-store kernel removes corruption without copying.
## 3. Other routes
- Correct the rotary write boundary and otherwise preserve the stock cache engine: ESTIMATED R=0.77, range 0.59–0.92. This is stronger than the author's universal conservative-copy baseline because it addresses the reported memory write directly.
- Sweep masked-vector store widths, append block sizes and private-copy thresholds on full reuse traces: ESTIMATED R=0.81, range 0.62–0.94. Use development lifecycle completion time for selection so a fast first append cannot conceal future repair cost.
- Pre-rotate into a temporary exact buffer before a checked append is ESTIMATED R=0.48, range 0.27–0.70. Extra traffic lowers useful service capacity but gives a straightforward legal fallback.
## 4. What would lower lawful saturation
Require a disclosed transactional interface with genuinely concurrent shared-page updates and a tight total-byte budget, backed by private ownership graphs that force different legal commit orders. Include equivalent structures during development and floor the repaired selective-copy engine. This could move the combined route to ESTIMATED R=0.45–0.61 if a stronger atomic commit design exists. ESTIMATED incremental cost is one engineer-week and 18 H100 GPU-h to construct and replay races; merely stretching request lifetimes would not change the local bounds repair. The redesign must retain feasible exact service rather than make races nondeterministically unwinnable.
## 5. Decisive-check GPU-h re-estimate
The card's old allowance is ESTIMATED 6 GPU-h. New ESTIMATED cost is 14 H100 GPU-h: ESTIMATED 4 implementations × 3 trace seeds × 0.5 hours = 6 GPU-h, plus ESTIMATED 4 GPU-h for delayed decode verification and ESTIMATED 4 GPU-h for compile, allocation and stress replay overhead. Use fixed tensors and an ESTIMATED 1B frozen decoder, with no optimizer or training phase. The earlier number is plausible for reproducing a store error, but not for comparing selective copying against a fully repaired service and checking later owners. Full researcher-tail studies remain outside this pilot.
## 6. Duplicate check
v3 06A — WEAK: its opened source concerns lossy compressed attention state and quality recovery, whereas this intervention preserves mutable state exactly. v3 05A — MODERATE: the inspected exact-serving task includes session state and reuse semantics, although it grades broader service capacity rather than a rotary append transaction specifically. Neither establishes the same narrow intervention and target together.
## 7. Verdict
CUT, with ESTIMATED single-run reward 0.13 above the single>0.70 boundary. The ESTIMATED best-of-4 excess is 0.30. This is primarily a public masked-store repair with readily available lifecycle engineering, and the conservative snapshot attack understates the strongest lawful route.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent repaired-store plus selective-copy submissions); grader noise UNMEASURED (planned: fixed-trace repeats including ownership transfers); score ladder UNMEASURED (planned: corrupt stock, bounded stores, temporary-buffer append and transactional control).
## Screen record
id: C078
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.83
attack_single_range: 0.68-0.95
bo4_est: 0.90
pass4_est: 0.99
ub95_est: 0.98
gpuh_old: 6
gpuh_new_est: 14
duplicate_of: v3 06A WEAK; v3 05A MODERATE
kill_reason: bounded rotary stores remove corruption without blanket copies
souping_flag: no
