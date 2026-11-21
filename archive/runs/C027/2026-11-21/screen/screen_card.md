# C027 — A curriculum that teaches the agent to discover new tools — saturation screen
## 1. What the grader actually rewards
Curriculum examples receive no direct reward: a trained agent must invent an executable affordance and use it to improve private ML campaigns after all development costs. ESTIMATED R≈0 corresponds to the stronger of unchanged-agent and ordinary coding-curriculum utility; ESTIMATED R≈1 means the independently attainable net campaign gain. The reference is provisionally ESTIMATED R=0.60, while an unchanged capable coding agent could already eliminate much of the native gap before normalization.
## 2. Strongest lawful combined attack
Generate development episodes by removing genuinely useful diagnostic operations, solve them with executable code, and retain only demonstrations whose tools improve a completed experiment. Combine error-driven repair, a reusable skill library, tool-use supervised training and outcome-based fine-tuning. [Voyager](https://arxiv.org/abs/2305.16291) provides the established curriculum/code-library/feedback pattern; [Toolformer](https://arxiv.org/abs/2302.04761) establishes learning when and how to invoke tools, although neither paper proves scientific-tool invention.

The attack should include unmodified coding-agent deployments as a control and concentrate curriculum tokens on situations where merely wrapping a profiler fails. During deployment the trained agent first tries a transparent general execution interface, then writes a small custom statistic or experiment wrapper when expected information gain warrants it. Search curriculum mixtures using downstream campaign utility, with every generated trace and failed tool charged. This is a realistic use of the target researcher's budget because curriculum synthesis parallelizes and most candidate programs can be rejected by inexpensive execution.

ESTIMATED single-run R=0.63 with range ESTIMATED 0.36–0.81; ESTIMATED best-of-4=0.73; ESTIMATED pass@4 at R≥0.60=0.78; ESTIMATED upper-95% projection=0.89. These forecasts assume that most hidden omissions require recombining available numerical operations. On that reward ladder the stack supplies roughly ESTIMATED 0.63 of net improvement beyond a fixed ordinary curriculum, rather than receiving points for producing many tools. Its missing share consists of unfamiliar scientific abstractions and tools whose benefit arrives too late to identify cheaply. An API-omission generator alone provides little protection against broad code synthesis.
## 3. Other routes
The strongest individual recipe is execution-filtered tool-building imitation: ESTIMATED R=0.52, range ESTIMATED 0.27–0.72. It learns successful repair patterns but lacks deployment-driven curriculum selection.

A mixture sweep over missing-operation types, demonstration difficulty and repair depth reaches ESTIMATED R=0.58, range ESTIMATED 0.31–0.78. Short training runs can screen easy failures, but final selection must replay complete private-proxy campaigns rather than tool unit tests. A lawful general Python execution wrapper with ordinary coding training is another threat, ESTIMATED R=0.46, range ESTIMATED 0.20–0.70: its success would show the omitted interfaces were superficial.
## 4. What would lower lawful saturation
Replace syntactic API omissions with development-observable failures of scientific identifiability: the useful tool must construct a new measurement that separates competing causal accounts. Include matched tasks where writing an elaborate tool wastes the remaining experiment budget. ESTIMATED attack utility could fall to R=0.43–0.55, at ESTIMATED four author-weeks and ESTIMATED 160 H100 GPU-h for constructing and validating learning-dependent episodes. Reward final trained capability under a common general execution interface so an arbitrary restriction on wrappers cannot manufacture difficulty. This redesign must retain an attainable control that actually invents the discriminating measurement.
## 5. Decisive-check GPU-h re-estimate
Old card allowance: ESTIMATED 16 GPU-h. New ESTIMATED 112 H100 GPU-h uses an ESTIMATED 1B research-policy subject with ESTIMATED four curriculum arms and ESTIMATED two seeds, at ESTIMATED six H100-hours per fine-tune: ESTIMATED 4×2×6=48. Subsequent campaigns require ESTIMATED 4×2×6=48 GPU-h for actual small-model training, plus ESTIMATED 16 GPU-h for trace filtering and repeated evaluation. This is a focused adapter-training pilot, not pretraining a research agent. The old estimate omits most downstream experimental work that defines the reward.
## 6. Duplicate check
Catalog T04: WEAK; its source trains transfer across fixed tool protocols rather than invention of missing operations. D21: MODERATE; its read contract jointly changes scaffold and policy, but evaluates protocol completion rather than curriculum-induced creation of new research affordances. These distinctions prevent a STRONG duplicate finding while leaving substantial methodological overlap.
## 7. Verdict
CUT, with ESTIMATED best-of-four excess 0.13 over its gate. The ESTIMATED pass probability exceeds its line by 0.28 and the projection is also unsafe. Unknown genuine abstraction demands do not outweigh the directly applicable synthesis-and-training stack.
## 8. Measurement status
Rollouts UNMEASURED (planned: curriculum-trained agents on omitted-operation campaigns). Grader noise UNMEASURED (planned: fixed tools and independently repeated downstream learning). Score ladder UNMEASURED (planned: generic coder, filtered imitation, combined curriculum, stronger causal-tool control).
## Screen record
id: C027
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.63
attack_single_range: 0.36-0.81
bo4_est: 0.73
pass4_est: 0.78
ub95_est: 0.89
gpuh_old: 16
gpuh_new_est: 112
duplicate_of: T04 WEAK; D21 MODERATE
kill_reason: executable skill curriculum plus ordinary coding transfer
souping_flag: no
