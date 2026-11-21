# C044 — Choose pretraining architectures using downstream editability — screen audit
## 1. What the screen claimed
The screen proposed sequential adaptation probes, gradient-interference measurements and a cost-sensitive Bayesian architecture selector. ESTIMATED single=0.48, bo4=0.57, pass@4=0.37 and ub95=0.72 supported CONDITIONAL, with no kill category entered; its condition was meaningful architecture-ranking reversals after dependent edits. It cited:
- https://arxiv.org/abs/2004.00345
- https://arxiv.org/abs/2110.11309
- https://proceedings.neurips.cc/paper/2013/hash/f33ba15effa5c10e873bf3842afb46a6-Abstract.html

## 2. Evidence audit
Editable Neural Networks shows that training can encourage later correction, while MEND demonstrates a learned editing procedure. C044 freezes downstream adaptation, so neither establishes that architecture properties measured cheaply predict executable code behavior after successive updates. Multi-task Bayesian optimization supports experimental allocation only when the transfer surrogate carries useful information. Evidence grade PARTIAL: selection machinery exists, but the architecture-to-future-editability relation remains the load-bearing extrapolation.

## 3. Research done now
The card-level distributions, their probabilities and every forecast recorded below are ESTIMATED. No architecture or adaptation run was executed.
- Editable Neural Networks — Anton Sinitsin et al., 2020 — https://arxiv.org/abs/2004.00345 — fetched — Editing-friendly training succeeds in image classification and translation. It supports measuring editability, with a substantial modality and intervention gap to architecture selection for code updates.
- Fast Model Editing at Scale — Eric Mitchell et al., 2021, revised 2022 — https://arxiv.org/abs/2110.11309 — fetched — MEND provides local gradient transformations for large pretrained models; substituting that editor would violate the frozen-adaptation contract, so it is evidence about probes rather than a complete attack.
- Multi-Task Bayesian Optimization — Kevin Swersky et al., 2013 — https://proceedings.neurips.cc/paper/2013/hash/f33ba15effa5c10e873bf3842afb46a6-Abstract.html — fetched — Shared-task surrogates justify adaptive experiment allocation, but not extrapolating unseen interference mechanisms from unrelated probe tasks.
- The Mirage of Model Editing: Revisiting Evaluation in the Wild — Wanli Yang et al., 2025 — https://aclanthology.org/2025.acl-long.745/ — fetched — Realistic decoding exposes large failures concealed by editing benchmarks. This lowers confidence that a convenient locality proxy tracks the executable old/new utility that C044 actually pays.
- Norm Anchors Make Model Edits Last — Mingda Liu et al., 2026 — https://arxiv.org/abs/2602.02543 — fetched — A norm-feedback mechanism and a simple stabilizer change long-horizon editing behavior substantially. That raises the value of mechanistic probes but warns that initial gradients alone can miss later failure modes.
- Session report: 0.9979 → 0.9697 in 126 experiments — agent posting for Andrej Karpathy, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — A Claude-driven training search includes architecture/configuration changes within an overnight budget. Its direct loss feedback is much cheaper than pretrain-then-edit evaluation, so transfer to C044 is limited.
- PaperBench: Evaluating AI’s Ability to Replicate AI Research — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched — Reproduction failures caution that implementing an interference metric is easier than validating the downstream conclusion.

## 4. Re-estimated attack
Use legal candidate architectures, equal-cost training probes, retained-behavior tests and short dependent edit chains. Fit a surrogate of final executable utility, then spend additional trials where architecture ordering is uncertain. Above the required loss-plus-adaptation floor, credit ESTIMATED 0.11 to avoiding obviously poor local adaptation, 0.18 to better probe allocation and 0.14 to detecting sequential interference: total 0.43. The residual is not implementing Bayesian search; it is obtaining enough causally relevant evidence before the architecture choice becomes irreversible.

Literature-conditioned outcomes are R={0.24,0.45,0.67} with masses {0.25,0.60,0.15}. Pretraining seeds, choice of code-edit family and whether the probe catches a delayed failure produce the spread. Mean=0.25×0.24+0.60×0.45+0.15×0.67=0.43, range 0.24–0.67. ESTIMATED bo4=0.67−0.22×0.85^4−0.21×0.25^4=0.55; pass@4=1−0.85^4=0.48; ub95=0.67. The old estimates gave a smaller repeated-attempt success probability despite a higher mean; the explicit successful-probe branch explains this difference instead of imposing a constant bo4 uplift.

