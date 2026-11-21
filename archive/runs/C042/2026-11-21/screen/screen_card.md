# C042 — Pretrain conditional computation with delayed expert utility — saturation screen
## 1. What the grader actually rewards
Held-out loss on compositions requiring complementary learned features determines reward under actual active-compute and stored-state limits. Balanced routing is diagnostic, so spreading traffic evenly cannot earn points unless the experts become useful together. ESTIMATED R≈0 is the strongest stable-MoE training floor and ESTIMATED R≈1 an attainable composition-sensitive policy; the balanced-but-failing starter is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Start with stable sparse training from [ST-MoE](https://arxiv.org/abs/2202.08906), compare auxiliary-loss and [loss-free balancing](https://arxiv.org/abs/2408.15664), and combine expert warmup, router exploration, capacity control and rare-task replay. Loss-free balancing matters because it can remove interference from a uniform auxiliary objective without abandoning utilization control. Do not assume changing the fixed architecture is permitted; shared/expert-capacity alternatives are only legal when admitted by the model interface.

Track per-expert gradient/feature diversity and rehearsal response, then tune replay and router regularization for later composition loss rather than marginal task loss. A target researcher can search an early exploration phase followed by reduced balancing pressure and targeted precursor preservation. Its best plausible controller also uses small charged composition probes to estimate expert complementarity before committing scarce retention capacity. The papers establish useful components, not a solution to delayed, resource-constrained joint usefulness.

ESTIMATED single-run R=0.49, range ESTIMATED 0.27–0.67; ESTIMATED best-of-4=0.58; ESTIMATED pass@4 at R≥0.60=0.41; ESTIMATED projected upper-95% bound=0.73. The provisional reward gap begins after a competent stable/replay stack; otherwise ordinary router repair would likely saturate it. That stack preserves broad precursor competence but cannot reliably tell which low-frequency features deserve capacity before complementary evidence arrives. The estimated missing share is delayed joint selection, not load balancing. If all precursor experts can be kept cheaply, this rationale collapses and the forecast must move upward.
## 3. Other routes
Loss-free balancing with standard warmup and capacity tuning reaches ESTIMATED R=0.34, range ESTIMATED 0.15–0.55. It addresses gradient interference but does not optimize future feature combinations.

A full-budget sweep of exploration schedules, replay fractions, expert dropout and capacity factors yields ESTIMATED R=0.43, range ESTIMATED 0.22–0.63. Such a search may find a universal preserve-all schedule and therefore must be allowed, not treated as an exploit. Uniform rare-task replay is another single-recipe control, ESTIMATED R=0.38, range ESTIMATED 0.18–0.59; its weakness is spending limited updates on specialists that never become complementary.
## 4. What would lower lawful saturation
Require paired private curricula with matched early marginal frequencies and losses but different, development-identifiable later expert interactions. Set a validated retention capacity where preserving every candidate precursor is infeasible, while a legal informed policy can preserve the right ones. ESTIMATED composite R would drop toward 0.41–0.50, with ESTIMATED best-of-four near 0.54. ESTIMATED authoring cost is five researcher-weeks plus ESTIMATED 384 H100 GPU-h of causal and feasibility checks. This exact generator/capacity change is required; simply adding experts or delaying all rewards supplies no evidence of research depth.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 18 GPU-h. New ESTIMATED 432 H100 GPU-h assumes an ESTIMATED 1.2B-total, 0.3B-active MoE subject, ESTIMATED four training arms, ESTIMATED three curriculum seeds and ESTIMATED 28 H100-hours per complete precursor-to-composition run. Arithmetic: ESTIMATED 4×3×28=336 GPU-h; add ESTIMATED 64 GPU-h for independent composition/retention evaluation and ESTIMATED 32 GPU-h for router/capacity calibration. The original estimate may show a routing trend but cannot test delayed joint utility after enough sparse learning to establish specialization.
## 6. Duplicate check
04A: WEAK, from its read asynchronous MoE contract; its intervention repairs policy/version/cache fidelity rather than preserving complementary pretraining features. FIX T08: MODERATE because its inspected update rule protects returning prerequisites, but it uses changing tool contracts rather than expert routing and delayed composition loss. No STRONG intervention/target match was found.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-four margin is 0.02 and projected-bound margin 0.02; pass@4 margin is ESTIMATED 0.09. Require the matched-marginal interaction generator and demonstrably binding precursor-retention capacity before spending on a larger screen.
## 8. Measurement status
Rollouts UNMEASURED (planned: precursor-to-composition curricula with combined MoE baselines). Grader noise UNMEASURED (planned: repeated routing and training seeds). Score ladder UNMEASURED (planned: balanced starter, stable/replay stack, complementarity controller and attainable informed policy).
## Screen record
id: C042
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.49
attack_single_range: 0.27-0.67
bo4_est: 0.58
pass4_est: 0.41
ub95_est: 0.73
gpuh_old: 18
gpuh_new_est: 432
duplicate_of: 04A WEAK; FIX-T08 MODERATE
kill_reason: near tail gates; require selective precursor-capacity mechanism
souping_flag: no
