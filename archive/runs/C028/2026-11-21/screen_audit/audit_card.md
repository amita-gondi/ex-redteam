# C028 — Adapt the scaffold's own compute governor — screen audit
## 1. What the screen claimed
The screen replaced gain-based patience with long-lived branches, restart portfolios and continuation forecasts, then tuned allocation on completed histories. Its ESTIMATED single/bo4/pass@4/ub95=0.76/0.83/0.95/0.96 supported saturation, but the recorded binding reason was CUT, category DUP, for overlap with catalog T03. Its cited URLs were:

- https://jmlr.org/papers/v18/16-558.html
- https://arxiv.org/abs/1406.3896

## 2. Evidence audit
Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization — Lisha Li, 2018, fetched — demonstrates resource diversification across configurations, without determining whether another research experiment will unlock new evidence. Freeze-Thaw Bayesian Optimization — Kevin Swersky, 2014, fetched — models training curves and resume decisions, rather than the changing semantics of a scientist's campaign. The attack's machinery is real; the claimed reliability on delayed scientific payoffs is not demonstrated by those sources.

Grade: PARTIAL. Search allocation and continuation are known capabilities, but integrating prerequisite-sensitive signals into a governor is the key extrapolation. Separate from performance, reading T03's controller contract confirms the same intervention and outcome: reusable experiment allocation over fresh live projects, including delayed reversals and complete cost accounting. That duplicate finding does not require a saturation forecast.

## 3. Research done now
- Supervising the Multi-Fidelity Race of Hyperparameter Configurations — Martin Wistuba, 2022 — https://arxiv.org/abs/2202.09774 — fetched — DyHPO learns continuation decisions from learning dynamics across architectures and modalities. It strengthens the curve-aware governor while leaving scientific action-dependent information acquisition outside the setup.
- Recursive self-improvement of AI research agents — Dhruv Srikanth, 2026 — https://arxiv.org/html/2609.26457v1 — fetched — Search-policy rewrites preserve multiple strategy arms and improve held-out research tasks. This is closer evidence for governor improvement, though its outer optimization lasts much longer than the target session.
- Session report: validation improvement through weight-decay and initialization experiments — agent posting for Andrej Karpathy, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — The recorded Claude loop persists through many discarded experiments within a working session. This raises a simple always-continue baseline; it is a self-report and offers no controlled comparison of governors.
- AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure — METR, 2026 — https://metr.org/blog/2026-11-20-q4-2026-capability-update/ — fetched — The update documents continuing weaknesses in extended optimization and feedback judgment alongside practical gains. It counters equating persistence with reliable recognition of delayed payoff.

## 4. Re-estimated attack
All reward values and distributions here are ESTIMATED. Removing premature termination plausibly contributes 0.33, diversified restarts add 0.20, and curve/experiment-aware continuation adds 0.13. Their 0.66 expected total assumes the stated starter defect accounts for substantial utility, not a measured decomposition.

Use ESTIMATED R∼U[0.53,0.79]. Many allocation choices contribute smooth variation; no particular hidden key is required to keep working. Forecast spread comes from dead-branch expenditure, stochastic experiment returns and choosing a reproducible final recipe. ESTIMATED single=0.66, range 0.53–0.79; bo4=0.53+0.26×4/5=0.74. Since p=(0.79−0.60)/0.26, ESTIMATED pass@4=1−(1−p)^4=0.99; ub95=0.53+0.95×0.26=0.78. These are independent-attempt calculations, not confidence bounds. The mean falls below the old forecast because delayed payoff requires more than persistence; the high repeated-search tail remains an assumption of this evidence-composition scenario.

## 4A. Demonstrated capability and subfield SOTA
For configuration continuation, DyHPO supplies a directly evaluated strong system baseline. For research-governor code, AIDE² is the closest contemporary SOTA located. Their objectives differ, so neither establishes a common absolute best or this card's normalized R≈1. The north star should be a live campaign controller exceeding both a persistent fixed allocation and contextual continuation on final training utility; that native ceiling has not been measured.

AIDE²'s Opus 4.7/Gemini 3 Flash loops accepted seven changes over eight days, including strategy allocation, with held-out transfer. Its financial accounting provides no matched H100-hour total. The autoresearch Claude report records 126 trials on an H100 in approximately 10.5 hours, improving validation bits/byte from 0.997900 to 0.969686. Neither a model revision nor a governor ablation is supplied there. These attributed demonstrations support persistence and allocation, without validating delayed-payoff recognition under the card's construction budget.

The KNOWN-RECIPE is resource diversification plus curve modeling. AGENT-DEMONSTRATED evidence does not establish a prerequisite-aware continuation policy at the full construction-inclusive budget. Thus attack_basis=LITERATURE-ONLY. In particular, an agent must distinguish an unpromising branch from an informative pending experiment rather than simply extend patience.

ANCHORED ESTIMATED outcomes R=0.42 and R=0.58 have probabilities 0.70 and 0.30, respectively. The lower outcome captures persistence and ordinary allocation; the upper credits useful learned continuation without assuming breakthrough recognition. ESTIMATED single=0.70×0.42+0.30×0.58=0.47, range 0.42–0.58; bo4=0.42×0.70^4+0.58×(1−0.70^4)=0.54; pass@4=0.00; ub95=0.58. This distribution is assumption-dependent; the duplicate verdict below is not.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT through ESTIMATED bo4 and pass@4. ANCHORED verdict: CUT, UNCHANGED, binding on duplicate rather than predicted saturation. T03 explicitly accepts research strategy switching, contextual multi-fidelity search, delayed-reversal histories and rollback under full costs. C028's self-edited configuration is a restricted representation of that same controller, with no new scientific outcome. Its numerical anchored margins cannot rescue a STRONG duplicate; the duplicate is established locally even though performance estimates rest on assumptions.

## 6. Redesign
DUPLICATE-STAYS-CUT. Cause (d): intervention/outcome duplication, not proof that all research continuation is solved. T03 already admits a governor that keeps uncertain branches alive and buys informative probes, so the obvious scientifically meaningful revision is already within its scope. A separate C028 task would require an independently justified research construct, which this audit has not identified. No redesign reward forecast or GPU allowance is assigned; duplicated controller variants belong in T03's comparison matrix.

## 7. Measurement status
Rollouts UNMEASURED (planned only within T03: live governors with cold campaign resets). Grader noise UNMEASURED (planned there: repeat selected training recipes independently). Score ladder UNMEASURED (planned comparison: patience cutoff, full persistence, restart portfolio and contextual continuation; no C028-specific rollout programme).

## Audit record
id: C028
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.76
old_bo4: 0.83
old_pass4: 0.95
old_ub95: 0.96
new_single: 0.66
new_single_range: 0.53-0.79
new_bo4: 0.74
new_pass4: 0.99
new_ub95: 0.78
new_verdict: CUT
binding_line: duplicate
flip: none
kill_cause_class: d
redesign_status: DUPLICATE-STAYS-CUT
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: AIDE2, Opus 4.7/Gemini 3 Flash, 2026; autoresearch, Claude unspecified, 2026
gap_to_attack: prerequisite-sensitive continuation validated in twelve hours
subfield_sota_ref: dynamic continuation DyHPO 2022; research strategy evolution AIDE2 2026
anchored_single: 0.47
anchored_bo4: 0.54
anchored_pass4: 0.00
anchored_ub95: 0.58
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
