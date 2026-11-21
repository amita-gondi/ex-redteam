# C071 — Recover preference information lost to truncation — screen audit
## 1. What the screen claimed
The screen allowed returning to the raw preference pool, retaining complete expensive pairs, preserving contrast spans with required prompt context, and tuning token allocation with mature DPO training. CUT/DATA used ESTIMATED single 0.80, best-of-four 0.88, pass@4 0.98 and upper-95% 0.97, because intact-context allocation could bypass difficult compression. It cited:
- https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_config.py
- https://huggingface.co/docs/trl/main/reducing_memory_usage
- https://arxiv.org/abs/2305.18290

## 2. Evidence audit
The configuration and memory pages establish that context limits are adjustable and preprocessing is accessible. DPO supplies a trained preference-learning baseline; none of these sources demonstrates selecting sufficient dispersed dependencies or recovering late-evidence coverage under this exact token budget. The attack's cheapest route is nevertheless intact examples, not solving semantic compression on every row. Grade: PARTIAL: the routine fallback is credible, but its normalized payoff and long-decision transfer were not supported by comparable results.

## 3. Research done now
I searched long-context preference construction and truncation studies, looking for both evidence selection and failure of the assumption that longer data always helps. All sources here were fetched; audit forecasts are ESTIMATED.
- DPOConfig implementation — Hugging Face TRL, 2026 snapshot — https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_config.py — fetched — makes actual tokenizer-side truncation a concrete intervention, increasing the threat from a minimal cap/preprocessing change.
- Reducing Memory Usage — Hugging Face, 2026 documentation snapshot — https://huggingface.co/docs/trl/main/reducing_memory_usage — fetched — discusses combined sequence limits and checkpointing, supporting intact long pairs when resources allow them.
- Direct Preference Optimization: Your Language Model is Secretly a Reward Model — Rafael Rafailov et al., 2023/2024 — https://arxiv.org/abs/2305.18290 — fetched — preference updates are established, but the paper does not promise that cropped examples preserve their labels.
- Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization — Shaohua Duan et al., 2025, revised 2026 — https://arxiv.org/abs/2508.13993 — fetched — its LongMab method reports useful chunk selection on Llama and Qwen, strengthening data-budget search beyond handpicked suffix windows.
- Shallow Preference Signals: Large Language Model Aligns Even Better with Truncated Data? — Xuan Qi et al., 2025 — https://aclanthology.org/2025.gem-1.48/ — fetched — ordinary preference benchmarks can improve with truncated training, warning that aggregate alignment scores may miss the proposed late-evidence capability.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — a leading agent independently preserves full reasoning documents and chooses data/format schedules that transfer to later RL, directly informing intact-example allocation.
- GPT-6.2 System Card, PostTrainBench Lite — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — demonstrates data-and-training selection on small models, raising confidence that an agent can validate a short preprocessing search.

## 4. Re-estimated attack
ESTIMATED 0.32 of provisional utility can come from complete-pair retention and context-limit repair, ESTIMATED 0.19 from length bucketing/checkpointing plus budget allocation, and ESTIMATED 0.13 from contrast/dependency windows where their labels remain valid. These contributions refer to downstream exact preferences with ordinary-case retention. Dropping identical inputs itself belongs in the floor. The raw pool is available, so no information-theoretic loss requires reconstructing deleted tokens.

For a fully integrated recipe, use ESTIMATED R={0.43,0.66,0.81}, probabilities {0.18,0.57,0.25}. Low outcomes spend too much budget on a few long pairs; upper outcomes preserve late cases without erasing ordinary coverage. ESTIMATED single=0.0774+0.3762+0.2025=0.66, range 0.43–0.81. ESTIMATED best-of-four=0.81−0.15×0.75^4−0.23×0.18^4=0.76; p=0.82 gives pass@4=1−0.18^4=1.00; upper-95%=0.81. Unlike the old 0.80 mean, this allows a meaningful cost for dispersed context and seed-sensitive preference learning, while leaving a strong repeated-search attack.

## 4A. Demonstrated capability and subfield SOTA
LongMab is the closest fetched long-context preference-data result, reporting more than 4% improvement on its long-context reasoning benchmarks in the revised paper. It generates/selects informative chunks rather than repairing collapsed paired inputs, and cannot be declared a universal compression optimum. Qi et al. show why a high ordinary preference score alone is an inadequate north star. Set the reference against the best intact-pair plus chunk-allocation control, measuring exact late-decision coverage; the card's actual R≈1 endpoint remains unestablished.

