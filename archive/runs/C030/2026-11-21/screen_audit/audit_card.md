# C030 — Serve hybrid recurrent states after canceled generations — screen audit
## 1. What the screen claimed
The strongest stack used committed checkpoints plus buffered inputs, pointer rollback, cancellation fences and generation-tagged slot ownership, then tuned checkpoint and speculation intervals. It reported ESTIMATED single/bo4/pass@4/ub95=0.82/0.89/0.98/0.98 and CUT, category SYS: a public buffered-replay representation directly addresses full-state copying. The URLs were:

- https://arxiv.org/abs/2610.13778
- https://docs.vllm.ai/en/latest/api/vllm/v1/worker/mamba_utils/

## 2. Evidence audit
ReplaySSM: Cache SSM Inputs, Not State — Ze-Wei Liou, 2026, fetched — actually implements buffered state for Mamba-2 and Gated DeltaNet with improved serving throughput. That closely supports the memory/rollback component. mamba_utils — vLLM project, 2026 documentation snapshot, fetched — exposes lifecycle utilities, without proving cancellation fencing and later slot reuse across every private transition graph. ReplaySSM's quality/precision comparisons also do not establish identical outputs to a separately ordered eager implementation.

Grade: PARTIAL. This bibliography is substantially closer to the actual bottleneck than generic transaction citations would be. The missing parts are the specified arithmetic contract, all asynchronous ownership transitions and copy-cap-dependent performance. A paper implementation is not evidence that an agent installs, adapts and validates the complete recipe inside the allowed campaign.

## 3. Research done now
- HybridSpec: Throughput-Aware Speculative Decoding for Hybrid GDN-MoE Models — Haiyu Wang, 2026 — https://arxiv.org/abs/2611.04055 — fetched — Reconstructs accepted recurrent states without retaining every intermediate snapshot and selects verification lengths from target costs. This strengthens the throughput attack; its single-request greedy setting does not certify canceled concurrent slot reuse.
- Lost in Rounding: bf16 Recurrent State Makes Hybrid Reasoning Models Think Longer — Yuchuan Weng, 2026 — https://arxiv.org/abs/2611.12127 — fetched — State rounding alters long generated behavior. It lowers confidence in algebraically equivalent replay passing the eager-output oracle and makes precision/order an explicit contract requirement.
- ReplaySSM CPU backup/restore loses pending accepted updates — SGLang project issue, 2026 — https://github.com/sgl-project/sglang/issues/38485 — fetched — Reports loss of accepted buffered updates during retraction/restore. This is a concrete integration hazard, not a benchmark-wide failure rate or independently reproduced finding.
- SWE-Serve: Benchmarking Agentic Engineering for Production Inference Serving — Jennifer Williams, 2026 — https://arxiv.org/html/2609.26777v1 — fetched — Its task inventory includes Mamba offloading, hybrid cache control and streaming state commits. That is direct evidence of relevant production engineering coverage, with a substantial gap between local and complete serving tests.
- Singularity-Bench: Can Agents Build Agents? — Infini-AI Lab, 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Agents implement hybrid-attention engines under a fixed session budget. Its cancellation-related availability failures show why faster valid isolated requests do not establish a correct service lifecycle.

## 4. Re-estimated attack
Every reward figure below is ESTIMATED. Buffered state representation plausibly recovers 0.31, ownership epochs/stream fences contribute 0.20 and checkpoint/batch tuning adds 0.13. The approximately 0.64 total leaves replay arithmetic, unsupported recurrence writes and dense cancellation bursts unresolved.

Use ESTIMATED probability 0.56 at R=0.54 for safe conservative replay and 0.44 at R=0.77 when asynchronous integration also preserves batching. The spread comes from implementation success, precision choices and workload pressure; it is not an invented grader-noise measurement. ESTIMATED single=0.56×0.54+0.44×0.77=0.64, range 0.54–0.77. ESTIMATED bo4=0.54×0.56^4+0.77×(1−0.56^4)=0.75; pass@4=1−0.56^4=0.90 with p=0.44; ub95=0.77. The lower forecast than the screen reflects documented integration hazards and unproven output parity. Independent attempt arithmetic and the provisional score scale remain assumptions.

## 4A. Demonstrated capability and subfield SOTA
ReplaySSM is the closest located serving SOTA for this representation: its vLLM implementation improves standard and speculative hybrid decoding at meaningful batch/model scale. HybridSpec provides a newer accepted-state reconstruction comparator. They anchor strong native-throughput floors, not an exact cancellation-safe ceiling: the author must demonstrate remaining throughput at fixed state bytes and eager parity before assigning R≈1.

Singularity-Bench reports Opus 5.5/Claude Code exceeding baseline serving income by 40.8% after twelve hours on four GB300s. That hybrid engine passes completion/answer-accuracy gates, without proving equality after adversarial cancellations. SWE-Serve's mini-SWE-agent runs Opus 5 and GPT-5.6 Sol on CPU or an H100 for at most 210 minutes; each reaches 75.5% mean feature pass@1. Its recurrent-state tasks are pertinent, but the paper does not isolate this cancellation-throughput endpoint. These are neighboring published capabilities, distinct from forecast audit rewards.

