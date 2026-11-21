# C077 — Attention composition needs correct log-normalizers too — screen audit

## 1. What the screen claimed
The screen joined the public GQA layout repair with FlashInfer's attention-state reducer and tuning of partition count, grouping and launch geometry. It forecast ESTIMATED single/bo4/pass4/ub95 0.80/0.88/0.98/0.97 and CUT, category SYS: an available exact composition backend appeared to capture the objective directly.

Old URLs, both opened now:
- Incorrect softmax_lse in paged GQA — Dao-AILab/flash-attention, 2026 issue snapshot — https://github.com/Dao-AILab/flash-attention/issues/3039
- Cascade API — FlashInfer authors, 2026 documentation — https://docs.flashinfer.ai/api/cascade.html

## 2. Evidence audit
The issue localizes the layout failure, and the API really exposes reduction of attention outputs and log-normalizers. Those support a recognizable mathematical repair, not a measured full-path speedup across all page layouts, empty partitions and head groups. Backend replacement also needs agreement on normalizer convention and on the statistics actually consumed during timing.

Grade: PARTIAL. The operation is implemented publicly, but neither old citation shows an autonomous agent integrating it and validating the entire composed path at the claimed reward. Fresh page tables alone are weak protection; however, correctness of a nominally mature reducer cannot simply be presumed either.

## 3. Research done now
- FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving — Zihao Ye et al., 2025 — https://arxiv.org/abs/2501.01005 — fetched — Reports end-to-end serving latency improvements from a customizable attention engine, strengthening the complete-backend attack without measuring this exact partition contract.
- Cascade state merging returns NaN when all input states are empty — flashinfer-ai/flashinfer, 2026 — https://github.com/flashinfer-ai/flashinfer/issues/4051 — fetched — A fully masked-state failure directly contradicts treating stock composition as automatically valid; the lawful attack needs an identity-state guard and regression checks.
- CudaForge: An Agent Framework with Hardware Feedback for CUDA Kernel Optimization — Zijian Zhang et al., 2025 — https://arxiv.org/abs/2511.01884 — fetched — o3-based Coder/Judge optimization takes approximately 26.5 minutes per kernel on one RTX6000, making reducer-level iteration plausible within the budget.
- Evaluating frontier AI R&D capabilities of language model agents against human experts — METR, 2024 — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/ — fetched — The successful o1-preview prefix-sum case supports reduction-kernel competence, while the broader timed comparison warns that local success is not universal integration reliability.
- KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch? — Yunxiang Zhang et al., 2026 — https://arxiv.org/abs/2607.16241 — fetched — Stronger baselines and hidden input distributions lower apparent generated-kernel gains, favoring real composed-path validation here.

Research searched cascade reduction performance, empty-state handling and timed agent kernel generation; all retained support was fetched.

## 4. Re-estimated attack
The following numerical model is ESTIMATED throughout. Relative to a corrected stock floor, backend substitution could contribute 0.27 reward, producer/reducer layout fusion 0.19 and split-count/launch tuning 0.12. The resulting 0.58 provisional gain assumes enough statistic traffic is avoidable; a benchmark speed ratio is not itself normalized reward. The empty-state report reduces confidence in plug-and-play correctness but does not make the repair scientifically novel.

Let rewards 0.39/0.57/0.73 have probabilities 0.20/0.50/0.30. A valid but conversion-heavy bridge gives the low state; profitable fusion and partition selection give the high state. Single = 0.078+0.285+0.219 = 0.58, range 0.39–0.73. Bo4 = 0.73−0.16×0.70^4−0.18×0.20^4 = 0.69. Pass4 = 1−0.70^4 = 0.76; ub95 = 0.73. Spread reflects layout-integration success and profitable split choices, rather than large learner-seed noise: this is an inference kernel task. The old 0.80 gave too much weight to library availability and too little to corrected-floor calibration.

## 4A. Demonstrated capability and subfield SOTA
The relevant verified systems reference is FlashInfer's 2025 engine, with public cascade composition APIs. Its broader serving results establish useful systems capability, but not a universal best reducer on this workload. Anchor the floor to a repaired FlashAttention/FlashInfer combination and R≈1 to a separately measured exact producer/consumer control; do not stretch a tiny residual speed range into apparent research headroom.

