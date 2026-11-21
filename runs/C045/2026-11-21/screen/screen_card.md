# C045 — Pretraining with stateful external memory under update churn — saturation screen
## 1. What the grader actually rewards
Reward comes from subsequent next-event prediction after a bounded, model-written memory undergoes replacement, including queries whose supporting entries were displaced. Reads, writes and refresh learning consume the same allowance, so storing more or rebuilding everything cannot provide free recovery. ESTIMATED R≈0 is competent bounded retrieval with refresh/rehearsal and ESTIMATED R≈1 an attainable churn-adapted learner; the static-memory starter is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Combine learned key/value memory as in [Memorizing Transformers](https://arxiv.org/abs/2203.08913) with refresh machinery motivated by [REALM](https://arxiv.org/abs/2002.08909). Track entry provenance, access frequency and downstream dependency links; evict low-value leaves before shared supports when the replacement interface allows a choice. Re-embed stale keys, invalidate dependent cached representations, rehearse vulnerable information and consolidate predictable material into the allowed model parameters through metered training.

The strongest version should explicitly search write granularity, dependency-aware replacement, rehearsal frequency and refresh cadence, and compare a memory-light parameter-consolidation fallback. These mechanisms can be composed without assuming that a fixed-index retrieval paper already solves a learner that writes the representations on which it later depends. Under forced private replacement waves the controller can anticipate vulnerability but cannot simply veto all harmful evictions. All retained summaries and dependency metadata count against the external-state budget.

ESTIMATED single-run R=0.42, range ESTIMATED 0.21–0.59; ESTIMATED best-of-4=0.51; ESTIMATED pass@4 at R≥0.60=0.23; ESTIMATED projected upper-95% bound=0.68. These are subjective saturation-screen forecasts, not confidence limits fitted to data. The scale assumes the complete conventional refresh stack defines the competent floor and that the stated private model-written dependency mechanism supplies the residual utility. The attack recovers much immediate retrieval validity but misses learning-dependent recovery: rewriting one entry changes later training, which changes future keys and what needs rehearsal. This feedback makes a stale dependency graph an imperfect guide even when every recorded edge is handled correctly.
## 3. Other routes
Age/frequency-aware replacement plus scheduled re-embedding reaches ESTIMATED R=0.28, range ESTIMATED 0.10–0.47. It fixes ordinary staleness but treats future dependency value as exogenous.

A joint search over memory partitions, replay quotas, refresh intervals and write compression gives ESTIMATED R=0.36, range ESTIMATED 0.16–0.55. Search is credible within the target budget using short churn cycles, yet those cycles imperfectly predict later model-written dependencies. Parameter-only consolidation is a lawful alternative, ESTIMATED R=0.31, range ESTIMATED 0.11–0.53; its limit is the actual update cost and the fixed learner's capacity, not a prohibition on learning displaced information.
## 4. What would lower lawful saturation
Strengthen the existing churn generator by matching immediate retrieval loss between replacement alternatives while varying their later effects on learned write paths. Include shared supports and redundant entries so indiscriminate protection is wasteful, and preserve development observability of the relevant interactions. ESTIMATED attack R could fall to 0.34–0.43, costing ESTIMATED five author-weeks and ESTIMATED 320 H100 GPU-h to validate dependency interventions. This would add margin rather than repair a specific current kill. Randomly increasing eviction rate without changing learned dependencies would not help and could remove attainable reserve.
## 5. Decisive-check GPU-h re-estimate
Old pilot: ESTIMATED 18 GPU-h. New ESTIMATED 400 H100 GPU-h assumes an ESTIMATED 1B memory-augmented subject, ESTIMATED four policy arms, ESTIMATED three independent dependency/churn seeds and ESTIMATED 24 H100-hours per full training-and-replacement trajectory: ESTIMATED 4×3×24=288. Refresh/rehearsal work beyond the base trajectories adds ESTIMATED 64 GPU-h and next-event/dependency evaluation adds ESTIMATED 48 GPU-h. This is a bounded continuation study, not a claim that a full memory model can be pretrained cheaply. The original estimate substantially underprices endogenous dependency formation and recovery learning.
## 6. Duplicate check
Catalog T05: MODERATE, after reading its revision-safe agent-memory contract; it maintains factual validity across sessions, whereas C045's mutable memory is training state that changes later learning. Catalog T20: WEAK, using its inspected frozen-actor retrieval contract. V3 06A: WEAK, from its read compressed-attention target, which changes representation bytes rather than learned external write dependencies.
## 7. Verdict
PASS-SCREEN as a desk hypothesis. ESTIMATED margins are 0.28 for single-run, 0.09 for best-of-four, 0.27 for pass@4 and 0.07 for the projected bound. This is no empirical certification: native anchors and an attainable stronger learner remain UNMEASURED, and a universal consolidation/refresh winner would overturn the screen.
## 8. Measurement status
Rollouts UNMEASURED (planned: full dependency-forming and churn-recovery trajectories). Grader noise UNMEASURED (planned: repeated learning with fixed replacement waves). Score ladder UNMEASURED (planned: static memory, refresh/rehearsal, dependency controller and attainable churn-aware learner).
## Screen record
id: C045
verdict: PASS-SCREEN
binding_line: none
attack_single_est: 0.42
attack_single_range: 0.21-0.59
bo4_est: 0.51
pass4_est: 0.23
ub95_est: 0.68
gpuh_old: 18
gpuh_new_est: 400
duplicate_of: T05 MODERATE; T20 WEAK; 06A WEAK
kill_reason: none
souping_flag: no
