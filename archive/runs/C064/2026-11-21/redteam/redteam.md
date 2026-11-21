# C064: Router regularization invariant to token packing — independent adversarial review

**Verdict: FIX.** Correcting accumulated counts is documented engineering, and published loss-free balancing directly challenges the claimed balance–expertise conflict. A narrower experiment about delayed demand for rare experts could still contain a learnable interaction, provided that interaction survives token-correct and loss-free controls. The current card neither defines the normalization semantics nor demonstrates that residual.

Source file: `/workspace/task_ideation_v4_creative/cards/C064.md`.

All reward quantities are ESTIMATED scenarios. Training outcomes, rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; the planned measurement is paired training on the same valid-token streams followed by independent compositional evaluation. The source gives a function-level upstream lead, not a delivered task package. Tests and services suggested here are proposed build content rather than inspected files.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Cumulative-token repair supplies most gain | Track valid tokens beside accumulated expert counts in `_apply_global_aux_loss`; match reduction scope and reset behavior; leave the rest of training unchanged. | ESTIMATED 0.52–0.83 | The card asks for this repair, so it is legal; no corrected baseline is frozen. | Establish a healthy token-correct starter before scoring new expertise improvement; test partition-equivalent streams and actual router gradients. | ESTIMATED 0.00–0.24 | Merely raising the baseline may reveal that there is little research reserve. |
| Remove the troublesome loss | Use expert selection biases updated from recent load; tune their update rate and only retain auxiliary regularization if legal dev loss improves. | ESTIMATED 0.58–0.83 | No; useful held-out loss rewards this published alternative. | Admit a faithful auxiliary-loss-free controller and compare both complete recipe families at equal capacity and work. | ESTIMATED 0.58–0.83 | The intended rare-expert mechanism may disappear when interfering gradients disappear. |
| Active-FLOP accounting loophole | Route hard tokens to cheap residual paths, count only selected expert matmuls, or use extra router/dense auxiliary computation without charging it. | ESTIMATED 0.67–0.96 | Equal active FLOPs is stated without an accounting definition or quality floors. | Trusted end-to-end work inventory, fixed model and token exposure; include router, padding, dropped tokens and any auxiliary path consistently. | ESTIMATED 0.00 | Legitimate compute redistribution can still be effective and must receive real credit. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read private packing schedules through dataloader descriptors or shared-memory queues; modify the held-out evaluator, base experts or token masks via writable mounts. | ESTIMATED 0.86–1.00 | No sandbox topology or frozen-asset list is provided. | Isolate evaluation text/schedules from solver processes; immutable base/runtime; descriptor and queue probes in proposed `test_router_asset_boundary`. | ESTIMATED 0.00 | Distributed rank helpers can inherit privileged handles even if the main trainer drops privilege. |
| Interface or encoded-state smuggling | Pass precomputed expert weights or protected labels through regularizer constants, serialized buffers or compressed configuration fields; reconstruct tensors in the loss callback. | ESTIMATED 0.82–1.00 | An objective artifact is named but its write authority is undefined. | Bound all nonweight channels, authenticate permitted training lineage and limit callbacks to declared differentiable quantities; distinguish lawful learned bias state. | ESTIMATED 0.00 | A generic expert-allocation algorithm is allowed even when compactly encoded. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Print fabricated held-out loss, terminate a rank before its difficult stream, or special-case the public normalization fixture's exact token mask. | ESTIMATED 0.80–1.00 | Held-out loss is an appropriate target but origin and completion checks are unspecified. | Parent computes loss over mandatory tokens; missing ranks stay failures; independently authored equivalent packing fixtures must all execute. | ESTIMATED 0.00 | A fixture-only repair could pass unit checks while training semantics remain wrong. |
| Timing/check-decoupling/branch laundering | Verify normalization on one gradient path, use another during training, import free warm optimizer state, or select a lucky unfinished branch without charging it. | ESTIMATED 0.71–0.97 | No replay or exact state/work binding is described. | Bind recipe, masks, checkpoints and work receipts; audit the trained path, cold-resume counters and charge failed searches and JIT setup consistently. | ESTIMATED 0.00 | Numerically equivalent loss values need not imply equivalent router gradients. |
| Dev-hidden leakage/cue inference | Infer mixture identity from pack lengths, padding layout or rare-domain tokenization and hardwire expert allocation to those signatures. | ESTIMATED 0.54–0.86 | Dev heterogeneity is matched, but correlation crossing is absent. | Cross domain demand with packing independently; use fresh semantic mixtures, protected dev text and a length-only router baseline. | ESTIMATED 0.19–0.49 | Content-based domain specialization is legitimate and could still solve the benchmark. |
| Adaptive aggregate oracle | Probe auxiliary coefficient, bias dynamics and rare-domain allocations, using scalar dev loss differences to recover demand weights across coordinated jobs. | ESTIMATED 0.55–0.81 | There is no stated scored-query ledger. | Publish episode-wide query, precision and cost limits; score on fresh protected blocks and test the strongest legal hyperparameter selector. | ESTIMATED 0.32–0.64 | Lawful global tuning can recover a broadly robust setting without any rare-expert insight. |
| Slice abandonment/denominator optimization | Let rare-token loss deteriorate while improving common tokens; exploit padding in the loss denominator or omit overflowed expert tokens. | ESTIMATED 0.62–0.90 | Compositional loss helps, but neither rare-cell weights nor valid-token denominator is fixed. | Parent-owned valid-token mask, fixed macro mixture and rare-composition non-regression floors; evaluate deliberate common-only specialization. | ESTIMATED 0.21–0.55 | Excessively strict rare floors could reward memorization or destroy attainable headroom. |
| Strongest lawful combined recipe | Repair all valid-token normalization and resets; search corrected auxiliary loss versus recent-load expert biases; jointly tune bias rate, capacity and coefficient schedules; select on protected compositional loss. | ESTIMATED 0.68 (ESTIMATED 0.44–0.88) | Nothing excludes this complete published-method stack, nor should it. | Compare the strongest resulting method against a demand-conditioned reference on new mixture/packing crossings. | ESTIMATED 0.68 (ESTIMATED 0.44–0.88) | Security controls leave this scientific shortcut's expected capability intact. |

