# C072 — Crash-consistent experience buffers that preserve learning — screen audit
## 1. What the screen claimed
The old attack combined an append-only rollout journal, atomic learner/queue commit, asynchronous writes, backpressure, bounded queues and age-aware admission. CUT/SYS had ESTIMATED single 0.78, best-of-four 0.87, pass@4 0.97 and upper-95% 0.96, because complete text-rollout persistence might be cheap enough to erase the supposed selection problem. It cited these URLs:
- https://www.sqlite.org/atomiccommit.html
- https://docs.nvidia.com/nemo/rl/latest/guides/single-controller.html
- https://docs.nvidia.com/nemo/rl/latest/guides/async-grpo.html

## 2. Evidence audit
SQLite supports transactional durability principles, while NeMo documents coordinated replay/controller state and restoration. Those are stronger leads than a weights-only checkpoint, but documentation does not measure crash-conditioned policy utility, and serializing a queue is not the same as preserving a distributed tool episode. The screen offered no storage profile proving either that full persistence is costly or that it wins cheaply. Grade: PARTIAL, with conventional correctness substantially supported and learning-value selection untested.

## 3. Research done now
Search examined replay-buffer state, contemporary fault-tolerant agentic RL and architecture-dependent recovery costs. All sources listed were opened; card scores and future compute allocations are ESTIMATED.
- Atomic Commit In SQLite — SQLite project, undated documentation, fetched 2026 — https://www.sqlite.org/atomiccommit.html — fetched — atomic multi-file reasoning supports a consistent checkpoint frontier; it does not choose which trajectories deserve storage.
- Train with Single-Controller (Async GRPO and PPO) — NVIDIA NeMo-RL, 2026 snapshot — https://docs.nvidia.com/nemo/rl/latest/guides/single-controller.html — fetched — complete controller/replay snapshots make wholesale replacement a serious lawful baseline.
- Train with Async GRPO — NVIDIA NeMo-RL, 2026 snapshot — https://docs.nvidia.com/nemo/rl/latest/guides/async-grpo.html — fetched — explicit buffer restoration and trajectory-age controls support a practical bounded-queue recipe.
- Checkpointing — TorchRL/PyTorch, 2026 snapshot — https://docs.pytorch.org/rl/main/reference/checkpoint.html — fetched — writer cursors, sampler priorities and storage are persisted together, while worker/environment state has stated limits; this strengthens ordinary buffer repair but cautions against assuming full-episode recovery.
- Belayer: Efficient Fault Tolerance for LLM Agentic RL Training — Jiecheng Zhou et al., 2026 — https://arxiv.org/abs/2608.14635 — fetched — directly demonstrates recovery of rollout workers and stateful containers, expanding the attack beyond text journaling.
- FailBench: Evaluating Fault Tolerance Across Distributed Training Architectures — Khaled Aljbab and Amine Barrak, 2026 — https://arxiv.org/abs/2610.07688 — fetched — measured mechanisms have architecture-dependent costs and throughput can improve without better loss progress, weakening a universal cheap-persistence claim.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — autonomous RL and orchestration systems demonstrate integration ability, but no injected crash/recovery objective appears in those tasks.
- GPT-6.2 System Card, research debugging — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — supports finding hidden-state bugs from code/logs, without demonstrating distributed durability validation.

## 4. Re-estimated attack
In a strong known-recipe scenario, ESTIMATED 0.35 of provisional utility comes from complete queue/checkpoint reconciliation, ESTIMATED 0.17 from asynchronous incremental writes, and ESTIMATED 0.12 from queue-depth and age tuning. These represent retained learning per total runtime; acknowledged-but-undurable groups cannot earn restoration credit. Distinguish deliberate, charged discards from silent loss, and reconcile optimizer state with consumption offsets. Text tokens may make full persistence nearly free, whereas tool snapshots can change the balance.

An ESTIMATED outcome distribution places probabilities {0.22,0.53,0.25} on R={0.43,0.65,0.80}. The spread comes from whether storage and replay costs permit full recovery without staleness damage, rather than randomizing the transaction protocol. ESTIMATED single=0.0946+0.3445+0.2000=0.64, range 0.43–0.80. ESTIMATED best-of-four=0.80−0.15×0.75^4−0.22×0.22^4=0.75; p=0.78 implies pass@4=1−0.22^4=1.00; upper-95%=0.80. The old 0.78 mean did not adequately price integration or distinguish recovery speed from learning progress.

## 4A. Demonstrated capability and subfield SOTA
Belayer is the closest fetched frontier agentic-RL recovery system: source-reported worker recovery improves by up to 42× over cold engine start and environment recovery by 1.5–3.5×, using coordinated context/runtime restoration. These are recovery metrics, not autonomous researcher scores. FailBench's more recent cross-architecture measurements prevent treating one recovery method as universally best. Anchor the scientific control to complete NeMo/TorchRL state plus Belayer-compatible environment handling where needed, then measure policy utility under real interruptions. The card's R≈1 selective-persistence advantage is currently UNMEASURED.

