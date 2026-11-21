Frontier reference for the saturation-screen audit — November 21, 2026; incorporates the project lead’s 12:04 PM PT binding update. Desk research only; no experiments performed.

The attack must be anchored to a demonstrated agent trajectory. A human recipe, a successful component, or a stronger model’s release does not demonstrate autonomous discovery and validation of the card’s combined solution within 12 hours. Public results establish substantial capability, but leave material gaps in budget comparability, autonomy, and transfer.

**Definitions and scoring rule**

**KNOWN-RECIPE** means a human-built recipe exists in the literature, with an identifiable task, implementation, and evaluation. It establishes an available method, not the attacker’s ability to select and execute it.

**AGENT-DEMONSTRATED** means an identified frontier model, in a documented agent protocol, was shown to find, integrate, execute, and independently validate the relevant recipe without human steering during the attempt, within a comparable time/compute budget. Prebuilt general tools are allowed; a supplied answer-specific implementation, manual repair, or manual reprompting must be disclosed and cannot establish unaided discovery. Comparability includes model size being trained, hardware, feedback availability, initialization, metric, and setup/validation time.

Assign each card’s proposed attack an `attack_basis`:

* **DEMONSTRATED-AGENT:** a qualifying demonstration supports the actual combined attack under comparable conditions. Only this label justifies a high attack score; it is necessary, not sufficient evidence of reliability across cards.
* **LITERATURE-ONLY:** a recipe or system exists, but its autonomous discovery/integration/validation within the card’s budget is undemonstrated. Longer-budget, incomplete, or non-agent automation results belong here for the unsupported attack claim.
* **ASSUMED:** the proposed combination, budget transfer, or success is conjectural. Mark quantitative projections **ESTIMATED**; do not assign invented success probabilities.

A demonstration of components A and B separately does not demonstrate A+B. Missing critical autonomy, budget, or validation metadata prevents promotion. Published demonstrations remain author-reported unless independently replicated. “No demonstration found” below means none verified in this search, not proof none exists.

**Dated frontier reference**

OpenAI’s GPT-6.2 Astra/Sol card was published November 17; Astra supports tools and subagent delegation. Anthropic’s November 9 Fable/Mythos 5.2 announcement documents Claude Code and orchestration, while stating that relevant kernel/architecture research remains around Opus 5.5 capability. Gemini 4 Neon’s November 18 card identifies Carbon as its parent. These configurations define reference candidates, not interchangeable benchmark scores. [1], [2], [3], [4]

“~10T parameters” remains an **assumption**, not a demonstrated frontier specification. Total/active counts for these closed systems are **unverified**. Google describes the underlying Gemini 4 Argon as a sparse mixture-of-experts transformer; that architectural disclosure supplies no numeric count. Context length is not parameter count. [5]

**Per-capability evidence ledger**

The bullets identify the strongest relevant verified results located, with narrower evidence where the requested demonstration is absent. “Comparator” means the best relevant published human/system reference located, not a claim of universal November SOTA. Absolute field-wide SOTA is **unverified** where benchmarks differ or rankings were not retrievable. Labels apply to the described attack scope, never automatically to every card in that subfield.

* **GPU kernels/compilers.** November 2026: Gemini 4 Neon XHigh, `agy` harness, RTX PRO 6000, reports 36.66× geomean Kimi-Linear decode speedup; elapsed search time is unreported on the fetched run page. March KernelAgent reports 250/250 correct kernels and 1.56× versus torch.compile on 100 L1 tasks; backbone and campaign runtime are unspecified there. **Comparator:** CUDA Agent’s human-engineered RL system reports faster-than-torch.compile rates of 100%/100%/92% on KernelBench L1/L2/L3 (2026). These suites and ratios differ. No comparable-budget end-to-end compiler-development demonstration was verified; unknown-duration runs cannot support a 12-hour high score: **LITERATURE-ONLY** pending timing and card equivalence. [6], [7], [8]

