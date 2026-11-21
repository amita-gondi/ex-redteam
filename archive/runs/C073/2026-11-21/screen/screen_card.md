# C073 — Packed attention whose speedup survives semantic isolation — saturation screen
## 1. What the grader actually rewards
Useful speed means reaching private loss sooner while preserving each packed segment's outputs, gradients and update semantics relative to unpacked execution. Neighboring-sequence perturbations must not change an isolated segment, and the same backend/metadata must pass correctness and timing. R≈0 is the competent isolated-packing floor and R≈1 the attainable exact training-speed control; every numeric forecast below is ESTIMATED because measured loss/time anchors are absent.

The optimized isolated graph has a nominal ESTIMATED R=0.60 author-reference target whose advantage beyond supported variable-length attention is still unknown.

## 2. Strongest lawful combined attack
Replace the defective lowering path with a supported variable-length attention backend that consumes explicit cumulative sequence lengths. The public [FlashAttention variable-length interface](https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/flash_attn_interface.py) exposes separate query/key boundaries and maximum lengths, while [FlashAttention-2](https://arxiv.org/abs/2307.08691) supplies an established efficient attention algorithm. Porting that approach to the pinned framework may take work, but the card permits a public boundary-aware backend or fallback, so retaining a known defective backend is not a lawful restriction to assume.

Combine length-aware bin packing, segment-local positions, exact completion/loss masks and fused attention for supported layouts. Bucket unusual layouts into a safe isolated path instead of disabling packing globally. Validate neighboring-segment perturbations in forward and backward, then compare full optimizer updates. Autotune packing bins, backend thresholds and recomputation jointly on total time-to-loss, including conversion and compile costs. This attacks both semantic leakage and the claimed waste from the blunt no-packing baseline.

ESTIMATED single-run R=0.86, range 0.68–0.95; ESTIMATED best-of-4=0.92; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% score=0.99. These are subjective estimates for stronger transferred integration than a frozen floor, not new kernel measurements. The residual is irregular block structure and dispatch overhead. For ordinary independent packed documents, however, variable-length attention already represents precisely the desired semantics. Extra sequence lengths do not make that dependency map scientifically novel, and including the full mature stack in the floor may leave no native range.

## 3. Other routes
A supported isolated variable-length attention implementation with ordinary greedy packing is the strongest single standard recipe: ESTIMATED R=0.78, range 0.56–0.92. It should be compared with the repaired starting backend, rather than claiming all leakage-removal cost against an unpacked baseline.

A lawful sweep over segment bins, padding boundaries, fused versus safe fallback, and activation recomputation yields ESTIMATED R=0.83, range 0.62–0.94. Its validity filter uses both gradient and forward isolation. A candidate-aware separate safe validation pass is an implementation threat, so the forecast assumes trusted captures bind checks to the actual timed path.

## 4. What would lower lawful saturation
Move beyond simple independent segments to disclosed, useful block-dependency patterns that available variable-length kernels cannot represent efficiently, while maintaining exact semantic truth and an executable faster reference. Hold out dependency compositions, with matched development examples and full compile accounting. ESTIMATED revised attack R=0.55–0.71, still unsafe at the upper end. ESTIMATED preparation is 8–12 person-days plus ESTIMATED 312 H100-h for a training-scale pilot. A larger shape zoo without a different graph structure would mostly expand an autotuning exercise.

## 5. Decisive-check GPU-h re-estimate
Old budget: ESTIMATED 12 GPU-h. New ESTIMATED 312 H100-GPU-h assumes an ESTIMATED 1B decoder trained on ESTIMATED 2B tokens, ESTIMATED 4 packed-backend arms×3 seeds×5 cluster-hours×4 H100s=240. Trusted forward/backward isolation probes and compile/packing profiles add ESTIMATED 24; full private-loss evaluation and repeated endpoint timing add ESTIMATED 48. Total ESTIMATED 240+24+48=312. The model's approximate training work is ESTIMATED 12×10^18 operations per run before attention overhead, making a multi-device pilot reasonable. The old estimate is a kernel-semantic smoke test, not a demonstrated time-to-quality study.

## 6. Duplicate check
05B: STRONG after reading its source: it submits a replacement fixed training graph and scores exact valid updates across sequence lengths while preserving loss reduction and state, with FlashAttention already an explicit baseline. Here the intervention remains an exact packed-attention graph replacement and the target remains valid training speed; centering a known leaky backend adds an incident, not a distinct scientific outcome. 04B: WEAK because numerical fidelity overlaps but the intervention is precision allocation instead.

## 7. Verdict
CUT, binding duplicate. C073 specializes the same exact-graph intervention and speed target already present in 05B without an additional nonstandard dependency structure. Independently, ESTIMATED single-run reward exceeds its line by 0.16 and best-of-4 exceeds its line by 0.32, so removing the duplicate concern would not rescue saturation.

## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget isolated-packing integrations on fresh segment structures); grader noise UNMEASURED (planned: repeated exact-kernel training and warmed timing for fixed graphs); score ladder UNMEASURED (planned: leaky negative, unpacked reference, corrected varlen backend, tuned packing and stronger exact graph).

## Screen record
id: C073
verdict: CUT
binding_line: duplicate
attack_single_est: 0.86
attack_single_range: 0.68-0.95
bo4_est: 0.92
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 12
gpuh_new_est: 312
duplicate_of: 05B STRONG; 04B WEAK
kill_reason: exact packed graph optimization repeats 05B and mature varlen recipes saturate
souping_flag: no
