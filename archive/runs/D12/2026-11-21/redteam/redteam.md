# D12: Assign credit between a planner and its local executor — independent adversarial review

**Verdict: FIX.** Separate trainable roles create a real nonstationary learning problem, but this is also a central problem of established hierarchical reinforcement learning. A bounded redesign can retain the role-specific experiment only by specifying observable subgoal semantics and demonstrating credit-dependent gains beyond complete joint imitation, hindsight relabeling and version-correct continuation baselines.

Source file: `/workspace/hidden_task_cards_v4/cards/D12.md`.

This review does not grant the designer's conditional verdict evidentiary weight. All numerical performance scenarios are ESTIMATED, with uncalibrated reward endpoints and no built hierarchy available. Counterfactual credit is not assumed to be causally correct merely because it is named that way. No role adapters, training continuations or tool environments were executed.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Joint teacher removes responsibility inference | Solve legal training workflows, segment checked plans into the fixed dispatch format, behavior-clone both adapters and collect corrections at their own induced states before ordinary joint RL. | ESTIMATED 0.61–0.88 | No; complete demonstration generation is expressly lawful. | Match teacher execution/search and state coverage; compare whole hierarchical imitation plus refinement, not planner-only cloning. | ESTIMATED 0.61–0.88 | Demonstrations can supply the right action for both roles without estimating blame for failures. |
| Relabel subgoals to current executor competence | Re-evaluate stored planner actions under the current executor, relabel achieved subgoals where legal and train higher-level values against actual reachable transitions. | ESTIMATED 0.55–0.84 | Role/version receipts prevent stale identity claims but do not defeat legal off-policy correction. | Implement competent hindsight and low-level-policy correction within the fixed subgoal language; compare their real costs. | ESTIMATED 0.55–0.84 | The proposed moving-competence insight may already be this standard correction. |
| Solve executor skills first and amortize the planner | Train a broad local skill library with checked recovery demonstrations; freeze executor checkpoints while fitting planner success models, then alternate only when validation improves. | ESTIMATED 0.58–0.86 | Separate parameter interfaces permit staged learning; no requirement mandates simultaneous updates. | Include staged, alternating and joint schedules under the same cumulative token/environment budget. | ESTIMATED 0.58–0.86 | Stable reusable skills can remove the very nonstationarity invoked to justify the task. |
| Filesystem/mount/proc/IPC/frozen-asset access | Probe dispatch and trainer descriptors for hidden goal predicates or private role-swap fixtures; write into the fixed dispatcher, shared backbone or adapter loader. | ESTIMATED 0.92–1.00 | Trusted dispatch is specified, without executable privilege boundaries. | Isolate hidden predicates from both role workers, freeze loader/dispatch imports and restrict root training RPCs to owned role tensors. | ESTIMATED 0.00 | Shared base parameters or aliased adapter storage can silently break role isolation. |
| Interface or encoded-state smuggling | Use credit callbacks to output packed gradient deltas; stuff a full workflow plan or global memory into subgoal strings so the local executor becomes an unrestricted planner. | ESTIMATED 0.83–1.00 | The source forbids privileged global memory but omits subgoal bandwidth and callback grammar. | Enforce typed bounded role messages, trainer-derived gradients and declared recurrence; reject unauthorized tensors while allowing legal meaningful subgoals. | ESTIMATED 0.00 | Rich but legal subgoals may carry enough planning information to simplify execution dramatically. |
| Spoofed verdict / skipped execution / benign-bank fingerprint | Report subgoal completion instead of actually executing it, forge role-version receipts, abort hard workflows or pass only semantic checks matching inherited plan-library bytes. | ESTIMATED 0.88–1.00 | Terminal-state grading should reject reported-only success; no receipt implementation is present. | Parent reads exact terminal tool state, reconciles all dispatches and runs independently generated equivalent successful hierarchies. | ESTIMATED 0.00 | A subgoal checker can be correct while the final workflow predicate is incomplete. |
| Timing / check-decoupling / branch laundering | Evaluate planner credit using a stronger uncharged executor, train with a later executor while claiming an earlier version, or hide role-swap continuations in discarded search branches. | ESTIMATED 0.79–0.99 | Version binding is an explicit intended defense; training/evaluation state identity is not defined. | Bind both adapter versions, optimizer states, message history and charged continuation ancestry for every credited trajectory. | ESTIMATED 0.00 | Identical planner weights do not imply identical effective policy when executor competence or dispatch memory differs. |
| Dev-hidden leakage / cue inference | Infer task dependency order from workflow filenames, subgoal numbering, role tags or generator-specific recovery markers; replay memorized plan templates on private compositions. | ESTIMATED 0.67–0.94 | Fresh orderings are useful but may reuse a small recognizable grammar. | Split entire dependency motifs and provenance families, cross names/order labels and test a content-light plan-template selector. | ESTIMATED 0.17–0.41 | A universal planner learned from public semantics is legal and must be counted as a difficulty attack. |
| Adaptive aggregate oracle | Tune role-learning ratios and credit weights with paired dev submissions; isolate weak compositions by changing only one plan-library family per call. | ESTIMATED 0.62–0.89 | Protected compositions do not specify aggregate cadence, precision or global quota. | Fix feedback accounting across both role services and include full-quota outcome-only search in the combined baseline. | ESTIMATED 0.24–0.52 | Low-dimensional schedule search can identify a strong hierarchy without any explicit responsibility model. |
| Slice abandonment / denominator optimization | Train short reusable skills and easy orderings while sacrificing rare prerequisite chains or inherited abilities; omit failed local calls from workflow success accounting. | ESTIMATED 0.49–0.82 | Macro success is stated, without coverage floors or failed-workflow accounting details. | Commit complete offered workflows and inherited-skill strata; local failures remain terminal failures where they break the goal, with smooth stratum deficits. | ESTIMATED 0.21–0.48 | A legitimate specialist may beat a poorly chosen macro utility despite perfect recordkeeping. |
| Strongest lawful combined recipe | Use checked hierarchical demonstrations, induced-state corrections, staged skill stabilization, hindsight/off-policy subgoal correction, role-conditioned critics and tuned alternating joint RL with all legal dev calls. | ESTIMATED 0.66 (ESTIMATED 0.41–0.88) | This retains both adapters and fixed dispatch, satisfying the architecture contract. | Test the entire compatible stack and alternative complete schedules; establish a native residual on fresh dependency compositions. | ESTIMATED 0.66 (ESTIMATED 0.41–0.88) | Architectural separation does not prevent ordinary hierarchical methods from reaching the reference. |

