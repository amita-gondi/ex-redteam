# C048 — Pretrain under a changing lossless data codec — screen audit
## 1. What the screen claimed
The screen recommended an ordered sample plan, asynchronous decompression workers, bounded lookahead, sampling-debt correction and cache/queue tuning. ESTIMATED single/bo4/pass@4/ub95 were 0.88/0.93/0.99/0.99; CUT, category SYS, followed because established overlap and fair delivery cover the named failure. It cited:
- https://docs.pytorch.org/docs/stable/data.html
- https://docs.nvidia.com/deeplearning/dali/user-guide/docs/pipeline.html
- https://docs.mosaicml.com/projects/streaming/en/stable/api_reference/generated/streaming.StreamingDataset.html

## 2. Evidence audit
The fetched PyTorch documentation explicitly warns that unordered loading can skew imbalanced training distributions. DALI and Streaming document buffering, asynchronous execution and cache/predownload controls, but documentation of APIs is not an end-to-end codec-learning result. The stronger claim that an agent integrates the stack needs demonstrated systems work. Grade PARTIAL, despite a close mechanistic match: no old citation measures this particular codec-switching pipeline or improvement beyond a competent loader floor.

## 3. Research done now
All C048 performance forecasts and pilot allocations are ESTIMATED. Published system results below are evidence from other tasks.
- torch.utils.data — PyTorch, 2026 documentation snapshot — https://docs.pytorch.org/docs/2.15/data.html — fetched — `in_order`, workers and prefetch settings directly address latency-induced exposure distortion; source-ID reconciliation must still verify custom dataset behavior.
- Pipeline and processing graph — NVIDIA, 2026 documentation accessed — https://docs.nvidia.com/deeplearning/dali/user-guide/docs/pipeline.html — fetched — CPU/GPU overlap and separate queue depths are implemented controls, raising confidence that ordinary decompression variance can be hidden within available buffering.
- StreamingDataset — MosaicML, undated API documentation, accessed 2026 — https://docs.mosaicml.com/projects/streaming/en/stable/api_reference/generated/streaming.StreamingDataset.html — fetched — Predownload, bounded caches and balanced sampling support a practical replacement loader. It does not benchmark the card's private codec dependencies.
- Scalable and Performant Data Loading — Moto Hira et al., 2025, revised 2026 — https://arxiv.org/abs/2504.20067 — fetched — SPDL demonstrates non-starving ViT training and faster, resource-efficient loading; transferring its concurrency design to compressed text remains an integration step.
- ATTUNE: Agentic Throughput Tuning for LLM Training — Amazon research team, 2026 — https://arxiv.org/html/2610.17528v2 — fetched — Autonomous tuning improves real training stacks under charged GPU budgets and external correctness gates. This raises confidence in finding interacting performance settings rather than merely knowing their names.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/abs/2611.16591 — fetched — End-to-end training and inference systems can be assembled autonomously at the twelve-hour horizon, countering a generic integration-hardness defense.
- Singularity-Bench project results — Infini AI Lab, 2026 — https://infini-ai-lab.github.io/singularity-bench/ — fetched — The pretraining case connects delivered compute, recipe choices and actual final perplexity; the reported inference failure rate also shows that systems success is not universal.

## 4. Re-estimated attack
Lock intended source IDs before dispatch, use parallel decode with a bounded reorder buffer, schedule imminent expensive blocks first, and tune caches, workers and codec blocks against full target-loss time. Where exact order is not required, carry sampling debt explicitly. Permit charged hot-set predecompression as another candidate.

The literature/API forecast credits ESTIMATED 0.31 to restoring intended exposure, 0.34 to overlap and 0.13 to joint block/cache tuning: 0.78. This is conditional on an avoidably inefficient inherited pipeline; these gains cannot be credited again if already absorbed in the frozen competent floor. Lack of physical residual reserve would itself invalidate the task's calibration.

Use R={0.60,0.78,0.86} with probabilities {0.10,0.65,0.25}. Most configurations implement the same mature solution; CPU/storage topology, cache state and integration defects drive a narrower spread than an insight-dependent scientific task. ESTIMATED mean=0.78, range 0.60–0.86; bo4=0.86−0.08×0.75^4−0.18×0.10^4=0.83. Here p=1.00, so pass@4=1−0^4=1.00; ub95=0.86. The old 0.88 is too close to perfect for an uninstantiated codec workload, even though the attack remains strong.

## 4A. Demonstrated capability and subfield SOTA
SPDL reports ImageNet iteration 74% faster than PyTorch DataLoader, using less CPU and memory, while avoiding ViT-B/16 starvation. This demonstrated systems result anchors an ambitious loader comparator; it is not a universal codec optimum. Combine its concurrency design with ordered Streaming-style delivery and metered buffering. R≈1 still needs a same-topology end-to-end control; no fetched source pins C048's numerical endpoint.

