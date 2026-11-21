# C086 — Research world models graded only by executed improvements — saturation screen
## 1. What the grader actually rewards
A trained proposal agent is reset on fresh LM-development projects, and only its executed improvements in protected training outcomes count. Proposal generation, surrogate refreshes and failed true runs all consume the utility budget. R≈0 denotes the strongest execution-grounded ordinary optimizer, R≈1 is an attainable transferable proposer, and the no-op/reference anchors are provisionally ESTIMATED R=0.00/0.60; better surrogate rankings alone have no reward meaning.
## 2. Strongest lawful combined attack
Reproduce the proposal-learning loop from verified [Language Models Learn to Improve Language Models](https://arxiv.org/abs/2610.23344), whose [project page](https://a-evo-lab.github.io/lm2lm/index.html) distinguishes real runs from predictions. Combine learned proposals with several independently fitted outcome predictors, disagreement-targeted true execution, conservative gain estimates and trust-region search around validated recipes. [AdaScale-TuRBO](https://github.com/PaulsonLab/AdaScale-TuRBO) supplies a concrete conventional black-box optimizer for numerical recipe subspaces. Predictor disagreement guides which experiment to run; no model parameters are combined.

The strongest bypass must also be attempted: skip proposal training and spend the same budget on direct execution-grounded optimization, then train the proposer only if its amortized benefit exceeds that opportunity cost. This stack handles optimism in familiar regions and can fall back to known recipes. It still lacks reliable knowledge of new architecture/data interactions when several predictors share the same blind spot, and every disambiguating observation requires real training rather than a cheap surrogate call. ESTIMATED single-run R=0.40, range 0.20–0.57; ESTIMATED oracle best-of-4=0.50; ESTIMATED pass@4 at R≥0.60=0.12; ESTIMATED projected upper-95% bound=0.67. The favorable screen rests on the card's promised held-out model mechanisms, not a belief that larger agents will fail to refresh obvious uncertain proposals.
## 3. Other routes
- Execution-grounded trust-region optimization over the inherited numerical recipe is ESTIMATED R=0.34, range 0.15–0.54. It is a serious proposer-training bypass but cannot express every architectural intervention through a fixed numeric parameterization.
- Evolutionary proposal search with short-run screening and true-run confirmation is ESTIMATED R=0.37, range 0.18–0.56. Search can discover local improvements, while cross-family transfer and misleading short curves limit its amortization.
- The published refresh loop without explicit disagreement probes is ESTIMATED R=0.29, range 0.11–0.49. It spends fewer executions on exploration but risks reinforcing regions that merely look optimistic to its surrogate.
## 4. What would lower lawful saturation
Hold out causal model/data interactions rather than model names, and require matched development interventions that permit learning how those interactions alter proposal value. Test a trained proposer against direct numerical and code-proposal optimizers after charging its full training cost. ESTIMATED attack could fall to R=0.31–0.43, with ESTIMATED added effort of several author-weeks and ESTIMATED 320 H100 GPU-h for fresh execution records. Reject the design if ordinary optimization already reaches the attainable control or if transfer requires an inaccessible family label. A larger proposal model by itself supplies neither meaningful novelty nor a valid hardness argument.
## 5. Decisive-check GPU-h re-estimate
The card's old value is ESTIMATED 20 GPU-h. New ESTIMATED total: 1,200 H100 GPU-h. Assume an ESTIMATED 3B proposer adapted through bounded fine-tuning and ESTIMATED 125M/1B downstream subjects. ESTIMATED 4 refresh/optimizer strategies × 2 independent seeds × 24 downstream probes × 4 H100-hours = 768 GPU-h; proposer adaptation costs ESTIMATED 4 strategies × 2 seeds × 24 GPU-h = 192 GPU-h; transfer confirmation costs ESTIMATED 8 continuations × 24 H100-hours = 192 GPU-h; add ESTIMATED 48 GPU-h for grading and replay. The earlier budget omits the nested campaign: even cheap individual experiments become expensive when acquiring enough true outcomes to evaluate a learned research policy.
## 6. Duplicate check
Catalog T03 — MODERATE: its inspected reusable controller also selects live experiments, but C086 trains the proposal-generating weights through a surrogate/real-execution loop. D21 — WEAK: its opened specification co-adapts tool scaffolds and policy under versioned replay, rather than learning transferable LM-improvement proposals. The different learned artifact and downstream training objective prevent a strong duplicate finding.
## 7. Verdict
PASS-SCREEN. ESTIMATED point margins are 0.30 below the single-run line, 0.10 below best-of-4, 0.38 below pass@4 and 0.08 below the upper-bound cutoff. The decision concerns an unimplemented fresh-mechanism design and remains contingent on actual native reserve, not surrogate self-reported progress.
## 8. Measurement status
Rollouts UNMEASURED (planned: reset trained proposers and direct-optimizer bypasses); grader noise UNMEASURED (planned: nested campaign/training-seed replication); score ladder UNMEASURED (planned: fixed recipes, direct optimization, published proposer and independently stronger transfer control).
## Screen record
id: C086
verdict: PASS-SCREEN
binding_line: none
attack_single_est: 0.40
attack_single_range: 0.20-0.57
bo4_est: 0.50
pass4_est: 0.12
ub95_est: 0.67
gpuh_old: 20
gpuh_new_est: 1200
duplicate_of: catalog T03 MODERATE; D21 WEAK
kill_reason: none
souping_flag: no
