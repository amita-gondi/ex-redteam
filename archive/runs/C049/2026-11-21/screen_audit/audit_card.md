# C049 — Research search over contradictory document versions — screen audit
## 1. What the screen claimed
The screen assembled typed version records, hybrid retrieval, compatibility-constrained evidence bundles, deterministic arithmetic and citation checking. Its ESTIMATED single/bo4/pass@4/ub95 were 0.79/0.87/0.97/0.98, with CUT, category MEM, because graph constraints supposedly make most numeric joins routine. Cited URLs:
- https://arxiv.org/abs/2404.16130
- https://arxiv.org/abs/2405.14831
- https://pint.readthedocs.io/en/0.25.1/user/contexts.html

## 2. Evidence audit
GraphRAG evaluates query-focused summarization, not valid numerical inference across scientific report revisions. HippoRAG supports graph-mediated multi-hop retrieval, while Pint implements conversions only after a user supplies the correct contextual relation. The key capability—extracting implicit population, normalization and experimental assumptions correctly—was therefore not established by the cited tools. Grade PARTIAL: retrieval and arithmetic components are real, but semantic compatibility is the hard unverified part of the attack.

## 3. Research done now
All reward forecasts and the scenario distributions in this audit are ESTIMATED. Reported benchmark percentages describe their authors' experiments only.
- From Local to Global: A Graph RAG Approach to Query-Focused Summarization — Darren Edge et al., 2024, revised 2025 — https://arxiv.org/abs/2404.16130 — fetched — Its global evidence organization helps find related assertions but does not certify that different report conditions may be joined.
- HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models — Bernal Jiménez Gutiérrez et al., 2024, revised 2025 — https://arxiv.org/abs/2405.14831 — fetched — Multi-hop graph access raises recall; conflicting edges still require an explicit validity model.
- Contexts — Pint developers, 0.25.1 documentation, accessed 2026 — https://pint.readthedocs.io/en/0.25.1/user/contexts.html — fetched — Contextual units are implementable, but the library cannot discover a changed denominator or experimental population for the actor.
- BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent — Zijian Chen et al., 2025 — https://arxiv.org/html/2508.06600 — fetched — Controlled corpus search demonstrates large retriever effects on final answers, supporting joint retrieval/context tuning while exposing dependence on the answering model.
- ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research — Soyoung Yoon et al., 2026 — https://arxiv.org/html/2609.01870v1 — fetched — Strong research agents can search alternatives and audit competing hypotheses. That strengthens bundle verification, but uses stronger actors and a different correctness criterion.
- When Evidence Conflicts: Uncertainty and Order Effects in Retrieval-Augmented Biomedical Question Answering — Yikun Han et al., 2026 — https://arxiv.org/abs/2605.14115 — fetched — Reversing contradictory evidence changes predictions even with both documents present. Retrieval completeness alone does not remove the compatibility hazard.
- Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation — Satyapriya Krishna et al., 2024, revised 2025 — https://arxiv.org/abs/2409.12941 — fetched — FRAMES supplies a closer multi-source reasoning comparator than summarization, without making scientific report-version consistency a solved property.

## 4. Re-estimated attack
Parse explicit version links and units into a graph, retain original passages, enumerate coherent bundles and calculate candidate numeric results using checked code. For implicit changes, have the fixed actor propose alternatives and retrieve evidence distinguishing their assumptions. The researcher may improve the pipeline but cannot replace the designated answering actor with its own stronger answers.

Conditional on a successfully integrated known recipe, allocate ESTIMATED 0.19 to version/population isolation, 0.23 to coherent multi-hop retrieval, 0.12 to arithmetic verification and 0.08 to alternative-assumption checks: 0.62. This assumes the provisional reward floor has not already eliminated all explicit joins. Remaining errors are scientific extraction and the frozen actor's interpretation limits.

Literature forecast R={0.40,0.63,0.82}, mass={0.20,0.60,0.20}. Easy explicit-chain coverage, partially inferred semantics and a particularly effective schema explain the modes. Document families and extractor errors matter more than arithmetic randomness. ESTIMATED mean=0.62, range 0.40–0.82; bo4=0.82−0.19×0.80^4−0.23×0.20^4=0.74; pass@4=1−0.20^4=1.00 rounded; ub95=0.82. This is materially below the old point estimate because graph connectivity and dimensional correctness do not establish valid scientific inference.

## 4A. Demonstrated capability and subfield SOTA
The strongest fetched corpus-search result is ArcticSwarm with GPT-5 at 88.3% on BrowseComp-Plus; its open-weight Qwen 3.5-27B result is 82.6%. Those anchor an ambitious search-system comparator, not C049's numeric-plus-compatible-citations ceiling. Han's conflicting-evidence result is closer to the semantic obstacle and does not report a solved compatibility method. R≈1 must therefore be an attainable coherent-answer control measured with the same frozen actor and report access; no published number pins it yet.

