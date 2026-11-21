# C087: Prior-support diagnostics that unlock genuinely new RL behavior — independent adversarial review

**Verdict: CUT.** The required distinction between sharpening and genuinely new capability is not identified by finitely sampled initial successes. A curriculum can earn high mechanism coverage by amplifying rare prior behavior, while the proposed evaluator labels that behavior new. Replacing the scientific claim with coverage under a fixed sampling budget would be defensible, but would constitute a different estimand and leave a strong ordinary curriculum baseline.

Source file: `/workspace/task_ideation_v4_creative/cards/C087.md`.

Only desk analysis was performed. Rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; a planned coverage study would require a frozen base checkpoint, decoder, mechanism ontology, training ledger and independent executable variants. Reward entries are ESTIMATED stress scenarios. The source names no grader files or actual mechanism interpreter, so proposed test identifiers below are not claims of existing implementation.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Manufacture apparent novelty through rare support | Select mechanisms with no sampled base success but accessible rare trajectories; use broader prompts/resampling to find successes, then reinforce them and claim discovery. | ESTIMATED 0.71–0.95 | The card recognizes finite-sampling error but offers no identifying condition. | Replace zero-support claims with preregistered bounded-probability statements or provide a genuinely restricted support model. | ESTIMATED 0.60–0.89 | A confidence bound on rare mass still cannot prove absence of an arbitrary behavior. |
| Solve the composition grammar directly | Infer executable primitives from legal training tasks; synthesize precursor demonstrations or curricula and train coverage without using the submitted diagnostic's support judgment. | ESTIMATED 0.63–0.91 | Exact coverage rewards this lawful route regardless of diagnostic theory. | Include generator-closure, planner-demonstration and no-diagnosis curriculum controls where permitted; compare native new-family success. | ESTIMATED 0.63–0.91 | A universal training grammar may make fresh combinations routine rather than new research. |
| Inflate mechanism labels | Split one effective solver into syntactically different mechanism ids, choose easy combinations, or rename equivalent tool trajectories to increase covered-family counts. | ESTIMATED 0.74–1.00 | Semantic IDs are meant to be separated from visible labels, without an equivalence relation. | Parent fixes mechanism ontology and executable obligations; count semantic classes independently of candidate names and trace paraphrases. | ESTIMATED 0.00–0.30 | Different successful algorithms can solve the same task, making mechanism identity scientifically contestable. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read private mechanism assignments, initial support probe receipts or verifier tests through rollout-worker handles; mutate the frozen base to make before-training success look worse. | ESTIMATED 0.90–1.00 | No reset/probe/evaluator namespace design is supplied. | Root owns base and pre/post probes, private tests stay outside solver mounts, and proposed `test_prior_probe_isolation` checks descriptors, shared memory and base writes. | ESTIMATED 0.00 | Sharing inference workers between before and after phases can leak states or alter the base distribution. |
| Interface or encoded-state smuggling | Store hidden demonstration traces in evaluator fixtures or integer mechanism metadata; use an exploration callback to inject fitted weights or relabeled outcomes into RL. | ESTIMATED 0.82–1.00 | Eval/harness authority versus learner authority is not defined. | Typed diagnostic output cannot replace rewards, labels or parameters; authenticate legal demonstrations and bound every auxiliary channel. | ESTIMATED 0.00 | Compact legal program synthesis can teach the same behavior and must remain eligible. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Report a mechanism as solved without tool execution, skip hard post-RL trials, or recognize baseline-positive fixtures from hashes and emit expected success records. | ESTIMATED 0.85–1.00 | Exact execution is intended, but receipt ownership and positive banks are unspecified. | Independent parent launches every indexed trial; healthy semantic equivalents must all pass; fake evaluator JSON and worker aborts cannot count as coverage. | ESTIMATED 0.00 | An executable outcome test may verify task success without verifying the claimed internal mechanism. |
| Timing/check-decoupling/branch laundering | Underbudget initial probes, overspend exploration outside the ledger, carry solved trajectories across reset or compare a weak initial decoder with a stronger final one. | ESTIMATED 0.73–0.98 | Diagnostic costs are explicitly charged in intent; matched before/after semantics are absent. | Freeze decoder/support-probe budgets; ledger all sampling/training ancestry; cold reset and grade the exact selected policy. | ESTIMATED 0.00 | Legitimate prompt changes alter operational support and must be part of the stated estimand. |
| Dev-hidden leakage/cue inference | Recognize executable family templates, infer hidden mechanism IDs from tool ordering or reuse public reasoning tasks with known solutions. | ESTIMATED 0.59–0.90 | Fresh combinations alone do not exclude shared generator closure or source overlap. | Hold out independently authored semantic mechanisms, cross surface aliases, and compare metadata-only and training-grammar solvers. | ESTIMATED 0.25–0.58 | Generalization over disclosed primitives is legal and can erase the claimed novelty barrier. |
| Adaptive aggregate oracle | Query coverage changes for one curriculum component at a time; infer hidden missing mechanisms through aggregate differences and coordinate evaluator branches. | ESTIMATED 0.60–0.87 | Matching dev probe budgets does not constrain adaptation or returned precision. | Global query accounting, protected fresh blocks and full-cap adaptive curriculum selection measured on untouched mechanisms. | ESTIMATED 0.34–0.66 | Legitimate exploration targeting may recover the entire useful curriculum from coarse feedback. |
| Slice abandonment/denominator optimization | Ignore low-support mechanisms, omit them from the discovered-mechanism set and report a high fraction over only families with initial or final successes. | ESTIMATED 0.66–0.94 | No offered-family denominator or empty-family convention appears. | Commit all semantic family slots before probing; retain never-solved cases and macro report precursor, composition and transfer outcomes. | ESTIMATED 0.20–0.54 | Fixed coverage weights still may favor cheaply learnable compositions over meaningful missing behavior. |
| Strongest lawful combined recipe | Audit operational support with diverse legal prompts, collect executable successes, train a precursor curriculum with entropy control and verified self-generated demonstrations, then adapt using protected coverage feedback. | ESTIMATED 0.79 (ESTIMATED 0.52–0.95) | This can satisfy coverage while bypassing the evaluator's novelty interpretation. | Test against matched-compute resampling and curriculum baselines; scientifically rename the outcome if true prior absence is not identifiable. | ESTIMATED 0.79 (ESTIMATED 0.52–0.95) | Security fixes cannot establish that an amplified rare behavior was genuinely absent before RL. |

