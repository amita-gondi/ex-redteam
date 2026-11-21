# D14 — Learn diagnoses that improve a policy's later corrections

**Generator:** diagnosis-component recovery. **Stage × artifact:** training × model weights. **Modality:** delayed action consequences.

## Problem

An inherited learner receives generic failure labels after long tool trajectories and repeats the same mistake on its next attempt. Train a separate diagnoser from permitted evidence, then use its output in the correction-learning loop. [Suite 7.10](/workspace/task_suites_claude.md:8656) makes subsequent improvement the objective; a convincing explanation is insufficient.

## Why known recipes plateau

Model-based credit, direct continuation search, generic error labels and correction demonstrations are the complete baseline. A possible gap is a diagnosis that changes which correction examples become useful after the policy updates. This could disappear if direct search supplies better continuations cheaply; no plateau is established.

## Deterministic grader

Root rebuilds the diagnoser and downstream learner, then compares fresh correction outcomes under identical starting checkpoints and training allowances. U is exact terminal success after the fixed correction budget, macro-averaged across fault families; pre-correction capability and incremental gain are both exported. Diagnoser accuracy receives no independent reward. F_D14 must favor genuine downstream improvement over fluent labels.

## Hidden-score design

Fresh delayed-consequence mechanisms separate visually similar errors with different repairs. Dev matches feedback delay and observability; a protected new-fault composition proxy validates transfer. Any observational collision receives an equivalence-class target or is removed before freeze, never arbitrarily labeled.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D14(U_continuation_search).** Assuming affordable branching and executable outcomes, search for successful continuations and train directly on them, bypassing a learned explanation. Charge rejected branches and demonstrations. A diagnoser emitting a hidden action planner violates its bounded output contract unless that broader intervention is explicitly permitted.

## Saturation note vs 10T / 12h

A strong researcher can synthesize counterfactual rollouts and train correction policies jointly. Residual difficulty must survive the bypass and show diagnosis×learner interactions with parent-off tests. Apply index S2/S4/S7 without equating low diagnosis accuracy to hard research.

## Cheapest decisive check

**ESTIMATED: 16 GPU-h** for matched continuation-search, generic-feedback and learned-diagnosis training, including held-out correction evaluation. Shuffle diagnosis while preserving token counts; stop if its causal learning benefit vanishes.

## GDM Round 2 compliance and shape

This has pretraining_latest-style measurable learning rather than report scoring. R1 noise guidance requires complete-pipeline reruns; R2 demands reconstruction through a trusted training service and per-seed deadlines, preventing precomputed corrected weights from crossing as diagnosis code.

## DISTINCTNESS NOTE

**Wrong parent: v3 02B. Nearest other: [Claude Suite 5.13](/workspace/task_suites_claude.md:6537).** Scalar delayed credit does not instantiate a diagnoser. Unlike a causal-certificate investigator, D14 earns reward only through a separate policy's later learning benefit; matched intervention tests would decide any future merge.

## Verdict

**conditional** — Needs a reproducible downstream benefit beyond continuation search and generic correction training, not merely better attribution labels.
