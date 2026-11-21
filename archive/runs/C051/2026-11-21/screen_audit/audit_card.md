# C051 — Search with retriever training that changes evidence reachability — screen audit
## 1. What the screen claimed
The screen combined an immutable lexical channel, dense hard-negative training, counterevidence replay and support/refutation queues. ESTIMATED single=0.73, bo4=0.81, pass@4=0.96 and ub95=0.94 led to CUT, category MEM: hybrid retrieval could bypass the feedback trap. Cited sources:
- https://arxiv.org/abs/2007.00808
- https://arxiv.org/abs/2104.08663

## 2. Evidence audit
ANCE supports mined negatives and refreshed indexes; BEIR establishes lexical retrieval as an out-of-domain baseline. Neither tests preservation of disconfirming evidence through changing agent queries. Finding evidence also need not improve independent recipe choices, particularly with unfrozen utility weights. PARTIAL: the compound research capability was extrapolated.

## 3. Research done now
Card forecasts, probabilities and future GPU allowances are ESTIMATED; external retrieval scores are attributed source results.
- Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval — Lee Xiong et al., 2020 — https://arxiv.org/abs/2007.00808 — fetched — Corpus-mined negatives and asynchronous index refresh are established training tools, with no proof that contradictory evidence receives appropriate relevance labels here.
- BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models — Nandan Thakur et al., 2021 — https://arxiv.org/abs/2104.08663 — fetched — Strong lexical robustness supports keeping a frozen branch; heterogeneous zero-shot retrieval does not demonstrate avoidance of hypothesis-dependent evidence censorship.
- BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval — Hongjin Su et al./benchmark maintainers, 2024 benchmark, 2026 leaderboard — https://brightbenchmark.github.io/ — fetched — Current reasoning-retrieval systems substantially outperform simple lexical matching, so an immutable BM25 channel is a safeguard rather than a completeness guarantee.
- Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems — Yilun Zhao et al., 2026 — https://arxiv.org/abs/2605.04018 — fetched — Multi-aspect evidence evaluation and complementary-positive training address evidence portfolios more directly than ANCE. This raises a better adaptation attack while warning that single-passage metrics conceal failures.
- CMASS: A ClimbMix Agentic Search Suite for Evaluating Search Agents Across Heterogeneous Tasks — Sahel Sharifymoghaddam et al., 2026 — https://arxiv.org/html/2608.20317v2 — fetched — Correct answers can coexist with incomplete evidence acquisition, and small actors perform much worse than frontier search agents. This cuts against treating a robust search index as sufficient for supported downstream research decisions.
- ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research — Soyoung Yoon et al., 2026 — https://arxiv.org/html/2609.01870v1 — fetched — Delaying consensus and reviewing alternatives demonstrate that evidence diversity is operationally achievable, strengthening explicit refutation search without establishing retriever-update safety.

## 4. Re-estimated attack
Keep sparse and frozen dense indexes alongside the updated encoder. Mine negatives only after distinguishing irrelevance from contradiction; retrieve both supporting and refuting queries, retain source versions and compare updated, frozen and union policies on protected development campaigns. Rebuild cost and every answer call are charged. An unchanged index remains a legal choice if adaptation is harmful.

A successful known-recipe pipeline plausibly earns ESTIMATED 0.24 through a frozen reachability backstop, 0.21 through complementary evidence/query expansion, 0.14 through safer training and 0.08 through downstream recipe selection: 0.67. These increments refer to an unfrozen provisional ladder. If the combined hybrid policy already defines the floor, this same intervention scores zero; the card must demonstrate additional native reserve rather than stretch the denominator.

Literature distribution R={0.45,0.68,0.82}, probabilities={0.15,0.65,0.20}. Query-policy collapse explains low outcomes; reliable counterevidence acquisition and transfer to recipe choices explain high ones. Encoder seeds, index refresh boundaries and evidence-graph families contribute spread. ESTIMATED single=0.67, range 0.45–0.82; bo4=0.82−0.14×0.80^4−0.23×0.15^4=0.76; pass@4=1−0.15^4=1.00 rounded; ub95=0.82. Compared with the old numbers, performance is less near-perfect because lexical availability does not ensure an agent asks the necessary query.

## 4A. Demonstrated capability and subfield SOTA
The fetched BRIGHT short-document leaderboard lists GRAIL first at 69.4 nDCG@10, dated November 10, 2026, ahead of Mira at 66.9. This is a reported retrieval ranking, not answer accuracy or a reproduced C051 control. Zhao's BRIGHT-Pro/RTriever work is the closer evidence-portfolio reference. Anchor the north star to supported answers and executed recipe utility after matched rebuild/training cost; BRIGHT scores cannot supply the task's R≈1 conversion. That constrained endpoint is still unmeasured.

