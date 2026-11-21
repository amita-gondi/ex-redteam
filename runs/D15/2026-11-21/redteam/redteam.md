# D15: Acquire evaluator evidence adaptively before committing a verdict — independent adversarial review

**Verdict: CUT.** Adaptive queries are a meaningful intervention, but the disclosed residual is already the objective of cost-sensitive active classification and finite-belief test selection. The card supplies no concrete artifact semantics or resource frontier that separates its learned acquisition policy from a compiled decision tree, a sufficient fixed view or ordinary active feature acquisition.

Source file: `/workspace/hidden_task_cards_v4/cards/D15.md`.

The scope is an independent design review, without running a producer, evaluator or query policy. All numerical judgments below are ESTIMATED scenarios rather than calibrated rewards. Inspection costs, exact run truth and anchor endpoints have not been measured or delivered here. A dishonest payoff presupposes an implementation weakness and is not a claim that one was found in an existing service.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Read the cheapest sufficient artifact set | Trace each validity predicate to its checkpoint, dataset manifest or update receipt; solve the weighted cover and train a classifier on that fixed view; use full context if it fits the cap. | ESTIMATED 0.69–0.95 | No. Required full-context/fixed-set controls are mentioned, without evidence that they fail at real prices. | Build and time the best complete fixed cover, including summary extraction costs and legal cache reuse. | ESTIMATED 0.69–0.95 | A manifest and committed-state receipt may settle most cases regardless of transcript length. |
| Compile an adaptive belief-state query tree | Maintain hypotheses about run validity, choose the next query by expected elimination of opposite-verdict hypotheses per cost, and stop when remaining hypotheses agree. | ESTIMATED 0.70–0.96 | This uses the allowed adaptive interface and directly implements the proposed sufficiency logic. | Compare a complete finite-belief planner and its distilled learned policy against the reference. | ESTIMATED 0.70–0.96 | Earlier evidence changing later query value is the standard algorithm's purpose, not a barrier to it. |
| Learn dependency features and amortize query value | Fit artifact-feature conditionals on legal runs, estimate remaining verdict uncertainty under candidate views, and train a cost-aware stopping/query head with hard producer negatives. | ESTIMATED 0.62–0.90 | No. Immutable query schemas constrain syntax, not this lawful learner. | Include a jointly trained active-feature-acquisition system with independent producer optimization, rather than greedy entropy alone. | ESTIMATED 0.62–0.90 | New producer mechanisms can challenge the learned model, but the reference must transport across the same shift. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read unpurchased checkpoint/log views through broker descriptors, query-service mounts or cached temporary files; alter the fixed artifact parser to reveal exact validity truth. | ESTIMATED 0.92–1.00 | Root answering paid queries is a useful boundary, but no actual ACLs, handle lifecycle or immutable parser exists in the card. | Keep all unpurchased views outside worker namespaces, scope query RPCs by opaque IDs, freeze parsers and audit mount/proc/IPC inheritance. | ESTIMATED 0.00 | Cached derived summaries can become an unmetered alternate route to the same evidence. |
| Interface or encoded-state smuggling | Put private-verdict tables or prepared evaluator deltas into query parameters, checkpoint metadata or compressed acquisition-code literals; return arbitrary diagnostic text interpreted as executable policy state. | ESTIMATED 0.85–1.00 | Immutable output schemas do not define training-state provenance or parameter domains. | Parent reconstructs evaluator weights from legal data, accepts only offered query IDs and bounded typed responses, and caps every artifact channel. | ESTIMATED 0.00 | A compact legal decision tree can encode strong general rules and must remain admissible. |
| Spoofed verdict / skipped execution / benign-bank fingerprint | Print the outer grader's verdict, abort attacker queries so no wrong artifact is seen, or match a clean sibling checkpoint hash instead of checking run validity. | ESTIMATED 0.89–1.00 | The card rejects slow-evaluator exhaustion and SHA shortcuts, but has no executed health gate. | Outer parent owns exact truth and all offered cases; independently valid refactored artifacts must pass; dead or timed-out evaluators lose their cases. | ESTIMATED 0.00 | A healthy attacker must still produce genuine wrong artifacts after evaluator optimization; otherwise robustness is vacuous. |
| Timing / check-decoupling / branch laundering | Prefetch full artifacts before cost debits, inspect a benign checkpoint during checks and a swapped checkpoint at verdict time, or keep paid-query cache state across nominally fresh cases. | ESTIMATED 0.80–1.00 | Root query logs help, but immutable per-case snapshots and debit atomicity are unspecified. | Snapshot the actual run before querying, atomically debit before returning evidence and bind verdicts to the same run/view versions. | ESTIMATED 0.00 | Artifact mutation by a producer during evaluation can create time-of-check inconsistencies even without evaluator cheating. |
| Dev-hidden leakage / cue inference | Infer validity from producer identity, run-directory layout, missing-view error shapes or protected-only serialization; classify malformed-looking artifacts as wrong. | ESTIMATED 0.73–0.98 | Independent producers and adversarially presented correct cases are specified without concrete crossed controls. | Cross producer/layout with truth, keep all independent correct equivalents, equalize errors and measure metadata-only and source-recognition policies. | ESTIMATED 0.15–0.37 | Real valid/invalid artifact differences are legitimate evidence; removing all correlates can destroy identifiability. |
| Adaptive aggregate oracle | Optimize query orders and stopping thresholds by differencing producer/class aggregates; pool the feedback budget across evaluator branches or exploit separate classifier and policy quotas. | ESTIMATED 0.64–0.92 | Protected gold alone does not bound information revealed by aggregate utility. | Use a single global feedback ledger, bounded release alphabet and untouched producer bank; run the strongest legal full-quota selector. | ESTIMATED 0.27–0.55 | An inexpensive decision tree can be selected from rich aggregate scores without learning new evaluation science. |
| Slice abandonment / denominator optimization | Certify obvious successes, reject ambiguous failures, hang on adversarial correct artifacts or omit unfinished verdicts from class-conditioned accuracy. | ESTIMATED 0.52–0.86 | Fixed denominators and unfinished-verdict costs are explicitly intended. | Root commits all class/producer opportunities and deadlines; report balanced completion plus correct-verdict utility and test deliberate asymmetric policies. | ESTIMATED 0.19–0.46 | Fixed class balance does not ensure coverage of difficult causal mechanisms inside each class. |
| Strongest lawful combined recipe | Use canonical commitment checks and best fixed evidence cover, then a finite-belief/learned-conditional acquisition tree with cost-aware stopping, hard-negative training and full legal producer-robust selection. | ESTIMATED 0.80 (ESTIMATED 0.55–0.97) | Every component follows the intended paid-query interface. | Establish a native residual beyond complete static and adaptive systems before fitting a special reference. | ESTIMATED 0.80 (ESTIMATED 0.55–0.97) | The strongest baseline may subsume the proposed reference's entire sufficiency mechanism. |

