# C010 — Train through delayed simulator corrections — saturation screen
## 1. What the grader actually rewards
Replay selection is valuable when chronological contact-label corrections improve a robot policy's completion on new manipulation geometries. Stored observations, recurrent context and any other retained replay content all count against the byte budget, so saving a compact-looking index cannot make its referenced frames free. ESTIMATED R≈0 is the competent corrected-replay floor and ESTIMATED R≈1 an achievable stronger retention policy; inherited FIFO is tentatively ESTIMATED R=0.00 and reference learning ESTIMATED R=0.60 until their native success rates are established.
## 2. Strongest lawful combined attack
Use correction-aware prioritized sequence replay with a mixture of recent, rare-contact and uniform-reservoir storage. Track which transitions share a contact episode, invalidate affected targets when an authorized correction arrives, and replay overlapping predecessor windows with recomputed recurrent states. [R2D2](https://openreview.net/pdf/387fb2fcee8f74c53cf707a9856f40c458f33933.pdf) verifies recurrent replay and the importance of state staleness; [Hindsight Experience Replay](https://arxiv.org/abs/1707.01495) verifies relabeling as a concrete replay technique. Contact-truth revision differs from changing a goal, so HER does not justify relabeling unseen physics or recovering discarded observations.

The combined policy allocates memory by expected correction sensitivity per byte, using public contact uncertainty, episode rarity and observed correction delays. Keep sparse keyframes and dense windows around plausible contact boundaries, with a small random reserve for confidently misclassified cases. Search window length and storage mixtures jointly on legal dev corrections. At every update, only labels that have arrived can affect replay; future simulator truth is unavailable. Compression is allowed only insofar as the actual stored representation remains sufficient for the fixed learner and its bytes are counted.

ESTIMATED single-run R=0.46, range 0.25–0.64; ESTIMATED oracle best-of-4=0.56; ESTIMATED pass@4 at R≥0.60=0.34; ESTIMATED upper-95% projection envelope=0.72. These are desk forecasts. The stack recovers local credit propagation and repeated contact motifs. Its residual is prospective retention: before receiving a correction it may not know which earlier apparently ordinary observation changes the interpretation of a later contact. Extending every replay window consumes the scarce resource and does not solve selective sufficiency. If complete trajectories fit cheaply, however, the residual disappears and the score forecast should rise sharply.
## 3. Other routes
- Ordinary prioritized relabeling with a fixed recurrent burn-in is the strongest single recipe: ESTIMATED R=0.34, range 0.16–0.54. It repairs nearby targets but loses dependencies outside its retained window.
- Search byte allocation among full trajectories, keyframes, recent windows and rare-contact buffers, with dev success rather than replay loss selecting the winner. ESTIMATED R=0.42, range 0.22–0.62. Cheap storage-policy replay can narrow the expensive policy-training choices.
- Preserve a uniform sample of complete episodes and relabel them fully after correction. ESTIMATED R=0.39, range 0.17–0.65. This is an essential bypass because causal dependency heuristics may not outperform simple trajectory coverage.
## 4. What would lower lawful saturation
Freeze a storage envelope where retaining every unresolved trajectory is infeasible but a same-budget reference can retain sufficient causal evidence. Include matched local and long-range correction cases, and hold out which observable earlier event governs the corrected contact interpretation. Dev must contain an analogous sufficiency problem, not a hidden-only delay increase. Expected revised composite: ESTIMATED R=0.36, best-of-four=0.46, pass@4=0.17 and upper envelope=0.64. Cost is ESTIMATED several weeks of contact-dependency authoring and ESTIMATED 180 additional H100 GPU-h for memory-pressure and transfer comparisons. The reference must not choose storage using future labels.
## 5. Decisive-check GPU-h re-estimate
Old figure: ESTIMATED 14 GPU-h. Revised ESTIMATED 120 H100 GPU-h assumes an ESTIMATED 100M-parameter visuomotor learner, ESTIMATED 4 replay policies, ESTIMATED 3 seeds and ESTIMATED 8 H100-hours per full correction-wave training run, plus ESTIMATED 24 GPU-h of fresh-geometry completion evaluation: ESTIMATED 4×3×8+24=120. Simulator collection and retained-byte tracing add CPU work and wall time. The old figure might reveal whether relabeling changes gradients but undercounts closed-loop retraining and geometric transfer. A larger vision backbone or expensive contact simulation requires a separately profiled budget.
## 6. Duplicate check
FIX T13 (`fix_packets_v4/T13/packet.md`, source opened): WEAK; it grounds passive egocentric data into control, whereas C010 chooses replay content before retroactive truth changes arrive. D03 (`hidden_task_cards_v4/cards/D03.md`, opened): MODERATE, sharing revised historical credit, but its artifact settles reward ledgers across resets rather than retaining observations to train manipulation behavior. Neither match has the same intervention and scientific endpoint together.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-four clears its threshold by only 0.04 and the upper projection by ESTIMATED 0.03. Require the explicit byte-pressure/sufficient-causal-evidence generator above; delay alone is insufficient. This preserves a plausible research problem while excluding the easy full-trajectory-storage regime by a scientifically justified resource contract.
## 8. Measurement status
Rollouts UNMEASURED (planned: retention policies with correction-arrival ledgers). Grader noise UNMEASURED (planned: paired simulator and training seeds plus repeated fixed-policy completions). Score ladder UNMEASURED (planned: FIFO, local relabeling, complete-episode reservoir, correction-aware selection and legal sufficient-evidence reference).
## Screen record
id: C010
verdict: CONDITIONAL
binding_line: none
attack_single_est: 0.46
attack_single_range: 0.25-0.64
bo4_est: 0.56
pass4_est: 0.34
ub95_est: 0.72
gpuh_old: 14
gpuh_new_est: 120
duplicate_of: FIX-T13 WEAK; D03 MODERATE
kill_reason: require real byte pressure and nonanticipatory causal retention
souping_flag: no
