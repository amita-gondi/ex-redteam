# C080 — Recover address-generation speed without changing integer semantics — screen audit

## 1. What the screen claimed
The screen combined ScalarEvolution ranges, bit-vector equivalence checking, guarded specializations and complete-graph profiling. Its ESTIMATED single/bo4/pass4/ub95 were 0.48/0.58/0.32/0.73; verdict CONDITIONAL because wrap-sensitive workload balance and specialization accounting were unresolved. The TSV gives no kill category; the concern is a potential compiler-analysis shortcut rather than an observed kill.

Old sources, all fetched now:
- SLSR stops strength-reducing Triton's GEPs — triton-lang/triton, 2026 — https://github.com/triton-lang/triton/issues/11750
- ScalarEvolution source — LLVM Project, 2026 accessed revision — https://llvm.org/doxygen/ScalarEvolution_8cpp_source.html
- Bitvectors — Microsoft Z3 guide, 2026 accessed docs — https://microsoft.github.io/z3guide/docs/theories/Bitvectors/

## 2. Evidence audit
The regression report explicitly explains why sign extension cannot distribute over wrapping addition, and why globally adding nonwrapping flags changes semantics. ScalarEvolution and Z3 support pieces of safe specialization, but neither is a demonstrated search procedure that discovers profitable graph-level bounds and validates hardware speed within this task's budget.

Grade: PARTIAL. Safe local reasoning is established; automated profitable integration across shape constraints is the missing component. The earlier conditional judgment was more cautious than most of this batch, yet its best-of-four and projected tail still lacked an explicit generating distribution.

## 3. Research done now
- Alive2: Automatic verification of LLVM optimizations — AliveToolkit contributors, 2026 accessed repository — https://github.com/AliveToolkit/alive2 — fetched — A practical translation validator strengthens the legality filter, while its supported LLVM semantics and bounded-loop treatment cannot be replaced by an arbitrary integer-equivalence script.
- LLVM Translation Validation Automated with Large Language Models and Lean — Chunhao Liao et al., 2026 — https://arxiv.org/html/2609.19583v1 — fetched — Trivet resolves 147 of 148 supplied transformations with checked proofs/refutations, materially raising the attack's proof capability; it does not invent profitable GPU transformations.
- Can Coding Agents Implement Missed Compiler Optimizations? Evaluating LLM Agents on LLVM Peephole Optimizations — Hongxu Xu et al., 2026 — https://arxiv.org/html/2607.02684v1 — fetched — Agents frequently miss human profitability or mishandle optimizer mechanisms, directly cutting against assuming that safe rewrite discovery and integration are solved.
- CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation — Weinan Dai et al., 2026 — https://arxiv.org/abs/2602.24286 — fetched — Strong KernelBench results establish serious GPU-code capability, but the fetched report does not demonstrate intentional-wrap preservation across address-program families within twelve hours.

Search included compiler-agent proofs, missed optimizations and the exact Triton regression. The two compiler-specific studies are more comparable than a generic code-generation score.

## 4. Re-estimated attack
All allocations, probabilities, ranges and derived rewards here are ESTIMATED. Stock safe-range reasoning might recover 0.22 of available reward, guarded factoring 0.15 and graph-aware specialization another 0.10. This totals 0.47 under the provisional scale; it assumes ordinary affine cases contribute substantial utility while valid wraps prevent a universal unsafe shortcut. Actual floor/control graph times are unavailable, so instruction counts are not converted mechanically into reward.

Use outcomes 0.28/0.47/0.68 with probabilities 0.20/0.60/0.20. The lower mode finds only conservative repairs; the upper mode discovers useful cross-operation bounds and amortizes proofs. Single = 0.056+0.282+0.136 = 0.47, range 0.28–0.68. Bo4 = 0.68−0.21×0.80^4−0.19×0.20^4 = 0.59; pass4 = 1−0.80^4 = 0.59; ub95 = 0.68. Despite a mean near the old estimate, this distribution's insight-dependent upper mode breaches pass4: the old 0.32 could not be assumed independently of its reward distribution. Spread comes from discovering profitable guards and completing validation, not invented grader noise.

