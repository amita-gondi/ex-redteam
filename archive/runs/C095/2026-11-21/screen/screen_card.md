# C095 — Find an optimizer coordinate system beyond standard recipe sweeps — saturation screen
## 1. What the grader actually rewards
The submitted optimizer must lower private loss after domain reuse while respecting model capacity, persistent optimizer bytes and complete update FLOPs. R≈0 is the best matched-state known optimizer, and R≈1 requires an attainable better coordinate strategy rather than extra trainable capacity. The inherited stalled learner is ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60; equivalent-parameterization experiments diagnose mechanism but do not independently earn reward.
## 2. Strongest lawful combined attack
The strongest baseline must include [SOAP](https://arxiv.org/abs/2409.11321), which already applies Adam in a changing preconditioner eigenbasis, not just AdamW and learning-rate grids. Combine blockwise [Shampoo](https://arxiv.org/abs/1802.09568), low-rank covariance approximations and basis-refresh scheduling with an ordinary orthogonalized-update alternative such as the verified [PyTorch Muon implementation](https://github.com/pytorch/pytorch/blob/main/torch/optim/_muon.py). Select one legal update strategy per parameter group; account for all stored bases, moments and factorization work. This compares optimizer operators without combining independently trained weights.

The agent should detect gradient-subspace drift around domain transitions, refresh or transport moments when needed, and compare transformed-coordinate updates against a matched-byte control. Existing coordinate-aware methods undermine the card's suggestion that standard recipes necessarily share one mistaken basis. ESTIMATED single-run R=0.49, range 0.28–0.66; ESTIMATED best-of-4=0.59; ESTIMATED pass@4 at R≥0.60=0.34; ESTIMATED projected upper-95% bound=0.74. The remaining gap is plausible only when the fixed state/work budget prevents sufficiently frequent or high-rank curvature tracking and the useful feature directions change nontrivially after reuse. Without that resource-sensitive mechanism, a SOAP-style stack could instead cross the kill lines comfortably.
## 3. Other routes
- Matched-budget blockwise SOAP with periodic eigenbasis updates is ESTIMATED R=0.43, range 0.22–0.63. It directly targets the proposed coordinate intervention and therefore belongs in the initial floor.
- Search block size, low-rank dimension, refresh trigger, moment-reset rule and group-specific optimizer assignment: ESTIMATED R=0.47, range 0.25–0.65. Auxiliary decompositions and failed training branches must be charged to avoid an artificial advantage.
- Muon on eligible matrices with AdamW on embeddings and scalars is ESTIMATED R=0.35, range 0.16–0.56. It may improve conditioning cheaply while missing domain-specific moving curvature.
## 4. What would lower lawful saturation
Make the byte/FLOP envelope numerical and require domain relations that move useful directions in ways a matched-budget SOAP/Shampoo/Muon search does not already track. Publish predictive curvature probes and define a trusted bounded coordinate-transform interface that admits legitimate moment transport. This is the exact required design change. ESTIMATED attack could fall to R=0.37–0.50, with ESTIMATED added effort of two optimizer engineer-weeks and ESTIMATED 192 H100 GPU-h for curvature and transition calibration. Prohibiting an existing basis method because it solves the task would be invalid; the author must instead demonstrate a real same-budget control beyond it.
## 5. Decisive-check GPU-h re-estimate
Old allocation: ESTIMATED 18 GPU-h. New ESTIMATED total: 624 H100 GPU-h. Use ESTIMATED 125M proxies and 1B decisive subjects: ESTIMATED 5 known/novel optimizer arms × 2 seeds × 48 H100-hours = 480 GPU-h, plus ESTIMATED 8 proxy configurations × 1 seed × 6 hours = 48 GPU-h and ESTIMATED 96 GPU-h for curvature work, byte-accounting ablations and protected loss evaluation. Full subjects should traverse roughly ESTIMATED several billion tokens across a domain transition. The old allowance is too short to establish optimizer rankings that persist after reuse and after the expensive basis operations are fully counted.
## 6. Duplicate check
Catalog T09 — WEAK after opening its sparse-support specification: that task changes a lifetime coordinate-write support and physical packed execution, whereas C095 changes the representation in which dense legal optimization operates. Catalog T02 — MODERATE because it admits optimizer recipes and shares held-loss improvement, but its defining packing/exposure/history treatment differs. The card's W09 pointer is outside the required existing-task index and is not treated as verified duplicate evidence.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 and upper-95% margins are each only 0.01. Require explicit resource limits, the complete coordinate-aware optimizer floor and a demonstrated moving-curvature mechanism beyond that floor. The promising aspect is constrained representation tracking, not novelty of using a different coordinate basis.
## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget matched-state optimizer searches); grader noise UNMEASURED (planned: independent training and domain-order seeds); score ladder UNMEASURED (planned: AdamW, Muon, blockwise SOAP, proposed transform and attainable matched-resource control).
## Screen record
id: C095
verdict: CONDITIONAL
binding_line: ub95>=0.75
attack_single_est: 0.49
attack_single_range: 0.28-0.66
bo4_est: 0.59
pass4_est: 0.34
ub95_est: 0.74
gpuh_old: 18
gpuh_new_est: 624
duplicate_of: catalog T09 WEAK; catalog T02 MODERATE
kill_reason: coordinate aware public optimizers require explicit resource sensitive residual
souping_flag: no