* **Serving/inference systems.** AutoTuneBench (2026) demonstrates 1.2753× SGLang throughput on GB10/Qwen2.5-7B after 20 iterations, but explicitly uses a deterministic proposer: this is not frontier-agent discovery. Engine-candidate timeboxes are 15–30 minutes; complete campaign runtime is not stated. **Comparator:** the same human-built SGLang default and tuned configuration; the vLLM arm gains only 1.005× p50. No unaided frontier-agent serving-stack discovery/integration/validation within 12 hours was verified. A fast decode kernel does not establish scheduler, batching, cache, and workload integration: **LITERATURE-ONLY**. [9]

* **Pretraining data curation/dedup/mixtures.** Curation-Bench (2026): Opus 4.7/Claude Code selects DataComp-Small CLIP data, with one H100 and approximately four hours per train/evaluate cycle (**ESTIMATED** by authors). It beats top-30% CLIP-score filtering; the text provides no exact CLIP score or total session duration. Its stronger numerically tabulated instruction-data result is 33.7±0.3 versus ICONS 33.3, using ten iterations and one A100 for LLaVA-7B training. **Comparator:** DCLM’s human-built filtering/dedup/mixing framework spans 412M–7B and reports 64% MMLU for a 7B model trained on 2.6T tokens (2024, revised 2025). No comparable 12-hour language-model pretraining dedup/mixture demonstration was verified: **LITERATURE-ONLY** for that combined claim. [10], [11]

* **RL post-training/reward modeling.** TrainExplorer/GLM-5.2, built on Claude Code (November 16, 2026), runs planning, data processing, training, and evaluation within ten wall-clock hours on one 80GB flagship GPU. It scores 39.02 weighted aggregate versus 31.70 for the same model in Claude Code; official instruct models score 51.14 under larger undisclosed development budgets. This is **DEMONSTRATED-AGENT** for bounded post-training, not automatically learned-reward design. PostTrainBench traces show some GRPO/DPO usage, but no comparable autonomous reward-model construction/calibration result was verified. Its November 20 site adds Astra; current ranking values were not retrievable, so latest rank is **unverified**. TrainExplorer’s seven-task mix retains BFCL, removed in PostTrainBench v1.2: do not compare those aggregates directly. [12], [13]

* **Optimizer/training-recipe search.** OpenAI’s unnamed evaluation scaffold with GPT-6.2 Astra saves 42.87% NanoGPT baseline training time after two hours on one H100 (2026). **Comparator:** best human solution saves 72.38%; human development time is unspecified. This is narrow **DEMONSTRATED-AGENT** evidence. METR’s Budget NanoGPT best run saves 15.7% with 48 hours/eight H100s/250M tokens; tested models include Fable 5.1, Opus 5.5, and GPT-6 Astra. A human, with AI assistance, reports 41% in about 60 hours against a different preceding record. Autoresearch’s Claude-based self-report claims 126 trials in approximately 10.5 hours on one H100, validation bits/byte 0.997900→0.969686; exact Claude version is unspecified. That reported combination is evidence to inspect, not independently established card-wide reliability. [1], [14], [15]

* **HPO/experimental design.** The two-hour Astra/NanoGPT experiment above demonstrates narrow search. Original MLE-bench’s o1-preview+AIDE reaches bronze-or-better on 16.9% of 75 tasks with 24 hours/one A10 (2024). The November 2026 MLE-Bench Revised result is Astra’s 96.06 mean percentile against generated reference solutions; runtime is unspecified. **Comparator:** historical Kaggle human medal thresholds in the original benchmark; generated references in the revision are not human experts. No comparable-budget demonstration of general scientific experimental-design competence was verified. Narrow training HPO can be **DEMONSTRATED-AGENT**; arbitrary card-level experiment design remains **LITERATURE-ONLY** or **ASSUMED**. [1], [16]

* **Memory/retrieval systems.** Agentic AutoRAG (2026) uses Kimi-K2.5 diagnosis/proposal, local embedding/reranking, and API generation/judging. Thirty-trial searches consume 11–16M embedding tokens per dataset; hardware count and elapsed time are unspecified. It reports 77% median healthcare exam accuracy versus the strongest compared baseline’s 71.5%, plus held-out QA evaluations. **Comparator:** the paper’s Bayesian MO-TPE/random/greedy baselines, not universal retrieval SOTA. No verified unaided 12-hour persistent-memory architecture discovery and validation was found. RAG configuration search exists, but its budget transfer is **ASSUMED**; published RAG recipes are **LITERATURE-ONLY** for a broader memory attack. [17]

