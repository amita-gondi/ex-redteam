# C112 — Recover scientific images while learning a better acquisition policy — screen audit
## 1. What the screen claimed
The earlier CONDITIONAL combined joint reconstruction/sampling, decision-oriented experimental design, posterior reconstructions, residual preservation and recurrent sensing. ESTIMATED single/bo4/pass@4/ub95 were 0.45/0.55/0.33/0.72; no kill category was assigned, with observation aliases and raw-input bypasses unresolved. Its URLs were https://arxiv.org/abs/1907.11374, https://arxiv.org/abs/2103.02438 and https://proceedings.neurips.cc/paper_files/paper/2024/hash/c59f05d7ab3638b138cc61f32e1a7cd1-Abstract-Conference.html.
## 2. Evidence audit
Deep-learning-based Optimization of the Under-sampling Pattern in MRI — Cagla D. Bahadir, 2019, revised 2020 — fetched at the first URL, learns reconstruction and a sampling pattern, rather than an adaptive causal-image learner. Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design — Adam Foster, 2021 — second URL, fetched, validates sequential experiment policies. Amortized Bayesian Experimental Design for Decision-Making — Daolang Huang, 2024 — third URL, fetched, directly targets downstream decisions, strengthening the old attack beyond generic information gain.

Grade PARTIAL. These are genuine results for relevant components; none demonstrates restoration-induced uncertainty loss, adaptive acquisition and subsequent learner training under one resource contract. The independent scene mechanisms, sensor likelihood and downstream task distribution remain unspecified. Consequently neither the old residual nor the apparent integrated solution is quantitatively established.
## 3. Research done now
- Adaptive Compressed Sensing with Diffusion-Based Posterior Sampling — Noam Elata, 2024 — https://arxiv.org/abs/2407.08256 — fetched — AdaSense selects measurements from posterior samples, increasing confidence that a strong restoration/acquisition baseline is readily available.
- Learned, uncertainty-driven adaptive acquisition for photon-efficient scanning microscopy — Cassandra Tong Ye, 2025 — https://pubmed.ncbi.nlm.nih.gov/40798069/ — fetched — experimental microscopy shows uncertainty-guided rescanning can recover fine features and reduce hallucinations; this raises the domain-specific attack substantially.
- Classification-oriented adaptive sensing via posterior sampling — Andriy Enttsel, 2026 — https://arxiv.org/abs/2609.21812 — fetched — semantic uncertainty improves measurement/accuracy trade-offs on MNIST/CIFAR-10, but those are far simpler than causal scientific-image tasks.
- PaperBench Science: expanding PaperBench into scientific domains — Elvis Zhang Research/Pipeline Lab, 2026 — https://pipelinelab.ai/blog/paperbench-expanded/ — fetched — identifies scientific validation as a persistent weakness, limiting transfer from a usable imaging recipe to trusted autonomous co-design.
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search — Yutaro Yamada, 2025 — https://arxiv.org/html/2504.08066v1 — fetched — confirms autonomous experimentation is possible while leaving observation-model validation outside the demonstrated result.

Searches covered adaptive compressed sensing, scientific microscopy and decision-focused acquisition. All eight cited works were fetched in this session; there is no search-only support in the estimate.
## 4. Re-estimated attack
The complete attack should use likelihood-conditioned posterior samples, raw acquired data, a task-sensitive sensing criterion and retraining on acquired evidence. ESTIMATED central contribution is 0.23 from recovering usable image information, 0.18 from adaptive sampling and 0.11 from aligning selection with the downstream task: total 0.52 above a provisional competent floor. The decomposition does not award reconstruction metrics as separate reward. Its unrecovered utility is shared prior misspecification and the downstream learner's response to a changed acquisition distribution.

ESTIMATED distribution: scores 0.28/0.52/0.74 at probabilities 0.22/0.62/0.16. Low runs rescan the wrong structure, typical runs recover ordinary features, and high runs identify task-relevant uncertainty affordably. Mean=0.50, range 0.28–0.74; E[max4]=0.74−0.22×0.84^4−0.24×0.22^4=0.63. With p=0.16, pass@4=1−0.84^4=0.50 rounded (unrounded 0.5021); q95=0.74. Prior/model choice and successful sensor-policy integration dominate spread; sensor noise and learner seeds add within-regime variability that still needs measurement. New microscopy evidence raises this literature-conditional forecast above the old one.
## 4A. Demonstrated capability and subfield SOTA
Ye's experimental result reports up to 16× lower acquisition time and light dose while recovering fine structure, a much more relevant reference than image-denoising PSNR alone. AdaSense and Enttsel's classification-oriented extension are additional strong comparators. No single ranking covers their distinct sensing physics and objectives, so universal SOTA is unverified. The card's R≈1 must be an attainable same-sensor-cost causal-task pipeline beating these controls; the private learner's achievable completion cannot be inferred from a microscopy acceleration ratio.

