# C107 — A tokenizer change that must pay for its own optimizer recovery — saturation screen
## 1. What the grader actually rewards
The useful quantity is held-out loss per original byte after a fixed total migration-and-continuation time, with retained compositions checked independently. Shorter token sequences help only if the trained model preserves and acquires the underlying support. ESTIMATED R≈0 corresponds to competent embedding migration with a safe optimizer restart; ESTIMATED R≈1 corresponds to a demonstrated stronger migration under the same byte, time and model constraints. The intended ESTIMATED reference R≈0.60 is not a measured baseline, and leaving the old tokenizer unchanged must be a scored control.
## 2. Strongest lawful combined attack
Use [FOCUS](https://aclanthology.org/2023.emnlp-main.829/) or [WECHSEL](https://aclanthology.org/2022.naacl-main.293/) as established within-model vocabulary-transfer initializers. Preserve identical vocabulary rows and their optimizer entries exactly, initialize changed rows through legal old/new correspondences, and reset ambiguous moment entries. These are transformations of one inherited learner, not combinations of separately trained models. The cited methods establish embedding-transfer tools; they do not establish a correct transport law for optimizer moments.

The strongest practical attack avoids solving that law universally. Preserve backbone moments where parameter meaning is unchanged, reset or damp affected rows, warm the new embeddings briefly, and sweep separate learning rates and moment damping. Evaluate byte-normalized learning curves and old/new composition retention before allocating the remaining budget to the best candidate. A strong researcher would compare a full restart, row-selective restart and simple correspondence-based transport, letting cheap sequence savings fund recovery. If moment transport has only a brief transient benefit, restarting can reach nearly the same final loss more reliably.

ESTIMATED single-run R=0.68, range 0.47–0.85; ESTIMATED oracle best-of-4=0.77; ESTIMATED pass@4 at R≥0.60=0.88; ESTIMATED projected upper-95% score=0.91. The residual is a gradient-distribution change induced by new segmentation: semantic similarity of rows does not preserve either the first moment or the squared-gradient statistics. This matters when continuation is short and the old state is valuable. The current card does not fix such an operating point; saved sequence work may simply amortize the restart cost.
## 3. Other routes
FOCUS-style embedding initialization followed by a clean optimizer restart is the strongest single recipe. ESTIMATED R=0.57, range 0.34–0.77. It exploits the main efficiency gain while refusing to import poorly justified statistics.

A structured search over unchanged-row preservation, changed-row damping, warmup duration and embedding/backbone rates is likely stronger than intricate hand-derived transport. ESTIMATED R=0.65, range 0.42–0.84. Selecting the original tokenizer is another lawful control if migration is optional: ESTIMATED R=0.39, range 0.14–0.71. If that wins on realistic byte-loss and retention, the task's premise fails; imposing migration solely to remove the control would not demonstrate scientific usefulness.
## 4. What would lower lawful saturation
Build migration histories where partial row overlap interacts with real compositional gradients, and freeze a continuation horizon short enough for state quality to affect total utility but long enough for genuine learning. Supply representative development metadata and keep both reset controls competitive. ESTIMATED attack score might fall by 0.12–0.20, leaving 0.48–0.56 and still requiring a tail screen. ESTIMATED cost is 9–16 person-days plus 240 H100-h to prepare ancestry-matched optimizer histories. Reweighting the scorer toward an arbitrarily brief restart transient would overstate the intervention's practical value.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 18 GPU-h. New ESTIMATED requirement: 336 H100 GPU-h. For a 1B controlled learner continued over an ESTIMATED multi-billion-token stream, use 5 migration/state arms × 2 seeds × 24 H100-h = 240 H100-h. A 4B sign/ranking check on 2 selected arms × 2 seeds × 16 H100-h adds 64; byte-loss, retention and resume evaluations add 32. ESTIMATED arithmetic is 240+64+32=336. The old value might compare a few immediate loss spikes but cannot establish durable optimizer-recovery benefit on substantial continuation. Token throughput remains a pilot quantity to measure.
## 6. Duplicate check
T02, MODERATE: the opened source explicitly studies corpus/boundary migration and optimizer-state transport, but keeps tokenization fixed and scores held-corpus learning rather than vocabulary conversion. W01 is a contextual near neighbor outside the required index: its source targets vocabulary migration and compositional support, making this card's extra optimizer treatment especially important to isolate. No indexed STRONG duplicate is established.
## 7. Verdict
CUT. ESTIMATED oracle best-of-4 is 0.17 above its boundary, with pass@4 also excessive. Safe partial restart plus familiar vocabulary transfer is a more credible floor than assuming semantic moment transport remains necessary throughout continuation.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent migration-program development with all search cost charged). Grader noise UNMEASURED (planned: repeat fixed migrations and continuation seeds on byte-identical corpora). Score ladder UNMEASURED (planned: unchanged tokenizer, fresh restart, selective restart, transported state, reference and attainable stronger migration).
## Screen record
id: C107
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.68
attack_single_range: 0.47-0.85
bo4_est: 0.77
pass4_est: 0.88
ub95_est: 0.91
gpuh_old: 18
gpuh_new_est: 336
duplicate_of: T02 MODERATE
kill_reason: vocabulary transfer and selective restart can amortize state recovery
souping_flag: no
