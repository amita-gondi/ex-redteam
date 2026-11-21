# C032 — Inference that survives bursty image token expansion — screen audit
## 1. What the screen claimed
Staged visual encoding, separate decoder admission, calibrated reservations and chunked scheduling supposedly bypassed uncertain crop counts. The screen assigned ESTIMATED single=0.73, bo4=0.81, pass@4=0.92 and ub95=0.94; its CUT, category SYS, rested on revealing sizes before allocating decoder state. The original citations were:
- https://docs.vllm.ai/en/latest/configuration/engine_args/
- https://www.usenix.org/conference/osdi24/presentation/agrawal

## 2. Evidence audit
The vLLM documentation confirms separate encoder capacity and work budgets, but the existence of these controls does not measure successful admission for content-dependent expansion. Sarathi-Serve evaluates chunked text prefill, not the information cost of discovering visual crops. Grade: PARTIAL: staged scheduling has real implementations, whereas the assumed cheap size revelation, correlated visual bursts and preserved large-image completion remain outside the screen's cited experiments.

## 3. Research done now
- Engine Arguments — vLLM project, 2026 maintained documentation — https://docs.vllm.ai/en/latest/configuration/engine_args/ — fetched — Encoder-output residency and per-step encoding limits are distinct, making separate admission practical. The documentation raises implementation confidence without supplying this card's completion curve.
- Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve — Amey Agrawal et al., 2024 — https://www.usenix.org/conference/osdi24/presentation/agrawal — fetched — Chunked prefill supports mixing long input work with decode; its text workload offers no direct evidence about unknown visual expansion.
- Efficiently Serving Large Multimodal Models Using EPD Disaggregation — Gursimran Singh et al., 2025 — https://proceedings.mlr.press/v267/singh25d.html — fetched — Separating encode, prefill and decode yields measured memory and service-level improvements. This is stronger support than a text scheduler for reclaiming wasted reservations, though dedicated resources cannot be added without charging them.
- EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models — Kunxiong Zhu et al., 2026 — https://arxiv.org/abs/2609.31551 — fetched — Joint encoding admission, offload and allocation search improves SLO goodput against production systems. It raises the combined recipe while also showing that merely exposing encoding as a service leaves flow-control problems.
- When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving — Jesse Gu et al./NVIDIA, 2026 — https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving — fetched — The body discusses media-heavy benefits and decode-heavy regimes where separation loses value. Those qualifications lower any claim that EPD automatically produces large normalized reward.

## 4. Re-estimated attack
All utility shares here are ESTIMATED allocations, pending measured floor and ceiling. Attribute 0.40 of the opportunity to safe staged admission, 0.35 to encoder/decoder queue utilization and 0.25 to costly revelation plus burst/fairness handling. ESTIMATED recovered fractions 0.95/0.65/0.36 yield 0.40×0.95+0.35×0.65+0.25×0.36=0.70. Completion denominators retain every image stratum, and work performed to discover crops is charged even if admission is delayed.

The ESTIMATED recipe distribution has R=0.50/0.69/0.81 at probabilities 0.18/0.47/0.35. These states represent a conservative queue, a tuned staged pipeline and successful cross-stage balancing. Variation arises from integration and burst composition rather than invented grader jitter. ESTIMATED mean=0.18×0.50+0.47×0.69+0.35×0.81=0.70, range 0.50–0.81. ESTIMATED bo4=0.81−0.12×0.65^4−0.19×0.18^4=0.79. With p=0.82, ESTIMATED pass@4=1−0.18^4=1.00 rounded; ESTIMATED ub95=0.81. This drops the screen's upper tail because even a good scheduler pays for information acquisition; it still predicts recipe-level saturation.

## 4A. Demonstrated capability and subfield SOTA
Subfield SOTA consulted is EAServe's measured encode-aware goodput versus Dynamo and vLLM, reinforced by EPDServe and NVIDIA's topology comparisons. The north star should be the best resource-matched EAServe/EPD configuration on the disclosed crop workload. Their published gains are not this task's R≈1: neither supplies a content-revelation optimum on this card's machine. An attainable stronger controller and public combined floor must be executed before fixing reward anchors.

- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Opus 5.5+Claude Code beat SGLang serving income within twelve hours on four GB300s. This demonstrates integrated admission/kernel work; no content-dependent visual expansion was evaluated.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern et al., 2024 — https://arxiv.org/html/2410.07095v1 — fetched — o1-preview+AIDE earned medals on a minority of competitions with twenty-four hours and one A10. Pipeline experimentation is demonstrated; multimodal queue validation is not its objective.

