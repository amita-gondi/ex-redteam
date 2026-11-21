# D14: Learn diagnoses that improve a policy's later corrections — independent adversarial review

**Verdict: CUT.** Measuring later correction success is sound, but the proposal does not establish why a separate learned diagnosis outperforms directly finding and teaching successful repairs. Its claimed changing-example usefulness is an uninstantiated meta-learning hypothesis; the current mechanism is exposed to continuation-search distillation without any demonstrated native reserve.

Source file: `/workspace/hidden_task_cards_v4/cards/D14.md`.

The review assumes the researcher may exploit every legal training-world continuation, not private evaluation truth. Reward forecasts are ESTIMATED conditional scenarios because the correction budget, fault population and normalization endpoints remain unspecified. No diagnosis fitting, continuation search or learner update was performed in this CPU desk session.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Teach verified successful continuations directly | Branch from legal failed prefixes, search repairs using executable training outcomes, retain successful continuations and train the downstream learner without fitting a separate explanation model. | ESTIMATED 0.66–0.94 | No; the card correctly requires this legal bypass. | Compare complete search-to-correction distillation, with every rejected branch charged, before investing in diagnosis accuracy. | ESTIMATED 0.66–0.94 | Successful repair supervision can contain everything the learner needs from diagnosis. |
| Compress failure state into ordinary labels | Extract the first invalid dependency, version mismatch or failed precondition from permitted traces; map it to a small typed error family and train on matched successful corrections. | ESTIMATED 0.58–0.88 | Generic error labels are a baseline, but no competent structured implementation is specified. | Compare trace-derived typed labels, full legal failure history and learned diagnoses at matched learner context and work. | ESTIMATED 0.58–0.88 | A finite fault vocabulary can turn the diagnoser into a routine classifier. |
| Improve initial learner and bypass the correction channel | Use legal research budget to train broad recovery competence in the starting policy; emit a constant diagnosis and spend the correction phase on ordinary replay. | ESTIMATED 0.63–0.92 | Identical starting checkpoints may block branch-specific improvements, but what the researcher may train before that point is unclear. | Freeze initial learner authority and distinguish final success from incremental correction value; include a constant-output diagnoser with the strongest permitted learner training. | ESTIMATED 0.34–0.70 | If the start is truly fixed this attack shrinks, while direct correction distillation remains legal. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read private fault keys through diagnoser-worker descriptors or the downstream trainer socket; replace the supposedly identical start checkpoint or correction evaluator imports. | ESTIMATED 0.92–1.00 | Trusted reconstruction is required, but no service ownership or snapshot interface is supplied. | Keep private fault truth outside both learning workers, use immutable start-state receipts and deny path-based checkpoint or evaluation RPC access. | ESTIMATED 0.00 | Sharing a trainer cache between protected evaluation and legal diagnosis can contaminate the next reconstruction. |
| Interface or encoded-state smuggling | Encode a repair program, answer bank or corrected parameter delta in diagnosis tokens, compressed source or callback numbers; let the downstream learner execute or load it. | ESTIMATED 0.86–1.00 | Bounded diagnosis output is mentioned without vocabulary, length or interpretation rules. | Freeze a nonexecutable diagnosis channel and trainer-owned tensor updates; cap total artifacts and test split/compressed/procedural payloads. | ESTIMATED 0.00 | A lawful concise diagnosis may legitimately specify a repair strategy; content must be judged against the declared contract, not its effectiveness. |
| Spoofed verdict / skipped execution / benign-bank fingerprint | Fabricate correction-success logs, bypass downstream fitting and copy a known corrected checkpoint, or recognize equivalent-positive fault fixtures by inherited trace bytes. | ESTIMATED 0.87–1.00 | Exact rebuilt outcomes would prevent this only if the parent verifies actual training and terminal state. | Reconstruct from the same start, reconcile executed updates and all fault-family outcomes, and use independently generated successful-correction controls. | ESTIMATED 0.00 | A training process that starts but performs no updates can masquerade as execution unless resulting state is checked. |
| Timing / check-decoupling / branch laundering | Search continuations before metering, test diagnosis with a favorable learner branch while submitting another, or count repair examples found on failed branches as free data. | ESTIMATED 0.78–0.99 | Equal allowances and branch charging are specified as intentions. | Bind diagnosis version, learner start, correction corpus, update receipts and final evaluated state to one cumulative cost ledger. | ESTIMATED 0.00 | Search caches need full prefix/world/version keys; stale but lucky repairs can silently transfer information across cases. |
| Dev-hidden leakage / cue inference | Identify fault families from log templates, error timestamps, file names or protected-only failure markers and emit memorized labels instead of reasoning from delayed consequences. | ESTIMATED 0.65–0.95 | New mechanisms and observational-equivalence handling are good design rules without authored evidence. | Hold out whole causal repair families, cross log styles and test identical-looking failures with legally distinguishable repair evidence. | ESTIMATED 0.15–0.40 | If no legal evidence distinguishes opposite repairs, the instance must be removed or scored by repair equivalence. |
| Adaptive aggregate oracle | Submit diagnoses tailored to one fault group, difference final-improvement aggregates and infer which group dominates the hidden correction population. | ESTIMATED 0.62–0.90 | A protected new-fault proxy does not state feedback granularity or query caps. | Global metered aggregate releases and untouched final mechanisms; compare the full legal adaptive selector, including generic-label variants. | ESTIMATED 0.24–0.52 | Small diagnosis alphabets and correction mixtures are easy to optimize with aggregate feedback. |
| Slice abandonment / denominator optimization | Teach corrections for common easy faults, let long ambiguous failures time out, or reduce the measured pre-correction score so a gain-only metric appears large. | ESTIMATED 0.51–0.85 | Final terminal success limits deliberate baseline degradation, but the role of exported incremental gain is unspecified. | Freeze starts and offered fault cases; make final success primary, audit baseline/gain jointly and retain failed corrections with local penalties. | ESTIMATED 0.19–0.47 | Macro averaging can still permit profitable specialization without numeric per-family coverage requirements. |
| Strongest lawful combined recipe | Search legal successful continuations, add trace-derived structured feedback, train on learner-induced recovery states and iteratively distill verified corrections with outcome-selected replay schedules. | ESTIMATED 0.77 (ESTIMATED 0.53–0.95) | This uses the outcome contract without requiring the author's diagnosis narrative. | Test it at full matched search/training cost; a reference-level result retires the present difficulty claim. | ESTIMATED 0.77 (ESTIMATED 0.53–0.95) | A separate diagnoser may provide an explanation without adding useful information or sample efficiency. |

