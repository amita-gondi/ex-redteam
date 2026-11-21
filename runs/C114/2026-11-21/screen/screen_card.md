# C114 — An agent that learns when its own memory should expire — saturation screen
## 1. What the grader actually rewards
A carried memory policy must improve the training interventions chosen by otherwise reset agents across later projects. Retrieval and context costs count, so unlimited historical notes cannot earn free improvement, and deleting all memory loses still-useful evidence. ESTIMATED R≈0 means no advantage over a competent condition-aware memory floor; ESTIMATED R≈1 means attainable stronger downstream model gains at equal memory and experiment budgets. The no-memory agent and the inherited age-only memory both require measurement before treating ESTIMATED reference R≈0.60 as meaningful.
## 2. Strongest lawful combined attack
Store each recommendation separately from its supporting observations and applicability predicates: model family, optimizer state, data regime, batch semantics and evidence confidence. [Zep](https://arxiv.org/abs/2501.13956) verifies a temporal knowledge-graph approach to evolving memory, while [Mem0](https://arxiv.org/abs/2504.19413) verifies extraction and update mechanisms for bounded long-term agent memory. Neither source proves scientific applicability inference, but both establish that invalidation and selective retrieval are mature baseline components.

At each project transition, compare conditions before retrieving actionable advice. Keep the mechanism explanation even when the old numerical recommendation becomes inapplicable; mark uncertainty when state is unavailable, and commission a small paid calibration experiment before large reuse. Rank advice by expected gain after probe and context cost, preserve source runs for auditing, and maintain contradictory results rather than overwriting them with a single universal lesson. Tune expiration and revalidation policies across full development project sequences. This addresses the exact proposed hard case—retaining a mechanism while withdrawing an old recommendation—without a new memory-learning principle.

ESTIMATED single-run R=0.75, range 0.54–0.89; ESTIMATED oracle best-of-4=0.83; ESTIMATED pass@4 at R≥0.60=0.96; ESTIMATED projected upper-95% score=0.94. Implicit optimizer/data conditions can remain hard to infer from limited history. Nonetheless, refusing to apply uncertain advice until a cheap matched probe succeeds is often enough; the card has not made that probe economically difficult or shown that a learned expiration policy finds information unavailable to this ordinary procedure.
## 3. Other routes
A provenance-aware temporal memory with condition filtering is the strongest single standard recipe. ESTIMATED R=0.61, range 0.40–0.80. It may already fix most harmful transfer without training any memory model.

Search over confidence decay, compatibility features, retrieval depth, probe triggers and context allocation has ESTIMATED R=0.70, range 0.47–0.87. Tune on complete sequences rather than individual retrieval accuracy so keeping old useful evidence is rewarded. A lawful conservative route retrieves observations but suppresses recommendations unless revalidated; ESTIMATED R=0.64, range 0.39–0.85. That route can bypass the need to decide a precise expiration time and should be included rather than barred for avoiding the preferred intervention.
## 4. What would lower lawful saturation
Use independently authored project sequences where applicability is latent but inferable from earlier interventions, and where revalidation consumes enough budget to compete with useful training. Preserve some old evidence whose value survives several changes, so universal expiration loses capability. ESTIMATED score reduction is 0.14–0.22, to around 0.53–0.61, with repeated search still dangerous. ESTIMATED preparation cost is 9–16 person-days and 200 H100-h for authentic transition histories. Merely hiding version labels would convert a solved explicit check into an arbitrary surprise unless other lawful evidence identifies the transition.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 10 GPU-h. New ESTIMATED cost is 144 H100 GPU-h: 4 memory policies × 2 sequence seeds × 3 successive projects × 4 H100-h on 1B subject models = 96; fixed 4B agent execution and retrieval comparisons = 24; independent final capability and repeat-grade evaluation = 24. ESTIMATED total 96+24+24=144. Memory construction is mostly CPU work, but its claimed value requires executing later interventions. The previous allowance can test advice retrieval cheaply, not whether selective reuse delivers superior scientific training decisions.
## 6. Duplicate check
T05, MODERATE: its opened source already submits revision-aware memory, invalidation and expected-value refresh on evolving ML projects. C114 narrows the treatment to expiration of experimental advice and explicitly grades new model gains, rather than all later correct session work. This is substantial overlap, but the stronger downstream learning estimand prevents claiming identical grader targets without qualification.
## 7. Verdict
CUT. ESTIMATED single-run reward is 0.05 above its limit and ESTIMATED best-of-4 is 0.23 above. Condition-scoped provenance plus paid revalidation is a competent complete replacement for an age-based memory policy, leaving no specified research residual large enough for the bar.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent memory-policy development over fresh project sequences). Grader noise UNMEASURED (planned: repeat reset-agent decisions and subject-training seeds with a fixed memory policy). Score ladder UNMEASURED (planned: no memory, age expiry, condition filtering, probe-gated reuse, reference and stronger same-cost policy).
## Screen record
id: C114
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.75
attack_single_range: 0.54-0.89
bo4_est: 0.83
pass4_est: 0.96
ub95_est: 0.94
gpuh_old: 10
gpuh_new_est: 144
duplicate_of: T05 MODERATE
kill_reason: condition scoped memory and revalidation solve stale advice reuse
souping_flag: no
