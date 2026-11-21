# C040 — Pretrain exact arithmetic without washing out language — saturation screen
## 1. What the grader actually rewards
The learner emits arithmetic programs whose executed results must be exact on fresh operator/numeral compositions while held-out language loss remains acceptable. Auxiliary training work is charged, and the unspecified utility weights materially affect how much arithmetic specialization is profitable. ESTIMATED R≈0 is a competent mixed-language computational-training floor and ESTIMATED R≈1 an attainable joint control; unchanged prose-focused training plausibly lies near ESTIMATED R=0.00, with reference ESTIMATED R=0.60 awaiting calibration.
## 2. Strongest lawful combined attack
Teach a compact parser-and-interpreter program family, generate diverse legally available operator compositions and radix conversions, and supervise both executable code and intermediate machine state. [Show Your Work](https://arxiv.org/abs/2112.00114) establishes scratchpad supervision. [Program of Thoughts](https://arxiv.org/abs/2211.12588) directly exploits generated programs to delegate exact numerical computation to an interpreter, matching this grader more closely than a claim about hidden neural carry circuits.

Combine that supervision with execution filtering, length-balanced curricula and language replay under a retention-constrained mixture. Search auxiliary-loss weights and arithmetic exposure using the actual joint utility. If submitted code controls only the objective, apply these mechanisms to the available executable traces and intermediate labels rather than assuming permission to replace the training corpus. The broad data-generation scope needs freezing, but standard token and intermediate-state objectives remain powerful even under the narrower reading.

ESTIMATED single-run R=0.77, range ESTIMATED 0.49–0.92; ESTIMATED best-of-4=0.85; ESTIMATED pass@4 at R≥0.60=0.95; ESTIMATED projected upper-95% bound=0.97. The forecast assumes a meaningful language-retention constraint and rewards most attainable arithmetic gain through learned program synthesis. Residual failures involve discovering unfamiliar operator semantics from limited examples, very long compositions and language/arithmetic interference. New numeral glyphs alone are weak protection when a program can parse the disclosed numeral system and execute a general algorithm. This route does not require neural internalization of exact arithmetic.
## 3. Other routes
Execution-filtered program-synthesis supervision alone reaches ESTIMATED R=0.66, range ESTIMATED 0.39–0.85. It directly targets the measured output and may beat elaborate arithmetic-specific objectives.

A sweep over language replay fraction, scratchpad depth, auxiliary-state weight and training order gives ESTIMATED R=0.70, range ESTIMATED 0.43–0.88. Proxy training can narrow this space before a complete retained-language check. A lawful generic interpreter-output strategy might obtain ESTIMATED R=0.61, range ESTIMATED 0.32–0.84 if problems expose their operator definitions in a uniform form. That is grader alignment, not parser cheating, and belongs among required saturation controls.
## 4. What would lower lawful saturation
Decide whether the intended product is program synthesis or internal exact computation. For the former, require genuinely new executable semantics and limited compositional examples, with a development generator that reveals the same difficulty. For the latter, change the deployment interface to direct bounded computation and recalibrate an attainable endpoint; that is a substantive task change. ESTIMATED combined R could then fall to 0.43–0.58, at ESTIMATED four researcher-weeks and ESTIMATED 256 H100 GPU-h of training and retention calibration. Hiding notation without making its semantics inferable would create ambiguity rather than research depth.
## 5. Decisive-check GPU-h re-estimate
Old card pilot: ESTIMATED 14 GPU-h. New ESTIMATED 320 H100 GPU-h assumes an ESTIMATED 1B mixed-corpus subject and ESTIMATED 2B training tokens per run. Compare ESTIMATED four objective/curriculum arms with ESTIMATED two seeds, each ESTIMATED 32 H100-hours: ESTIMATED 4×2×32=256. Reserve ESTIMATED 48 GPU-h for generated-program and language-loss evaluation and ESTIMATED 16 GPU-h for equal-FLOP auxiliary calibration. Throughput is a planning assumption. The old allowance can test toy arithmetic learning but cannot establish retained language competence after meaningful objective modification.
## 6. Duplicate check
Catalog T02: WEAK, from its read continued-pretraining contract; its target is held-corpus loss rather than executed arithmetic plus language retention. 02A: MODERATE after reading its objective/intermediate-supervision interface, but transferable sparse-success learning is broader and differently graded. C040 itself needs no excluded parameter-combination mechanism.
## 7. Verdict
CUT. ESTIMATED best-of-four excess is 0.25 and single-run excess 0.07. The program-execution grader admits a strong general synthesis route that bypasses the proposed need to discover arithmetic circuitry.
## 8. Measurement status
Rollouts UNMEASURED (planned: objective searches with complete retention evaluation). Grader noise UNMEASURED (planned: repeated training and exact execution banks). Score ladder UNMEASURED (planned: prose baseline, program imitation, scratchpad stack and stronger joint control).
## Screen record
id: C040
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.77
attack_single_range: 0.49-0.92
bo4_est: 0.85
pass4_est: 0.95
ub95_est: 0.97
gpuh_old: 14
gpuh_new_est: 320
duplicate_of: T02 WEAK; 02A MODERATE
kill_reason: executable program synthesis bypasses internal arithmetic mechanism
souping_flag: no
