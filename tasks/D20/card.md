# D20 — Amplify grounded content without amplifying teacher errors

**Generator:** synthetic-fidelity recovery. **Stage × artifact:** data × code. **Modality:** source documents and generated traces.

## Problem

An inherited synthetic-training pipeline produces plausible continuations that repeat a teacher's correlated factual mistakes. Submit the source-grounded generation/fidelity mechanism while coverage and curriculum stay fixed. [Suite 19.6](/workspace/task_suites_claude.md:24736) changes content generation itself; selecting source IDs or reordering a fixed multiset cannot express this treatment.

## Why known recipes plateau

Retrieval-grounded generation, executable fact checks, rejection sampling, direct source continued pretraining and ordinary checked SFT are the combined recipe. A possible limitation is correlated errors that survive local checks while altering compositional relations needed by the learner. This is an unmeasured source-grounding hypothesis, not a reported failure of those methods.

## Deterministic grader

Train identical learners on generated content under fixed source coverage, token exposure and ordering rules. U measures exact factual and compositional outcomes on independently authored source-grounded tasks, with ordinary domain capability separately retained. Neither teacher agreement nor generated-trace plausibility earns reward. All generation, verification and discarded samples are charged; use F_D20.

## Hidden-score design

Private source worlds introduce new relational facts and exception structures rather than public benchmark answers. A protected source-family dev proxy matches source access, context limits and factual/compositional balance. Training may legally inspect training sources; private evaluation questions and answer programs remain absent.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D20(U_checked_generation+CPT).** If source facts are fully executable and checked examples preserve the useful relations, direct source training plus checked synthesis may reach the reference. Include a source-only learner to test whether amplification is needed at all. Encoded dev facts entering through a generator script are invalid.

## Saturation note vs 10T / 12h

The researcher can extract a fact graph and synthesize verified curriculum content. Reserve must concern actual learning of source-bound compositions after that complete recipe, not extraction accuracy alone. Apply index absolute/tail/projection and S7 gates; larger corpora cannot substitute for causal edge evidence.

## Cheapest decisive check

**ESTIMATED: 20 GPU-h** including matched source-only, checked-synthetic and fidelity-aware learner runs and exact evaluation. Cross correlated teacher mistakes with source-check completeness; stop if straightforward checking or direct training removes the gain.

## GDM Round 2 compliance and shape

This directly resembles pretraining_latest. R1 forbids narrow trainer ceilings and calibration contamination; R2 requires enough balanced legal training content, protected dev gold and structural separation between generation code and immutable trainer/model assets.

## DISTINCTNESS NOTE

**Wrong parent: v3 01A. Nearest other: [T02](/workspace/task_catalog_v3_full/packets/T02.md).** Source selection cannot synthesize grounded traces. T02 discovers a continued-pretraining recipe; D20 fixes coverage/curriculum and isolates the content-fidelity mechanism rather than general recipe search.

## Verdict

**conditional** — Authentic data research if correlated compositional error remains after checked generation and direct source training; otherwise the recipe floor wins.
