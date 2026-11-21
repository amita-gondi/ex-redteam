# v2 RSI task designs — red-team summary

**Recommendation: 12 tasks need fixes; cut/merge 4 standalone candidates; no task earns “holds” on the available evidence.** These are design judgments, not measured saturation or exploit results.

This is a **design-level adversarial review**, not an executed 12-hour solve, live exploit session, or acceptance-bar D2/D8 certification. The inputs explicitly contain proposed designs, authoring scripts and an authoring log, not built task containers or measured b/c anchors. No attack reward, model result or sandbox exploit has been measured here. All reward predictions below are **estimates**, including conditional upper cases. “To verify” means the relevant implementation, compatibility, data or outcome is unavailable or untested.

The assumed attacker is the user’s roughly 10T research model with twelve hours and the full task cluster. That is an attack model, not an independently verified GDM specification. Paper recall and legal algorithmic generalization are valid solutions and can invalidate the task’s claimed difficulty; they should not be prohibited after the fact.

**Block labels assess the written design:** **yes** means the specification explicitly rules the attack out if implemented faithfully; **partly** means a control exists but leaves the stated boundary or objective unresolved; **no** means the current formula/contract allows the route or lacks that specific control. A design promise is not evidence of a functioning implementation. A low predicted score for a blocked attack is a credit to the design, not a verified security result.

In the tables, **F(S)** means the exact current piecewise reward: 0 for S≤b; 0.60(S−b)/(c−b) for b<S≤c; and 0.60+0.40(S−c)/(1−c) for c<S≤1. Values outside the allowed finite domain are invalid. No numeric b or c has been supplied. Therefore an unconditional numerical payout would be invented. R≈0.60 means the explicitly stated conditional estimate S≈c; R≥0.80 requires S≥(1+c)/2; R≥0.95 requires S≥c+0.875(1−c). “Up to 1” is a conditional worst case, not a prediction of success. Arithmetic examples specify their assumptions and are not experimental results.

The current floor already includes enumerated trivial methods, competent defaults and isolated insights. A named baseline truly included at its best full-budget performance should earn approximately zero on a representative fresh instance. The challenge is whether the **combined, competent attack** is actually in that floor and whether raising the floor leaves the stipulated raw ≥0.20 advantage and useful partial credit. The report does not recommend moving b after a hidden score is observed.

## Verdicts

