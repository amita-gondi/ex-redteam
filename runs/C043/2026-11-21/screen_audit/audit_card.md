# C043 — Pretrain through storage corruption with uncertain provenance — screen audit
## 1. What the screen claimed
The screen attacked the read service with metadata checks, selective reread consensus, source-reliability histories and disagreement-based training weights. Its ESTIMATED single/bo4/pass@4/ub95 were 0.65/0.74/0.82/0.91; CUT, category DATA, rested on cheap recovery of transient corruption. These were the cited URLs:
- https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Data%20Storage/Checksums.html
- https://arxiv.org/abs/1804.06872

## 2. Evidence audit
OpenZFS documents checking against a checksum established when the block was written; uncertain provenance does not grant that trusted witness. Co-teaching concerns noisy labels, whereas damaged language-model input changes both context and target statistics. Neither source establishes clean-learning gains from a paid adaptive reread policy. Grade PARTIAL: byte-integrity primitives are well established, but the distribution of recoverable faults and the reward-producing learning policy remain unsupported.

## 3. Research done now
Scores and resource projections in this file are ESTIMATED, including all audit-record forecasts. External source results are attributed observations, not C043 measurements.
- Checksums and Their Use in ZFS — OpenZFS, undated documentation, accessed 2026 — https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Data%20Storage/Checksums.html — fetched — Trusted write-time metadata supports detection, not reconstruction from arbitrary untrusted copies. This narrows the checksum attack's legal capability.
- Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels — Bo Han et al., 2018 — https://arxiv.org/abs/1804.06872 — fetched — Selecting training examples through peer networks is a plausible ingredient, but its label-noise setup does not validate semantic text recovery.
- An Analysis of Data Corruption in the Storage Stack — Lakshmi N. Bairavasundaram et al., 2008 — https://www.usenix.org/legacy/event/fast08/tech/full_papers/bairavasundaram/bairavasundaram_html/ — fetched — Production corruption has multiple mechanisms and correlations. This argues against granting independent clean rereads without specifying the fault model.
- A Pretrainer’s Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity — Shayne Longpre et al., 2024 — https://aclanthology.org/2024.naacl-long.179/ — fetched — Model-scale curation experiments show filtering tradeoffs; losing hard-source coverage can offset cleaner training inputs.
- Pretrain Shard Corruption — Emmy Liu et al./Harbor, 2026 — https://hub.harborframework.com/tasks/terminal-bench/pretrain-shard-corruption — fetched — A concrete shard-repair benchmark exists, but its fetched task page supplies no agent solve rate. It is task evidence, not proof of autonomous recovery.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern et al., 2024 — https://arxiv.org/html/2410.07095v1 — fetched — Autonomous pipeline search succeeds on some known-recipe problems but often fails validation, limiting claims about reliability-weighted training integration.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — Research-debugging credit supports identifying corrupt data as a cause; it does not demonstrate a metered repair policy improving final loss.

## 4. Re-estimated attack
The attacker should fingerprint each read, estimate agreement conditioned on source, allocate audits where a corrected sample has highest learning value, and reserve difficult-source coverage. Relative to the provisional integrity floor, assign ESTIMATED 0.24 to transient-fault recovery, 0.18 to better source allocation and 0.16 to training weights and coverage: approximately 0.58. All increments depend on actual recoverable clean information; there is no credit for merely announcing corruption.

A literature-based scenario model places probability {0.20,0.55,0.25} on R={0.36,0.58,0.77}. The low branch has correlated rereads and false rejection of hard text; the high branch finds predominantly transient faults. Learner seeds and source mixtures widen outcomes but do not justify independent token-level errors. ESTIMATED mean=0.20×0.36+0.55×0.58+0.25×0.77=0.58, range 0.36–0.77. For independent attempts, bo4=0.77−0.19×0.75^4−0.22×0.20^4=0.71; pass@4=1−0.75^4=0.68; ub95=0.77. The old figures overstated both the expected gain and extreme tail without specifying how independent rereads could be.

## 4A. Demonstrated capability and subfield SOTA
The strongest established systems reference is verified-checksum recovery with redundant storage; the strongest fetched model-scale curation comparator is Longpre's controlled pretraining study. There is no matched SOTA result for budgeted uncertain-provenance reads followed by clean-source loss. A future R≈1 control must show native loss improvement over the complete checksum/consensus/reliability floor at equal reads and training work. Neither a filesystem checksum guarantee nor a clean-data oracle is an attainable learning reference by itself.

