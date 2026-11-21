# C033 — Inference placement under asymmetric interconnect failures — saturation screen
## 1. What the grader actually rewards
The experiment plan is scored by verified inference output after paying for probes, placement changes and service execution on the chosen routes. Detecting a slow link is not independently valuable if the discovery cost exceeds the service benefit. ESTIMATED R≈0 denotes a competent fixed placement and probing floor, ESTIMATED R≈1 an attainable cost-inclusive placement policy; the proposed reference targets ESTIMATED R=0.60, with no native anchors yet measured.
## 2. Strongest lawful combined attack
Measure directional point-to-point and actual collective performance at workload-relevant message sizes using [NVIDIA nccl-tests](https://github.com/NVIDIA/nccl-tests). Fit an empirical cost model, enumerate feasible tensor/pipeline partitions, and validate the promising placements using real prefill and decode. [AlpaServe](https://arxiv.org/abs/2302.11665) establishes model-parallel serving placement, while [TACCL](https://arxiv.org/abs/2111.04867) supplies topology-aware collective synthesis when the allowed interface includes collective changes. Placement alone can still exploit the measured topology if synthesis is outside scope.

Combine those tools with successive elimination: first use cheap probes to discard clearly bad paths, then spend full serving measurements only on contenders. Retest under representative concurrent traffic and reserve a robust fallback placement. Since the card specifies stable private asymmetric graphs rather than an explicit nonstationary interference law, a broad initial scan is likely cheap relative to the long service window. A frontier agent can also bypass diagnosis by timing every feasible placement when the grid is small.

ESTIMATED single-run R=0.78, range ESTIMATED 0.53–0.92; ESTIMATED best-of-4=0.85; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED projected upper-95% bound=0.97. The reward interpretation is recovery of most avoidable communication loss after accounting for discovery. Residual loss arises from interference that does not appear in isolated probes and from switching costs near tied placements. Unless those interactions are demonstrated, they are possibilities rather than evidence of a large protected research gap.
## 3. Other routes
Full placement enumeration is the strongest standalone recipe, ESTIMATED R=0.72, range ESTIMATED 0.47–0.89. It ignores topology interpretation but directly optimizes the correct endpoint and can be entirely lawful within the wall-time allowance.

A search route combining reduced-size probe runs, a fitted latency model and local placement permutations gives ESTIMATED R=0.74, range ESTIMATED 0.49–0.90. Tuning probe duration jointly with service horizon matters because overmeasurement lowers net utility. A conservative single-device or smaller-parallel fallback is also legal when the model fits, ESTIMATED R=0.37, range ESTIMATED 0.12–0.64; the benchmark must include it among floors rather than force communication artificially.
## 4. What would lower lawful saturation
Require identifiable, state-dependent contention where choosing a probe perturbs the same shared route later used for service. Freeze a short discovery horizon that makes exhaustive scanning costly, with a matched development proxy and an attainable adaptive control. ESTIMATED combined R could become 0.47–0.60. Authoring realistic contention and proving its information structure costs ESTIMATED four engineer-weeks plus ESTIMATED 192 H100 GPU-h. Simply expanding the topology count leaves the cost-model recipe intact and risks turning the task into infrastructure enumeration.
## 5. Decisive-check GPU-h re-estimate
Old card estimate: ESTIMATED 10 GPU-h. New ESTIMATED 112 H100 GPU-h assumes an ESTIMATED 14B inference subject spread over ESTIMATED four H100s, ESTIMATED four plan arms and ESTIMATED three asymmetric topology blocks. At ESTIMATED two wall-hours per arm/block, service costs ESTIMATED 4×3×2×4=96 GPU-h. Directional probes, placement warmup and independent output truth add ESTIMATED 16 GPU-h. This is not training, but multi-device wall time must be multiplied by active device count; the old allowance obscures that cost and cannot cover independent graph blocks.
## 6. Duplicate check
05A: MODERATE, after reading its exact-serving contract; topology identification is an additional action interface, although final utility is the same serving capacity. 05B: WEAK, using its inspected distributed-training statement, because exact gradient execution rather than inference placement is its target. No existing source examined requires precisely this paid topology-probing intervention.
## 7. Verdict
CUT. ESTIMATED best-of-four is 0.25 above its line, and the single-run forecast breaches by ESTIMATED 0.08. Stable asymmetric routes are well served by measurement, topology modeling and direct placement search.
## 8. Measurement status
Rollouts UNMEASURED (planned: paid probe-and-service policies on independent graphs). Grader noise UNMEASURED (planned: repeated collective and serving timings). Score ladder UNMEASURED (planned: fixed placement, exhaustive grid, modeled search and adaptive contention control).
## Screen record
id: C033
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.78
attack_single_range: 0.53-0.92
bo4_est: 0.85
pass4_est: 0.96
ub95_est: 0.97
gpuh_old: 10
gpuh_new_est: 112
duplicate_of: 05A MODERATE; 05B WEAK
kill_reason: topology probes and placement enumeration recover stable asymmetry
souping_flag: no
