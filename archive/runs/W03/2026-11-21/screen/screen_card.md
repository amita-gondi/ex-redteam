# W03 — Dense-to-MoE growth with compositional expert specialization — saturation screen
## 1. What the grader actually rewards
The retained W03 formula grades exact neural answers across semantic families, composition depths and lexical swaps, subject to actual active-work and memory limits on the same execution. Using the ESTIMATED constants, it averages seed capability minus small slice deficits, subtracts a reporting deduction and computes `clip((V_native−0.32)/0.68)`: effective utility at ESTIMATED 0.32 earns zero, ESTIMATED 0.728 corresponds to R=0.60, and perfect unpenalized answering corresponds to R=1. The floor has never been calibrated, dense/default no-op outcomes are UNMEASURED, and the revision withdraws its reference and stronger-control performance predictions. Neither specialization nor load balance receives direct reward, and failed novel triples only lose their local share and bounded deficit penalty. Numerical scenarios, resource estimates and the Screen record below are all ESTIMATED; the cited hard lines remain the user's requirements.

## 2. Strongest lawful combined attack
Use the dense ancestor to initialize narrow routed FFNs plus a shared path, then optimize all allowed weights jointly without attempting to name expert roles. [Sparse Upcycling](https://arxiv.org/abs/2212.05055) establishes dense-checkpoint reuse as a standard starting method. [Upcycling Large Language Models into Mixture of Experts](https://arxiv.org/abs/2410.07524) supplies more specific compatible ideas: virtual-group initialization, weight scaling and softmax-before-top-k routing for granular experts. [DeepSeekMoE](https://arxiv.org/abs/2401.06066) contributes fine expert segmentation and shared capacity. These are initialization and persistent conditional branches from one ancestor; there is no souping/merging dependency.

Constrain the sum of activated widths, shared path and router costs before training. A copied full-width expert plus an additional full shared FFN would breach this task's envelope; the attack needs width redistribution and a checked forward match. Compare a conservative copied-expert branch with the granular/shared branch and dense continuation, using the same frozen data stream and CE targets. Apply trusted balancing and router z-loss within their allowed coefficient ranges, cautious router warmup, ordinary AdamW continuation and protected composition-based selection. The verified [OLMoE instructions](https://github.com/allenai/OLMoE/blob/main/README.md) already describe upcycling, expert-choice and shared-layer options, although conversion into W03's unbuilt tensor interface remains unverified.

An ESTIMATED full-budget allocation is 16 H100-h for initialization/parity and gradient probes, 24 H100-h for short architecture comparisons, 128 H100-h for completed longer contenders, 16 H100-h for protected/audit inference and 8 H100-h for failed work: ESTIMATED 192 H100-h. The selected ancestry must complete inside research time; the grader cannot finish an unfinished plan. The architecture variants receive identical examples/order, and no solver-generated demonstrations or replacement targets enter the common stream. Submit receipt-backed mandatory claims and leave optional functional interpretations unestablished.

I estimate **single-run R=0.54**, range **0.31–0.73**; **best-of-four R=0.63**; **pass@4 at R≥0.60=0.59**; and **projected upper-95% score bound=0.80**, all ESTIMATED. This is a subjective forecast, not a measured tail law or fitted projection. A central ESTIMATED capability vector by relation stratum is `(0.91,0.87,0.75,0.22)`, averaged across families/renderings: ESTIMATED U=0.6875 and approximately R=0.54 with accurate reporting and inactive floors. A favorable ESTIMATED `(0.95,0.92,0.83,0.22)` gives U=0.73 and approximately R=0.60 without solving triples well. Assigning ESTIMATED per-attempt threshold success 0.20 yields ESTIMATED `1−0.80⁴≈0.59`; dependence through the inherited instance is a major uncertainty.

I disagree with §10's ESTIMATED U=0.80/R≈0.71 stress center as a typical outcome. Fixed attention, unchanged demonstrations, near-dense active work and limited completed training can leave a much larger triple-composition deficit than that scenario assumes. Copying experts preserves functions but does not establish new combinations, and published upcycling results do not supply task-specific exact-answer accuracy. Even my lower center is dangerous because useful generic improvements on the easier strata can carry repeated attempts over the reward threshold. The source's existing CUT additionally rests on its structurally insufficient insight graph; that is separate from this saturation forecast.

## 3. Other routes
- **Copied upcycling with conventional routing:** retain dense behavior initially, then train a balanced top-one expert model without specialized subspace diagnosis: ESTIMATED R=0.38, range 0.17–0.59. Expert redundancy and weak composition learning can limit gains despite sound initialization.
- **Architecture/configuration search:** rank sharing fractions, expert granularity, routing conventions and warmup using partial runs, then complete the best candidates across the available GPU groups: ESTIMATED R=0.50, range 0.28–0.71. Proxy-to-private-seed transport may reverse short-run rankings; the branch timeout is no lower bound on how many useful trials fit.
- **Reward specialization:** prioritize single-domain, familiar and pair behavior, accepting poor novel triples and using truthful minimal reporting: ESTIMATED R=0.52, range 0.32–0.63. The task's own illustrative ESTIMATED `(0.98,0.98,0.98,0)` earns approximately R=0.603 after the slice deduction. This is formula arithmetic, not evidence that the learner attains those easy-stratum accuracies. Certification floors expose the abandonment but do not prevent its reward.

## 4. What would lower lawful saturation
Give independently authored novel-triple outcomes greater scientific weight before calibration, while retaining continuous partial credit and checking every slice. One concrete candidate is ESTIMATED relation weights `(0.20,0.20,0.20,0.40)`, instead of equal weights. Applied only as sensitivity arithmetic to the central vector, ESTIMATED U becomes 0.594 and R approximately 0.40, a reduction near ESTIMATED 0.14 R; the favorable vector similarly falls below the success line. ESTIMATED cost is 2 author-days plus 192 H100-h to test preservation, specialization and score-ladder behavior. This does not prove a harder attainable problem: the reference and same-contract stronger control must still demonstrate real reserve.

A meaningful scientific successor would also need architecture-specific cases where generic shared/private optimization loses to a reproducible intervention on inherited functions, under unchanged data/work. Establishing that could cost ESTIMATED 4–6 author-weeks and 768 H100-h of matched architecture/subspace controls; its score effect is UNMEASURED, planned as the raw capability contrast, rather than an assumed benefit. Additional graph labels, mandatory role claims and delayed training would not create the missing dependence. These are redesign candidates, not repairs that reopen the current source's closed spending contract.

## 5. Decisive-check GPU-h re-estimate
The stated §7 “Cheap anchor tranche” is “19×384+10×192=9,216” GPU-h, an ESTIMATED retired validation allowance. Section 7 also retains ESTIMATED B=192 H100-h and complete H≤192 H100-h, with the private training seeds already included in H.

For the binding repeated-attempt concern, my new ESTIMATED screen is **5,760 H100-h** if a successor package already exists. Run ESTIMATED 3 independent ancestor/content blocks × 4 randomized full-budget scripted stack searches. Search costs ESTIMATED 12×16 H100×12 hours=2,304 H100-h. Each selected artifact's reconstructed training costs ESTIMATED 3 seeds×8 H100×6 hours=144 H100-h; over the attempts that is ESTIMATED 1,728 H100-h. Budget ESTIMATED 12×32=384 H100-h for hidden and source-audit inference, plus ESTIMATED 12×16=192 H100-h for conversion/cold-resume audits. Attack total is ESTIMATED 4,608 H100-h; add ESTIMATED 3 reference builds-and-grades×384=1,152 H100-h, yielding ESTIMATED 5,760 H100-h.

The subject is the continued OLMo-1B ancestor with width-matched sparse variants; a larger OLMo-7B study is unnecessary for this first kill test. Independent searches and continuation seeds are different sampling units. This small block sample can expose a clear high-scoring recipe or single-run breach, but its pass@4 uncertainty may remain unresolved; it cannot certify survival. The evaluation allowance is provisional because the critique identifies insufficient per-slice effective sample size and unprofiled decoding cost. None of this work is launched, and no GPU experiment is needed to recognize the source's separate graph failure.

## 6. Duplicate check
- **v3 04A — WEAK:** the opened source targets asynchronous version/router/cache fidelity; W03 begins with healthy synchronous execution and changes persistent FFN capacity.
- **FIX T09 — WEAK:** its actual intervention changes lifetime update-coordinate supports and packed training, rather than conditional inference activation.
- **Catalog T04 / retained suite 5.2 — MODERATE:** both actual sources admit jointly trained shared/private capacity and gates, closely matching the functional-factorization narrative; their tool-policy terminal-success target differs from W03's FFN composition task.
- **D26 — WEAK:** source geometry guides trajectory acquisition after actor updates, not dense-to-expert construction.
- **Creative C042 — MODERATE:** its source grades complementary expert compositions but starts from an existing conditional learner and targets delayed utility, rather than constructing experts from a dense checkpoint.
- **Creative C064 — MODERATE; C046 / C104 — WEAK:** opened sources respectively concern router-objective packing semantics, changing activation depth, and compression/curriculum feedback; none duplicates the same intervention and grader target.
- **Sibling W04 — MODERATE:** its actual revised source grows a prescribed dense all-active deployment architecture, whereas W03 retains conditional branches. No STRONG duplicate is established by these comparisons.

## 7. Verdict
**CUT**, with binding ESTIMATED pass@4=0.59 exceeding 0.50 by ESTIMATED 0.09. ESTIMATED best-of-four also exceeds its line, and the ESTIMATED projected upper bound crosses 0.75; these remain desk judgments rather than measured kills. The unresolved critique objections are that joint training may discover the supposed functional split without diagnosis and that the published utility pays substantial reward despite novel-triple failure. The current revision has already cut itself for a separate A7 structural failure; this card neither substitutes that failure for measured saturation nor recommends resurrecting it.

## 8. Measurement status
Rollouts UNMEASURED (planned: completed generic upcycling searches over fresh ancestors, alongside dense/reference arms). Grader noise UNMEASURED (planned: same-seed replay, cross-seed reconstruction and world-cluster inference variance separately). Score ladder UNMEASURED (planned: dense continuation, copied experts, granular/shared experts, joint optimization and triple-specialized controls). Competent-recipe anchor UNMEASURED (planned: matched active-work, identical-stream comparisons before accepting the retained floor or any claimed architecture reserve).

## Screen record
id: W03
verdict: CUT
binding_line: pass4>0.50
attack_single_est: 0.54
attack_single_range: 0.31-0.73
bo4_est: 0.63
pass4_est: 0.59
ub95_est: 0.80
gpuh_task_stated: 9216
gpuh_new_est: 5760
duplicate_of: T04 MODERATE; C042 MODERATE; C064 MODERATE; W04 MODERATE
kill_reason: generic shared and routed expert training can cross repeated-success line without strong triple composition
souping_flag: no
