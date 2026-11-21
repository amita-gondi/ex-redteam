# C096 — Discover an image representation that retains violated constraints — saturation screen
## 1. What the grader actually rewards
The encoder must preserve enough information through a fixed-byte channel for exact violation detection and downstream constraint reasoning on private diagrams. Pixel reconstruction is diagnostic, so a sharp normal-looking image that drops the falsifying mark can still have poor utility. R≈0 is the competent task-aware bottleneck floor, R≈1 is an attainable semantically sufficient representation, and the no-op/reference anchors are provisionally ESTIMATED 0.00/0.60 rather than reconstruction-score percentages.
## 2. Strongest lawful combined attack
Start from a multiscale visual encoder, using [Vision Transformer](https://arxiv.org/abs/2010.11929) and [masked-autoencoder](https://arxiv.org/abs/2111.06377) training as concrete standard representation baselines. Add paired diagrams that differ only in a decisive mark, balanced sampling of tiny semantic changes, and supervised relation/constraint losses before the byte bottleneck. The strongest bypass is to train the encoder toward a compact symbol-and-relation description instead of spending bytes on a photorealistic reconstruction. Legal training-time vectorization or symbolic parsing can supply supervision; the delivered artifact remains the learned encoder and reasoner unless executable parsing is explicitly allowed.

Combine a coarse structural code with a budgeted high-frequency residual and tune their byte allocation using downstream execution accuracy. This stack can preserve obvious anomalies and much diagram syntax. ESTIMATED single-run R=0.47, range 0.25–0.65; ESTIMATED best-of-4=0.57; ESTIMATED pass@4 at R≥0.60=0.28; ESTIMATED projected upper-95% bound=0.72. Remaining loss concerns which tiny features matter under a new constraint system when the channel cannot retain everything. The forecast would rise sharply if a lossless sparse symbol graph fits the byte budget: then semantic compression becomes an ordinary parser problem and the claimed bottleneck disappears. Neither the channel capacity nor the diagram information rate is specified yet.
## 3. Other routes
- A supervised task-aware encoder with counterfactual pairs and relation loss is ESTIMATED R=0.40, range 0.20–0.60. It attacks semantic preservation directly rather than optimizing normal-region reconstruction.
- Sweep patch scale, latent precision, structural/residual allocation and anomaly oversampling under an identical byte cap: ESTIMATED R=0.44, range 0.22–0.63. Search can identify gross capacity misallocation but cannot infer unseen semantic dependencies automatically.
- Amortized symbol-graph encoding is ESTIMATED R=0.45, range 0.18–0.76. Its unusually wide range reflects whether diagram primitives admit a compact faithful symbolic representation; this shortcut must be measured rather than ruled out by architectural preference.
## 4. What would lower lawful saturation
Specify the actual channel bytes and show that a competent sparse graph codec or uniform high-resolution residual cannot retain all relevant information. Require new constraint compositions where visually identical small marks have different relational importance, while development exposes the same compositional rules and visual resolution. ESTIMATED attack could fall to R=0.36–0.49. ESTIMATED author effort is three weeks and ESTIMATED extra calibration is 192 H100 GPU-h. A stronger attainable codec must demonstrate that selective retention is possible at the chosen cap; reducing bytes until every method fails would not create a valid research task.
## 5. Decisive-check GPU-h re-estimate
Old card value: ESTIMATED 16 GPU-h. New ESTIMATED total: 336 H100 GPU-h. Assume an ESTIMATED 100M image encoder/decoder and 300M downstream reasoner: ESTIMATED 4 representations × 3 seeds × 16 H100-hours = 192 GPU-h for representation training; identical reasoner training costs ESTIMATED 4 × 3 × 8 hours = 96 GPU-h; add ESTIMATED 48 GPU-h for byte-matched decoding, private diagram reasoning and counterfactual checks. This is a bounded synthetic-diagram pilot, not a frontier VLM training claim. The old allowance omits retraining the reasoner for each representation and replication of rare decisive-mark outcomes.
## 6. Duplicate check
Catalog T11 and FIX T11 — MODERATE after opening both grounding specifications. They train visual/temporal reasoning from pixels with counterfactual supervision, whereas this intervention changes a learned fixed-byte information channel and isolates what survives it. Catalog T21 — WEAK: both use resource constraints, but that source compresses model weights rather than example evidence. No strong intervention/target identity is established.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 is 0.03 below its line and the projected upper bound has 0.03 clearance. Require a numerical byte budget, a sparse-symbol-codec baseline and evidence of attainable selective retention. The low author forecast cannot substitute for establishing that the bottleneck is consequential.
## 8. Measurement status
Rollouts UNMEASURED (planned: learned semantic codecs and symbol-supervision bypasses); grader noise UNMEASURED (planned: encoder/reasoner training seeds and counterfactual diagram repeats); score ladder UNMEASURED (planned: reconstruction codec, anomaly codec, symbolic supervision and attainable semantic codec).
## Screen record
id: C096
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.47
attack_single_range: 0.25-0.65
bo4_est: 0.57
pass4_est: 0.28
ub95_est: 0.72
gpuh_old: 16
gpuh_new_est: 336
duplicate_of: catalog T11 MODERATE; FIX T11 MODERATE; catalog T21 WEAK
kill_reason: byte cap must defeat lossless sparse symbol encoding while retaining feasible control
souping_flag: no
