# C116: A tool-building curriculum for unfamiliar accelerator DSLs — independent adversarial review

**Verdict: CUT.** The card offers syntax/primitive novelty and curriculum training, but no evidence that a general semantics-probing compiler workflow leaves a research bottleneck. Its final graph-speed reward permits direct tracing, differential testing and schedule search, which can bypass the curriculum's supposed necessity. Keeping the proposed task would require a new grounded compiler-research mechanism rather than a bounded security repair.

Source path: `/workspace/task_ideation_v4_creative/cards/C116.md`.

No accelerator execution, compilation trial or agent training was performed. Reward forecasts are ESTIMATED scenarios, not results. The card identifies the curriculum, trained kernel agent, held-out interpreter, compiler, semantic tests and final ML graphs; it does not name their files or establish an implemented artifact boundary.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Differentially recover primitive semantics | Generate tiny tagged-input kernels, vary lane/group participation and barriers, compare interpreter and compiler outputs, and synthesize a communication wrapper from the observed truth table. | ESTIMATED 0.70–0.96 | No; development explicitly matches interpreter/compiler access. | Run this complete semantics-probing control before training a curriculum; retain every lawful inferred wrapper. | ESTIMATED 0.70–0.96 | A finite primitive family can be learned by tests without teaching a new research skill. |
| Lower through a canonical representation | Parse the unfamiliar syntax, map operators to a common tensor/communication IR, apply known schedules and emit the target DSL; tune only layouts and launch parameters. | ESTIMATED 0.61–0.92 | The missing primitive may complicate lowering, but no semantics prevents it. | Test legal source-to-source lowering with a mature optimization/search backend and a complete communication adapter. | ESTIMATED 0.61–0.92 | Renaming operations or withholding templates does not remove the shared algebra. |
| Synthesize tool-use traces automatically | Use legal compiler failures, interpreter traces and generated correct kernels to produce instrument-building demonstrations, then perform ordinary supervised training or use the tool directly. | ESTIMATED 0.59–0.90 | The requested self-generated curriculum permits this standard route. | Compare generic generated test/debug traces against the proposed instrument curriculum at equal lifetime work. | ESTIMATED 0.59–0.90 | A larger trace corpus can cover the exposed error grammar rather than acquire transferable instrument invention. |
| Filesystem/mount/proc/IPC/frozen-asset access | Read held-out semantic tests, target graph inputs or interpreter dispatch tables through mounts/process handles; replace frozen communication semantics or compiler dependencies. | ESTIMATED 0.93–1.00 | Immutability of interpreter/tests is explicitly required, with no actual sandbox supplied. | Privileged immutable compiler/test service, hidden operand delivery, isolated descriptors/IPC and loader paths; live mutation and read probes. | ESTIMATED 0.00 | Compiler diagnostics may accidentally expose complete hidden tests even when files are unreadable. |
| Interface or encoded-state smuggling | Put optimized target kernels, uncharged trained agent tensors or benchmark answers into curriculum comments, generated profiling data or compressed tool packages. | ESTIMATED 0.86–1.00 | No curriculum format or training-state provenance exists. | Authenticate generated examples and all charged state; cap decoded handoff bytes; trusted agent rebuilding from declared data and initialization. | ESTIMATED 0.00 | Short correct kernel templates are lawful source, so length scanners cannot distinguish all prohibited state. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Print compiler-success and speed markers, bypass the timed kernel, abort problematic graphs or match public semantic fixtures by hash and return cached outputs. | ESTIMATED 0.83–1.00 | Compile-and-execute is promised, but actual result authority is undefined. | Trusted driver checks real outputs and synchronized device execution on fresh operands; all independent equivalent positive kernels must pass. | ESTIMATED 0.00 | Correctness on a few fixed inputs permits output specialization without actual graph computation. |
| Timing/check-decoupling/branch laundering | Validate a correct slow kernel and time a no-op, optimize before the diagnostic clock, hide profiler warmup work, or report only the fastest repeated timing. | ESTIMATED 0.78–1.00 | Every tool step is nominally charged; same-work binding and timing policy are absent. | Bind checked executable to timed graph, host-owned launches and synchronization, representative shape warmup and all-branch/self-training ledger. | ESTIMATED 0.00 | Host/JIT variation can invert speed rankings even for honest kernels. |
| Dev-hidden leakage/cue inference | Recognize a held-out DSL by parser errors, reserved tokens, primitive ordering or leaked source lineage, then select a memorized adapter and schedule family. | ESTIMATED 0.65–0.95 | Fresh semantics is asserted without describing independence or available documentation. | Cross syntax with semantics and hidden tests; compare source-recognition and semantics-probing solvers; retain matched legal evidence for unfamiliar behavior. | ESTIMATED 0.27–0.68 | A canonical adapter can legally handle every crossed family. |
| Adaptive aggregate oracle | Sweep layout/blocking/communication choices against graph-speed and correctness summaries, use compilation failures as extra bits, and share quotas across tuning workers. | ESTIMATED 0.67–0.94 | Feedback limits, timing precision and compiler-query budgets are not specified. | Single global work/query meter and independent final shapes; include full lawful autotuning in the ordinary recipe floor. | ESTIMATED 0.60–0.89 | Legitimate cost-model search is the intended objective's natural optimizer. |
| Slice abandonment/denominator optimization | Accelerate easy elementwise graphs, skip collective-heavy graphs or drop failed compilations from a speedup geometric mean; maximize cheap diagnostic successes. | ESTIMATED 0.54–0.93 | No graph mix, failed-graph treatment or primitive-family floors are stated. | Fixed graph roster, explicit zero/failure arithmetic, smooth correct-coverage requirements and per-family output validation. | ESTIMATED 0.25–0.63 | A workload mix can still make avoiding the novel primitive optimal. |
| Strongest lawful combined recipe | Infer semantics through generated differential tests, build a canonical adapter, use tracing/race diagnostics and cost-model schedule search, then distill legal generated debugging traces only where training beats direct use. | ESTIMATED 0.81 (ESTIMATED 0.57–0.97) | No valid security boundary excludes these compiler methods. | Execute the complete direct-tool and learned-agent alternatives at matched total cost; cut if either reaches the reference. | ESTIMATED 0.81 (ESTIMATED 0.57–0.97) | The finite exposed language may admit a reusable universal optimizer. |

