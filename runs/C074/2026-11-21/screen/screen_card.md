# C074 — Partial rotary embeddings with multimodal position semantics — saturation screen
## 1. What the grader actually rewards
The submitted kernel must match a declared multimodal partial-rotation reference in outputs and gradients, then deliver better spatial/temporal learning and held-out loss per complete cost. Text-only parity or rotating the unassigned channels is insufficient. R≈0 is the complete correct positional implementation floor and R≈1 the attainable faster learning control; all numerical predictions below are ESTIMATED because the mixed-axis learning and timing anchors are UNMEASURED.

Specialized mixed-axis execution would occupy nominal ESTIMATED reference R=0.60, requiring a training-cost benefit beyond the fully corrected positional implementation.

## 2. Strongest lawful combined attack
Write the rotation as an explicit channel partition: each assigned range receives its declared temporal, horizontal or vertical phase, and untouched channels pass through exactly. Verify position construction, channel ordering, partial dimension rounding and gradient flow against the independent reference. Public [Qwen2-VL implementation code](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen2_vl/modeling_qwen2_vl.py) provides a concrete multimodal rotary starting point, with the model's perception design described in [Qwen2-VL](https://arxiv.org/abs/2409.12191). It does not establish that any arbitrary partial factor is natively supported without adaptation.

Specialize the declared axis/channel maps at compile time, fuse phase application with adjacent tensor layout work where lawful, and reuse rotation factors by actual positions rather than modality labels alone. [JAX compilation guidance](https://docs.jax.dev/en/latest/jit-compilation.html) supports specializing stable arguments and warns about recompilation; compile and warmup costs remain charged. Tune specialization granularity, phase-cache policy and mixed-modality batching jointly, validating long interleavings and real training updates on the same path.

ESTIMATED single-run R=0.79, range 0.57–0.92; ESTIMATED best-of-4=0.88; ESTIMATED pass@4 at R≥0.60=0.97; ESTIMATED upper-95% projection=0.97. These forecasts describe stronger transferred integration than a frozen calibration floor. The residual is axis-layout overhead and a potentially narrow kernel share of the complete step. Once outputs and gradients match, the specialized implementation should not mysteriously need a new learning rule at the same updates; most learning benefit comes from executing more correct work. If positional redesign is also allowed, its objective and capacity must be specified separately rather than smuggled into a parity task.

## 3. Other routes
A faithful complete reference with ordinary compilation is the strongest single standard recipe: ESTIMATED R=0.66, range 0.42–0.84. It may already restore the long-context behavior lost through the ignored partial factor.

A sweep over channel-slice fusion, factor-cache granularity, compiler specializations and batch composition yields ESTIMATED R=0.75, range 0.52–0.90. Short numerical probes filter invalid kernels before expensive training. An unfused reference is a lawful final artifact if the expensive part of the workload lies elsewhere; claiming a larger isolated rotary speedup would not change its complete utility.

## 4. What would lower lawful saturation
Decide whether the task is exact kernel optimization or learning a better positional representation. For the former, establish a meaningful native time-to-quality reserve over a tuned reference across unseen axis-dependency compositions. For the latter, publish a bounded representation-change interface and fresh identifiable visual-temporal relations. ESTIMATED attack after the stronger exact-kernel specification is 0.55–0.71, so survival remains doubtful. ESTIMATED authoring is 10–16 person-days and ESTIMATED 672 H100-h for axis-sensitive learning pilots; shape variety alone supplies no new scientific barrier.

## 5. Decisive-check GPU-h re-estimate
Old amount: ESTIMATED 14 GPU-h. New ESTIMATED 672 H100-GPU-h assumes an ESTIMATED 3B vision-language subject, ESTIMATED 4 positional implementations×3 seeds×12 cluster-hours×4 H100s=576 for mixed-modality training. Long-interleaving evaluation and spatial/temporal checks add ESTIMATED 72; phase-gradient probes, compilation and cache profiling add ESTIMATED 24. Total ESTIMATED 576+72+24=672. The vision encoder and image/video token processing are included in the training envelope, not treated as free text tokens. The old estimate can establish a local partial-rotation mismatch, but not show useful axis-sensitive learning beyond the repaired reference.

## 6. Duplicate check
T11: WEAK after reading its counterfactual visual-learning packet; spatial and temporal endpoints overlap, while data/objective interventions differ from positional kernel parity. 05B: MODERATE from its exact-graph source because the proposed useful gain is faster correct updates, although multimodal axis handling is a narrower target. 04B: MODERATE if phase precision is part of the intervention, but its activation-drift policy is not identical to channel-selective rotary execution.

## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds the binding line by 0.28 and ESTIMATED single-run reward exceeds its line by 0.09. Correct reference transplantation, explicit channel maps and ordinary compiler specialization offer a strong lawful route, while the claimed additional trainability residual remains undefined.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent positional-kernel searches with fresh multimodal interleavings); grader noise UNMEASURED (planned: repeated fixed-kernel training and axis-sensitive scoring); score ladder UNMEASURED (planned: ignored-factor negative, correct reference, specialized slices, fused/cache-tuned path and stronger attainable control).

## Screen record
id: C074
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.79
attack_single_range: 0.57-0.92
bo4_est: 0.88
pass4_est: 0.97
ub95_est: 0.97
gpuh_old: 14
gpuh_new_est: 672
duplicate_of: T11 WEAK; 05B MODERATE; 04B MODERATE
kill_reason: explicit channel parity and compiler specialization likely capture useful gain
souping_flag: no
