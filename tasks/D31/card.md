# D31 — Select simulator-ranked policies for independent-user outcomes

**Generator:** ranking-transport recovery. **Stage × artifact:** eval/grading × model weights or bounded selector state. **Modality:** randomized user-cohort outcome logs.

## Problem

A simulator-validation researcher must choose among frozen assistant policies using source/bridge evidence and predict which choices help independent users. [Suite 17.9](/workspace/task_suites_claude.md:23045) requires consented private randomized outcomes, assignment/enrollment/attrition records and executable nonclinical task completion. It explicitly says that this dataset is not supplied. No user study or collection is authorized here.

## Why known recipes plateau

Randomized-arm means, supported off-policy estimation, inverse-propensity correction, standard transport and small CPU selectors may exhaust any identifiable selection signal. A learned simulator representation is only justified if it adds predictive policy-relevant information after those controls. Simulator cross-play cannot demonstrate that claim about independent users.

## Deterministic grader

If the required asset existed, freeze candidate policies and select using permitted preassignment descriptors and source/bridge logs. U would be the selected policy's intention-to-treat exact completion rate on sealed randomized cohorts, with fixed assignment-unit denominators. Disengagement is noncompletion under the source contract; missing administrative telemetry is an integrity fault. Rescoring fixed outcomes is deterministic, but cohort uncertainty remains. F_D31 needs a measured attainable candidate ceiling, not assumed perfect human success.

## Hidden-score design

Disjoint users and task mechanisms must define source, bridge and sealed cohorts before outcomes are inspected. Positive assignment support and no cross-arm interference require independent audit. A protected cohort dev proxy must predict rankings without exposing sealed outcomes. None of these private asset properties is established; simulated users are not a replacement.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D31(U_randomized_transport), currently unevaluable.** Assuming adequate support and cohort precision, a CPU randomization-aware transport selector may match the reference. Missing outcomes, selective attrition or post-treatment covariates could create false gains; these are cohort-integrity blockers, not permissible optimization strategies.

## Saturation note vs 10T / 12h

A stronger researcher can implement supported transport and best-arm selection cheaply. Resistance would require valid independent-user signal beyond that complete recipe and a substantive ML learning role. The index's S2/S4/S7 hard gates remain mandatory if assets arrive; absence of data cannot count as low frontier performance.

## Cheapest decisive check

**ESTIMATED: 0 GPU-h** for an asset/provenance/assignment inventory. The source establishes no usable private cohort, so stop. Acquisition, consent, replication and cohort precision costs are unknown and unfunded; no empirical selector reward can be reported now.

## GDM Round 2 compliance and shape

Compared with agentic_search_inference_efficiency, this lacks both the outcome asset and demonstrated GPU research. R1 requires private untouched truth; R2 requires protected data ownership and complete per-target evidence. Static deterministic rescoring cannot erase sampling uncertainty or justify idle accelerators.

## DISTINCTNESS NOTE

**Wrong parent: [T16](/workspace/task_catalog_v3_full/packets/T16.md). Nearest other: [T03](/workspace/task_catalog_v3_full/packets/T03.md).** Simulated user laws cannot certify randomized independent-user ranking transport. Research-controller experiment selection also lacks this fixed-policy, real-outcome authority.

## Verdict

**cut** — Asset-blocked: no private consented randomized outcome package is established. CPU dominance and standard-transport saturation remain additional unresolved blockers, even if data later arrive.
