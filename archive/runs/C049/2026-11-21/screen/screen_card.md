# C049 — Research search over contradictory document versions — saturation screen
## 1. What the grader actually rewards
An answer must have the right numeric value and cite evidence whose experimental assumptions can coexist. Retrieving individually relevant passages is insufficient if their denominators, populations or report versions make the final calculation invalid. ESTIMATED R≈0 is competent version-aware evidence selection and ESTIMATED R≈1 an attainable coherent-answer pipeline; relevance-only retrieval is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Extract assertions into typed records carrying version ancestry, population, normalization, units and experimental configuration. Build a compatibility graph, retrieve candidate passages with hybrid search, then search coherent evidence bundles before invoking the fixed answering model. [GraphRAG](https://arxiv.org/abs/2404.16130) and [HippoRAG](https://arxiv.org/abs/2405.14831) establish graph-based evidence organization and multi-hop retrieval. Neither guarantees scientific compatibility; the attack must add explicit constraints rather than treat graph connectivity as support.

Use deterministic calculations for the numeric join and independent citation checks for every premise. [Pint's contexts](https://pint.readthedocs.io/en/0.25.1/user/contexts.html) support context-dependent unit conversions, illustrating a concrete implementation component for normalization checks. When assumptions are implicit, ask the fixed actor to propose competing interpretations, retrieve discriminating passages and reject unsupported joins. Tune bundle width, contradiction thresholds and retrieval depth under the full inference ledger. Do not silently substitute the outer researcher's answers for the fixed actor's outputs.

ESTIMATED single-run R=0.79, range ESTIMATED 0.51–0.93; ESTIMATED best-of-4=0.87; ESTIMATED pass@4 at R≥0.60=0.97; ESTIMATED projected upper-95% bound=0.98. The scale credits recovering most attainable answer gain from version isolation, typed joins and verified arithmetic. Residual errors concern unspoken changes in scientific meaning, ambiguous population definitions and extraction mistakes the frozen model cannot resolve. Those are real but the current specification gives no mechanism ensuring they dominate after a full coherent-bundle pipeline. Fresh correction chains defeat memorized answers, not the general graph-and-constraint algorithm.
## 3. Other routes
A single version-aware retrieval policy with strict same-condition evidence bundles reaches ESTIMATED R=0.67, range ESTIMATED 0.40–0.86. It handles explicit corrections cheaply, though excessive conservatism can miss valid cross-version combinations.

Searching retrieval/reranking weights, context budgets and bundle constraints reaches ESTIMATED R=0.73, range ESTIMATED 0.46–0.90. Brute-force coherent bundles are plausible when each question has a modest candidate pool. A lawful calculation-first route can obtain ESTIMATED R=0.63, range ESTIMATED 0.34–0.85 if structured tables expose enough conditions to compute answers before asking the actor to explain them. Citation correctness must be checked independently, but valid deterministic reasoning is not an exploit.
## 4. What would lower lawful saturation
Require scientifically meaningful latent assumption changes that can be identified from permitted evidence but are not reducible to date precedence or a fixed field join. Counterbalance explicit version cues, add valid cross-version bundles, and demonstrate an attainable control beyond graph extraction plus constraint search. ESTIMATED combined R could fall to 0.50–0.63. ESTIMATED cost is five scientific-curation weeks and ESTIMATED 48 H100 GPU-h for frozen-actor evaluation. Raising document count alone invites better indexing; hiding the compatibility rule would invalidate the task rather than create difficulty.
## 5. Decisive-check GPU-h re-estimate
Old card value: ESTIMATED 4 GPU-h. New ESTIMATED 16 H100 GPU-h assumes an ESTIMATED 8B frozen answer model, ESTIMATED four pipeline arms, ESTIMATED three independent report-family blocks and ESTIMATED one H100-hour per block: ESTIMATED 4×3×1=12. Embedding/index construction costs ESTIMATED 2 GPU-h and repeated fixed-answer/citation evaluation ESTIMATED 2 GPU-h. CPU graph and arithmetic work is separately charged elapsed time, without training a model. The old estimate might cover a tiny paired question set but underprices full bundle search and family generalization.
## 6. Duplicate check
Catalog T20: MODERATE, after reading its editable retrieval/context workers and frozen-actor outcome contract; C049 adds compatibility of cited scientific versions as an explicit target. Catalog T05: MODERATE, from its read provenance/version-scoped memory interface, but it learns persistent session memory rather than searching reports for numeric answers. The stronger citation condition adds enough to avoid a STRONG duplicate ruling.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds the gate by 0.27 and single-run by 0.09. Coherent evidence bundles with typed arithmetic are a strong direct route to the grader, leaving no supported broad margin.
## 8. Measurement status
Rollouts UNMEASURED (planned: full graph/constraint pipelines on new report chains). Grader noise UNMEASURED (planned: repeated fixed-actor answers and citation validation). Score ladder UNMEASURED (planned: relevance baseline, version retrieval, coherent bundles and attainable scientific-assumption control).
## Screen record
id: C049
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.79
attack_single_range: 0.51-0.93
bo4_est: 0.87
pass4_est: 0.97
ub95_est: 0.98
gpuh_old: 4
gpuh_new_est: 16
duplicate_of: T20 MODERATE; T05 MODERATE
kill_reason: version graph constraints and verified arithmetic target grader directly
souping_flag: no
