# C124 — Self-repairing tools that learn when repair evidence is enough — saturation screen
## 1. What the grader actually rewards
After a runner fault, the submitted repair policy must restore the scientific operation and enable useful later training. Startup success and passing self-written tests are insufficient; independent implementation checks reject silent changes in semantics, and failed launches remain charged. ESTIMATED R≈0 is competent contract-preserving repair followed by ordinary research, while ESTIMATED R≈1 is attainable stronger downstream utility under the same repair and experiment budget. A broken unrepaired runner should remain at ESTIMATED R≈0, and the intended ESTIMATED reference around 0.60 needs actual campaign anchors.
## 2. Strongest lawful combined attack
Use a mature coding-agent repair loop with versioned runner contracts, minimized reproductions and separate behavioral oracles. [SWE-agent](https://arxiv.org/abs/2405.15793) verifies repository navigation, editing and execution feedback as a capable automated repair framework. [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html) verifies generated action sequences and invariants, relevant to launch, retry, checkpoint and resume transitions. These tools do not automatically prove scientific equivalence, so the attack must bind tests to the declared operation.

Capture the failing request and legal initial state, reduce the sequence with differential tests, and compare candidate repairs against independently implemented small reference operations. Keep an immutable transaction ledger so retries cannot replace failures. Roll back only the faulty component, preserving support for new operations through a separately tested adapter when needed. Validate the actual update or data transformation on bounded cases, then run a short learning continuation before resuming the campaign. Search several minimal repairs and choose the cheapest valid one. This stack addresses both the obvious startup issue and the card's stated concern that a broad rollback removes newly required functionality.

ESTIMATED single-run R=0.82, range 0.61–0.94; ESTIMATED oracle best-of-4=0.89; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% score=0.97. Long-range semantic bugs whose effects appear only after many updates remain harder than unit-level repair. But the card provides an independent implementation and a contract, making reference replay unusually strong. No specific scientific uncertainty survives ordinary differential testing and minimal component replacement in the current description.
## 3. Other routes
Reference replay with minimal patching and a known-good fallback is the strongest single recipe. ESTIMATED R=0.68, range 0.45–0.86. It restores many runner faults without learning a sophisticated stopping rule for validation.

A bounded repair search can enumerate plausible changes, generate transition tests and progressively promote candidates to longer continuation. ESTIMATED R=0.77, range 0.54–0.92. Test selection and patch search fit naturally together, with all failed candidates retained in the bill. A lawful runner reimplementation behind the published interface has ESTIMATED R=0.80, range 0.50–0.95 if the operation set is small. This whole-component replacement must remain a baseline; requiring the original buggy code structure would artificially protect the task.
## 4. What would lower lawful saturation
Use genuine ML incidents where runner semantics are locally correct but interact with delayed optimizer or data state, and where a bounded diagnostic distinguishes causes before an expensive continuation. Keep the independent semantic reference available on representative small cases rather than making correctness unknowable. ESTIMATED score reduction is 0.14–0.22, to around 0.60–0.68, still likely above repeated-search gates. ESTIMATED development effort is 12–22 person-days and 240 H100-h. A meaningful redesign would emphasize a concrete learning mechanism, not merely a larger collection of ordinary runner faults.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 16 GPU-h. New ESTIMATED comparison is 112 H100 GPU-h: 4 repair policies × 2 fault histories × 2 seeds × 4 H100-h on 1B learner continuations = 64; fixed 4B agent repair execution and bounded semantic replay = 16; independent healthy-runner and new-operation controls = 16; repeated final grades = 16. ESTIMATED total 64+16+16+16=112. Most test generation and code repair is CPU work, but final learning gains cannot be inferred from CPU startup tests. The old budget was sufficient only for a narrower incident demonstration.
## 6. Duplicate check
D13, MODERATE: its source trains incident repair with complete causal certificates, while this card modifies the agent's runner-repair/validation scaffold and grades continued research utility. 07A, MODERATE: it repairs a measurement ecosystem and checks induced learning, whereas C124 repairs experiment execution rather than the reward checker. The interventions overlap operationally without being identical.
## 7. Verdict
CUT. ESTIMATED single-run reward exceeds its kill line by 0.12 and best-of-4 by 0.29. Mature repair tooling plus independent reference replay can plausibly restore the complete declared operation; downstream continuation does not introduce an identified additional research barrier.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent self-repair policy attempts followed by real resumed campaigns). Grader noise UNMEASURED (planned: repeated fault histories, repair-agent decisions and subject-training seeds). Score ladder UNMEASURED (planned: unrepaired runner, retry-only, minimal reference repair, component replacement, reference and stronger valid campaign).
## Screen record
id: C124
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.82
attack_single_range: 0.61-0.94
bo4_est: 0.89
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 16
gpuh_new_est: 112
duplicate_of: D13 MODERATE; 07A MODERATE
kill_reason: independent replay and minimal component repair restore the runner contract
souping_flag: no
