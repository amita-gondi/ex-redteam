# C055 — Search with local surrogate models that must know when to retire — screen audit
## 1. What the screen claimed
The old attack joined local trust-region Bayesian optimization, external audit experiments, changepoint detection and surrogate reset. ESTIMATED single/bo4/pass@4/ub95 were 0.74/0.82/0.95/0.94; the verdict was CUT, category DUP, with T03 STRONG because its controller already changes response models and allocation after contradictory experiments. The cited web addresses were:
- https://arxiv.org/abs/1910.01739
- https://arxiv.org/abs/0710.3742

## 2. Evidence audit
TuRBO supports local models, adaptive regions and restarts. Bayesian online changepoint detection supplies an update rule for changing sequence distributions, but not reliable discovery of bias induced by the optimizer's own proposal distribution. Their combination with an independent audit stream is reasonable human engineering; the old sources do not demonstrate autonomous lifecycle construction or the quoted training-utility gain.

Grade: PARTIAL. The algorithms are established, while their integration and marginal value above a strong controller floor are unmeasured. Duplicate status has a different evidential basis: the locally inspected T03 packet explicitly allows posterior response updates, strategy switching, rollback and a combined contextual-BO baseline. Its hypothesis is not a fixed surrogate.

## 3. Research done now
Forecasts and later experiment allocations are ESTIMATED throughout; published outcomes below retain their source meaning.
- Scalable Global Optimization via Local Bayesian Optimization — David Eriksson et al., 2019 — https://arxiv.org/abs/1910.01739 — fetched — local trust regions directly address stale global surrogate behavior, strengthening the baseline without proving retirement under adaptive selection.
- Bayesian Online Changepoint Detection — Ryan Prescott Adams and David MacKay, 2007 — https://arxiv.org/abs/0710.3742 — fetched — establishes online regime inference; its assumptions require scrutiny when audits are proposal-selected.
- Agentic Bayesian Optimization through Surrogate-Augmented Autoresearch — Paul Brunzema et al., 2026 — https://arxiv.org/html/2608.00316v2 — fetched — Sara with a lenz Bayesian backend supplies a concrete agent-managed optimization system; the reported gains are not a surrogate-retirement benchmark.
- Session report: 0.9979 → 0.9697 in 126 experiments — Claude agent reporting in Andrej Karpathy's autoresearch repository, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — shows fast multi-change training search, but remains a selected self-report with unspecified Claude version.
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering — Chan Jun Shern et al., 2024 — https://arxiv.org/html/2410.07095v1 — fetched — evidence of executed ML search is mixed, limiting extrapolation from a short-loop optimizer to a reusable lifecycle controller.

Local duplicate evidence: /workspace/task_catalog_v3_full/packets/T03.md, inspected read-only, especially its allowed controller actions, I3 response-model update and combined-control definition. This is a design comparison, not a published SOTA result or rollout measurement.

## 4. Re-estimated attack
A stronger attacker can bypass surrogate sophistication when it costs more than direct experiments. The combined candidate therefore compares TuRBO/restarts, independent residual audits, adaptive reset and a model-free elimination fallback under one ledger. On a competent integration path, ESTIMATED utility recovery is 0.20 from local adaptation, 0.17 from detecting stale regions and 0.21 from preserving useful experiments through fallback: total 0.58. These are conditional headroom allocations, not additional independently payable reward terms.

Represent recipe-level outcomes as ESTIMATED 0.31/0.58/0.76 with probabilities 0.24/0.49/0.27. The low path wastes audits or resets useful state; the upper path finds and confirms a neglected basin. ESTIMATED single=0.24×0.31+0.49×0.58+0.27×0.76=0.56, range 0.31–0.76. ESTIMATED bo4=0.31+0.27(1−0.24^4)+0.18(1−0.73^4)=0.71. ESTIMATED pass@4=1−0.73^4=0.72; ESTIMATED ub95=0.76. The screen's much higher mean assumed reliable useful audits and downstream validation, rather than deriving their costs.

