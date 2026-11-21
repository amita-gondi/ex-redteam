# C111 — Make lossless training faster, then test whether the saved time is useful — screen audit
## 1. What the screen claimed
The screen's SYS CUT proposed compatible compilation/fusion, then equal-time tuning of warmup, decay, batching and data schedules. ESTIMATED single/bo4/pass@4/ub95 were 0.85/0.91/0.99/0.98; the reason was that engine replacement plus retuning directly optimizes the endpoint. URLs: https://docs.pytorch.org/tutorials/intermediate/torch_compile_full_example.html, https://arxiv.org/abs/2307.08691 and https://github.com/kellerjordan/modded-nanogpt.
## 2. Evidence audit
The fetched torch.compile End-to-End Tutorial — PyTorch, current documentation fetched 2026, publication year unspecified — demonstrates compilation, not contracted equivalence across checkpoint resumes. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning — Tri Dao, 2023 — fetched, supports faster attention but mathematical equivalence need not satisfy a bitwise update contract. Keller Jordan's modded-nanogpt — repository, accessed 2026, evolving record history — fetched, combines systems and training changes without the card's mandatory separation.

Grade PARTIAL. Fast training stacks exist, but availability is not proof that a drop-in exact engine passes the task's unspecified tolerance. The second-stage retuning recipe is much better supported than the old forecast's near-certain full-chain success. Exactness and the useful attainable reserve must be settled before assigning normalized reward.
## 3. Research done now
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — autonomous target-quality speedups are directly relevant; the evaluation permits changes beyond lossless execution.
- AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure — Megan Kinniment/METR, 2026 — https://metr.org/blog/2026-11-20-q4-2026-capability-update/ — fetched — real optimization gains coexist with a large best-human gap and costly validation, weakening a near-saturated score.
- Session report: 0.9979 → 0.9697 in 126 experiments — Claude agent posting/Andrej Karpathy repository, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — gives a budget-comparable model-quality search trajectory, strengthening ordinary equal-time recipe optimization.
- NanoGPT-Bench — IntologyAI, 2026 — https://github.com/IntologyAI/NanoGPT-Bench — fetched — autonomous historical-record recovery is studied with a much larger 512 H100-hour budget, exposing the danger of ignoring search compute.

Search explicitly sought lossless training acceleration and agent speedrunning. Four new sources supplement the three opened screen references; all count as fetched.
## 4. Re-estimated attack
All forecasts and probability masses in this audit are ESTIMATED. The lawful attack profiles actual bottlenecks, applies only equivalent execution changes, verifies a resume trajectory, then retunes training at the measured new horizon. Provisional central reward is 0.29 for useful extra updates, 0.23 for horizon-correct decay and batch selection, and 0.11 for staged data/retention tuning: 0.63 total. These credits describe native-quality improvements after a competent joint floor, not two separate payments for speed and quality. Their overlap remains unmeasured.

A scenario mixture handles the exactness gate: scores 0.41/0.63/0.84 with masses 0.18/0.57/0.25 represent few legal optimizations, a useful compatible speedup, and a particularly favorable coupled recipe. Mean=0.64, range 0.41–0.84; bo4=0.84−0.21×0.75^4−0.22×0.18^4=0.77. Here p=0.82 and pass@4=1−0.18^4=1.00 rounded; q95=0.84. Workload bottlenecks and finding a compatible implementation drive the mixture; ordinary timing noise is secondary. Even this recipe-conditional estimate is materially below the old 0.85 mean.
## 4A. Demonstrated capability and subfield SOTA
Subfield anchors are observed target-loss speedruns and the best feasible same-time learning curve. OpenAI reports a best human saving of 72.38% of baseline training time on its NanoGPT evaluation; this is a concrete reference comparator, not an exact-update result. The modded-nanogpt ecosystem is another real frontier, but changes there cannot automatically enter stage one. R≈1 requires an exact accelerated implementation plus a demonstrably stronger retuned learner at the task's model scale. No source calibrates that complete quantity.

Two fetched demonstrations make this more vulnerable than an arbitrary research task. GPT-6.2 Astra, in OpenAI's evaluation scaffold whose internal details are unreported, saves 42.87% of baseline NanoGPT time with two hours and one H100 while reaching target quality. The missing piece is guaranteed unchanged training updates before retuning. The autoresearch Claude trajectory uses one H100 80GB for about 10.5 hours and 126 trials, improving bits/byte from 0.997900 to 0.969686. Its model version is unspecified, and it starts in a prepared short-loop setup rather than validating a replacement exact engine. METR's separate 48-hour/eight-H100 search reaches a best 15.7% speedup, showing that reference strength and budget matter.

