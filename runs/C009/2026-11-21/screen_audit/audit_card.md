# C009 — Optimizer state for episodically reactivated modules — screen audit
## 1. What the screen claimed
The attack jointly searched active-update clocks, inactive moment decay, selective resets and return warmups, with cold-resume validation. ESTIMATED single/bo4/pass@4/ub95 were 0.80/0.87/0.98/0.97. CUT, category TRAIN, rested on a small configuration search repairing the exposed stale-state failure. Old URLs:
- https://arxiv.org/abs/1412.6980
- https://docs.pytorch.org/docs/stable/generated/torch.optim.SparseAdam.html

## 2. Evidence audit
Adam: A Method for Stochastic Optimization — Diederik P. Kingma, 2014/2015, fetched at the arXiv URL — establishes the recurrence but not a dormancy-aware solution. SparseAdam — PyTorch, 2026 access to undated documentation — the old URL redirects; the substantive page fetched is https://docs.pytorch.org/docs/2.15/generated/torch.optim.SparseAdam.html. It masks parameter and moment updates for sparse gradients, explicitly an approximation rather than universal dense-Adam equivalence.

Grade: PARTIAL. The basic counter/moment mechanics are solid, but the old citations do not demonstrate post-reactivation loss gains or retention at matched active FLOPs. A module-local clock and a sparse-coordinate mask are different objects. Gradient-conditioned decisions also require a configurable hook; absent that hook, the lawful attack must search duration/activity-based rules.

## 3. Research done now
- SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training — Tianjin Huang, 2025 — https://arxiv.org/abs/2501.06842 — fetched — Demonstrates reset/clipping benefits in language-model pretraining and sparse-momentum settings. This raises the plausibility of managing stale state, but spike contamination differs from returning useful old moments.
- GradientStabilizer: Fix the Norm, Not the Gradient — Tianjin Huang, 2025, revised 2026 — https://arxiv.org/abs/2502.17055 — fetched — The fetched current version has this title, replacing the Stable-SPAM title shown in search. It reports improved optimizer-state stability through norm control; it supplies an additional conventional baseline, not proof of dormancy transfer.
- Maintaining Plasticity in Deep Continual Learning — Shibhansh Dohare, 2023, revised 2024 — https://arxiv.org/abs/2306.13812 — fetched — Demonstrates learning deterioration across task changes despite common optimizer choices. It lowers confidence that bookkeeping fixes solve genuine representation plasticity; its weight-reinitialization method is outside the submitted configuration unless explicitly allowed.

The search covered sparse experts, optimizer clocks, momentum resets and continual plasticity. Current fetched versions, rather than search-title memory, determine the evidence used.

## 4. Re-estimated attack
ESTIMATED recipe contributions are 0.30 from coherent local bias correction, 0.27 from the best inactive decay/reset convention and 0.16 from jointly tuned warm returns and retention weights: total 0.73. This credits ordinary clock repair heavily because the card names stale moments as the inherited cause and matches activation statistics across development and hidden histories. It leaves some loss for useful historical direction and task-dependent curvature.

For a fully integrated mature search, take ESTIMATED R uniform on [0.62,0.84]. The continuous spread represents remaining threshold, seed and task-switch variation; it is not a measured noise band. Single=(0.62+0.84)/2=0.73. Expected maximum of four uniform draws is 0.62+0.22×4/5=0.80; p=1.00 gives pass@4=1−0^4=1.00; ub95=0.62+0.95×0.22=0.83. This replaces the old arbitrary bound with explicit finite support. The recipe point is lower because sparse-update documentation does not establish full conditional-state utility.

## 4A. Demonstrated capability and subfield SOTA
SPAM is the strongest directly relevant reset-based training system consulted at the proposed subject scale; its comparisons span models through 1B parameters. GradientStabilizer supplies a current stabilization competitor. Neither establishes a dormancy optimum, so put all legal reset/norm/clock variants in the native-loss floor and measure a stronger same-budget return policy before assigning R≈1. The claimed reference remains a hypothesis, not a published benchmark score.

- Session report: 0.9979 → 0.9697 in 126 experiments — Claude agent, version unspecified, in Karpathy autoresearch, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched. The one-H100, approximately ten-and-a-half-hour log includes joint optimizer, momentum-warmup and schedule trials with retained validation gains. This directly demonstrates the search style, although it is a self-report on a smaller continuously active model.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched. An internal NanoGPT evaluation reports Astra saving 42.87% training time in two hours on one H100; scaffold internals are not disclosed. It demonstrates bounded training-loop optimization, while its speed-to-quality metric omits dormant-skill retention.

