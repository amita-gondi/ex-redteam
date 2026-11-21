# D22 — Train the teacher on states induced by student mistakes

**Generator:** trainable-teacher recovery. **Stage × artifact:** training × model weights. **Modality:** student failure prefixes and teacher continuations.

## Problem

An inherited teacher succeeds on clean demonstrations but gives poor continuations after the student's own mistakes. Submit teacher-adapter training on legal student-induced states, then distill into a freshly rebuilt student. [Suite 7.22](/workspace/task_suites_claude.md:9520) changes teacher competence itself; teacher queries and student losses alone cannot repair an immutable deficient teacher.

## Why known recipes plateau

[A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686) provides the DAgger baseline for learning on induced states. Its lesson makes ordinary failure-state aggregation essential, not novel. Teacher SFT, a stronger fixed teacher, student-direct training and checked continuation search may remove the entire proposed gap.

## Deterministic grader

Root generates student prefixes, trains the teacher adapter using allowed outcomes, then runs the fixed student-distillation stage. U is exact teacher-free student terminal success across fresh induced-state task families; teacher accuracy is diagnostic. Charge teacher fitting, rejected continuations, queries and student training. F_D22 must not reward teacher improvement that fails to transfer.

## Hidden-score design

Private prefix mechanisms change recoverable error interactions, with a protected induced-state dev proxy. Match student competence, recovery opportunity and teacher context budgets. Hidden prefixes and answers never become teacher training examples, and deployment has no teacher endpoint.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D22(U_DAgger_teacher).** Assuming ordinary state aggregation covers recoverable student errors, teacher SFT followed by checked distillation should reach the reference. A stronger immutable teacher and direct student training test necessity; neither may be prohibited to protect the teacher-update narrative.

## Saturation note vs 10T / 12h

A powerful researcher can regenerate recovery demonstrations and select a complete teacher-training recipe. Reserve needs a demonstrated teacher-update→changed-prefix→student-transfer dependency that survives joint/direct controls. The index's absolute and ceiling-relative hard kills remain mandatory and unmeasured.

## Cheapest decisive check

**ESTIMATED: 18 GPU-h** for teacher adaptation and matched student rebuilds, including stronger-fixed-teacher and direct-training controls. Evaluate student outcomes after removing all teacher access; stop if ordinary induced-state SFT closes the gap.

## GDM Round 2 compliance and shape

This is pretraining_latest-shaped parameter research with an additional metered teacher stage. R1 requires genuine learner reserve and independent seeds; R2 requires portable lifecycle replay, pruning unused checkpoints and explicit accounting for both teacher and student rather than a free hidden teacher-training phase.

## DISTINCTNESS NOTE

**Wrong parent: [T07](/workspace/task_catalog_v3_full/packets/T07.md). Nearest other: [T17](/workspace/task_catalog_v3_full/packets/T17.md).** T07 fixes teacher weights; T17 repairs an exploited actor. D22 updates teacher conditional competence and grades transfer into a separate teacher-free student.

## Verdict

**conditional** — Retain the teacher-update treatment only if complete DAgger/SFT and stronger-fixed-teacher baselines leave student-learning reserve.