## 4A. Demonstrated capability and subfield SOTA
Current editing SOTA is metric-dependent: Liu's norm anchoring extends usable editing horizons by more than fourfold across tested backbones/editors, while Yang's WILD evaluation shows how familiar benchmark success can collapse under deployment-like decoding. Neither is a best architecture-selection result with fixed adaptation. Anchor the reference to reproducible executable edit-chain outcomes after equal pretraining budgets, using these papers to choose failure-sensitive probes. A numerical R≈1 cannot yet be tied to a matched published champion.

The autoresearch report names Claude, without a version, operating the edit/train/retain scaffold for approximately 10.5 hours on an H100. It reports loss moving from 0.997900 to 0.969686. This is self-reported evidence that coupled small-model choices can be searched, not that their downstream editability can be predicted. PaperBench reports o1+IterativeAgent at 24.4% replication credit with twelve-hour attempts and one A10; its incomplete empirical closure is relevant to the need to replay old and new code behavior after several updates. Neither benchmark's score is substituted into C044's reward units.

KNOWN-RECIPE architecture HPO is available; AGENT-DEMONSTRATED selection for delayed code editability is absent in fetched sources. attack_basis=LITERATURE-ONLY. An agent must discover a useful probe, validate ranking transfer across training states, and choose an architecture within twelve hours despite each final outcome requiring downstream adaptation.

ANCHORED distribution uses four outcomes {0.20,0.40,0.62,0.78}, probabilities {0.25,0.65,0.08,0.02}. The rare top branch allows a simple architecture to dominate; it is not evidence that such domination is likely. ESTIMATED single=0.25×0.20+0.65×0.40+0.08×0.62+0.02×0.78=0.38, range 0.20–0.78. bo4=0.78−0.16×0.98^4−0.22×0.90^4−0.20×0.25^4=0.49. With p=0.10, pass@4=1−0.90^4=0.34; cumulative mass reaches 0.98 at 0.62, giving ub95=0.62. Independent restart probabilities are assumptions, and a future observed score over 0.70 would still immediately kill the task.

## 5. Verdict under the kill lines
Section 4 is CONDITIONAL because bo4 sits about 0.05 below its limit and pass@4 about 0.02 below. Headline ANCHORED verdict PASS-SCREEN, FLIPPED CONDITIONAL→PASS-SCREEN: margins are 0.32 on single, 0.11 on bo4, 0.16 on pass@4 and 0.13 on ub95. The change follows the demonstrated gap between optimizing immediate training loss and validating downstream sequential editing, reinforced by WILD's proxy failures. This is an assumption-dependent screening forecast, not measured certification; native reward anchors still require construction.

## 6. Redesign
NOT-NEEDED: the strongest agent-grounded forecast has clear margins, while the existing fixed-adaptation and sequential executable-test contract targets the remaining research problem. Preserve lawful sequential-probe HPO in the floor and reject the difficulty hypothesis if one affordable architecture wins across all development mechanisms. The original matched-probe ranking-reversal requirement remains a calibration check, rather than a promise already demonstrated here.

## 7. Measurement status
Rollouts UNMEASURED (planned independent architecture-selection campaigns with charged probes). Grader noise UNMEASURED (planned repeated pretraining and update seeds on identical edit sequences). Score ladder UNMEASURED (planned loss selector, isolated-adaptation floor, sequential probe policy and stronger validated selector).

## Audit record
id: C044
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.48
old_bo4: 0.57
old_pass4: 0.37
old_ub95: 0.72
new_single: 0.43
new_single_range: 0.24-0.67
new_bo4: 0.55
new_pass4: 0.48
new_ub95: 0.67
new_verdict: CONDITIONAL
binding_line: pass4>0.50
flip: none
kill_cause_class: na
redesign_status: NOT-NEEDED
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: autoresearch, Claude unspecified, 2026; PaperBench, o1 IterativeAgent, 2025
gap_to_attack: Immediate HPO does not validate delayed code-editability rankings
subfield_sota_ref: Norm-Anchor Scaling, Liu, 2026; WILD evaluation, Yang, 2025
anchored_single: 0.38
anchored_bo4: 0.49
anchored_pass4: 0.34
anchored_ub95: 0.62
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CONDITIONAL->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