* **Scientific/simulation ML.** PaperBench Science (2026): GPT-6 Astra, scaffold/hardware unspecified in the fetched report, achieves 59.08% partial score and 13.98% “full” reproduction, meaning above 90% rubric credit, across 93 tasks; limits are 4–24 hours, median seven. **Comparator:** expert-built validated reference workflows; no matched timed human baseline. Original PaperBench (2025) reports o1+IterativeAgent at 24.4% rubric credit in 12 hours/one A10. Its three-paper comparison is best-of-three ML PhDs 41.4% after 48 hours versus o1 26.6% after 36 hours. Successful budget-matched individual reproductions could qualify; the aggregate does not demonstrate arbitrary simulation-ML attacks: **LITERATURE-ONLY** until task/run matching. [18], [19]

* **Privacy/unlearning.** **No agent-engineering demonstration verified**: AUBench (2026) tests human-selected GD/KL/NPO methods on Llama-3.1-8B and Qwen3-8B with memory/tools; the agent is the object being unlearned, not an autonomous method inventor. **Comparator:** among its Llama parameter-only baselines, NPO reduces forget F1 to 27.0% while retain F1 falls to 34.4%; no unique privacy–utility SOTA follows. Memory/tool access changes the trade-off. Discovery scaffold, search time, and engineering compute: not applicable/unreported. **LITERATURE-ONLY** for those methods; an agent-designed combined privacy attack remains **ASSUMED**. [20]

* **Evaluation/grader design.** Double Ratchet/Opus 4.7 (2026) co-evolves metrics and skills over 100 skill rounds with interleaved metric rounds, retaining 88–110% of oracle-driven held-out improvement. Compute/wall time are unspecified; unaided status of the documented detector/rubric repair is **unverified**. **Comparator:** supplied ground-truth anchors/oracle metrics; PaperBench’s author-built rubrics yield judge F1 0.83 (2025). METR’s 48-hour task-building agents generally fail inclusion requirements despite three test environments and 100M developer tokens. No verified unaided 12-hour general grader-design/validation demonstration: **LITERATURE-ONLY**; autonomous discovery of trustworthy criteria remains **ASSUMED**. [21], [19], [14]

**What the evidence permits**

Longer-budget success is not a 12-hour result. Sakana AI Scientist-v2 uses Claude 3.5 Sonnet/GPT-4o and a 15-hour paper-generation cap; one of three selected workshop submissions clears review. AlphaEvolve’s Gemini search delivers a 23% kernel gain/1% training-time reduction, but describes days of experiments; its 2026 cache-policy example takes two days. Neither supplies the missing comparable-budget combined attack. [22], [23], [24]

RE-Bench’s 2024 agents beat average experts at two-hour budgets, but average humans score almost twice the best agent at 32 hours; best-of-shorter-attempt selection differs from serial integration. METR’s November 2026 pooled 50% horizons are **ESTIMATED** at 40 human-hours for GPT-6 Astra (95% CI 13–2645 hours) and 39 for Opus 5.5 (12–1253). Those measure task difficulty, not uninterrupted agent runtime or guaranteed success. [25], [14]

For each card, record model/scaffold/version, source trajectory, unaided status, exact combined changes, target scale, starting assets, accelerator count, aggregate accelerator-hours, wall time, grader access, held-out validation, and failures. Require the entire combined attack to meet the demonstration rule before scoring it high. Partial rubric credit is not complete card success. Keep incomplete metadata as evidence gaps; do not fill them with our own proposed recipe.

Operational attacker: the dated public systems above with lawful tools and explicitly specified resources (**assumption**), twelve wall-clock hours from disclosure including setup and validation, no human steering. Relevant 1.7B–4B post-training is evidenced; coverage of all 0.3B–4B RL cards is not. Noisy graders, slow training, selection over many trials, and component interactions require fresh validation. The audit’s reliable claim is the measured result under its reported conditions; transfer beyond those conditions is **ASSUMED**, not a demonstrated attack score.

