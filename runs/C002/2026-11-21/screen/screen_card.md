# C002 — Learn a curriculum from optimizer blind spots — saturation screen
## 1. What the grader actually rewards
Compilation and execution of newly learned syntax, across required construct families, determine utility; gradient activity is only a diagnostic. ESTIMATED R≈0 denotes the executable coverage of the committed competent sampler, and ESTIMATED R≈1 denotes a feasible stronger schedule at identical training work with common syntax preserved. An unchanged inherited schedule is provisionally ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60, but the source supplies neither native execution rates nor frozen anchors.
## 2. Strongest lawful combined attack
Build a prerequisite graph from compiler errors and gradient traces, then allocate exposure according to measured learning progress rather than absolute loss. [Graves et al., Automated Curriculum Learning](https://proceedings.mlr.press/v70/graves17a) verifies adaptive syllabus selection using progress signals; [Teacher-Student Curriculum Learning](https://arxiv.org/abs/1707.00183) supplies a second concrete progress-based scheduling formulation. Combine these with common-syntax replay, a minimum exploration mass for currently unreachable constructs, and short paired continuation probes around apparent support transitions.

The researcher can use inherited gradients to distinguish examples that are simply difficult from those producing no useful change. Compiler-derived precursors seed the graph; probe gains update edges and retirement timing. Once a construct becomes trainable, its precursor exposure decays, but retention probes can reactivate it. This is lawful scheduling rather than an optimizer rewrite, and it directly addresses the card's proposed hard case. Under a fixed subject allocation, short diagnostic continuations must be charged; the attack cannot assume unlimited fully trained candidates.

ESTIMATED single-run R=0.53 with range 0.32–0.72; ESTIMATED oracle best-of-4=0.63; ESTIMATED pass@4 at R≥0.60=0.54; ESTIMATED projected upper-95% envelope=0.79. These are judgmental forecasts, not rollout statistics. Much of the executable gain should come from exposing prerequisites and retiring them at the right time. The remaining gap is whether absent gradients reflect a history-dependent representational barrier that schedule-only probes cannot diagnose cheaply; a finite error-order graph would remove that gap and raise the attack further.
## 3. Other routes
- The strongest uncomplicated recipe is a compiler-topological curriculum followed by mixed rehearsal. ESTIMATED R=0.42, range 0.21–0.64: it repairs obvious reachability but cannot time reversals caused by optimizer history.
- A bounded sweep searches precursor duration, exploration weight, switch threshold and rehearsal fraction using successive elimination of weak continuations. ESTIMATED R=0.49, range 0.28–0.70. This route may find a good transition without explaining it, so the task must survive outcome-only tuning.
- Maximizing gradients alone is weaker: ESTIMATED R=0.24, range 0.06–0.47. A large gradient can repeatedly target unsupported syntax, which is precisely why loss mining is an insufficient floor.
## 4. What would lower lawful saturation
Require curricula to handle independently authored construct combinations where an identical compiler-error prefix needs different exposure depending on prior training, and supply dev histories displaying that distinction. Freeze the optimizer and permit only the schedule channel, while making its actual delivered samples observable. Demonstrate that no fixed prerequisite order handles both histories. Forecast after that change: ESTIMATED composite R=0.39, range 0.20–0.57, with ESTIMATED best-of-four=0.49 and ESTIMATED upper envelope=0.67. Cost is ESTIMATED several weeks of language-generator and trace authoring plus ESTIMATED 192 H100 GPU-h for additional history-crossed pilots. The change must preserve a same-budget discoverable reference; otherwise it merely makes the learner fail.
## 5. Decisive-check GPU-h re-estimate
The original is ESTIMATED 8 GPU-h. Budget ESTIMATED 208 H100 GPU-h: ESTIMATED 1B-parameter code learner; ESTIMATED 4 schedule arms; ESTIMATED 3 seeds; ESTIMATED 16 H100-hours per continuation; ESTIMATED 16 GPU-h for compiled-sample generation and retention evaluation. Arithmetic: ESTIMATED 4×3×16+16=208. This assumes a continuation long enough to cross a rare-construct support event, plausibly involving billions of tokens, rather than a token-sized syntax classifier. The old pilot can inspect the first gradient appearance but cannot establish durable executable coverage or isolate seed-sensitive transitions.
## 6. Duplicate check
Catalog T07 (`task_catalog_v3_full/packets/T07.md`, opened): MODERATE, as both optimize curriculum transitions, but teacher-information retirement is different from a fixed-data sampler responding to optimizer reachability. D18 (`hidden_task_cards_v4/cards/D18.md`, opened): MODERATE, because constructing missing support can target similar capability, whereas this card changes exposure to an existing pool rather than synthesizing reachable worlds. No strong duplicate is established.
## 7. Verdict
CONDITIONAL. The current ESTIMATED best-of-four exceeds its line by ESTIMATED 0.03 and the projection by ESTIMATED 0.04; both sit in the specified redesign band. Require the history-crossed, non-fixed-order construct generator described above, plus an independently demonstrated schedule-only reference. Without that exact revision, the known progress/prerequisite stack is too close to saturation.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent researchers with identical sample-work ledgers). Grader noise UNMEASURED (planned: repeated continuation seeds around the acquisition transition). Score ladder UNMEASURED (planned: static sampling, loss mining, fixed prerequisites, adaptive progress schedule and attainable control scored by executable construct coverage).
## Screen record
id: C002
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.53
attack_single_range: 0.32-0.72
bo4_est: 0.63
pass4_est: 0.54
ub95_est: 0.79
gpuh_old: 8
gpuh_new_est: 208
duplicate_of: catalog-T07 MODERATE; D18 MODERATE
kill_reason: conditional on history-crossed prerequisite transitions
souping_flag: no

## Screening-lead reconciliation (added after batch review, 2026-11-21 PT)
The author verdict above is CONDITIONAL, but this card's own ESTIMATED numbers cross a kill line (best-of-4 0.63 > 0.60, pass@4 0.54 > 0.50, upper-95% 0.79 ≥ 0.75). The bar says over a line is CUT, so the final screen verdict is **CUT (bar-applied)**. The card may come back as a CONDITIONAL candidate only after the redesign described in section 7 and a fresh screen.
