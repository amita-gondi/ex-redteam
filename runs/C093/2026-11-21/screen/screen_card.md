# C093 — Spend late research budget on complementary compression failures — saturation screen
## 1. What the grader actually rewards
The chosen program must deploy one compressed model with high private executable utility, counting all stored tensors and every recovery branch used during research. R≈0 is a competent joint compression/recovery floor, and R≈1 is an attainable better quality/bytes/recovery-cost point under the same limits. The unmodified campaign is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; individual component accuracy does not establish the utility of the jointly transformed delivered model.
## 2. Strongest lawful combined attack
Apply sequential transformations to the same immutable starting model: quantization using [GPTQ](https://arxiv.org/abs/2210.17323), pruning using [SparseGPT](https://arxiv.org/abs/2301.00774) where its deployed sparsity is supported, and single-teacher recovery following [Minitron](https://arxiv.org/abs/2408.11796). Compare both transformation orders, measure residual activation/error covariance, and reserve longer recovery for structurally different finalists rather than pruning every initially worse candidate. The verified [NVIDIA pruning guide](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/pruning/README.md) explicitly recommends recovery of top candidate architectures before selection. No independently trained weights are combined at any stage.

This is substantially stronger than greedy individually safe compression. A frontier agent can retain representatives from diverse error profiles and use partial recovery curves to decide which deserve continued training. ESTIMATED single-run R=0.62, range 0.39–0.81; ESTIMATED oracle best-of-4=0.73; ESTIMATED pass@4 at R≥0.60=0.82; ESTIMATED projected upper-95% bound=0.90. Residual reward concerns unusually delayed representation repair and truly complementary errors whose recoverability is invisible to cheap probes. The card does not specify a novel observable predictor or a different intervention; it asks for joint compression search and recovery that are already legal complete methods in the existing compression task.
## 3. Other routes
- Structured pruning followed by ordinary single-teacher distillation is ESTIMATED R=0.51, range 0.29–0.73. It can exploit compression-axis interactions without a bespoke late-budget reasoning policy.
- Joint sweep over quantization, pruning order, recovery duration and distillation weights with finalist continuation is ESTIMATED R=0.59, range 0.35–0.80. Charge the losing branches and do not choose retrospectively from private outcomes.
- A conservative quantization-only conversion is ESTIMATED R=0.40, range 0.18–0.65. It sacrifices possible compression but can dominate if the byte budget lies in a near-lossless regime, which would also destroy native research reserve.
## 4. What would lower lawful saturation
Require a reusable measurement policy that predicts delayed recoverability across unseen compression mechanisms, then grade its selections through live recovery rather than accepting one final compressed model. Include full joint-search and multi-fidelity recovery in the floor. ESTIMATED attack might fall to R=0.41–0.55 if new recoverability interactions are identifiable. ESTIMATED authoring cost is several weeks and ESTIMATED additional calibration is 384 H100 GPU-h. That would materially change the intervention and help address the duplicate; simply asking the same converter to spend its budget more thoughtfully would not. Training-time information and total deployed memory must remain matched.
## 5. Decisive-check GPU-h re-estimate
Old card value: ESTIMATED 16 GPU-h. New ESTIMATED total: 720 H100 GPU-h. Assume an ESTIMATED 8B teacher and compressed ESTIMATED 4B students: ESTIMATED 4 conversion/recovery programs × 2 seeds × 4 H100s × 18 hours = 576 GPU-h, plus ESTIMATED 96 GPU-h for short rejected branches and conversion/calibration and ESTIMATED 48 GPU-h for packed deployment and private execution. The per-run envelope includes teacher inference and recovery, not just checkpoint conversion. The original budget cannot distinguish delayed recovery from a misleading initial accuracy drop; that distinction is the entire proposed scientific mechanism.
## 6. Duplicate check
Catalog T21 — STRONG. Its source was opened: the intervention already jointly selects quantization/structured pruning and recovery under actual bytes/runtime, with cross-layer compensation and recovery interaction as difficulty knobs. C093's final-program submission and quality/resource grader coincide with that intervention and target. Late-investment reasoning is a search strategy inside T21, not a separate scientific task as currently specified.
## 7. Verdict
CUT for duplicate, with independent saturation concern. ESTIMATED best-of-4 exceeds its line by 0.13 and ESTIMATED pass@4 exceeds its threshold by 0.32. There is no souping/merging dependency: sequential compression of one model is lawful here, but it does not rescue the duplicate.
## 8. Measurement status
Rollouts UNMEASURED (planned: joint compression plus long-recovery searches); grader noise UNMEASURED (planned: independent recovery seeds and packed deployment repeats); score ladder UNMEASURED (planned: conservative conversion, joint short search, extended finalist recovery and attainable compressed control).
## Screen record
id: C093
verdict: CUT
binding_line: duplicate
attack_single_est: 0.62
attack_single_range: 0.39-0.81
bo4_est: 0.73
pass4_est: 0.82
ub95_est: 0.90
gpuh_old: 16
gpuh_new_est: 720
duplicate_of: catalog T21 STRONG
kill_reason: joint compression and recovery already define T21 intervention and target
souping_flag: no
