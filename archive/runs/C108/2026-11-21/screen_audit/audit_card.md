# C108 — Teach an agent to create adversaries before choosing its data — screen audit
## 1. What the screen claimed
The screen's CUT, category DATA, joined regret-driven generation, evolutionary mutations, replay and transfer-based filtering, claiming these already supplied the competence-before-curation chain. ESTIMATED single/bo4/pass@4/ub95 were 0.72/0.81/0.94/0.93. It cited https://arxiv.org/abs/2012.02096, https://arxiv.org/abs/2203.01302 and https://arxiv.org/abs/2110.02439.
## 2. Evidence audit
The fetched old sources are Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design — Michael Dennis, 2020; Evolving Curricula with Regret-Based Environment Design — Jack Parker-Holder, 2022, revised 2023; and Replay-Guided Adversarial Environment Design — Minqi Jiang, 2021, revised 2022, respectively. They establish useful curriculum mechanisms in parameterized RL environments. They do not demonstrate mechanism-diverse executable code-tool adversaries, nor select a corpus through validated downstream repair transfer against adaptive opponents.

Grade ASSUMED: the decisive domain transfer was asserted. Mutation, solvability checks and prioritized replay have human-built precedents, but their success does not establish that a code-tool generator escapes shallow exploit families. The original estimate treated a proposed research program as a demonstrated combined recipe.
## 3. Research done now
- RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents — Mohamed Dhouib, 2026 — https://arxiv.org/html/2610.06401v2 — fetched — self-generated tool scenarios plus clean/injected training directly strengthen this card's baseline; benign utility is explicitly retained.
- WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections — Tri Cao, 2026 — https://arxiv.org/abs/2605.15030 — fetched — memory-based attack/guard co-evolution supplies a closer adaptive recipe than gridworld curriculum generation, raising attack plausibility.
- Agent vs. Agent: Automated Data Generation and Red-Teaming for Custom Agentic Workflows — Ninad Kulkarni/AWS AI Labs, 2025 — https://aclanthology.org/2025.emnlp-industry.62.pdf — fetched — automated adversary refinement works against tool agents, but improved defenses are future work, limiting the claimed end-to-end attack.
- Can Generalist Agents Automate Data Curation? — Feiyang Kang, 2026 — https://arxiv.org/html/2606.04261v1 — fetched — agents improve selected-data training, while frequent simple mixture edits weaken the assumption of deep mechanism discovery.

Searches targeted adaptive tool-agent attacks and robust training, rather than treating generic curriculum learning as sufficient. The four additions and three historical references were fetched; no source is search-only.
## 4. Re-estimated attack
All subsequent reward figures and distribution assignments are ESTIMATED. A stronger lawful recipe now uses generated executable scenarios, an adaptive attacker, admission checks, clean-context behavior preservation and independent transfer filtering. Provisional central utility contributions are 0.24 from covering known attack families, 0.18 from utility-preserving adversarial learning and 0.14 from transfer-aware selection, totaling 0.56. Generation validity earns no independent reward. Missing compositions and adaptive opponent responses remain outside those credits.

Model complete-run variation as R=0.31/0.56/0.78 with probabilities 0.25/0.55/0.20. The low case produces valid but redundant attacks; the middle repairs familiar mechanisms; the top discovers transferable compositions. ESTIMATED mean=0.54, range 0.31–0.78; bo4=0.78−0.22×0.80^4−0.25×0.25^4=0.69. Here p=0.20, so pass@4=1−0.80^4=0.59; q95=0.78. The broad spread comes from finding a useful mechanism before training consumes the budget, compounded by learner/opponent randomness. The old mean was excessive, yet repeated attempts still kill this recipe-conditional scenario.
## 4A. Demonstrated capability and subfield SOTA
RAISED is the closest strong human-engineered comparator found: on Gemma its AgentDojo ASR drops from 39.5% to 1.0±0.3%, with clean utility 83.5±0.8% versus 84.5% untreated; AgentDyn retains 60.0±2.4% utility. WARD adds adaptive co-evolution, but the metrics differ, so universal subfield leadership is unverified. The card's reference must beat these relevant families on its own code-tool invariants and independently adaptive opponents. Their public ASR cannot be relabeled R≈1; the raw utility floor and feasible ceiling still need paired calibration.

