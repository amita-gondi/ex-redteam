# C083 — Augmentation gains after semantic invariance is broken — saturation screen
## 1. What the grader actually rewards
Training must improve protected prose loss and executable program performance at equal complete work, rather than maximizing how many transformed examples parse. R≈0 is the full competent modality-conditioned augmentation baseline; R≈1 requires an attainable improvement on both useful text prediction and program behavior under the disclosed mixture. The no-op and reference are provisionally ESTIMATED R=0.00 and R=0.60; unspecified code/text utility weights remain a material calibration limitation.
## 2. Strongest lawful combined attack
Use the verified [official augmentation implementation](https://github.com/michaelchen-lab/data-augmentations-for-pretraining), which distinguishes input noise, sequence permutation and target-offset objectives. An important correction to the difficulty story is that corruption used to predict the original clean targets need not preserve the semantics of its corrupted input. The agent should preserve the original target relation, tag auxiliary tasks, separate clean autoregressive evaluation, and tune augmentation strength independently for code and prose. For transformations intended to create new labeled programs, apply exact executable equivalence checks on the bounded mini-language, using [Z3 bit-vectors](https://microsoft.github.io/z3guide/docs/theories/Bitvectors/) when its semantics fit that theory.

Combine clean-code replay, conservative program transformations, aggressive prose regularization and development selection on the actual executable/prose mixture. No universal semantic filter is required if questionable code augmentation can simply be disabled at modest opportunity cost. ESTIMATED single-run R=0.69, range 0.48–0.85; ESTIMATED best-of-4=0.78; ESTIMATED pass@4 at R≥0.60=0.91; ESTIMATED projected upper-95% bound=0.93. The residual concerns valid auxiliary tasks whose transfer effects conflict across modalities and long-range causal text. Those are learning questions, but they do not justify assuming that syntax-valid corruptions necessarily contaminate supervision when targets are constructed correctly.
## 3. Other routes
- Clean code with the published augmentation stack applied only to prose is ESTIMATED R=0.60, range 0.39–0.79. It loses possible code regularization gains while avoiding the card's most obvious hazard entirely.
- Sweep modality-specific corruption rates, clean replay fractions, target offsets and task tags with successive resource allocation: ESTIMATED R=0.66, range 0.45–0.84. A development execution metric prevents selecting purely by language-model loss.
- Restrict code augmentation to provably equivalent renamings and bounded rewrites: ESTIMATED R=0.54, range 0.32–0.75. Parser acceptance alone is insufficient, but a narrow verified transformation set is a strong lawful baseline.
## 4. What would lower lawful saturation
State precisely whether each transformation is denoising input corruption, a task permutation, or purportedly new clean training content. Require fresh mini-language mechanisms where a proven semantics-preserving augmentation can still teach a harmful statistical invariance, and show that clean-code plus prose-only augmentation leaves attainable reserve. ESTIMATED combined reward could fall to 0.42–0.57 if cross-modal transfer truly forces conditional choices. ESTIMATED authoring cost is two weeks and ESTIMATED extra training calibration is 192 H100 GPU-h. Simply classifying random replacement as “invalid code” would misdescribe the published objective and manufacture a weak baseline.
## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 12 GPU-h. Revised ESTIMATED total: 288 H100 GPU-h, assuming 150M reproduction subjects plus 1B transfer subjects. Allocate ESTIMATED 4 policies × 2 seeds × 6 hours = 48 GPU-h at proxy scale; ESTIMATED 3 finalists × 2 seeds × 32 H100-hours = 192 GPU-h for approximately ESTIMATED 2B-token full runs; add ESTIMATED 48 GPU-h for clean loss, private execution and transformed-pass accounting. These are future runtime assumptions, not measured throughput. The original allowance misses both repeated-exposure training and the program/general-text tradeoff; a short parsing test cannot decide the scientific claim.
## 6. Duplicate check
Catalog T02 and FIX T02 — MODERATE. Their source files admit broad pretraining data/objective recipes and share held-loss evaluation, but their defining interventions concern exposure, packing and optimizer history rather than augmentation target semantics. This card adds executable program outcomes, so the overlap does not meet the strong same-intervention/same-target criterion.
## 7. Verdict
CUT, binding on ESTIMATED best-of-4=0.78, exceeding the limit by 0.18. ESTIMATED pass@4 also exceeds its boundary by 0.41. The strongest bypass retains clean code, uses auxiliary corruption correctly and applies the full prose recipe, rather than trying to repair every possible augmentation.
## 8. Measurement status
Rollouts UNMEASURED (planned: modality-conditioned complete augmentation searches); grader noise UNMEASURED (planned: retraining seeds and private executable-case repeats); score ladder UNMEASURED (planned: clean training, prose-only augmentation, verified-code augmentation and attainable joint policy).
## Screen record
id: C083
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.69
attack_single_range: 0.48-0.85
bo4_est: 0.78
pass4_est: 0.91
ub95_est: 0.93
gpuh_old: 12
gpuh_new_est: 288
duplicate_of: catalog T02 MODERATE; FIX T02 MODERATE
kill_reason: correct auxiliary targets and prose only augmentation bypass invalid invariance story
souping_flag: no