KNOWN-RECIPE covers both stages separately; AGENT-DEMONSTRATED supports bounded training optimization but not their complete exactness-certified composition. Overall basis LITERATURE-ONLY. A high card-wide score would therefore be unjustified. The anchored mean below reflects the missing equivalence, horizon transfer and independent quality validation; its optimistic tail remains possible rather than demonstrated.

ANCHORED ESTIMATED outcomes: 0.33/0.55/0.76 with masses 0.24/0.61/0.15. Central credits are 0.25 affordable updates, 0.21 recipe tuning and 0.09 validated interaction. Mean=0.53, range 0.33–0.76; bo4=0.76−0.21×0.85^4−0.22×0.24^4=0.65; pass@4=1−0.85^4=0.48; q95=0.76. Integration probabilities are assumed. This is a precautionary forecast CUT, not evidence that an autonomous agent already reaches that reward.
## 5. Verdict under the kill lines
Evidence re-estimate CUT with bo4 0.17 above threshold. ANCHORED verdict CUT, UNCHANGED: bo4 is about 0.05 above its line, while ub95 exceeds 0.75 by 0.01. Demonstrated short-loop optimization preserves a credible saturation route, but removes the old claim of near-certain high performance. The anchored verdict rests on transfer assumptions and must be tested against a properly tuned floor.
## 6. Redesign
Class (a), mature engine/training search. REDESIGNABLE through a substantive scientific interaction. Use a real continued-pretraining workload with scarce high-value data and optimizer-state histories where acceleration changes whether a later recovery or specialization phase is worth attempting. Supply representative full learning curves, data availability and execution profiles. Grade final held-out quality with retention constraints; equivalent execution receipts remain admission checks. Independently retune both slow and fast engines, and include modern recipe search in the baseline.

The strongest re-attack combines compatible compilation, short-loop HPO, curve extrapolation and staged source allocation. It now needs to forecast delayed interference and data exhaustion after a changed update horizon, rather than merely extend decay. This preserves a frontier-lab problem: converting infrastructure savings into durable learning utility. It fails as a redesign if an ordinary data schedule solves the interaction or if the chosen history creates no feasible stronger control. No artificial deadline is used to make learning impossible.

Re-attack basis LITERATURE-ONLY. ESTIMATED mixture 0.30/0.47/0.67 at 0.27/0.64/0.09 yields mean 0.44; bo4=0.67−0.20×0.91^4−0.17×0.27^4=0.53; pass@4=1−0.91^4=0.31; q95=0.67. ESTIMATED check: 1B continuation, two engines × three schedules × two seeds × twenty hours × one H100=240 GPU-h; equivalence/resume work=16; 4B confirmation two pairs × two seeds × twelve H100-hours=48; independent loss/retention evaluation=16. Total 320 H100 GPU-h; longer-horizon feasibility is the decisive uncertainty.
## 7. Measurement status
Rollouts UNMEASURED (planned: full engine-plus-recipe attempts). Grader noise UNMEASURED (planned: fixed-artifact timing and continuation repeats). Score ladder UNMEASURED (planned: retuned slow engine, exact accelerated fixed schedule, retuned fast engine and stronger interaction-aware control).
## Audit record
id: C111
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.85
old_bo4: 0.91
old_pass4: 0.99
old_ub95: 0.98
new_single: 0.64
new_single_range: 0.41-0.84
new_bo4: 0.77
new_pass4: 1.00
new_ub95: 0.84
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Require economically meaningful delayed data and optimizer interactions after verified acceleration with both engines independently retuned.
redesign_single: 0.44
redesign_bo4: 0.53
redesign_pass4: 0.31
redesign_ub95: 0.67
redesign_gpuh: 320
attack_basis: LITERATURE-ONLY
demonstrated_ref: NanoGPT internal evaluation, GPT-6.2 Astra, 2026; autoresearch, Claude unspecified, 2026
gap_to_attack: exact-update certification plus coupled horizon and quality validation
subfield_sota_ref: NanoGPT human 72.38% time saved, OpenAI, 2026
anchored_single: 0.53
anchored_bo4: 0.65
anchored_pass4: 0.48
anchored_ub95: 0.76
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
