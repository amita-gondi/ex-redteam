# C122 — Self-training a research critic without rewarding persuasive prose — saturation screen
## 1. What the grader actually rewards
The trained critic must help a reset proposal agent select interventions that actually improve private learning projects. Agreement with preferences, critique eloquence and rejection of awkward prose contribute nothing directly, and inspecting rejected ideas still consumes the budget. ESTIMATED R≈0 means no gain over a competent execution-trained ranker; ESTIMATED R≈1 means attainable stronger selected-proposal utility under equal costs. An unchanged critic and a critic-free researcher need native outcomes before setting the intended ESTIMATED reference near 0.60.
## 2. Strongest lawful combined attack
Build a proposal corpus containing executable intervention code, preconditions, project diagnostics and measured development consequences. Vary the prose independently, strip presentation cues from a second input view, and train a pairwise utility predictor with uncertainty rather than ask for persuasive free-form reviews. [Ranking Algorithms by Performance](https://arxiv.org/abs/1311.4319) verifies the established algorithm-selection/ranking approach. [CodeRL](https://arxiv.org/abs/2207.01780) verifies the more specific precedent of an execution-outcome-trained critic assisting a generative policy, without demonstrating scientific proposal transfer.

Use code features and intervention-response summaries alongside text, calibrate on unseen development mechanism families, and allocate execution to uncertain high-upside proposals. [BoTorch](https://arxiv.org/abs/1910.06403) supplies a practical Bayesian optimization framework for this expensive acquisition loop. Retrain the critic on results from its own selected proposals, retaining random or diversity-selected execution to reduce selection bias. Distill successful selection trajectories into the internal critic and compare against a critic-free execution portfolio. Every label-generating run and rejected candidate evaluation is charged. This is stronger than stylistic augmentation alone and directly optimizes the final research decision.

ESTIMATED single-run R=0.50, range 0.29–0.71; ESTIMATED oracle best-of-4=0.59; ESTIMATED pass@4 at R≥0.60=0.46; ESTIMATED projected upper-95% score=0.74. Novel mechanism transfer remains the difficult part: a ranker can be confidently wrong about a valid intervention whose effect is absent from its outcome support. Active execution helps, but labels are costly and their value depends on which experiment the critic is willing to propose. These limits leave plausible reserve while placing the current design very close to several kill lines.
## 3. Other routes
A supervised outcome ranker over code and project state is the strongest single standard recipe. ESTIMATED R=0.38, range 0.19–0.60. It removes many presentation effects but may systematically suppress unfamiliar mechanisms.

Search over critic input representation, ranking loss, uncertainty thresholds, exploration fraction and training mix has ESTIMATED R=0.46, range 0.24–0.68. Selection must use completed campaigns rather than held-out ranking accuracy alone. A lawful critic-free portfolio that executes diverse proposals directly has ESTIMATED R=0.54, range 0.30–0.77 if interventions are cheap. That branch would CUT the current economics; the lower central forecast assumes the substantive execution cost implied by real training projects, which must be profiled rather than presumed.
## 4. What would lower lawful saturation
Commit to mechanism-held-out proposals whose code is valid but whose useful effect requires a paid, informative project probe. Cross writing style independently, include genuinely bad polished ideas, and make the proxy cost match final campaign economics. ESTIMATED attack reduction is 0.07–0.13, to approximately 0.37–0.43. ESTIMATED authoring effort is 14–24 person-days and 400 H100-h for executed outcome labels and probe validation. The exact required change is to enforce this mechanism/probe split and test the critic-free portfolio; removing unconventional positives would simply favor conservative rejection.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 18 GPU-h. New ESTIMATED total is 256 H100 GPU-h. Assume a 4B critic with adapter training: 4 critic arms × 2 seeds × 4 H100-h = 32; outcome-label collection on 1B projects, 12 intervention/project pairs × 8 H100-h = 96; reset-agent selections, 4 × 2 × 3 held-out projects × 4 H100-h = 96; independent final evaluation and critic-free controls add 32. ESTIMATED sum 32+96+96+32=256. The old estimate can train a small ranker from existing labels but leaves the costly scientific supervision and selected-proposal consequences unpriced.
## 6. Duplicate check
07B, MODERATE: its source trains an evidence evaluator under adaptive research optimization and independent truth, while C122 changes an internal proposal critic and grades later executed learning gains. T03, MODERATE: selecting experiments overlaps, but its artifact is a full transferable controller rather than critic weights. D24, WEAK: it selects fixed policies from measurements without training the scientific critic or executing new proposals.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 has only 0.01 margin, pass@4 only 0.04, and the projected bound only 0.01. Require the explicit mechanism/probe split and matched critic-free execution control; cheap direct evaluation or an ordinary ranker crossing any line requires CUT.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent critic-training attempts and reset proposal campaigns). Grader noise UNMEASURED (planned: repeat critic seeds, selection trajectories and intervention training). Score ladder UNMEASURED (planned: original critic, style-invariant ranker, active ranker, critic-free portfolio, reference and stronger selection control).
## Screen record
id: C122
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.50
attack_single_range: 0.29-0.71
bo4_est: 0.59
pass4_est: 0.46
ub95_est: 0.74
gpuh_old: 18
gpuh_new_est: 256
duplicate_of: 07B MODERATE; T03 MODERATE; D24 WEAK
kill_reason: none
souping_flag: no