Two agent demonstrations matter. Chen's GPT-5 search-tool loop with Qwen3-Embedding-8B reaches 70.12% on the fixed corpus. It uses high reasoning effort and truncated search previews; the fetched report does not give a matched per-question wall/GPU ledger. Yoon's Qwen 3.5-27B ArcticSwarm uses a gated evidence board and review stages, with a 9,000-second timeout, approximately 24.9M recorded end-to-end tokens per case and an 83.3-minute median. Timeout-error reruns are allowed there, unlike unconditional retention of failures here. These show substantial multi-hop evidence work, but neither certifies cross-version assumptions with an 8B fixed actor or demonstrates that a researcher builds that pipeline unaided in twelve hours.

KNOWN-RECIPE graph/arithmetic processing is available; the full C049 attack remains LITERATURE-ONLY. AGENT-DEMONSTRATED general search does not imply the smaller actor can reliably extract scientific compatibility. Twelve-hour integration must establish schema coverage and validate families where dates and unit strings are insufficient.

ANCHORED R={0.31,0.50,0.69}, probability={0.25,0.61,0.14}: ESTIMATED single=0.48, range 0.31–0.69; bo4=0.69−0.19×0.86^4−0.19×0.25^4=0.59; pass@4=1−0.86^4=0.45; ub95=0.69. Scenario masses are judgment calls about extractor transfer, not search-benchmark solve rates. The anchored verdict rests on that assumption and the unresolved native anchors.

## 5. Verdict under the kill lines
The evidence-only recipe estimate gives CUT. ANCHORED verdict CONDITIONAL, FLIPPED CUT→CONDITIONAL: bo4 is only 0.01 below its threshold, pass@4 roughly 0.05 below, and ub95 0.06 below. Modern research agents strengthen the search component, while the frozen-actor and implicit-assumption gaps invalidate the old nearly complete attack. The required condition is substantive scientific compatibility beyond a fixed metadata join.

## 6. Redesign
Class (c), machine-exploitable explicit version semantics; REDESIGNABLE. Supply complete version histories and raw ML experiment tables where a report correction changes an estimand, population inclusion or normalization convention. Include valid older/newer combinations and invalid same-date combinations. Require a numeric result plus an executable provenance derivation whose permitted transformations are checked against independently authored experimental records. Publish examples of each transformation and allow access to all underlying evidence; the difficulty is selecting the scientifically valid derivation, not guessing undisclosed rules.

Freeze typed version graphs, hybrid search, exact arithmetic and bundle enumeration as the floor. The strongest re-attack infers latent measurement semantics, tests competing derivations and uses constraint solving over them. It falls short only where understanding the scientific design is necessary before any correct constraint graph exists. This is useful for auditing large ML experiment repositories. Risks are an overly expressive deterministic schema that compiles every answer, or an actor-limited ceiling with no stronger attainable control.

Redesign basis LITERATURE-ONLY. ESTIMATED R={0.24,0.43,0.61}, masses={0.25,0.65,0.10}: single=0.40; bo4=0.61−0.18×0.90^4−0.19×0.25^4=0.49; pass@4=0.34; ub95=0.61. Decisive pilot ESTIMATED 24 H100 GPU-h: fixed 8B actor, four pipelines × three independent report blocks × 1.5 hours × one H100=18; indexing adds three and repeated citation/derivation evaluation three GPU-h. CPU parsing and calculation time remain charged to each campaign.

## 7. Measurement status
Rollouts UNMEASURED (planned coherent-evidence pipelines across fresh correction families). Grader noise UNMEASURED (planned repeated frozen-actor extraction and deterministic provenance replay). Score ladder UNMEASURED (planned relevance retrieval, complete version/units floor, semantic derivation selector and attainable stronger control).

## Audit record
id: C049
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.79
old_bo4: 0.87
old_pass4: 0.97
old_ub95: 0.98
new_single: 0.62
new_single_range: 0.40-0.82
new_bo4: 0.74
new_pass4: 1.00
new_ub95: 0.82
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: c
redesign_status: REDESIGNABLE
redesign_oneline: Require evidence-grounded estimand transformations beyond explicit version and unit graph joins.
redesign_single: 0.40
redesign_bo4: 0.49
redesign_pass4: 0.34
redesign_ub95: 0.61
redesign_gpuh: 24
attack_basis: LITERATURE-ONLY
demonstrated_ref: BrowseComp-Plus, GPT-5 search loop, 2025; ArcticSwarm, Qwen 3.5-27B, 2026
gap_to_attack: Fixed smaller actor must infer scientific compatibility and cite valid numeric joins
subfield_sota_ref: BrowseComp-Plus 88.3 percent, ArcticSwarm GPT-5, 2026
anchored_single: 0.48
anchored_bo4: 0.59
anchored_pass4: 0.45
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
