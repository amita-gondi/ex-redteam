# C051 — Search with retriever training that changes evidence reachability — saturation screen
## 1. What the grader actually rewards
The useful outcome is supported research answers and better executed recipe choices after retriever updates, including answers that require evidence against the current hypothesis. Under the design contract, R≈0 is the frozen competent recipe floor, including an unchanged retriever; R≈1 means reaching the independently attainable constrained control, not perfect retrieval recall. Those utility anchors and the answer/recipe weighting are UNMEASURED, so all numerical forecasts below are ESTIMATED scenarios on the provisional scale.

The counterevidence-aware author reference has a nominal ESTIMATED R=0.60 target; its actual advantage over fixed hybrid retrieval is UNMEASURED.

## 2. Strongest lawful combined attack
Keep an immutable lexical retrieval channel alongside the trainable encoder. Train the encoder using globally mined hard negatives and periodically refreshed indexes, following [ANCE](https://arxiv.org/abs/2007.00808); preserve counterevidence as relevant evidence rather than accidentally labeling it negative. [BEIR](https://arxiv.org/abs/2104.08663) supports treating lexical retrieval as a serious robustness control, while also motivating reranking. Neither source establishes performance on this proposed task.

The researcher would maintain separate support and refutation query queues, retrieve their union through both channels, rerank for relevance independently of agreement, retain evidence provenance, and rehearse past contradictory examples during updates. A bounded search compares frozen-only, updated-only and hybrid policies while charging index construction and answer inference. This attacks the claimed feedback loop directly: a suppressed dense embedding need not prevent the lexical path or explicit refutation queue from finding the document.

ESTIMATED single-run R=0.73, range 0.57–0.86; ESTIMATED oracle best-of-4=0.81; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED projected upper-95% bound=0.94. These are subjective scenario summaries, not fitted intervals. They describe an improved transferred stack exceeding a previously frozen floor; if that exact stack sets the floor, it scores zero and the whole scale requires new measured anchors. The remaining gap is evidence whose vocabulary and causal relevance are both unfamiliar, plus downstream experiment selection errors. The present card supplies no constrained corpus size or retrieval budget demonstrating that these cases dominate.

## 3. Other routes
A frozen hybrid retriever with contradiction-directed query expansion is the strongest uncomplicated recipe: ESTIMATED R=0.65, range 0.45–0.80. It avoids the moving-index hazard entirely and remains lawful unless the task explicitly requires a useful training intervention, which the current grader does not establish causally.

A budgeted successive-elimination search over update frequency, lexical allocation, hard-negative mixture and replay fraction has ESTIMATED R=0.70, range 0.51–0.84. Selection must use disclosed development feedback only. Exhaustive document reading is an additional lawful shortcut when the inherited corpus fits the actor's total context budget; its affordability is currently unspecified.

## 4. What would lower lawful saturation
Author held-out evidence graphs where terminology changes across independently meaningful relations and a fixed retrieval allowance forces a choice between broad lexical coverage and adaptive semantic access. Give development instances the same update opportunities and require the trained retriever's causal contribution through an unchanged-retriever ablation. Do not ban the lexical control after it wins. ESTIMATED combined score after this redesign: 0.48–0.62, still borderline rather than a promised pass. ESTIMATED authoring effort is 8–12 person-days, plus ESTIMATED 48 H100-h for an initial matched-budget comparison; proving attainable reserve costs extra.

## 5. Decisive-check GPU-h re-estimate
Old card allocation: ESTIMATED 12 GPU-h. New ESTIMATED 72 H100-GPU-h: an ESTIMATED 300M-parameter retriever, ESTIMATED 4 arms (frozen hybrid, ordinary adaptation, protected-counterevidence adaptation, proposed reference), ESTIMATED 3 seeds per arm, and ESTIMATED 2 H100-h per fit give 4×3×2=24. An ESTIMATED 8B frozen answer actor gets ESTIMATED 3 H100-h per arm/seed for downstream campaigns, giving 4×3×3=36; index encoding/rebuilds and independent grading add ESTIMATED 12. Total ESTIMATED 24+36+12=72. This is a narrow falsification check, not the saturation panel. The original allowance omitted repeated downstream consequences and rebuild costs.

## 6. Duplicate check
Catalog T20: MODERATE, after reading its source packet; both grade research retrieval and tool outcomes, but T20 freezes the actor and optimizes the harness, whereas this intervention changes retriever weights and future evidence access. Task 07B: WEAK, from its source contract; evaluator learning changes selection quality but does not train the retrieval index. Neither comparison establishes the same intervention and target.

## 7. Verdict
CUT. The ESTIMATED best-of-4 exceeds the binding 0.60 line by ESTIMATED 0.21; the single-run, pass@4 and projection estimates also cross their respective limits. A fixed robust retrieval channel is an available lawful escape from the proposed feedback trap, and the card does not establish a budget that defeats it.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget attempts on fresh evidence graphs); grader noise UNMEASURED (planned: replay fixed trained retrievers through repeated complete campaigns); score ladder UNMEASURED (planned: unchanged, lexical-only, joint-training, hybrid and attainable-control anchors in native answer and experiment utility).

## Screen record
id: C051
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.73
attack_single_range: 0.57-0.86
bo4_est: 0.81
pass4_est: 0.96
ub95_est: 0.94
gpuh_old: 12
gpuh_new_est: 72
duplicate_of: T20 MODERATE; 07B WEAK
kill_reason: immutable hybrid retrieval bypasses adaptive evidence suppression
souping_flag: no