## Published recipe shortcut — web checked

- [Megatron-LM issue: global_aux_loss uses current microbatch token count](https://github.com/NVIDIA/Megatron-LM/issues/7197): the opened issue specifies cumulative valid-token accounting, matching reduction scopes and reset handling; it explicitly limits its invariance claim to the examined routing-frequency fixture.
- [Megatron Core moe_utils documentation](https://docs.nvidia.com/megatron-core/developer-guide/latest/apidocs/core/core.transformer.moe.moe_utils.html): official loss documentation defines token fractions and probability averages, making numerator/denominator scope an explicit baseline obligation.
- [Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664): the primary abstract describes recent-load-dependent expert biases as an alternative to interference-producing auxiliary gradients.
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437): the primary report confirms use of auxiliary-loss-free balancing in a full MoE training system.

Verification included the actual linked issue text, official API page and primary-paper abstracts returned this session. I did not reproduce the issue's experiments, inspect its linked regression implementation or assume an upstream repair is scientifically sufficient. The recipe forecast is **ESTIMATED 0.68 (ESTIMATED 0.44–0.88)**. Its mechanisms are verified; compatibility with an unspecified task trainer and resulting reward remain unverified.

This composite is stronger than denominator correction followed by a conventional fixed balance coefficient. It gives the adversary a choice between loss families, allows unnecessary regularization to vanish and scales controller history by meaningful token exposure instead of pack count. The selected configuration is a single legal method; incompatible alternatives are compared rather than blindly combined.

## Saturation against the hypothetical 10T researcher / 12h

The immediate paper-recall shortcut is unusually direct: the card supplies the issue location, and the issue supplies the accounting intervention. A stronger researcher can reproduce the algebra, implement metamorphic partition tests, and devote remaining experiments to a small family of ordinary balancing controllers. Hidden pack schedules do not defeat a semantic invariant derived from token totals.

My conditional tail forecast is **ESTIMATED single-run maximum 0.82 compared with >0.70**, **ESTIMATED best-of-4 mean 0.77 compared with >0.60**, **ESTIMATED pass@4 0.85 compared with >0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.95 compared with ≥0.75**. These likely cross the supplied single, best-of-four, repeated-success and stronger-compute kill lines respectively. They are adverse planning estimates, with no fitted attempt distribution or confidence procedure. The wide recipe scenario includes lower outcomes because a real delayed-demand conflict might remain after accounting repair.

S1 has no measured reference, stronger feasible control or native rare-domain reserve. S7 lacks an independent achievable ceiling; smaller attainable improvement would make moderate reward less reassuring. These gates are OPEN rather than independently demonstrated breaches. The measurement plan must hold subject parameters, token exposures and deployed compute constant while separately varying researcher time, token budget and experiment concurrency. A larger MoE does not test a stronger research solver.

The supplied weakness reports suggest checking sustained experimentation and verification, but they also warn about strong known-recipe ML performance. I assume competent persistence and gradient checks. A FIX remains credible only if independent data show that future useful expert demand changes which balancing intervention is beneficial, and that ordinary history-aware bias adaptation cannot learn the same rule within budget. That interaction needs intervention evidence, not the label “rare expertise.” All observed tail metrics remain UNMEASURED until full-budget restarts on independently authored mixtures; intervals touching a kill line cannot pass.

## Revised estimate versus the source card

The card assigns **ESTIMATED 0.47** to normalization repair plus standard balance/capacity control. My strongest lawful forecast rises to **ESTIMATED 0.68 (ESTIMATED 0.44–0.88)** because loss-free allocation is a pertinent bypass of the auxiliary-gradient conflict itself. The card acknowledges a possible generic robust recipe but does not incorporate its strength into a ceiling analysis. The calibration FIX packets teach that complete legal methods can remain close to the reference after security repair; they do not supply C064's numerical forecast. Here the higher estimate follows directly from an alternative published mechanism and a publicly explained first-stage repair.

## Boilerplate and missing build content

**ESTIMATED 25–35%** of the source is general evaluation/compliance language; **ESTIMATED 65–75%** concerns router normalization, packing and expertise. It is not mostly boilerplate, but its specificity is conceptual. The exact desired objective is still missing: running-prefix versus full accumulated-batch probabilities, stop-gradient treatment of expert counts, rank reduction scope, reset cadence, gradient-accumulation scaling, padding semantics and numerical tolerances.

Also missing are subject architecture and capacity, corpus/domain rights, rare-composition definitions, a faithful corrected starter, exposure/work budgets, editable routing operations, bias persistence, held-out reward normalization and a causal reference. A loss disagreement cannot become hidden truth while the public contract leaves these choices open. Any reference fitted after looking at private schedules would contaminate the test. The builder must retain raw per-token loss and work alongside reward, showing both actual specialization value and dependence on packing.

## Duplicate check

I checked v3 04A in `04_training_fidelity.md`. It concerns asynchronous MoE version, route and cache consistency, whereas C064 isolates packing-dependent objective accounting. These share routing instrumentation but have different causal interventions. No duplicate is established; that judgment does not cover unread catalog packets or other creative cards. A future implementation should keep async repair out of C064's reward, otherwise its boundary could drift toward the checked task.

## Verdict, required fixes and cheapest decisive check

**FIX**, with these bounded requirements:

1. Freeze token-normalization mathematics and ship a repaired, healthy baseline. Put the public accounting fix below the new research reward floor while retaining native outcomes.
2. Define a disclosed, observable delayed-demand interaction with fresh semantic compositions. Cross demand with packing so length recognition cannot stand in for expertise.
3. Admit complete auxiliary and loss-free controllers, including adaptive history and legal tuning. Require a native margin and causal interaction after both have been tuned competently.
4. Specify all work accounting, protected feedback, fixed denominators and the objective callback's state authority; independently verify the delivered trainer and evaluator boundaries.

The cheapest decisive experiment is CPU algebra and a hand-designed partition counterexample: compare the proposed contract's value and gradient under alternative packings of the same legal token stream, including resets and changing route frequencies. **ESTIMATED 0 H100-hours**. This can refute the stated invariance or reveal that the public fix already fulfills the whole specified mechanism. It cannot measure expertise; only if it survives should paired MoE training be costed from an actual architecture and token ledger. The card's GPU allowance cannot be validated without those missing inputs.

Before release, R2 still requires actual independent cheat sessions and negative regressions for encoded payloads, fake rank completion, frozen expert mutation, score-channel bypass and seed starvation. Portable local OCI startup, trusted CUDA linkage, symmetric warmup, no credentials/egress, private provenance and complete archive/rollout reconciliation are also absent. None was exercised in this session.

## Verdict record
id: C064
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.68 (0.44–0.88)
combined_recipe_attack: ESTIMATED 0.68 (0.44–0.88)
best_of_4: ESTIMATED 0.77
pass_at_4: ESTIMATED 0.85
single_run_max: ESTIMATED 0.82
upper95_projected: ESTIMATED 0.95
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: public normalization contract; repaired starter; loss-free composite floor; observable delayed-demand interaction; trusted work and score ledger
main_kill_reason: known balancing methods may absorb specialization gain
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 4
