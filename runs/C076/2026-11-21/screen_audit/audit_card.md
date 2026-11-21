# C076 — Adapter checkpoints whose reported training gains survive reload — screen audit

## 1. What the screen claimed
The old attack replaced export with a mature adapter serializer, enumerated all required state, staged CPU chunks and checked clean-process parity. Its ESTIMATED single/bo4/pass4/ub95 were 0.95/0.98/0.99/1.00; CUT, category SYS, because faithful independent export appeared to construct almost the entire solution despite the unverified incident body.

Screen URLs, fetched this session:
- PEFT checkpoint format — Hugging Face, 2026 accessed repository — https://github.com/huggingface/peft/blob/main/docs/source/developer_guides/checkpoint.md
- Troubleshooting — Hugging Face, 2026 accessed documentation — https://huggingface.co/docs/peft/developer_guides/troubleshooting

## 2. Evidence audit
PEFT explains adapter/config serialization and reload pitfalls, including state outside the low-rank matrices. That supports a complete-state checklist, but provides no measurement of this TorchTitan distributed exporter, its peak memory or the normalized benefit over a working independent exporter. Chunked staging is a reasonable engineering route, not evidence of almost-certain full reward.

Grade: PARTIAL. The validity recipe is mature; scientific headroom and autonomous incident resolution remain unestablished. The issue's body is still unverified after a direct fetch failure, so no mechanism-specific claim about its cause enters this audit. An indexed title is not a reproduced failure.

## 3. Research done now
- Issues, including SLAKE LoRA recipes crash at the final checkpoint save on 8 GB300 — pytorch/torchtitan, 2026 — https://github.com/pytorch/torchtitan/issues — fetched — Confirms that an incident is indexed; its individual body could not be retrieved and supplies no trustworthy diagnosis here.
- TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — GLM-5.2's planning/decoupling system completes bounded post-training, raising confidence in producing trained deliverables; no VLM exporter repair is reported.
- More reliable scores and verdicts, PostTrainBench v1.2 — PostTrainBench team, 2026 — https://posttrainbench.com/blog/posttrainbench-1-2/ — fetched — Gives independently evaluated trained-model results and documents scoring fixes, tempering any inference from a single apparent successful save.
- PostTrainBench — AISA group, 2026 — https://posttrainbench.com/ — fetched — The ten-hour, one-H100 delivered-model protocol is a relevant autonomy comparator, although it does not exercise multimodal processor dependencies.

Search included the exact incident identifier and agent save/reload evidence. Direct issue-body access was attempted but failed; that failed URL is deliberately not presented as a verified source.

## 4. Re-estimated attack
All scores, scenario frequencies, ranges and resource costs below are ESTIMATED. A full tensor/config map and reload audit could recover 0.31 of provisional utility if the inherited exporter loses trained state. Bounded staging could add 0.15 by preventing memory failures, with save/shard tuning adding 0.12. The 0.58 sum is conditional on those deficits existing; if a mature exporter is already the floor, those same repairs earn no gain. This unresolved anchor is the largest uncertainty, not tiny serialization rounding error.

Use outcomes 0.34/0.61/0.73 with probabilities 0.20/0.55/0.25. They distinguish an incomplete architecture mapping, faithful but ordinary export, and a profitable pressure-aware path. Single = 0.068+0.3355+0.1825 = 0.59, range 0.34–0.73. Bo4 = 0.73−0.12×0.75^4−0.27×0.20^4 = 0.69. Here p=0.80, because both upper modes exceed 0.60; pass4 = 1−0.20^4 = 1.00 rounded, not certainty. Ub95 = 0.73. These are lower than the old estimates because the old screen priced a generic fix as nearly all attainable research value.

## 4A. Demonstrated capability and subfield SOTA
The verified field reference is PEFT's complete adapter artifact contract, rather than a published leaderboard for exact export cost. No universal export SOTA was established. A legal north star must preserve the same trained behavior with lower complete train/save/reload cost than the best working independent exporter; its R≈1 placement cannot be inferred from medical-task accuracy or a documentation example.

