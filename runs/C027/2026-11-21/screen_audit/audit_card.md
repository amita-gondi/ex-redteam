# C027 — A curriculum that teaches the agent to discover new tools — screen audit
## 1. What the screen claimed
The screen generated executable missing-operation episodes, filtered them by campaign utility, and combined coding imitation, a skill library and outcome training. It estimated single/bo4/pass@4/ub95 at ESTIMATED 0.63/0.73/0.78/0.89 and CUT, category MEM, assuming ordinary code transfer solves most omissions. It linked:

- https://arxiv.org/abs/2305.16291
- https://arxiv.org/abs/2302.04761

## 2. Evidence audit
Voyager: An Open-Ended Embodied Agent with Large Language Models — Guanzhi Wang, 2023, fetched — demonstrates an executable skill library and feedback-driven curriculum in Minecraft, rather than a trained researcher inventing ML diagnostics. Toolformer: Language Models Can Teach Themselves to Use Tools — Timo Schick, 2023, fetched — learns API invocation from filtered examples; its tools already exist. The original attack's decisive jump is from these ingredients to novel scientific measurement and net downstream learning.

Grade: PARTIAL. Tool-use learning and reusable code are demonstrated individually. Neither source validates the entire curriculum-generation, policy-training and research-deployment chain under a shared allowance. The screen also leaves the hidden omission family unspecified, so its claim that most are numerical recombinations is an assumption about task construction.

## 3. Research done now
- CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets — Lifan Yuan, 2023/2024 — https://arxiv.org/abs/2309.17428 — fetched — Validated GPT-4 solutions become reusable code tools. This strengthens execution-filtered libraries, but the system does not train the agent to discover a scientific information gap.
- ToolRL: Reward is All Tool Learning Needs — Cheng Qian, 2025 — https://arxiv.org/abs/2504.13958 — fetched — Tool-selection rewards improve training beyond simple imitation. This raises the learning component while leaving new-tool invention and campaign utility outside its reported endpoint.
- Tool-Genesis: A Task-Driven Tool Creation Benchmark for Self-Evolving Language Agent — Bowei Xia, 2026 — https://arxiv.org/abs/2603.05578 — fetched — Interface and executable-logic errors propagate into downstream failures even for strong models. Its one-shot regime is weaker than a full repair loop, but it directly challenges treating tool creation as automatically solved.
- CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution — Xu Huang, 2025 — https://arxiv.org/html/2512.23880v1 — fetched — Scientific skill construction improves executable science tasks. The benchmark isolates a useful autonomous subsystem; broader human-assisted demonstrations should not be mistaken for unaided performance.
- LLM Agents Making Agent Tools — Georg Wölflein, 2025 — https://aclanthology.org/2025.acl-long.1266.pdf — fetched — TOOLMAKER turns scientific repositories into tested interfaces, including model-training tools. It raises the generic-wrapper threat while preserving the distinction between wrapping known code and inventing a discriminating statistic.

## 4. Re-estimated attack
All score contributions are ESTIMATED. Execution-filtered code examples plausibly supply 0.21 reward, varied tool-gap episodes and repair training add 0.16, and selecting curricula by completed campaign utility adds 0.13. The mean near 0.50 leaves synthesis/training cost and unseen scientific abstractions unresolved.

An ESTIMATED two-regime forecast assigns probability 0.55 to R=0.37 and probability 0.45 to R=0.65. The high outcome occurs when omissions match learned wrapper/measurement patterns; the low outcome reflects trained tool competence without a useful diagnostic. Curriculum seed, policy optimization and downstream exploration all contribute. ESTIMATED single=0.55×0.37+0.45×0.65=0.50, range 0.37–0.65. ESTIMATED bo4=0.37×0.55^4+0.65×(1−0.55^4)=0.62; pass@4=1−0.55^4=0.91 with p=0.45; ub95=0.65. This lowers the screen's mean and upper tail while retaining repeated-search danger. The distribution has no measured calibration, and independent restarts are a conditional assumption.

## 4A. Demonstrated capability and subfield SOTA
TOOLMAKER and CASCADE are the strongest directly relevant scientific tool-construction systems located, without a shared leaderboard permitting a universal winner claim. The reference should match their competent repository reuse, then earn additional reward only from newly informative measurements and realized ML gains. No published score anchors a top bucket after curriculum training and generation costs.

