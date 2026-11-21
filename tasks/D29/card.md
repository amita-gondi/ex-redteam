# D29 — Localize the committed event that causally determines failure

**Generator:** causal-localization recovery. **Stage × artifact:** eval/grading × model weights. **Modality:** long committed-event traces.

## Problem

An inherited evaluator correctly declares a run invalid but identifies the wrong event as its cause. Train an evaluator returning a validity bit and exactly one committed-event ID when localization is required. [Suite 9.5](/workspace/task_suites_claude.md:12097) establishes truth through intervention and replay, so a correlated suspicious event is not enough.

## Why known recipes plateau

Graph tracking, backward slicing, intervention search and synthetic causal supervision are complete recipes for bounded unique-cause traces. A possible residual is learning which event matters when local appearances are misleading and dependencies must be inferred from permitted observations. Conversely, observationally identical traces with different hidden causes make unique localization impossible, not difficult.

## Deterministic grader

Before candidate evaluation, root substitutes candidate-independent event alternatives and replays the workflow to establish eligible uniquely decisive causes. U is balanced exact validity/localization agreement with a frozen component split; export validity and causal-ID accuracy separately. No cause is inferred from the evaluator's explanation. Ambiguous or multiple-cause episodes are handled by a predeclared separate class, not filtered after submission. Apply F_D29.

## Hidden-score design

Fresh dependency structures and independent producers use matched style and trace lengths. A protected producer/graph-family proxy must predict localization performance. The evaluator sees allowed committed-event evidence, never root replay outcomes or private event-substitution keys. Ordinary-looking wrong and adversarially presented correct traces test robustness.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D29(U_slice+synthetic).** Assuming observable dependency tracking identifies the decisive event, compile a causal slicer and train on synthetic interventions, potentially reaching reference accuracy. A first-error heuristic and event-position classifier expose leakage; root must not share eligibility metadata that identifies the cause.

## Saturation note vs 10T / 12h

The researcher can synthesize the complete graph algorithm and generate labels. Only a real, identifiable learned dependency residual can protect reserve. Apply index S2/S4/S7; a forced unique-cause generator may instead make universal localization easier and should be attacked directly.

## Cheapest decisive check

**ESTIMATED: 8 GPU-h** including evaluator fitting and replay-backed tests, preceded by a CPU observational-collision audit. Compare causal slicing and synthetic supervision against the learned evaluator; cut if the former solves it or the latter lacks identifiable inputs.

## GDM Round 2 compliance and shape

Compared with agentic_search_inference_efficiency, this needs demonstrated neural evaluation work. R1 requires complete cause keys; R2 requires independent equivalent replay positives and healthy optimizers, with candidate timeouts scored as failures and no sibling-file SHA localization shortcut.

## DISTINCTNESS NOTE

**Wrong parent: v3 07B. Nearest other: [Claude Suite 5.13](/workspace/task_suites_claude.md:6537).** Validity prediction omits the causal-ID estimand. Complete incident certificates require broad evidence obligations; D29 isolates a uniquely decisive committed event verified by substitution and replay.

## Verdict

**conditional** — Retain only if causal localization is both observation-identifiable and resistant to complete slicing/synthetic-supervision recipes.
