# C022 — A research search tool that learns from failed reproductions — saturation screen
## 1. What the grader actually rewards
A reset frozen researcher uses the submitted retrieval/extraction tool to choose training recipes, and actual training utility determines reward. Retrieving a failed-reproduction note is useful only if its conditions change the executed recipe for the better. ESTIMATED R≈0 is the complete competent evidence-tool floor and ESTIMATED R≈1 an attainable stronger tool-assisted campaign; positive-only search is provisionally ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60, with no native training-gain anchors established.
## 2. Strongest lawful combined attack
Build a hybrid lexical/dense index over all legal reports, code diffs and failed-run notes, then rerank by applicability to the current proposed intervention. [BEIR](https://arxiv.org/abs/2104.08663) verifies strong lexical and reranking baselines across retrieval domains. [SciFact](https://aclanthology.org/2020.emnlp-main.609/), whose paper was verified in web search, supplies a concrete scientific support/refutation evidence formulation. Neither benchmark measures downstream recipe learning, so their scores cannot be imported into this screen.

Extract a versioned evidence record containing implementation, data regime, compute, optimizer, failure symptom, intervention and stated boundary conditions, while preserving linked original passages. Expand each proposal into prerequisite and falsification queries, retrieve both supporting and contradictory records, and return a compact condition comparison to the frozen agent. Use code/config identifiers as exact anchors and semantic retrieval for differently worded failure mechanisms. A second retrieval pass follows unresolved dependencies rather than a fixed failure taxonomy. Tune retrieval depth, condition matching and context allocation on full reset campaigns, including executed recipes and complete experiment cost.

ESTIMATED single-run R=0.79, range 0.55–0.91; ESTIMATED oracle best-of-4=0.86; ESTIMATED pass@4 at R≥0.60=0.97; ESTIMATED upper-95% projection envelope=0.96. These remain judgmental forecasts. Most gain should come from making the missing conditions available in the agent's context and preventing positive-claim dominance. The residual is causal transfer between genuinely different mechanisms and whether the fixed agent can act on conditional evidence. Because the tool may restructure and compare evidence, that agent limitation does not automatically protect the task: carefully packaged prerequisites can make the repair nearly explicit.
## 3. Other routes
- Structured condition extraction plus lexical retrieval of failed notes: ESTIMATED R=0.61, range 0.36–0.82. Exact optimizer/version/symptom matches can already expose many missing implementation assumptions.
- Sweep chunk boundaries, sparse/dense ranking weights, contradiction prompts, condition filters and context budget, selecting by actual reset-agent campaign outcomes. ESTIMATED R=0.73, range 0.48–0.89. Retrieval recall alone would select the wrong target and is not used for this estimate.
- Give the frozen agent an exhaustive, compressed condition ledger rather than search results where the corpus fits. ESTIMATED R=0.68, range 0.39–0.88. This lawful full-context bypass should be tested before claiming hard evidence discovery.
## 4. What would lower lawful saturation
Require composing conditional findings across independent failed reproductions where no single note names the missing prerequisite, and where a paid diagnostic experiment disambiguates competing explanations. Keep all necessary evidence accessible and dev context limits predictive. Hold the full hybrid/structured/multi-hop tool in the floor and require an executed training advantage beyond it. Forecast after such a revision: ESTIMATED R=0.46, range 0.24–0.68. Cost is ESTIMATED several weeks of authentic failure-ledger and causal-dependency authoring plus ESTIMATED 240 H100 GPU-h of downstream campaigns. A rare failure vocabulary alone is unlikely to survive semantic expansion.
## 5. Decisive-check GPU-h re-estimate
Old pilot: ESTIMATED 7 GPU-h. Revised ESTIMATED 144 H100 GPU-h assumes an ESTIMATED 8B frozen local agent and ESTIMATED 1B training subjects. ESTIMATED 4 retrieval arms×3 campaign seeds×8 H100-hours of downstream continuation costs ESTIMATED 96 GPU-h; agent inference and embedding/reranking add ESTIMATED 24 GPU-h, and independent loss/retention grading adds ESTIMATED 24 GPU-h. Total ESTIMATED 96+24+24=144. If a metered hosted agent replaces local inference, its separate cost must be stated rather than called free GPU work. The old allowance can compare retrieval outputs but cannot substantiate the task's real training-utility endpoint.
## 6. Duplicate check
Catalog T20 (`task_catalog_v3_full/packets/T20.md`, source opened): MODERATE. It already permits a full frozen-actor retrieval/tool stack, but scores executable document/SQL/code outcomes; C022 measures recipe selection through later training utility and specifically conditions on negative experimental evidence. v3 07B, previously opened, is WEAK because it trains an evidence evaluator rather than revising the retrieval tool. Same broad workflow does not establish identical grader targets.
## 7. Verdict
CUT. The ESTIMATED best-of-four breach is 0.26 and single-run breach ESTIMATED 0.09. Condition-aware evidence extraction and complete retrieval are mature components whose combination directly repairs the stated positive-claims indexing failure.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent tool-building attempts followed by reset-agent campaigns). Grader noise UNMEASURED (planned: fixed-tool agent repeats and paired subject training seeds). Score ladder UNMEASURED (planned: positive-only, failure lexical, structured hybrid, dependency-seeking retrieval and stronger attainable evidence tool).
## Screen record
id: C022
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.79
attack_single_range: 0.55-0.91
bo4_est: 0.86
pass4_est: 0.97
ub95_est: 0.96
gpuh_old: 7
gpuh_new_est: 144
duplicate_of: catalog-T20 MODERATE; v3-07B WEAK
kill_reason: complete condition-aware retrieval supplies the missing evidence
souping_flag: no