These are reported agent outcomes, not measurements made for this audit. The relevant multimodal recipe is KNOWN-RECIPE; AGENT-DEMONSTRATED evidence stops short of integrating uncertain encoding cost with completion guarantees. attack_basis=LITERATURE-ONLY, and the verdict rests on extrapolation. Twelve hours must cover constructing a cost model, instrumenting real memory peaks, implementing flow control and checking tail completions; neighboring text-serving success does not establish that reliability.

ANCHORED ESTIMATED modes are 0.31/0.51/0.66 with probabilities 0.25/0.63/0.12. The central mode assumes a functional staged server; the upper one requires a validated content-aware policy. ESTIMATED single=0.25×0.31+0.63×0.51+0.12×0.66=0.48, range 0.31–0.66. ESTIMATED bo4=0.66−0.15×0.88^4−0.20×0.25^4=0.57; p=0.12 gives pass@4=1−0.88^4=0.40; ub95=0.66. Conditional independence is over researcher restarts given matched arrival-family coverage.

## 5. Verdict under the kill lines
The section-4 evidence re-estimate remains CUT through ESTIMATED bo4=0.79. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; bo4 is ESTIMATED 0.03 below its line and therefore lacks comfortable margin. New multimodal system evidence strengthens the available recipe, while the two fetched agent studies do not show its uncertain-size integration. Retention requires an explicit finite-horizon service objective and a measured content-revelation control, not a ban on staged preprocessing.

## 6. Redesign
Cause (a), serving-stack reuse. REDESIGNABLE with concrete conditioning: use a progressive document/image encoder that produces genuinely useful intermediate work, where further prescribed crops reveal downstream memory and encoding cost. Supply the splitter, feature telemetry, cost accounting and representative content-dependent bursts. Measure complete, quality-equivalent responses delivered before application deadlines, with large-image strata retained and the same total device pool for every arm. Choose feasible loads where the combined EAServe-style floor and a stronger controller both finish substantial work; overload alone earns no difficulty claim.

The strongest remaining attack combines incremental revelation, uncertainty-calibrated reservations, age protection, stage batching and model-predictive admission. It must decide whether another reveal is worth occupying an encoder slot while decode deadlines approach. Static tuning cannot recover that information-value tradeoff by simply waiting until all sizes are known. The redesign's re-attack basis is LITERATURE-ONLY: this specific coupled policy has no fetched autonomous demonstration.

ESTIMATED outcomes 0.29/0.45/0.62, probabilities 0.45/0.47/0.08, encode failure to improve the combined floor, useful ordinary control and rare effective lookahead. ESTIMATED single=0.45×0.29+0.47×0.45+0.08×0.62=0.39, range 0.29–0.62; bo4=0.62−0.17×0.92^4−0.16×0.45^4=0.49; pass@4=1−0.92^4=0.28; ub95=0.62. Risks are predictable crop costs collapsing the problem into ordinary queueing, or latency targets manufacturing infeasibility. A frontier lab would value avoiding encoder-induced service collapse under genuine demand.

Decisive pilot ESTIMATED GPU-h: an 8B VLM, one H100, five policies, three independent image-history seeds, one hour per run gives 5×3×1×1=15.00. Add ESTIMATED 5.00 for exact-output references and 4.00 for repeated memory/deadline captures: total 24.00 H100 GPU-h; this cost is a plan only.

## 7. Measurement status
Rollouts UNMEASURED (planned actual progressive encoding under identical arrival histories). Grader noise UNMEASURED (planned hardware-memory and timing replication with fixed outputs). Score ladder UNMEASURED (planned production staged queue, encode-aware tuned floor and attainable lookahead policy).

## Audit record
id: C032
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.73
old_bo4: 0.81
old_pass4: 0.92
old_ub95: 0.94
new_single: 0.70
new_single_range: 0.50-0.81
new_bo4: 0.79
new_pass4: 1.00
new_ub95: 0.81
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Couple progressive visual-cost revelation with feasible application deadlines and quality-preserving complete-response utility.
redesign_single: 0.39
redesign_bo4: 0.49
redesign_pass4: 0.28
redesign_ub95: 0.62
redesign_gpuh: 24
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench, Opus 5.5 plus Claude Code, 2026; MLE-bench, o1-preview plus AIDE, 2024
gap_to_attack: no autonomous uncertain-crop admission result
subfield_sota_ref: EAServe encode-aware multimodal goodput, Zhu et al., 2026
anchored_single: 0.48
anchored_bo4: 0.57
anchored_pass4: 0.40
anchored_ub95: 0.66
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
