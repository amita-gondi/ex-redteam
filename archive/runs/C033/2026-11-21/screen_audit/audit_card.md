# C033 — Inference placement under asymmetric interconnect failures — screen audit
## 1. What the screen claimed
The proposed attack scanned directional links and collectives, fitted communication costs, enumerated placements and validated survivors under serving traffic. ESTIMATED single/bo4/pass@4/ub95 were 0.78/0.85/0.96/0.97; CUT, category SYS, followed from stable asymmetry being cheaply measurable. Its source URLs were:
- https://github.com/NVIDIA/nccl-tests
- https://arxiv.org/abs/2302.11665
- https://arxiv.org/abs/2111.04867

## 2. Evidence audit
NCCL tests provide measurement machinery, not evidence that a complete scan amortizes in this service horizon. AlpaServe supports model-parallel placement under variable demand; TACCL demonstrates topology-specific collectives but relies on designer communication sketches and principally evaluates training. Grade: PARTIAL: placement and collective optimization are real, while identifying impaired directional paths, installing a compatible plan and recovering most net utility within the allotted research budget were not established by those citations.

## 3. Research done now
- NCCL Tests — NVIDIA, 2026 repository state — https://github.com/NVIDIA/nccl-tests — fetched — Correctness and performance tests make message-size-sensitive collective probing readily available. This raises the measurement attack, without resolving total discovery cost.
- AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving — Zhuohan Li et al., 2023 — https://arxiv.org/abs/2302.11665 — fetched — Measured placement gains support searching parallel configurations, but its burst multiplexing objective does not validate faulty-path diagnosis.
- TACCL: Guiding Collective Algorithm Synthesis using Communication Sketches — Aashaka Shah et al., 2021, revised 2022 — https://arxiv.org/abs/2111.04867 — fetched — Synthesis outperforms standard collectives on tested topologies. Designer sketches and deployment integration limit the inference that an unaided researcher can apply it to arbitrary damaged routes.
- HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment — Youhe Jiang et al., 2025 — https://arxiv.org/abs/2502.07903 — fetched — Graph partitioning and flow optimization are evaluated on heterogeneous-network model serving. This directly strengthens the alternative to symmetric placement, though its topology inputs are not the outcome of this card's paid experiments.
- Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads — Tianxi Lu and Sherief Reda, 2026 — https://arxiv.org/html/2607.22242v1 — fetched — A monitored language-model scheduler reaches optimal mappings in its small heterogeneous-tool scenarios. The careful reprobing design is evidence for measurement-driven adaptation, not proof of directional collective diagnosis at serving scale.

## 4. Re-estimated attack
ESTIMATED opportunity decomposition: 0.30 identifying stable slow routes, 0.40 selecting placements and 0.30 minimizing probe/switch overhead. Recovering ESTIMATED fractions 0.95/0.80/0.47 gives 0.30×0.95+0.40×0.80+0.30×0.47=0.75. This assumes lawful access to directional probes and sufficiently persistent topology; it charges every failed placement and changes no output semantics.

For the literature recipe, use ESTIMATED R=0.53/0.74/0.85 with probabilities 0.15/0.50/0.35. The low state is a poorly amortized scan, the middle a sound measured placement, and the upper a well-pruned search. ESTIMATED single=0.15×0.53+0.50×0.74+0.35×0.85=0.75, range 0.53–0.85. ESTIMATED bo4=0.85−0.11×0.65^4−0.21×0.15^4=0.83; p=0.85 implies pass@4=1−0.15^4=1.00 rounded; ub95=0.85. Workload persistence and probe quality create spread, with negligible scorer randomness assumed rather than measured. Compared with the old forecast, uncertain amortization removes some mean and much of its extreme upper tail.

## 4A. Demonstrated capability and subfield SOTA
The closest subfield north star is HexGen-2's resource-matched heterogeneous inference placement, supplemented by TACCL where collective replacement is authorized. Deploy that family as the reference instead of assuming a symmetric grid. None of the fetched work establishes R≈1 after paying for unknown-fault discovery; an attained cost-inclusive controller is still needed to anchor the top reward.

Two agent results provide different pieces:
- Lu and Reda's fetched 2026 Agentic CPU-GPU Scheduling study above uses DeepSeek-R1-Distill-Qwen-32B-AWQ with runtime-monitor feedback, separate A5500 GPUs for scheduler and tools, and bounded scheduling rounds. It reports optimal mappings across its scenarios, but no twelve-hour development trial. The scaffold is human-built and the placement space is much smaller than model-parallel route search.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou, Krish Agarwal and collaborators, 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Opus 5.5+Claude Code exceeded the Dynamo/KAI cluster reference in four hours on sixteen GB300s. This supports empirical placement tuning; damaged directional collectives and paid topology identification remain absent.

