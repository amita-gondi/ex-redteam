# C088 — Graceful failure when fallback itself has opportunity cost — saturation screen
## 1. What the grader actually rewards
The policy is scored on realized workflow utility after action damage, deferral, recovery and any paid measurement, while retaining successful intervention where justified. R≈0 is the competent state-cost-aware policy floor; R≈1 is an attainable sequential decision policy with better net outcomes. The no-op is ESTIMATED R=0.00 and the intended reference is ESTIMATED R=0.60, but the reward cannot be identified more precisely until the distribution of costs and recovery opportunities is frozen.
## 2. Strongest lawful combined attack
Use verified [GracefulRL](https://arxiv.org/abs/2610.20401) to avoid collapse into universal fallback, but condition values on the actual state and visible action costs rather than a constant abstention bonus. Train an action-value critic with terminal workflow returns, augment training with short legal counterfactual branches, and optimize the policy using [PPO](https://arxiv.org/abs/1707.06347) or the inherited compatible objective. Add planner-generated training demonstrations whenever the bounded workflow rules permit exact value-of-information calculation. This is ordinary sequential cost-sensitive learning applied jointly with the published fallback recipe.

The agent can explicitly compare acting now, deferring now and paying for another experiment, then distill that comparison into the deployed policy. Fresh numeric costs are natural conditioning inputs, not a new scientific obstacle for every instance. ESTIMATED single-run R=0.73, range 0.53–0.88; ESTIMATED best-of-4=0.82; ESTIMATED pass@4 at R≥0.60=0.94; ESTIMATED projected upper-95% bound=0.95. Residual errors concern long-horizon recovery uncertainty and imperfect value calibration in rare states. The card specifies no mechanism that prevents a jointly trained critic or training-only planner from resolving the cheaper one-more-experiment cases, so the fixed-reward baseline understates the lawful threat.
## 3. Other routes
- A recurrent PPO policy trained directly on true cost-adjusted terminal utility is ESTIMATED R=0.63, range 0.41–0.81. It bypasses new fallback shaping, though sparse credit and risk of policy collapse make the combined recipe stronger.
- Sweep fallback conditioning, entropy, critic loss, replay mixture and exploration horizon against complete workflow utility: ESTIMATED R=0.70, range 0.48–0.87. Search should include the fixed-shaping and direct-return alternatives rather than presupposing the new objective wins.
- Exact bounded planning on training states followed by imitation is ESTIMATED R=0.66, range 0.37–0.88. It is particularly strong when the visible recovery interface exposes a small state/action language.
## 4. What would lower lawful saturation
Introduce learnable recovery dynamics whose value depends on earlier information acquisition and where individually attractive measurements are jointly redundant. Keep costs and available actions visible, provide development trajectories with the same causal structure, and floor planner imitation plus the state-value recipe. ESTIMATED combined reward might become 0.44–0.59. ESTIMATED added work is two author-weeks and 160 H100 GPU-h for actual recovery histories and matched learning comparisons. Hidden penalty changes would not qualify. If the generator remains a compact finite decision problem, an amortized planner should remain legal and may still erase the reserve.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 14 GPU-h. New ESTIMATED total: 256 H100 GPU-h, on an ESTIMATED 3B policy and associated small critic. ESTIMATED 4 objective/planner controls × 2 seeds × 2 H100s × 12 hours = 192 GPU-h; legal branch generation costs ESTIMATED 32 GPU-h and independent workflow evaluation costs ESTIMATED 32 GPU-h. The per-run envelope includes policy optimization and critic updates, with no claim of measured throughput. The source allowance covers a toy shaping comparison but not meaningful sequential training and damage/recovery tail evaluation. CPU planning expense must also be recorded without pretending it is accelerator work.
## 6. Duplicate check
Catalog T14 — MODERATE: its inspected task trains cost-sensitive reporting and terminal defer/escalate actions, while this card prices future experiment opportunities. Catalog T15 — MODERATE: its opened source learns decision-changing paid evidence and permits exact-planner imitation, making it the closer causal neighbor. Recovery after action changes this card's target enough that a strong duplicate is not established from the current specification.
## 7. Verdict
CUT. ESTIMATED single-run reward breaches its line by 0.03, ESTIMATED best-of-4 by 0.22 and ESTIMATED pass@4 by 0.44. A state-conditioned critic, legal planner demonstrations and existing anti-collapse shaping form a competent complete attack rather than an exotic new method.
## 8. Measurement status
Rollouts UNMEASURED (planned: joint critic/shaping and planner-imitation training); grader noise UNMEASURED (planned: training-seed and rare-recovery replication); score ladder UNMEASURED (planned: fixed fallback, direct return, state-cost critic and attainable sequential control).
## Screen record
id: C088
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.73
attack_single_range: 0.53-0.88
bo4_est: 0.82
pass4_est: 0.94
ub95_est: 0.95
gpuh_old: 14
gpuh_new_est: 256
duplicate_of: catalog T14 MODERATE; catalog T15 MODERATE
kill_reason: state conditioned value learning and planner demonstrations price fallback
souping_flag: no
