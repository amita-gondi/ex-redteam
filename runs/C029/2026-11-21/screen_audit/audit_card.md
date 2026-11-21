# C029 — Exact speculative decoding across tool-boundary rollback — screen audit
## 1. What the screen claimed
The screen joined exact speculative verification, immutable prefix identities, copy-on-write cache branches and acceptance/risk-dependent draft depth. It forecast ESTIMATED single/bo4/pass@4/ub95=0.79/0.86/0.97/0.97 and CUT, category SYS, because ancestry caching appears to capture the available legal reuse. Its sources were:

- https://proceedings.mlr.press/v202/leviathan23a.html
- https://arxiv.org/abs/2312.07104

## 2. Evidence audit
Fast Inference from Transformers via Speculative Decoding — Yaniv Leviathan, 2023, fetched — proves and demonstrates exact-distribution acceleration, without promising the identical sampled trajectory under an arbitrary random-stream contract. SGLang: Efficient Execution of Structured Language Model Programs — Lianmin Zheng, 2023/2024, fetched — demonstrates prefix-tree caching and structured execution, but not arbitrary tool-result rollback with the card's token-for-token oracle. Their composition is plausible and substantial engineering, rather than a directly measured complete solution.

Grade: PARTIAL. The prefix invariant and exact decoder are genuine foundations. What remains unshown is budgeted integration, numerical consistency on the timed path and enough throughput reserve beyond a fully competent combined floor. A transformer suffix changed by an ancestor revision costs recomputation for the author as well as the attacker.

## 3. Research done now
- EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test — Yuhui Li, 2025 — https://arxiv.org/abs/2503.01840 — fetched — Strong modern draft modeling improves speculative acceleration. It raises the legal decoder baseline; its distributional guarantee and draft-training setup do not establish rollback-safe trajectory identity.
- SPECTRE: Hybrid Ordinary-Parallel Speculative Serving for Resource-Efficient LLM Inference — Jincheng Xie, 2026 — https://arxiv.org/abs/2605.08151 — fetched — Implements scheduling/overlap within SGLang at large-model scale. This strengthens the combined serving recipe, with a remote-drafter resource contract unlike the small colocated target/draft pilot.
- SWE-Serve: Benchmarking Agentic Engineering for Production Inference Serving — Jennifer Williams, 2026 — https://arxiv.org/html/2609.26777v1 — fetched — Includes speculative runtime, streaming KV commit and cache-lifecycle changes with executable tests. Its production-test gap is evidence against assuming that a locally correct state patch survives complete serving workloads.
- Singularity-Bench: Can Agents Build Agents? — Infini-AI Lab, 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Agents build performant full engines within the target wall-time class. Accuracy-gated serving is closer than isolated kernel generation, but still weaker than equality of every committed token after revisions.

## 4. Re-estimated attack
All reward reasoning is ESTIMATED. Correct ancestry tracking and conservative invalidation plausibly contribute 0.30, exact decoder integration supplies 0.21, and adaptive drafting/verification scheduling adds 0.12. This totals 0.63 under an optimistic integration assumption, leaving numerical path differences and nonreusable suffix work.

ESTIMATED R=0.51 with probability 0.33 and R=0.69 with probability 0.67. The lower mode is a correct but conservative runtime; the upper mode adds effective speculative scheduling. Most variation comes from finding a reliable execution/sampling path and workload-sensitive tuning, not arbitrary grader noise. ESTIMATED single=0.33×0.51+0.67×0.69=0.63, range 0.51–0.69. ESTIMATED bo4=0.51×0.33^4+0.69×(1−0.33^4)=0.69; pass@4=1−0.33^4=0.99 with p=0.67; ub95=0.69. Both mean and tail fall versus the screen because tested components do not guarantee the full exact rollback path. Independent restart assumptions and provisional normalization limit these forecasts.

## 4A. Demonstrated capability and subfield SOTA
EAGLE-3 and SPECTRE supply strong located SOTA controls for draft quality and serving overlap, respectively. Neither is a top result on tool-boundary rollback with identical token outputs. Anchor the reference to native useful target-time throughput above an exact ancestry-aware combined floor; no fetched source establishes its attainable R≈1, so physical reserve remains unmeasured.

Singularity-Bench's Opus 5.5/Claude Code reports serving income of 11.52 versus SGLang's 8.18 USD/GPU-hour after twelve hours on four GB300s. Its answer-accuracy gate and larger hardware allocation do not establish exact rollback. SWE-Serve reports 75.5% mean feature pass@1 for both GPT-5.6 Sol and Opus 5 in mini-SWE-agent, under a 210-minute CPU/single-H100 limit. Speculative state commits appear in its inventory; aggregate feature completion is still different from this token-equality throughput metric. These source results demonstrate integration while leaving the final exactness obligation open.

