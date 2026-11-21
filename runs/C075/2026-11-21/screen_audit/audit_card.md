# C075 — Rollback research branches that stay rolled back — screen audit

## 1. What the screen claimed
The screen proposed immutable checkpoint identities, transactional selection, asynchronous persistence, exact chunk reuse and a bounded search beam. Its ESTIMATED single/bo4/pass4/ub95 were 0.83/0.90/0.99/0.98; verdict CUT, category MEM, because a checkpoint DAG and retention policy supposedly solve the storage extension.

Old citations, fetched here:
- Distributed Checkpoint — PyTorch, 2026 accessed docs — https://docs.pytorch.org/docs/main/distributed/checkpoint.html
- Asynchronous Saving with Distributed Checkpoint — PyTorch, 2026 accessed tutorial — https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html

## 2. Evidence audit
DCP supplies serialization and staging, not a branch-value policy or guaranteed storage savings after optimizer trajectories diverge. The old exact chunk-dedup claim lacked measurements of unchanged bytes, and ordinary dense training can replace almost every tensor chunk. Atomic manifests plausibly repair ancestry, but validity repair alone does not demonstrate better final model quality under the joint resource limits.

Grade: PARTIAL. Saving complete distributed states is well documented; the load-bearing bridge from safe storage to superior scientific exploration is not. A small full-copy beam could still saturate the task, but that requires an actual campaign comparison rather than citing checkpoint APIs.

## 3. Research done now
- `--resume-step` rollback re-saves into the abandoned run's `step-N` and does not survive a restart — pytorch/torchtitan, 2026 — https://github.com/pytorch/torchtitan/issues/6064 — fetched — Confirms the lineage incident motivating this card; it does not establish a storage-dependent learning advantage.
- wdCP: Windowed Incremental Checkpointing for Efficient and Bounded LLM Recovery — Wendi Cheng et al., 2026 — https://shujiehan.github.io/_pages/files/cf26.pdf — fetched — Reports optimizer-delta buffering, bounded replay and substantial checkpoint reduction; it raises the threat beyond naive byte dedup, but arbitrary branching and complete optimizer lineage need separate verification.
- ByteCheckpoint: A Unified Checkpointing System for Large Foundation Model Development — Borui Wan et al., 2025 — https://www.usenix.org/conference/nsdi25/presentation/wan-borui — fetched — Production resharding and lower save/load stalls support a strong persistence floor, without showing which research branches to retain.
- PaperBench: Evaluating AI's Ability to Replicate AI Research — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched — o1/IterativeAgent reaches partial reproduction credit under a twelve-hour protocol, illustrating that runnable research infrastructure does not imply complete experimental validation.
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search — Yutaro Yamada et al., 2025 — https://arxiv.org/html/2504.08066v1 — fetched — Demonstrates autonomous experiment-tree execution, but the fifteen-hour ceiling and human paper selection do not prove storage-constrained, crash-safe campaign optimization.

Searches targeted incremental LLM checkpoints, branch storage and agent experiment management. Search-only recommendations were excluded from the numerical basis.

## 4. Re-estimated attack
All reward forecasts, mixture weights and proposed resource amounts are ESTIMATED. Immutable selection supplies correctness; asynchronous staging could recover 0.16 reward through less idle time. Better cadence/retention could add 0.19, and exact representation/replay plus branch allocation another 0.16. The 0.51 total explicitly assumes those changes improve the best final model, not merely checkpoint throughput. No frozen native-quality anchors currently quantify that conversion.

Use outcomes 0.26/0.52/0.71 with probabilities 0.25/0.45/0.30. These represent safe full copies with little extra exploration, useful bounded retention, and successful storage-aware exploration. Single = 0.065+0.234+0.213 = 0.51, range 0.26–0.71. Bo4 = 0.71−0.19×0.70^4−0.26×0.25^4 = 0.66; pass4 = 1−0.70^4 = 0.76; ub95 = 0.71. Variation comes mainly from whether retained alternatives matter, with learner noise folded into the scenario outcomes. Unlike the old 0.83, this forecast does not assume unchanged-byte sharing remains effective through dense optimizer updates.

## 4A. Demonstrated capability and subfield SOTA
The best directly relevant systems comparisons located are wdCP's 2026 bounded incremental LLM recovery and ByteCheckpoint's industrial foundation-model persistence. Neither reports final research quality for a bounded-storage branching campaign. Their native storage/recovery outcomes should anchor the competent systems floor; R≈1 still needs a legal campaign control that actually learns a better model at the same resources.