TrainExplorer/GLM-5.2 reports a 39.02 aggregate under ten hours on one 80GB flagship GPU, versus 31.70 with the same model in Claude Code. Its subject models span roughly 1.7B–4B; it does not expose a VLM save-repair trajectory. PostTrainBench v1.2 places Opus 5.5 at 43.8% using Claude Code under the benchmark's ten-hour/one-H100 protocol. This confirms learned model delivery, but neither establishes exact parity repair across fresh adapter architectures, processor state and distributed export. These are two agent results, not two proofs of C076 success.

KNOWN-RECIPE is well established for ordinary complete export. AGENT-DEMONSTRATED transfer stops short of this combined incident, so basis=LITERATURE-ONLY. An agent must still identify all architecture state and validate the actual memory-bound delivery path within twelve hours. Anchored ESTIMATED atoms 0.32/0.51/0.66, probabilities 0.20/0.66/0.14, yield single 0.49, range 0.32–0.66; bo4 = 0.66−0.15×0.86^4−0.19×0.20^4 = 0.58; pass4 = 1−0.86^4 = 0.45; ub95 = 0.66. Numerical transfer and the existence of useful headroom remain assumptions.

## 5. Verdict under the kill lines
Section 4: CUT, particularly bo4 and pass4. ANCHORED verdict: CONDITIONAL, FLIPPED CUT→CONDITIONAL; the ESTIMATED bo4 margin is only 0.02. The strongest positive evidence is actual bounded model delivery, while missing VLM incident and memory-path demonstrations prevent a high-confidence saturation claim. This condition does not certify an unreproduced task: incident verification and a genuine cost frontier are prerequisites.

## 6. Redesign
Class a; REDESIGNABLE. Begin with a reproduced, already repaired save path and a faithful PEFT-compatible independent exporter. Make the research target overlap-safe streaming export during real multimodal adapter training across declared shard layouts and trainable side modules. Publish state schemas and memory budgets, keep an ordinary pause-and-save path feasible, and score extra useful learning achieved after all final exports and cold reloads complete. Development includes the same layout and pressure mechanisms as final workloads.

The combined name-mapping, CPU-staging and shard-size sweep is still legal, but no longer earns credit for restoring baseline behavior; it must solve contention between live training, staging and complete artifact production. ESTIMATED LITERATURE-ONLY re-attack outcomes 0.24/0.46/0.64 with probabilities 0.25/0.66/0.09 give single 0.42, bo4 = 0.64−0.18×0.91^4−0.22×0.25^4 = 0.52, pass4 = 1−0.91^4 = 0.31, ub95 = 0.64. A standard asynchronous exporter could erase the reserve, so compare it before retention. Decisive-check GPU-h ESTIMATED: 3B VLM, four export strategies×three seeds×three hours×two H100 = 72; reload, peak-memory and held-out evaluation overhead 24; total 96 H100-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: after pinned failure verification, timed exporter agents). Grader noise UNMEASURED (planned: repeated cold reload of identical adapters plus paired task evaluation). Score ladder UNMEASURED (planned: repaired exporter, independent complete serializer, streaming staging and attainable concurrent-export control).

## Audit record
id: C076
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.95
old_bo4: 0.98
old_pass4: 0.99
old_ub95: 1.00
new_single: 0.59
new_single_range: 0.34-0.73
new_bo4: 0.69
new_pass4: 1.00
new_ub95: 0.73
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize faithful concurrent streaming export above repaired independent serializers under disclosed training and memory contention.
redesign_single: 0.42
redesign_bo4: 0.52
redesign_pass4: 0.31
redesign_ub95: 0.64
redesign_gpuh: 96
attack_basis: LITERATURE-ONLY
demonstrated_ref: TrainExplorer, GLM-5.2, 2026; PostTrainBench v1.2, Opus 5.5 Claude Code, 2026
gap_to_attack: VLM state enumeration and pressure-safe exact export repair
subfield_sota_ref: complete PEFT adapter export contract, Hugging Face, 2026 accessed
anchored_single: 0.49
anchored_bo4: 0.58
anchored_pass4: 0.45
anchored_ub95: 0.66
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
