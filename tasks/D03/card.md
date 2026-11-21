# D03 — Settle dense training credit across resets and reversals

**Generator:** recovered credit intervention. **Stage × artifact:** objective × reward. **Modality:** state/action trajectories.

## Problem

An inherited sparse-reward learner receives dense progress credit that survives a reset or is not repaid when progress reverses. Submit a restricted potential/value-feature and settlement mechanism; keep terminal success semantics fixed. The research question in [Suite 3.5](/workspace/task_suites_claude.md:3264) is whether limited observable features can make dense guidance teach useful terminal behavior.

## Why known recipes plateau

[Policy invariance under reward transformations: Theory and application to reward shaping](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/NgHaradaRussell-shaping-ICML1999.pdf) establishes potential-based shaping as a baseline. Correct boundary settlement is a repair, not novelty. The unmeasured residual is learning a useful potential from partial evidence after exact shaping, value learning and planner demonstrations are combined.

## Deterministic grader

Root replays training from clean initialization with the submitted shaping graph, checks reset/termination accounting, and evaluates the resulting policy using terminal predicates only. U is macro-averaged terminal success across reversible, reset-prone and ordinary workflows. Dense reward, value fit and training return are diagnostics. All attempted evaluation episodes remain in denominators; score with F_D03.

## Hidden-score design

Private prerequisite graphs change which apparent progress becomes reversible. Dev matches observation limits, rollback frequency and horizon; a protected composition proxy must rank methods predictively. The shaping graph never receives hidden terminal labels or privileged state unavailable at deployment.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D03(U_potential+planner).** Assuming planner-generated demonstrations cover useful bottlenecks, exact potential settlement plus learned values may attain the reference without a new credit method. Procedural answer planning inside a purported scalar potential must be excluded by the typed feature API; legal planner demonstrations remain allowed and charged.

## Saturation note vs 10T / 12h

The target solver knows the theorem and can generate counterfactual trajectories. Surviving difficulty must couple observability, learned potential errors and future exploration, with parent-off ablations; merely adding reset cases fails. S2/S4/S7 from the index are hard gates, presently unmeasured.

## Cheapest decisive check

**ESTIMATED: 12 GPU-h** including paired learner continuations and terminal evaluation. Compare terminal-only, exact settled shaping, learned values and demonstration-assisted shaping at equal samples; kill if the complete recipe removes native reserve.

## GDM Round 2 compliance and shape

Like pretraining_latest, actual parameter learning supplies the outcome. R1 trainer-cap and seed-lottery lessons require adequate schedules and salted multi-seed replay; R2 requires per-seed timeouts and no embedded label/weight channel in the shaping artifact.

## DISTINCTNESS NOTE

**Wrong parent: v3 07A. Nearest other: [v3 02B](/workspace/task_design_v3_codex/02_objectives_and_credit.md).** Repairing a checker cannot settle training potentials. D03 studies state-potential accounting and terminal usefulness, rather than delayed event-credit attribution.

## Verdict

**conditional** — Retain only if useful learned shaping survives the theorem-plus-demonstrations floor and causal learning ablations.
