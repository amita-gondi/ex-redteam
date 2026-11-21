# C032 — Inference that survives bursty image token expansion — saturation screen
## 1. What the grader actually rewards
The server must finish the original image requests under real peak-device-state limits, with rejected or deferred large images retained in their strata. Useful multimodal completions per total GPU time define the utility, not a predicted crop count or admission rate. ESTIMATED R≈0 means competent safe admission, ESTIMATED R≈1 the attainable same-device completion rate; worst-case reservation is provisionally ESTIMATED R=0.00 and the desired reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Use separate queues for arrival preprocessing, visual encoding and decoder admission. Cheap image metadata supplies an initial reservation, but the scheduler reveals the actual crop workload before committing expensive decoder state. [vLLM's encoder-aware scheduling configuration](https://docs.vllm.ai/en/latest/configuration/engine_args/) distinguishes encoder work and cached encoder capacity; [Sarathi-Serve](https://www.usenix.org/conference/osdi24/presentation/agrawal) establishes chunked-prefill scheduling as a mature way to mix long input work with decodes.

Combine staged admission with a calibrated reserve, bounded visual work in flight, paged decoder state and age-based protection for large requests. Where crop expansion itself requires GPU work, charge it before deciding whether to defer the request and retain the discovered size. Jointly tune queue thresholds, encoding batch size and memory margins, using stratum completion utility rather than average request latency. The strongest route does not need a perfect crop predictor: it can purchase exact cost information incrementally and then schedule known work.

ESTIMATED single-run R=0.73, range ESTIMATED 0.48–0.88; ESTIMATED best-of-4=0.81; ESTIMATED pass@4 at R≥0.60=0.92; ESTIMATED upper-95% projection=0.94. The forecast attributes most reward to avoiding both unsafe over-admission and global maximum-size reservations, with further gain from queue overlap. What remains is costly information revelation, burst-correlated crop expansion and the fairness cost of large jobs. Without a latency or finite-horizon commitment, a scheduler can simply wait for size revelation, making the apparent uncertainty substantially easier than the card suggests.
## 3. Other routes
Metadata-based cost prediction plus conservative margins gives ESTIMATED R=0.53, range ESTIMATED 0.29–0.74. This reproduces the obvious single recipe but can fail on content-dependent splitting.

A production-style staged queue without learned predictions reaches ESTIMATED R=0.65, range ESTIMATED 0.40–0.83. Sweeping its encoder concurrency, decoder token budget and aging threshold improves that to ESTIMATED R=0.69, range ESTIMATED 0.44–0.86. Size specialization remains lawful only if all image strata retain their disclosed weights; dropping difficult images is not included in these scores.
## 4. What would lower lawful saturation
Freeze a real completion-deadline contract and construct content-dependent expansions where learning whether to reveal more size information changes subsequent queue opportunities. Development must expose the same information and tail structure. ESTIMATED attack score could decline to R=0.48–0.60, at ESTIMATED three systems-weeks and ESTIMATED 40 H100 GPU-h of trace calibration. The benchmark also needs an attainable controller that exploits those opportunities; an overloaded arrival process cannot establish reserve. If standard staged queues already match that controller, retire the task rather than restricting legal preprocessing.
## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 8 GPU-h. New ESTIMATED 20 H100 GPU-h assumes an ESTIMATED 7B VLM on one H100, ESTIMATED four admission arms, ESTIMATED three independently composed image traces and ESTIMATED one hour per trace: ESTIMATED 4×3×1=12. Allocate ESTIMATED 4 GPU-h to exact completion/output references and ESTIMATED 4 GPU-h to repeated peak-memory and warmup checks. All arms include actual visual encoding; no crop-count simulator replaces it. The original value misses cross-stratum queue behavior and reference execution, although no training cost is necessary.
## 6. Duplicate check
05A: MODERATE; the read source already optimizes correct serving capacity across shapes, but uncertain visual expansion adds a specific admission-information boundary. Catalog T10: WEAK, after inspecting its acquisition-policy statement; choosing informative crops is different from completing all prescribed crops efficiently. Neither pairing supports STRONG equivalence.
## 7. Verdict
CUT, binding ESTIMATED best-of-four excess 0.21. The ESTIMATED single-run forecast also crosses its cutoff by 0.03. Incremental revelation and existing encoder/decoder scheduling are too effective unless the missing deadline and information-value mechanism are made concrete.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete image traces with retained large-request denominators). Grader noise UNMEASURED (planned: repeated actual encoding and device-memory capture). Score ladder UNMEASURED (planned: maximum reservation, metadata admission, staged queues and stronger controller).
## Screen record
id: C032
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.73
attack_single_range: 0.48-0.88
bo4_est: 0.81
pass4_est: 0.92
ub95_est: 0.94
gpuh_old: 8
gpuh_new_est: 20
duplicate_of: 05A MODERATE; T10 WEAK
kill_reason: staged encoder admission removes unknown-size bottleneck
souping_flag: no