Two fetched agent studies constrain the autonomous research claim. Pipeline Lab's GPT-6 Astra obtains 59.08% partial scientific-reproduction credit and 13.98% full reproduction; the opened report does not establish the exact scaffold, accelerator budget or per-run timing. It validates some scientific workflow autonomy, not a learned adaptive imager. AI Scientist-v2 uses Sonnet 3.5 and GPT-4o in experiment-tree scaffolding with a fifteen-hour cap and one accepted paper among three selected submissions. GPU totals are unreported in the fetched text. Producing a research artifact differs from checking that an inverse model preserves precisely the evidence needed for another learner.

KNOWN-RECIPE is strong for posterior acquisition and real microscopy rescanning. No AGENT-DEMONSTRATED result located integrates restoration, sensor actions and downstream training within twelve hours. attack_basis=LITERATURE-ONLY. The necessary unsupported work is adapting the likelihood/prior, diagnosing confident shared errors and validating causal completion beyond reconstruction appearance.

ANCHORED ESTIMATED scenarios are 0.20 (0.33), 0.43 (0.59), 0.66 (0.08). The central outcome credits 0.21 restoration, 0.14 sensing and 0.08 independently confirmed task alignment. Mean=0.37, range 0.20–0.66; bo4=0.66−0.23×0.92^4−0.23×0.33^4=0.49; pass@4=1−0.92^4=0.28; q95=0.66. Those are judgmental scenario weights, with the lower high-case probability reflecting the unverified integration gap. The verdict rests on assumption and unmeasured reward anchors, rather than treating benchmark partial credit as a reward conversion.
## 5. Verdict under the kill lines
Section 4 is CUT, binding bo4 at roughly 0.03 over the line, with pass@4 also narrowly over before rounding. ANCHORED verdict PASS-SCREEN, FLIPPED CONDITIONAL→PASS-SCREEN: margins are 0.33 for single, 0.11 for bo4, 0.22 for pass@4 and 0.09 for ub95. Stronger human-built imaging methods raise the recipe attack; lack of a comparable autonomous imaging-research demonstration lowers confidence that the whole chain can be discovered and validated during the allowed attempt. This is a forecast judgment, not measured release clearance.
## 6. Redesign
NOT-NEEDED: the amended headline forecast clears every kill line with margin, so additional task difficulty is not justified by this audit. Class na. A build must still preserve the original real research question: useful raw observations and sensor actions remain available, the downstream task must be identifiable without the clean image, and a direct raw-observation policy is a lawful comparator. These are feasibility and baseline obligations, not hidden restrictions. If real rescanning plus task disagreement solves the task, it should invalidate the difficulty hypothesis rather than trigger an artificial prohibition on the successful method.
## 7. Measurement status
Rollouts UNMEASURED (planned: independent full restoration/acquisition/downstream-learning campaigns). Grader noise UNMEASURED (planned: fixed-policy sensor-noise repeats and downstream retraining). Score ladder UNMEASURED (planned: uniform sampling, posterior sensing, microscopy-style rescanning, semantic acquisition, raw-input policy and feasible stronger causal-task pipeline, all in native completion per total cost).
## Audit record
id: C112
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.45
old_bo4: 0.55
old_pass4: 0.33
old_ub95: 0.72
new_single: 0.50
new_single_range: 0.28-0.74
new_bo4: 0.63
new_pass4: 0.50
new_ub95: 0.74
new_verdict: CUT
binding_line: bo4>0.60
flip: CONDITIONAL->CUT
kill_cause_class: na
redesign_status: NOT-NEEDED
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: PaperBench Science, GPT-6 Astra, 2026; AI Scientist-v2, Sonnet 3.5 and GPT-4o, 2025
gap_to_attack: causal imaging and sensor-policy co-design with downstream training
subfield_sota_ref: uncertainty-driven microscopy, Ye, 2025; AdaSense, Elata, 2024; semantic sensing, Enttsel, 2026
anchored_single: 0.37
anchored_bo4: 0.49
anchored_pass4: 0.28
anchored_ub95: 0.66
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CONDITIONAL->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
