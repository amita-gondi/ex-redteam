# D15 — Acquire evaluator evidence adaptively before committing a verdict

**Generator:** active-evaluation recovery. **Stage × artifact:** eval/grading × model weights. **Modality:** run artifacts and query transcripts.

## Problem

A run evaluator receives an expensive collection of checkpoints, traces and diagnostic views. It must decide which artifact to inspect next and when to stop, rather than classify a fixed rendered summary. Train an evidence-acquisition policy from the inherited incorrect-verdict histories in [Suite 9.2](/workspace/task_suites_claude.md:11826), with immutable query and output schemas.

## Why known recipes plateau

Full-context evaluation, a fixed sufficient query set, classical sequential testing and cost-sensitive active classification are required recipes. A proposed residual exists if earlier evidence changes which later observation is causally sufficient. More files alone do not establish it, and unrestricted complete inspection may already fit the budget.

## Deterministic grader

Root answers paid queries, logs stopping decisions and checks final validity against exact run truth. U is balanced correct verdict utility under the disclosed inspection budget; false positives, false negatives and unfinished verdicts remain in fixed denominators. Query cost is a real cap rather than an inactive bonus. F_D15 rewards correct economical evaluation, not persuasive rationale.

## Hidden-score design

Private producer and artifact-dependency mechanisms require a protected unseen-producer dev proxy. Match evidence availability, costs, class balance and sufficient-evidence coverage. Healthy independent optimizers must generate ordinary-looking wrong artifacts and adversarially presented correct ones without receiving candidate-controlled failure labels.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D15(U_fixed_sufficient).** If a cheap common subset identifies truth, a fixed inspection schedule followed by a standard classifier can reach the reference. Test full inspection at the actual cap too. A slow evaluator that exhausts attackers must score as failure, not robustness; stopping cannot delete difficult cases.

## Saturation note vs 10T / 12h

The target researcher can derive an adaptive decision tree or replace the evaluator stack. Genuine reserve requires learned artifact sufficiency under new causal producer relationships, not hidden-only query mechanics. The index's S2/S4/S7 cutoffs govern both adaptive and static legal solvers.

## Cheapest decisive check

**ESTIMATED: 10 GPU-h** for policy/classifier fitting and independent optimized-artifact evaluation. Compare full context, best fixed query sets and adaptive querying; reject the premise if adaptivity offers no meaningful native advantage.

## GDM Round 2 compliance and shape

This can resemble agentic_search_inference_efficiency when evidence queries and model execution are substantive. R1 requires exact complete keys; R2 requires protected dev gold, cap-reaching oracle-leak tests and no metadata-only sibling-SHA verdicts. Every attacker query must complete under a trusted limit.

## DISTINCTNESS NOTE

**Wrong parent: v3 07B. Nearest other: [T15](/workspace/task_catalog_v3_full/packets/T15.md).** A declarative evidence renderer cannot execute adaptive queries. T15 elicits missing requirements; D15 inspects existing ML run evidence to reach an exact verdict.

## Verdict

**conditional** — Requires real, predictive value from adaptive evidence acquisition after complete-context and fixed-sufficiency controls.