## 4A. Demonstrated capability and subfield SOTA
The closest inspected contemporary system is Sara/lenz, using Claude Opus 4.8 at high reasoning with a GP backend, acquisition optimization and agent-level decisions. It reports competitive or improved sample efficiency over Ax and other agent baselines on synthetic and HPO problems. The reference north star should be final validated learning quality after lifecycle overhead against such combined optimizers, not surrogate prediction accuracy. No fetched result establishes a universal best lifecycle policy or an attainable R=1 for this private mechanism distribution.

Two measured demonstrations bound the claim. Sara/lenz demonstrates an agent operating a modular surrogate-assisted search loop with matched evaluation counts; wall-clock and accelerator totals sufficient for a twelve-hour comparison are unreported. The autoresearch Claude session reports 126 trials in approximately 10.5 hours on one H100, improving validation bits/byte from 0.997900 to 0.969686. That is relevant evidence for rapid candidate testing, but not repeated independent discovery of a retirement policy that transfers across hidden recipe changes. Neither demonstration shows unaided construction and validation of C055's complete artifact.

Thus KNOWN-RECIPE is supported, while card-wide attack_basis=LITERATURE-ONLY. The researcher must decide when to spend true measurements, calibrate selected residuals and establish actual learning gains beyond the frozen floor. A larger stipulated model may do so, but no measured probability follows from its assumed size.

ANCHORED ESTIMATED distribution: 0.19/0.46/0.69 with probabilities 0.36/0.47/0.17. The larger failure mass reflects the need to learn a transferable policy rather than optimize one training run; a successful external-audit strategy creates the upper mode. ESTIMATED single=0.36×0.19+0.47×0.46+0.17×0.69=0.40, range 0.19–0.69; ESTIMATED bo4=0.19+0.27(1−0.36^4)+0.23(1−0.83^4)=0.58; ESTIMATED pass@4=1−0.83^4=0.53; ESTIMATED ub95=0.69. Training and grader variance remain unmeasured rather than being added as a guessed standard deviation.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT numerically through ESTIMATED bo4=0.71; duplicate is independently binding. ANCHORED verdict: CUT, UNCHANGED, binding duplicate. Its assumed successful-integration tail also gives ESTIMATED pass@4=0.53, but valid reward anchors remain unresolved. The decisive fact is T03's already editable, updateable response model and identical downstream controller target. Lower confidence in autonomous optimizer invention does not create a distinct task.

The original distinctness statement contrasts C055 with a fixed-surrogate predecessor. T03's executable-reference proposal instead updates posterior predictions using live outcomes and branches from ancestors after contradictory evidence. Its baseline also includes change detection. C055 supplies no additional constrained artifact or instantiated causal interaction that separates those interventions.

## 6. Redesign
DUPLICATE-STAYS-CUT. Cause class (d): same research-controller intervention and live-training objective as T03, independently of whether either task eventually passes saturation testing. No redesign is proposed for this inventory item, as required for a STRONG duplicate. Any useful lifecycle stress cases belong in T03's validation distribution and do not justify another task count. Redesign re-attack and additional GPU budget are therefore not applicable.

## 7. Measurement status
Rollouts UNMEASURED (planned only if retained as T03 variants: fresh live-controller campaigns). Grader noise UNMEASURED (planned: paired incumbent confirmations across learner seeds). Score ladder UNMEASURED (planned: fixed predictor, restart BO, independent audits, adaptive retirement and matched model-free bypass).

## Audit record
id: C055
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.74
old_bo4: 0.82
old_pass4: 0.95
old_ub95: 0.94
new_single: 0.56
new_single_range: 0.31-0.76
new_bo4: 0.71
new_pass4: 0.72
new_ub95: 0.76
new_verdict: CUT
binding_line: duplicate
flip: none
kill_cause_class: d
redesign_status: DUPLICATE-STAYS-CUT
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: Sara lenz, Claude Opus 4.8, 2026; autoresearch report, Claude unspecified, 2026
gap_to_attack: transferable retirement policy construction and live validation
subfield_sota_ref: surrogate-augmented agent optimization, Brunzema et al., 2026
anchored_single: 0.40
anchored_bo4: 0.58
anchored_pass4: 0.53
anchored_ub95: 0.69
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
