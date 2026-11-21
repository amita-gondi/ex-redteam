# C094 — Keep improving the worst-conditioned training phase — screen audit
ANCHORED headline: CONDITIONAL, flipped from CUT; ESTIMATED best-of-four rounds to 0.60.
## 1. What the screen claimed
The screen proposed full-run profiling, critical-path ranking, asynchronous checkpoints, shape prewarming and checkpoint-local transition replay. ESTIMATED single 0.75, bo4 0.84, pass@4 0.96 and ub95 0.95 yielded CUT, category SYS: rare bottlenecks seemed cheaply observable with standard tooling. Its URLs were:
- https://docs.pytorch.org/docs/stable/profiler
- https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html
- https://github.com/pytorch/torchtitan/blob/main/docs/checkpoint.md

## 2. Evidence audit
Profiler and distributed-checkpoint documentation establish available mechanisms, without demonstrating complete time-to-quality improvement across changing curricula. The specific TorchTitan checkpoint URL returns 404 in this session; its asserted document is unverified and supplies no support. Most importantly, local replay of an inherited state does not necessarily predict how an earlier optimization changes the state or learning regime reached later. Grade PARTIAL: the systems pieces are mature, but their autonomous phase-allocation combination was assumed to work.

## 3. Research done now
- *torch.profiler* — PyTorch, versioned documentation inspected 2026, original publication year unspecified — https://docs.pytorch.org/docs/2.15/profiler.html — fetched — verifies complete-event tracing tools, while making no claim about an agent recognizing future learning bottlenecks.
- *Asynchronous Saving with Distributed Checkpoint* — PyTorch, tutorial inspected 2026, initial publication year unspecified — https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html — fetched — supplies a direct durability-overlap baseline that must precede any claim of phase-aware novelty.
- *6x faster Async Checkpointing in PyTorch, using Cached Plans, no GIL contention* — Meta and Crusoe, 2025 — https://pytorch.org/blog/6x-faster-async-checkpointing/ — fetched — real implementation gains strengthen the checkpoint recipe, without converting checkpoint speedup into whole-learning speedup automatically.
- *Checkmate: Zero Performance Overhead Model Checkpointing via Network Gradient Replication* — Ankit Bhardwaj et al., 2026 — https://people.csail.mit.edu/ghobadi/papers/checkmate_nsdi_2026.pdf — fetched — network replication changes the attainable durability frontier; its shadow resources must be charged before treating it as a legal replacement.
- *GPT-6.2 System Card* — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — demonstrates training-time optimization at fixed quality, raising the attack on ordinary phases.
- *AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure* — Megan Kinniment et al./METR, 2026 — https://metr.org/blog/2026-11-20-q4-2026-capability-update/ — fetched — mature NanoGPT optimization remains weaker than top human changes despite much longer agent budgets, limiting confidence in anticipatory phase research.

The broken old checkpoint reference is recorded only as an attempted fetch, not a verified source. Counts: three old links, four new works, six successfully fetched works.

## 4. Re-estimated attack
ESTIMATED score capture is 0.20 from whole-run critical-path selection, 0.18 from checkpoint/compilation fixes and 0.19 from replay-guided phase configuration. Existing fixes included in the competent floor earn no gain twice. Unresolved value is the interaction between earlier allocations, subsequent learning states and the cost of reaching rare transitions.

Use ESTIMATED outcomes {0.35,0.58,0.76}, probabilities {0.20,0.60,0.20}: ordinary fixes reveal little reserve, phase tuning works, or the agent identifies a major coupled improvement. ESTIMATED single = 0.57, range 0.35–0.76; bo4 = 0.76−0.18×0.80^4−0.23×0.20^4 = 0.69; pass@4 = 1−0.80^4 = 0.59; ub95 = 0.76. Discovery of the moving bottleneck, training seed effects and successful restart integration dominate variation. The old estimates treated complete profiling and future-state extrapolation as almost deterministic; neither was shown.

## 4A. Demonstrated capability and subfield SOTA
Checkmate is the strongest fetched durability comparator: it reports per-iteration checkpointing at throughput comparable to no-checkpoint training, using network gradient replication into a CPU shadow cluster. Its resource assumptions differ from plain DCP. PyTorch's cached-plan/process improvements are a more portable baseline. Neither establishes the best full curriculum time-to-quality policy. Anchor the reference to an attained full learning trajectory with charged durability and restart costs, rather than a sum of isolated phase gains; that native reference is UNMEASURED.