## Published recipe shortcut — web checked

- [Near-Optimal Bayesian Active Learning with Noisy Observations](https://arxiv.org/abs/1010.3091): the primary abstract develops EC2 for expensive adaptive tests and nonuniform costs; equivalence-class determination directly matches stopping when verdict alternatives are resolved.
- [Active Feature Acquisition with Generative Surrogate Models](https://arxiv.org/abs/2010.02433): the primary result and conference text describe learning feature dependencies to assess the value of later acquisitions, matching the card's proposed earlier-evidence/later-sufficiency interaction.
- [Near-optimal Bayesian Active Learning with Correlated and Noisy Tests](https://arxiv.org/abs/1605.07334): primary search discovery establishes a correlated-test extension that a serious evaluator baseline must consider rather than assuming conditionally independent evidence.

I verified titles and mechanisms through primary search abstracts and publisher snippets, without reading full proofs or benchmarking code. Their assumptions, priors and test families may not match real ML artifacts, so no approximation theorem is asserted for D15. The combined recipe estimate is ESTIMATED 0.80, scenario range ESTIMATED 0.55–0.97. It is an inference about available controls, not a transferred result.

## Saturation against the hypothetical 10T researcher / 12h

The cited parent suite proposes a finite-hypothesis evidence algorithm and bounded sufficient-support paths. That is useful for exact grading, but also makes active query planning a direct algorithmic target. D15 does not commit that entire parent schema, so I do not silently import its constants; the narrower card still fails to explain what learned causal relationship remains beyond complete query planning and hard-negative classification.

A capable researcher can inspect public tool semantics, identify commitment witnesses and train an amortized decision tree from legally simulated runs. More checkpoints or longer logs do not force deeper reasoning when the same receipt proves committed state. New producers are meaningful only if their evidence relationships are learnable from the declared proxy; hidden-only query rules could make any method fail, including the author reference.

Single-run maximum is ESTIMATED 0.95 versus the binding 0.70 cutoff; oracle best-of-4 mean is ESTIMATED 0.89 versus 0.60; pass@4 is ESTIMATED 0.93 versus 0.50 at the binding reward threshold of 0.60; projected upper-95% is ESTIMATED 1.00 versus 0.75. These conditional scenarios suggest single, bo4, pass4 and upper95 breaches. They are not observed scores or an identified stronger-tier confidence interval.

S1 has no executable midrange reference and stronger same-information control establishing native reserve. S7 cannot be certified from the query cap or theoretical exact truth: the learnable constrained ceiling may be low because the necessary artifact is unaffordable. Such a cap would tighten ceiling-relative saturation. The supplied weakness reports' current-model verification errors motivate testing, but do not establish that a much stronger researcher cannot compile and validate a full evaluator.

Rollout scores: UNMEASURED; plan independent producer/mechanism blocks with correct and wrong artifacts. Grader noise: UNMEASURED; repeat full fitting and exact-query execution, separating training variability from deterministic truth reduction. Observed runs: UNMEASURED; record stalled attackers and unfinished evaluator cases rather than dropping them. pass@k observed: UNMEASURED; use independent researcher attempts, separate legal selection from retrospective oracle scores and charge every optimized-artifact query. Full resource/tier sweeps remain future mandatory gates if a new concrete residual survives.

## Revised estimate versus the source card

The source's strongest attack is `F_D15(U_fixed_sufficient)`, not a number. My ESTIMATED 0.80 extends that route with standard adaptive belief-state and learned feature acquisition for residual cases. This matters because defeating a fixed schedule would not establish resistance against a target allowed to derive an adaptive decision tree.

I agree that attacker health, protected gold and fixed denominators are necessary. They secure the scientific measurement but do not make the underlying inspection strategy difficult. The calibration FIX packets illustrate why a complete lawful recipe must retain its forecast after boundary hardening; I do not reuse their scenario points as D15 evidence.

## Boilerplate and missing build content

ESTIMATED 35–45% of the source restates shared safeguards, with ESTIMATED 55–65% describing active evaluation. It is not mostly boilerplate, but it is missing what an implementer needs to distinguish real active evaluation from a synthetic test-selection puzzle: the run-truth language, artifact queries, costs, natural dependency mechanisms, checkpoint/log fidelity, training observations, prior histories, policy model and actual budget. Reward endpoints and complete fixed-view controls are also absent. No implementation filename is provided for the broker or evaluator.

The parent suite's finite support design cannot establish production-scale ML relevance by itself. The build must show that expensive views involve authentic evaluation/inference work, rather than arbitrary prices on easy JSON fields. Immutable snapshots must prevent both producer mutation and evaluator prefetching. GDM requires root-owned truth, strict bounded parsers, independent equivalent positives, fail-closed skipped execution, real attacker health, portable OCI execution, query-scope isolation and exact per-case exports. There can be no LLM judgment of evidence persuasiveness in the outer reward. None of those future requirements is claimed measured here.

## Duplicate check

I checked v3 07B and catalog T15, as well as the cited Suite 9.2 parent. The v3 task classifies a trusted fixed rendering against optimized producers; T15 elicits missing decision requirements. D15 selects existing evidence adaptively, so the intervention is distinguishable. Suite 9.2 is its declared ancestry rather than a newly discovered duplicate. The independent objection is saturation by ordinary active test selection, not identity with an unchecked creative card.

## Verdict, required fixes and cheapest decisive check

CUT the present proposal. Re-entry requires a concrete ML-artifact family with naturally priced evidence, observable transferable dependencies and a native adaptive learning advantage after best fixed-cover, finite-belief and learned-surrogate acquisition controls. Merely requiring a neural policy does not create that advantage; legal planner distillation must remain available.

The cheapest decisive check is a CPU sufficient-evidence audit on the proposed query/validity specification. Derive whether a common cover fits the true cap, then solve bounded belief-state query planning on representative public semantics and compare its decisions to the reference's proposed information needs. Its accelerator requirement is ESTIMATED 0 H100-hours. This prices a specification/decision-structure screen, not classifier training or a live producer campaign. If real artifact access entails accelerator inference, that later cost must be profiled separately before authorizing a learner pilot. No query policy or rollout was run here.

## Verdict record

id: D15
source_group: D_card
verdict: CUT
strongest_attack: ESTIMATED 0.80 (ESTIMATED 0.55–0.97)
combined_recipe_attack: ESTIMATED 0.80 (ESTIMATED 0.55–0.97)
best_of_4: ESTIMATED 0.89
pass_at_4: ESTIMATED 0.93
single_run_max: ESTIMATED 0.95
upper95_projected: ESTIMATED 1.00
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: new natural evidence-cost witness; full fixed-cover and adaptive-planning controls; ML-relevant artifact semantics
main_kill_reason: standard active test selection subsumes the proposed residual
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
