# D27 — Learn safe browser action groups under asynchronous deadlines

**Generator:** local-computer-use recovery. **Stage × artifact:** training × model weights. **Modality:** DOM/accessibility state and browser actions.

## Problem

An inherited local computer-use policy spends too long observing between actions, yet batching edit/save/launch/publish operations can race asynchronous commits. Train a text policy that groups safe actions and schedules observations under actual latency costs. [Suite 5.12](/workspace/task_suites_claude.md:6442) grades application state; browser implementation changes are outside the learning intervention.

## Why known recipes plateau

Dependency-aware batching, event-driven waits, deterministic commit checks, planner demonstrations and behavioral cloning are complete recipes. A possible residual concerns partial local observations whose value depends on a learned grouping policy and pending commit state. The task collapses if an ordinary dependency scheduler plus demonstrations handles it all.

## Deterministic grader

Execute the trained policy through a trusted local application runner. U is exact durable terminal database/workflow completion within the disclosed end-to-end deadline, macro-averaged over workflow classes; unsafe commits and unfinished sessions lose their own episode credit. Charge observations, actions and actual waits. F_D27 cannot reward fewer screenshots while silently failing publication or persistence.

## Hidden-score design

Fresh commit-dependency graphs and application workflows preserve public action semantics and legal local observations. Strict dev fidelity includes latency distributions, deadline pressure and cancellation behavior. Any virtual-time model needs independent physical replay validation; hidden-only delays are prohibited difficulty.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D27(U_scheduler+BC).** Assuming commit dependencies are inferable from local event state, a mature asynchronous scheduler with planner-trained actions may attain reference utility. Full-serial safe execution is a legal control at the actual deadline. Candidate-reported completion or timestamps cannot replace trusted durable-state checks.

## Saturation note vs 10T / 12h

The target researcher can synthesize dependency guards and demonstrations. Reserve must remain in learned action/observation coupling after that composite, rather than generic browser repair. Index absolute and ceiling-relative hard gates apply, and a simulator timing artifact is a validity failure before saturation analysis.

## Cheapest decisive check

**ESTIMATED: 14 GPU-h** for matched policy fitting and physical application replay, comparing serial safety, dependency batching and learned grouping. CPU/browser runtime is additional and must be priced. Stop if ordinary batching supplies all deadline-qualified gains.

## GDM Round 2 compliance and shape

This resembles agentic_search_inference_efficiency only when policy learning matters. R1 requires actual useful work and complete failure logs; R2 cold-JIT and inactive-speed-term lessons require matched warmup, physical timing and a deadline that actually binds without host-CPU ranking inversion.

## DISTINCTNESS NOTE

**Wrong parent: [T10](/workspace/task_catalog_v3_full/packets/T10.md). Nearest other: [T04](/workspace/task_catalog_v3_full/packets/T04.md).** Pixels-only observation/answer acquisition omits browser commit actions. Protocol transfer differs from deadline-constrained action grouping with exact durable application state.

## Verdict

**conditional** — Requires physical timing fidelity and a learned grouping benefit beyond dependency scheduling, with ML research dominating generic browser engineering.