## 4A. Demonstrated capability and subfield SOTA
The strongest verified proof-system comparator located is Trivet alongside Alive2. Trivet extends integer transformation validation beyond fixed widths and some bounded-loop limitations, but leaves memory instructions outside its current formalization. A native R≈1 reference must therefore demonstrate faster legal ML address execution with accepted wrapping cases, not merely prove a supplied algebraic identity. No global best GPU address compiler was verified.

Trivet uses GPT-5.5 through Codex CLI inside a deterministic proof scaffold; Lean checks success. Its difficult fixed-width cases take reported 207–1257 seconds, while hardware/total campaign compute is not specified in the fetched account. The gap is finding profitable transforms and connecting integer proofs to pointer/memory semantics. PeepholeBench evaluates Sonnet 4.6/Claude Code, GPT-5.4/Codex and Gemini 3 Flash/Gemini CLI with two-hour task limits and three runs per task, retrying empty patches. No agent matches human correctness and profitability together; host specifications were not established here. Its gap to C080 is GPU whole-graph performance, but its optimizer-specific failures are directly relevant negative evidence.

KNOWN-RECIPE includes range analysis, checked candidates and guarded dispatch. The full autonomous profitable compiler attack is LITERATURE-ONLY; proof completion is AGENT-DEMONSTRATED as a component, not as the whole research outcome. Within twelve hours the attacker still needs useful shape-derived bounds, semantically valid lowering and amortized speed. Anchored ESTIMATED outcomes 0.17/0.39/0.64 have probabilities 0.28/0.64/0.08: single 0.35, range 0.17–0.64; bo4 = 0.64−0.25×0.92^4−0.22×0.28^4 = 0.46; pass4 = 1−0.92^4 = 0.28; ub95 = 0.64. These scenario masses are assumed transfers, not frequencies measured by either compiler paper.

## 5. Verdict under the kill lines
Section 4's recipe stress case is CUT through ESTIMATED pass4 0.59. The headline ANCHORED verdict is PASS-SCREEN, FLIPPED CONDITIONAL→PASS-SCREEN. Anchored margins to single, bo4, pass4 and ub95 lines are ESTIMATED 0.35/0.14/0.22/0.11. Recent checked-proof results raise one component, but the more comparable profitability benchmark leaves the combined optimization unproven. This is an assumption-dependent desk pass, not acceptance-bar certification or a claim that the future approximately 10T attacker has been measured.

## 6. Redesign
NOT-NEEDED. The original contract already includes legitimate wrapping inputs and disclosed bounds, so the anchored forecast does not require a new hidden mechanism. Preserve that contract in implementation: both wrapping and bounded programs must carry meaningful useful work, all accepted inputs remain legal, and proof/compile costs enter complete graph cost. A future bank dominated by trivial affine offsets would change this verdict; it should trigger recalibration, not retroactive exclusion of a correct optimizer. Kill cause class is na because the anchored task is retained.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent semantics-preserving compiler agents on frozen address families). Grader noise UNMEASURED (planned: paired timing repeats with unchanged compiled artifacts). Score ladder UNMEASURED (planned: safe local repair, ScalarEvolution guards, translation-validated search, graph-bound reference and stronger feasible control).

## Audit record
id: C080
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 7
old_single: 0.48
old_bo4: 0.58
old_pass4: 0.32
old_ub95: 0.73
new_single: 0.47
new_single_range: 0.28-0.68
new_bo4: 0.59
new_pass4: 0.59
new_ub95: 0.68
new_verdict: CUT
binding_line: pass4>0.50
flip: CONDITIONAL->CUT
kill_cause_class: na
redesign_status: NOT-NEEDED
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: Trivet, GPT-5.5 Codex, 2026; PeepholeBench, Sonnet 4.6 and GPT-5.4 CLI agents, 2026
gap_to_attack: discover profitable wrap-safe graph-bound GPU transformations
subfield_sota_ref: Trivet integer validation, Liao et al., 2026; Alive2 LLVM validation, AliveToolkit, 2026 accessed
anchored_single: 0.35
anchored_bo4: 0.46
anchored_pass4: 0.28
anchored_ub95: 0.64
anchored_verdict: PASS-SCREEN
anchored_binding_line: none
anchored_flip: CONDITIONAL->PASS-SCREEN
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
