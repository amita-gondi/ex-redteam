# D09 — Transfer a missing skill through a contaminated teacher channel

**Generator:** teacher-channel sketch recovery. **Stage × artifact:** objective × code. **Modality:** hard targets and probability traces.

## Problem

A student lacks a useful capability available in a fixed teacher, but teacher targets also carry nuisance-conditioned behavior. Starting from cached targets and failed distillation histories, submit a bounded channel filter controlling hard/soft targets and probability mass. [Suite 10.11](/workspace/task_suites_claude.md:14608) fixes the teacher; deployment must use the student alone.

## Why known recipes plateau

[Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) establishes soft-target transfer as a known recipe, not evidence of safe transfer. Temperature tuning, target masking, checked hard-target SFT and direct student training are the combined baseline. The unmeasured hypothesis is that useful relational probability information shares channels with nuisance effects and survives neither indiscriminate masking nor hard-target conversion.

## Deterministic grader

Trusted training replays the submitted filter against immutable legal teacher outputs. U measures exact teacher-free student task success under crossed nuisance conditions, retaining skill-transfer and ordinary-capability slices. A student that imitates teacher probabilities without useful terminal competence earns no proxy credit. Grade all continuation seeds and apply F_D09.

## Hidden-score design

Fresh skill/nuisance combinations use independent exact task truth. Dev contains matched teacher competence and a protected compositional proxy; hidden outcomes never control which teacher target is retained. Cached query provenance and costs are public, while teacher/test condition labels are permission-separated.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D09(U_checked_SFT).** If executable filtering preserves enough useful demonstrations, hard-target SFT can reach the reference and make soft-channel research unnecessary. Ignoring the teacher and training directly is also legal; its success kills teacher necessity. A channel callback that acts as an unmetered teacher must fail the interface boundary.

## Saturation note vs 10T / 12h

A large researcher can synthesize clean targets, repair the student objective and search temperatures jointly. A genuine gap must depend on identifiable transferable probability structure; teacher-use restrictions cannot manufacture it. Apply the index's S2/S4/S7 hard tests to complete bypasses as well as intended filters.

## Cheapest decisive check

**ESTIMATED: 14 GPU-h** for student rebuilds comparing soft distillation, checked SFT and teacher-free training at equal total data/query/training cost. Measure missing-skill acquisition before interpreting nuisance reduction.

## GDM Round 2 compliance and shape

The accepted pretraining_latest shape fits the student-learning estimand. R1 requires real trainer reserve and multi-seed uncertainty; R2 requires frozen teacher/base assets, charged caches and code-channel controls against encoded targets or offline student weights.

## DISTINCTNESS NOTE

**Wrong parent: [T17](/workspace/task_catalog_v3_full/packets/T17.md). Nearest other: [T07](/workspace/task_catalog_v3_full/packets/T07.md).** This transfers a missing skill through an immutable teacher channel; it neither repairs an already contaminated actor nor studies when to retire teacher assistance.

## Verdict

**conditional** — Advance only if checked SFT and direct student training leave a measurable channel-specific learning problem.