Agent demonstrations: Kulkarni's Sonnet 3.7 AgentHarm-Gen and DeepSeek-R1 Red-Agent-Reflect achieve 86% attack success against Gemini 2.5 Pro; search extends through eight attempts. Campaign wall time and accelerator use are unreported. That demonstrates adversary production, not downstream robust learning. Kang's Opus 4.7/Claude Code performs ten selection iterations for LLaVA-7B on one A100 per training run, obtaining 33.7 versus ICONS 33.3. Total elapsed time is unspecified; fixed-pool curation lacks co-evolving opponents and training-method adaptation.

KNOWN-RECIPE now includes much closer security-training work, but AGENT-DEMONSTRATED remains component-level. Overall attack_basis=LITERATURE-ONLY. Autonomous selection, integration and independent validation of the complete adversary-to-repair loop in twelve hours was not verified.

ANCHORED ESTIMATED distribution: 0.26 (0.30), 0.48 (0.60), 0.69 (0.10). The typical run captures 0.22 familiar coverage, 0.16 robust learning and 0.10 validated transfer. Mean=0.44, range 0.26–0.69; bo4=0.69−0.21×0.90^4−0.22×0.30^4=0.55; pass@4=1−0.90^4=0.34; q95=0.69. Tail mass and integration discount are assumptions, not benchmark-derived frequencies.
## 5. Verdict under the kill lines
Evidence-only verdict CUT: bo4 is 0.09 over, pass@4 0.09 over, and ub95 0.03 over. ANCHORED verdict CONDITIONAL, FLIPPED CUT→CONDITIONAL; bo4 is approximately 0.05 below its line (unrounded margin 0.0496). Direct tool-agent research strengthens the floor while the absence of a budget-matched autonomous learning loop prevents the old high score from surviving the amendment.
## 6. Redesign
Class (a), adversarial-data/RL machinery. REDESIGNABLE. Define development and private opponent families through executable stateful workflows: benign permissions, delayed tool results and cross-step dependencies can compose into attacks, while matched legitimate workflows need the same actions. Publish the authorization semantics and enough dev interactions to learn them. Train, update the defender, then test an independently implemented opponent adapting to that new defender. Reward constrained task utility rather than refusal or the number of attacks generated.

The combined re-attack is RAISED-style preservation, WARD-style refresh, mechanism clustering and regret replay. Its limitation becomes learning causally useful distinctions across workflow transitions, instead of memorizing common injection forms. Keep static corpora, simple authorization rules and a strong guard in the floor; do not add reward merely for completing generator stages. This remains useful frontier agent robustness research. Risks are an overly restrictive action policy matching the reference or a public guard covering the workflow semantics cheaply.

Re-attack basis LITERATURE-ONLY. ESTIMATED outcomes 0.22/0.41/0.62 with probabilities 0.35/0.58/0.07 give mean 0.36; bo4=0.62−0.21×0.93^4−0.19×0.35^4=0.46; pass@4=1−0.93^4=0.25; q95=0.62. ESTIMATED decisive check: 4B defender, four corpus arms × two seeds × twelve hours × one H100=96 GPU-h; 1B transfer proxies four × eight H100-hours=32; adaptive evaluation four × two × eight=64; honest-task and validity repeats=24. Total 216 H100 GPU-h, contingent on measured workflow throughput.
## 7. Measurement status
Rollouts UNMEASURED (planned: complete generator-to-defender campaigns). Grader noise UNMEASURED (planned: fixed-corpus retraining and opponent-search repeats). Score ladder UNMEASURED (planned: static library, adaptive attacks, behavior preservation, transfer filtering and feasible robust reference).
## Audit record
id: C108
old_verdict: CUT
evidence_grade: ASSUMED
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.72
old_bo4: 0.81
old_pass4: 0.94
old_ub95: 0.93
new_single: 0.54
new_single_range: 0.31-0.78
new_bo4: 0.69
new_pass4: 0.59
new_ub95: 0.78
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Evaluate causally composed workflow attacks after defender updates with matched useful benign actions.
redesign_single: 0.36
redesign_bo4: 0.46
redesign_pass4: 0.25
redesign_ub95: 0.62
redesign_gpuh: 216
attack_basis: LITERATURE-ONLY
demonstrated_ref: Agent vs Agent, Sonnet 3.7 and DeepSeek-R1, 2025; Curation-Bench, Opus 4.7 Claude Code, 2026
gap_to_attack: unaided attack generation through validated robust defender learning
subfield_sota_ref: RAISED, Dhouib, 2026; WARD, Cao, 2026
anchored_single: 0.44
anchored_bo4: 0.55
anchored_pass4: 0.34
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