Opus 5.5+Claude Code builds Singularity-Bench's cluster orchestrator within four hours on sixteen GB300s, reaching reported score 0.510 versus Dynamo's 0.460 by measuring interference and choosing scheduling/capacity policies. This supports system integration and empirical tuning; it does not demonstrate a crash-consistent learner/queue frontier. GPT-6.2 Astra obtains reported 81.85% average rubric credit on OpenAI research-debugging cases. The vendor does not disclose a comparable runtime or device budget for that evaluation, and identifying a cause in logs is a weaker deliverable than proving durable replay across process death.

KNOWN-RECIPE includes journaling, complete replay snapshots and fault-aware checkpoint scheduling. The sources do not show a frontier research agent autonomously integrating and validating that complete recipe on this learning objective within twelve hours. attack_basis=LITERATURE-ONLY. It must still reconcile all hidden state, exercise actual crash boundaries and run enough continued learning to distinguish stale-but-durable from useful experience.

For the anchored ESTIMATED distribution use R={0.35,0.52,0.69}, probabilities {0.30,0.56,0.14}. ESTIMATED single=0.1050+0.2912+0.0966=0.49, range 0.35–0.69; best-of-four=0.69−0.17×0.86^4−0.17×0.30^4=0.60 (unrounded 0.59563); pass@4=1−0.86^4=0.45; upper-95%=0.69. The high mode requires a verified recovery stack with good learning transfer. Its probability is a desk assumption, not Belayer's measured recovery ratio.

## 5. Verdict under the kill lines
Section 4 says CUT. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL. Best-of-four has less than ESTIMATED 0.01 clearance before rounding, and pass@4 is only ESTIMATED 0.05 below its line. Stronger recovery literature establishes a real attack, but the missing autonomous durability-plus-learning demonstration prevents accepting the screen's high reliability forecast. No rounded 0.60 value is treated as strictly greater than 0.60.

## 6. Redesign
Cause (a), REDESIGNABLE. Extend pending experience to genuine stateful tool episodes whose future rewards require resuming their sandbox state, with documented delayed reward-release processes. Expose storage throughput, current snapshot sizes, episode provenance and legal discard semantics. Use deployment-derived snapshot/compute ratios, not artificial disk throttling. Allow incremental content-addressed snapshots, replication, full checkpointing and explicit regeneration. A complete durable baseline must finish usefully within the same runtime cap.

Reward the learning value retained after interruption, with shared snapshot dependencies coupling which episodes can be preserved cheaply. Include Belayer-style recovery, deduplicated full persistence, age policies and value-based replay in the floor. The strongest re-attack adds a value/cost predictor and standard scheduling search; correctly journaling all text no longer determines which expensive shared state to retain. Its basis is LITERATURE-ONLY on this joint learning problem. ESTIMATED {0.29,0.45,0.66}, probabilities {0.42,0.51,0.07}, yields single=0.40, best-of-four=0.66−0.21×0.93^4−0.16×0.42^4=0.50, pass@4=1−0.93^4=0.25, upper-95%=0.66. Full incremental persistence may still dominate; that is a decisive failure of the redesign, not grounds to ban it. ESTIMATED pilot: 3B policy/reference components, four policies × three seeds × eight hours × four H100s=384; crash replay 48 plus policy evaluation 48 totals 480 H100-h. CPU/storage resources require a separate measured ledger.

## 7. Measurement status
Rollouts UNMEASURED (planned independent recovery/selection research attempts); grader noise UNMEASURED (planned fixed crash histories with separate learner and environment seeds); score ladder UNMEASURED (planned weights-only negative, complete queue restore, incremental persistence, stateful recovery and selective durability).

## Audit record
id: C072
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.78
old_bo4: 0.87
old_pass4: 0.97
old_ub95: 0.96
new_single: 0.64
new_single_range: 0.43-0.80
new_bo4: 0.75
new_pass4: 1.00
new_ub95: 0.80
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Allocate durability to shared stateful tool episodes with delayed learning value above complete incremental recovery controls.
redesign_single: 0.40
redesign_bo4: 0.50
redesign_pass4: 0.25
redesign_ub95: 0.66
redesign_gpuh: 480
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench orchestration, Opus 5.5+Claude Code, 2026; Internal Research Debugging, GPT-6.2 Astra, 2026
gap_to_attack: crash-validated distributed replay with continued policy utility
subfield_sota_ref: Belayer agentic-RL recovery, Zhou et al., 2026; FailBench, Aljbab and Barrak, 2026
anchored_single: 0.49
anchored_bo4: 0.60
anchored_pass4: 0.45
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
