# C017 — Keep useful GPU work under adversarially correlated arrivals — screen audit
## 1. What the screen claimed
The screen upgraded the engine, used chunked prefill or feasible prefill/decode separation, and added dependency-aware burst prediction plus deadline admission. Its ESTIMATED single/bo4/pass@4/ub95 were 0.70/0.79/0.91/0.94; CUT, category SYS, because serving replacement and burst-aware tuning likely absorb the reserve. The old citations were:
- https://www.usenix.org/conference/osdi24/presentation/agrawal
- https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin
## 2. Evidence audit
Sarathi-Serve directly supports chunked prefill; DistServe supports disaggregation under its allocation and networking assumptions. They are competing architecture choices, not benefits to add without accounting. Neither old citation demonstrates prediction of tool-return bursts, and their standard objectives do not certify exact token sequences on this workload.

The screen understated how much newer work addresses program and tool dependencies, but overstated what its two citations alone establish. Grade: PARTIAL. Current systems and agent benchmarks make the whole-stack attack credible; exact-output conformance, fixed offered-load coverage and the normalized goodput frontier still need task-specific validation.
## 3. Research done now
- Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve — Amey Agrawal et al., 2024 — https://www.usenix.org/conference/osdi24/presentation/agrawal — fetched — Establishes prefill/decode interference control, raising the engine-replacement floor without establishing causal burst forecasting.
- DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving — Yinmin Zhong et al., 2024 — https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin — fetched — Demonstrates goodput-oriented separation; on a small fixed allocation its additional resources may be unavailable.
- Parrot: Efficient Serving of LLM-based Applications with Semantic Variable — Chaofan Lin et al., 2024 — https://www.usenix.org/conference/osdi24/presentation/lin-chaofan — fetched — Application dataflow is already an optimization interface, weakening novelty based only on knowing dependency graphs.
- Autellix: An Efficient Serving Engine for LLM Agents as General Programs — Michael Luo et al., 2025 — https://arxiv.org/abs/2502.13965 — fetched — Demonstrated program-aware prioritization directly strengthens the proposed aging and dependency-aware scheduler.
- TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving — Shuhuai Li et al., 2026 — https://arxiv.org/abs/2610.37230 — fetched — Joint admission/placement uses near-term tool readiness, cache credit and token footprint; the old burst predictor is now a published concrete recipe.
- JITServe: SLO-aware LLM Serving with Imprecise Request Information — Wei Zhang et al., 2026 — https://www.usenix.org/system/files/nsdi26-zhang-wei.pdf — fetched — Demonstrates goodput scheduling with uncertain request information, countering a hardness claim based merely on imperfect length forecasts.

Search also found the fetched autonomous-serving results in section 4A. None of the positive systems evidence permits silently relaxing exact generation or dropping difficult offered strata.
## 4. Re-estimated attack
Every reward allocation is ESTIMATED. Engine modernization captures about 0.34, deadline-aware batching adds 0.21, and readiness/cache-aware admission adds 0.18 after overhead. The residual involves token conformance, joint-queue effects and forecast mistakes; the floor/control anchors are still absent.

Represent recipe-conditioned attempts by R=0.52/0.72/0.86 with probabilities 0.15/0.60/0.25 for poor architecture fit, successful standard integration and effective joint tuning. ESTIMATED single=0.15×0.52+0.60×0.72+0.25×0.86=0.73, range 0.52–0.86. ESTIMATED bo4=0.52×0.15^4+0.72×(0.75^4−0.15^4)+0.86×(1−0.75^4)=0.82; p=0.85 gives pass@4=1−0.15^4=1.00 rounded; ub95=0.86 since mass below the last state is 0.75. Spread comes from engine suitability and tuning paths, with process/workload variance not yet measured. The mean rises from the old screen because current tool-aware scheduling evidence is closer, not because of an automatic offset.
## 4A. Demonstrated capability and subfield SOTA
JITServe and TAO are the closest verified SOTA anchors for deadline-qualified tokens and tool-aware admission. A credible north star is their native goodput frontier under the same hardware, augmented by exact-output checks. Published headline gains cannot set this card's R≈1 or reference numerically; the stronger control must reproduce that capability on the offered graph distribution.

- ServerBench: How can your coding agents design specialized LLM serving systems? — Xinrui Zhong et al., 2026 — https://arxiv.org/html/2611.06841v1 — fetched. Opus 5.5+Claude Code improves qualified serving value to a reported 2.71 times SGLang on Qwen3.5 9B in eight development hours using two L40s. Stateful response-dependent replay is close to this attack; its tolerance-based output verification and chosen concurrency are weaker than exact fixed-offered-load requirements.
- Singularity-Bench: Can Agents Build Agents? — Infini-AI-Lab, 2026 — https://arxiv.org/html/2611.16591v1 — fetched. Opus 5.5+Claude Code builds a combined kernel/cache/prefill engine in twelve hours on four GB300s, earning reported 11.52 versus SGLang's 8.18 simulated dollars per GPU-hour. The closed-loop coding workload supports integration ability; different hardware and accuracy gates leave an exactness gap.
- InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents — Yeon et al., 2026 — https://arxiv.org/html/2607.20468v1 — fetched. Sonnet 4.6+Claude Code achieves reported aggregate 8.08 times naive PyTorch performance in two hours on one H100. Same-budget SMAC does better, and many agents ship brittle launchers: real counterevidence to assuming universally reliable integration.