Two agent observations are relevant. OpenAI reports GPT-6.2 Astra at 81.85% mean research-debugging rubric credit in an internal tool-using evaluation; time, hardware and detailed scaffold for that debugging slice are undisclosed. Identifying data corruption is therefore supported more directly than implementing its learning-optimal recovery. MLE-bench's o1-preview+AIDE earned bronze or better on 16.9% of competitions with twenty-four hours and one A10. It demonstrates data-pipeline experimentation but uses direct validation feedback and twice this wall-time allowance, without paid integrity evidence.

KNOWN-RECIPE consensus is easy to describe; AGENT-DEMONSTRATED source-aware learning recovery was not found. attack_basis=LITERATURE-ONLY. Within twelve hours the agent must establish fault independence, estimate marginal clean-source value and validate its chosen audit policy. The unspecified fault process is particularly consequential: the verdict rests on assumption.

ANCHORED distribution R={0.32,0.53,0.72}, probabilities {0.20,0.62,0.18}, discounts autonomous integration and the clean-reread premise. ESTIMATED single=0.52, range 0.32–0.72; bo4=0.72−0.19×0.82^4−0.21×0.20^4=0.63; pass@4=1−0.82^4=0.55; ub95=0.72. These probabilities express the audit's hypotheses rather than empirical corruption frequencies.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT. ANCHORED verdict: CUT, UNCHANGED, through bo4 exceeding 0.60 by 0.03 and pass@4 exceeding 0.50 by 0.05. This is a provisional assumption-dependent cut, not a demonstrated saturation result. The low-complexity consensus route remains sufficient often enough under the original unconstrained corruption description, despite the substantial reduction from the old attack forecast.

## 6. Redesign
Cause (a), mature integrity/recovery stack; REDESIGNABLE. Replace independent corrupt reads with realistic persistent provenance errors: a source can consistently return a stale but syntactically valid shard. Supply accessible independent version manifests and sampled clean-source witnesses through explicitly priced interfaces. Acquiring a witness informs reliability of related shards, so the task becomes choosing scientifically useful provenance checks alongside training exposure. Dev must exhibit both costly checks that improve downstream learning and hard clean sources that simple filtering harms.

Include checksums, cache fingerprints, repeat consensus, source posteriors and robust weighting together in calibration. Repeating the same stale read no longer resolves provenance, while a legal witness-aware reference can recover the correct data. Nothing needed for diagnosis is hidden; difficult cases have a disclosed distinguishing action. Labs would benefit from reliable training on imperfect data lineage. The best attacker uses Bayesian acquisition and influence-weighted audit allocation; whether this is already sufficient remains the decisive residual risk.

Re-attack basis LITERATURE-ONLY. ESTIMATED outcomes {0.26,0.44,0.59}, weights {0.30,0.60,0.10}: single=0.40; bo4=0.59−0.15×0.90^4−0.18×0.30^4=0.49; pass@4=0.00; ub95=0.59. Pilot ESTIMATED 216 H100 GPU-h: 1B learner × four policies × two seeds × twenty-two hours on one H100=176, plus 24 final-loss evaluation and 16 disagreement-model GPU-h. Witness reads must also fit each policy's complete time ledger.

## 7. Measurement status
Rollouts UNMEASURED (planned policies across independent provenance histories). Grader noise UNMEASURED (planned paired learner/corruption repeats). Score ladder UNMEASURED (planned loss filtering, combined recovery floor, witness acquisition reference and feasible stronger acquisition control).

## Audit record
id: C043
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.65
old_bo4: 0.74
old_pass4: 0.82
old_ub95: 0.91
new_single: 0.58
new_single_range: 0.36-0.77
new_bo4: 0.71
new_pass4: 0.68
new_ub95: 0.77
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Couple persistent lineage errors to useful priced independent witnesses and final clean-source learning.
redesign_single: 0.40
redesign_bo4: 0.49
redesign_pass4: 0.00
redesign_ub95: 0.59
redesign_gpuh: 216
attack_basis: LITERATURE-ONLY
demonstrated_ref: Research Debugging, GPT-6.2 Astra, 2026; MLE-bench, o1-preview AIDE, 2024
gap_to_attack: Diagnose versus validate clean-learning recovery under paid reads
subfield_sota_ref: Verified integrity, OpenZFS, accessed 2026; pretraining curation, Longpre, 2024
anchored_single: 0.52
anchored_bo4: 0.63
anchored_pass4: 0.55
anchored_ub95: 0.72
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
