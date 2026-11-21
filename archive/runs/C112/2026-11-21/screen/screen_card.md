# C112 — Recover scientific images while learning a better acquisition policy — saturation screen
## 1. What the grader actually rewards
Restoration and sensing must jointly produce observations that train a better downstream learner on exact causal image tasks. Pixel reconstruction quality is a diagnostic, and all acquired measurements and restoration computation count against the budget. ESTIMATED R≈0 is the utility of a competent uncertainty-preserving restoration/acquisition baseline; ESTIMATED R≈1 is an attainable stronger closed-loop pipeline. Uniform sensing and the inherited restorer need native scores before placing the intended reference at ESTIMATED R≈0.60; an impossible imaging inverse cannot be used as the upper anchor.
## 2. Strongest lawful combined attack
The attacker should optimize sensing for decisions, not merely append variance maps to a pixel denoiser. [LOUPE](https://arxiv.org/abs/1907.11374) verifies joint sampling-pattern and reconstruction learning, although its sampling setting is not this card's full adaptive causal task. [Deep Adaptive Design](https://arxiv.org/abs/2103.02438) verifies amortized sequential experiment design, and [Amortized Bayesian Experimental Design for Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c59f05d7ab3638b138cc61f32e1a7cd1-Abstract-Conference.html) verifies a direct decision-oriented acquisition precedent. These are stronger controls than independent restoration and generic information gain.

Use multiple plausible reconstructions conditioned on the actual sensor likelihood, retain permitted raw residuals and acquisition history, and train a recurrent sensing policy against downstream task loss. Mix uniform exploration with decision-sensitive acquisition so confident reconstruction artifacts do not permanently remove a region from consideration. Short development campaigns can compare posterior disagreement, task disagreement and expected downstream improvement; final selection uses freshly trained learner utility. All simulation, policy training and sensor calls are paid. The known methods support this architecture but do not establish its performance on the proposed hidden noise/structure dependencies.

ESTIMATED single-run R=0.45, range 0.26–0.65; ESTIMATED oracle best-of-4=0.55; ESTIMATED pass@4 at R≥0.60=0.33; ESTIMATED projected upper-95% score=0.72. The residual is shared inverse-model misspecification: plausible-looking reconstructions can agree while omitting a small causal feature, and learning which alternative measurement exposes it requires generalizing the observation process. Task-driven acquisition reduces this risk substantially, so variance failure alone cannot justify a lower forecast. A simple raw-observation bypass could also make this card much easier than intended.
## 3. Other routes
An uncertainty ensemble with expected information gain is the strongest single ordinary recipe. ESTIMATED R=0.32, range 0.17–0.53. It handles noise and many artifacts but can spend measurements on high-variance regions irrelevant to the causal endpoint.

Search across reconstruction regularization, posterior temperature, acquisition lookahead, raw-residual channels and exploration fractions has ESTIMATED R=0.41, range 0.22–0.62. Development tasks must charge full learner retraining; selecting only pixel metrics would understate the true attack. A raw-image recurrent acquisition network without an explicit restored image is lawful if permitted, ESTIMATED R=0.46, range 0.24–0.72. Its comparison tests whether restoration is a necessary intervention rather than an avoidable lossy bottleneck.
## 4. What would lower lawful saturation
Commit to identifiable noise/structure aliases where a small causal feature and an artifact initially look alike but a disclosed affordable sensor action distinguishes them. Cross task relevance with image appearance, retain a predictive protected development slice, and evaluate both raw-observation and decision-focused joint controls. ESTIMATED attack reduction is 0.05–0.11, to roughly 0.34–0.40. ESTIMATED authoring effort is 14–24 person-days plus 200 H100-h for observation-process validation. If only the privileged clean image identifies the correct action, reject the instance rather than calling it difficult.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 18 GPU-h. New ESTIMATED budget: 160 H100 GPU-h. Assume 100M–300M restoration/acquisition models and a 100M downstream learner: 4 coupled arms × 3 seeds × 8 H100-h training = 96; downstream learner rebuilds, 4 × 3 × 3 H100-h = 36; closed-loop sensor and exact causal-task evaluation = 16; repeated grades and raw-bypass control preparation = 12. ESTIMATED sum 96+36+16+12=160. CPU rendering is separately costed. The earlier estimate can compare pretrained restorers but misses the task-dependent acquisition and learner stages.
## 6. Duplicate check
T10, MODERATE: its opened source learns budgeted crop/revisit acquisition, but C112 changes the restoration process that determines what evidence reaches that policy. FIX T11, WEAK: it tests grounded visual/temporal learning on truth-changing media, without adaptive sensor reconstruction. No indexed task shares both the joint inverse-model intervention and the downstream acquisition-dependent training target.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 is only 0.05 below its kill threshold and the projected score bound only 0.03 below its limit. Require the identifiable observation aliases and the complete raw-observation/decision-focused controls; a variance-only baseline would be insufficient evidence of reserve.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent joint sensing/restoration development attempts). Grader noise UNMEASURED (planned: fixed-policy acquisition repeats, observation noise seeds and downstream learner rebuilds). Score ladder UNMEASURED (planned: uniform sensing, pixel restorer, uncertainty acquisition, direct task-driven policy, reference and stronger feasible pipeline).
## Screen record
id: C112
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.45
attack_single_range: 0.26-0.65
bo4_est: 0.55
pass4_est: 0.33
ub95_est: 0.72
gpuh_old: 18
gpuh_new_est: 160
duplicate_of: T10 MODERATE; FIX T11 WEAK
kill_reason: none
souping_flag: no