## Published recipe shortcut — web checked

- [Demystifying Reinforcement Learning Post-Training of Language Models](https://arxiv.org/abs/2608.24949): the cited primary page was opened to verify the proposal's theoretical source; detailed proofs and any assumptions needed for a support theorem were not audited.
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837): primary search material frames the distinction between improved sampling and expanded reasoning capability, supporting the need for stronger controls rather than proving either outcome here.
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465): the primary abstract describes iterative generation, verification/conditioning and fine-tuning, giving a standard self-generated-success training route.
- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560): the primary abstract establishes synthetic instruction generation as an existing source of training diversification.

Verification stopped at primary pages and search-returned abstracts. No paper's benchmark score or theorem is assumed to apply to these executable families. Demonstration generation is included only using legal training truths and tool outcomes; unavailable private correct answers are not smuggled in under STaR's name. The complete lawful recipe's forecast is **ESTIMATED 0.79 (ESTIMATED 0.52–0.95)**.

The decisive objection needs no empirical citation. For a finite initial sampling budget n and an existing success probability p, observing no success has probability `(1−p)^n`. This is compatible with both absent success and arbitrarily small positive success probability. A finite trace record cannot identify which world generated it without additional structural assumptions. A softmax policy may assign positive mass to every permitted finite token sequence, making literal support expansion a particularly unsuitable claim unless “support” is explicitly operationalized.

## Saturation against the hypothetical 10T researcher / 12h

The researcher need not resolve the philosophical novelty question to win a coverage reward. It can use broad search, external scientific reasoning over legal tasks, curriculum construction and ordinary reinforcement to move useful behaviors into a readily sampled regime. If the subject cannot initially produce a complete composition, successful precursor learning can still be found by standard curriculum search. None of this is forbidden by the card.

Forecasts for the proposed operational coverage score are **ESTIMATED single-run maximum 0.92 against >0.70**, **ESTIMATED oracle best-of-4 mean 0.87 against >0.60**, **ESTIMATED pass@4 0.94 against >0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.99 against ≥0.75**. They indicate likely saturation on every listed absolute line, not measured breaches. The record uses these conditional values because a quantitative output is required; no hidden attempt distribution is inferred from the desk argument.

