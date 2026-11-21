# C074 — Partial rotary embeddings with multimodal position semantics — screen audit

## 1. What the screen claimed
The proposed attack repaired channel parity, specialized axis ranges, cached phases and jointly tuned batching and compilation. The screen's ESTIMATED single/bo4/pass4/ub95 were 0.79/0.88/0.97/0.97, producing CUT, category SYS, on presumed gains from explicit channel maps and compiler specialization.

The screen cited these URLs, all fetched now:
- Qwen2-VL implementation — Hugging Face, 2026 accessed version — https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen2_vl/modeling_qwen2_vl.py
- Qwen2-VL — Peng Wang et al., 2024 — https://arxiv.org/abs/2409.12191
- Just-in-time compilation — JAX authors, 2026 accessed documentation — https://docs.jax.dev/en/latest/jit-compilation.html

## 2. Evidence audit
M-RoPE implementation evidence supports allocating phases across axes, and JAX documents specialization. It does not demonstrate profitable partial-factor specialization across this workload's backward path, cache turnover and long mixed sequences. Numerical parity also cannot create an additional learning benefit at equal updates; it mainly prevents invalid execution.

Grade: PARTIAL. Correct reference transplantation is credible, but complete cost savings and agent execution were extrapolated. The original card leaves ambiguous whether changing positional representations is legal alongside parity with a fixed reference; those choices define materially different tasks.

## 3. Research done now
- partial_rotary_factor is ignored when use_mrope is true — AI-Hypercomputer/maxtext, 2026 — https://github.com/AI-Hypercomputer/maxtext/issues/4616 — fetched — Confirms the concrete channel-range defect; fixing it belongs in the floor rather than earning a research windfall.
- Revisiting Multimodal Positional Encoding in Vision-Language Models — Jie Huang et al., 2025, revised 2026 — https://arxiv.org/abs/2510.23095 — fetched — MHRoPE and MRoPE-I report benchmark improvements, strengthening a positional-representation attack if the submission interface permits it.
- RIG-RoPE: Relation-Stratified Multimodal Attention with Instance-Local Rotary Geometry and Representation-Aware Traversal Coordinates — Donggen Li, 2026 — https://arxiv.org/abs/2608.05154 — fetched — The matched Qwen2-VL-2B experiment is inference-only invariance evidence, not proof of improved training efficiency; this narrows the seemingly strongest recent lead.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — H100 profiler search exceeds torch.compile on many forward kernels, increasing the local-fusion threat without demonstrating multimodal gradient validation.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Opus 5.5/Claude Code beats an OLMo-2 pretraining baseline within twelve hours on four GB300s; it does not test partial multimodal rotary semantics.

The search explicitly included recent multimodal position variants and timed agent systems research. No source demonstrated this complete partial-factor optimization campaign.

## 4. Re-estimated attack
Every probability, reward allocation, interval and compute forecast below is ESTIMATED. Above a corrected compiled floor, phase/layout fusion could plausibly capture 0.24 reward, cache/specialization selection 0.18, and mixed-length scheduling another 0.15. Their 0.57 total is conditional on a useful rotary-related share of step time; no published kernel ratio determines that share here.

Model the recipe's outcome as 0.38/0.56/0.72 with probabilities 0.20/0.50/0.30. Recompilation-heavy schedules produce the low outcome; a stable profitable fusion produces the upper outcome. Single = 0.076+0.280+0.216 = 0.57, range 0.38–0.72. Expected max4 = 0.72−0.16×0.70^4−0.18×0.20^4 = 0.68. Since only the upper atom reaches 0.60, pass4 = 1−0.70^4 = 0.76, and ub95 = 0.72. The smaller scores versus the screen remove repair credit and recognize Amdahl limits and compile costs, rather than assuming full specialized-kernel speed reaches the complete trainer.

## 4A. Demonstrated capability and subfield SOTA
The closest verified positional SOTA comparison is Huang et al.'s MHRoPE/MRoPE-I benchmark improvement over prior variants; Li's newer work adds a narrower invariance demonstration. Neither establishes a global best time-to-quality solution. A defensible R≈1 requires the best independently validated exact partial-rotation control, or a separately specified learned-position control, with native cost and accuracy reported before normalization.

