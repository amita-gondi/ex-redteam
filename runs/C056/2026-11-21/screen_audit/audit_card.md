# C056 — Search that learns executable query rewrites for codebases — screen audit
## 1. What the screen claimed
The screen's combined attack used static retrieval, runtime discrimination of dispatch paths and trajectory fine-tuning for a learned inspector. It assigned ESTIMATED single/bo4/pass@4/ub95=0.48/0.57/0.35/0.71 and CONDITIONAL, with an empty kill-category field, because tracing costs and mechanism generalization were unspecified. Its cited URLs:
- https://arxiv.org/abs/2303.12570
- https://arxiv.org/abs/2405.15793

## 2. Evidence audit
RepoCoder supports iterative repository retrieval, not runtime specialization diagnosis. SWE-agent demonstrates navigation and execution feedback, but does not show learning an inspector whose findings causally improve a fixed agent's ML optimization. The old attack's data-generation, learning and downstream-repair stages consequently rest on extrapolation.

Grade: PARTIAL. Existing coding interfaces make the static/executable inspection route credible. They do not establish the dependent chain from a diagnostic trace, through policy training on limited authorized trajectories, to useful changes on an unseen dispatch mechanism. Stronger kernel agents now supply relevant execution evidence, but do not erase this distinction.

## 3. Research done now
All reward values and future compute envelopes in this audit are ESTIMATED; no codebase was benchmarked or trained.
- RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation — Fengji Zhang et al., 2023 — https://arxiv.org/abs/2303.12570 — fetched — supports finding relevant source context; says little about observing the kernel selected at runtime.
- SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering — John Yang et al., 2024 — https://arxiv.org/abs/2405.15793 — fetched — establishes execution-enabled repair interfaces; the inspector-training and ML-speedup target are absent.
- SWE-smith: Scaling Data for Software Engineering Agents — John Yang et al., 2025 — https://arxiv.org/abs/2504.21798 — fetched — execution-grounded trajectory training works at substantial data scale, raising feasibility while exposing the cost of assuming a quick training recipe.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al., PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — profiling and validation support executable inspection, but benchmark kernels differ from inherited dynamic code generators.
- CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation — Weinan Dai et al., 2026 — https://arxiv.org/abs/2602.24286 — fetched — trained kernel generation is powerful; the opened abstract supplies no comparable twelve-hour inspector-learning experiment.

## 4. Re-estimated attack
The attacker first installs static call-path retrieval and ordinary profiling; it uses contrasting shapes, dtypes and cache states to distinguish dispatch hypotheses. Only trajectories that change a downstream repair outcome train the policy. On a competent path, ESTIMATED 0.14 comes from source-path localization, 0.19 from discriminating runtime probes and 0.17 from delivering actionable evidence to the fixed researcher: ESTIMATED 0.50 total. These are utility hypotheses conditional on actual repairs, not rewards for trace counts. Blanket tracing and an untrained execution agent must be included in the floor.

Use ESTIMATED states 0.29/0.50/0.66 with probabilities 0.25/0.60/0.15, representing nontransferring probes, useful ordinary inspection and learned transfer. ESTIMATED single=0.25×0.29+0.60×0.50+0.15×0.66=0.47, range 0.29–0.66. ESTIMATED bo4=0.29+0.21(1−0.25^4)+0.16(1−0.85^4)=0.58. ESTIMATED pass@4=1−0.85^4=0.48; ESTIMATED ub95=0.66. The old mean is approximately retained, but its small pass probability and high bound did not follow an explicit distribution. Here successful transfer produces the tail, rather than an arbitrary offset.

## 4A. Demonstrated capability and subfield SOTA
The closest kernel SOTA inspected is CUDA Agent, reporting faster-than-torch.compile rates of 100%, 100% and 92% on KernelBench levels one through three. Those rates are not downstream repair reward. The eventual reference must beat mature static analysis, profilers and execution agents on actual ML outcomes; no published score anchors R≈1 for a learned dispatch inspector consumed by a different frozen researcher.

Demonstrated result one: KernelAgent's authored orchestration system reports correctness on all 250 KernelBench tasks and average 1.56× speedup over default torch.compile on its level-one evaluation. It uses H100 profiling; the fetched report does not establish a fixed model version or a twelve-hour end-to-end construction budget. Demonstrated result two: SWE-smith trains SWE-agent-LM-32B using execution-grounded synthetic tasks and reports 40.2% pass@1 on SWE-bench Verified. Its dataset spans 50k tasks; the fetched abstract does not give total training hours or accelerator counts. This supports learning from executable trajectories, while making a tiny-data, twelve-hour transfer claim substantially weaker.

