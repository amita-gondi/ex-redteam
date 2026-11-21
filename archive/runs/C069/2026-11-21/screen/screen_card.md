# C069 — Finite policy losses without deleting informative extremes — saturation screen
## 1. What the grader actually rewards
Training must remain numerically valid on extreme log-probability probes while improving exact policy success and retained task coverage under a fixed rollout allowance. Skipped groups and nonfinite updates remain charged failures, so quieter logs or lower surrogate variance cannot substitute for learning. R≈0 is the competent stable-loss floor, including the repaired implementation; R≈1 is the attainable signal-preserving policy control, with all quantitative forecasts below ESTIMATED and the success/coverage anchors UNMEASURED.

The signal-preserving robust-loss reference targets nominal ESTIMATED R=0.60; retaining informative extremes has not yet shown the required native coverage reserve.

## 2. Strongest lawful combined attack
Separate arithmetic safety from estimator design. Compute log probabilities and normalizers in stable precision, using operations such as documented [logsumexp](https://docs.pytorch.org/docs/stable/generated/torch.logsumexp.html), and avoid evaluating overflowing exponentials on branches that should already be clipped. Apply bounded importance updates and monitor actual KL, with explicit semantics for singleton and zero-variance groups. A genuinely enormous unbiased importance ratio cannot in general be both retained exactly and made statistically harmless through a numerical trick.

Compare token-level stable PPO/GRPO with [GSPO](https://arxiv.org/abs/2507.18071), which changes importance weighting to the sequence level, wherever that objective replacement is lawful. Use the token-level accounting and training-system lessons of [DAPO](https://papers.nips.cc/paper_files/paper/2025/file/a4277440d50f1f15d2cb4c14f7e0c0d2-Paper-Conference.pdf) as another complete arm. Combine adaptive KL, more frequent policy refresh, robust advantage scale estimates and coverage-aware prompt replay, charging every generated trajectory. Tune clipping asymmetry and group-size handling against exact downstream success, not loss finiteness alone.

ESTIMATED single-run R=0.62, range 0.40–0.79; ESTIMATED best-of-4=0.72; ESTIMATED pass@4 at R≥0.60=0.78; ESTIMATED upper-95% projection=0.88. These are subjective estimates of stronger transferred recipes above a frozen floor. The residual is distinguishing rare genuinely informative updates from high-variance harmful ones before collecting enough new evidence. That can be difficult, but unlike T18's explicit correlated corruption, this card has not committed a mechanism that defeats sequence weighting, on-policy refresh and ordinary replay together.

## 3. Other routes
A mature numerically stable PPO/GRPO implementation with adaptive KL and fixed clipping is the strongest single standard recipe: ESTIMATED R=0.49, range 0.28–0.69. It should already recover the original guard/clamp inconsistencies, leaving only statistical tail utility in the reward gap.

Search jointly over token/sequence estimators, clip asymmetry, advantage scaling, refresh interval and replay strength. ESTIMATED R=0.59, range 0.36–0.77. All losing branches consume rollout budget. Rejecting informative tails can be a lawful specialization strategy rather than an exploit, so the coverage metric must price the resulting missing skills continuously and materially.

## 4. What would lower lawful saturation
Define supported tail mechanisms where informative rare successes and nuisance extremes overlap in observable magnitude, and make their distinction learnable through authorized history rather than a hidden label. Include explicit rare-skill retention in the native utility and compare the complete sequence-weighted/refresh/replay control. ESTIMATED combined R after this change is 0.43–0.58. ESTIMATED effort is 12–18 person-days plus ESTIMATED 576 H100-h for a pilot. This begins approaching T18's research target, so a redesign must explain what additional intervention it contributes instead of merely importing that task's difficulty.

## 5. Decisive-check GPU-h re-estimate
Old card amount: ESTIMATED 12 GPU-h. New ESTIMATED 576 H100-GPU-h assumes an ESTIMATED 3B policy, with an ESTIMATED 3B reference/value component as required by the selected estimator. ESTIMATED 4 arms×3 seeds×10 cluster-hours×4 H100s=480 for generation and updates; trusted extreme probes, exact coverage evaluation and independent endpoint checks add ESTIMATED 96, making ESTIMATED 576. Rollout generation is included rather than treated as free inventory. The old number can reveal a nonfinite loss on a saved batch, but cannot show whether a tail-preserving algorithm acquires more private skills after fixed-cost training.

## 6. Duplicate check
T18: MODERATE after the FIX source review; both optimize robust policy updates while retaining important tails, but its coupled reward-corruption process is absent here. T06: MODERATE because exact success and retained finite-budget coverage are shared endpoints, while this intervention is stable loss/estimator design rather than exposure and support recovery. The concrete implementation incident does not itself establish scientific novelty, but neither comparison proves identical mechanisms.

## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds the binding line by 0.12 and ESTIMATED pass@4 exceeds its line by 0.28; the projected upper bound also breaches. The single-run point alone would look modest, illustrating why the competent stack and repeated-search tails are decisive here.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget stable-estimator research on fresh tail regimes); grader noise UNMEASURED (planned: fixed recipes retrained with independent generation and training seeds); score ladder UNMEASURED (planned: clamp repair, stable arithmetic, adaptive clipping, sequence weighting plus refresh, and attainable coverage control).

## Screen record
id: C069
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.62
attack_single_range: 0.40-0.79
bo4_est: 0.72
pass4_est: 0.78
ub95_est: 0.88
gpuh_old: 12
gpuh_new_est: 576
duplicate_of: T18 MODERATE; T06 MODERATE
kill_reason: stable sequence-weighted refresh stack breaches repeated-search limits
souping_flag: no
