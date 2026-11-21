# C085 — Diffusion draft lengths under shared verifier contention — saturation screen
## 1. What the grader actually rewards
Reward tracks target-correct, deadline-qualified service completions after charging shared verifier time and the delay each draft imposes on other requests. R≈0 is the strongest ordinary load-aware speculative service, and R≈1 is an attainable coordinated service frontier under the same workload and resource cap. The untouched isolated-cost policy is provisionally ESTIMATED R=0.00, with an intended reference of ESTIMATED R=0.60; local accepted-token yield is not itself the graded quantity.
## 2. Strongest lawful combined attack
Combine the confidence-to-marginal-gain rule in verified [LibraSpec](https://arxiv.org/abs/2608.08721) with the explicit batch-size-to-draft-length dispatch already documented by [vLLM dynamic speculation](https://docs.vllm.ai/en/stable/features/speculative_decoding/dynamic_speculative_decoding/). Maintain an online verifier cost surface indexed by active batch, prefix length and candidate verify length; at each service round allocate the shared verification-token budget to the largest expected accepted-token gains, adjusted for deadline slack. Confidence-based per-request lengths and concurrency-based controls are independently documented in [vLLM Ascend's speculation interface](https://docs.vllm.ai/projects/ascend/en/v0.27.1rc/user_guide/feature_guide/speculative_decoding.html); that source establishes the method family, not H100 implementation compatibility.

A capable agent would profile a bounded cost grid, fit incremental costs from real service rounds, and retune conservatively when the batch changes. It can disable drafting under heavy load and preserve exact verification. ESTIMATED single-run R=0.79, range 0.60–0.92; ESTIMATED oracle best-of-4=0.87; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% bound=0.96. Residual loss arises from rapidly changing joint acceptance patterns and discrete batch packing, but ordinary receding-horizon allocation already responds to the card's main externality. The new stress hypothesis is plausible; the claimed absence of a complete recipe is not supported by the available interfaces.
## 3. Other routes
- A batch-size-conditioned draft-length table with exact verification is ESTIMATED R=0.68, range 0.47–0.86. It directly addresses contention without learning a sophisticated model of every request.
- Sweep concurrency bins, verify-token caps, confidence thresholds and deadline-priority weights, selecting on full service replay: ESTIMATED R=0.76, range 0.55–0.91. An online table update can then absorb mild cost drift.
- Short fixed drafts or speculation-off during overload are ESTIMATED R=0.45, range 0.22–0.68. This lawful fallback is especially dangerous if deadline utility mostly rewards avoiding queue blowups rather than exploiting complementary request opportunities.
## 4. What would lower lawful saturation
Floor the complete load-aware controller and use real shared-verifier workloads where correlated acceptance, prefix-cache reuse and deadline slack change the best joint action. Development must expose all these state variables and equivalent contention mechanisms. ESTIMATED combined attack might fall to R=0.46–0.62, with ESTIMATED cost of an engineer-week plus 48 H100 GPU-h to calibrate interaction traces. That remains borderline; merely adding arrivals or raising concurrency is unlikely to help because the verified standard recipe was designed for variable concurrency. A stronger same-budget scheduler must establish meaningful native headroom before changing normalization.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 10 GPU-h. New ESTIMATED total is 60 H100 GPU-h. Assume a frozen ESTIMATED 8B target and 0.5B diffusion drafter, with no training and a one-H100 service envelope. ESTIMATED 5 controllers × 3 workload seeds × 3 hours = 45 GPU-h, plus ESTIMATED 9 GPU-h for exact-sequence verification and ESTIMATED 6 GPU-h for warmup, confidence replay and timing replication. The old budget is adequate for an isolated/shared cost contrast, but insufficient to establish the coordinated-service frontier against mature adaptive controls. Diffusion confidence must be generated or replayed from authorized measured drafts, not invented traces.
## 6. Duplicate check
v3 05A — MODERATE. Its inspected source already allows complete exact serving engines, speculative controls and scheduling across heterogeneous sessions; this card restricts the editable artifact to diffusion draft length and directly accounts for shared verification externalities. The narrower intervention is not enough to assert a strong duplicate solely from the common exact-service objective.
## 7. Verdict
CUT. ESTIMATED single-run reward is 0.09 above its boundary, and ESTIMATED best-of-4 is 0.27 above its line. Known dynamic speculation plus online shared-cost allocation plausibly exhausts the proposed isolated-cost correction within the research budget.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent load-aware diffusion-length controllers); grader noise UNMEASURED (planned: repeated complete arrival-trace service grades); score ladder UNMEASURED (planned: fixed length, LibraSpec, batch-conditioned dispatch and coordinated attainable controller).
## Screen record
id: C085
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.79
attack_single_range: 0.60-0.92
bo4_est: 0.87
pass4_est: 0.98
ub95_est: 0.96
gpuh_old: 10
gpuh_new_est: 60
duplicate_of: v3 05A MODERATE
kill_reason: known dynamic speculation already conditions on shared load
souping_flag: no
