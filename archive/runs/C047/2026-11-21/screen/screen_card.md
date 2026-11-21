# C047 — Continue pretraining after a causal feature is deliberately removed — saturation screen
## 1. What the grader actually rewards
The removed feature in the problem is the shortcut watermark; success requires recovering the true visual relation on private counterfactual pairs while retaining ordinary image capability. Merely making outputs insensitive to watermarks earns nothing if relation accuracy stays poor. ESTIMATED R≈0 is competent clean/counterfactual recovery and ESTIMATED R≈1 an attainable retained-capability control; clean-only continuation is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
First test whether useful causal features survived beneath a biased readout, then adapt the necessary visual layers rather than assume the representation was erased. [On Feature Learning in the Presence of Spurious Correlations](https://arxiv.org/abs/2210.11369) studies this distinction and feature reweighting. [All Layer Deep Feature Reweighting](https://arxiv.org/abs/2409.14637) expands the readout search across layers. These works motivate a cheap recovery baseline; they do not prove every shortcut-trained VLM retained the required relation.

Combine that probe with counterfactual recovery examples, group-balanced sampling, relation-focused auxiliary losses and ordinary-image replay. Where features truly are weak, progressively unfreeze the vision stack, use an easy-to-hard bridge curriculum and train the needed visual distinction directly from legal annotations. Sweep recovery depth, replay ratio and auxiliary loss jointly. All rendering and annotation must come from the permitted recovery pool; no hidden target labels are assumed. A frontier researcher can test both retained-feature and relearning hypotheses within a disciplined multi-fidelity campaign.

ESTIMATED single-run R=0.64, range ESTIMATED 0.36–0.84; ESTIMATED best-of-4=0.74; ESTIMATED pass@4 at R≥0.60=0.81; ESTIMATED projected upper-95% bound=0.92. The estimate credits correcting a biased readout when possible and targeted feature relearning otherwise, while retaining general performance through replay. The unrecovered share is a genuinely lost relational representation whose gradient signal remains too weak even in bridge data. The card asserts that possibility but does not show it survives the full recovery stack; a removed watermark does not imply removed causal support in the checkpoint.
## 3. Other routes
Balanced counterfactual fine-tuning is the strongest single recipe: ESTIMATED R=0.53, range ESTIMATED 0.27–0.75. It directly teaches the relation and avoids requiring an explicit mechanism diagnosis.

A search over layer unfreezing, clean/bridge proportions, relation losses and training order reaches ESTIMATED R=0.59, range ESTIMATED 0.32–0.80. Short readout probes cheaply allocate training to the right hypothesis. Last-layer recovery alone can obtain ESTIMATED R=0.41, range ESTIMATED 0.15–0.72 if the core representation remains, making it a decisive cheap falsifier despite its low expected generality.
## 4. What would lower lawful saturation
Supply checkpoint families with independently demonstrated loss of the relevant causal feature, rather than simply poor end-to-end answers, and legal bridge support that restores subsequent learnability at matched exposure. Compare against full visual unfreezing, all-layer readouts and broad counterfactual training. ESTIMATED composite R could fall to 0.42–0.55. ESTIMATED cost is five multimodal-research weeks and ESTIMATED 288 H100 GPU-h for checkpoint/probe and recovery validation. An assay must distinguish inaccessible features from a poorly trained probe; otherwise the new premise would remain unsupported.
## 5. Decisive-check GPU-h re-estimate
Old card value: ESTIMATED 12 GPU-h. New ESTIMATED 256 H100 GPU-h assumes an ESTIMATED 3B VLM, ESTIMATED four recovery arms, ESTIMATED two independently shortcut-trained starting seeds and ESTIMATED 24 H100-hours per recovery: ESTIMATED 4×2×24=192. Counterfactual/ordinary-image evaluation adds ESTIMATED 32 GPU-h, all-layer probes ESTIMATED 16 and independent rendering/feature intervention checks ESTIMATED 16. Compatible starting checkpoints are assumed available; creating them would cost extra. The old pilot is too small to distinguish simple readout recovery from meaningful relearning with retained general capability.
## 6. Duplicate check
Catalog/FIX T11: MODERATE, after reading both source contracts; they already train counterfactual visual relations and retain useful skills, while C047 emphasizes recovery after shortcut removal. D07: WEAK, after reading its causal onset-control intervention; it acts before exploit learning rather than rebuilding a damaged visual representation. Starting-state emphasis alone is thin novelty, but the proposed learnability outcome prevents a definitive STRONG finding.
## 7. Verdict
CUT. ESTIMATED best-of-four excess is 0.14 and pass@4 excess 0.31. The claimed lost-feature mechanism is not established strongly enough to discount the combined reweighting, counterfactual and full-recovery recipe.
## 8. Measurement status
Rollouts UNMEASURED (planned: matched-exposure recovery from independent shortcut checkpoints). Grader noise UNMEASURED (planned: repeated rendering and recovery seeds). Score ladder UNMEASURED (planned: readout-only, clean continuation, full bridge stack and stronger relation-recovery control).
## Screen record
id: C047
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.64
attack_single_range: 0.36-0.84
bo4_est: 0.74
pass4_est: 0.81
ub95_est: 0.92
gpuh_old: 12
gpuh_new_est: 256
duplicate_of: T11 MODERATE; FIX-T11 MODERATE; D07 WEAK
kill_reason: combined counterfactual recovery likely exceeds tail gates
souping_flag: no
