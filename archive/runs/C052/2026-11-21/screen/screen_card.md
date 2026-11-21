# C052 — Search that allocates shared answering capacity across campaigns — saturation screen
## 1. What the grader actually rewards
Reward follows final correct scientific decisions across all concurrent campaigns, with unanswered or displaced campaigns still counted and all answering tokens charged. R≈0 corresponds to the frozen competent shared-service floor; the no-op independent-agent scheduler must be at or below that floor. R≈1 is an attainable allocation control under the same service limit, rather than unlimited answering accuracy; its distance from the reference is UNMEASURED, and all forecasts and costs here are ESTIMATED.

Coordinated campaign allocation is the proposed reference, nominally ESTIMATED R=0.60, whose real decision-value position has not been measured.

## 2. Strongest lawful combined attack
Represent shared evidence as a dependency graph, collapse identical questions only when evidence versions agree, and update all dependent campaigns when an answer arrives. Allocate the next request by approximate expected reduction in terminal decision regret per token, with a minimum service share to avoid abandoning campaigns. [Correlated knowledge gradient](https://people.orie.cornell.edu/pfrazier/pub/CorrelatedKG.pdf) provides a concrete method for exploiting information shared among alternatives; its assumptions would need adaptation to discrete campaign decisions. Use short posterior rollouts to account for a question unlocking several downstream branches.

At the execution layer, batch compatible requests and retain exact evidence prefixes using [vLLM prefix caching](https://docs.vllm.ai/en/stable/design/prefix_caching/). Prefix reuse saves computation, not necessarily metered answering tokens: the attack only claims token savings for actual elimination of duplicate requests and shorter sufficient evidence. Tune the graph policy and response length jointly against terminal decisions. A frontier researcher can implement this without first discovering an unfamiliar learning mechanism.

ESTIMATED single-run R=0.77, range 0.62–0.89; ESTIMATED best-of-4=0.85; ESTIMATED pass@4 at the specified success threshold=0.98; ESTIMATED upper-95% projection=0.95. These are planning beliefs conditional on fixed native anchors, not empirical confidence limits. Even if the frozen floor already includes batching and a response cache, the correlated decision policy can recover much of the remaining gap. Residual errors come from badly estimated dependencies, surprising answer lengths and answers the fixed model cannot produce. The last category caps every legal policy and cannot be counted as useful research headroom.

## 3. Other routes
A greedy shared evidence cache plus expected-value-per-token queue is the strongest single standard recipe: ESTIMATED R=0.69, range 0.51–0.83. Its weakness is complementary questions whose value appears only after another answer, but that does not prevent good average utility on ordinary dependency graphs.

An offline policy sweep can compare greedy, limited lookahead, round-robin quotas and uncertainty sampling, then tune request length and admission thresholds on disclosed graphs. ESTIMATED R=0.74, range 0.58–0.87. Small outcome tables also make exact dynamic programming lawful when enough transition structure is exposed; private final answers must never enter that computation.

## 4. What would lower lawful saturation
Construct independently authored campaign graphs with complementary evidence purchases, delayed dependency revelation and nontrivial cancellation costs. Provide matching development graphs, keep all campaigns in the denominator, and choose budgets where both shallow greed and full enumeration lose to an executable bounded reference. ESTIMATED revised attack R=0.49–0.64: this narrows saturation but does not guarantee survival. ESTIMATED preparation is 6–10 person-days and ESTIMATED 32 H100-h for feasibility and terminal-decision verification. Merely increasing the simultaneous campaign count would mostly reward an established scheduler.

## 5. Decisive-check GPU-h re-estimate
The old estimate is ESTIMATED 6 GPU-h. Budget ESTIMATED 32 H100-GPU-h instead: an ESTIMATED 8B answering model, ESTIMATED 4 allocation arms, ESTIMATED 3 fresh graph blocks per arm with one answering seed per block, and ESTIMATED 2 device-hours per complete replay give 4×3×2=24. Repeated grading, prefix-cache warmup and answer calibration contribute ESTIMATED 8, making ESTIMATED 24+8=32. There is no model training in this pilot; policy fitting and graph search run on CPU. The earlier amount could compare a pair of tiny traces, but cannot establish whether coordination survives graph changes and model-answer stochasticity.

## 6. Duplicate check
T20 is MODERATE: its inspected packet includes evidence organization and inference-budget allocation but centers a single frozen-model harness rather than competing campaigns. T03 is MODERATE after source inspection because adaptive experiment allocation and terminal learning value overlap, although its resource is live training experiments rather than a shared answering queue. Neither has exactly this cross-campaign service intervention.

## 7. Verdict
CUT, with ESTIMATED best-of-4 exceeding its binding limit by ESTIMATED 0.25. ESTIMATED single-run reward is also above the single-run line by 0.07, and pass@4 and projected upper bound breach their limits. Correlated value-of-information scheduling is an established answer to the stated obstacle; the card has not supplied a harder residual regime.

## 8. Measurement status
Rollouts UNMEASURED (planned: full-budget independent scheduler construction on unseen campaign graphs); grader noise UNMEASURED (planned: repeated whole-service replays of fixed policies); score ladder UNMEASURED (planned: independent agents, exact caching, greedy allocation, correlated lookahead and same-budget stronger control).

## Screen record
id: C052
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.77
attack_single_range: 0.62-0.89
bo4_est: 0.85
pass4_est: 0.98
ub95_est: 0.95
gpuh_old: 6
gpuh_new_est: 32
duplicate_of: T20 MODERATE; T03 MODERATE
kill_reason: correlated information scheduling covers the central allocation mechanism
souping_flag: no