Agent evidence one: GPT-6.2 Astra in OpenAI's unnamed NanoGPT scaffold saves 42.87% of baseline time to target quality after two hours on one H100; the best reported human solution saves 72.38%. This directly supports ordinary training optimization, but the evaluation does not establish rare curriculum/restart anticipation. Evidence two: METR's Budget NanoGPT campaigns test models including Opus 5.5, Fable 5.1 and GPT-6 Astra in autonomous scaffolds. The best run, whose model identity is not specified in the cited summary, achieves 15.7% improvement in forty-eight hours on eight H100s with a 250M-token allowance. Its 384 GPU-h envelope and mature starting record differ sharply from the shorter OpenAI test. Neither result supplies a phase-aware allocation trajectory for this card.

KNOWN-RECIPE covers full profiling, async durability and local replay. The combined anticipatory allocation attack is not AGENT-DEMONSTRATED. attack_basis=LITERATURE-ONLY. In twelve hours an agent still must quantify complete-run savings, account for altered learning dynamics and validate quality after restart; the anchored conclusion rests on that assumption.

ESTIMATED anchored states {0.29,0.51,0.70}, masses {0.23,0.63,0.14}, give single 0.49, range 0.29–0.70; bo4 = 0.70−0.19×0.86^4−0.22×0.23^4 = 0.60 after rounding, strictly below its line beforehand; pass@4 = 1−0.86^4 = 0.45; ub95 = 0.70. The nearly binding maximum reflects occasional useful anticipation rather than a fixed mean uplift.

## 5. Verdict under the kill lines
Evidence recipe verdict: CUT through bo4, pass@4 and ub95. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; the unrounded bo4 clearance is less than ESTIMATED 0.01. Actual agent training gains justify a serious threat, but neither those gains nor checkpoint documentation demonstrates solving the rare-phase allocation problem. The condition must distinguish a reusable anticipatory policy from simply enabling mature checkpoint features.

## 6. Redesign
Class (a), with allocation search as a secondary class-(b) route. REDESIGNABLE. Inherit full-run traces, asynchronous checkpointing, prewarming and legal transition replay. Evaluate the submitted allocation policy through a reset optimizer across fresh training campaigns. Earlier data-packing, sharding and representation choices must change later context/curriculum costs and quality, so replaying one inherited checkpoint cannot evaluate all counterfactual histories.

Expose representative causal relationships and all resource costs on dev; do not conceal future shapes or invent surprise failure penalties. Establish a feasible anticipatory reference that decides which counterfactual training branches to fund. Reward complete time to held-out quality after charging every probe and durable recovery. Frontier labs need this capacity when short profiles misprice changes that alter later training.

The redesign's strongest attack combines full profiling, replay, multi-fidelity branch continuation and a learned predictor of future critical paths. Basis LITERATURE-ONLY; cross-history prediction remains undemonstrated. ESTIMATED distribution {0.24,0.45,0.67}, weights {0.28,0.63,0.09}, gives single 0.41, bo4 = 0.67−0.22×0.91^4−0.21×0.28^4 = 0.52, pass@4 = 1−0.91^4 = 0.31, ub95 0.67. Risk remains that a small finite configuration sweep resolves every history cheaply.

ESTIMATED check: 1B learner on four H100s, four allocation policies × two seeds × twelve hours × four H100 = 384 GPU-h; phase probes add 48 GPU-h and final-quality/durability evaluations add 48 GPU-h, totaling 480 H100 GPU-h. This is proposed future measurement only.

## 7. Measurement status
Rollouts UNMEASURED (planned full training-history allocation campaigns). Grader noise UNMEASURED (planned repeated phase timings, learning seeds and cold restores). Score ladder UNMEASURED (planned steady-state, full-profile, replay-guided and anticipatory controls).

The record labels all score projections and proposed check costs ESTIMATED; counts are factual.

## Audit record
id: C094
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.75
old_bo4: 0.84
old_pass4: 0.96
old_ub95: 0.95
new_single: 0.57
new_single_range: 0.35-0.76
new_bo4: 0.69
new_pass4: 0.59
new_ub95: 0.76
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Evaluate anticipatory allocation across counterfactual training histories above complete phase-replay tooling.
redesign_single: 0.41
redesign_bo4: 0.52
redesign_pass4: 0.31
redesign_ub95: 0.67
redesign_gpuh: 480
attack_basis: LITERATURE-ONLY
demonstrated_ref: NanoGPT, GPT-6.2 Astra, 2026; Budget NanoGPT, METR frontier panel, 2026
gap_to_attack: full rare-phase and learning-history anticipation unshown
subfield_sota_ref: Checkmate durability frontier, Bhardwaj, 2026; complete curriculum SOTA unverified
anchored_single: 0.49
anchored_bo4: 0.60
anchored_pass4: 0.45
anchored_ub95: 0.70
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