KNOWN-RECIPE covers tracing, profiling and trajectory imitation. AGENT-DEMONSTRATED does not cover autonomously creating the training corpus, adapting the inspector and validating its contribution through another agent on new generators. attack_basis=LITERATURE-ONLY. CUDA Agent's substantial pretraining cannot be treated as an episode-budget recipe.

ANCHORED ESTIMATED outcomes 0.18/0.42/0.67 at probabilities 0.28/0.66/0.06 reflect failed training integration, helpful ordinary probes and rare transferable inspection. The upper mode is separated because policy learning must improve another agent's repairs, not merely trace familiar shapes. ESTIMATED single=0.28×0.18+0.66×0.42+0.06×0.67=0.37, range 0.18–0.67; bo4=0.18+0.24(1−0.28^4)+0.25(1−0.94^4)=0.47; pass@4=1−0.94^4=0.22; ub95=0.67. Downstream training variance remains an unmeasured calibration problem. The forecast assumes independent restarts and a useful normalized reserve.

## 5. Verdict under the kill lines
Section 4 gives CONDITIONAL, with ESTIMATED pass@4 approximately 0.02 below its line. The ANCHORED verdict stays CONDITIONAL, UNCHANGED, despite numerical margins of ESTIMATED 0.33/0.13/0.28/0.08 for single/bo4/pass4/ub95. The condition is scientific: establish reserve over blanket tracing and an executable end-to-end interface. Agent results do not show this complete dependent learning chain, so lower scores cannot certify an underspecified environment. The anchored verdict rests on transfer assumptions and unresolved anchors.

## 6. Redesign
Cause class (a), ordinary inspection infrastructure, is potentially fixable. REDESIGNABLE. Freeze the exact runtime-inspection API and charge trace collection, compilation and downstream repair against the same ledger. Use private dispatch dependencies where two plausible source explanations require different executable probes, with equivalent development coverage. Expose all legitimate source and diagnostics. Include exhaustive tracing and fixed profiler-driven repair in the floor, then shuffle inspector findings to verify that learned evidence actually causes a better downstream outcome.

The strongest re-attack trains from successful contrastive probes and uses a model-free trace search when confidence falls. It should fall short only if selecting interventions transfers beyond enumerated profiling states, not because filenames are obfuscated. ESTIMATED states 0.22/0.40/0.62 with probabilities 0.30/0.63/0.07 give single=0.36, bo4=0.22+0.18(1−0.30^4)+0.22(1−0.93^4)=0.45, pass@4=0.25, ub95=0.62. Basis LITERATURE-ONLY. Main risk: blanket instrumentation may already dominate; if so, eliminate this task instead of restricting useful tools.

ESTIMATED pilot GPU-h: 4B inspector, four methods × three seeds × six H100-hours adaptation=72; 8B trajectory teacher=24; downstream 1B training or 8B inference subjects, four methods × three seeds × six hours=72; independent grading and trace overhead=24. Total ESTIMATED 72+24+72+24=192 H100-GPU-h.

## 7. Measurement status
Rollouts UNMEASURED (planned: full learned-inspection searches on fresh generators). Grader noise UNMEASURED (planned: repeat fixed findings with paired downstream agents and learner seeds). Score ladder UNMEASURED (planned: source retrieval, static analysis, exhaustive tracing, selective learned probes and stronger verified repair).

## Audit record
id: C056
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.48
old_bo4: 0.57
old_pass4: 0.35
old_ub95: 0.71
new_single: 0.47
new_single_range: 0.29-0.66
new_bo4: 0.58
new_pass4: 0.48
new_ub95: 0.66
new_verdict: CONDITIONAL
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Freeze charged executable inspection and demonstrate causal downstream gains over exhaustive tracing.
redesign_single: 0.36
redesign_bo4: 0.45
redesign_pass4: 0.25
redesign_ub95: 0.62
redesign_gpuh: 192
attack_basis: LITERATURE-ONLY
demonstrated_ref: KernelAgent, model unspecified, 2026; SWE-smith, SWE-agent-LM-32B, 2025
gap_to_attack: learned probing transfers through a fixed researcher to real ML repairs
subfield_sota_ref: KernelBench fast rates 100/100/92, CUDA Agent Dai et al., 2026
anchored_single: 0.37
anchored_bo4: 0.47
anchored_pass4: 0.22
anchored_ub95: 0.67
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
