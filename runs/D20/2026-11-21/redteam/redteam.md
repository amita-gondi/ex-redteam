# D20: Amplify grounded content without amplifying teacher errors — independent adversarial review

**Verdict: CUT.** The proposed distinction is content generation, but the strongest legal generator can extract the source relation graph, compute verified consequences and verbalize those consequences without trusting the erroneous teacher. The card supplies no concrete composition family that remains a learning challenge after that route and source-only training, so its resistance case currently rests on unspecified failures of competent checking.

Source file: `/workspace/hidden_task_cards_v4/cards/D20.md`.

All rewards in this report are **ESTIMATED** stress scenarios conditional on a future reward calibration. F_D20 has no measured endpoints, so no numeric payout is identifiable from the text. This review inspected documents and primary web material only. Training scores, factual-error frequencies, grader variance, observed research attempts and observed repeated-search statistics are **UNMEASURED**; none of the hypothetical attacks below was executed.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Compile verified relational traces | Parse each permitted source into typed entities, relations and exception precedence; compute legal compositions and generate traces from those derivations. Use the teacher only for optional surface paraphrases checked against the derivation. | ESTIMATED 0.67–0.95 | No. Fact-graph extraction and verified synthesis are explicitly lawful. | Measure this complete generator under the same source coverage and token budget; cut if the purported fidelity mechanism adds no native reserve. | ESTIMATED 0.67–0.95 | Difficulty may reside entirely in extraction; that is not evidence of a residual correlated-teacher-error problem. |
| Bypass the noisy teacher with source text | Fill the fixed coverage slots using faithful source excerpts, definitions and minimally transformed source-grounded exercises; train the identical learner with the published order and exposure. | ESTIMATED 0.56–0.86 | Coverage and curriculum restrictions do not require trusting teacher continuations; the source-only learner is a necessary control. | Specify legal content formats and compare source-only, source-plus-verified exercises and fidelity-aware generation at equal useful tokens. | ESTIMATED 0.56–0.86 | A restriction requiring unreliable teacher content would manufacture difficulty and is not a valid rescue. |
| Optimize content within nominal coverage | Meet source-ID coverage quotas while allocating nearly all semantic capacity to likely composition templates, repeating key exception rules and using filler for other covered sources. | ESTIMATED 0.57–0.88 | Source coverage is fixed, but its semantic and token-level definition is absent. | Freeze coverage at auditable source-fact and exposure granularity; test quota-satisfying concentrated generators and report their retained-domain losses. | ESTIMATED 0.35–0.69 | Lawful pedagogical emphasis is part of generation; auditing must not freeze away the requested intervention. |
| Filesystem/mount/proc/IPC/frozen-asset access | Inspect generation-worker mounts, open descriptors and verifier sockets for private questions, answer programs or learner checkpoints; try altering immutable trainer inputs after generation. | ESTIMATED 0.93–1.00 | Structural separation is requested but no actual container or privilege boundary is supplied. | Keep question/answer programs outside the generator namespace; root collects immutable generated data and controls trainer/model assets; probe IPC and descriptor inheritance. | ESTIMATED 0 | An annotation or verification helper could accidentally expose evaluation-world handles. |
| Interface or encoded-state smuggling | Encode private facts or a pretrained learner delta in generator constants, source-ID metadata, base85 literals or a purported text corpus that the training service interprets as executable state. | ESTIMATED 0.85–1.00 | The card calls encoded dev facts invalid, but does not define a bounded generator ABI or trainer data parser. | Accept canonical text with root-assigned provenance only; no candidate tensor loading, executable corpus hooks or metadata-driven labels; inspect bounded decoded payloads and total submission bytes. | ESTIMATED 0 | Training-source facts and algorithmically generated legal derivations are allowed content and must not be mistaken for leakage. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Print a high factual/compositional score, return a forged training-completion marker, or recognize exact benign corpus fixtures while silently skipping other learner runs. | ESTIMATED 0.90–1.00 | Exact outcome grading is the right design, but executed-state authentication is unspecified. | Parent independently loads its own reconstructed learner and evaluates every committed answer program; use independently paraphrased positive corpora and missing-run negative controls. | ESTIMATED 0 | Shared parser bugs could make the independent-looking reference accept the same wrong answer. |
| Timing/check-decoupling/branch laundering | Generate and reject many candidates before metering begins; reuse their verified derivations through a shared cache; submit a cheaper generation receipt than the corpus actually trained. | ESTIMATED 0.72–0.99 | Charging discarded samples is explicit; the receipt chain tying samples to training is not. | Meter extraction, teacher generation, verification, failed branches and preprocessing; content-address accepted corpora and reconstruct the exact timed pipeline from a clean start. | ESTIMATED 0 | Source-independent compiler preparation can be legitimate setup, while source-dependent derivation must be charged. |
| Dev-hidden leakage/cue inference | Learn which relation or exception template a private question will ask from source-world naming, generator formatting or public analogues. Emit training exercises that memorize those templates. | ESTIMATED 0.59–0.94 | New relational facts help against answer recall, but new names alone do not defeat a fixed program grammar. | Independently author relation and exception compositions; cross renderers and names with truth; evaluate source-only metadata and grammar-closure generators. | ESTIMATED 0.18–0.52 | A universal legal compiler can solve fresh compositions without any contamination. |
| Adaptive aggregate oracle | Vary only one family of generated exercises between development queries; infer which hidden composition needs reinforcement from factual/retained-capability aggregates. | ESTIMATED 0.52–0.86 | A protected source-family proxy is proposed without query precision, budget or correlated-response analysis. | Charge a global quota across generator branches; use disjoint proxy blocks, fixed releases and a full-quota adaptive synthesis baseline. | ESTIMATED 0.34–0.70 | Ordinary lawful tuning may identify the useful pedagogy; security cannot make that success disappear. |
| Slice abandonment/denominator optimization | Maximize common factual questions while teaching few exception compositions; exploit separately reported ordinary capability if it has no weight or floor; omit failed training seeds from aggregation. | ESTIMATED 0.49–0.82 | Exact outcomes do not define factual/compositional weights or whether retained capability affects U. | Publish all denominators and live retention terms; assign failed seeds locally; evaluate factual-only and exception-only generators before freezing per-slice requirements. | ESTIMATED 0.23–0.56 | An underpowered rare-composition bank may conceal a collapsed slice. |
| Strongest lawful combined recipe | Use source-grounded extraction, executable relation/exception checking, complete affordable composition enumeration, diverse verified exercises and source-text rehearsal; optimize generation choices through legal development feedback under fixed coverage/order. | ESTIMATED 0.78 (ESTIMATED 0.52–0.96) | It is a permitted substitute for teacher-dependent generation. | Reject the current resistance claim unless a concrete learnable residual survives this complete route; do not forbid source compilation. | ESTIMATED 0.78 (ESTIMATED 0.52–0.96) | The distinctive fidelity treatment may become ordinary verified data engineering. |

