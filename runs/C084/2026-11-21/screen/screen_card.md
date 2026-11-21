# C084 — Approximate speculation with a real downstream regret contract — saturation screen
## 1. What the grader actually rewards
The decoder earns utility from executed private programs and tool choices per serving second, with actual semantic damage charged through a disclosed quality tradeoff. R≈0 should include the strongest exact speculative alternative; R≈1 means an attainable faster decoder at the same executable-utility contract. I place the no-op at ESTIMATED R=0.00 and the intended reference at ESTIMATED R=0.60, conditional on a live speed/quality scalarization; acceptance rate and local logit regret are diagnostics only.
## 2. Strongest lawful combined attack
Begin with exact verification from [Fast Inference from Transformers via Speculative Decoding](https://proceedings.mlr.press/v202/leviathan23a.html), which offers a legal speed route without semantic approximation. Add the approximate-verification policy identified by the verified [ASD checkpoint repository](https://huggingface.co/ynFeng/approximate-speculative-decoding/tree/main), then reserve exact verification for control-flow tokens, tool arguments and low-confidence spans. Tune speculative length using the concurrency-aware dispatch available in [vLLM dynamic speculative decoding](https://docs.vllm.ai/en/stable/features/speculative_decoding/dynamic_speculative_decoding/). Select on executed development tasks, never on acceptance alone.

The full stack can approximate formatting and predictable boilerplate while preserving sensitive regions; it can also choose entirely exact decoding when approximation does not pay. Its limitation is recognizing semantic sensitivity before a mismatch changes the future branch. A low-regret identifier, literal or apparently harmless earlier statement may determine later execution, and token-category rules cannot always detect that dependency. ESTIMATED single-run R=0.49, range 0.28–0.67; ESTIMATED best-of-4=0.59; ESTIMATED pass@4 at R≥0.60=0.36; ESTIMATED projected upper-95% bound=0.74. This is close to failure, with forecasts conditional on exact speculation already being the measured floor. If the grader instead rewards speed over plain target autoregression, the exact route could yield ESTIMATED R=0.75–0.92 and immediately kill the card.
## 3. Other routes
- Exact speculative decoding with a tuned fixed draft length is ESTIMATED R=0.15, range 0.00–0.35 on the assumed exact-competent scale. Its native utility may still dominate approximate methods, exposing absent reserve rather than demonstrating hardness.
- Sweep approximate acceptance tolerance, draft length and token-class exemptions against actual program execution: ESTIMATED R=0.45, range 0.23–0.65. Development feedback can learn broad safe regions but may overfit visible syntax categories.
- Use approximate verification only for syntactically constrained boilerplate: ESTIMATED R=0.37, range 0.16–0.58. This gives a narrow reliable speed gain while leaving most branch-dependent tokens exact.
## 4. What would lower lawful saturation
The required redesign is to freeze a tuned exact speculative decoder as the floor and state an executable quality constraint with measured nonzero weight. Include private dependency structures where semantically sensitive tokens are not recognizable from token class, paired with development probes that reveal the mechanism. ESTIMATED attack reward could fall to 0.39–0.52, with ESTIMATED authoring effort of one to two weeks and ESTIMATED added calibration of 48 H100 GPU-h. An independently attainable approximation policy must still outperform exact decoding; otherwise the task has no useful speed reserve and should be cut rather than rescued by penalizing exactness.
## 5. Decisive-check GPU-h re-estimate
Old pilot: ESTIMATED 8 GPU-h. New ESTIMATED total: 48 H100 GPU-h. Assume a frozen ESTIMATED 8B target and 0.5B draft, each pair fitting one H100 with the chosen context envelope. ESTIMATED 4 decoder policies × 3 independent workload seeds × 3 hours = 36 GPU-h; add ESTIMATED 8 GPU-h for executed quality comparisons and ESTIMATED 4 GPU-h for warmup and timing controls. There is no draft training in this pilot. The earlier budget could inspect a few semantic mistakes but cannot estimate utility per second and the exact-decoder frontier across branch families.
## 6. Duplicate check
Catalog T21 — WEAK after reading its single-model compression specification: compression changes weights and recovery, while this intervention changes trajectory acceptance with frozen weights. v3 05A — MODERATE, since exact serving is a legal alternative and shares service timing, but approximate downstream-utility grading changes both the tolerated semantics and the optimization target.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 and the projected upper bound each have only 0.01 clearance. Require the tuned exact-speculation floor, a live executable-quality contract and demonstrated attainable speed beyond that floor. Without those changes, this screen would become CUT on the exact-decoder bypass.
## 8. Measurement status
Rollouts UNMEASURED (planned: exact/approximate selective decoder searches); grader noise UNMEASURED (planned: repeated task execution and end-to-end serving grades); score ladder UNMEASURED (planned: autoregression, exact speculation, published approximation and semantic-aware control).
## Screen record
id: C084
verdict: CONDITIONAL
binding_line: ub95>=0.75
attack_single_est: 0.49
attack_single_range: 0.28-0.67
bo4_est: 0.59
pass4_est: 0.36
ub95_est: 0.74
gpuh_old: 8
gpuh_new_est: 48
duplicate_of: catalog T21 WEAK; v3 05A MODERATE
kill_reason: exact speculation floor and executable quality tradeoff remain unspecified
souping_flag: no
