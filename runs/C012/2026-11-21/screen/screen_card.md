# C012 — Recover learnability after curriculum-induced gradient starvation — saturation screen
## 1. What the grader actually rewards
The trained video model must answer event-order and delayed-cause questions on new scenes while retaining short-event accuracy, with every reused clip exposure charged. ESTIMATED R≈0 is the strongest competent replay/recovery floor and ESTIMATED R≈1 an achievable stronger representation intervention at the same exposure budget. The starved inherited model is provisionally ESTIMATED R=0.00 and the reference ESTIMATED R=0.60; recovery of training loss alone does not locate either reward anchor.
## 2. Strongest lawful combined attack
Combine balanced delay-stratified replay, temporal-order and future-feature prediction, a controlled learning-rate restart, and selective renewal of low-utility temporal units. [Loss of Plasticity in Deep Continual Learning](https://www.nature.com/articles/s41586-024-07711-7) verifies that plasticity can degrade and documents continual backpropagation and shrink-and-perturb remedies. [Understanding Plasticity in Neural Networks](https://proceedings.mlr.press/v202/lyle23b) supplies a mechanistic analysis supporting targeted controls. These studies do not establish that a video's long-delay features have the same failure mechanism, so neither is evidence for a numerical recovery claim here.

The researcher would inspect temporal-feature sensitivity at the inherited checkpoint, compare resetting only temporal blocks with gentle perturbation, and use a mixed short/long rehearsal loss to preserve established visual features. Clip transformations and auxiliary targets must derive from the existing pool; no new media or private scene answers are introduced. A small set of staged continuations can select the perturbation strength and recovery duration before the final mixed training. Where parameter renewal is not admitted by the eventual weights-training API, use fresh trainable temporal adapters within the same capacity cap and charge their training; the scientific comparison must state which intervention is permitted.

ESTIMATED single-run R=0.49, range 0.27–0.68; ESTIMATED oracle best-of-4=0.59; ESTIMATED pass@4 at R≥0.60=0.43; ESTIMATED upper-95% projection envelope=0.74. These are design judgments. Exposure balancing recovers neglected examples; plasticity repair adds a mechanism beyond more replay. The difficult remainder is restoring temporal credit features without destroying short-event behavior under a fixed clip and exposure allowance. A generic reset may need more relearning than the budget permits. Yet the current grader mostly measures final answers, so it can mistake relearning familiar temporal patterns for restored capacity to acquire a genuinely new delayed relation.
## 3. Other routes
- Balanced long-delay replay followed by mixed fine-tuning: ESTIMATED R=0.36, range 0.17–0.57. It is the key null explanation because changing exposure can look like representation recovery.
- Sweep reset fraction, temporal-layer selection, restart learning rate, auxiliary-loss mix and recovery duration. ESTIMATED R=0.45, range 0.24–0.65. Search must include the opportunity cost of clips spent selecting and warming each recovery path.
- Retrain temporal components from an authorized earlier initialization while keeping spatial features fixed. ESTIMATED R=0.40, range 0.18–0.66 if that checkpoint channel is allowed. This could bypass the entire starvation diagnosis but may lose too much accumulated temporal knowledge.
## 4. What would lower lawful saturation
Add a disclosed final acquisition phase using an untouched relation composition drawn from the same fixed clip pool, identical across candidate methods, and grade learning speed plus final delayed-cause transfer. Compare against matched-exposure replay and the full perturbation/restart stack. This makes restored trainability observable instead of inferred from recovery on old skills. Forecast after revision: ESTIMATED composite R=0.37, best-of-four=0.48, pass@4=0.20 and upper envelope=0.66. Cost is ESTIMATED several weeks of causal-video and phase authoring plus ESTIMATED 216 extra H100 GPU-h for acquisition-curve controls. Holding out an impossible relation would invalidate the test rather than increase its difficulty.
## 5. Decisive-check GPU-h re-estimate
Old pilot value: ESTIMATED 16 GPU-h. Revised ESTIMATED 252 H100 GPU-h includes an ESTIMATED 300M-parameter video model, ESTIMATED 4 recovery arms, ESTIMATED 3 seeds and ESTIMATED 18 H100-hours per recovery-plus-acquisition run, with ESTIMATED 36 GPU-h for scene inference and short-event retention: ESTIMATED 4×3×18+36=252. This assumes an inherited starvation checkpoint is already available and does not charge its creation to every arm. Creating and validating that checkpoint is additional author work. The previous allowance could examine feature probes, but not separate exposure recovery from later acquisition using independent learner seeds.
## 6. Duplicate check
FIX T11 (`fix_packets_v4/T11/packet.md`, previously opened): MODERATE. Both grade counterfactual event/order capability, but T11 changes grounding objectives generally while C012 intervenes on an inherited training-induced plasticity failure. The distinction survives only if recovery changes future learning at matched exposure. Otherwise the card becomes another temporal fine-tuning recipe with substantially the same outcome target.
## 7. Verdict
CONDITIONAL. The ESTIMATED best-of-four margin is only 0.01 and projection clearance ESTIMATED 0.01, well inside the redesign band. Require the matched final acquisition phase and complete plasticity-repair baseline above; final old-skill accuracy cannot by itself substantiate learnability recovery.
## 8. Measurement status
Rollouts UNMEASURED (planned: exposure-accounted recovery research including restart and renewal controls). Grader noise UNMEASURED (planned: repeated starvation/recovery seeds and scene-cluster evaluation). Score ladder UNMEASURED (planned: unchanged checkpoint, balanced exposure, temporal auxiliaries, plasticity stack and independently attainable feature recovery).
## Screen record
id: C012
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.49
attack_single_range: 0.27-0.68
bo4_est: 0.59
pass4_est: 0.43
ub95_est: 0.74
gpuh_old: 16
gpuh_new_est: 252
duplicate_of: FIX-T11 MODERATE
kill_reason: require new-relation acquisition beyond exposure-matched recovery
souping_flag: no