KNOWN-RECIPE is buffered recurrent replay plus ownership fencing. The specific AGENT-DEMONSTRATED gap is unaided verification of the exact eager lifecycle under the memory limit, so attack_basis=LITERATURE-ONLY for the complete combined attack. This makes the verdict assumption-dependent even though the central representation is unusually well supported.

ANCHORED ESTIMATED R∼U[0.41,0.69] discounts section 4's optimized mode for that gap. ESTIMATED single=0.55, range 0.41–0.69; bo4=0.41+0.28×4/5=0.63; p=(0.69−0.60)/0.28 gives pass@4=1−(1−p)^4=0.79; ub95=0.41+0.95×0.28=0.68. The smooth range reflects different safe batching/replay compromises. No public pass rate is being used as a reward probability, and no scaling fit establishes this upper percentile.

## 5. Verdict under the kill lines
Both section 4 and ANCHORED verdicts are CUT; UNCHANGED. Anchored ESTIMATED pass@4 exceeds its boundary by 0.29 and bo4 by 0.03, with pass4>0.50 binding. ReplaySSM and HybridSpec eliminate the premise that conventional exactness requires a full state copy per draft token. Whole-engine agent results make integration credible, while rounding and restore failures justify a much lower forecast than the original 0.82. The tail estimate, and thus this kill, still rests on transfer assumptions.

## 6. Redesign
Cause (a), established recurrent serving stack; REDESIGNABLE. Change the target to choosing per-layer state representation and commit placement across a real heterogeneous hybrid model. Disclose each recurrence and its eager arithmetic, including layers where accepted-state reconstruction is cheap and layers where replay or buffering dominates. Long shared sessions, asynchronous cancellation and slot migration create coupled state-memory and scheduling choices; dev must exhibit the same interactions.

Grade later-request throughput with exact output agreement and a complete state-byte ledger. Include ReplaySSM, HybridSpec-style target-cost adaptation, epoch ownership and a tuned uniform checkpoint policy as one combined floor. A feasible reference must beat this by assigning different commit/replay strategies to layers according to measured write traffic and restoration demand, with an ablation showing the coupling matters. Never tighten the copy cap merely until ordinary methods cannot run. This targets deployment of mixed recurrent architectures that frontier labs already serve.

The strongest redesigned attack profiles layers and searches a cost-aware checkpoint policy with migration fences. Basis LITERATURE-ONLY. ESTIMATED outcomes 0.32/0.58/0.66 with probabilities 0.80/0.17/0.03 represent ordinary profiling, good coupled placement and rare near-complete tuning. ESTIMATED single=0.80×0.32+0.17×0.58+0.03×0.66=0.37. ESTIMATED bo4=0.32×0.80^4+0.58×(0.97^4−0.80^4)+0.66×(1−0.97^4)=0.48; pass@4=1−0.97^4=0.11; ub95=0.58 because cumulative mass there is 0.97. A general cost model could raise the upper regime's frequency and erase resistance.

Decisive-check cost ESTIMATED 72 H100 GPU-h: an 8B hybrid target, four implementation arms, three cancellation/migration histories, three hours on one H100 per replay gives 36. Independent eager truth costs 12, state-cap sweeps 12 and warm/cold lifecycle repeats 12: 4×3×3×1+12+12+12=72. No learner training is needed; model compatibility and stronger-control feasibility are prerequisites.

## 7. Measurement status
Rollouts UNMEASURED (planned: cold engines followed through cancellation, migration and slot reassignment). Grader noise UNMEASURED (planned: identical event schedules with repeated warmed timing). Score ladder UNMEASURED (planned: unsafe starter, eager snapshots, bounded buffers, buffered replay and layer-adaptive exact runtime).

## Audit record
id: C030
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.82
old_bo4: 0.89
old_pass4: 0.98
old_ub95: 0.98
new_single: 0.64
new_single_range: 0.54-0.77
new_bo4: 0.75
new_pass4: 0.90
new_ub95: 0.77
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize layer-specific exact recurrent state representation and commit placement jointly with cancellation and migration demand.
redesign_single: 0.37
redesign_bo4: 0.48
redesign_pass4: 0.11
redesign_ub95: 0.58
redesign_gpuh: 72
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench, Opus 5.5/Claude Code, 2026; SWE-Serve, Opus 5 and GPT-5.6 Sol/mini-SWE-agent, 2026
gap_to_attack: eager-output parity after asynchronous cancellation and state reuse under a fixed copy budget
subfield_sota_ref: buffered hybrid serving ReplaySSM 2026; accepted-state reconstruction HybridSpec 2026
anchored_single: 0.55
anchored_bo4: 0.63
anchored_pass4: 0.79
anchored_ub95: 0.68
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
