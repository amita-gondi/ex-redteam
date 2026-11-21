# D26 — Allocate trajectories for their gradients after the next update

**Generator:** gradient-acquisition recovery. **Stage × artifact:** data × code. **Modality:** RL trajectories and metered gradient sketches.

## Problem

An inherited pruning controller retains diverse current gradients but wastes future rollouts when an actor update changes interference between task families. Submit trajectory selection and future rollout allocation using trusted, versioned gradient sketches. [Suite 12.5](/workspace/task_suites_claude.md:17708) fixes correct optimizer/batch transport and makes acquisition geometry the intervention.

## Why known recipes plateau

[Gradient Surgery for Multi-Task Learning](https://arxiv.org/abs/2001.06782) establishes direct conflict handling as a known method. Combine advantage-aware pruning, unbiased sampling histories, exploration, current-gradient diversity and generic lookahead allocation. The hypothesized residual is future geometry that changes which apparently redundant trajectories become useful; current-vector diversity alone need not predict it. This remains unmeasured in the proposed task.

## Deterministic grader

Root replays selection/allocation, recomputes eligible sketches after model changes and trains the actor under equal generation/training allowances. U is exact private semantic competence across interference-sensitive and retained-skill strata. Charge every generated/rejected trajectory, backward sketch, clone update and selection computation. F_D26 ignores reported gradient diversity and paper wall-time speedups.

## Hidden-score design

Fresh task-family interactions must arise from actual model gradients, not synthetic vector tables. Strict dev fidelity covers sketch error, opportunity costs and gradient-version semantics, with protected unseen-interference proxies. Historical sketches cannot be passed off as current, and private validation gradients are never acquisition inputs.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D26(U_prune+lookahead).** Assuming affordable cloned updates predict useful geometry, complete advantage pruning plus current sketches and generic lookahead may reach reference competence. Include no-prune and direct checked-SFT controls. Reusing stale sketches for free or hiding a clone update violates trusted cost/version accounting.

## Saturation note vs 10T / 12h

The strong researcher can port the full pruning stack and perform no-diagnosis allocation search. Surviving reserve needs actual interference diagnosis→future transport→changed acquisition effects, including bypass and edge tests. Index S2/S4/S7 apply; noise-limited sketches cannot manufacture low frontier scores.

## Cheapest decisive check

**ESTIMATED: 24 GPU-h** including actual-update gradient comparisons, selector continuations and exact evaluation. Compare no-prune, competent pruning/current geometry and future-aware allocation at matched full costs; stop if geometry does not rotate usefully or lookahead closes the gap.

## GDM Round 2 compliance and shape

Like pretraining_latest, changed data determines real parameter learning. R1 demands native reserve beyond sampling noise; R2 requires immutable trainer state, per-seed timeouts and bounded typed sketches so the acquisition API cannot inject arbitrary gradients or offline weights.

## DISTINCTNESS NOTE

**Wrong parent: [T18](/workspace/task_catalog_v3_full/packets/T18.md). Nearest other: [v3 01B](/workspace/task_design_v3_codex/01_data_distribution.md).** Robust reward objectives do not allocate future trajectories. Acquisition is the closer family, but requires an explicit costed/versioned gradient-sketch API to preserve this intervention.

## Verdict

**promising** — Concrete acquisition/learning coupling with exact outcomes, contingent on real future interference and a competent complete pruning/lookahead floor.