Basis DEMONSTRATED-AGENT for low-dimensional optimizer/configuration search, the closest comparable capability actually required by this exposed repair. KNOWN-RECIPE state fixes need limited integration rather than a new learned semantic extractor. Exact dormant-module transfer is not demonstrated: successful short-probe ranking and sufficient trial throughput in C009 remain explicit assumptions. If full trajectories alone reveal rankings, this basis loses budget comparability and must be downgraded.

ANCHORED ESTIMATED distribution: probability 0.23 at R=0.31 for failed integration/proxy selection; probability 0.77 uniformly spread on [0.60,0.74] for a competently validated search. Single=0.23×0.31+0.77×0.67=0.59, range 0.31–0.74. Integrating the fourth power of its CDF gives bo4=0.74−0.29×0.23^4−0.14×(1−0.23^5)/(5×0.77)=0.70. Pass@4=1−0.23^4=1.00 rounded, not literal certainty. Ub95=0.60+0.14×(0.95−0.23)/0.77=0.73. These probabilities are forecasts, not empirical autoresearch rates.

## 5. Verdict under the kill lines
Evidence estimate CUT; ANCHORED verdict CUT, UNCHANGED. Anchored bo4 exceeds 0.60 by ESTIMATED 0.10 and pass@4 exceeds 0.50 by about 0.50. The anchored mean falls sharply from the old 0.80 because integration failures are retained. Unlike a mere recurrence citation, actual autonomous optimizer/schedule search supports the remaining saturation concern. The decision still rests on the stated transfer, throughput and native-anchor assumptions; it does not claim a measured C009 solve.

## 6. Redesign
Cause (a): mature state handling plus demonstrated short-loop optimizer search. Required redesign: initialize from a correct local-clock implementation and cross earlier/returning task relationships while matching dormancy age and initial return-gradient norm. Supply earlier training evidence, valid retention examples and a bounded configuration policy that can condition on observable gradient/history summaries. Keep equal active FLOPs and include return trajectories where an initially helpful moment later damages another preserved skill.

The re-attack combines reset/decay sweeps, norm stabilization, cosine-gated momentum and autoresearch-style paired probes. It cannot infer longer-horizon usefulness from age or the first update alone. Basis LITERATURE-ONLY for this history-dependent extension; the demonstrated fast configuration loops do not show discovery of a transferable state-value statistic. A same-budget conditional reference must work before this is considered feasible research. A frontier lab would value optimizer memory that preserves transfer under conditional computation.

ESTIMATED redesign states {0.22,0.44,0.65}, masses {0.30,0.58,0.12}: single=0.30×0.22+0.58×0.44+0.12×0.65=0.40; bo4=0.65−0.21×0.88^4−0.22×0.30^4=0.52; pass@4=1−0.88^4=0.40; ub95=0.65. REDESIGNABLE, with ordinary gradient alignment still a serious shortcut. Pilot GPU-h ESTIMATED: 1B modular learner, five policies×two crossed histories×three seeds×eight H100-hours, plus thirty-six H100-hours for resumed-loss, retention and checkpoint checks: 5×2×3×8+36=276. This is a planned author pilot, not the agent's assumed trial budget.

## 7. Measurement status
Rollouts UNMEASURED (planned configuration-only search including its failed branches and cold resumes). Grader noise UNMEASURED (planned paired full-history learner seeds and resumed-loss trajectories). Score ladder UNMEASURED (planned global/local clocks, decay/reset portfolio, history-conditioned policy and independent stronger state control).

## Audit record
id: C009
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.80
old_bo4: 0.87
old_pass4: 0.98
old_ub95: 0.97
new_single: 0.73
new_single_range: 0.62-0.84
new_bo4: 0.80
new_pass4: 1.00
new_ub95: 0.83
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Begin after clock repair and learn history-dependent value of returning moments across coupled retained skills.
redesign_single: 0.40
redesign_bo4: 0.52
redesign_pass4: 0.40
redesign_ub95: 0.65
redesign_gpuh: 276
attack_basis: DEMONSTRATED-AGENT
demonstrated_ref: autoresearch, Claude unspecified version, 2026; NanoGPT, GPT-6.2 Astra internal optimization agent, 2026
gap_to_attack: Verify that short return probes rank full dormant-skill trajectories at adequate trial throughput
subfield_sota_ref: Momentum-reset LLM training through 1B, Huang SPAM, 2025; norm stabilization Huang GradientStabilizer, 2026
anchored_single: 0.59
anchored_bo4: 0.70
anchored_pass4: 1.00
anchored_ub95: 0.73
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
