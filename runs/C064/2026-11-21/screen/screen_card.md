# C064 — Router regularization invariant to token packing — saturation screen
## 1. What the grader actually rewards
The endpoint is compositional held-out loss at equal active FLOPs, after fixing the intended token-normalization semantics; expert count balance is only a diagnostic. R≈0 is the competent token-correct routing floor, so repairing a denominator or retaining the unchanged router should contribute no residual reward. R≈1 reaches a stronger feasible specialization control across heterogeneous mixtures, with all numerical projections below ESTIMATED because raw loss anchors, reference reserve and training variability are UNMEASURED.

Adaptive specialization is assigned nominal ESTIMATED reference R=0.60; rare-domain loss improvements needed to justify that assignment have not been observed.

## 2. Strongest lawful combined attack
Accumulate valid-token expert statistics across the declared global window, excluding padding, and verify the same stream's loss and gradients under repacking. Then compare corrected global auxiliary regularization, sequence-level regularization and [auxiliary-loss-free balancing](https://arxiv.org/abs/2408.15664). The latter is especially important: it changes expert selection through balancing biases rather than introducing the same unwanted auxiliary gradients. [Megatron's router configuration documentation](https://docs.nvidia.com/megatron-core/developer-guide/latest/apidocs/core/core.transformer.transformer_config.html) confirms that multiple balancing semantics already exist; the desired one must be published before grading.

Combine slowly updated global load estimates with faster overload protection, conservative capacity margins and task-mixture-aware monitoring from legal training data. Tune update timescales, balancing strength, capacity and warmup jointly at fixed useful FLOPs, retaining rare-domain validation rather than choosing only aggregate training loss. This removes both the bookkeeping error and the obvious overly aggressive balance recipe. It remains constrained by the routing decisions available before a rare skill's future usefulness is observed.

ESTIMATED single-run R=0.47, range 0.26–0.64; ESTIMATED best-of-4=0.56; ESTIMATED pass@4 at R≥0.60=0.32; ESTIMATED projected upper-95% bound=0.70. These are uncalibrated planning estimates for a better transferred stack than a frozen floor, not training results. The residual is the balance/specialization tradeoff across bursty valid-token mixtures: a global load statistic can be stable while discouraging an expert needed for a later compositional slice. Unlike denominator correction, selecting the right adaptation timescale need not be invariant across histories. The card does not yet establish the size of that effect after the loss-free baseline.

## 3. Other routes
Correct global token normalization with a fixed auxiliary coefficient has ESTIMATED R=0.28, range 0.10–0.48. Most of its native improvement should be absorbed into the committed floor, leaving only workload-transfer gains on this reward scale.

A budgeted search over published balancing modes, coefficient schedules, bias update rates and capacity factors has ESTIMATED R=0.44, range 0.23–0.62. Loss-free balancing alone is a particularly important arm, with ESTIMATED R=0.40, range 0.20–0.59. Search must compare complete training endpoints, since early expert uniformity is not a reliable proxy for rare expertise.

## 4. What would lower lawful saturation
Require independently authored task mixtures where rare experts have demonstrable later compositional value, while keeping the valid-token objective identical under repacking. Freeze per-domain retention accounting and show that a tuned loss-free controller cannot match the reference merely by increasing capacity within the active-FLOP cap. ESTIMATED attack under that specification is 0.39–0.51. ESTIMATED preparation is 12–18 person-days and ESTIMATED 768 H100-h for a first learning-scale check. Excluding loss-free balancing would invalidate the screen; if it solves every regime, the residual hypothesis fails.

## 5. Decisive-check GPU-h re-estimate
The old ESTIMATED 14 GPU-h is a normalization-debugging pilot, not a specialization study. Revised ESTIMATED 768 H100-GPU-h uses an ESTIMATED 3B-total/0.5B-active MoE, ESTIMATED 5B training tokens, ESTIMATED 4 routing arms×3 seeds×14 cluster-hours×4 H100s=672. Exact stream/repacking gradient probes, rare-domain evaluation and independent endpoint replay add ESTIMATED 96, giving ESTIMATED 768. The active training-operation approximation is ESTIMATED 6×0.5B×5B=15×10^18 per run; sparse communication and low utilization justify a much slower wall-time assumption than dense peak FLOPs. The pilot still tests a reduced subject rather than certifying frontier MoE behavior.

## 6. Duplicate check
04A: MODERATE after inspecting its source. Routing fidelity and useful learning overlap, but that task's intervention is asynchronous version/cache consistency, whereas this card changes the balancing objective under token packing. 05B: WEAK because exact gradient invariance is shared but specialization loss is an additional learning target. Neither indexed task has the same objective intervention and grader target together.

## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 has only 0.04 clearance and the projected bound has 0.05 clearance, insufficient for a clear screen pass. Retention requires the rare-expert compositional mixtures, published packing-invariant objective, and complete tuned loss-free/capacity control described above, with demonstrated native reserve. The research hypothesis is plausible, but the bookkeeping bug alone supplies none of that reserve.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent routing-objective searches across fresh task mixtures); grader noise UNMEASURED (planned: repeated fixed-recipe MoE training and held-out scoring); score ladder UNMEASURED (planned: corrected normalization, global/sequence losses, loss-free balance, adaptive capacity and attainable specialization control).

## Screen record
id: C064
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.47
attack_single_range: 0.26-0.64
bo4_est: 0.56
pass4_est: 0.32
ub95_est: 0.70
gpuh_old: 14
gpuh_new_est: 768
duplicate_of: 04A MODERATE; 05B WEAK
kill_reason: near tail boundary until rare specialization survives loss-free balancing
souping_flag: no