KernelAgent supplies a profiler/orchestrator scaffold and reported 1.56× forward-kernel advantage on H100; the fetched account omits backbone and elapsed campaign time. Its gap is multimodal backward correctness plus end-to-end useful work. Singularity-Bench's Opus 5.5/Claude Code pretrainer attained perplexity 12.77 under the stated four-GB300/twelve-hour setup. That demonstrates substantial systems integration, but on text pretraining rather than an axis-sensitive parity constraint.

KNOWN-RECIPE includes phase partitioning, fusion and established positional designs. AGENT-DEMONSTRATED coverage does not include their card-specific integration. Basis=LITERATURE-ONLY: within twelve hours an agent must locate the profitable granularity, amortize compilation and validate long-interleaving updates. Anchored ESTIMATED outcomes 0.25/0.47/0.65 have probabilities 0.20/0.66/0.14. Single = 0.45, range 0.25–0.65; bo4 = 0.65−0.18×0.86^4−0.22×0.20^4 = 0.55; pass4 = 1−0.86^4 = 0.45; ub95 = 0.65. These transfer probabilities remain assumptions; no matching agent success frequency was measured.

## 5. Verdict under the kill lines
Section 4 yields CUT through bo4 and pass4. The headline ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL: bo4 is only ESTIMATED 0.05 below its boundary before rounding, and pass4 is approximately 0.05 below its line. Fetched agent evidence supports integration ability without proving reliable axis-specific gains, so the old high score is unwarranted. Conditional retention also requires resolving the fixed-parity versus learned-position ambiguity.

## 6. Redesign
Class a; REDESIGNABLE. Freeze the positional map and include the fully repaired, compiled, cache-tuned implementation in the starting assets. Grade complete training on disclosed compositions of image crops, video time coordinates and partial channel maps where phase generation, layout conversion and attention scheduling interact. Supply representative compositions and profiling tools; vary actual dependency composition rather than introducing hidden semantics. Require a demonstrated profitable reference over this complete floor before building.

The strongest re-attack remains parity transplantation plus cached factors, fusion and schedule search. It now earns only residual interaction gains. ESTIMATED LITERATURE-ONLY re-attack atoms 0.20/0.43/0.61, probabilities 0.25/0.67/0.08, give single 0.39, bo4 = 0.61−0.18×0.92^4−0.23×0.25^4 = 0.48, pass4 = 1−0.92^4 = 0.28, ub95 0.61. This is a conditional research design, not demonstrated reserve. Risks are a negligible positional cost share or universal compiler fusion; either would kill native headroom. Decisive-check GPU-h ESTIMATED: 3B vision-language subject, four arms×three seeds×eight hours×four H100 = 384; long-context evaluation and parity overhead 64; total 448 H100-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: timed partial-rotation integrations). Grader noise UNMEASURED (planned: repeated axis-task learning and synchronized full-step measurements). Score ladder UNMEASURED (planned: repaired reference, compiled cache path, fused schedule, independent stronger control).

## Audit record
id: C074
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.79
old_bo4: 0.88
old_pass4: 0.97
old_ub95: 0.97
new_single: 0.57
new_single_range: 0.38-0.72
new_bo4: 0.68
new_pass4: 0.76
new_ub95: 0.72
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Freeze exact positional semantics and establish interaction gains beyond a complete corrected compiler and cache baseline.
redesign_single: 0.39
redesign_bo4: 0.48
redesign_pass4: 0.28
redesign_ub95: 0.61
redesign_gpuh: 448
attack_basis: LITERATURE-ONLY
demonstrated_ref: KernelAgent, unspecified backbone, 2026; Singularity-Bench, Opus 5.5 Claude Code, 2026
gap_to_attack: partial multimodal rotary backward parity and amortized training benefit
subfield_sota_ref: MHRoPE and MRoPE-I, Huang et al., 2025 revised 2026
anchored_single: 0.45
anchored_bo4: 0.55
anchored_pass4: 0.45
anchored_ub95: 0.65
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
