# C102 — Learn useful failed experiments under sparse scientific feedback — saturation screen
## 1. What the grader actually rewards
The submitted failure corpus must improve a reset research agent's subsequent choices on actual learning projects, after paying for corpus creation and agent training. Fluent explanations of unsuccessful experiments earn nothing by themselves. On the provisional scale, ESTIMATED R≈0 means no gain over competent failure replay and retrieval, while ESTIMATED R≈1 means reaching an independently attainable downstream improvement control; neither native anchor has been measured. The intended reference belongs around ESTIMATED R=0.60, but that placement cannot establish a real gap.
## 2. Strongest lawful combined attack
The attacker would separate scientific nulls from crashed or underpowered jobs, extract intervention, context, comparator and uncertainty, and retrieve condition-matched records before proposing experiments. [Reflexion](https://arxiv.org/abs/2303.11366) verifies the precedent for episodic linguistic feedback. Its role here is memory construction, followed by conditional imitation training rather than unrestricted trust in generated explanations. [LoRA](https://arxiv.org/abs/2106.09685) supplies an economical adapter-training mechanism, without any parameter combination between models. The corpus would pair similar projects where an intervention failed and succeeded, preserving the changed condition and the next useful action.

A strong agent would explicitly mark missing causal support, mix raw records with summaries, and compare retrieval-only, training-only and combined deployments. [Optuna](https://arxiv.org/abs/1907.10902) can select corpus weights, retrieval depth and adapter settings on lawful development campaigns. This is practical within the research horizon if inherited records already exist; collecting a new causal dataset from scratch is much less favorable. It attacks the purported distinction between avoiding failures and learning their scope directly.

ESTIMATED single-run R=0.64, range 0.43–0.80; ESTIMATED oracle best-of-4=0.73; ESTIMATED pass@4 at R≥0.60=0.82; ESTIMATED projected upper-95% score=0.88. These are subjective, mutually compatible planning forecasts, not confidence intervals fitted to data. The residual is genuinely unidentifiable nulls: records without power or changed-condition contrasts cannot tell the learner when to reverse an avoidance rule. Nevertheless, the card does not require enough of that residual to dominate reward. Most useful improvement could come from ordinary deduplication and context-sensitive retrieval.
## 3. Other routes
The strongest single recipe is structured Reflexion-style failure memory with retrieval, retaining the original run evidence beside the lesson. ESTIMATED R=0.51, range 0.30–0.69, because eliminating repeated identical hypotheses can improve downstream utility without learning a new scientific abstraction.

A search-focused route would vary failure inclusion, condition granularity, positive-to-negative balance and retrieval budget, then train only the best development candidate. ESTIMATED R=0.59, range 0.36–0.77. Search can discover that almost no failure training is useful and select a sparse corpus; that is lawful if the artifact contract permits it. Rewriting crashes as informative nulls would instead be a data-validity error and cannot support the estimate.
## 4. What would lower lawful saturation
Require held-out projects with matched early null observations but different valid conclusions, where an affordable diagnostic distinguishes insufficient exposure from a genuinely ineffective mechanism. Construct the histories through real interventions, include success cases for previously unsuccessful methods, and charge diagnostic acquisition. ESTIMATED combined attack reduction is 0.16–0.24 reward, to roughly 0.40–0.48. ESTIMATED authoring cost is 7–12 person-days plus 120 H100-h to generate and audit matched histories. If diagnostics cannot identify the distinction from available evidence, this change creates impossibility rather than research difficulty.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 16 GPU-h. New ESTIMATED value: 128 H100 GPU-h. Assume an ESTIMATED 4B research agent with adapter updates: 4 corpus/memory arms × 2 training seeds × 2 H100-h = 16 H100-h. Execute ESTIMATED 4 arms × 2 seeds × 3 fresh projects × 4 H100-h per project = 96 H100-h on 1B subject learners; reserve ESTIMATED 16 H100-h for independent final evaluations and agent execution. Thus ESTIMATED 16+96+16=128. This checks transfer direction, not the complete saturation panel. The old allowance could cover adapter training alone but omitted most downstream experiments.
## 6. Duplicate check
T03, MODERATE: its source packet submits a transferable experiment controller and grades live project gains, but C102 specifically submits failed-experiment training data rather than the controller. The narrower treatment can be distinguished through fixed-agent corpus ablations; the downstream target alone is insufficient for STRONG duplication.
## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds its kill line by 0.13 and ESTIMATED pass@4 exceeds its line by 0.32; the projected score bound also crosses. Context-aware failure retrieval followed by selective training is an ordinary combined baseline whose remaining reward gap has not been instantiated.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent complete-budget corpus-building attempts on fresh project blocks). Grader noise UNMEASURED (planned: repeat fixed-corpus agent training and downstream executions with independent seeds). Score ladder UNMEASURED (planned: no-op, raw replay, structured retrieval, joint training, reference and attainable stronger control in native improvement units).
## Screen record
id: C102
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.64
attack_single_range: 0.43-0.80
bo4_est: 0.73
pass4_est: 0.82
ub95_est: 0.88
gpuh_old: 16
gpuh_new_est: 128
duplicate_of: T03 MODERATE
kill_reason: conditional failure memory and training saturate downstream selection
souping_flag: no
