# C043 — Pretrain through storage corruption with uncertain provenance — saturation screen
## 1. What the grader actually rewards
The integrity controller must improve final loss on clean private sources after paying for inspection, duplicate reads and skipped exposure. Correctly diagnosing damaged shards earns no utility unless the resulting accepted training stream teaches the model better. ESTIMATED R≈0 is a competent integrity/recovery floor and ESTIMATED R≈1 a stronger attainable clean-learning policy; loss-only filtering is provisionally near ESTIMATED R=0.00 and reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Exploit verified metadata where it exists, request independent rereads selectively, and separate source reliability from example difficulty. [OpenZFS's checksum documentation](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Data%20Storage/Checksums.html) establishes end-to-end integrity checking; it does not justify inventing trusted clean digests when provenance is uncertain. Store accepted-read fingerprints and disagreement histories, infer corruption probabilities per source/read regime, and reserve coverage for rare hard sources rather than dropping all high-loss text.

Add a robust weighting model using disagreement between independently trained small predictors, inspired by [Co-teaching](https://arxiv.org/abs/1804.06872). That paper concerns noisy labels, so applying disagreement weighting to corrupted language-model input is an extrapolation, not a verified complete solution. Jointly tune audit rates, reread stopping thresholds and training mixture under the actual read budget. The strongest lawful route may be much simpler: if each reread has an appreciable independent chance of returning clean bytes, consensus recovery cheaply preserves difficult examples without asking a model whether the text looks plausible.

ESTIMATED single-run R=0.65, range ESTIMATED 0.37–0.84; ESTIMATED best-of-4=0.74; ESTIMATED pass@4 at R≥0.60=0.82; ESTIMATED projected upper-95% bound=0.91. The estimate credits reliable recovery of transient faults and source-conditioned training allocation beyond naive loss filtering. Remaining loss comes from persistent plausible corruption, correlated rereads and hard clean data with no independent integrity witness. Those cases could be genuinely difficult, but the card does not quantify their prevalence or distinguish inferable faults from irretrievable missing information.
## 3. Other routes
Selective reread consensus is the strongest individual standard recipe: ESTIMATED R=0.56, range ESTIMATED 0.29–0.78. It keeps semantically difficult examples when their bytes repeat consistently, but cannot identify persistently corrupted content without provenance.

A search over source audit fractions, repeat counts, confidence thresholds and retained hard-source quotas reaches ESTIMATED R=0.60, range ESTIMATED 0.33–0.81. Training proxies can estimate marginal value per extra read. A lawful trusted-subset-only policy scores ESTIMATED R=0.43, range ESTIMATED 0.19–0.68 if clean sources span most evaluation support; that shortcut must be checked before claiming rare-source reconstruction is necessary.
## 4. What would lower lawful saturation
Specify correlated plausible corruption that survives repeated reads but has an accessible costly independent witness. Pair it with rare clean sources of similar model loss, and make audit evidence change the optimal future acquisition policy. ESTIMATED combined R could fall to 0.43–0.55. ESTIMATED cost is four data-systems weeks plus ESTIMATED 192 H100 GPU-h for validating source coverage and learnability. The witness must be genuinely available through the disclosed interface; removing all distinguishing evidence would make failure inevitable rather than research-sensitive.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 8 GPU-h. New ESTIMATED 224 H100 GPU-h assumes an ESTIMATED 1B learner, ESTIMATED four integrity-policy arms and ESTIMATED two independent corruption/training seeds, with ESTIMATED 24 H100-hours per continuation: ESTIMATED 4×2×24=192. Clean-source and hard-source evaluation add ESTIMATED 24 GPU-h; small disagreement-model calibration adds ESTIMATED 8 GPU-h. All reread latency is retained in the campaign accounting. The old pilot can verify service corruption behavior but cannot establish final clean-learning effects across competing policies.
## 6. Duplicate check
01A: MODERATE, based on its read provenance-aware corpus policy; C043 adds paid, stochastic integrity evidence at read time. FIX T18: WEAK, from its inspected clean-audit versus noisy-signal contract, because that task changes policy updates under reward noise rather than restoring training text. D18: WEAK after reading its support-generator target; unavailable examples there arise from reachability rather than damaged reads.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds its line by 0.14; pass@4 exceeds its limit by ESTIMATED 0.32. Reread recovery plus source reliability modeling is too strong against the unspecified corruption process.
## 8. Measurement status
Rollouts UNMEASURED (planned: integrity policies through the metered read service). Grader noise UNMEASURED (planned: repeated corruption and learner seeds). Score ladder UNMEASURED (planned: loss filter, read consensus, combined recovery and attainable witness-aware policy).
## Screen record
id: C043
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.65
attack_single_range: 0.37-0.84
bo4_est: 0.74
pass4_est: 0.82
ub95_est: 0.91
gpuh_old: 8
gpuh_new_est: 224
duplicate_of: 01A MODERATE; FIX-T18 WEAK; D18 WEAK
kill_reason: reread consensus and reliability-weighted learning likely suffice
souping_flag: no
