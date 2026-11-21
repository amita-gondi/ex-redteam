# C037 — Co-schedule draft training and target inference — saturation screen
## 1. What the grader actually rewards
The scheduler wins only by increasing exact target completions after paying for draft data, updates, synchronization and contention on the common pool. Better draft acceptance can reduce reward if obtaining it displaces more valuable target service. ESTIMATED R≈0 is the strongest frozen/periodic scheduling floor, ESTIMATED R≈1 the attainable cost-inclusive adaptive controller; a frozen draft is provisionally near ESTIMATED R=0.00 and the proposed reference near ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Use [Online Speculative Decoding](https://arxiv.org/abs/2310.07177) to train from target verification feedback and a small replay buffer. Couple it to a measured break-even controller: estimate how a draft update changes future accepted tokens, multiply by remaining demand, and compare saved target work with training and synchronization cost. [DistillSpec](https://research.google/pubs/distillspec-improving-speculative-decoding-via-knowledge-distillation/) supplies a mature draft-alignment baseline. Neither source by itself validates the shared-pool economic decision under drift.

Maintain current and candidate draft versions, evaluate a refresh on charged recent traffic, and publish only after it crosses a conservative net-service threshold. Batch updates into low-contention intervals, tune speculation length with acceptance rate, and keep frozen-draft and no-update paths available. A multi-fidelity search over update cadence, replay recency and training fractions can be performed by the target researcher. The harder part is estimating whether a newly observed prompt regime will persist long enough to amortize learning; current acceptance alone does not reveal that.

ESTIMATED single-run R=0.51, range ESTIMATED 0.30–0.68; ESTIMATED best-of-4=0.59; ESTIMATED pass@4 at R≥0.60=0.46; ESTIMATED projected upper-95% bound=0.74. These are desk projections with unresolved anchor uncertainty. The scale assumes standard online distillation is already included in the floor, leaving reward for adaptive scheduling across drift and contention transitions. The stack recovers about half that residual gap; it loses on delayed training payoffs whose usefulness changes while the update occupies the serving resource. If the floor is only a weak frozen draft, the same attack would likely score much higher.
## 3. Other routes
Periodic online distillation with a fixed low-load training window gives ESTIMATED R=0.37, range ESTIMATED 0.17–0.57. It adapts the model but pays for stale or poorly timed refreshes.

A budgeted cadence/training-fraction/speculation-length sweep reaches ESTIMATED R=0.44, range ESTIMATED 0.23–0.64. It can discover average economics without modeling regime duration, and should be allowed full legal development selection. A frozen domain-specialized draft remains a dangerous lawful shortcut, ESTIMATED R=0.32, range ESTIMATED 0.12–0.56, particularly if the private drift repeats a small set of familiar domains.
## 4. What would lower lawful saturation
Require an independently authored generator where prompt persistence and update benefit interact: some visible acceptance drops recover unaided, while others justify a refresh only before an approaching service peak. Include a protected development proxy for these causal relationships and retain standard online-distillation scheduling in the baseline. ESTIMATED attack score would become R=0.43–0.52, with ESTIMATED best-of-four near 0.56. ESTIMATED cost is four author-weeks and ESTIMATED 144 H100 GPU-h to establish both positive and negative refresh value. This exact design change is required; arbitrary surprising drift is insufficient.
## 5. Decisive-check GPU-h re-estimate
Old figure: ESTIMATED 12 GPU-h. New ESTIMATED 60 H100 GPU-h assumes an ESTIMATED 7B target and ESTIMATED 0.5B trainable draft sharing an ESTIMATED two-H100 pool. Compare ESTIMATED four scheduling arms across ESTIMATED three independently authored drift blocks, at ESTIMATED two wall-hours each: ESTIMATED 4×3×2×2=48 GPU-h. Add ESTIMATED 8 GPU-h for target-only truth and refresh evaluation plus ESTIMATED 4 GPU-h of warmup/synchronization replay. This is short online adaptation rather than large-scale pretraining; the old pilot omits multiple regime outcomes and resource interference.
## 6. Duplicate check
03B: WEAK, from its read inference-budget training contract; it changes reasoning expenditure rather than training a draft while serving. 05A: MODERATE because the read serving task optimizes exact capacity but does not endogenously improve a draft under the same resource pool. The train/serve coupling adds a distinct intervention.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-four margin is only 0.01 and projected-bound margin only 0.01; pass@4 margin is ESTIMATED 0.04. Require the persistence-by-update-benefit generator and an online-distillation floor specified above before further screening. No empirical saturation gate is passed.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete competing train/serve schedules). Grader noise UNMEASURED (planned: repeated draft updates and shared-pool service). Score ladder UNMEASURED (planned: frozen, periodic, break-even and attainable anticipatory scheduling).
## Screen record
id: C037
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.51
attack_single_range: 0.30-0.68
bo4_est: 0.59
pass4_est: 0.46
ub95_est: 0.74
gpuh_old: 12
gpuh_new_est: 60
duplicate_of: 03B WEAK; 05A MODERATE
kill_reason: near repeated-search line; require persistence-dependent refresh value
souping_flag: no
