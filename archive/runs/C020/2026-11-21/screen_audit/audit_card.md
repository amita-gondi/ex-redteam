# C020 — Train a memory admission predictor for inference state — screen audit
## 1. What the screen claimed
The old attack learned future use from workflow progress and cost, combined size-aware host/device allocation with recency and prefix retention, and distilled the result into predictor weights. It forecast ESTIMATED single/bo4/pass@4/ub95 = 0.48/0.59/0.44/0.74 and CONDITIONAL, with no kill category populated; retention required conditional portfolio reversals beyond modern caches. Its citations were:
- https://www.usenix.org/conference/nsdi20/presentation/song
- https://arxiv.org/abs/2605.18825
- https://arxiv.org/abs/2611.09715
- https://docs.vllm.ai/en/stable/design/prefix_caching/
## 2. Evidence audit
Learning Relaxed Belady demonstrates practical learned eviction, but for CDN objects rather than expensive GPU inference state. The semantic-aware and intent-aware cache papers supply much closer online adaptation evidence; vLLM documents a production prefix allocator. None demonstrates an unaided researcher training the submitted predictor and validating joint host/device workflow utility within twelve hours.

The screen acknowledged that distinction but gave little basis for the specific remaining portfolio difficulty. Grade: PARTIAL. New CacheScout evidence directly learns agent execution transitions for eviction/prefetch, weakening the idea that future workflow use is itself unsolved. However, a human-engineered online caching system is not evidence that an R&D agent can reproduce every interaction and train the permitted artifact on budget.
## 3. Research done now
- Learning Relaxed Belady for Content Distribution Network Caching — Zhenyu Song et al., 2020 — https://www.usenix.org/conference/nsdi20/presentation/song — fetched — Establishes future-use learning with practical overhead; transfer to GPU state requires reconstruction and transfer costs beyond WAN traffic.
- Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches — Shaoke Fang et al., 2026 — https://arxiv.org/abs/2605.18825 — fetched — Learns semantic reuse weights online, raising the floor above a static frequency predictor while leaving branch-conditional joint admission untested.
- Intent-Aware Caching for Efficient LLM Serving — Kazi Hasan Ibn Arif et al., 2026 — https://arxiv.org/abs/2611.09715 — fetched — Connects request intent to continuation and timing, demonstrating a relevant contextual signal rather than merely naming it.
- Automatic Prefix Caching — vLLM project, 2026 accessed documentation — https://docs.vllm.ai/en/stable/design/prefix_caching/ — fetched — Supplies practical exact-prefix allocation, with ancestry/version validity needing enforcement at the task boundary.
- Learning Agent Execution for KV-Cache Management in Agentic Serving — Rui Zhang et al., 2026 — https://arxiv.org/abs/2608.14624 — fetched — CacheScout learns execution transitions online and improves real agent-serving latency/throughput; this is close positive evidence against novelty based only on branch progress.
- When Cache Pressure Becomes a Trap: Metastability in Agent Serving — Chengzhi Lu et al., 2026 — https://arxiv.org/abs/2611.02543 — fetched — Demonstrates population/cache feedback and a predictor-driven admission policy. It both raises the attack and shows why marginal hit-rate optimization can miss a system-wide collapse; demand shedding must not evade this card's fixed workflow denominator.

Search included workflow-aware eviction and automated cache-policy discovery; the two agent demonstrations below were fetched as well.
## 4. Re-estimated attack
The score decomposition is ESTIMATED: cost-aware future-use prediction recovers 0.25, learned execution/intent conditioning adds 0.22, and coordinated allocation/overhead tuning adds 0.15. Native completion gains and anchors remain unknown, so these are hypothesized marginal contributions after earlier components, not sums of paper speedups.

Recipe-conditioned R=0.38/0.64/0.80 with probabilities 0.20/0.60/0.20 represents costly prediction or wrong reuse, a successful CacheScout-class policy, and effective joint tuning. ESTIMATED single=0.20×0.38+0.60×0.64+0.20×0.80=0.62, range 0.38–0.80; bo4=0.38×0.20^4+0.64×(0.80^4−0.20^4)+0.80×(1−0.80^4)=0.73; pass@4=1−0.20^4=1.00 rounded; ub95=0.80 because lower-state probability is 0.80. Spread comes from predictor training and whether competing workflow states are priced correctly, not measured timing noise. This rises materially above the old screen because new execution-aware caching directly implements part of its purported residual.
## 4A. Demonstrated capability and subfield SOTA
The closest verified domain frontier is CacheScout's workflow-transition learning, supplemented by SAECache/IAC for semantics and Basin for admission feedback. They anchor the reference to real completed-service value under cache pressure; none establishes the best constrained joint-memory predictor on this distribution. R≈1 therefore needs a measured same-capacity stronger control, with hit-rate leadership explicitly insufficient.

- ServerBench: How can your coding agents design specialized LLM serving systems? — Xinrui Zhong et al., 2026 — https://arxiv.org/html/2611.06841v1 — fetched. Opus 5.5+Claude Code delivers reported 4.40 qualified dollars per dollar on Qwen3.5 9B after eight hours using two L40s. It integrates state reuse with scheduling in response-dependent sessions. Its artifact is unrestricted serving code, so this does not demonstrate training a standalone predictor under a two-tier state budget.
- ArchAgent: Agentic AI-driven Computer Architecture Discovery — Raghav Gupta et al., 2026 — https://arxiv.org/abs/2602.22425 — fetched. The AlphaEvolve/Gemini-based scaffold produces a cache-replacement policy with reported 5.3% IPC improvement over prior SOTA on multi-core Google traces in two days without human intervention. Exact Gemini version and compute allocation are unreported. It demonstrates actual policy discovery, but hardware-cache simulation, longer search and coded policies leave substantial distance to twelve-hour predictor training for inference state.