S1 cannot pass while “new mechanism” lacks a fixed estimand and an attainable stronger same-contract reference. S7 has no valid achievable ceiling bracket. Neither is marked a measured failure: both are OPEN, with ontology/identifiability review preceding any native frontier study. If the reward is changed to operational coverage, all anchors and saturation studies must be rebuilt for that version.

Actual before/after support estimates, sampling covariance, evaluator noise and repeated-attempt outcomes are UNMEASURED. Planned measurements would hold base decoder and sampling budgets fixed, use independently authored family blocks, distinguish subject-policy pass@k from outer-researcher pass@k, and report lawful dev-selected as well as oracle winners. Increasing the base sample count can tighten an upper mass bound; it cannot turn it into proof of zero support. The target researcher's stronger persistence cannot cure an unidentified outcome.

## Revised estimate versus the source card

The source's **ESTIMATED 0.44** already concedes that finite sampling mistakes rare existing behavior for discovery. My **ESTIMATED 0.79 (ESTIMATED 0.52–0.95)** treats that as a core measurement failure rather than a small residual risk. Extensive support sampling plus a conventional curriculum may obtain excellent operational coverage while the novelty claim remains false.

The higher estimate also admits a route the source underweights: a very capable researcher can synthesize legal examples or precursor curricula directly from executable semantics. The subject model's initial sampled mistakes do not bound the researcher's knowledge. No benefit from model weakness reports' early stopping or poor verification is assumed. Ordinary verified self-training is strengthened until it is a credible adversary, rather than constrained to preserve the designer's proposed story.

## Boilerplate and missing build content

**ESTIMATED 30–40%** of the card is general evaluation/training framing; **ESTIMATED 60–70%** concerns prior support and semantic coverage. It is not mostly boilerplate, but crucial mathematical definitions are missing. “Mechanism,” “initial support,” “new capability,” and the equivalence relation among solving strategies require distinct operational meanings before implementation.

Further missing are base model/decoder pins, tool environments, lawful demonstration policy, true mechanism ontology, initial probe sampling plan, cost of repeated diagnostics, exploration objective interface, exact family weights and coverage reward anchors. A held-out combination is not necessarily a new mechanism, and an executable final success predicate cannot by itself inspect an internal reasoning strategy. If private IDs define novelty while visible tasks do not identify them, the evaluator may reward author labeling rather than research. These gaps are more serious than packaging incompleteness.

## Duplicate check

I checked the T06 FIX packet's support/reliability discussion and known-method controls. It also separates subject repeated-success metrics from researcher search, but its endpoint is reliability with retained support rather than proof of discovery. C087 overlaps the support-audit machinery and makes a stronger unidentified claim; it is not established as a duplicate. Checked D18 concerns support construction and likewise does not identify literal prior novelty. No broader catalog comparison is claimed.

## Verdict, required fixes and cheapest decisive check

**CUT** the current scientific outcome. A replacement may grade fixed-budget operational coverage gain with explicit uncertainty and admit curriculum/demonstration baselines. It must not call that gain proof of a previously absent behavior. Alternatively, an unusually restricted subject hypothesis class might make support analytically decidable, but that would require a new realism and research-difficulty case.

The cheapest decisive check is the CPU indistinguishability argument above plus a contract audit of whether the proposed mechanism predicate is observable. Cost **ESTIMATED 0 H100-hours**. No amount of GPU sampling is needed to establish that the current finite-sampling procedure lacks the claimed identification. A larger sampling pilot could characterize practical rarity, but cannot settle the stronger statement and should not be advertised as its decisive test.

R2 security must still be implemented for any replacement: protected initial/final probes, immutable base state, provenance-limited diagnostic interfaces, bounded encoded payloads, independent executed positives and a trusted fixed-denominator ledger. It needs live adversarial tests for fabricated success, baseline degradation, skipped hard mechanisms and leaked IDs, plus portable offline execution and complete archive reconciliation. These controls would improve measurement integrity without resolving the scientific identifiability defect.

## Verdict record
id: C087
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.79 (0.52–0.95)
combined_recipe_attack: ESTIMATED 0.79 (0.52–0.95)
best_of_4: ESTIMATED 0.87
pass_at_4: ESTIMATED 0.94
single_run_max: ESTIMATED 0.92
upper95_projected: ESTIMATED 0.99
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: replace unidentified novelty claim; operational support contract; complete curriculum and self-training floor
main_kill_reason: finite samples do not identify genuine prior absence
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 4