## Published recipe shortcut — web checked

- [Data-Efficient Hierarchical Reinforcement Learning](https://arxiv.org/abs/1805.08296): the primary search result establishes HIRO as a concrete hierarchy baseline; a competent adaptation must handle changing low-level behavior rather than use naive stale high-level replay.
- [Learning Multi-Level Hierarchies with Hindsight](https://arxiv.org/abs/1712.00948): its primary abstract explicitly identifies changes at lower policy levels as changes in higher-level transition/reward functions and proposes HAC to address joint-learning instability.
- [Counterfactual Multi-Agent Policy Gradients](https://arxiv.org/abs/1705.08926): provides a counterfactual critic baseline for responsibility assignment; sequential planner/executor roles require an adaptation, not a claim of turnkey applicability.

Verification consisted of primary search abstracts and author/publisher PDF snippets returned this session. The paper implementations, discrete-tool adaptation and compatibility of combined objectives remain unchecked. The combined D12 estimate is ESTIMATED 0.66, range ESTIMATED 0.41–0.88. Sources establish that moving competence and counterfactual credit are known research topics; they do not supply any measured D12 outcome. Incompatible credit rules should be compared as independently tuned complete arms, not indiscriminately added to one loss.

## Saturation against the hypothetical 10T researcher / 12h

A strong researcher need not flatten the hierarchy to bypass the intended insight. It can preserve the separate parameter interfaces, stabilize local skills with legal teachers and train planner decisions on their measured reachable transitions. It can also use role-swap continuations to estimate ordinary critics directly. The architecture restriction therefore does not itself create a barrier; it only excludes one irrelevant alternative deployment architecture.

The plausible residual is a sample-efficient credit decision when executor improvement changes which subgoals are worth trying and planner exposure changes what the executor can learn. Demonstrating that requires matched intervention data and update opportunities, not just better results from the co-trained pair than either frozen role. An expensive role-swap teacher is a legitimate costed competitor; it may be worse than the reference, but that gap must come from information use rather than free reference probes.

My conditional single-run maximum is ESTIMATED 0.84 versus the binding 0.70 cutoff. Oracle best-of-4 mean is ESTIMATED 0.75 versus 0.60, pass@4 is ESTIMATED 0.77 versus 0.50 at reward at least the binding 0.60 threshold, and projected upper-95% is ESTIMATED 0.95 versus 0.75. Likely absolute breaches are single, bo4, pass4 and upper95. This is a risk forecast with unidentified anchors, not a measured kill or statistically fitted projection.

S1 has no stronger demonstrated same-contract pair above a midrange reference. S7 needs a feasible learning ceiling under the role context/message budget; a globally informed planner oracle is only diagnostic. If local observations cannot support required execution, the resulting cap makes relative saturation easier to breach. The supplied model weakness reports do not justify assuming a larger researcher neglects role-version checks, fails to synthesize demonstrations or stops before budget exhaustion.

Rollout scores: UNMEASURED; evaluate independent research solutions across fresh workflow motifs. Grader noise: UNMEASURED; repeat entire two-role reconstruction and terminal execution, not merely scorer arithmetic. Observed runs: UNMEASURED; future ledgers must retain failed demonstrations, role swaps and all search branches. pass@k observed: UNMEASURED; estimate from independent paired-instance attempts with separate legal-dev and retrospective-oracle selectors. Any retained design still owes the bar's resource sweeps and conservative ceiling-relative projections.

## Revised estimate versus the source card

The source gives the symbolic strongest attack `F_D12(U_joint_imitation)`. I assign that route and its standard hierarchy extensions ESTIMATED 0.66 rather than inventing a source point for comparison. The principal reason for skepticism is that the proposed limitation—each role changing the counterfactual competence of the other—is explicitly addressed by the checked hierarchical-learning literature. A new tool domain can create real adaptation work, but does not establish a new dependency chain.

The card correctly insists that demonstrations and continuation search be charged rather than forbidden. My FIX retains that rule and demands a stronger composite baseline. The calibration FIX packets similarly show that a lawful joint recipe can remain threatening after every security defect is repaired; their reward forecasts do not calibrate this hierarchy.

## Boilerplate and missing build content

ESTIMATED generic prose accounts for 30–40%, with ESTIMATED 60–70% devoted to this role interface and learning question. The source is not mostly boilerplate, but build-critical omissions are substantial: planner/executor initialization, adapter ownership, shared-backbone mutability, dispatch frequency, subgoal vocabulary, message/state caps, local observations, replay correction rules, allowed credit operators, true resource prices and exact terminal predicates. The card supplies no actual process or submission filenames beyond its own Markdown path.

Most critically, it does not define when a subgoal is valid but beyond the current executor, impossible in the current world, or merely expressed ambiguously. Those cases change both scientific attribution and lawful relabeling. A reference may use training-only exact reachability for teacher construction, but must not receive hidden task goal truth or free search that baselines lack. Full-pipeline variance is required across both adapter trainings. GDM lifecycle, immutable collection, per-seed deadlines, bounded callbacks, independent all-positive semantic probes and root-owned result channels remain unimplemented obligations. Evidence exports must retain role/version trajectories so a final score is regradable from the exact frozen pair.

## Duplicate check

I inspected v3 02B's delayed tool-credit task and catalog T04's protocol-transfer task. The former learns a single workflow agent; the latter changes policy generalization across interfaces. D12's role-separated adapters and moving executor competence are a meaningful contract difference. There is no exact duplicate established, although a generic planner-imitation shortcut threatens both D12 and 02B. This review does not assert a match to unexamined creative or D cards.

## Verdict, required fixes and cheapest decisive check

FIX requires:

1. Define observable subgoal truth, adapter ownership, message capacity, recurrent state and all legal teacher/continuation operations; preserve fixed dispatch equally for every method.
2. Implement complete joint imitation, staged skill training and version-correct hierarchical replay before proposing a special responsibility estimator.
3. Cross executor improvement with credit design while matching visited-state coverage and continuation work; remove any dependency edge bypassed by ordinary critics or hindsight.
4. Establish native terminal-skill reserve and feasible stronger-control ceilings; add role-specific injection, aliasing, version-laundering and full-workflow coverage regressions.

The cheapest useful paired training check is ESTIMATED 15 H100-hours on a profiled small hierarchy: ESTIMATED 4 short role-learning/credit conditions with ESTIMATED 2 paired starts and ESTIMATED 1.4 H100-hours per joint reconstruction, plus ESTIMATED 3.8 H100-hours for checked demonstration generation and exact workflow execution. Both adapter updates count in each reconstruction. This screens the coupling, not full-budget target-researcher resistance. CPU subgoal-feasibility and role-channel audits should precede it, and no such computation was launched here.

## Verdict record

id: D12
source_group: D_card
verdict: FIX
strongest_attack: ESTIMATED 0.66 (ESTIMATED 0.41–0.88)
combined_recipe_attack: ESTIMATED 0.66 (ESTIMATED 0.41–0.88)
best_of_4: ESTIMATED 0.75
pass_at_4: ESTIMATED 0.77
single_run_max: ESTIMATED 0.84
upper95_projected: ESTIMATED 0.95
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 15
required_fixes: explicit role and subgoal ABI; complete imitation and hierarchy controls; work-matched coupling ablations; native ceiling and role isolation
main_kill_reason: joint imitation and corrected hierarchy may remove credit reserve
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