attack_basis=DEMONSTRATED-AGENT for comparable complete serving optimization, with explicit transfer risk for exact outputs and causal bursts. KNOWN-RECIPE readiness scheduling supplies the remaining component; no result demonstrates this exact task. ANCHORED ESTIMATED states 0.42/0.66/0.81 with probabilities 0.25/0.50/0.25 allow substantial validity/transfer failures. ESTIMATED single=0.25×0.42+0.50×0.66+0.25×0.81=0.64, range 0.42–0.81; bo4=0.42×0.25^4+0.66×(0.75^4−0.25^4)+0.81×(1−0.75^4)=0.76; pass@4=1−0.25^4=1.00 rounded; ub95=0.81. The verdict relies on demonstrated nearby integration, with quantitative reward mapping still estimated.
## 5. Verdict under the kill lines
Both the evidence re-estimate and ANCHORED headline are CUT; UNCHANGED versus the screen. Anchored ESTIMATED bo4 breaches by 0.16, pass@4 by 0.50 rounded, and ub95 by 0.06. Unlike a literature-only kill, ServerBench and Singularity-Bench actually demonstrate multi-piece serving improvement in comparable development time. Exactness is a material limitation to test, not evidence that integration cannot occur.
## 6. Redesign
Cause (a), mature serving and program-aware scheduling. REDESIGNABLE, but simply adding causal graphs is no longer enough after the newer systems results.

Expose a joint tool-dispatch and GPU-admission interface with finite shared CPU tool queues, reusable inference state and observable branch joins. Finishing a branch releases downstream work that competes with retained state; dispatch order changes both future readiness and cache opportunity cost. Provide tool profiles, graph semantics and representative branch/cache reversals on dev. Keep every offered request in fixed deadlines and coverage denominators. Reward useful exact completions per fully charged resource ledger, with a feasible same-resource stronger controller.

The re-attack combines JITServe uncertainty margins, TAO placement, Parrot dataflow and model-predictive queue simulation. Current demonstrated agents can integrate serving machinery, but no fetched result establishes discovery of a joint downstream-resource controller within twelve hours. Re-attack basis=LITERATURE-ONLY. Its residual task is predicting the value of a dispatch-induced future queue rather than forecasting an exogenous return. A simple ready-time dynamic program may still suffice; test it before claiming headroom.

ESTIMATED redesigned outcomes 0.24/0.43/0.66 have probabilities 0.40/0.53/0.07. ESTIMATED single=0.40×0.24+0.53×0.43+0.07×0.66=0.37; bo4=0.24×0.40^4+0.43×(0.93^4−0.40^4)+0.66×(1−0.93^4)=0.48; pass@4=1−0.93^4=0.25; ub95=0.66. The rare high branch corresponds to successful causal simulation. This plausibly passes after native calibration and keeps a real agent-serving capability.

ESTIMATED decisive cost: 8B dense subject, 4 arms × 4 graph families × 2 starts × 1 hour × 1 H100=32 GPU-h; tuning adds 16 and independent exact replay 16, totaling 64 H100 GPU-h. No model training is required.
## 7. Measurement status
Rollouts UNMEASURED (planned full-budget serving integrations on endogenous graphs). Grader noise UNMEASURED (planned warm repeated launches and paired graph replays). Score ladder UNMEASURED (planned modern engine, readiness scheduler and attainable joint-resource control). Record rewards and resource forecasts are ESTIMATED.
## Audit record
id: C017
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 7
sources_fetched_count: 9
old_single: 0.70
old_bo4: 0.79
old_pass4: 0.91
old_ub95: 0.94
new_single: 0.73
new_single_range: 0.52-0.86
new_bo4: 0.82
new_pass4: 1.00
new_ub95: 0.86
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Jointly schedule observable tool queues and inference state where dispatch changes downstream demand and cache value.
redesign_single: 0.37
redesign_bo4: 0.48
redesign_pass4: 0.25
redesign_ub95: 0.66
redesign_gpuh: 64
attack_basis: DEMONSTRATED-AGENT
demonstrated_ref: ServerBench, Opus 5.5 Claude Code, 2026; Singularity-Bench serving, Opus 5.5 Claude Code, 2026; InferenceBench, Sonnet 4.6 Claude Code, 2026
gap_to_attack: exact tokens and fixed offered-load burst feedback
subfield_sota_ref: tool-aware placement, TAO, 2026; uncertain-SLO goodput, JITServe, 2026
anchored_single: 0.64
anchored_bo4: 0.76
anchored_pass4: 1.00
anchored_ub95: 0.81
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
