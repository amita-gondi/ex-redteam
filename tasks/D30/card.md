# D30 — Recover temporal evidence from forward-corrupted endpoint latents

**Generator:** latent-observation recovery. **Stage × artifact:** eval/grading × model weights. **Modality:** noisy video latents and noise indices.

## Problem

A video-evaluation project asks a Wan-backbone predictor to rank temporal validity from a forward-corrupted finished-clip latent and its noise index. Submit noise-conditioned evaluator training, using the restricted interface in [Suite 15.6](/workspace/task_suites_claude.md:20802). Runtime excludes clean decoding and VAE access. This studies corrupted endpoints, not actual intermediate denoising trajectories.

## Why known recipes plateau

Correct latent scaling, timestep alignment, noise-balanced pairwise learning, pooled latent statistics and ordinary noise-aware hard mining are full baselines. A proposed residual is temporal evidence whose reliability depends jointly on event type and corruption. High noise may instead destroy identifiability, while low noise may permit trivial statistics; neither establishes research headroom.

## Deterministic grader

Root constructs exact valid/invalid temporal counterfactual clips, applies a frozen encoding/corruption process and evaluates pairwise ranking within independently calibrated informative-noise strata. U macro-averages eligible-stratum ranking accuracy, with ties and failed outputs treated by a fixed rule. Eligibility is selected on separate calibration families before hidden construction. F_D30 never rewards clean-video reconstruction or human preference guesses.

## Hidden-score design

Fresh event-order and persistence mechanisms preserve the frozen latent/noise contract. Strict dev fidelity covers noise policy, encoding scale and evidence sufficiency; a protected temporal-family proxy tests generalization. Neither pair identity, noise seeds, clean latents nor label-correlated latent energy may reveal truth. Unsupported bands are rejected prospectively, not pruned after scoring.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D30(U_noise_conditioned).** Assuming accessible latent statistics retain the relevant temporal signal, a noise-conditioned backbone with hard mining or a simple statistics head could match the reference. Compare both. Smuggling a decoder into the evaluator is invalid under the declared runtime; a truly legal latent-only algorithm remains allowed.

## Saturation note vs 10T / 12h

The target researcher can repair normalization and sweep full noise-conditioned recipes. Reserve requires an identifiable temporal-evidence interaction beyond those repairs. Index hard gates apply within the measured attainable ceiling; chance-limited high-noise bins cannot artificially depress frontier reward. Cross-state-domain efficacy is a separate unproved bridge.

## Cheapest decisive check

**ESTIMATED: 16 GPU-h** for statistics/backbone fitting and independent per-band evaluation, including repeated corruption draws. First validate exact Wan latent shape/scale and informative bands; stop on unidentifiability or a simple-head ceiling. The source's unverified port assets remain a build dependency.

## GDM Round 2 compliance and shape

This is pretraining_latest-like evaluator training. R1 precision/physical-ceiling lessons require native signal above noise; R2 demands frozen base assets, bounded checkpoint retention and no hidden-only formatting cues. No claimed upstream reproduction follows from an author analogue.

## DISTINCTNESS NOTE

**Wrong parent: [T19](/workspace/task_catalog_v3_full/packets/T19.md). Nearest other: [T23](/workspace/task_catalog_v3_full/packets/T23.md).** Pixel-based visual evaluation violates this latent-only contract. Low-cost controllability generation differs from noise-conditioned endpoint ranking; clean temporal QA is not a legal adapter.

## Verdict

**conditional** — Port readiness, informative-noise eligibility and latent-only recipe headroom must all be established; no denoising-trajectory or human-validity claim is supported.