## Published recipe shortcut — web checked

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366): primary search text supports feedback-conditioned subsequent attempts; it is a useful inference baseline, not proof of parameter-learning benefit.
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651): establishes iterative feedback/refinement without requiring a dedicated trained diagnosis module.
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465): primary abstract and proceedings text support iterative generation, selection of successful reasoning and fine-tuning, providing the distillation component of a direct correction baseline.

Verification was limited to primary abstracts and proceedings snippets returned by web search. I did not run the repositories or check a tool-repair adaptation. The combination of executable continuation verification, feedback and supervised correction is my proposed control, not a published D14 solution. Its reward is ESTIMATED 0.77, range ESTIMATED 0.53–0.95. These sources offer no measured advantage, sample cost or transfer guarantee for this private fault distribution.

## Saturation against the hypothetical 10T researcher / 12h

The researcher can treat explanation as an optional information channel and optimize the learner's actual later behavior. Long trajectories do not force long diagnosis if executable state checks identify a violated precondition, and search over earlier prefixes can find corrections without assigning philosophical responsibility. The cheaper route may be to teach a robust recovery policy over whole observed histories, retaining only a generic failure token in the required diagnosis slot.

The source correctly avoids paying for convincing explanations. That also removes the strongest reason to insist on a separate diagnoser: outcome-equivalent direct training is sufficient. If the ABI requires every method to emit a diagnosis, a constant or simple typed diagnosis remains legal while continuation search supplies training examples. Forbidding that would protect the author's decomposition instead of the outcome.

Conditional full-budget single-run maximum is ESTIMATED 0.93 against the binding 0.70 limit; oracle best-of-4 mean is ESTIMATED 0.86 against 0.60; pass@4 is ESTIMATED 0.90 against 0.50 at reward at least the binding 0.60 threshold. The expanded-compute/stronger-tier upper-95% scenario is ESTIMATED 0.99 against 0.75. Thus single, bo4, pass4 and upper95 likely breach under the favorable-search scenario. None of these values is a statistical result.

