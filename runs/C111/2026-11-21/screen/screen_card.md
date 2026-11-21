# C111 — Make lossless training faster, then test whether the saved time is useful — saturation screen
## 1. What the grader actually rewards
An accelerated implementation must first reproduce the contracted training update; a subsequently changed learning schedule is then judged by private final loss at fixed total time. The ledger must separate those two claims so that altered arithmetic cannot masquerade as an exact speed gain. ESTIMATED R≈0 is the competent fast-engine plus retuned-schedule floor, while ESTIMATED R≈1 is the attainable stronger same-time model. An unchanged slow engine may lie below the floor; the intended ESTIMATED reference score of 0.60 cannot create headroom if ordinary retuning already reaches the useful frontier.
## 2. Strongest lawful combined attack
Profile the inherited engine, remove avoidable host synchronization, use compatible fused operations and compile stable regions with [torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_full_example.html). [FlashAttention-2](https://arxiv.org/abs/2307.08691) provides a mature attention implementation to test where the contract admits its numerical differences. Neither compiler output nor mathematically exact attention is automatically bitwise equivalent: the trusted update comparison must reject incompatible substitutions before they enter the attack score.

After that check, measure the actual affordable update horizon and retune warmup, decay, batch size and source schedule under the final learning-stage rules. Use short horizon-matched probes, then extend the most promising schedules rather than linearly extrapolating the initial curve. The public [modded-nanogpt](https://github.com/kellerjordan/modded-nanogpt) project verifies an active ecosystem combining training systems and learning recipes; its algorithmic changes are relevant only in the permitted retuning stage. Charge compilation, rejected candidates and recipe search. The best practical attack treats speed as extra training capacity and optimizes final loss directly, precisely the endpoint described by the card.

ESTIMATED single-run R=0.85, range 0.67–0.95; ESTIMATED oracle best-of-4=0.91; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% score=0.98. Long-horizon rank reversal and data exhaustion leave some residual. They do not establish a new coupled research problem when the learner can simply train longer with a tuned decay. If bitwise exactness removes every useful engine substitution, the task instead risks having too little physical reserve, which also cannot support a pass.
## 3. Other routes
A compatible optimized engine with an ordinary horizon-adjusted decay schedule is the strongest single recipe. ESTIMATED R=0.73, range 0.51–0.89. This can capture both most execution savings and their most obvious use without complex scientific planning.

A multi-fidelity sweep across compatible engine configurations and equal-time schedules has ESTIMATED R=0.81, range 0.60–0.94. Development loss supplies a direct fitness signal, making blind but competent search powerful. A lawful minimal route retains the existing engine and retunes its schedule thoroughly; ESTIMATED R=0.56, range 0.33–0.80. That control is necessary to identify whether the claimed benefit came from acceleration or merely fixing an undertuned baseline.
## 4. What would lower lawful saturation
Require a meaningful horizon-dependent choice such as retaining a scarce data source for a delayed learning stage, with real measured reversals after the engine speed changes. Compare against independently retuned slow and fast engines and show an additional gain from that choice. ESTIMATED reduction is 0.12–0.20, leaving 0.65–0.73, so this is not a convincing small repair. ESTIMATED development effort is 8–14 person-days and 360 H100-h. Exactness auditing should remain separate from learning utility; paying two bonuses for one speedup would inflate apparent progress.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 16 GPU-h. New ESTIMATED value is 320 H100 GPU-h: 2 engines × 3 schedule families × 2 seeds × 20 H100-h for meaningful 1B continuation = 240; exact update, warmup and resume checks = 16; 2 selected engine/schedule pairs × 2 seeds × 12 H100-h on a 4B continuation = 48; independent loss evaluation = 16. ESTIMATED total 240+16+48+16=320. This includes billions-of-token-scale continuation planning rather than assuming a microbenchmark settles final learning. The original estimate was plausible only for an engine smoke test.
## 6. Duplicate check
05B, MODERATE: the source already optimizes exact training graphs and state, but its target is valid update throughput rather than final retuned loss. FIX T02, MODERATE: it searches continuation schedules and optimizer behavior, with execution already healthy. C111 composes those treatments; the composition is distinct enough to avoid an automatic duplicate cut but supplies little new saturation resistance.
## 7. Verdict
CUT. ESTIMATED single-run reward exceeds the threshold by 0.15 and ESTIMATED best-of-4 by 0.31. A standard compatible engine and equal-time recipe search are the direct solution, not merely partial components of an unresolved mechanism.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent engine-and-schedule development attempts). Grader noise UNMEASURED (planned: repeated fixed-recipe training and matched-host timing). Score ladder UNMEASURED (planned: original engine, retuned original, exact accelerated fixed schedule, retuned acceleration, reference and stronger equal-time control).
## Screen record
id: C111
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.85
attack_single_range: 0.67-0.95
bo4_est: 0.91
pass4_est: 0.99
ub95_est: 0.98
gpuh_old: 16
gpuh_new_est: 320
duplicate_of: 05B MODERATE; FIX T02 MODERATE
kill_reason: compatible engine plus equal time retuning directly solves the objective
souping_flag: no
