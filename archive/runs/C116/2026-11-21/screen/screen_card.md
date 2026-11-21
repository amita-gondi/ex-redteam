# C116 — A tool-building curriculum for unfamiliar accelerator DSLs — saturation screen
## 1. What the grader actually rewards
The corpus must train a reset kernel agent that subsequently builds useful instruments and delivers correct graph speedups in unfamiliar accelerator languages. Curriculum construction, self-training, compiler probes and downstream tool development all consume the same scientific budget; an elegant profiler receives no standalone reward. ESTIMATED R≈0 is the mature kernel-demonstration/tracing curriculum floor, and ESTIMATED R≈1 is a stronger attainable transfer curriculum under identical compiler access. The unmodified agent should be measured alongside that floor, with the intended ESTIMATED reference around 0.60 remaining provisional.
## 2. Strongest lawful combined attack
Mine checked kernel transformations, failed compiler traces and debugging trajectories, then construct curriculum episodes that require writing a small observation tool before solving a kernel. [KernelBench](https://arxiv.org/abs/2502.10517) verifies an executable kernel-generation benchmark and toolkit useful for source workloads, but its public tasks cannot substitute for unseen semantics. [Triton's debugging documentation](https://triton-lang.org/main/programming-guide/chapter-3/debugging.html) verifies interpreter and debugging facilities that a strong baseline should exploit wherever the new DSL exposes equivalent access.

The attack would generate semantic differential tests, trace communication ownership and barriers, reduce counterexamples, and train the agent on the sequence from failed observation to instrument to corrected implementation. Use adapter training on a single coding model, replay ordinary kernel work, and select curricula by full graph performance on held-out development DSL families. During deployment, pair compiler tracing with bounded synthesis of missing wrappers and active tests of competing communication interpretations. A tool-assisted general coding agent without additional training is also a full-strength control. This is a serious combined attack, not merely public-example replay.

ESTIMATED single-run R=0.41, range 0.24–0.64; ESTIMATED oracle best-of-4=0.51; ESTIMATED pass@4 at R≥0.60=0.24; ESTIMATED projected upper-95% score=0.69. The remaining gap is transfer of instrument design: observing local values is insufficient when the missing fact concerns collective progress, ownership or an asynchronous dependency. New semantic primitive families require choosing what trace to build before the final kernel can be optimized. Training a compact agent to generalize that investigative skill, while charging all teaching and downstream search, is materially harder than supplying the outer researcher with a better profiler. This forecast reads the card's fresh semantics literally, rather than treating renamed Triton operations as new tasks.
## 3. Other routes
Kernel demonstrations plus ordinary execution-feedback training are the strongest single recipe. ESTIMATED R=0.28, range 0.13–0.48. They teach useful code search but provide few examples of discovering which observation is missing.

Evolutionary curriculum search can vary tool-writing frequency, failed-trace balance, primitive combinations and diagnostic complexity. ESTIMATED R=0.36, range 0.19–0.56. Its expensive fitness is transfer after agent training, limiting how many meaningful arms fit. A direct untrained coding-agent/compiler loop has ESTIMATED R=0.39, range 0.20–0.61; it could become the winner if mature tracing exposes every new primitive immediately. It must retain the same tool-development and graph-evaluation costs as trained agents.
## 4. What would lower lawful saturation
Strengthen the existing semantic holdout by varying collective completion and ownership interactions while keeping adequate interpreter evidence and independently implemented reference kernels. Cross tool availability with the new primitive so one universal trace dump cannot supply the answer at negligible cost. ESTIMATED attack reduction is 0.04–0.08, to around 0.33–0.37. ESTIMATED preparation is 18–30 person-days and 120 H100-h for curriculum feasibility and correctness audits. These changes are optional strengthening; the screen's lower forecast already assumes genuinely unfamiliar semantic families as stated, not cosmetic syntax changes.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 20 GPU-h. New ESTIMATED total is 144 H100 GPU-h. Use a 4B coding agent: 3 curricula × 2 seeds × 8 H100-h adaptation = 48; downstream compiler/kernel campaigns, 3 × 2 × 3 held-out primitive families × 4 H100-h = 72; independent correctness, timing and repeated graph grades = 24. ESTIMATED sum 48+72+24=144. Kernel tests individually may be tiny, but training and evaluating transferable tool construction across semantic families dominate. The original budget could establish one illustrative transfer, not the stronger curriculum effect being screened.
## 6. Duplicate check
T03, MODERATE: the opened contract trains a reusable research controller, while C116 submits data teaching a specific instrument-building skill and grades accelerator graphs. 05B, WEAK: it optimizes an existing fixed training implementation, without training an agent to construct tools for new DSL semantics. D24, WEAK: its instrument selects fixed policies rather than enabling kernel implementation or learned research transfer.
## 7. Verdict
PASS-SCREEN, as a provisional desk forecast. ESTIMATED margins are 0.29 below the single-run line, 0.09 below best-of-4, 0.26 below pass@4 and 0.06 below projected upper-95%. This does not certify the unbuilt semantic holdout or a physical speedup ceiling; those remain decisive empirical gates.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent curriculum-building attempts with direct-agent bypass controls). Grader noise UNMEASURED (planned: repeated agent training, compiler campaigns and warm graph timings). Score ladder UNMEASURED (planned: unchanged agent, kernel corpus, tracing corpus, instrument curriculum, reference and stronger attainable transfer control).
## Screen record
id: C116
verdict: PASS-SCREEN
binding_line: none
attack_single_est: 0.41
attack_single_range: 0.24-0.64
bo4_est: 0.51
pass4_est: 0.24
ub95_est: 0.69
gpuh_old: 20
gpuh_new_est: 144
duplicate_of: T03 MODERATE; 05B WEAK; D24 WEAK
kill_reason: none
souping_flag: no
