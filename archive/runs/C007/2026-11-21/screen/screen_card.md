# C007 — A loss that preserves counterexample repair — saturation screen
## 1. What the grader actually rewards
The resulting repair learner must implement newly requested behavior while keeping still-binding invariants throughout a dependent edit sequence. Individual preserved behaviors receive local credit, with complete executability recorded separately; an obsolete requirement should contribute no retention obligation. ESTIMATED R≈0 means the competent repair/replay floor and ESTIMATED R≈1 the stronger same-budget repair objective; unchanged training is provisionally ESTIMATED R=0.00 and the reference ESTIMATED R=0.60, with the scalarization still unmeasured.
## 2. Strongest lawful combined attack
Maintain versioned counterexamples and infer which old tests remain semantically applicable from the current specification and public edit history. Construct a loss combining current counterexample likelihood, rehearsal of applicable old repairs and selective behavioral distillation only on unaffected inputs. Use conflict-aware regularization inspired by [Gradient Episodic Memory](https://arxiv.org/abs/1706.08840) and compare its cheaper [A-GEM implementation](https://github.com/facebookresearch/agem). These verified methods establish available forgetting controls; they do not solve test-validity inference by themselves.

For an objective-only interface, express the protection through loss weights and a penalty on valid-old behavior rather than assuming permission to replace the optimizer with gradient projection. Counterexample-guided training uses legal program execution to produce repair traces; hidden invariant tests stay inaccessible. A validity classifier trained on specification diffs gates old losses, and a probe set measures whether the gate protects an obsolete behavior. Tune that gate and the stability/plasticity weights jointly, then train on the full edit sequence. All additional execution-generated examples must obey the task's fixed-data or generation permissions.

ESTIMATED single-run R=0.66, range 0.42–0.84; ESTIMATED oracle best-of-4=0.75; ESTIMATED pass@4 at R≥0.60=0.84; ESTIMATED upper-95% projection envelope=0.91. These are uncalibrated planning values. Selective protection addresses the obvious weakness of uniform KL: it need not preserve superseded output behavior. The residual lies in specifications whose dependencies reveal obsolescence only through later edits, and in finite model capacity. The current card asserts such dependencies but provides no instantiated case where a competent validity-aware objective loses a substantial fraction of the achievable invariant gain.
## 3. Other routes
- Apply current-repair cross-entropy plus replay and uniform KL. ESTIMATED R=0.43, range 0.20–0.66. This is a necessary simple baseline, but freezing irrelevant behavior can impede legitimate edits.
- Search the loss coefficients, replay-loss strata, gate thresholds and per-edit annealing schedule on public sequences. ESTIMATED R=0.58, range 0.34–0.79. Low-fidelity probes can discard bad tradeoffs before full retraining, making the search stronger than one hand-tuned regularizer.
- Train the loss to favor repairs that pass automatically generated metamorphic tests for unchanged semantics. ESTIMATED R=0.55, range 0.30–0.78. This lawful augmentation is conditional on the generator channel being allowed and cannot substitute for hidden-test correctness.
## 4. What would lower lawful saturation
Build edits where a shared abstraction supports both revised and retained semantics, so a validity gate alone does not determine a safe parameter update. Expose enough history to identify the current requirements and keep data generation fixed across objectives. Require independent tests of composed later edits, not only tests replayed during training. A demonstrated selective-protection failure could lower the attack to ESTIMATED R=0.44, range 0.23–0.65. Estimated cost is ESTIMATED a month of semantic-edit authoring and ESTIMATED 240 H100 GPU-h for crossed objective/history comparisons. If the only difficulty is labeling obsolete tests, it substantially overlaps ordinary contract migration.
## 5. Decisive-check GPU-h re-estimate
Old budget: ESTIMATED 9 GPU-h. New ESTIMATED 168 H100 GPU-h assumes an ESTIMATED 1B-parameter repair learner, ESTIMATED 4 objective arms, ESTIMATED 3 training seeds and ESTIMATED 12 H100-hours for each complete edit-sequence fine-tune; add ESTIMATED 24 GPU-h for repair generation and retained-semantics evaluation. Total: ESTIMATED 4×3×12+24=168. CPU compilation is additional elapsed work but is not mislabeled as GPU time. The original short sequence can demonstrate one conflict; it cannot show compositional repair survives later updates across seeds. Larger learners or long program contexts would increase this estimate.
## 6. Duplicate check
FIX T08 (`fix_packets_v4/T08/packet.md`, intervention and grader opened): MODERATE, bordering on STRONG if “new program semantics” merely encode changing tool contracts. Both change learning losses to preserve valid old behavior while replacing obsolete targets. Here the subject must synthesize dependent program repairs and is tested on program invariants, so identical intervention and identical grader target are not established. The distinction needs an actual compositional program mechanism to remain meaningful.
## 7. Verdict
CUT. The ESTIMATED best-of-four breach is 0.15, and the upper projection exceeds its line by ESTIMATED 0.16. Strong contract-aware replay and selective regularization attack the declared mechanism directly; domain-specific repair terminology does not demonstrate remaining headroom.
## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget objective synthesis on independent edit histories). Grader noise UNMEASURED (planned: retraining seeds and deterministic replay of fixed generated repairs). Score ladder UNMEASURED (planned: newest-only loss, uniform protection, validity-aware protection, compositional objective and feasible stronger control).
## Screen record
id: C007
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.66
attack_single_range: 0.42-0.84
bo4_est: 0.75
pass4_est: 0.84
ub95_est: 0.91
gpuh_old: 9
gpuh_new_est: 168
duplicate_of: FIX-T08 MODERATE
kill_reason: selective validity-aware repair losses plausibly remove the gap
souping_flag: no