| Task | Verdict | Main reason |
|---|---|---|
| [01A](/workspace/task_design_v2_redteam/01_data_distribution_redteam.md#task-01a) — Reconstruct a training corpus whose apparent quality rankings reverse across stages | **needs fixes** | Stage-dependent mixture search may bypass the diagnosis chain; learner/variant floors are incomplete. |
| [01B](/workspace/task_design_v2_redteam/01_data_distribution_redteam.md#task-01b) — Acquire RL experience that remains useful as the learner changes | **needs fixes** | Nonstationary bandit recipes and checkpoint gaming threaten the proposed learning-curve objective. |
| [02A](/workspace/task_design_v2_redteam/02_objectives_and_credit_redteam.md#task-02a) — Create transferable learning signal beyond a policy’s success frontier | **needs fixes** | STaR-style rationalization and hint annealing may solve the supposed zero-success barrier directly. |
| [02B](/workspace/task_design_v2_redteam/02_objectives_and_credit_redteam.md#task-02b) — Train a research agent to assign credit across delayed and irreversible tool actions | **needs fixes** | Planner demonstrations, executable memory and convex all-eight reliability can bypass credit research. |
| [03A](/workspace/task_design_v2_redteam/03_knowledge_transfer_redteam.md#task-03a) — Consolidate conflicting experts into a student that solves new joint tasks | **cut** | Cut as standalone; fold joint-transfer controls into 02A unless strong distillation leaves proven raw reserve. |
| [03B](/workspace/task_design_v2_redteam/03_knowledge_transfer_redteam.md#task-03b) — Learn a reasoning policy that allocates variable inference budgets without losing coverage | **needs fixes** | The score rewards capped correctness/coverage, with no benefit for using less than the cap. |
| [04A](/workspace/task_design_v2_redteam/04_training_fidelity_redteam.md#task-04a) — Recover useful asynchronous MoE learning across version, routing and cache boundaries | **needs fixes** | A healthy synchronous/off-policy stack may erase the chain; sampled probes leave counterfeiting risk. |
| [04B](/workspace/task_design_v2_redteam/04_training_fidelity_redteam.md#task-04b) — Co-design precision and correction for a learner whose activation distribution drifts | **needs fixes** | Standard current scaling may remove drift; the 20% speed weight cannot provide a 0.20 raw gap alone. |
| [05A](/workspace/task_design_v2_redteam/05_exact_systems_redteam.md#task-05a) — Increase exact useful serving capacity across coupled sessions, adapters and model shapes | **needs fixes** | Selective service and check/timing splits threaten goodput; exactness and demand may cap headroom. |
| [05B](/workspace/task_design_v2_redteam/05_exact_systems_redteam.md#task-05b) — Accelerate a distributed training graph while preserving updates and resumable state | **needs fixes** | Timed/check-path separation, tolerance accumulation and exactness restrictions require a concrete contract. |
| [06A](/workspace/task_design_v2_redteam/06_architecture_resource_codesign_redteam.md#task-06a) — Build a recoverable compressed attention state across long-context workloads | **needs fixes** | The quarter-size KV envelope has strong known quantization attacks; the fixed schema limits novel research. |
| [06B](/workspace/task_design_v2_redteam/06_architecture_resource_codesign_redteam.md#task-06b) — Train one elastic model whose representations survive several deployment envelopes | **cut** | Standard nested-model distillation is the task’s core recipe; sharing identity does not exclude independent capacity. |
| [07A](/workspace/task_design_v2_redteam/07_measurement_and_reward_redteam.md#task-07a) — Repair an RL measurement ecosystem and prove that optimization learns the intended skill | **needs fixes** | Adaptive attacker obstruction and 60% checker credit can win without better learned capability. |
| [07B](/workspace/task_design_v2_redteam/07_measurement_and_reward_redteam.md#task-07b) — Train an evidence evaluator that remains useful when researchers optimize against it | **needs fixes** | Renderer computation, finite-attacker gaming and evidence-limited truth threaten valid evaluator rewards. |
| [08A](/workspace/task_design_v2_redteam/08_experimental_design_and_transfer_redteam.md#task-08a) — Design proxy experiments that transfer a continued-pretraining policy across scale and horizon | **cut** | The exp(−loss) utility compresses the primary science; the controller can outsource search to grading. |
| [08B](/workspace/task_design_v2_redteam/08_experimental_design_and_transfer_redteam.md#task-08b) — Co-design midtraining for the downstream learning it enables | **cut** | Merge into 01A: final capability does not identify improved trainability or necessary experimental design. |

## Top 10 cross-cutting issues

### 1. The objective can reward the wrong outcome.

03B rewards correctness under caps, not actual savings; 02B’s all-eight term favors concentrating success; 07A can award 60% checker utility without improved learning; 08B does not identify trainability.

Evidence: [03B §Reward](/workspace/task_design_v2_codex/03_knowledge_transfer.md:259); [02B §Reward](/workspace/task_design_v2_codex/02_objectives_and_credit.md:259); [07A §Reward](/workspace/task_design_v2_codex/07_measurement_and_reward.md:127); [08B §Reward](/workspace/task_design_v2_codex/08_experimental_design_and_transfer.md:259).

**Fix:** Define the scientific estimand first, then align reward and controls. Preserve useful partial credit; do not add undocumented post-hoc gates. Bar C5/B9/A1.

### 2. Combined known methods may bypass the proposed chain.

DoGE-style stage weighting, STaR/planner demonstrations, verifier-filtered GKD, current FP8 scaling, low-bit KV/TurboQuant and nested-transformer distillation can directly implement the final policy. Several are mentioned generically, but none has measured raw deficit.

Evidence: [01A §E2/E3](/workspace/task_design_v2_codex/01_data_distribution.md:190); [02A §E2/E3](/workspace/task_design_v2_codex/02_objectives_and_credit.md:190); [03A §E2/E3](/workspace/task_design_v2_codex/03_knowledge_transfer.md:190); [04B §E2/E3](/workspace/task_design_v2_codex/04_training_fidelity.md:322); [06A §E2/E3](/workspace/task_design_v2_codex/06_architecture_resource_codesign.md:190); [06B §E2/E3](/workspace/task_design_v2_codex/06_architecture_resource_codesign.md:322).

**Fix:** Run strong complete recipes, combined fixes, whole-stack replacement and no-diagnosis search at the same budget. Floor them only on independent calibration and cut if physical reserve disappears. Bar A5/A8/B2/B4.

### 3. Executable artifact boundaries are still promises.

A typed loss can inject updates; memory can emit plans; a renderer can reimplement a checker; masks/adapters can partition independent capacity. Reconstruction and byte caps alone do not prove the intended intervention.

Evidence: [02A §Environment](/workspace/task_design_v2_codex/02_objectives_and_credit.md:85); [02B §Environment](/workspace/task_design_v2_codex/02_objectives_and_credit.md:217); [07B §Environment](/workspace/task_design_v2_codex/07_measurement_and_reward.md:217); [06B §Environment](/workspace/task_design_v2_codex/06_architecture_resource_codesign.md:217).

**Fix:** Specify and prototype the actual dataflow/action APIs. Test procedural payloads and external-planner/checker equivalents before freezing. Retain legitimate methods, or change the task’s claim. Bar D3/D5/D9/D10.

### 4. Formal perfect scores and rooflines can still manufacture apparent slack.

The designs explicitly warn against this, but no constrained optima or numeric anchors exist. In 04B equal-quality speed improvement is <0.20 raw for any positive efficiency floor; 08A’s exp(−loss) can make loss progress nearly dead. Demand can cap 05A before hardware does.

Evidence: [04B §Reward](/workspace/task_design_v2_codex/04_training_fidelity.md:259); [08A §Reward](/workspace/task_design_v2_codex/08_experimental_design_and_transfer.md:127); [05A §Reward](/workspace/task_design_v2_codex/05_exact_systems.md:127).

**Fix:** Apply the existing raw-headroom gate to attainable native outcomes before a rollout. Measure stronger legal controls and actual physical limits; cut infeasible metrics instead of rescaling noise. Bar B3/B4/B9; GDM MF-2/SP-1.

### 5. Aggregate means allow strategic abandonment; hard validity limits can create cliffs.

Averaging can hide learner×domain, budget, deployment or workload failures. Unspecified 0.02 non-regression rules can also zero unrelated progress on one noisy slice. Equal family weights do not prevent within-family request shedding.

Evidence: [01A §Reward](/workspace/task_design_v2_codex/01_data_distribution.md:127); [03B §Reward](/workspace/task_design_v2_codex/03_knowledge_transfer.md:259); [04B §Reward](/workspace/task_design_v2_codex/04_training_fidelity.md:259); [05A §Reward](/workspace/task_design_v2_codex/05_exact_systems.md:127); [05B §Reward](/workspace/task_design_v2_codex/05_exact_systems.md:259); [06B §Reward](/workspace/task_design_v2_codex/06_architecture_resource_codesign.md:259); [08B §Reward](/workspace/task_design_v2_codex/08_experimental_design_and_transfer.md:259).

**Fix:** Freeze denominators, weights, slice definitions and noise treatment. Use disclosed continuous penalties or meaningful service floors, and test deliberate slice abandonment and one-item boundary changes. Bar B9/C5/C6.

### 6. Probe/timing separation and candidate-controlled attacker health create new grader games.

Correctness on sampled or separate probes does not establish valid timed work. A checker/evaluator can make its finite attacker slow, uninformative or optimizer-specific and receive apparent robustness.

Evidence: [04A §Verification](/workspace/task_design_v2_codex/04_training_fidelity.md:121); [04B §Verification](/workspace/task_design_v2_codex/04_training_fidelity.md:253); [05A §Verification](/workspace/task_design_v2_codex/05_exact_systems.md:121); [05B §Verification](/workspace/task_design_v2_codex/05_exact_systems.md:253); [07A §Verification](/workspace/task_design_v2_codex/07_measurement_and_reward.md:121); [07B §Verification](/workspace/task_design_v2_codex/07_measurement_and_reward.md:253).

**Fix:** Bind checks to credited execution, choose audits after work, verify cold resume and completed work externally, and score attacker health plus independent search budgets. Bar C1/D1/D8; GDM RH-2b/RH-3.

### 7. Secret seeds do not establish secret content or new reasoning.

A small/reused PRNG space can expose exact items; even secure seeds only randomize instances of known algorithms. Public-answer recall and a legal universal training solver can remain effective offline.

Evidence: [01A §Environment](/workspace/task_design_v2_codex/01_data_distribution.md:85); [01B §Environment](/workspace/task_design_v2_codex/01_data_distribution.md:217); [02A §Environment](/workspace/task_design_v2_codex/02_objectives_and_credit.md:85); [06A §Environment](/workspace/task_design_v2_codex/06_architecture_resource_codesign.md:85).

**Fix:** Use high-entropy independent keyed generation, inspect images/caches/logs, and test public/generator fingerprints. Add independently authored semantic families and legal algorithmic-solver controls. Bar A9/D3/E8; GDM AS-1/AS-2.

### 8. A rate-limited aggregate service remains an adaptive oracle.

The proposed 120 calls and fixed strata limit queries but have no stated information/generalization guarantee. Adaptive search can select noise or fingerprint low-entropy generator hypotheses without per-item outputs.

Evidence: [01A §Environment](/workspace/task_design_v2_codex/01_data_distribution.md:85); [03A §Environment](/workspace/task_design_v2_codex/03_knowledge_transfer.md:85); [07B §Environment](/workspace/task_design_v2_codex/07_measurement_and_reward.md:217); [08A §Environment](/workspace/task_design_v2_codex/08_experimental_design_and_transfer.md:85).

**Fix:** Run an adaptive-query red team at the real cap; justify response precision/noise/refresh policy, preserve an untouched bank, and verify dev-to-hidden method ranking. Bar C7/D10/E8; GDM MF-4/MF-5; [P17](https://arxiv.org/abs/1506.02629).

### 9. The saturation study cannot certify the target attacker, and its absolute thresholds can miss a low physical ceiling.

Four confounded pairings, three instance blocks and one 24h step cannot tightly identify behavior of an unavailable 10T solver. Absolute max≤0.70 can pass even when the attainable normalized ceiling is 0.68.

Evidence: [overview §Saturation resistance is a release gate](/workspace/task_design_v2_codex/00_overview.md:91).

**Fix:** Retain honest conditional projections and HOLD on wide uncertainty; independently bound achievable native improvement and test adaptive/parallel researcher compute separately. Never infer 10T resistance from a low 8B subject score. Bar A2/A6/B4 plus the user’s saturation gate.

### 10. Budgeted validation does not yet specify feasible or complete experiments.

The verified ledger arithmetic is 3,433,336 estimated GPU-h, including 940,380 for E6, but measured throughput, complete grading n, warmup, attacker and replay costs remain open. E6 also gives two different seed labels to cells it says it reuses; edge tests do not specify enough interventions to certify every edge.

Evidence: [overview §Validation program and evidence](/workspace/task_design_v2_codex/00_overview.md:139); [_build.py experiment-cell construction](/workspace/task_design_v2_codex/_build.py:55); [validation ledger](/workspace/task_design_v2_codex/validation_budget.csv).

**Fix:** Preserve all-task E6; pin paired seed identities, every edge intervention, exact per-grade workload and end-to-end caps after pilots. Stage cheap kills before canaries/panels; never present the budget as authorization. Bar B10/F1/F3/F5 and experiment E6/E7.

## Primitive-level flaws

| Primitive | Structural concern | Disposition |
|---|---|---|
| 01 data distribution | Distribution research is a sound intervention, but unknown labels, stage reversals and corpus size do not establish search hardness. The trusted source-ID channel is a substantial defense. The missing object is an experimentally demonstrated transfer landscape that beats outcome-driven mixture optimization, rather than a narrative explaining why the author chose its mixture. | Needs task-specific fixes and raw anchors. |
| 02 objectives and credit | Learning signals and causal credit deserve a separate primitive, but privileged supervision and planner availability can erase the very exploration problem being tested. The final fixed-model interface is essential. Method difficulty must survive a solver that converts the whole legal training generator into supervised demonstrations. | Needs task-specific fixes and raw anchors. |
| 03 knowledge transfer | Teacher transfer is real research, but heterogeneous teacher errors do not automatically require diagnosing those errors: executable filtering and on-policy distillation can perform the join directly. 03A still carries the old souping capacity/ceiling risk; 03B has a separate, repairable mismatch between allocation language and its score. | Keep the primitive conditional on task-specific fixes; cut 03A. |
| 04 training fidelity | Fidelity under distributed execution is relevant, but quality plus efficiency can reward a fallback without requiring fidelity research. The healthy reference must actually exercise the same workload. Separate end-to-end learning, update validity and physical capacity; none is proved by a printed version ledger. | Needs task-specific fixes and raw anchors. |
| 05 exact systems | Exact execution is the strongest systems primitive in profile, but strict output semantics and commodity hardware limits can make the remaining space tiny. A valid task needs a measured attainable performance interval, not only a roofline and a large source tree. The exclusion of compile time also requires a real deployment contract. | Needs task-specific fixes and raw anchors. |
| 06 architecture resource codesign | The primitive has a valid quality/resource intervention, but its bounded schema creates a tension: too narrow and it becomes configuration search, too broad and it accepts an untrusted inference program. Independent accounting must include every state tier while preserving a feasible envelope. Native persistent KV compression and whole-process memory are distinct quantities. | Keep KV feasibility; cut standalone 06B. |
| 07 measurement and reward | An independent executable outer checker is a strong foundation. The remaining danger is that the submitted measurement surface controls the optimizer’s experience: it can censor, slow or identify attacks while passing a fixed classification bank. A learned evaluator also needs truth that is observable in its permitted evidence; labels from execution alone do not guarantee that. | Needs task-specific fixes and raw anchors. |
| 08 experimental design and transfer | Experiment selection is a legitimate research skill, but executing a good final controller does not establish that informative experiments or cross-scale inference were necessary. A direct target-feedback controller can bypass that epistemic chain. The two tasks also overlap strongly with 01A’s stage-aware distribution/transfer problem. | Drop standalone 08A/08B; merge useful controls. |

The common A→C→D / B→D graph is generated from one template in [_build.py](/workspace/task_design_v2_codex/_build.py:80). That is evidence of document structure, not evidence of either falsehood or scientific necessity. The key challenge is to hold the child method fixed while replacing its parent diagnosis with a generic robust method, a direct outcome optimizer or legal demonstration generator. Zero reward for a floored single insight is not independent evidence that the insight was insufficient. The existing raw-margin and E7 edge-falsification promises must do the work. A5/A7 require measured dependencies, not a preferred reference narrative.

## Recommended cuts and merges

- **03A: cut as standalone.** Reuse conflicting-teacher and joint-composition controls in 02A. Re-entry needs a measured ≥0.20 raw gap over verifier-filtered multi-teacher on-policy distillation and composed-demonstration SFT.
- **06B: cut as standalone.** Keep as a later architecture variant only after a named nested-transformer baseline, physical sharing audit and recoverable shared-frontier gap.
- **08A: cut this version.** Re-entry requires a live pretraining metric and a decision contract that makes cross-scale experimental evidence necessary; a direct target controller is the first adversary.
- **08B: merge into 01A.** Use actual downstream adaptations as a transfer test. Create a separate task only with an operational trainability estimand and matched starting-capability controls.
- **01B/02A: conditional merge.** If the same curriculum, legal oracle demonstrations and standard RL dominate both, keep one task; distribution versus objective boundaries must be reflected in measured interventions.
- **04A/05B: retain distinct only if learning fidelity versus exact execution produces distinct evidence.** Do not duplicate a version/cache repair behind two reward curves. Use common trusted measurement infrastructure.
- **07A: preserve infrastructure if universal checking saturates it.** Do not keep a standalone research task solely by adding finite known holes.

## Credibility of saturation sections and kill rules

The common saturation protocol is an explicit **plan**, not evidence: max frontier run≤0.70; mean oracle best-of-4≤0.60; pass@4 at R≥0.60≤0.50; and a projected upper 95% score at 10× compute/one stronger tier below 0.75. Preserve the independent B4 margin, B5 learning band, C2/C6 noise and B9 liveness gates. The three S2 instance blocks are only a pilot; attempts within one instance do not provide eight independent instance draws. Pre-register instance expansion and threshold uncertainty, without dropping hard/easy blocks or retrying failed solver attempts.

These absolute reward thresholds can miss an already attained **constrained** ceiling if F(S*) is well below 1. For example, an attainable maximum reward 0.68 with rare successes can pass the max≤0.70 gate, and a low enough hit rate can pass the two best-of-k gates. This is an analytical counterexample, not a v2 measurement. Therefore independently bracket S* and report the remaining native achievable improvement, not merely the distance to formal S=1.

The available four model+harness pairings do not identify a 10T scaling law. A 24h check validates at most a local time extrapolation, not a 10× cluster/token campaign or an unavailable architecture. Low subject-model scores and larger task data do not imply difficulty for a much stronger researcher. Label all extrapolations conditional, hold when intervals are uninformative, and test full-budget combined default methods before spending on S1–S4. Every task’s own kill option must be acted on; “at-risk” must not become a permanent exception.

No task’s section establishes that a much stronger model cannot saturate it. The documents are appropriately explicit that all empirical gates are open, and several contain useful own-task cut criteria. The report’s four cuts prioritize structural/portfolio concerns before expensive validation. “Needs fixes” means a plausible task remains after a concrete repair and physical-anchor test; it does not mean ready to ship. No target count is a reason to retain any candidate.

## GDM precedent and controls worth preserving

The supplied review is dated 2026-11-12 and concerns four earlier samples. The acceptance bar also cites a separate round-2 context; this review does not pretend the supplied file is that second review. Its directly relevant findings are MF-2/SP-1 (physical ceiling), MF-3/MF-6 (dtype/format artifacts), MF-4/MF-5 (dev leakage/predictivity), RH-2b/RH-3 (in-process verdict spoofing and invented tests), AS-1–AS-4 (public answers and weak compliance), SP-7/MF-9/AS-7 (error attribution and no-grade), and AS-12/SP-6 (measurement/portability mismatch). Source: [GDM review](/workspace/model-souping-ro/souping-audit/gdm_feedback.txt).

The v2 design already makes substantial correct commitments: offline solver/no credentials; hidden assets attached after freeze; trusted parent scoring with isolated candidate workers; reconstruction from permitted assets; immutable tokenizers and explicit dtype; private content; no outer LLM judge; complete launch ledger and explicit failure statuses; C2 plus solver-run C6; matched dev/private interfaces; plain OCI portability; and staged owner-controlled rollout/spend gates. These controls block many earlier attacks **by specification**. Preserve them and obtain executable evidence; this report does not claim those old vulnerabilities remain open merely because the implementation is absent.

## Read scope, evidence limits and next concrete checks

The review covered every file in `/workspace/task_design_v2_codex/`: the ten design Markdown files, PROMPT.md, _build.py, _assemble.py, _frontmatter.py, all eight _pNN.py files, design_manifest.json, all 304 validation-budget rows, the authoring run log, PID and ten compiled Python cache files. Repeated generated text was compared with its rendered Markdown; compiled/cache content is authoring material, not an executable grader. The entire acceptance bar and supplied GDM review were also read. No authoring generator was imported or executed, because its imports write into the input tree. The report generator reads those inputs and writes only under this output folder. No task experiment, GPU training, live exploit or external write was performed.

The independently recomputed ledger totals match the overview: **3,433,336 estimated GPU-h**, with **940,380 for E6** and **1,134,164 for S1–S4**. At the design’s expressly assumed $3/GPU-h this is **$10,300,008 estimated GPU-only cost**; it is not a quote or spend authorization. The [open questions](/workspace/task_design_v2_codex/99_open_questions.md) already exclude preparation, outer inference and failed-version redesign from the fixed total. Counts/costs do not certify that the proposed evals fit their per-grade hours.

Next, implement the smallest reviewable typed-interface/probe harness, run the strongest cheap recipe and physical anchors for 06A, 04A and 05B, and exercise the formula-specific counterexamples for 03B/02B/07A. Do not launch a native canary until the bar’s F1 gates pass; full panel and outbound delivery still require their existing owner decisions. This is a recommendation for subsequent work, not an execution of those experiments or a new approval request.

## Primary source index

- **[P1](https://arxiv.org/abs/2310.15393)** [DoGE: Domain Reweighting with Generalization Estimation](https://arxiv.org/abs/2310.15393). Proxy-derived domain reweighting and inter-domain generalization; applicability to these stage-dependent tasks is an inference to test.
- **[P2](https://arxiv.org/abs/1603.06560)** [Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization](https://arxiv.org/abs/1603.06560). Successive-halving resource allocation; no published result is claimed on these proposed tasks.
- **[P3](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a4277440d50f1f15d2cb4c14f7e0c0d2-Abstract-Conference.html)** [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a4277440d50f1f15d2cb4c14f7e0c0d2-Abstract-Conference.html). A concrete dynamic-sampling RL baseline, not evidence that its default solves 01B.
- **[P4](https://arxiv.org/abs/2203.14465)** [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465). Rationalization using correct answers followed by training on successful rationales; transfer to the proposed private compositions is to verify.
- **[P5](https://arxiv.org/abs/1806.07857)** [RUDDER: Return Decomposition for Delayed Rewards](https://arxiv.org/abs/1806.07857). Generic return redistribution for delayed rewards; applying it to an 8B workflow policy is an untested adaptation.
- **[P6](https://arxiv.org/abs/2306.13649)** [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649). The cited on-policy/generalized distillation baseline. Multi-teacher executable filtering here is a proposed attack composition.
- **[P7](https://proceedings.mlr.press/v80/espeholt18a.html)** [IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures](https://proceedings.mlr.press/v80/espeholt18a.html). A standard off-policy correction precedent; MoE cache/routing integration remains to verify.
- **[P8](https://github.com/verl-project/verl)** [verl official repository](https://github.com/verl-project/verl). A real upstream named by v2. No particular defect, fix commit or compatible latest release is asserted; those are to verify.
- **[P9](https://docs.nvidia.com/deeplearning/transformer-engine/features/low_precision_training/fp8_current_scaling/fp8_current_scaling.html)** [NVIDIA Transformer Engine: FP8 Current Scaling](https://docs.nvidia.com/deeplearning/transformer-engine/features/low_precision_training/fp8_current_scaling/fp8_current_scaling.html). Read alongside NVIDIA’s delayed-scaling documentation: [additional primary source](https://docs.nvidia.com/deeplearning/transformer-engine/features/low_precision_training/fp8_delayed_scaling/fp8_delayed_scaling.html) . These are known scaling options; exact pinned-kernel support is to verify.
- **[P10](https://github.com/pytorch/torchtitan)** [TorchTitan official repository](https://github.com/pytorch/torchtitan). A real candidate inherited platform. No exactness-compatible speedup or particular upstream patch is claimed.
- **[P11](https://arxiv.org/abs/2402.02750)** [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](https://arxiv.org/abs/2402.02750). Also KVQuant: [additional primary source](https://arxiv.org/abs/2401.18079) . These establish concrete low-bit baselines; their performance on this checkpoint, resource accountant and workload is to verify.
- **[P12](https://arxiv.org/abs/2504.19874)** [TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://arxiv.org/abs/2504.19874). Google Research’s primary announcement is dated March 24, 2026: [additional primary source](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) . Its existence and method are verified; its v2 reward, compatibility and full resource cost are unmeasured.
- **[P13](https://arxiv.org/abs/2310.07707)** [MatFormer: Nested Transformer for Elastic Inference](https://arxiv.org/abs/2310.07707). Also DynaBERT: [additional primary source](https://arxiv.org/abs/2004.04037) . Nested/adaptive transformer prior art; efficient recovery from the proposed decoder checkpoint is to verify.
- **[P14](https://arxiv.org/abs/2210.10760)** [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760). Evidence that optimization against an imperfect proxy can reduce true quality; the particular finite-attacker counterstrategies here are red-team hypotheses.
- **[P15](https://arxiv.org/abs/2203.03466)** [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2203.03466). A concrete transfer baseline when parameterization permits it; a history-dependent continuation controller is a proposed extension.
- **[P16](https://arxiv.org/abs/1711.09846)** [Population Based Training of Neural Networks](https://arxiv.org/abs/1711.09846). A generic online schedule-search baseline, not a published solution to the proposed target states.
- **[P17](https://arxiv.org/abs/1506.02629)** [Generalization in Adaptive Data Analysis and Holdout Reuse](https://arxiv.org/abs/1506.02629). Motivates controlling adaptive holdout reuse. A throttle alone is not a privacy or generalization proof; no complete v2 bank reconstruction is claimed.
