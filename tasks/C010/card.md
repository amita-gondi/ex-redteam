# C010 — Train through delayed simulator corrections

**Generator:** G1. **Seeds:** S010. **Stage × artifact:** training × data. **Modality:** robotics.

## Problem

An inherited robot training stream receives corrected contact labels after newer trajectories have been learned. Select what to retain and revisit.

## Why known recipes plateau

FIFO replay and uniform relabeling erase the rare states needed to propagate corrections.

## Deterministic grader

Apply transcript-like contact corrections at their committed arrival times, then continue robot-policy training from the same initial state. Score completion on new manipulation episodes and count replay bytes throughout, including stored observations needed to propagate a correction backward.

## Hidden-score design

New contact geometries and delayed correction causes; dev shares delay and storage distributions.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED attack R≈0.44** — Use prioritized replay, relabel corrected transitions and retain recurrent burn-in windows. This captures nearby effects, but a delayed contact revision may alter the meaning of earlier unretained states far outside a fixed window.

## Saturation note vs 10T / 12h

If local relabeling reaches the final private utility, there is no need for causal trace retention. Increasing correction delay alone cannot establish a new insight unless it changes which earlier experience is sufficient for learning.

## Cheapest decisive check

**ESTIMATED pilot: 14 GPU-h** — Compare FIFO, ordinary prioritized relabeling and dependency-aware retention through one correction wave. Look for recovery on geometries absent from the replayed trajectories, not just lower loss on relabeled samples.

## GDM Round 2 compliance and shape

**Accepted shape:** pretraining_latest; **ESTIMATED live-attack/fix allowance:** 42 GPU-h — Corrections must be delivered by the simulator's chronology service; the submitted buffer cannot pull later contact truth into an earlier training update.

## DISTINCTNESS NOTE

**Nearest existing task:** [T13](../../task_catalog_v3_full/packets/T13.md) —  Training reacts to retroactive simulator truth changes rather than passive-video action reconstruction.
