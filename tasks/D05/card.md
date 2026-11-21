# D05 — Generate semantic tests that distinguish skill from actor identity

**Generator:** recovered evaluation-design sketch. **Stage × artifact:** eval/grading × model weights. **Modality:** typed tasks and actor executions.

## Problem

An inherited benchmark separates named models but may be testing style recognition. Train a bounded semantic test generator to separate root-fixed capable actors from matched skill-impaired actors, following [Suite 10.6](/workspace/task_suites_claude.md:13896). Submit generator training choices and weights reconstructed through the trusted trainer; test validity comes from executable state truth.

## Why known recipes plateau

Grammar enumeration, direct prerequisite probes and adaptive difficulty search can already target a known lesion. Their possible limitation is nuisance-independent discrimination when the same skill failure appears through different task compositions. This is a design hypothesis: lesions may instead leave an easily exploited signature, making the task trivial.

## Deterministic grader

Generate tests before observing evaluation actor responses. Validate each test, run matched actor pairs under crossed irrelevant cues, and compute U as the mean capable-minus-impaired exact-success contrast over all scheduled tests. Invalid tests contribute no contrast and remain in the denominator. Report capable success and cue sensitivity to expose universally impossible tests. F_D05 supplies the calibrated outer reward.

## Hidden-score design

Withhold independently implemented lesion mechanisms and task compositions, with a protected dev lesion-family proxy. Counterbalance producer/style metadata across capability conditions. Require an observation-matched identifiability witness; a lesion distinguishable only through unavailable internal state is not a target.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D05(U_direct_probes).** Assuming each impairment corresponds to an expressible prerequisite, enumerate short valid probes, retain the most discriminative and diversify them by semantics. This may equal the reference. An identity-only generator must fail on crossed cues; actor file names and runtimes cannot expose lesion status.

## Saturation note vs 10T / 12h

The researcher can infer lesions and search the full grammar. Novelty requires tests whose usefulness depends on learned compositional diagnosis, beyond direct probes. The index hard gates include reference-reaching recipes and S2/S4/S7; adding more lesion seeds offers no defense.

## Cheapest decisive check

**ESTIMATED: 8 GPU-h** for fixed-actor execution of enumerated versus learned probes, including generator fitting. Kill if direct probes saturate or if discrimination disappears after metadata counterbalancing.

## GDM Round 2 compliance and shape

Relative to agentic_search_inference_efficiency, the edited component is a test generator, so useful GPU work must be demonstrated. R1 exact answer-key obligations apply; R2's protected-only-cue and equivalent-positive lessons require valid difficult controls and independently implemented actor variants.

## DISTINCTNESS NOTE

**Wrong parent: v3 07A. Nearest other: [v3 07B](/workspace/task_design_v3_codex/07_measurement_and_reward.md).** This creates discriminating interventions; 07B predicts validity from evidence, while 07A repairs acceptance logic. Static correctness is not intervention discrimination.

## Verdict

**conditional** — Keep only if a trained generator is necessary after complete grammar/direct-skill probing and nuisance controls.