Two demonstrated search systems give useful boundaries. ArcticSwarm's Qwen 3.5-27B agents achieve 82.6% corpus-answer accuracy with a gated board, approximately 24.9M end-to-end tokens per case and a 9,000-second timeout; its search scaffolding sustains alternative evidence paths but never updates retriever weights during the campaign. CMASS's GPT-6.1 Sol with Piika and BM25 reaches 90.1% strict set accuracy on its DSQA subset, while hop groundedness is 75.7%. Its generation safeguard is twelve hours; API compute is outside the paper's GPU accounting. This demonstrates strong search and remaining evidence gaps, not preservation of refutations through learning updates. Neither study tests downstream ML recipe utility or an 8B fixed actor.

The full combined attack is KNOWN-RECIPE, with only its search components AGENT-DEMONSTRATED: attack_basis=LITERATURE-ONLY. An unaided researcher must assemble a relevance-safe training set, characterize feedback-induced query drift and validate independent learning decisions in twelve hours. Evidence that an existing strong search scaffold answers questions is not evidence that this training intervention has been integrated successfully.

ANCHORED R={0.36,0.57,0.74}, mass={0.20,0.60,0.20}: ESTIMATED single=0.56, range 0.36–0.74; bo4=0.74−0.17×0.80^4−0.21×0.20^4=0.67; pass@4=1−0.80^4=0.59; ub95=0.74. The favorable branch assumes that the unchanged hybrid route remains effective across fresh terminology. That assumption, and unresolved answer/recipe weighting, explicitly underlie the verdict.

## 5. Verdict under the kill lines
Evidence re-estimate CUT; ANCHORED CUT, UNCHANGED. Anchored bo4 exceeds its gate by 0.07 and pass@4 by 0.09; ub95 sits 0.01 below its own cutoff. Current evidence weakens the claimed near-certainty but leaves a substantial lawful bypass because the grader does not establish a necessary causal benefit from retriever adaptation. No measured saturation claim is made.

## 6. Redesign
Cause (a), robust retrieval-stack bypass; REDESIGNABLE. Freeze an immutable hybrid policy as the competent floor and include it lawfully in every comparison. Build live research campaigns where newly learned concepts determine which previously accessible evidence refutes a proposed recipe. Provide equivalent dev opportunities, raw evidence access and explicit evidence-version provenance. Evaluate actual independent continuation utility with supported-answer coverage, using an unchanged-retriever ablation to establish whether adaptation helped. Freeze the scientifically justified compound weighting before seeing attacks.

Require semantic evidence portfolios at realistic cost. Test complementary positives, hard negatives, refutation queues, frozen-index unions and reranking together. The strongest re-attack learns relation-aware retrieval and alternative hypotheses; it must recognize when learned queries omit an accessible disconfirmation. Frontier labs would value that capability in self-updating research systems. If frozen hybrid retrieval matches the attainable reference, retire the task rather than prohibit it or reward training itself.

Redesign basis LITERATURE-ONLY. ESTIMATED outcomes {0.27,0.46,0.63}, probabilities {0.20,0.68,0.12}: single=0.44; bo4=0.63−0.17×0.88^4−0.19×0.20^4=0.53; pass@4=1−0.88^4=0.40; ub95=0.63. Pilot ESTIMATED 108 H100 GPU-h: 300M retriever, four arms × three seeds × 1.5 hours × one H100=18; fixed 8B actor campaigns add 4×3×2.5=30; independent 1B recipe continuations add 4×3×4=48; index/replay/evaluation adds twelve. Available inherited checkpoints are assumed. This tests both reachability and realized learning utility.

## 7. Measurement status
Rollouts UNMEASURED (planned complete retrieval-update campaigns on independently authored evidence graphs). Grader noise UNMEASURED (planned repeated actor trajectories and independent final recipe continuations). Score ladder UNMEASURED (planned frozen hybrid, updated encoder, full counterevidence union and attainable adaptive control with explicit native weights).

## Audit record
id: C051
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.73
old_bo4: 0.81
old_pass4: 0.96
old_ub95: 0.94
new_single: 0.67
new_single_range: 0.45-0.82
new_bo4: 0.76
new_pass4: 1.00
new_ub95: 0.82
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Require useful adaptive semantic evidence portfolios beyond a lawful frozen hybrid floor in live recipe-selection campaigns.
redesign_single: 0.44
redesign_bo4: 0.53
redesign_pass4: 0.40
redesign_ub95: 0.63
redesign_gpuh: 108
attack_basis: LITERATURE-ONLY
demonstrated_ref: ArcticSwarm, Qwen 3.5-27B, 2026; CMASS Piika, GPT-6.1 Sol, 2026
gap_to_attack: Search demonstrations omit retriever-update feedback and realized recipe utility
subfield_sota_ref: BRIGHT GRAIL 69.4 nDCG at 10, benchmark leaderboard, 2026; BRIGHT-Pro, Zhao, 2026
anchored_single: 0.56
anchored_bo4: 0.67
anchored_pass4: 0.59
anchored_ub95: 0.74
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