## Sources

Every entry was **fetched November 21, 2026**; none is search-only. Linked titles resolve to the opened URLs.

1. OpenAI (2026). [GPT-6.2 System Card][1], November 17.
2. OpenAI (2026). [GPT-6.2 Astra Model][2].
3. Anthropic (2026). [Claude Fable 5.2 and Mythos 5.2][3].
4. Google DeepMind (2026). [Gemini 4 Neon — Model Card][4].
5. Google DeepMind (2026). [Gemini 4 Argon — Model Card][5].
6. Elliot Arledge/kernelbench.com (2026). [Gemini 4 Neon XHigh: Kimi-Linear Decode, RTX PRO 6000][6], November 18; independent of Stanford KernelBench.
7. Weinan Dai et al. (2026). [CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation][7].
8. Kaiming Cheng et al., PyTorch (2026). [KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration][8].
9. Li Chen, harnets.ai (2026). [AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines][9].
10. Feiyang Kang et al. (2026). [Can Generalist Agents Automate Data Curation?][10].
11. Jeffrey Li et al. (2024; revised 2025). [DataComp-LM: In search of the next generation of training sets for language models][11].
12. Xuannan Liu et al. (2026). [TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration][12].
13. AISA group/PostTrainBench team (2026). [PostTrainBench: leaderboard, protocol, changelog, observations][13].
14. Megan Kinniment et al., METR (2026). [AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure][14], November 20.
15. Agent posting for Andrej Karpathy (2026). [Session report: 0.9979 → 0.9697 in 126 experiments][15].
16. Chan Jun Shern et al., OpenAI (2024). [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering][16].
17. Lasse B. Strand et al. (2026). [Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents][17].
18. Elvis Zhang Research, Pipeline Lab (2026). [PaperBench Science: expanding PaperBench into scientific domains][18].
19. Giulio Starace et al., OpenAI (2025). [PaperBench: Evaluating AI’s Ability to Replicate AI Research][19].
20. Junkai Lin et al. (2026). [Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents][20].
21. Xing Zhang et al. (2026). [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents][21].
22. Yutaro Yamada et al. (2025). [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search][22].
23. Google DeepMind (2025). [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms][23].
24. AlphaEvolve team, Google DeepMind (2026). [AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields][24].
25. METR (2024). [Evaluating frontier AI R&D capabilities of language model agents against human experts][25].

[1]: https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts
[2]: https://developers.openai.com/api/docs/models/gpt-6.2-astra
[3]: https://www.anthropic.com/claude-fable-and-mythos-5-2
[4]: https://deepmind.google/models/model-cards/gemini-4-neon/
[5]: https://deepmind.google/models/model-cards/gemini-4-argon/
[6]: https://kernelbench.com/runs/rtxpro6000/20261118_150415_agy_gemini-4-neon-xhigh_02_kimi_linear_decode
[7]: https://arxiv.org/abs/2602.24286
[8]: https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/
[9]: https://arxiv.org/html/2609.18123v1
[10]: https://arxiv.org/html/2606.04261v1
[11]: https://arxiv.org/abs/2406.11794
[12]: https://arxiv.org/html/2611.20430v1
[13]: https://posttrainbench.com/
[14]: https://metr.org/blog/2026-11-20-q4-2026-capability-update/
[15]: https://github.com/karpathy/autoresearch/discussions/43
[16]: https://arxiv.org/html/2410.07095v1
[17]: https://arxiv.org/html/2610.08452v1
[18]: https://pipelinelab.ai/blog/paperbench-expanded/
[19]: https://arxiv.org/html/2504.01848v1
[20]: https://arxiv.org/html/2610.17659v1
[21]: https://arxiv.org/html/2607.12790v1
[22]: https://arxiv.org/html/2504.08066v1
[23]: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
[24]: https://deepmind.google/blog/alphaevolve-impact/
[25]: https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/
