# C005 — Reward counterfactual experiment cancellation — saturation screen
## 1. What the grader actually rewards
Cancellation has no intrinsic reward: the trained policy must turn released, acknowledged reservations into valuable later experiments. Realized decision value includes wasted reservations and lost successors on the complete private dependency graph. ESTIMATED R≈0 is the competent stopping-policy floor and ESTIMATED R≈1 is an attainable constrained planner; an unchanged manager is provisionally ESTIMATED R=0.00, with the card's reference conventionally targeted at ESTIMATED R=0.60 until native value anchors are measured.
## 2. Strongest lawful combined attack
Fit calibrated conditional distributions for unfinished-run outcomes and durations from inherited partial traces. Couple them to a dependency-aware rollout planner that explicitly represents capacity release, cancellation latency and successor eligibility. [Decima](https://arxiv.org/abs/1810.01963) verifies learned scheduling over dependent stages, while [BOHB](https://proceedings.mlr.press/v80/falkner18a.html) verifies a mature combination of predictive search and resource-aware early termination. Neither source is an exact solution to this environment; the attack borrows their concrete components.

Generate legal training trajectories using approximate lookahead on public graph families, derive counterfactual advantages from paired simulated continuations, and distill those advantages through the permitted reward/objective channel. A potential based on remaining attainable experiment value can improve credit without awarding cancellation itself. Then tune the opportunity-cost multiplier and uncertainty penalty with full-graph terminal value. If reward edits alone are admitted, the deployed artifact remains a reward function used by the fixed trainer; an external planner cannot replace the policy at grading time.

ESTIMATED single-run R=0.68, range 0.45–0.85; ESTIMATED best-of-4 mean=0.77; ESTIMATED pass@4 at R≥0.60=0.88; ESTIMATED upper-95% planning projection=0.92. The forecast assumes the committed cost/outcome tables describe a learnable family rather than reveal protected future outcomes. Predictive stopping supplies the obvious cancellations; graph lookahead adds the reward the card claims naive stopping misses. The residual is imperfect beliefs about interim signals and long-horizon branch interactions. Since graph replay is inexpensive, substantial lawful planning and reward search fits within the research budget even when policy training is constrained.
## 3. Other routes
- A failure predictor with a fixed expected-value-per-capacity threshold is the strongest single recipe. ESTIMATED R=0.51, range 0.29–0.72; it loses value when freeing a resource changes which successor can run.
- Search over termination thresholds, lookahead depth, discounting and risk penalties, using identical graph blocks and retaining failed decisions in denominators. ESTIMATED R=0.63, range 0.40–0.81. This can discover an effective objective without reproducing the intended causal explanation.
- If table access makes outcomes conditionally deterministic, dynamic programming over the small reachable resource state could nearly solve training instances and supply teaching targets. ESTIMATED R=0.79, range 0.48–0.96 under that interface interpretation; the main forecast does not assume hidden table access.
## 4. What would lower lawful saturation
Make cancellation alter an observable downstream scientific opportunity distribution, with reusable capacity, restart penalties and correlated evidence jointly affecting successors. Private graphs should change causal dependencies, not just durations, and dev must expose analogous transitions. Require calibrated belief updates before a lookahead policy can value a release; do not conceal scheduler mechanics. Such a redesign might reduce the attack to ESTIMATED R=0.47, range 0.25–0.68, at ESTIMATED several weeks of graph and predictor authoring plus ESTIMATED 96 H100 GPU-h for policy and real-experiment validation. If the objective is scored only on synthetic cost tables, accepted-shape fit remains weaker than the scientific narrative suggests.
## 5. Decisive-check GPU-h re-estimate
Old allowance is ESTIMATED 6 GPU-h. An ESTIMATED 48 H100 GPU-h pilot uses an ESTIMATED 100M-parameter graph policy, ESTIMATED 4 reward arms, ESTIMATED 3 seeds and ESTIMATED 3 H100-hours per training run, plus ESTIMATED 12 GPU-h for paired downstream ML campaign checks: ESTIMATED 4×3×3+12=48. CPU graph simulation and a small predictor need little accelerator time. The former budget is plausible for simulation-only demonstrations, but omits replication and proof that cancellation improves actual research work rather than a convenient scheduler surrogate. This costing does not finance a complete saturation panel.
## 6. Duplicate check
v3 02B (`task_design_v3_codex/02_objectives_and_credit.md`, task source opened): MODERATE, sharing delayed irreversible research-action credit but not the explicit capacity-release counterfactual. D06 (`hidden_task_cards_v4/cards/D06.md`, opened): WEAK, since its irrevocable spending concerns repairing or replacing training worlds rather than terminating active experiments. Resource allocation alone does not establish the same intervention and grader target.
## 7. Verdict
CUT. The ESTIMATED best-of-four breach is 0.17, with a pass@4 breach of ESTIMATED 0.38. A failure model, graph-aware opportunity pricing and reward distillation form a coherent standard stack that the current task does not place below the reference.
## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget objective construction with charged graph search). Grader noise UNMEASURED (planned: paired policy seeds and independent dependency families). Score ladder UNMEASURED (planned: never cancel, threshold stopping, successor-aware planning, learned counterfactual reward and stronger attainable control).
## Screen record
id: C005
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.68
attack_single_range: 0.45-0.85
bo4_est: 0.77
pass4_est: 0.88
ub95_est: 0.92
gpuh_old: 6
gpuh_new_est: 48
duplicate_of: v3-02B MODERATE; D06 WEAK
kill_reason: graph lookahead supplies capacity-aware cancellation credit
souping_flag: no
