You are doing a CPU-only DESK SATURATION SCREEN of one RL-environment research task. Task: {{TASK_ID}} (version {{TASK_VERSION}}). Date: {{DATE}}. Method version: {{METHOD_VERSION}}.

{{COMMON}}

METHOD FILES (read-only)
- method/kill_thresholds.md: the kill lines, the attacker model, and why a panel can kill but not clear.
- method/evidence_grounding_rule.md: DEMONSTRATED-AGENT vs LITERATURE-ONLY vs ASSUMED.
- method/verdict_schema.md: the field meanings.

STAGE-SPECIFIC INPUTS
- The canonical pairing set for any later rollout is in task/task_public.yaml. It does not affect this desk screen.
- Do not anchor on the card's own attack estimate. Re-derive it.

WRITE out/screen_card.md with exactly these sections. The headings are fixed; all prose is hand-written and task-specific, about 600-1100 words.

# {{TASK_ID}}: <task title>: saturation screen
## 1. What the grader actually rewards
2-4 sentences, in your own words, including what R~0 and R~1 correspond to.
## 2. Strongest lawful combined attack
- Name concrete known methods, libraries and papers (each verified, with its URL) and HOW they combine into the stack a 10T/{{WALLCLOCK_HOURS}}h agent would actually run.
- Then give ESTIMATED single-run R (point + range), ESTIMATED best-of-4, ESTIMATED pass@4 at R>={{TAU}} and ESTIMATED upper-95%, derived as in HOW TO ESTIMATE.
- Explain the residual: what part of the reward the stack can't get, and why.
## 3. Other routes
At least two, each with ESTIMATED R and range:
- (a) the strongest single standard recipe;
- (b) a search/autotune/sweep route;
- optionally (c) a lawful-looking shortcut or grader-gaming route.
## 4. What would lower lawful saturation
Specific design changes, the ESTIMATED effect of each on the attack, and the ESTIMATED cost (GPU-h, authoring effort).
## 5. Decisive-check GPU-h estimate
An explicit breakdown (model size, arms, seeds, hours per run, H100, eval overhead) with the arithmetic. This is a plan only; nothing is run.
## 6. Duplicate check
Nearest peer cards in peers/ that you actually opened, each rated NONE / WEAK / MODERATE / STRONG with a one-sentence reason. If peers/ is empty, say so.
## 7. Verdict
- PASS-SCREEN: clearly below every line, with a margin of more than ~0.05 on all four.
- CONDITIONAL: within ~0.05 of a line, or survives only with a stated design change. Give the exact change and its cost.
- CUT: over a line (say which), a souping dependency, or a STRONG duplicate.
## 8. Measurement status
Rollouts UNMEASURED (planned ...), grader noise UNMEASURED (planned ...), score ladder UNMEASURED (planned ...).
## Screen record
(machine-readable, one per line, exactly these keys; numbers are ESTIMATED)
id: {{TASK_ID}}
verdict: PASS-SCREEN|CONDITIONAL|CUT
binding_line: single>0.70|bo4>0.60|pass4>0.50|ub95>=0.75|none|duplicate|souping
attack_single_est: 0.xx
attack_single_range: 0.xx-0.xx
bo4_est: 0.xx
pass4_est: 0.xx
ub95_est: 0.xx
gpuh_new_est: N
duplicate_of: <id(s) and strength, or none>
kill_reason: <short phrase, or none>
souping_flag: yes|no