## Published recipe shortcut — web checked

- [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://arxiv.org/abs/2006.06762): the primary abstract describes hierarchical program generation, evolutionary search, learned cost modeling and scheduling across subgraphs.
- [Tensor Program Optimization with Probabilistic Programs](https://arxiv.org/abs/2205.13603): the primary result identifies MetaSchedule's extensible probabilistic search-space construction; it supports a serious generic optimization baseline beyond kernel templates.
- [Debugging Triton](https://triton-lang.org/main/programming-guide/chapter-3/debugging.html): official documentation returned this session describes compile/runtime inspection, CPU interpreter debugging and memory/race tooling. It also lists interpreter limitations, so universal simulator coverage is not assumed.

The paper checks reached primary abstract depth; the official debugging page was returned with operational text. No backend was installed, no compiler compatibility checked and no hardware measurement imported. These mechanisms do not prove that an arbitrary unknown communication operation can be lowered. They do establish that diagnostic tooling, interpreters and search are mature ingredients the attacker can combine. My forecast for that legal workflow is ESTIMATED 0.81 (ESTIMATED 0.57–0.97).

## Saturation against the hypothetical 10T researcher / 12h

The source bar's fixed kill lines are single >0.70, oracle best-of-four mean >0.60, pass@4 >0.50 for R≥0.60, and projected upper-95% ≥0.75; they are requirements rather than estimated compiler scores. S1 further requires reference [0.50,0.65], stronger same-contract control ≥reference+0.20 and reachable ≥0.75. Under S7 the same limits apply to the floor-adjusted fraction Q=(R−r_floor)/(C_L−r_floor), so limited hardware headroom cannot disguise saturation.

An unfamiliar DSL is a strong transfer test only if its semantics requires substantive inference from the same accessible evidence a reference uses. If the interpreter code is public, semantic recovery may reduce to reading it. If the interface is black box but the primitive has a small finite behavior, tagged microtests can reveal it. If the operation is hidden and its necessary behavior cannot be identified by permitted probes, the task becomes an information-access problem. The card does not identify a fourth, research-intensive regime.

Training an agent does not by itself fix this. A curriculum that teaches “write a tiny test, compare outputs, inspect the trace” may be ordinary code-agent supervision. The grader then measures final graph optimization, so the researcher can choose direct tooling, synthetic traces or a small learned controller according to their true costs. Forcing a training step without demonstrating its causal contribution would add bookkeeping rather than resistance.

ESTIMATED single-run maximum is 0.97; ESTIMATED oracle best-of-four mean is 0.91; ESTIMATED pass@4 is 0.98; ESTIMATED projected upper-95% scenario is 0.995. All corresponding binding kill lines are likely crossed. Those are conditional desk forecasts for a finite accessible semantics family, not measured statistics. The upper-95% remains an unfit risk scenario; an empirical prediction bound is UNMEASURED. No probability calculation from an assumed distribution is implied.

S1 is unsupported because there is no executable agent reference, attainable stronger control or measured training-versus-direct-tool frontier. S7 is unsupported because theoretical peak hardware throughput does not establish the achievable graph-speed ceiling under the actual correctness and diagnostic constraints. Unknown or overlapping ceiling evidence remains HOLD. Observed rollout scores, runs, grader timing noise and observed pass@k are UNMEASURED. Plan: repeated synchronized timings for identical binaries across representative hosts, independently generated semantic families, separate direct-tool/agent-training costs, and full-budget outer researcher restarts after the CPU kill screen. The supplied weakness reports' current-agent under-exploration cannot discount a target assumed to use the full horizon.

## Revised estimate versus the source card

The source's ESTIMATED 0.37 posits that diverse demonstrations and tracing may fail to teach invention of an appropriate diagnostic. My ESTIMATED 0.81 (ESTIMATED 0.57–0.97) follows a different route: infer the primitive operationally, construct the instrument with ordinary programming, and only train if amortization helps. The card never explains why the target researcher cannot do that within its access contract. The combined-recipe calibration counsels against assigning difficulty to components that disappear under whole-stack replacement.

## Boilerplate and missing build content

ESTIMATED 30–45% is shared conceptual scaffolding. It is mostly boilerplate for buildability: no actual DSL, communication semantics, hardware backend, graph suite, correct baseline, tool API, trained-agent checkpoint, curriculum schema, cost equation or deployment/training budget is given. Compilation and semantic tests are useful verification promises but are not an environment implementation.

Missing evidence is particularly material for workload realism. Compiler-instrument construction may be authentic ML systems research, while arbitrary invented opcodes and a finite interpreter puzzle may be generic software. A naturally occurring communication failure with inherited traces, concrete optimization choices and a faithful hardware mechanism would be needed to establish the former.

## Duplicate check

I did not open the source's referenced broad suite file because it is outside the specifically permitted reference set. Its claimed nearest suite location is therefore unverified. None of the other assigned cards centers on compiler semantics or kernel-agent curriculum. The inspected catalog T10 and T13 material does not establish duplication. No D-card, uninspected v3 task or unseen catalog identifier is recorded as a duplicate.

## Verdict, required fixes and cheapest decisive check

CUT the card as a resistant research task. Its objective is coherent as a compiler benchmark, but no bounded change establishes that self-generated tool curricula supply an unsolved mechanism beyond the ordinary direct workflow. Security isolation and honest timing are necessary delivery work, not a repair to that premise. A future replacement would need a concrete production-relevant communication phenomenon and an independently demonstrated training-transfer advantage.

The cheapest decisive check is CPU-only inspection and differential testing of a proposed DSL family's observable semantics and adapter tractability, ESTIMATED 0 H100-hours. It should compare a direct probe/adapter generator with the proposed curriculum reference before any agent training. A few device microbenchmarks could later verify that the recovered adapter has the expected communication behavior, but the card does not specify hardware or graph size well enough to estimate a meaningful full training campaign. The source's pilot allocation is not inherited as a cost measurement.

No live anti-cheat gate is passed. Any future implementation would still require immutable interpreter/test authority, typed and provenance-checked curricula, actual-work timing checks, all-positive independent controls, bounded per-graph failures, portable startup, private decontamination and exact archive/report reconciliation. Keeping these obligations explicit does not change the CUT verdict, and no accelerator work or external communication is authorized by this review.

## Verdict record

id: C116
source_group: creative_v4
verdict: CUT
strongest_attack: ESTIMATED 0.81 (0.57–0.97)
combined_recipe_attack: ESTIMATED 0.81 (0.57–0.97)
best_of_4: ESTIMATED 0.91
pass_at_4: ESTIMATED 0.98
single_run_max: ESTIMATED 0.97
upper95_projected: ESTIMATED 0.995
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: none; requires replacement mechanism and new design
main_kill_reason: semantics probing and compiler search bypass curriculum necessity
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
