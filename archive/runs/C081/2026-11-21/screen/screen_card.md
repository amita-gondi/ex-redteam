# C081 — Masked-input regularization after repetitions stop being exchangeable — saturation screen
## 1. What the grader actually rewards
Utility is clean private language-model loss per raw byte after equal total training FLOPs, including auxiliary masked passes. R≈0 represents the complete published regularization floor, and R≈1 requires a stronger attainable objective that preserves rare condition-bearing facts while exploiting redundant surfaces. The inherited no-op is ESTIMATED R=0.00 and the intended conditional-masking reference is ESTIMATED R=0.60; lower masked-training loss alone earns nothing.
## 2. Strongest lawful combined attack
Reproduce masked-input regularization and strong weight decay from the verified [data-constrained pretraining paper](https://arxiv.org/abs/2606.06888), using its [official implementation](https://github.com/yixinw-lab/dc_pretrain). Add duplicate clustering, cluster-frequency features and development ablations separating fact reuse from surface-template reuse. Fit a small conditional policy for masking probability, auxiliary-loss weight and schedule stage; use [RegMix](https://arxiv.org/abs/2407.01492)-style proxy regression to prioritize promising configurations. RegMix supports the proxy-selection component, not a claim that it already solves semantic repetition.

The combined attack can recognize exact duplicates and tune ordinary corruption strength. However, a repeated surface may encode a new conditional relation, while different surfaces may repeat a fact; input frequency does not identify whether masking removes the only useful condition. Factorial development probes help estimate that distinction without furnishing every private dependency. ESTIMATED single-run R=0.43, range 0.24–0.58; ESTIMATED best-of-4=0.52; ESTIMATED pass@4 at R≥0.60=0.16; ESTIMATED projected upper-95% bound=0.68. These forecasts assume the promised independently authored fact/template mechanisms are implemented and the full public recipe is genuinely in the floor. The remaining reward is better allocation of corruption across condition-dependent information, rather than a missing optimizer flag.
## 3. Other routes
- The complete MIR-plus-weight-decay recipe, retuned for the provided FLOP envelope, is ESTIMATED R=0.24, range 0.08–0.43. Its general regularization benefit is already acknowledged, so the screen does not give free reward merely for reproducing the paper.
- A multi-fidelity sweep over mask probability, auxiliary weight, decay and training stage is ESTIMATED R=0.38, range 0.18–0.56. It can approximate a good average policy but lacks a representation of which condition a corruption destroys.
- Frequency-aware deduplication followed by clean training is ESTIMATED R=0.30, range 0.10–0.50. It avoids harmful masks but may discard meaningful evidence whenever template repetition is mistaken for factual duplication.
## 4. What would lower lawful saturation
Strengthen the already proposed factorial generator with independently composed conditional relations whose surface multiplicity and factual redundancy vary separately, and require clean loss on every condition-support stratum. Supply matching intervention probes during development. ESTIMATED combined reward could move to 0.33–0.44, at ESTIMATED cost of two author-weeks plus 96 H100 GPU-h for generator and reference checks. The important constraint is observable, learnable distinction; a secret semantic label unavailable from the training material would create an identification failure. Keep raw-byte denominators frozen and count every auxiliary forward/backward pass so allocating more compute cannot masquerade as a better objective.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 14 GPU-h. New ESTIMATED total: 408 H100 GPU-h. Use ESTIMATED 125M proxy models and 1B decisive subjects, with ESTIMATED 4 full recipes × 2 training seeds × 42 H100-hours = 336 GPU-h for roughly ESTIMATED 3B tokens per full run; add ESTIMATED 8 proxy arms × 1 seed × 3 hours = 24 GPU-h and ESTIMATED 48 GPU-h for clean evaluations, auxiliary-pass overhead and checkpoint replay. The full-run estimate corresponds to approximately ESTIMATED 120 TFLOP/s effective training throughput and must be profiled later. The old budget cannot establish a persistent regularization ranking after billions of repeated exposures; a tiny quick run could test code only.
## 6. Duplicate check
Catalog T02 and FIX T02 — MODERATE after reading both pretraining descriptions and the FIX saturation dossier. They share data-constrained loss and recipe selection, but their packing/exposure/optimizer-state intervention differs from this masking policy under independently varied semantic repetition. No existing task inspected establishes the same intervention paired with the same conditional-loss target.
## 7. Verdict
PASS-SCREEN under the specified factorial workload. ESTIMATED margins are 0.27 for the typical single-run point, 0.08 for best-of-4, 0.34 for pass@4 and 0.07 for the projected upper bound. This is a desk prioritization judgment; absent measured anchors and attainable reserve, it grants no empirical acceptance.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete combined masking-policy attempts); grader noise UNMEASURED (planned: independent retraining and clean byte-loss repeats); score ladder UNMEASURED (planned: no-op, full MIR, frequency policy, conditional reference and stronger control).
## Screen record
id: C081
verdict: PASS-SCREEN
binding_line: none
attack_single_est: 0.43
attack_single_range: 0.24-0.58
bo4_est: 0.52
pass4_est: 0.16
ub95_est: 0.68
gpuh_old: 14
gpuh_new_est: 408
duplicate_of: catalog T02 MODERATE; FIX T02 MODERATE
kill_reason: none
souping_flag: no
