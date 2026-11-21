# C104 — A compression method that changes the optimal curriculum — saturation screen
## 1. What the grader actually rewards
Useful outputs must come from the compressed model, with recovery training, curriculum search and serving costs all charged. Retention constraints prevent a cheap specialist from winning by sacrificing old skills. ESTIMATED R≈0 is the competent compressed-and-recovered floor, and ESTIMATED R≈1 is a stronger attainable deployment frontier at identical costs; an unchanged dense model need not even satisfy the memory constraint. The proposed ESTIMATED reference score of about 0.60 cannot be checked until actual compression ratios, native utility and retention tolerances are frozen.
## 2. Strongest lawful combined attack
The obvious attack is already joint optimization. Start alternative calibrations with [GPTQ](https://arxiv.org/abs/2210.17323) and [AWQ](https://arxiv.org/abs/2306.00978), measure per-domain output and activation damage, and protect expensive or sensitive layers within a real packed-memory budget. Select compressed candidates on native outputs rather than average quantization error. Those measurements provide curriculum features directly: examples causing the largest useful teacher/student disagreement become recovery candidates, subject to old-skill replay and coverage constraints.

Use a fixed, charged teacher during training only, and perform quantization-aware recovery following the established premise of [LLM-QAT](https://aclanthology.org/2024.findings-acl.26/). Alternate short recovery runs with recalibration of damage and data weights, keeping every candidate's byte count and actual serving path valid. A modest development search can compare static mixtures, disagreement sampling and stage-conditioned mixtures without solving the author's preferred causal narrative. Training from one model and distilling its outputs does not require combining independent parameter sets.

ESTIMATED single-run R=0.79, range 0.61–0.92; ESTIMATED oracle best-of-4=0.86; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% score=0.96. Compression can indeed reverse example value, but measuring disagreement after compression is precisely how this attack updates that value. The remaining gap is feature support destroyed by structural removal and interference among recovery objectives. Nothing in the current task requires such irrecoverable interactions to account for a substantial share of attainable utility. Ordinary low-bit damage could dominate instead.
## 3. Other routes
AWQ calibration with a balanced recovery corpus is a strong single recipe. ESTIMATED R=0.65, range 0.47–0.82: it protects salient weights and can leave little meaningful curriculum work in a mild compression regime.

A cost-aware grid would vary compression family, layer precision, recovery duration, domain proportions and teacher-loss weight, pruning uncompetitive configurations early. ESTIMATED R=0.74, range 0.54–0.89. This route can locate the joint optimum without explicitly identifying a reversal. A further lawful simplification is selective high precision for rare-skill layers; if the budget permits it, allocating bytes can outperform any clever ordering of recovery data. Its ESTIMATED R=0.71, range 0.48–0.88, must enter the floor rather than be declared a shortcut violation.
## 4. What would lower lawful saturation
Choose a deployment regime in which preserving one representation consumes capacity needed by another, and construct independently held-out task relationships whose useful recovery examples change after actual learning. Match available development probes to those interactions, and compare the entire adaptive quantization/recovery stack. ESTIMATED score reduction is only 0.12–0.22, leaving approximately 0.57–0.67, so this redesign may still fail repeated-search gates. ESTIMATED development effort is 8–15 person-days and 320 H100-h for feature-loss and retention pilots. Merely demanding more aggressive compression risks lowering the attainable ceiling instead of creating reserve.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 18 GPU-h. New ESTIMATED total is 240 H100 GPU-h. For a 4B subject, allow 6 compression/curriculum arms × 2 seeds × 12 H100-h for calibration plus substantial recovery = 144 H100-h; use 4 selected arms × 2 seeds × 8 H100-h for held-out continuation = 64 H100-h; packed inference, retention evaluation and independent dense controls add 32 H100-h. ESTIMATED arithmetic is 144+64+32=240. These are continued-training runs, not full pretraining. The old budget could expose near-lossless quantization quickly, but cannot establish the proposed training-dependent curriculum reversal.
## 6. Duplicate check
T21, STRONG: the opened source already jointly varies compression, data-aware allocation, single-teacher recovery and real packed inference, with private capability and cost as the target. Calling the recovery data policy a curriculum does not create a new intervention or grader. 01A, WEAK: stage-dependent data value overlaps conceptually but does not compress the learner.
## 7. Verdict
CUT on both saturation and duplication. The binding recorded reason is STRONG duplication of T21; independently, ESTIMATED single-run reward exceeds its kill threshold by 0.09 and ESTIMATED best-of-4 by 0.26. The proposed coupling is already inside the older task's lawful intervention space.
## 8. Measurement status
Rollouts UNMEASURED (planned: joint compression-and-curriculum attempts with complete search accounting). Grader noise UNMEASURED (planned: repeat recovery and timed deployment of frozen artifacts). Score ladder UNMEASURED (planned: dense control, calibration-only, generic recovery, adaptive curriculum, reference and stronger same-budget compressed control).
## Screen record
id: C104
verdict: CUT
binding_line: duplicate
attack_single_est: 0.79
attack_single_range: 0.61-0.92
bo4_est: 0.86
pass4_est: 0.98
ub95_est: 0.96
gpuh_old: 18
gpuh_new_est: 240
duplicate_of: T21 STRONG; 01A WEAK
kill_reason: same joint compression recovery intervention and deployment target
souping_flag: no
