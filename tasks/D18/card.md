# D18 — Construct reachable training support that the existing pool lacks

**Generator:** support-construction recovery. **Stage × artifact:** data × data. **Modality:** initial states and executable goals.

## Problem

An inherited training pool covers individual prerequisites but lacks jointly reachable state/goal configurations needed by the learner. Submit a static support generator under fixed scheduling, transition semantics and learner recipe. [Suite 11.3](/workspace/task_suites_claude.md:15435) changes which examples can exist, rather than selecting IDs from a preassembled pool.

## Why known recipes plateau

Constraint solving, backward planning, counterfactual generation and exhaustive support enumeration are mandatory baselines. The proposed residual is distinguishing legally reachable combinations that teach a missing abstraction from redundant combinations that consume the same exposure. Reachability certification alone is standard computation, and no learning plateau is established.

## Deterministic grader

Validate each generated reset/goal pair using trusted transition rules and an executable reachability witness. Train the fixed learner in the fixed order, then compute U as exact terminal success on independently generated target compositions. Invalid support consumes its allotted generation/exposure budget without adding examples; missing targets retain denominator weight. F_D18 rewards learned support value, not generator validity alone.

## Hidden-score design

Private families alter prerequisite interactions while preserving the declared action grammar and observation sufficiency. Dev contains protected unseen-interaction proxies. The generator receives training requirements only; hidden witnesses and target reset programs are absent from its execution environment.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D18(U_backward_support).** Assuming backward reachable-state enumeration spans the useful prerequisite combinations, construct balanced coverage and generate planner demonstrations at equal total cost. This may reach reference learning without adaptive support insight. Trivial-goal generation cannot earn reward on independent target tasks.

## Saturation note vs 10T / 12h

A stronger solver can synthesize the reachable support directly. To survive, support interactions must affect abstraction learning after enumeration and demonstration baselines, with evidence that scheduling changes do not explain the gain. Apply the index's hard kills and require attainable reserve rather than an ideal coverage ceiling.

## Cheapest decisive check

**ESTIMATED: 14 GPU-h** for fixed-order learner training on exhaustive balanced support versus the proposed construction, including independent targets. First test reachability completeness analytically; no GPU study is needed if the generator merely enumerates the answer.

## GDM Round 2 compliance and shape

The accepted pretraining_latest analogy is data-support-dependent learning. R1's trainer-ceiling warning requires enough exposure to reveal support value; R2's smuggling lesson requires typed state/goal artifacts that cannot carry arbitrary labels or executable learner replacements.

## DISTINCTNESS NOTE

**Wrong parent: v3 01A. Nearest other: [v3 02A](/workspace/task_design_v3_codex/02_objectives_and_credit.md).** Reweighting corpus IDs cannot create absent reachable states. Objective design changes learning signal; D18 fixes that signal and scheduling while constructing static support.

## Verdict

**conditional** — The construction interface is necessary, but useful support must beat complete reachability/planning recipes on actual learning.
