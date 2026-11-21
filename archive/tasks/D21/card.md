# D21 — Co-adapt an agent's scaffold and policy under versioned replay

**Generator:** joint-treatment recovery. **Stage × artifact:** self-modification × code and model weights. **Modality:** tool protocols and policy traces.

## Problem

An inherited scaffold compresses observations and expands actions in ways the policy has learned to rely on. Changing either alone can make recorded trajectories misleading. Submit bounded scaffold code together with policy training, as in [Suite 5.4](/workspace/task_suites_claude.md:5718), under a shared resource ledger and explicit scaffold/policy versions.

## Why known recipes plateau

Harness search with a frozen actor, policy-only training, alternating optimization, replay conversion and strong joint imitation are complete controls. A possible residual is that representation changes alter which policy errors can be observed and which replay remains useful, feeding back into subsequent scaffold search. This causal coupling is unproved; ordinary joint optimization may solve it.

## Deterministic grader

Root validates scaffold action semantics, reconstructs the learner and executes the submitted pair on exact private terminal tasks. U macro-averages successful useful completion across protocols and inherited skills, within actual token/action/runtime caps. Charge replay conversion, demonstrations and failed scaffold candidates. F_D21 uses outcomes rather than code compactness or apparent replay consistency.

## Hidden-score design

New protocol compositions retain the disclosed operation semantics, with a protected unseen-composition dev proxy. Match tool latency and observation/action budgets. The scaffold cannot access goal truth or inject parameters through callbacks; policy updates travel only through the trusted trainer. Semantically valid alternative algorithms remain legal.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D21(U_alternating_joint).** If canonical replay conversion removes all representation mismatch, alternating scaffold search and policy fine-tuning may attain the reference. A strong joint demonstration optimizer is a parent-bypass baseline. Hidden planners concealed inside an observation renderer must be tested against the declared executable boundary.

## Saturation note vs 10T / 12h

The target solver can search complete scaffolds and synthesize training traces. Reserve must survive that replacement route and show version-dependent learning interactions, not merely a brittle old adapter. Index S2/S4/S7 apply to all valid scaffold/policy pairs and full selection costs.

## Cheapest decisive check

**ESTIMATED: 24 GPU-h** for scaffold-only, policy-only, alternating and joint learning comparisons, including replay rebuilding and private evaluation. Cross canonical replay conversion with adaptive scaffold changes; stop if ordinary alternation explains the whole gain.

## GDM Round 2 compliance and shape

This combines agentic_search_inference_efficiency's scaffold work with pretraining_latest's actual training. R1 requires current-version outcomes; R2 requires replay receipts, bounded code channels, immutable base assets and exact frozen submission bundles, rather than a transcript provenance audit.

## DISTINCTNESS NOTE

**Wrong parent: [T04](/workspace/task_catalog_v3_full/packets/T04.md). Nearest other: [T20](/workspace/task_catalog_v3_full/packets/T20.md).** T04 fixes the interpreter and trains the policy; T20 optimizes a frozen actor's harness. Neither preserves the joint scaffold/policy causal treatment.

## Verdict

**promising** — A clear joint intervention with genuine learning feedback, subject to full alternating/joint baselines and structural artifact isolation.
