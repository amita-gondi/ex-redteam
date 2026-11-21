# C042: Pretrain conditional computation with delayed expert utility — independent adversarial review

**Verdict: FIX.** Delayed complementary specialization is a plausible learning problem if early evidence lets a policy preserve useful precursors within a genuinely binding budget. The current card does not show that this survives modern balancing, router exploration and rehearsal; it also leaves expert identity and the alleged need for complementary experts unverified.

Source file: `/workspace/task_ideation_v4_creative/cards/C042.md`.

The proposed conditional model, routing monitor and composition grader have no named implementation files. Their presence is not assumed. All reward forecasts are ESTIMATED scenarios, not measured conditional-model results; no learning run or hardware profiling was performed.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Remove balancing-gradient interference | Use expert-wise routing bias control instead of a large uniform load penalty; tune exploration, warmup, capacity and moments jointly on rare precursor tasks. | ESTIMATED 0.64–0.86 | No: the stated plateau specifically concerns uniform load penalties. | Competent loss-free balancing plus same-budget rehearsal floor; compare outcome, not load uniformity. | ESTIMATED 0.61–0.84 | The supposed delayed-utility effect may be an ordinary balancing-loss artifact. |
| Replicate useful features across legal experts | Encourage distributed precursor representations with varied routing and replay, so later compositions do not depend on one fragile specialist identity. | ESTIMATED 0.62–0.85 | The card assumes complementary experts without proving unavoidable specialization. | Permutation-invariant expert ablations and legal redundancy/representation-sharing controls at identical total/active capacity. | ESTIMATED 0.56–0.81 | A generic representation can dissolve the author's preferred expert decomposition. |
| Relearn precursors when joint utility arrives | Reserve legal training work, retain diverse old tasks, then jointly replay precursor and composition examples after the later phase is observed. | ESTIMATED 0.59–0.83 | No chronology, revisit limit or irreversibility law is specified. | Late-relearning and static full-support curricula with full exposure accounting; show why early preservation adds native value. | ESTIMATED 0.52–0.80 | Making early information unavailable can create impossibility instead of useful learning depth. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read private composition programs and future phase queues from trainer descriptors or shared memory; patch the initial conditional checkpoint or expert-work counter. | ESTIMATED 0.95–1.00 | Actual active work must be measured, but protected assets and counters are not assigned authority. | Root-only future-composition service, immutable initialization, independent work instrumentation and no solver-visible private handles. | ESTIMATED 0.00 | The task-generation service may reveal future interaction labels through diagnostics. |
| Interface or encoded-state smuggling | Hide reserve expert weights in optimizer tensors, recipe constants, host files or router metadata and restore them when a composition arrives. | ESTIMATED 0.88–1.00 | Stored expert state is charged in principle; auxiliary persistent state is undefined. | Reconstructed-byte ledger across weights, moments, code and caches; trainer-owned updates and aggregate decoded-payload limits. | ESTIMATED 0.00 | Legal optimizer state also preserves information and must be budgeted consistently. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Print balanced loads and low loss without expert execution, skip difficult compositions, or recognize positive routing fixtures by checkpoint hashes. | ESTIMATED 1.00 | Diagnostic routing logs are not the reward, which helps; result authentication is absent. | Parent computes loss from executed logits and full token IDs; test fake logs, absent dispatch and independently implemented equivalent positives. | ESTIMATED 0.00 | A trusted evaluator importing the candidate's routing logger would reopen the channel. |
| Timing/check-decoupling/branch laundering | Run dense all-expert work on a hidden branch, report sparse counters from another pass, or submit weights trained before the metered phase. | ESTIMATED 0.91–1.00 | The actual-work requirement targets this route but supplies no capture protocol. | Bind dispatch traces, optimizer ancestry and evaluated checkpoint; charge every branch and kill orphan workers at freeze. | ESTIMATED 0.00 | Activation recomputation and fused routing can conceal work from superficial counters. |
| Dev-hidden leakage/cue inference | Read task IDs, phase order or text templates to infer the future expert pairing; allocate capacity from these cues rather than learned transferable features. | ESTIMATED 0.72–0.97 | Matching task depth alone does not match interaction or nuisance structure. | Cross templates, expert permutations and composition semantics; provenance-family holdout and task-ID-only policy. | ESTIMATED 0.20–0.49 | A lawful rule parser may learn all composition structure cheaply. |
| Adaptive aggregate oracle | Sweep bias strengths, reset schedules and precursor replay allocations; difference held-out loss to identify the private interaction matrix. | ESTIMATED 0.65–0.90 | No scoring quota or response precision is described. | Root-global protected-dev accounting; fresh final interactions and an adaptive full-budget routing search baseline. | ESTIMATED 0.43–0.73 | A small expert-interaction space can be searched without new representation insight. |
| Slice abandonment/denominator optimization | Fit common shallow compositions, drop tokens or route rare branches to cheap defaults, and report loss only on surviving dispatches. | ESTIMATED 0.63–0.93 | The card specifies held-out loss without per-composition denominator rules. | Parent-fixed token counts, full likelihood on every item, numeric precursor/composition strata and deliberately specialized controls. | ESTIMATED 0.28–0.59 | Aggregate NLL can still underweight rare tasks that supposedly justify the mechanism. |
| Strongest lawful combined recipe | Jointly search loss-free balancing, causal router exploration, capacity/moment schedules, diverse precursor replay and later joint rehearsal; allow distributed legal representations within the fixed model. | ESTIMATED 0.66 (ESTIMATED 0.43–0.87) | No scientific rule rules out this standard training-policy family. | Compare the full stack to an executable delayed-utility reference on identifiable interaction shifts. | ESTIMATED 0.66 (ESTIMATED 0.43–0.87) | Scientific reserve, not security hardening, must defeat this recipe. |

