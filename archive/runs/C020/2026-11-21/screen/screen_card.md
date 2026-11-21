# C020 — Train a memory admission predictor for inference state — saturation screen
## 1. What the grader actually rewards
The predictor must increase exact completed workflows per GPU-second under combined host/device state limits, after paying transfer, reconstruction and prediction costs. Cache-hit rate is incidental: preserving an expensive prefix can still hurt if it blocks several more useful workflow states. ESTIMATED R≈0 is the competent learned-admission floor and ESTIMATED R≈1 an attainable stronger predictor/allocator outcome; inherited eviction is tentatively ESTIMATED R=0.00 and reference ESTIMATED R=0.60, without a measured native goodput ladder.
## 2. Strongest lawful combined attack
Train a cost-sensitive future-use model from legal workflow traces, using branch progress, elapsed tool time, request intent, prefix ancestry, reconstruction FLOPs and transfer bytes. [Learning Relaxed Belady](https://www.usenix.org/conference/nsdi20/presentation/song) verifies learning-based approximation to future-use eviction. Newer verified leads include [semantic-aware prefix eviction](https://arxiv.org/abs/2605.18825) and [Intent-Aware Caching](https://arxiv.org/abs/2611.09715). Their existence strengthens the baseline; none proves performance on branching tool graphs or this joint-memory contract.

Combine reuse predictions with a size/cost-aware host/device allocator, recency fallback, partial-prefix retention and a small reserve for imminent joins. Use training-only future traces to label counterfactual cache value, then distill the policy into the submitted predictor weights. Online predictions receive only observations available before the next tool outcome. Jointly tune inference frequency, eviction granularity and risk penalty, including the cost of every model invocation. [vLLM prefix-caching design](https://docs.vllm.ai/en/stable/design/prefix_caching/) provides a verified practical allocator/control, with the task's version and ancestry checks still required.

ESTIMATED single-run R=0.48, range 0.26–0.67; ESTIMATED oracle best-of-4=0.59; ESTIMATED pass@4 at R≥0.60=0.44; ESTIMATED upper-95% projection envelope=0.74. These are scenario judgments. The stack should recover predictable rejoins and avoid expensive unnecessary recomputation, yielding a substantial fraction of the available goodput gain. Its residual is conditional value: a tool result changes which prefix is needed, and the best retention choice depends on the competing workflow states and both memory tiers. Marginal reuse estimates may be accurate yet select the wrong portfolio. That residual is plausible, but a graph-conditioned learned predictor can also learn these interactions if the training family exposes them compactly.
## 3. Other routes
- Learned next-use prediction with recency fallback and reconstruction-cost normalization: ESTIMATED R=0.35, range 0.16–0.56. This is stronger than LRU but may misprice jointly valuable branches.
- Sweep admission thresholds, host/device watermarks, retained-prefix granularity and predictor refresh frequency on complete workflow replays. ESTIMATED R=0.43, range 0.22–0.64. Search must charge replay training and predictor overhead, rather than optimize a free simulator-hit metric.
- Retain only long, expensive-to-recompute prefixes and recompute cheap state unconditionally. ESTIMATED R=0.31, range 0.12–0.57. Its simplicity makes it a necessary native goodput anchor when sophisticated prediction is costly.
## 4. What would lower lawful saturation
Instantiate protected workflow families where observable tool outcomes reverse entry value, and where accurate independent next-use probabilities fail to identify the best byte-constrained portfolio. Match these conditional reversals in dev, with an independently trained same-capacity reference exploiting the available graph evidence. Include intent-aware, semantic-aware and cost-aware caching in the frozen floor. Forecast redesigned composite: ESTIMATED R=0.37, best-of-four=0.48, pass@4=0.21 and upper envelope=0.66. Cost is ESTIMATED several weeks of real branch/rejoin workload authoring and ESTIMATED 72 H100 GPU-h for portfolio-versus-marginal controls. Longer prefixes alone would not supply the interaction.
## 5. Decisive-check GPU-h re-estimate
Old figure: ESTIMATED 10 GPU-h. Revised ESTIMATED 68 H100 GPU-h assumes an ESTIMATED 8B inference subject and ESTIMATED 10M-parameter predictor. ESTIMATED 4 predictor arms×3 training seeds×2 H100-hours costs ESTIMATED 24 GPU-h; ESTIMATED 4 arms×3 workflow families×2 process starts×1 H100-hour costs another ESTIMATED 24 GPU-h. Reserve ESTIMATED 12 GPU-h for cost-label generation and ESTIMATED 8 GPU-h for exact-output/reconstruction checks: ESTIMATED total 68. Predictor training is modest; target-model workflow replay dominates. The old budget can screen frequency versus workflow features but not compare the strongest learned stacks across independent processes.
## 6. Duplicate check
v3 06A (`task_design_v3_codex/06_architecture_resource_codesign.md`, source opened): WEAK; its intervention compresses and recovers lossy attention state, whereas C020 chooses which exact states to admit. v3 05A (`task_design_v3_codex/05_exact_systems.md`, previously inspected): MODERATE, because exact serving-state management is shared, but this card's artifact is a trained workflow-conditioned predictor rather than unrestricted serving code. No STRONG identity is established.
## 7. Verdict
CONDITIONAL. Both ESTIMATED best-of-four and projected-bound clearances are only 0.01. Require the explicit conditional-value reversal/portfolio generator and the complete modern learned-cache floor above. The current idea is more specific than ordinary LRU tuning, but has insufficient desk margin for PASS-SCREEN.
## 8. Measurement status
Rollouts UNMEASURED (planned: weights-only admission training and complete serving replays). Grader noise UNMEASURED (planned: predictor-seed and process-start replication with fixed workload denominators). Score ladder UNMEASURED (planned: LRU, cost-aware recency, learned reuse, graph-conditioned portfolio admission and attainable control).
## Screen record
id: C020
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.48
attack_single_range: 0.26-0.67
bo4_est: 0.59
pass4_est: 0.44
ub95_est: 0.74
gpuh_old: 10
gpuh_new_est: 68
duplicate_of: v3-06A WEAK; v3-05A MODERATE
kill_reason: require outcome-conditioned portfolio reversals beyond modern caches
souping_flag: no
