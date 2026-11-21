# C077 — Attention composition needs correct log-normalizers too — saturation screen
## 1. What the grader actually rewards
The outcome is throughput of attention partitions whose outputs and normalizers compose into the correct dense result. R≈0 means no useful gain over the competent corrected floor, including a path that computes plausible local vectors but combines them incorrectly; R≈1 means the independently attainable fast exact composition control. Those endpoints are uncalibrated: for this screen the no-op is ESTIMATED R=0.00 and the intended reference is ESTIMATED R=0.60, rather than treating percentage speedup as reward.
## 2. Strongest lawful combined attack
Start with the publicly documented head/sequence layout correction in [FlashAttention issue 3039](https://github.com/Dao-AILab/flash-attention/issues/3039). Replace the composition path with the sufficient-statistic reduction exposed by [FlashInfer cascade](https://docs.flashinfer.ai/api/cascade.html), then specialize contiguous head groups, fuse the final reduction and select partition counts on representative development shapes. This combines an already localized correctness repair with an existing implementation of the mathematical operation being optimized. Attention-state reduction here combines activation statistics; it has no model-weight combination dependency.

The researcher would first check output and normalizer agreement independently, including empty partitions, then profile the exact composed path and retain a safe fallback for rare layouts. Most tuning dimensions are layout, launch geometry and partition count, so repeated development measurements can explore them without training a subject model. The screen forecast is ESTIMATED single-run R=0.80, range 0.65–0.93; ESTIMATED oracle best-of-4=0.88; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% bound=0.97. These are judgmental planning quantities, not fitted statistics. The residual is irregular-page traffic and launch overhead: the stock reducer may materialize statistics that a purpose-built producer/consumer pipeline could keep local. Nothing in the card establishes that this residual occupies a large reward interval after the whole-stack replacement is floored.
## 3. Other routes
- A single corrected split-attention implementation, with its existing stable softmax reduction, is ESTIMATED R=0.70, range 0.50–0.86. Fixing the layout can recover the entire correctness deficit before any original algorithm is needed.
- Enumeration over split count, head grouping and reduction block size, selecting by complete-path throughput rather than local kernel time, is ESTIMATED R=0.77, range 0.58–0.91. The finite dispatch space fits the stated research budget more credibly than an unspecified novel attention algorithm.
- Dense fallback on troublesome partitions is lawful if all its cost is counted: ESTIMATED R=0.39, range 0.18–0.60. It preserves coverage but sacrifices the reason to partition.
## 4. What would lower lawful saturation
Freeze the repaired FlashAttention plus FlashInfer composition stack as a measured floor and introduce independently constructed graph-dependent partition reuse, where materializing normalizers changes later cache residency. Preserve identical development access to those interactions. ESTIMATED attack reward could drop to 0.43–0.57, but only if a same-budget control demonstrates a real producer/consumer advantage; renormalizing a tiny remaining speed difference cannot qualify. ESTIMATED authoring cost is several engineer-days and ESTIMATED additional validation cost is 12 H100 GPU-h. Adding more head counts alone is unlikely to alter the verdict.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 6 GPU-h. New ESTIMATED total: 12 H100 GPU-h. No trainable model is required: use fixed attention tensors and a frozen ESTIMATED 1B decoder only for end-to-end replay. Budget ESTIMATED 4 implementations × 3 independent timing seeds × 0.5 H100-hours = 6 GPU-h, plus ESTIMATED 3 hours for compile/warmup and dense correctness comparisons and ESTIMATED 3 hours for composed-graph replay. The old allocation could falsify a transposition fix but underfunds competing backends and repeatable timing. This is a narrow decisive check, not a full saturation panel.
## 6. Duplicate check
v3 05A — MODERATE. Its source in `task_design_v3_codex/05_exact_systems.md` optimizes exact serving capacity across sessions and shapes; this card restricts the intervention to attention sufficient statistics and scores their composed path. The overlap is substantial systems work, but the intervention and grader target are not identical enough for a strong duplicate finding.
## 7. Verdict
CUT. The binding single-run line is exceeded by an ESTIMATED 0.10, and ESTIMATED best-of-4 exceeds its line by 0.28. A public repair followed by an available reduction backend plausibly captures most attainable benefit; fresh page tables do not defeat that recipe.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget corrected-backend attempts); grader noise UNMEASURED (planned: repeated complete-path timing on fixed artifacts); score ladder UNMEASURED (planned: no-op, corrected stock, optimized reducer and attainable control in native throughput).
## Screen record
id: C077
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.80
attack_single_range: 0.65-0.93
bo4_est: 0.88
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 6
gpuh_new_est: 12
duplicate_of: v3 05A MODERATE
kill_reason: public layout repair plus existing exact composition backend
souping_flag: no
