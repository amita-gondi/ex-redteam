# C035 — Keep inference fast through online adapter admission — screen audit
## 1. What the screen claimed
The screen proposed dynamic multi-adapter serving with immutable version handles, asynchronous copies, staging memory and graph-slot reuse. It forecast ESTIMATED single=0.84, bo4=0.90, pass@4=0.99 and ub95=0.99, assigning CUT/SYS because online loading already exists. Its citations were:
- https://arxiv.org/abs/2311.03285
- https://arxiv.org/abs/2310.18547
- https://docs.vllm.ai/en/stable/features/lora/

## 2. Evidence audit
S-LoRA and Punica establish heterogeneous adapter batching with real memory management; vLLM exposes runtime admission rather than requiring a frozen inventory. None of these citations demonstrates an autonomous researcher validating atomic fresh-version boundaries and graph preparation on newly arriving structures in twelve hours. Grade: PARTIAL: the main execution substrate is well evidenced, while exact-version integration, graph-cache compatibility and the presumed reward recovery were inferred.

## 3. Research done now
- S-LoRA: Serving Thousands of Concurrent LoRA Adapters — Ying Sheng et al., 2023, revised 2024 — https://arxiv.org/abs/2311.03285 — fetched — Host-resident adapters, unified paging and heterogeneous kernels defeat the preloading straw baseline. This raises the serving attack without proving arbitrary arrival-time graph support.
- Punica: Multi-Tenant LoRA Serving — Lequn Chen et al., 2023 — https://arxiv.org/abs/2310.18547 — fetched — Shared-base concurrent adapter kernels demonstrate that distinct requested adapters can be batched efficiently. Version publication and first-use preparation are separate obligations here.
- LoRA Adapters — vLLM project, 2026 current documentation — https://docs.vllm.ai/en/stable/features/lora/ — fetched — Runtime load/unload functionality provides a direct implementation route; documentation alone supplies no latency or exact-version stress result for this card.
- ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving — Jiuchen Shi et al., 2026 — https://www.cse.ust.hk/~weiwa/papers/elora-hpca26.pdf — fetched — Dependency-aware adapter/KV residency and cost-based swapping improve measured first-token latency. This raises the public floor beyond LRU and undermines a redesign based merely on adding cache dependencies.
- Singularity-Bench: Can Agents Build Agents? — Y. Zhou, K. Agarwal, Z. Chen and coauthors, 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Demonstrated custom serving engines support substantial integration ability; the evaluated requests do not require online adapter version publication.
- InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents — J. Yeon, B. Rank and M. Andriushchenko, 2026 — https://arxiv.org/html/2607.20468v1 — fetched — Production-backend selection and tuning are agent-accessible, but observed narrow exploration warns against assuming a fully searched adapter/cache stack.

## 4. Re-estimated attack
ESTIMATED gain allocations are 0.45 dynamic batching/loading, 0.35 cost-aware residency and overlap, and 0.20 graph/version integration. ESTIMATED recovery fractions 0.98/0.80/0.46 give 0.45×0.98+0.35×0.80+0.20×0.46=0.81 rounded. Correctness is a prerequisite, not a separate reward bonus; stale outputs invalidate affected requests and cannot count as saved service time.

An ESTIMATED literature-capable execution yields R=0.65/0.81/0.89 with probabilities 0.12/0.58/0.30. The modes correspond to safe but blocking admissions, an overlapped mature runtime and effective cache/graph tuning. ESTIMATED mean=0.12×0.65+0.58×0.81+0.30×0.89=0.81, range 0.65–0.89. ESTIMATED bo4=0.89−0.08×0.70^4−0.16×0.12^4=0.87; p=1.00 gives pass@4=1−0^4=1.00; ub95=0.89. This distribution conditions on implementing the recipe successfully; section 4A removes that assumption. Its narrower upper tail than the screen reflects unavoidable cold transfers and graph misses, not new measured variability.

## 4A. Demonstrated capability and subfield SOTA
ELORA is the most relevant recent dependency-aware multi-adapter result fetched. Use its cost-aware residency with a current runtime-loader implementation as the reference configuration. R≈1 must be anchored to a subsequently demonstrated stronger admission/graph strategy at identical memory and exactness requirements. Published first-token gains neither provide that ceiling nor imply that a naive synchronous loader is a competent floor.

The two fetched agent results identify a remaining capability gap. Zhou et al.'s 2026 Singularity-Bench reports GPT-6.1 Sol+Codex beating SGLang income after twelve hours on four GB300s. It rebuilt serving machinery; fresh immutable adapter identities were absent. Yeon et al.'s 2026 InferenceBench reports GPT-5.4 in its Codex configuration improving serving speed on one H100 with two hours; a structured search prompt broadens exploration. It measures speed, not concurrent publication correctness. These are source-reported achievements, not card trials.