CudaForge's o3 Coder/Judge system reports 97.6% kernel correctness and 1.68× against PyTorch, with the RTX6000 timing stated above. It supports fast synthesis, but its benchmark does not establish paged GQA state-convention integration. RE-Bench's o1-preview computer agent achieved 0.64 ms prefix-sum latency under timed attempts; task-specific accelerator allocation and the highlighted attempt duration are not identified in the blog excerpt. That result is closer to stable reduction than to a validated multi-backend attention pipeline.

KNOWN-RECIPE covers the algebra, identity guard and stock reducers. The complete strongest attack remains LITERATURE-ONLY because no comparable-budget autonomous composition integration was verified. In twelve hours the agent must bind layouts, normalization bases and timed statistics, then find a profitable execution plan. Anchored ESTIMATED atoms 0.33/0.54/0.67 with probabilities 0.20/0.68/0.12 produce single 0.51, range 0.33–0.67; bo4 = 0.67−0.13×0.88^4−0.21×0.20^4 = 0.59; pass4 = 1−0.88^4 = 0.40; ub95 = 0.67. This assumption-based transfer is deliberately separate from the papers' measured native results.

## 5. Verdict under the kill lines
The section-4 literature stress case is CUT via bo4/pass4. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; bo4 lies only ESTIMATED 0.01 below 0.60. Timed kernel-generation evidence keeps the threat serious, but the discovered empty-state issue and missing combined agent trajectory undermine the original near-certain saturation forecast. The condition is a measurable residual beyond the entire repaired backend stack.

## 6. Redesign
Class a; REDESIGNABLE. Supply corrected normalizer layouts and empty-state behavior from the start. Change the workload to explicit attention-reuse DAGs where multiple queries consume overlapping partitions and alternative materialization/recompute schedules contend for cache space. Provide these graph semantics and matched development examples, and reward complete exact graph throughput including planning, page gathering and final composition. A frontier serving team would value this schedule, especially with shared contexts and branching generation.

The strongest attack combines FlashInfer cascade, generic DAG scheduling, fusion and split autotuning. A fixed local reducer cannot choose global statistic reuse versus eviction by itself; a profitable reference must establish this distinction. ESTIMATED LITERATURE-ONLY redesigned atoms 0.21/0.45/0.63, weights 0.25/0.65/0.10: single 0.41; bo4 = 0.63−0.18×0.90^4−0.24×0.25^4 = 0.51; pass4 = 1−0.90^4 = 0.34; ub95 0.63. Generic cache-aware scheduling might still solve the workload, so include it in the decisive comparison. GPU-h ESTIMATED: frozen 1B decoder, four schedule arms×three independent blocks×one hour×one H100 = 12; compilation/correctness 4 plus end-to-end replay 8; total 24 H100-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: twelve-hour reducer integration attempts). Grader noise UNMEASURED (planned: repeated synchronized composed-path timing). Score ladder UNMEASURED (planned: repaired stock cascade, tuned split reducer, producer fusion and independent reuse-aware control).

## Audit record
id: C077
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.80
old_bo4: 0.88
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.58
new_single_range: 0.39-0.73
new_bo4: 0.69
new_pass4: 0.76
new_ub95: 0.73
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize cache-sensitive attention-state reuse over disclosed dependency graphs after the complete cascade repair is floored.
redesign_single: 0.41
redesign_bo4: 0.51
redesign_pass4: 0.34
redesign_ub95: 0.63
redesign_gpuh: 24
attack_basis: LITERATURE-ONLY
demonstrated_ref: CudaForge, o3, 2025; RE-Bench prefix sum, o1-preview, 2024
gap_to_attack: paged GQA normalization and timed multi-backend composition integration
subfield_sota_ref: FlashInfer exact attention-state engine, Ye et al., 2025
anchored_single: 0.51
anchored_bo4: 0.59
anchored_pass4: 0.40
anchored_ub95: 0.67
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