PaperBench's o1/IterativeAgent result is 24.4% rubric credit with twelve hours and one A10. It supports partial infrastructure integration, while leaving transactional branch recovery and value-sensitive eviction untested. AI Scientist-v2 uses Claude 3.5 Sonnet code generation with GPT-4o feedback, experiment-tree search and a fifteen-hour campaign cap; accelerator count is not established in the fetched protocol. One of three selected workshop submissions was accepted. That is evidence of experiment branching, not autonomous invention and verification of a new checkpoint runtime.

KNOWN-RECIPE covers immutable manifests, staging and bounded replay. AGENT-DEMONSTRATED does not cover their combination with scientifically useful branch retention under this contract; attack_basis=LITERATURE-ONLY. The agent must establish recovery correctness and exploit saved resources before its twelve-hour window closes. This creates a large insight-dependent spread: most safe managers deliver little additional learning, while finding a valuable retained loser can change the campaign outcome. Anchored ESTIMATED atoms 0.12/0.37/0.70 with probabilities 0.30/0.55/0.15 give single 0.34, range 0.12–0.70; bo4 = 0.70−0.33×0.85^4−0.25×0.30^4 = 0.53; pass4 = 1−0.85^4 = 0.48; ub95 = 0.70. The retention-success probability is assumed, not a measured benchmark conversion.

## 5. Verdict under the kill lines
The evidence-only stress estimate remains CUT on bo4 and pass4. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL, with pass4 only ESTIMATED 0.02 below its boundary. The newly fetched delta-checkpoint result strengthens the available recipe, but no agent demonstration closes the final-model-quality gap. Retention matters only if a conventional beam measurably loses useful continuations.

## 6. Redesign
Class a; REDESIGNABLE. Ship a correct immutable DCP branch manager and expose its full storage accounting. Use real curriculum or regularization continuations whose early validation rankings sometimes reverse, with public matched examples and sufficient budget to complete several scientifically meaningful continuations. Allow exact replay/deltas and charge reconstruction; score eventual held-out quality, not branch count or storage compression. Precommit a storage envelope derived from measured complete state sizes, and require the reference to beat full-copy beams and wdCP-style replay at equal cost.

A transactional manager plus asynchronous deltas, conventional beam selection and checkpoint-cadence search remains the strongest lawful recipe. It cannot decide which initially inferior continuation to preserve merely by deduplicating bytes. ESTIMATED LITERATURE-ONLY re-attack: 0.18/0.40/0.64 with probabilities 0.28/0.65/0.07 gives single 0.36, bo4 = 0.64−0.24×0.93^4−0.22×0.28^4 = 0.46, pass4 = 1−0.93^4 = 0.25, ub95 = 0.64. Residual risk is that greedy retention works or all branches fit cheaply, in which case the proposed research residual disappears. Decisive check ESTIMATED: 1B model, four policies×three seeds×six hours×four H100 = 288; recovery/lineage audits 32 and evaluation 32; total 352 H100-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: independent storage-aware campaign agents). Grader noise UNMEASURED (planned: repeated fixed-policy training with paired kill schedules). Score ladder UNMEASURED (planned: safe full copies, bounded beam, exact replay, retention-aware reference and stronger control).

## Audit record
id: C075
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.83
old_bo4: 0.90
old_pass4: 0.99
old_ub95: 0.98
new_single: 0.51
new_single_range: 0.26-0.71
new_bo4: 0.66
new_pass4: 0.76
new_ub95: 0.71
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Start from safe persistence and test quality-sensitive ancestry retention against full-copy and exact-replay beams.
redesign_single: 0.36
redesign_bo4: 0.46
redesign_pass4: 0.25
redesign_ub95: 0.64
redesign_gpuh: 352
attack_basis: LITERATURE-ONLY
demonstrated_ref: PaperBench, o1 IterativeAgent, 2025; AI Scientist-v2, Claude 3.5 Sonnet GPT-4o, 2025
gap_to_attack: validated storage-aware branch selection improves final learner quality
subfield_sota_ref: wdCP bounded recovery, Cheng et al., 2026; ByteCheckpoint, Wan et al., 2025
anchored_single: 0.34
anchored_bo4: 0.53
anchored_pass4: 0.48
anchored_ub95: 0.70
anchored_verdict: CONDITIONAL
anchored_binding_line: pass4>0.50
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
