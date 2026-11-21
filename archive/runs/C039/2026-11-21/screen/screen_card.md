# C039 — Pretrain from revisable scientific records — saturation screen
## 1. What the grader actually rewards
The learner must assign high conditional likelihood to current conclusions and to older statements when their historical evidence conditions are supplied. Current and historical questions retain fixed weight, so newest-only filtering cannot erase the historical obligation. ESTIMATED R≈0 represents competent temporally qualified exposure, ESTIMATED R≈1 an attainable condition-sensitive learner; uniform-history training is provisionally ESTIMATED R=0.00 and the author reference ESTIMATED R=0.60, with the actual likelihood anchors unresolved.
## 2. Strongest lawful combined attack
Parse record lineage into assertions, validity intervals, evidence versions and experimental conditions. Train on explicit condition-qualified passages, balance exposure across versions, and interleave current summaries with old-valid evidence rather than blindly repeating obsolete statements. [Time-Aware Language Models as Temporal Knowledge Bases](https://arxiv.org/abs/2106.15110) establishes time-conditioned knowledge learning. [TemporalWiki](https://arxiv.org/abs/2204.14211) provides a concrete precedent for learning from revision differences instead of entire redundant snapshots.

Combine temporal qualification with lineage deduplication, contrastive old/new examples using only legal records, and a mixture schedule tuned on protected development likelihood. If the allowed artifact permits only exposure rather than rewritten text, select original condition-bearing spans and paired versions; do not assume unrestricted synthetic answers. A frontier researcher can derive a compact temporal knowledge pipeline directly. The card does not require most revisions to be implicit causal changes, so standard extraction may cover much of the held distribution.

ESTIMATED single-run R=0.67, range ESTIMATED 0.41–0.85; ESTIMATED best-of-4=0.76; ESTIMATED pass@4 at R≥0.60=0.85; ESTIMATED projected upper-95% bound=0.92. These estimates describe recovery of the available likelihood improvement after ordinary recency filtering, assuming a fixed stronger endpoint. The remaining share concerns revisions where a changed experimental condition, rather than a timestamp, determines validity. A textual likelihood metric can also reward predictable record wording without demonstrating causal generalization, potentially making this forecast conservative unless paired conditional probes rule that out.
## 3. Other routes
Time-conditioned balanced replay is the strongest single standard recipe: ESTIMATED R=0.56, range ESTIMATED 0.31–0.76. It preserves historical support but may encode coarse dates rather than the scientific reason a claim changed.

A sweep over current/history exposure ratios, revision-diff oversampling, chain-depth weighting and curriculum order reaches ESTIMATED R=0.61, range ESTIMATED 0.36–0.81. Short proxy runs can screen mixtures, with finalists retrained at the scored horizon. A lawful source-style shortcut that models version language well could obtain ESTIMATED R=0.39, range ESTIMATED 0.17–0.65 if the grader evaluates long predictable passages rather than conclusion-sensitive likelihood contrasts.
## 4. What would lower lawful saturation
Require revision pairs in which chronology and truth come apart: an older result remains valid under its original conditions while a newer result overturns only a specific causal generalization. Score contrastive likelihood on minimally differing conclusion/condition pairs, with wording and temporal tokens counterbalanced. ESTIMATED combined R could drop to 0.44–0.56. ESTIMATED preparation cost is five scientific-author weeks and ESTIMATED 192 H100 GPU-h for learning-validity checks. Keep the record interface expressive enough for ordinary temporal qualification; banning timestamps would obscure the real scientific question.
## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 12 GPU-h. New ESTIMATED 240 H100 GPU-h assumes an ESTIMATED 1B subject continued on an ESTIMATED 1B-token revision corpus. Budget ESTIMATED four exposure arms, ESTIMATED two seeds each and ESTIMATED 24 H100-hours per training run: ESTIMATED 4×2×24=192. Evaluation of paired current/historical likelihood and repeated checkpoints adds ESTIMATED 32 GPU-h; preprocessing-proxy calibration adds ESTIMATED 16. This is a planning throughput assumption, not a benchmark. The original estimate cannot establish historical/current interference after meaningful continued pretraining.
## 6. Duplicate check
01A: MODERATE, after reading its stage-aware corpus contract; it changes source exposure for downstream learning but does not require temporal validity of paired scientific assertions. Catalog T02: WEAK, from its inspected fixed-corpus continuation statement. FIX T08: MODERATE, using its read old-valid/obsolete/returning contract, though that task changes parameter updates under tool-contract evolution rather than corpus exposure.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds its threshold by 0.16; pass@4 exceeds its limit by ESTIMATED 0.35. Temporal extraction and balanced qualified training plausibly recover too much of the currently specified objective.
## 8. Measurement status
Rollouts UNMEASURED (planned: exposure policies on independent revision families). Grader noise UNMEASURED (planned: repeated continuation seeds and conclusion likelihood checks). Score ladder UNMEASURED (planned: newest-only, uniform history, temporal pipeline and causal-condition control).
## Screen record
id: C039
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.67
attack_single_range: 0.41-0.85
bo4_est: 0.76
pass4_est: 0.85
ub95_est: 0.92
gpuh_old: 12
gpuh_new_est: 240
duplicate_of: 01A MODERATE; T02 WEAK; FIX-T08 MODERATE
kill_reason: temporal qualification and replay likely cover most revision utility
souping_flag: no
