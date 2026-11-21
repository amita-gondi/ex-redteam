# C068 — Preserve mixed DPO/SFT semantics while packing uneven responses — saturation screen
## 1. What the grader actually rewards
The declared DPO/SFT objective must produce equivalent gradients when one effective batch is repartitioned, and trained models must improve exact preference behavior while retaining generation quality. Shortening responses or changing normalization units without authorization does not establish a better implementation. R≈0 is the correctly reduced competent preference-learning floor; R≈1 is the stronger attainable model under the same training resources, and every forecast here is ESTIMATED because the joint utility and its anchors are UNMEASURED.

Adaptive mixed supervision is the provisional ESTIMATED R=0.60 reference, with no demonstrated private preference/retention utility at that placement.

## 2. Strongest lawful combined attack
Build a scalar objective oracle on unpacked examples, keeping preference-pair contributions and supervised-token contributions in their separately declared units. Accumulate numerators and global denominators over the full effective batch, accounting explicitly for distributed gradient averaging. Preserve pair membership, completion masks and reference log probabilities during packing, then match actual parameter updates against the oracle before optimization.

Use [DPO](https://arxiv.org/abs/2305.18290) as the preference component and the documented mixed-loss capabilities in [TRL's DPO trainer](https://huggingface.co/docs/trl/main/en/dpo_trainer) as the implementation starting point. Sweep mixture weights, preference temperature, supervised warmup and allowed length-conditioned coefficients together, retaining exact behavior and generation checks. Conditioning on legal semantic or length features is a recipe choice; accidentally conditioning on microbatch layout is a bug. Reference computations may be cached when fixed, with preparation charged.

ESTIMATED single-run R=0.81, range 0.62–0.92; ESTIMATED best-of-4=0.89; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED upper-95% projection=0.97. These estimates concern a tuned transferred recipe above a fixed calibration stack, not the same stack assigned zero by definition. The residual is generalization of supervision weights to new preference mechanisms. The card presently offers only length correlations as the extra difficulty, a low-dimensional signal a standard mixture sweep can exploit. Correct packed execution does not itself make the objective scientifically unfamiliar.

## 3. Other routes
Correctly reduced static DPO/SFT with a small mixture-weight search is the strongest single recipe: ESTIMATED R=0.70, range 0.49–0.86. It should be included as a competent floor rather than comparing adaptive weighting with a reduction-bug baseline.

A broader held-out sweep over length bins, supervised-loss schedules, DPO temperature and regularization gives ESTIMATED R=0.78, range 0.57–0.91. It can choose an unpacked implementation when the packing overhead and semantic risk outweigh its speed gain. Deployment-only requirements should not suppress that legal control unless the resource contract demonstrates its actual inferiority.

## 4. What would lower lawful saturation
Separate implementation parity from the scientific task, then introduce supported preference mechanisms in which equal-length examples need different supervision because their trustworthy evidence differs. Hold out those semantic relationships and retain the same token budget and packing options in development. ESTIMATED combined R after redesign is 0.50–0.66, requiring further screening. ESTIMATED authoring cost is 9–14 person-days and ESTIMATED 192 H100-h for preference/retention pilots. Simply adding more unequal-length examples is unlikely to defeat an already length-conditioned mixture policy.

## 5. Decisive-check GPU-h re-estimate
Old card estimate: ESTIMATED 12 GPU-h. New ESTIMATED 192 H100-GPU-h uses an ESTIMATED 3B policy with a frozen ESTIMATED 3B reference, ESTIMATED 200M preference/supervision tokens per training run, ESTIMATED 4 recipe arms×3 seeds×12 device-hours=144. Reference-logprob preparation and partition-equivalence checks add ESTIMATED 24; independent exact behavior and retained-generation evaluation add ESTIMATED 24. Total ESTIMATED 144+24+24=192. The estimate assumes the reference can be processed in a separate charged pass. The old amount could test algebraic equivalence or train one small arm, not compare downstream adaptation and retention across private mechanisms.

## 6. Duplicate check
T18: WEAK after reading the FIX packet, which changes robust updates under corrupted reward and ratio tails rather than supervised/preference reduction units. T06: MODERATE from its packet because it also trains for reliable preference-related behavior with retained support, but the submitted loss and unequal-length packing mechanism differ. 05B: MODERATE because preserving gradients through execution changes is already its central contract; this card additionally claims an adaptive preference-learning objective.

## 7. Verdict
CUT. ESTIMATED single-run reward exceeds its binding threshold by 0.11 and ESTIMATED best-of-4 exceeds its line by 0.29. Correct global reduction plus mature preference training and mixture search is a particularly direct combined route to the stated grader; no specific semantic residual presently defeats it.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent mixed-objective searches on private preference mechanisms); grader noise UNMEASURED (planned: repeated fixed-recipe training and retained-generation evaluation); score ladder UNMEASURED (planned: erroneous reduction, corrected static mixture, length-conditioned search, semantic weighting and stronger attainable control).

## Screen record
id: C068
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.81
attack_single_range: 0.62-0.92
bo4_est: 0.89
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 12
gpuh_new_est: 192
duplicate_of: T18 WEAK; T06 MODERATE; 05B MODERATE
kill_reason: corrected reductions and joint DPO SFT mixture search cover the extension
souping_flag: no
