# C117 — A data flywheel that retires solved failure modes — saturation screen
## 1. What the grader actually rewards
The flywheel must produce successive coding-agent improvements on exact private repairs while retaining earlier skills. Generated, rejected, retired and replayed examples all consume resources; deleting a solved category receives no reward unless later learning improves. ESTIMATED R≈0 denotes a competent progress-based generation/replay floor, while ESTIMATED R≈1 denotes attainable stronger coding gains at the same full cost. A frozen hard corpus and the original agent need native scores before interpreting the intended ESTIMATED reference near 0.60.
## 2. Strongest lawful combined attack
Maintain current-checkpoint success estimates by bug mechanism, refresh them after learning, and generate examples around unsolved combinations rather than repeatedly mutating surface syntax. [Prioritized Level Replay](https://proceedings.mlr.press/v139/jiang21b.html) verifies staleness-aware selection by learning potential. Combine it with a small mechanism-stratified replay reservoir and conservative retirement: reduce a family's generation rate after repeated success, but retain representative precursor examples and periodically challenge it with composed bugs.

[Maximally Interfered Retrieval](https://arxiv.org/abs/1908.04742) verifies replay selection based on predicted interference from an imminent update. Use that idea on cheap candidate updates to identify apparently solved examples whose losses would rise, then preserve them in the next training mix. [Gradient Episodic Memory](https://arxiv.org/abs/1706.08840) provides an additional established retention control where its cost is justified. Executable tests label generated repairs; full development rounds select generation/retirement thresholds and replay ratios. No parameter averaging or model combination is needed: candidates are independently charged and one is selected.

ESTIMATED single-run R=0.69, range 0.47–0.85; ESTIMATED oracle best-of-4=0.78; ESTIMATED pass@4 at R≥0.60=0.91; ESTIMATED projected upper-95% score=0.92. Long-term prerequisite value can remain invisible to short lookahead, especially when a precursor is easy alone but essential in a later repair. The proposed combined-bug probes and retained mechanism reservoir address much of that risk. The card does not quantify a delayed dependency that makes ordinary conservative replay too costly or ineffective.
## 3. Other routes
Current-competence sampling with a fixed stratified replay buffer is the strongest single recipe. ESTIMATED R=0.56, range 0.35–0.76. It should eliminate most redundant generation while avoiding catastrophic retirement.

A sweep over retirement patience, confidence threshold, replay capacity, checkpoint refresh interval and composition depth has ESTIMATED R=0.65, range 0.41–0.83. Search must use complete learning rounds; static success classification would miss interference. Another lawful route never fully retires a mechanism, merely downweights it smoothly. ESTIMATED R=0.62, range 0.38–0.82. If modest residual replay is cheap, this simple policy avoids the purported hard binary decision and could match the more elaborate flywheel.
## 4. What would lower lawful saturation
Build real repair-learning histories where several apparently redundant precursor families support different later bug combinations and storage/exposure limits make replaying every precursor expensive. Include affordable causal probes and representative development combinations, keeping an attainable nonuniform retention solution. ESTIMATED attack reduction is 0.12–0.20, to about 0.49–0.57. ESTIMATED cost is 12–20 person-days plus 280 H100-h for delayed-interference histories. A smaller arbitrary replay cap without a feasible stronger policy would only depress the ceiling.
## 5. Decisive-check GPU-h re-estimate
Old value from card: ESTIMATED 18 GPU-h. New ESTIMATED cost is 240 H100 GPU-h. With a 4B coding agent, allocate 4 flywheel arms × 2 seeds × 3 learning rounds × 6 H100-h = 144; checked generation and candidate-update interference probes add 48; independent composed-bug and old-skill evaluation adds 32; repeated grades add 16. ESTIMATED total 144+48+32+16=240. This assumes adapter continuation rather than pretraining a coding model. The old estimate could compare one corpus refresh but not the delayed support value across successive updates.
## 6. Duplicate check
01B, MODERATE: its source acquires experience as the learner changes and tests retention, but C117 generates coding-repair examples and explicitly retires their support. D26, MODERATE: its source anticipates post-update gradient value when allocating trajectories; it has a fixed acquisition/sketch interface rather than a self-generated repair-data flywheel. The changed generation treatment prevents a STRONG duplicate finding despite close learning dynamics.
## 7. Verdict
CUT. ESTIMATED best-of-4 crosses its line by 0.18 and pass@4 by 0.41. Checkpoint-refreshed competence plus interference-aware conservative replay supplies a direct lawful response to both repetition and premature retirement.
## 8. Measurement status
Rollouts UNMEASURED (planned: independent flywheel construction spanning successive repair updates). Grader noise UNMEASURED (planned: fixed-policy generation, training seeds and composed-bug evaluation repeats). Score ladder UNMEASURED (planned: frozen corpus, progress sampling, conservative replay, interference replay, reference and stronger support-allocation control).
## Screen record
id: C117
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.69
attack_single_range: 0.47-0.85
bo4_est: 0.78
pass4_est: 0.91
ub95_est: 0.92
gpuh_old: 18
gpuh_new_est: 240
duplicate_of: 01B MODERATE; D26 MODERATE
kill_reason: refreshed competence and interference aware replay avoid redundant data and forgetting
souping_flag: no
