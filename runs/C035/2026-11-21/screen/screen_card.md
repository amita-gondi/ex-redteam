# C035 — Keep inference fast through online adapter admission — saturation screen
## 1. What the grader actually rewards
Service utility counts completed requests using their exact requested adapter version, with transfer, preparation and real adapter occupancy charged. A cache hit on stale weights is a correctness failure, even if the answer happens to look reasonable. ESTIMATED R≈0 denotes the precommitted competent serving floor and ESTIMATED R≈1 a stronger attainable admission policy; synchronous loading is provisionally ESTIMATED R=0.00 and the author's reference ESTIMATED R=0.60. Forecasted gain concerns a stronger deployment-tuned replacement on fresh arrivals, not replaying the exact calibration artifact for positive reward; if mature admission already occupies the endpoint, there is no usable native task gap.
## 2. Strongest lawful combined attack
Replace the inherited loader with immutable version handles, reference-counted residency, asynchronous transfer and a production multi-adapter batch path. [S-LoRA](https://arxiv.org/abs/2311.03285) and [Punica](https://arxiv.org/abs/2310.18547) establish efficient concurrent adapter execution. [vLLM's LoRA documentation](https://docs.vllm.ai/en/stable/features/lora/) explicitly supports runtime loading and unloading, so an immutable inventory is not a necessary assumption of mature implementations.

Use version-specific cache identities and publish a newly loaded version atomically; in-flight requests retain their original handles. Reserve staging memory, overlap copies with independent requests, reuse graph structures through stable storage slots, and evict according to recency, frequency and loading cost. Tune transfer concurrency, graph buckets and residency jointly. The stack performs ordinary separate adapter execution; no weight averaging or combined-model construction is part of this route.

ESTIMATED single-run R=0.84, range ESTIMATED 0.61–0.95; ESTIMATED best-of-4=0.90; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% bound=0.99. The provisional ladder assigns most gain to eliminating synchronous stalls and stale-version hazards, then additional gain to better memory reuse. Residual costs are unpredictable first demand, unavoidable transfer bandwidth and genuinely novel graph shapes. Those are also lower bounds for the author, so their mere existence cannot support a large normalized research reserve.
## 3. Other routes
Dynamic loading with a conventional LRU and fixed multi-adapter batching reaches ESTIMATED R=0.74, range ESTIMATED 0.48–0.90. It is a complete useful baseline even without a learned popularity model.

A workload sweep over cache fractions, prefetch depth, staging slots and graph buckets yields ESTIMATED R=0.79, range ESTIMATED 0.54–0.93. Because the subject weights remain frozen, short service trials make a broad search realistic. A lawful low-memory synchronous fallback for rare adapters scores ESTIMATED R=0.50, range ESTIMATED 0.26–0.73, and can be combined with the fast popular-adapter path. Rejecting rare adapters is excluded from these estimates because requests remain in the denominator.
## 4. What would lower lawful saturation
Require arrivals to create disclosed representation-dependent graph choices whose compilation and residency compete with serving, and establish native gains beyond a tuned production replacement. Use new dependency structures rather than only new adapter names or arrival seeds. ESTIMATED composite R may fall to 0.55–0.68, with ESTIMATED three systems-author weeks and ESTIMATED 48 H100 GPU-h for graph/arrival calibration. This remains a risky redesign: ordinary admission control and cost-aware caching may still capture the same opportunity. Tighter memory alone can simply lower the common ceiling.
## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 8 GPU-h. New ESTIMATED 16 H100 GPU-h uses an ESTIMATED 7B base model and already trained adapters, ESTIMATED four runtime arms, ESTIMATED three independent arrival/version traces, and ESTIMATED 0.75 hour each: ESTIMATED 4×3×0.75=9 GPU-h. Add ESTIMATED 3 GPU-h for separately verified adapter-version outputs and ESTIMATED 4 GPU-h for cold preparation and memory-pressure repetition. Adapter training is unnecessary for this systems falsification provided genuine compatible arrivals already exist; generating those assets would be separate. The original budget nearly covers one pass but misses independent correctness and first-use accounting.
## 6. Duplicate check
05A: MODERATE. Its source explicitly includes adapter switching, memory contention and exact useful serving capacity, but starts from supplied adapter artifacts rather than a defined fresh-admission interface. Catalog T08: WEAK; the read packet updates parameters through changing contracts rather than serving immutable learned versions. The online arrival boundary adds something concrete, so I do not assert STRONG duplication.
## 7. Verdict
CUT for saturation, with ESTIMATED best-of-four excess 0.30. The ESTIMATED single-run excess is 0.14. Public runtime admission and concurrent adapter execution already supply the card's main proposed gains.
## 8. Measurement status
Rollouts UNMEASURED (planned: real fresh-adapter arrival traces). Grader noise UNMEASURED (planned: repeated cold loading and exact-version replay). Score ladder UNMEASURED (planned: synchronous loader, dynamic runtime, tuned residency and attainable admission control).
## Screen record
id: C035
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.84
attack_single_range: 0.61-0.95
bo4_est: 0.90
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 8
gpuh_new_est: 16
duplicate_of: 05A MODERATE; T08 WEAK
kill_reason: mature dynamic multi-adapter service covers main intervention
souping_flag: no