KNOWN-RECIPE learned caching is demonstrated; AGENT-DEMONSTRATED comparable-budget weights-only joint admission is not. attack_basis=LITERATURE-ONLY. An attacker still must obtain counterfactual value labels, train the allowed model, integrate its overhead and check every reconstructed branch. The anchored decision rests on transfer assumptions rather than denying the two successful agent systems.

ANCHORED ESTIMATED R=0.29/0.49/0.70 with probabilities 0.32/0.55/0.13 gives single=0.32×0.29+0.55×0.49+0.13×0.70=0.45, range 0.29–0.70; bo4=0.29×0.32^4+0.49×(0.87^4−0.32^4)+0.70×(1−0.87^4)=0.58; pass@4=1−0.87^4=0.43; ub95=0.70. The low branch explicitly prices failed weights-only transfer; the upper branch preserves successful learned integration as a serious risk.
## 5. Verdict under the kill lines
The literature-conditioned section 4 verdict is CUT, a CONDITIONAL→CUT evidence re-estimate. The headline ANCHORED verdict is CONDITIONAL, UNCHANGED versus the screen: ESTIMATED bo4 clears by 0.02 and ub95 by 0.05. New cache systems strengthen the recipe, but neither agent result validates the specific artifact and budget. Require the concrete portfolio test rather than treating a longer prefix trace as hardness.
## 6. Redesign
Potential cause (a), a capable learned cache and allocator. REDESIGNABLE through an explicit outcome-conditioned portfolio condition. Re-attack basis=LITERATURE-ONLY; a graph-conditioned predictor with a learned value model is scientifically plausible, not a demonstrated twelve-hour agent solve.

Provide branching workflows with observable tool-result classes and joins whose useful completion depends on retaining complementary states. Competing joins share host/device transfer bandwidth, so independently accurate next-use probabilities can choose the wrong retained set. Expose all causally necessary features and representative value reversals on dev. Permit recomputation, prefetched restoration and simple policies, charging exact bytes, prediction, transfer and reconstruction in the same ledger. Training-only future traces may label counterfactual portfolios, while online inference sees only past observations.

Freeze CacheScout-style transition prediction, semantic/intent reuse, weighted Belady, recency fallback and a cost-aware two-tier allocator in the floor. The strongest re-attack learns joint values and solves a small contextual knapsack. It must learn non-additive join/transfer interactions; if additive scores or a generic knapsack already capture the whole gain, the condition fails and this task should be cut. A same-budget independent reference must demonstrate exact completed-workflow reserve, ensuring this is feasible frontier serving research rather than concealed future information.

ESTIMATED redesigned states 0.25/0.45/0.64 with probabilities 0.41/0.51/0.08 yield single=0.41×0.25+0.51×0.45+0.08×0.64=0.38; bo4=0.25×0.41^4+0.45×(0.92^4−0.41^4)+0.64×(1−0.92^4)=0.50; pass@4=1−0.92^4=0.28; ub95=0.64. Spread represents failure or success in learning portfolio interactions. Risks include cheap universal retention priorities and simulator labels that fail to transfer to real GPU queues.

ESTIMATED decisive cost: 8B serving subject and 10M predictor; 4 arms × 3 training seeds × 2 hours × 1 H100=24 GPU-h. Replays cost 4×3 workflow families×2 starts×1 H100-hour=24; label generation adds 16 and correctness evaluation 8, totaling 72 H100 GPU-h.
## 7. Measurement status
Rollouts UNMEASURED (planned independent predictor-training campaigns and complete rejoin replays). Grader noise UNMEASURED (planned training-seed and allocator-process replication). Score ladder UNMEASURED (planned semantic/transition-aware floor and a feasible joint-portfolio reference). Record forecast numbers below are ESTIMATED.
## Audit record
id: C020
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 4
sources_new_count: 4
sources_fetched_count: 8
old_single: 0.48
old_bo4: 0.59
old_pass4: 0.44
old_ub95: 0.74
new_single: 0.62
new_single_range: 0.38-0.80
new_bo4: 0.73
new_pass4: 1.00
new_ub95: 0.80
new_verdict: CUT
binding_line: bo4>0.60
flip: CONDITIONAL->CUT
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Test learned complementary-state portfolio admission across observable joins and shared host/device transfer contention.
redesign_single: 0.38
redesign_bo4: 0.50
redesign_pass4: 0.28
redesign_ub95: 0.64
redesign_gpuh: 72
attack_basis: LITERATURE-ONLY
demonstrated_ref: ServerBench, Opus 5.5 Claude Code, 2026; ArchAgent, AlphaEvolve Gemini unspecified, 2026
gap_to_attack: twelve-hour training and validation of a weights-only joint-memory predictor
subfield_sota_ref: workflow-transition cache management, CacheScout, 2026; cache-population feedback admission, Basin, 2026
anchored_single: 0.45
anchored_bo4: 0.58
anchored_pass4: 0.43
anchored_ub95: 0.70
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
