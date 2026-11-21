# C038 — Make decoding batch-invariant without widening the whole model — saturation screen
## 1. What the grader actually rewards
The same token inputs must produce outputs consistent with the disclosed arithmetic contract across the tested batch arrangements, and only that actual execution contributes serving throughput. Selective recomputation is charged, so correctness from an unrelated slow replay cannot certify a fast run. ESTIMATED R≈0 is the independently committed invariant-serving floor; ESTIMATED R≈1 requires an attainable faster invariant implementation, with reference ESTIMATED R=0.60 and serialized execution provisionally ESTIMATED R=0.00. The forecast is conditional on a real fresh-workload gap above that floor, and cannot assign positive reward to the identical baseline simply for enabling its own invariant mode.
## 2. Strongest lawful combined attack
Transplant the compatible deterministic kernel path from a mature backend, then optimize only the remaining measured bottlenecks. [vLLM's batch-invariance feature](https://docs.vllm.ai/en/v0.31.0/features/batch_invariance/) explicitly changes inference operations to remove batch dependence. Its [kernel implementation documentation](https://docs.vllm.ai/en/latest/api/vllm/model_executor/determinism/batch_invariant/) describes fixed-order accumulation, giving a concrete alternative to globally widening arithmetic or running requests separately.

Preserve fixed reduction trees, operation shapes and random streams for decision-sensitive paths; bucket batches without changing per-token reduction order. Use a checked fallback where the disclosed arithmetic contract differs from the backend's convention. Profile stable GEMMs, normalization, attention and collectives independently, and tune launch geometry within the invariant family. Near-tie logit recomputation helps only if the upstream error can be bounded; otherwise recompute the causally relevant path rather than pretending the final softmax fixes earlier drift.

ESTIMATED single-run R=0.87, range ESTIMATED 0.64–0.96; ESTIMATED best-of-4=0.92; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED upper-95% projection=0.99. This scale assumes the native gap is primarily between reliable serialized inference and efficient batch-invariant kernels. If that public path already belongs in the floor, the card must show a new substantial native gap beyond it before these normalized numbers mean anything. The residual is compatibility with an unusually specific arithmetic contract and throughput lost to invariant reductions. Both may constrain the author almost as strongly as the attacker.
## 3. Other routes
The single strongest recipe is enabling and correctly integrating the existing batch-invariant backend: ESTIMATED R=0.79, range ESTIMATED 0.53–0.93. A feature flag may be sufficient; code length is irrelevant to its legitimacy.

A deterministic-kernel configuration sweep across tile sizes, batch buckets and attention split policies reaches ESTIMATED R=0.83, range ESTIMATED 0.58–0.95. The researcher can exhaust a compact compatibility grid cheaply. A conservative selective replay policy scores ESTIMATED R=0.57, range ESTIMATED 0.31–0.79, but only when its uncertainty test is sound under the declared near-tie distribution; unsupported sensitivity heuristics receive no assumed correctness bonus.
## 4. What would lower lawful saturation
Begin after a fully tuned batch-invariant backend and require a distinct, attainable execution improvement under a published arithmetic contract that standard paths cannot express efficiently. Include interacting parallel layouts and shape transitions with a faithful development proxy. ESTIMATED attack R could fall to 0.52–0.66, costing ESTIMATED four kernel-engineer weeks and ESTIMATED 64 H100 GPU-h to establish reserve and numerical truth. Hardening the token oracle or increasing near-tie density alone tests correctness more severely without creating an algorithmic frontier.
## 5. Decisive-check GPU-h re-estimate
Old card estimate: ESTIMATED 8 GPU-h. New ESTIMATED 16 H100 GPU-h uses an ESTIMATED 7B frozen subject, ESTIMATED four backend arms, ESTIMATED three input/batching blocks and ESTIMATED 0.75 H100-hour each: ESTIMATED 4×3×0.75=9. Reserve ESTIMATED 4 GPU-h for contract-reference outputs and ESTIMATED 3 GPU-h for warmup and repeated timed-path parity. No training or weight adaptation is involved. The original allowance is reasonable for finding one inconsistent batch and too low for proving that a public deterministic replacement leaves throughput reserve.
## 6. Duplicate check
05A: MODERATE; its read source already requires exact outputs under mixed serving arrangements, but an explicit invariant arithmetic contract is narrower than generic session correctness. 04B: WEAK after inspecting its precision-policy and learning-utility interface, which permits approximation and correction rather than requiring invariant inference arithmetic. The primary overlap is exact inference execution, not recovery learning.
## 7. Verdict
CUT, with ESTIMATED best-of-four excess 0.32 and single-run excess 0.17. The existence of a documented batch-invariant runtime makes this a particularly direct transplant-and-tune saturation risk.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete invariant-runtime substitutions). Grader noise UNMEASURED (planned: repeated fixed inputs over batch permutations). Score ladder UNMEASURED (planned: serialized, stock invariant, tuned invariant and stronger arithmetic-compatible kernels).
## Screen record
id: C038
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.87
attack_single_range: 0.64-0.96
bo4_est: 0.92
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 8
gpuh_new_est: 16
duplicate_of: 05A MODERATE
kill_reason: documented batch-invariant backend supplies a direct replacement
souping_flag: no