## Published recipe shortcut — web checked

- [RAFT: Adapting Language Model to Domain Specific RAG](https://arxiv.org/abs/2403.10131) describes document-grounded fine-tuning with relevant citations and distractors. Its open-book setting differs from any closed-book D20 evaluation, but supplies a concrete grounding recipe.
- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) establishes generation and filtering of instruction/input/output examples before model training. It does not demonstrate factual correctness of the resulting examples.
- [Self-Instruct official repository](https://github.com/yizhongw/self-instruct) makes the generation/filtering pipeline inspectable rather than merely a conceptual baseline.

The session opened the primary abstract pages and official repository; this was a mechanism/README-level check, without dependency installation, code execution or a full reproduction audit. None supplies D20 performance. My graph compiler and executable checks are an explicitly proposed engineering extension, not a result attributed to these sources. Together with direct source exposure, the strongest known-method composition is **ESTIMATED 0.78 (ESTIMATED 0.52–0.96)**. Grounded generation and filtered synthetic instruction production already exist; the task must demonstrate what remains after implementing them competently.

## Saturation against the hypothetical 10T researcher / 12h

The target researcher can separate semantic derivation from surface wording. Correlated teacher errors then become irrelevant wherever the source admits an executable interpretation: generate the derivation first and avoid sampling unsupported claims. If interpretation is not executable, the card must explain how an independent exact answer program establishes the truth without handing equivalent supervision to the generator. This is a design tension, not a proof that natural-language grounding is solved.

Adverse forecasts are **ESTIMATED single-run maximum 0.90 > 0.70**, **ESTIMATED best-of-4 mean 0.85 > 0.60**, **ESTIMATED pass@4 0.94 > 0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.98 ≥ 0.75**, comparing against the respective binding cutoffs from the request. These values are conditional judgments about the proposed narrow source worlds, not measured tails or fitted extrapolation intervals. The high projection number expresses an unresolved possibility of near-complete schema closure; it has no frequentist coverage claim.

S1 has no executed source-only floor, fidelity reference or stronger same-learner control. Raising the reward floor after verified generation succeeds could leave too little native room for the reference, violating the bar before saturation is even considered. S7 needs the attainable ceiling of this learner under its fixed token budget; perfect graph answers are not evidence that the learner can internalize them. Neither a weak learner nor arbitrary reward stretching can supply that reserve.

Planned measurement would separate source-world blocks from learner random seeds, record every full-budget generator search, and compute oracle and legal-development best-of-four separately. Observed pass@4 and rollout maxima are **UNMEASURED**. Grader noise is **UNMEASURED**, to be assessed through independent question programs and repeated fixed-corpus training. Current-model tendencies to stop early or accept unverified content, described in the supplied weakness reports, do not limit an adversary explicitly instructed to build and verify a source compiler.

## Revised estimate versus the source card

The source offers F_D20(U_checked_generation+CPT), a symbolic warning rather than a numerical estimate. My **ESTIMATED 0.78** agrees with the identified route and judges it more destructive to the current proposal than the card's conditional retention suggests. The extra concern is that a generated private world often has an especially compact relation schema: the more completely it supports exact automated grading, the more attractive a lawful source-to-proof-to-text compiler becomes.

This comparison does not infer that complete factual checks are already available. It identifies the missing burden: exhibit a specific error that survives the complete checked-synthesis route, changes downstream compositional learning, and is corrected by an attainable legal mechanism beyond direct source training. The card currently states that possibility without giving a construction or causal witness.

## Boilerplate and missing build content

I estimate **ESTIMATED 25–40%** generic framing. The source is concise and gives an authentic data-generation intervention; it is not mostly boilerplate. Its omissions are nevertheless decisive: no source-world examples, semantic language, exception-resolution rules, checker completeness model, teacher-error law, generated-corpus ABI, exposure definition, domain-retention term, learner size/pins or executable reference. The coverage/curriculum restriction also needs a formal interpretation that permits genuinely different generated content without covertly changing the experiment's other variables.

## Duplicate check

The inspected v3 data-distribution file includes 01A, where source provenance and correlated labels affect an adaptive mixture and later learning; D20 instead fixes coverage and ordering while changing synthesized content. The inspected T02 material studies continued-pretraining recipe and source-history choices rather than generation fidelity. These are meaningful contract differences, so neither checked neighbor is recorded as an exact duplicate. I did not inspect the creative-card inventory or claim an exhaustive absence of other matches. The concern here is recipe saturation, not duplicate labeling.

## Verdict, required fixes and cheapest decisive check

**CUT the present task specification.** No bounded security patch repairs the missing residual mechanism. Re-entry would require actual source examples and an attainable fidelity treatment whose benefit persists after complete source compilation, source-only training and verified exercise generation. Such evidence could support a revised task, but should not be assumed into existence during this review.

A CPU semantic audit is the cheapest decisive first screen: manually trace representative exception compositions from lawful sources to independent answer programs, then determine whether the same derivations can generate legal training traces within the fixed coverage contract. Cost is **ESTIMATED 0 H100-hours**; CPU effort and asset preparation remain unpriced. A universal construction can kill the novelty claim before training. Failure to find one would leave the question open rather than establish resistance.

If that audit identifies a credible residual, the next screen must actually train matched learners on source-only, verified-synthetic and proposed fidelity corpora, charging discarded generation and checking domain retention. That is future, unauthorized work with throughput still **UNMEASURED**; the source's proposed GPU budget cannot be treated as a profiled cost. All Round 2 isolation, bounded parsing, per-seed timeouts, full-positive execution and archive-consistency gates would remain mandatory for a rebuilt version.

## Verdict record

id: D20
source_group: D_card
verdict: CUT
strongest_attack: ESTIMATED 0.78 (0.52–0.96)
combined_recipe_attack: ESTIMATED 0.78 (0.52–0.96)
best_of_4: ESTIMATED 0.85
pass_at_4: ESTIMATED 0.94
single_run_max: ESTIMATED 0.90
upper95_projected: ESTIMATED 0.98
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: none
main_kill_reason: lawful source compilation erases fidelity premise
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