KNOWN-RECIPE covers dynamic loading and adapter/KV caching. AGENT-DEMONSTRATED evidence covers neighboring server construction but not the versioned online-admission contract, so attack_basis=LITERATURE-ONLY. The agent must connect loader lifecycle, in-flight handles, graph buckets and cache eviction and independently test races within twelve hours. Success looks plausible; assuming it is routine would repeat the screen's evidential error. The anchored verdict explicitly rests on that transfer assumption.

ANCHORED ESTIMATED outcomes are 0.40/0.59/0.71 with probabilities 0.18/0.64/0.18. They model an incomplete but safe adapter path, competent current-backend integration and successful optimized admission. ESTIMATED single=0.18×0.40+0.64×0.59+0.18×0.71=0.58, range 0.40–0.71. ESTIMATED bo4=0.71−0.12×0.82^4−0.19×0.18^4=0.66; pass@4=1−0.82^4=0.55 from p=0.18; ub95=0.71. Reruns primarily vary integration and policy validation, with exact grader noise still unmeasured.

## 5. Verdict under the kill lines
Section 4 remains CUT at ESTIMATED bo4=0.87. ANCHORED CUT is UNCHANGED versus the old verdict: bo4 exceeds its boundary by ESTIMATED 0.06 and pass@4 by 0.05, while single is 0.12 below its line. ELORA reinforces a strong lawful cache recipe, but the smaller anchored margins acknowledge the absent autonomous versioning demonstration. These are hypothesis-level breaches pending native anchors and full-budget trials, not observed S2 kills.

## 6. Redesign
Cause (a): production multi-adapter runtime replacement. REDESIGNABLE by admitting genuinely different, disclosed adapter execution graphs rather than new names for the same low-rank layout. Arrivals can place trained low-rank transformations at different supported modules and share reusable operator subgraphs; provide complete tensor schemas, operator semantics and an exact unfused interpreter. Each request pins an immutable graph/version. Compilation work, staging bytes, live KV dependencies and service all share the resource ledger.

Reward complete correct responses with first-use latency and full residency charged. Supply development examples for each supported operator family and mixed graph reuse, plus an attained specialized compilation/cache policy showing native reserve. This remains useful frontier customization infrastructure: new learned structures should enter service without global downtime. It does not rely on withholding graph meaning or forcing infeasible memory pressure.

Strongest re-attack is ELORA dependency caching plus vLLM-style admission, shape bucketing, asynchronous copies and compiler autotuning. It can handle ordinary ranks; the remaining opportunity is deciding which shared graph fragments to compile, retain or interpret as demand and KV lifetimes interact. Re-attack basis=LITERATURE-ONLY because the cited serving agents do not demonstrate this graph lifecycle.

ESTIMATED distribution 0.27/0.46/0.63, probabilities 0.35/0.55/0.10: useful generic compilation is common, a well-adapted online specialization policy less so. ESTIMATED single=0.35×0.27+0.55×0.46+0.10×0.63=0.41, range 0.27–0.63; bo4=0.63−0.17×0.90^4−0.19×0.35^4=0.52; pass@4=1−0.90^4=0.34; ub95=0.63. Residual risk is that a small graph-bucket enumeration solves every case or compile time is too small to matter end to end.

Decisive check ESTIMATED: an 8B base with supplied trained adapters, one H100, five admission/compiler arms, three graph-arrival seeds, one hour per run: 5×3×1×1=15.00 GPU-h. Add ESTIMATED 5.00 for independent graph/version truth and 4.00 for cold-start/race repetition, totaling 24.00 H100 GPU-h; adapter training is outside this pilot because the assets must already exist.

## 7. Measurement status
Rollouts UNMEASURED (planned dynamic-load and graph-admission trace replay). Grader noise UNMEASURED (planned repeated cold transfers and version-pinned output comparison). Score ladder UNMEASURED (planned current runtime, dependency-aware cache and attained graph-specialization controller).

## Audit record
id: C035
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.84
old_bo4: 0.90
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.81
new_single_range: 0.65-0.89
new_bo4: 0.87
new_pass4: 1.00
new_ub95: 0.89
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Admit immutable heterogeneous adapter graphs while optimizing shared compilation, KV lifetimes and real residency.
redesign_single: 0.41
redesign_bo4: 0.52
redesign_pass4: 0.34
redesign_ub95: 0.63
redesign_gpuh: 24
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench, GPT-6.1 Sol plus Codex, 2026; InferenceBench, GPT-5.4 plus Codex, 2026
gap_to_attack: atomic online versions and adapter-graph validation were not evaluated
subfield_sota_ref: ELORA dependency-aware adapter and KV caching, Shi et al., 2026
anchored_single: 0.58
anchored_bo4: 0.66
anchored_pass4: 0.55
anchored_ub95: 0.71
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