## Published recipe shortcut — web checked

- [Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664) explicitly addresses harmful balancing gradients with expert-wise routing biases. This directly challenges the card's uniform-penalty plateau.
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066) studies finer expert combinations and shared knowledge, showing that specialization structure is a known design variable. Architectural changes are eligible only if the eventual artifact contract permits them at matched capacity.
- [Mixture-of-Experts with Expert Choice Routing](https://arxiv.org/abs/2202.09368) establishes alternative token/expert allocation and under-training concerns. Unrestricted batch-dependent routing is not a legal autoregressive control if it reveals future tokens; a faithful incompatible version is diagnostic only.

All primary abstract pages were opened during this session. I checked mechanism descriptions, not routing implementation causality or tensor-level cost. The compatible fixed-model floor uses bias-based balancing, exploration and rehearsal; it does not silently borrow extra experts or future-token information. Its ESTIMATED score is 0.66, with ESTIMATED range 0.43–0.87. The architecture and expert-choice sources enlarge the control inventory, but do not prove a compatible full solution.

## Saturation against the hypothetical 10T researcher / 12h

Expert utility delayed by curriculum is not automatically a hard preservation problem. If early precursor examples are still available, an adaptive researcher can simply reserve updates for later joint training. If all precursors fit inside total expert capacity, routing exploration and mild rehearsal may preserve them without predicting the future. If they cannot all fit, the learner needs early observable information about their likely future value; otherwise the claimed reference may depend on knowing the future composition. The interesting regime lies between these easy and unidentifiable cases, and the card does not instantiate it.

My tail assessment is single-run maximum ESTIMATED 0.83 versus the binding >0.70 line; oracle best-of-4 mean ESTIMATED 0.74 versus >0.60; pass@4 ESTIMATED 0.83 versus >0.50 at R>=0.60; and projected upper-95% ESTIMATED 0.94 versus >=0.75. The current design therefore likely breaches every absolute kill line. The projection is an ESTIMATED conservative scenario endpoint, not a regression-based confidence statement. FIX retains only a hypothesis that a bounded, identifiable precursor-selection distribution could change this conclusion.

S1 is OPEN: there is no midrange executable reference, demonstrated stronger legal training policy or native loss reserve. S7 is OPEN because the achievable same-budget ceiling is unknown. Teacher-forced optimal expert assignments are privileged diagnostics unless they use the identical legal information. A dense or all-expert model can diagnose representation capacity, but cannot demonstrate an attainable ceiling under the sparse active-work contract. Matching dev task depth is inadequate if the hidden interaction law changes the optimal policy without a predictive proxy.

Observed runs, observed rewards and observed pass@k are UNMEASURED. Plan independent outer training-policy searches over fresh composition families and compare complete selection policies, preserving failed attempts. Grader noise is UNMEASURED; measure both repeated evaluation of fixed logits/checkpoints and entire training reruns. Routing stochasticity, token-sampling variability and between-family variation require separate accounting. Serial time, outer reasoning, parallel search and actual activated subject work must remain distinct in scaling studies. Nothing in current-model passivity or verification weakness establishes survival against the assumed target researcher.

## Revised estimate versus the source card

The card assigns source ESTIMATED 0.45 to strong load balancing, warmup, capacity and rare-task replay. I put the lawful composite at ESTIMATED 0.66 because balancing need not inject uniform auxiliary gradients, expert identity need not remain fixed, and the training policy can postpone or repeat learning until utility is visible. The source treats preservation of marginal competence as the limit of known methods without testing whether joint rehearsal or a more distributed representation already transfers. My increase is a mechanism-based risk judgement, not a calibrated expected score.

The checked FIX packets demonstrate why a reassuring midpoint would be insufficient even if this estimate were lower: a competent combination can absorb the hypothesized reference without an obvious single exploit. Here the specific potential bypass is causal bias-based routing plus broad precursor rehearsal, not a numerical default imported from those packets. If that combination reaches the proposed reference, the delayed-specialization narrative has failed even with exemplary work accounting.

## Boilerplate and missing build content

ESTIMATED 0.65–0.82 of this short card is specific to conditional computation, and ESTIMATED 0.18–0.35 is generic proposal framing. It is not mostly boilerplate. Still missing are actual conditional architecture/checkpoint, expert state capacity, per-token versus aggregate activation budget, legal routing edits, precursor exposure schedule, availability of old tasks, composition generator, observable signals of future value and exact loss-to-reward mapping. No executable reference or native anchors are supplied.

The budget must count router features, shared modules, dormant weights, gradients and moments as well as activated experts. A peak active-parameter cap differs from a sum of all expert work across sequential passes. Both can matter; allowing serial invocation of every expert while counting only simultaneous activation would undermine the premise. Loss must use the same tokenizer, target mask and causal observation rule for every router. Excluding dropped tokens from loss would reward avoiding precisely the difficult precursor interactions.

## Duplicate check

The source points to W03, but that file is outside the permitted named reference set and was not read. Its asserted relationship remains unverified. Among checked material, T09's FIX packet addresses lifetime sparse coordinates and state allocation, and T08 addresses changing tool obligations; both share preservation under resource limits but have different interventions and truth. C012 in this assigned session also repairs a starved representation, but C042 adds conditional resource allocation and delayed interaction value. No checked comparison establishes a duplicate, and no broader uniqueness claim is made.

## Verdict, required fixes and cheapest decisive check

FIX, provided the following bounded work is completed:

1. Specify an observable precursor-selection problem with competing capacity needs and a common nonclairvoyant policy that can succeed; make the chronology and lawful revisitation budget explicit.
2. Establish a native gap above loss-free balancing, exploration, diverse replay, later relearning and whole-schedule search. Test expert permutations and distributed representations rather than requiring the author's expert identities.
3. Define total and active work, all persistent state and complete token denominators; calibrate outcome loss and slice deficits before any reward scaling. Produce both reference and feasible stronger control under those exact limits.
4. Build a trusted causal trainer/evaluator, capped recipe boundary and immutable artifact ledger. Include actual-work versus fake-counter controls, reserve-weight smuggling, future-token routing, skipped dispatch, stdout spoofing and independent all-positive implementations in `tests/test_anticheat.py`. Deliver portable privilege separation, network-none execution, trusted libraries, shape warmup, finite seed deadlines, protected dev, decontamination and complete frozen-archive records.

The cheapest decisive action is a CPU information/capacity audit, ESTIMATED 0 H100-hours: list legally distinguishable early histories and show a feasible causal preservation policy for later compositions without consulting final labels. Reject a claimed reference that needs a different early choice in indistinguishable worlds. The subsequent useful training pilot is ESTIMATED 26 H100-hours, allowing fixed-model bias-balancing, broad-replay, late-relearning and reference arms across a compact staged task distribution. This is deliberately more than the card's source ESTIMATED 18 GPU-h because the complete alternative explanations need real training, but architecture and throughput remain unpinned. No GPU work was performed; surviving either pilot would leave the empirical gates open.

## Verdict record

id: C042
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.66 (ESTIMATED 0.43–0.87)
combined_recipe_attack: ESTIMATED 0.66 (ESTIMATED 0.43–0.87)
best_of_4: ESTIMATED 0.74
pass_at_4: ESTIMATED 0.83
single_run_max: ESTIMATED 0.83
upper95_projected: ESTIMATED 0.94
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: identifiable precursor allocation; loss-free and relearning floors; actual activated work; expert-independent causal reference
main_kill_reason: modern routing and joint rehearsal may erase delayed utility
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