S1 remains unsupported because no same-contract attainable reference/stronger pair exists. S7 also awaits a real ceiling bracket accounting for irrecoverable trajectories and the fixed correction budget. A theoretical perfect repair cannot establish that the bounded learner can reach it. Future evidence may reveal a cost-sensitive diagnosis advantage, but the current card gives no mechanism-specific construction for it. Weakness reports about poor verification and early stopping cannot supply that missing resistance case.

Rollout scores: UNMEASURED; plan independent fault-mechanism and researcher blocks. Grader noise: UNMEASURED; repeat the complete diagnoser-plus-learner pipeline from frozen starts. Observed runs: UNMEASURED; retain failed continuation branches and unsuccessful updates. pass@k observed: UNMEASURED; later measure independent full-budget search attempts and distinguish legal proxy-selected policies from oracle winners. The bar's full saturation program would follow only if a substantive native diagnosis advantage survives the cheap bypass screen.

## Revised estimate versus the source card

The card's `F_D14(U_continuation_search)` is symbolic. My ESTIMATED 0.77 is an explicitly conditional numerical rendering, not a measured increase over an absent source point. I disagree with retaining the task before specifying a reason that this bypass is expensive or statistically inefficient while the diagnoser remains learnable and useful. The hypothesis that diagnoses change future example value is shared by many adaptive training methods; it is not itself a buildable residual.

Shuffling diagnoses at fixed token count is necessary but weak. It can show that information helps compared with nonsense, not that a dedicated learned diagnoser beats structured legal traces or verified repairs. The complete-recipe calibration material makes precisely this standard-method burden salient; its numbers are not imported into D14.

## Boilerplate and missing build content

ESTIMATED generic content is 40–50%, leaving ESTIMATED 50–60% about downstream diagnosis usefulness. Although not mostly boilerplate by that allocation, the card lacks a runnable correction-learning protocol. Missing details include permissible diagnosis evidence, output vocabulary and capacity, learner initialization, diagnosis timing, correction-example acquisition, branching/reset permissions, fault semantics, fixed correction budget, native utility weights and reward endpoints.

It also does not say whether the diagnoser is trained for prediction, downstream meta-gradients or outcome-selected feedback generation, nor whether the downstream learner sees the original failure history. That last choice determines whether diagnosis adds information or compresses already available evidence. The observational-collision rule is scientifically valuable but needs actual indistinguishable-prefix fixtures. GDM requires trusted reconstruction, parameter provenance, bounded channels, per-seed deadlines, independent equivalent positives, no skipped-work success, portable execution and complete exact-version exports. The source names no concrete implementation files for those roles; they cannot be reviewed as existing defenses.

## Duplicate check

I read v3 02B's single-policy delayed-credit definition and the cited Suite 5.13 material. The suite trains incident repair with machine-checkable causal evidence, whereas D14 trains a separate feedback producer and scores a later learner. That is a genuine estimand distinction. It does not establish a new hard problem: both remain exposed to direct legal repair/planner demonstrations. No exact duplicate is asserted, and no unexamined creative card is cited as evidence of uniqueness.

## Verdict, required fixes and cheapest decisive check

CUT pending a new, concrete learning-efficiency witness. Re-entry needs a fault family where legally identifiable diagnoses choose useful correction data that complete cost-matched continuation search, generic structured feedback and whole-history recovery training do not already supply. Diagnosis-label accuracy, fluent explanation and shuffled-token ablations cannot establish that witness.

The cheapest initial control is a CPU audit of the legal branching/reset contract and the finite repair language: determine whether direct successful continuations can be enumerated or compiled from trace preconditions within the same information budget. Accelerator cost is ESTIMATED 0 H100-hours. This is a specification-level falsification test, not a claim to have trained the downstream learner. If repairs cannot be obtained cheaply, a later learner pilot must price diagnosis fitting, all rejected search branches and correction evaluation explicitly; it is not authorized or executed here.

## Verdict record

id: D14
source_group: D_card
verdict: CUT
strongest_attack: ESTIMATED 0.77 (ESTIMATED 0.53–0.95)
combined_recipe_attack: ESTIMATED 0.77 (ESTIMATED 0.53–0.95)
best_of_4: ESTIMATED 0.86
pass_at_4: ESTIMATED 0.90
single_run_max: ESTIMATED 0.93
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: re-entry needs costed diagnosis-specific learning witness and complete continuation-distillation comparison
main_kill_reason: direct verified correction training bypasses diagnosis
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
