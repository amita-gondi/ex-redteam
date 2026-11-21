# C041 — Pretrain with a tokenizer whose byte cost changes — saturation screen
## 1. What the grader actually rewards
The tokenizer is fixed despite the title: the artifact changes multilingual allocation and packing, and the grader evaluates loss per source byte within language strata at metered training FLOPs. Thus a better token-count accounting convention earns reward only when it improves the trained model. ESTIMATED R≈0 is the independently frozen byte-aware allocation floor and ESTIMATED R≈1 an attainable multilingual efficiency policy; the token-balanced starter is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60. Positive attack reward presumes additional transfer from jointly optimizing mixture and physical packing on fresh dialects, not a second reward for the same units correction already included in calibration.
## 2. Strongest lawful combined attack
Measure accepted bytes, token expansion, padding and per-language learning response. Apply byte-balanced sampling, length-aware packing with correct document boundaries, and learning-rate schedules indexed to actual delivered work. Then optimize language weights using [DoReMi](https://arxiv.org/abs/2305.10429) or a [RegMix](https://arxiv.org/abs/2407.01492) response model trained on legal small runs. These methods supply a stronger stack than simply correcting the sampler's units.

Cross mixture weights with sequence-length buckets and accumulation schedules under the full FLOP ledger. Use protected per-stratum development loss to reject policies that win by overserving easy languages, and retest finalists at the actual training horizon. Because the tokenizer never changes, there is no embedding migration or optimizer-state transport problem. Technical dialect shifts alter observable expansion and source response, both inputs that a cost-aware allocation policy can use directly.

ESTIMATED single-run R=0.81, range ESTIMATED 0.55–0.94; ESTIMATED best-of-4=0.88; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% bound=0.98. The estimate assumes most headroom over the token-balanced starter comes from avoiding unintended exposure imbalance and padding waste, with mixture optimization recovering much of the rest. Residual loss is cross-language transfer that proxies predict poorly and long-horizon effects of sequence packing. The card does not instantiate a causal interaction strong enough to show those residuals exceed ordinary response-model tuning.
## 3. Other routes
Byte-balanced sampling with a standard efficient packer reaches ESTIMATED R=0.68, range ESTIMATED 0.42–0.86. This simple control must be measured before funding a novel schedule.

A multi-fidelity search across language temperatures, byte quotas, pack lengths and warmup/decay reaches ESTIMATED R=0.75, range ESTIMATED 0.49–0.91. Selection must compare complete training FLOPs, not equal requested token counts. A metadata-only expansion correction without any learned transfer estimate could score ESTIMATED R=0.59, range ESTIMATED 0.33–0.80. If it matches the reference, the task is chiefly a units repair and should be cut regardless of implementation detail.
## 4. What would lower lawful saturation
Demonstrate a held-out interaction where choosing exposure changes useful sequence length, which then changes cross-language transfer and reverses the best allocation. Keep expansion ratios visible and include the complete byte-aware mixture stack in calibration. ESTIMATED composite R might become 0.49–0.62, costing ESTIMATED four multilingual-research weeks and ESTIMATED 256 H100 GPU-h to establish real learning reversals. New dialect names and tokenization patterns alone do not alter the algorithm. Do not normalize a small residual packing gain into a large reward range without native reserve.
## 5. Decisive-check GPU-h re-estimate
Old figure: ESTIMATED 10 GPU-h. New ESTIMATED 280 H100 GPU-h assumes an ESTIMATED 1B multilingual subject, ESTIMATED four allocation arms and ESTIMATED two training seeds, with ESTIMATED 28 H100-hours per run on an ESTIMATED 1.5B-token continuation: ESTIMATED 4×2×28=224. Smaller mixture/packing proxies cost ESTIMATED 32 GPU-h and complete byte-normalized evaluations cost ESTIMATED 24 GPU-h. The old budget can check byte ledgers and short-run packing, but it cannot resolve cross-language learning after substantial exposure under matched compute.
## 6. Duplicate check
01A: MODERATE, using its read source-distribution policy and downstream utility contract; multilingual byte cost is a narrower resource mechanism rather than stage-quality reversal. Catalog T02: MODERATE, from its inspected allocation/packing continuation statement, though its target is a fixed migrated corpus rather than language-stratified byte loss. No source examined establishes identical intervention and target together.
## 7. Verdict
CUT, binding ESTIMATED best-of-four excess 0.28. The ESTIMATED single-run excess is 0.11. Fixed-tokenizer cost accounting plus standard data-mixture optimization is a plausible near-complete solution.
## 8. Measurement status
Rollouts UNMEASURED (planned: allocation searches on independent dialect mixtures). Grader noise UNMEASURED (planned: repeated complete multilingual training). Score ladder UNMEASURED (planned: token balance, byte balance, response-optimized mixture and stronger interaction-aware policy).
## Screen record
id: C041
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.81
attack_single_range: 0.55-0.94
bo4_est: 0.88
pass4_est: 0.98
ub95_est: 0.98
gpuh_old: 10
gpuh_new_est: 280
duplicate_of: 01A MODERATE; T02 MODERATE
kill_reason: byte-aware packing and optimized source mixture cover main gain
souping_flag: no