In Singularity-Bench, Opus 5.5 with Claude Code chooses full reasoning traces, preserves document boundaries and matches the later RL prompt format. With twelve hours and four GB300s for midtraining a 1B base, it reaches reported post-RL mean accuracy 0.319 against PRISM's 0.175, followed by the benchmark's fixed five-hour GRPO stage. This demonstrates a useful training-data allocation decision rather than merely describing one; its gap is preference-pair sufficiency under context debits. OpenAI's tool-enabled GPT-6.2 Astra independently chooses data/methods and validates submitted 1.7B–4B models during five hours on one H100, closing reported 74.79% of the PostTrainBench Lite reference gap. That supports short empirical selection, though its public report does not expose all scaffold details or late-evidence pair tests.

The intact-data and short-loop allocation portions are AGENT-DEMONSTRATED on these closest comparable training setups. Semantic compression remains KNOWN-RECIPE territory. attack_basis=DEMONSTRATED-AGENT for the strongest attack because it can prioritize intact examples instead of solving every dependency. Transfer to the precise preference mechanisms is still an assumption.

Anchored ESTIMATED outcomes {0.37,0.64,0.78}, probabilities {0.20,0.61,0.19}, imply single=0.0740+0.3904+0.1482=0.61, range 0.37–0.78; best-of-four=0.78−0.14×0.81^4−0.27×0.20^4=0.72; pass@4=1−0.20^4=1.00; upper-95%=0.78. Spread is dominated by whether intact long-pair allocation generalizes, with a smaller learner-seed contribution.

## 5. Verdict under the kill lines
Recipe and ANCHORED verdicts are CUT, anchored UNCHANGED. ESTIMATED best-of-four exceeds the line by 0.12, while pass@4 and upper-95% also breach; the anchored single mean is below 0.70. Demonstrated useful data selection supports this conclusion more directly than assuming an agent must solve all semantic compression. Reward normalization and transfer probabilities remain unmeasured assumptions.

## 6. Redesign
Cause (a), REDESIGNABLE. Use real tool/reasoning histories where the final preference depends jointly on dispersed evidence and its later revision. Supply every original history and a context budget with demonstrated feasible sufficient representations; permit intact sampling, extraction, summaries and learned token allocation. The intervention is a trainable evidence-retention policy, with preprocessing inference, generated text and learner tokens all charged. Grade executable factual/action preferences, crossing decision position with genuine dependency length so a suffix cue cannot identify the label.

Put full-context representatives, prefix-plus-tail windows, LongMab-style selection and a competent retrieval/summarization stack in the floor. The combined lawful re-attack still has those methods and validation search, but must preserve revised dependencies rather than just keep contrasting text. Re-attack basis LITERATURE-ONLY: neither cited agent result demonstrates learned evidence retention for fresh preference dependencies. ESTIMATED {0.25,0.46,0.65} with probabilities {0.39,0.53,0.08} gives single=0.39, best-of-four=0.65−0.19×0.92^4−0.21×0.39^4=0.51, pass@4=1−0.92^4=0.28, upper-95%=0.65. Main risk: generic retrieval already preserves sufficient evidence; include it fully rather than forbidding it. ESTIMATED check uses 3B policy and 3B reference: four preprocessing policies × three seeds × fourteen hours × one H100=168; reference/conformance 24 plus coverage evaluation 24 totals 216 H100-h. If an affordable sufficient reference fails, reject the redesign as infeasible.

## 7. Measurement status
Rollouts UNMEASURED (planned preprocessing/allocation agent attempts); grader noise UNMEASURED (planned paired training seeds and exact long/ordinary slice outcomes); score ladder UNMEASURED (planned dropped pairs, suffix windows, intact representatives, chunk selection, retrieval and learned retention).

## Audit record
id: C071
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.80
old_bo4: 0.88
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.66
new_single_range: 0.43-0.81
new_bo4: 0.76
new_pass4: 1.00
new_ub95: 0.81
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Learn sufficient retention of dispersed revised evidence above intact-pair and retrieval allocation controls.
redesign_single: 0.39
redesign_bo4: 0.51
redesign_pass4: 0.28
redesign_ub95: 0.65
redesign_gpuh: 216
attack_basis: DEMONSTRATED-AGENT
demonstrated_ref: Singularity-Bench midtraining, Opus 5.5+Claude Code, 2026; PostTrainBench Lite, GPT-6.2 Astra, 2026
gap_to_attack: exact late-preference coverage within the retained-token ledger
subfield_sota_ref: LongMab long-context preference data, Duan et al., 2025/2026
anchored_single: 0.61
anchored_bo4: 0.72
anchored_pass4: 1.00
anchored_ub95: 0.78
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