TOOLMAKER uses GPT-4o and reports twelve correct tools out of fifteen; per-tool actions/API costs are available, without a matched elapsed-time or accelerator allowance. That establishes integration rather than curriculum-induced invention. CASCADE's GPT-5/DeepSolver reports 93.26% SciSkillBench mean success and 587.84 seconds average execution through APIs; total GPU use is unspecified. It constructs science skills during inference, rather than training a research policy and measuring subsequent ML gains. Both are attributed experimental results, not observations generated in this workspace.

KNOWN-RECIPE combines tool learning, code retrieval and repair. AGENT-DEMONSTRATED evidence supports useful tools, but not the complete training-to-novel-research transfer demanded here. Therefore attack_basis=LITERATURE-ONLY. The remaining twelve-hour obligation is to generate informative episodes, fit a policy and validate its learning benefit, with all branches charged.

ANCHORED ESTIMATED uniform [0.26,0.54] credits common tool transfer but discounts this unshown chain: single=0.40, range 0.26–0.54; bo4=0.26+0.28×4/5=0.48; pass@4=1−(1−0)^4=0.00; ub95=0.26+0.95×0.28=0.53. Continuous spread approximates curriculum quality and learner variation. Native anchors and an attainable discovery-trained control are missing, so these margins do not establish passage.

## 5. Verdict under the kill lines
Section 4 gives CUT through ESTIMATED bo4=0.62 and pass@4=0.91. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL, nearest to bo4 with clearance 0.12. Tool-Genesis failures and the narrower endpoints of TOOLMAKER/CASCADE prevent translating code capability into high whole-chain reliability. The condition is a learning-dependent advantage over an unchanged strong coder and a fully charged tool-library baseline; the favorable estimate rests on that unresolved scientific reserve.

## 6. Redesign
Cause (a), standard coding/tool-learning stack; REDESIGNABLE. Give every agent unrestricted ordinary Python and profiler access. Generate curricula around authentic training ambiguities: similar validation deterioration can arise from data duplication, optimizer-state lag or interference between gradient components. Useful episodes require constructing a measurement such as a matched state-reset continuation, per-source gradient interference estimate or held-out resampling contrast, then choosing a better training intervention.

Use fresh causal compositions with all relevant logs and data available. Score final trained quality after curriculum synthesis, policy fitting, diagnostic code and unsuccessful experiments. Include unchanged TOOLMAKER-style coding, CRAFT-like libraries and ToolRL-style learning as floors. Demonstrate transfer beyond the particular measurement vocabulary using an ablation with the same code tokens and compute. A lab would value research-policy training that teaches when existing metrics are insufficient; hiding APIs would not create that value.

The strongest redesigned attacker synthesizes those measurements and trains on execution-filtered outcomes. Re-attack basis LITERATURE-ONLY. ESTIMATED R∼U[0.24,0.51] yields single=0.38, bo4=0.24+0.27×4/5=0.46, pass@4=0.00 and ub95=0.24+0.95×0.27=0.50. The unsupported part is transferable diagnostic selection; a generic code agent may already perform it, which would kill the learning-dependent design.

Pilot cost ESTIMATED 312 H100 GPU-h: a 4B policy, four curriculum arms, three seeds, six hours on two H100s costs 144; 1B downstream learners consume 4×3×8×1=96; demonstration filtering adds 48 and independent evaluation 24. Total 144+96+48+24=312. No work in this budget is authorized or executed now.

## 7. Measurement status
Rollouts UNMEASURED (planned: independently generated curricula and cold downstream research workflows). Grader noise UNMEASURED (planned: paired policy-training seeds and repeated fixed-tool campaigns). Score ladder UNMEASURED (planned: generic coder, repository wrapper, filtered imitation, outcome curriculum and attainable causal-measurement reference).

## Audit record
id: C027
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.63
old_bo4: 0.73
old_pass4: 0.78
old_ub95: 0.89
new_single: 0.50
new_single_range: 0.37-0.65
new_bo4: 0.62
new_pass4: 0.91
new_ub95: 0.65
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Train invention of discriminating learning measurements with a common general execution interface and fully charged downstream utility.
redesign_single: 0.38
redesign_bo4: 0.46
redesign_pass4: 0.00
redesign_ub95: 0.50
redesign_gpuh: 312
attack_basis: LITERATURE-ONLY
demonstrated_ref: TOOLMAKER, GPT-4o, 2025; CASCADE DeepSolver, GPT-5, 2025
gap_to_attack: curriculum-induced scientific tool invention after generation and training costs
subfield_sota_ref: scientific tool construction TOOLMAKER and CASCADE, 2025
anchored_single: 0.40
anchored_bo4: 0.48
anchored_pass4: 0.00
anchored_ub95: 0.53
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
