# C044 — Choose pretraining architectures using downstream editability — saturation screen
## 1. What the grader actually rewards
The experiment plan selects an architecture, after which a fixed bounded adaptation procedure must implement new code behavior while retaining old behavior. Current perplexity is only evidence; post-update executable utility under total research and adaptation cost determines reward. ESTIMATED R≈0 is competent loss-plus-adaptation selection and ESTIMATED R≈1 an attainable sequential-editability selector; the loss-only campaign is provisionally ESTIMATED R=0.00 and reference ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Measure more than validation loss: run small sequential edit probes, estimate gradient interference and retained-behavior degradation, then allocate architecture continuation to candidates with favorable joint predictions. [Editable Neural Networks](https://arxiv.org/abs/2004.00345) establishes edit locality as a trainable property; [MEND](https://arxiv.org/abs/2110.11309) demonstrates explicit locality-oriented editing machinery. Here those sources motivate measurements, not permission to replace the grader's frozen adaptation algorithm with a learned editor.

Fit a cost-sensitive surrogate over architecture features, pretraining loss and edit-interference traces. Use [multi-task Bayesian optimization](https://proceedings.neurips.cc/paper/2013/hash/f33ba15effa5c10e873bf3842afb46a6-Abstract.html) to transfer information across permitted development edit families, and retain finalists through longer edit chains before choosing. Include broad modular/dense candidates only within the declared architecture space and full training ledger. This stack is more potent than generic few-shot fine-tuning because it directly targets the downstream metric.

ESTIMATED single-run R=0.48, range ESTIMATED 0.26–0.67; ESTIMATED best-of-4=0.57; ESTIMATED pass@4 at R≥0.60=0.37; ESTIMATED projected upper-95% bound=0.72. The scale places ordinary adaptation probes in the floor and leaves reward for predicting architecture ordering after dependent update sequences. Local gradient alignment supplies partial signal but may miss representations whose locality changes after earlier edits. The residual is a transfer problem from cheap measurements to a later learning state, not an assumption that a frontier model cannot implement standard architecture search. A tiny candidate set with stable rankings would raise the forecast sharply.
## 3. Other routes
A fixed sequential adaptation benchmark used to rank every candidate reaches ESTIMATED R=0.39, range ESTIMATED 0.18–0.60. Its weakness is spending comparable probe effort on obvious losers and trusting a single edit family.

A multi-fidelity sweep over candidate architecture, probe length and selection weights gives ESTIMATED R=0.44, range ESTIMATED 0.23–0.64. This may discover that one general modular design wins universally, a lawful saturation result that the task must accept. Choosing solely by pretraining loss is expected to reach ESTIMATED R=0.18, range ESTIMATED 0.03–0.42 on the provisional residual scale; that low value requires actual ranking reversals rather than a narrative about perplexity being imperfect.
## 4. What would lower lawful saturation
Construct independent edit mechanisms with matched initial loss and matched isolated-edit response, but different architecture rankings after related sequential changes. The development proxy must permit probing those interactions, and candidate architectures must remain trainable under the common budget. ESTIMATED attack R would move toward 0.39–0.49 and ESTIMATED best-of-four toward 0.53. ESTIMATED cost is six author-weeks and ESTIMATED 480 H100 GPU-h to validate ranking reversals across pretraining seeds. This matched-probe generator is the exact required change; increasing architecture count would only enlarge the search.
## 5. Decisive-check GPU-h re-estimate
Old card figure: ESTIMATED 16 GPU-h. New ESTIMATED 480 H100 GPU-h assumes ESTIMATED four 1B-scale architecture candidates, ESTIMATED two pretraining seeds and ESTIMATED 40 H100-hours per candidate/seed: ESTIMATED 4×2×40=320. Run ESTIMATED three sequential edit chains per checkpoint at ESTIMATED four H100-hours each: ESTIMATED 4×2×3×4=96. Research-plan proxy arms and full old/new executable evaluation add ESTIMATED 64 GPU-h. This shares immutable candidate checkpoints across selectors where valid. The old allowance ignores architecture construction and repeated downstream learning, which dominate the decisive experiment.
## 6. Duplicate check
T03: MODERATE, from its read live experiment-selection contract, but C044 selects architecture by future local adaptation rather than generic campaign outcome. FIX T09: WEAK, after inspecting its fixed-architecture sparse-coordinate intervention. D23: WEAK, after reading its evidence-recoverability target; retaining a pre-action assay differs from executable code editability. None is a STRONG match.
## 7. Verdict
CONDITIONAL with ESTIMATED best-of-four margin 0.03 and projected-bound margin 0.03. Require matched isolated probes with consequential sequential ranking reversals before claiming a robust margin. Ordinary edit-aware Bayesian search remains a serious saturation route.
## 8. Measurement status
Rollouts UNMEASURED (planned: architecture-selection plans over fresh edit chains). Grader noise UNMEASURED (planned: pretraining and adaptation seed replication). Score ladder UNMEASURED (planned: loss ranker, isolated probes, sequential selector and stronger editability control).
## Screen record
id: C044
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.48
attack_single_range: 0.26-0.67
bo4_est: 0.57
pass4_est: 0.37
ub95_est: 0.72
gpuh_old: 16
gpuh_new_est: 480
duplicate_of: T03 MODERATE; FIX-T09 WEAK; D23 WEAK
kill_reason: probe-transfer uncertainty near gates; require sequential ranking reversals
souping_flag: no