ATTUNE's Opus 4.8+Claude Code controller, guided by a tuning skill and a correctness gate, reports +33.9% throughput on GLM-4.5 using a mean 669 GPU-h over 6.4 hours on 128 B200s. Its gate preserves data order and checks losses. That is strong evidence of autonomous coupled systems tuning inside this wall-time, but vastly more GPUs and a distributed-training bottleneck differ from codec starvation. Singularity-Bench's Opus 5.5+Claude Code built a training system in twelve hours on four GB300s, reaching 12.77 perplexity against an OLMo 2 recipe around 14.2. This validates useful delivered-compute optimization end to end, with no direct codec-switch test. The same project reports seven inference engines failing its quality/validity checks, limiting any claim of deterministic integration.

KNOWN-RECIPE and AGENT-DEMONSTRATED overlap for the relevant capability of integrating and validating an efficient training pipeline. attack_basis=DEMONSTRATED-AGENT, scoped to systems integration, not a claim that C048 was solved. The remaining twelve-hour work is adapting the codec interface and proving exposure conservation; no novel learning mechanism is demanded by the original card.

ANCHORED R={0.54,0.72,0.82}, masses={0.15,0.65,0.20}: ESTIMATED single=0.71, range 0.54–0.82; bo4=0.82−0.10×0.80^4−0.18×0.15^4=0.78; pass@4=1−0.15^4=1.00; ub95=0.82. Transfer from training-system demonstrations and the unknown native reward ladder remain assumptions, so verdict_rests_on_assumption=yes even with demonstrated agent capability.

## 5. Verdict under the kill lines
Both forecasts give CUT, UNCHANGED. Anchored single exceeds its threshold by 0.01, bo4 by 0.18, pass@4 by 0.50 and ub95 by 0.07. Autonomous training-system results substantiate the direction of the old kill, while reducing its near-perfect numerical confidence. This is the clearest mature-stack failure in the pretraining portion of B04.

## 6. Redesign
Cause (a); REDESIGNABLE. Start with ordered fair asynchronous loading already functioning. Permit disclosed phase-level sampling flexibility while fixing total source obligations and final coverage. Introduce realistic dictionary/checkpoint reuse across codec blocks and development-visible learning-stage differences in the value of source exposure. The research decision becomes which source blocks to prepare and cache now so that later curriculum choices remain cheap and useful; preparation, recompression, cache eviction and all GPU waiting count toward final learning utility.

An ordered loader, static lookahead, deficit correction and worker tuning cannot anticipate every change in marginal learning value. The strongest new attack combines a learned source-value model, model-predictive cache scheduling and trajectory-aware mixture search. It may still work; the redesign survives only after a measured reversal where a static throughput winner loses in final loss and an attainable adaptive control wins. This is useful at frontier corpus scale, without hiding the codec graph, adding random latency or making memory infeasible.

Re-attack basis LITERATURE-ONLY: joint curriculum/cache optimization has not been established by the cited agent results. ESTIMATED R={0.31,0.49,0.64}, masses={0.25,0.65,0.10}: single=0.46; bo4=0.64−0.15×0.90^4−0.18×0.25^4=0.54; pass@4=0.34; ub95=0.64. Pilot ESTIMATED 96 H100 GPU-h: a 0.3B mechanism-preserving learner, five policies × three seeds × five hours × one H100=75, plus twelve cache-state replication and nine final-loss GPU-h. A later 1B–3B continuation must confirm that the interaction persists when GPU work increases.

## 7. Measurement status
Rollouts UNMEASURED (planned full compressed-corpus training with accepted-source receipts). Grader noise UNMEASURED (planned cache-state and learner replication). Score ladder UNMEASURED (planned stock delivery, complete fair-overlap floor, adaptive cache/curriculum policy and measured stronger pipeline).

## Audit record
id: C048
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.88
old_bo4: 0.93
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.78
new_single_range: 0.60-0.86
new_bo4: 0.83
new_pass4: 1.00
new_ub95: 0.86
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Couple fully metered codec cache preparation to observable stage-dependent curriculum value beyond fair asynchronous loading.
redesign_single: 0.46
redesign_bo4: 0.54
redesign_pass4: 0.34
redesign_ub95: 0.64
redesign_gpuh: 96
attack_basis: DEMONSTRATED-AGENT
demonstrated_ref: ATTUNE, Opus 4.8 Claude Code, 2026; Singularity-Bench pretraining, Opus 5.5 Claude Code, 2026
gap_to_attack: Codec integration and receipt validation remain untested directly
subfield_sota_ref: SPDL non-starving training and efficient loading, Hira, 2025 revised 2026
anchored_single: 0.71
anchored_bo4: 0.78
anchored_pass4: 1.00
anchored_ub95: 0.82
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