KNOWN-RECIPE is exact speculative sampling plus ancestry-safe cache management. AGENT-DEMONSTRATED evidence reaches related full-engine integration; it does not establish this complete exact-trajectory recipe. attack_basis=LITERATURE-ONLY. The additional obligation is validating committed tokens and reconstructing every invalidated state while preserving a throughput gain inside the same research budget.

ANCHORED ESTIMATED uniform [0.38,0.66] gives single=0.52, range 0.38–0.66; bo4=0.38+0.28×4/5=0.60 rounded. Its unrounded value exceeds the boundary slightly. With p=(0.66−0.60)/0.28, ESTIMATED pass@4=1−(1−p)^4=0.62; ub95=0.38+0.95×0.28=0.65. The spread represents continuous integration/tuning quality, discounted from section 4 by the exactness gap. This moderate mean still produces an unsafe repeated-search tail; it remains an assumption-based forecast, not demonstrated saturation.

## 5. Verdict under the kill lines
Evidence re-estimate CUT; ANCHORED verdict CUT, UNCHANGED. The robust anchored binding line is pass4>0.50, breached by ESTIMATED 0.12; bo4 is also slightly over before rounding. SWE-Serve and Singularity-Bench justify a credible integration threat, while the invariant leaves limited unique author headroom. The verdict rests on assumed transfer to exact rollback and unidentified native anchors, explicitly weaker evidence than a successful measured attack.

## 6. Redesign
Cause (a): mature decoder/cache stack. REDESIGNABLE. Make the research target joint speculation and cache placement for asynchronous tool branches under realistic memory pressure. Branches disclose ancestry, outstanding tool dependencies and empirical completion histories; costs include eviction, data movement, draft work and target recomputation. Several requests share prefixes but have different reachable rejoins, so keeping the deepest cache is not always useful. All such regimes must appear predictively in dev.

Require exact deterministic decoding or a fully specified coupled random stream, checked on the timed committed path. Include SGLang-style radix caching, conservative invalidation, strong speculative drafts, risk-adaptive depth and standard cost-aware eviction as the floor. The reference must exploit a demonstrable interaction between tool-return hazard and future target-state reuse, with a native throughput advantage that survives equal-memory and equal-compute comparisons. This is useful frontier serving work without withholding required tool semantics.

The strongest redesigned attack adds a learned hazard model to greedy recomputation-cost caching. Re-attack basis LITERATURE-ONLY, since the fetched systems do not validate exact asynchronous rejoins. ESTIMATED R∼U[0.28,0.57] yields single=0.43; bo4=0.28+0.29×4/5=0.51; pass@4=0.00; ub95=0.28+0.95×0.29=0.56. Ordinary online caching may absorb the supposed interaction; if a tuned generic policy matches the reference, there is no redesigned reserve.

Decisive-check ESTIMATED 60 H100 GPU-h: an 8B target and 1B draft, four engine arms, three authored branch workloads, two hours on one H100 per run gives 24. Exact target-only replay adds 12, independent warmed repeats add 12 and higher-concurrency validation adds 12: 4×3×2×1+12+12+12=60. No draft training is assumed; permitted fixed draft assets must fit and be licensed before the pilot.

## 7. Measurement status
Rollouts UNMEASURED (planned: complete engine submissions on fresh tool trees). Grader noise UNMEASURED (planned: repeated warmed target-time measurements and coupled-token replay). Score ladder UNMEASURED (planned: target-only decoding, full flush, exact ancestry cache, adaptive speculation and joint cache-placement reference).

## Audit record
id: C029
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.79
old_bo4: 0.86
old_pass4: 0.97
old_ub95: 0.97
new_single: 0.63
new_single_range: 0.51-0.69
new_bo4: 0.69
new_pass4: 0.99
new_ub95: 0.69
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize exact speculation jointly with memory placement across observable asynchronous tool rejoins.
redesign_single: 0.43
redesign_bo4: 0.51
redesign_pass4: 0.00
redesign_ub95: 0.56
redesign_gpuh: 60
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench, Opus 5.5/Claude Code, 2026; SWE-Serve, GPT-5.6 Sol and Opus 5/mini-SWE-agent, 2026
gap_to_attack: identical committed-token trajectories and throughput after arbitrary tool-prefix revisions
subfield_sota_ref: speculative drafts EAGLE-3 2025; parallel speculative serving SPECTRE 2026
anchored_single: 0.52
anchored_bo4: 0.60
anchored_pass4: 0.62
anchored_ub95: 0.65
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