KNOWN-RECIPE evidence is strong for stable heterogeneous graphs. The closest AGENT-DEMONSTRATED results cover monitor-guided mapping and cluster control, but not the combined diagnosis interface. attack_basis=LITERATURE-ONLY; the forecast assumes transfer, rather than claiming an observed solve. A researcher must still discover which collective measurements predict full service and avoid wasting the service horizon on validation.

ANCHORED ESTIMATED distribution: 0.39/0.58/0.72 at probabilities 0.20/0.60/0.20. These represent partial topology integration, ordinary measured placement and successful efficient diagnosis. ESTIMATED mean=0.20×0.39+0.60×0.58+0.20×0.72=0.57, range 0.39–0.72. ESTIMATED bo4=0.72−0.14×0.80^4−0.19×0.20^4=0.66; pass@4=1−0.80^4=0.59 with p=0.20; ub95=0.72. Repeated independent attempts can find a good plan despite a moderate average, which is why the verdict does not follow single alone.

## 5. Verdict under the kill lines
Evidence-only CUT, ESTIMATED bo4=0.83; ANCHORED CUT, UNCHANGED from the screen. The anchored bo4 breach is ESTIMATED 0.06 and pass@4 breach 0.09. The decisive distinction is a tail-based saturation hypothesis supported by neighboring scheduling demonstrations, not the screen's claim of nearly automatic integration. This CUT rests on the explicit transfer assumption; measuring discovery amortization could reverse it. Its ub95 remains ESTIMATED 0.03 below that separate line.

## 6. Redesign
Cause (b): direct experimental search over stable placements. REDESIGNABLE by replacing a fixed defective graph with a disclosed, workload-dependent contention mechanism: prefill transfers, decode collectives and colocated jobs share actual links, and an intrusive bandwidth probe changes queue occupancy. Expose routing, live counters, background-job descriptors and realistic development histories. Score verified output over complete discovery plus service time; charge migrations and drain costs. A useful controller must learn which low-impact observations distinguish competing interference explanations and then choose placement jointly with communication scheduling.

Full scans, HexGen-style optimization, TACCL-generated routes and robust bandit placement remain legal and belong in the comparison. They lose their universal advantage when isolated bandwidth does not predict simultaneous flows and their measurements perturb queues. This is a real cluster-utilization problem, not hidden fault rules or random timing noise. Before retention, an adaptive control must beat a competent queue-aware model-predictive baseline on the same feasible load.

Redesign basis=LITERATURE-ONLY. ESTIMATED R states 0.26/0.46/0.67 with probabilities 0.50/0.42/0.08 represent conservative fallback, useful contention fitting and rare successful active diagnosis. ESTIMATED single=0.38, range 0.26–0.67, from 0.50×0.26+0.42×0.46+0.08×0.67; bo4=0.67−0.21×0.92^4−0.20×0.50^4=0.51; pass@4=1−0.92^4=0.28; ub95=0.67. Risk remains that ordinary queueing models and short reprobes solve the full mechanism, or that perturbation creates unmanageable nondeterminism rather than research headroom.

Decisive-check allocation ESTIMATED: a 32B subject on four H100s, five probe/placement arms, three independent topology-traffic seeds, 1.50 hours each gives 5×3×1.50×4=90.00 GPU-h. ESTIMATED exact-output replay and contention reproducibility add 18.00+12.00, totaling 120.00 H100 GPU-h. This tests falsifiability before a larger frontier panel.

## 7. Measurement status
Rollouts UNMEASURED (planned charged topology plans on real collective paths). Grader noise UNMEASURED (planned repeat traffic replays and cost-meter reconciliation). Score ladder UNMEASURED (planned symmetric placement, complete scan, pruned topology optimizer and feasible adaptive control).

## Audit record
id: C033
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.78
old_bo4: 0.85
old_pass4: 0.96
old_ub95: 0.97
new_single: 0.75
new_single_range: 0.53-0.85
new_bo4: 0.83
new_pass4: 1.00
new_ub95: 0.85
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Jointly choose minimally intrusive topology measurements and placement under disclosed traffic-dependent link contention.
redesign_single: 0.38
redesign_bo4: 0.51
redesign_pass4: 0.28
redesign_ub95: 0.67
redesign_gpuh: 120
attack_basis: LITERATURE-ONLY
demonstrated_ref: Agentic CPU-GPU Scheduling, DeepSeek-R1-Distill-Qwen-32B-AWQ plus monitor, 2026; Singularity-Bench, Opus 5.5 plus Claude Code, 2026
gap_to_attack: paid directional-fault diagnosis is untested
subfield_sota_ref: HexGen-2 heterogeneous-network inference placement, Jiang et al., 2025
anchored_single: 0.57
anchored_bo4: 0.66
anchored_pass4: 0.59
anchored_ub95: 0.72
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
