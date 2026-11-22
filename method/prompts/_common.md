HARD LIMITS (non-negotiable; they apply to every stage)
- CPU and desk work only. No GPU jobs, no training, no rollouts, nothing that spends money. You may reason, search and fetch from the web (if web search is enabled), and read the files in this working directory.
- Do not write to any Google Doc. Send nothing, contact no one, and share nothing outside the team.
- Write ONLY inside out/. Never modify task/, method/, peers/, prior/ or grader_src/. Treat every file outside out/ as read-only.
- Do not try to find the repository this task came from, other tasks' run records, the grader's hidden data, secret seeds, or prior verdicts for this task. If you can see them, you are not meant to; do not use them.
- Never read, print or write keys, tokens, credentials or .env files.
- Never invent numbers or sources. Every number you produce is a forecast and must be labelled ESTIMATED. Every measurement field (rollout scores, grader noise, score ladders, observed runs) is UNMEASURED, followed by the planned measurement.
  - Cite only sources you opened in this session (title, author or org, year, URL). Mark each one "fetched" or "search-only".
  - If you cannot verify a source, write "unverified" and give no URL.
- Souping and model merging (weight averaging, model soups, task arithmetic, TIES/DARE, any merging) are EXCLUDED entirely. Never use them as an attack, a fix or a redesign ingredient. If the task's core depends on them, write souping_flag: yes and give the verdict CUT.
- Grader access is limited to the interface in task/grader_interface.md. Do not assume grader internals, hidden seeds or private data. (The white-box exploit probe is the one exception, and only for the read-only copy in grader_src/.)
- Do not write or run any script that generates, templates or batch-writes your report's prose. Write it by hand, specifically for this task. Ordinary read-only shell commands are fine.

WORKING DIRECTORY (everything you may read is here; this is your whole world)
- task/card.md             the task card: problem, action surface, reward, budget, submission format.
- task/grader_interface.md the black-box grader interface (the only way scores are obtained).
- task/sota_sources.md     the evidence the task was filed with (may be absent; then find sources yourself).
- task/task_public.yaml    the machine-readable task spec (hidden data and the grader source location are removed).
- task/extra/              any extra task inputs (may be absent).
- method/                  the method files named in your stage instructions below.
- peers/                   other tasks' cards, for duplicate checks only (may be absent).
- out/                     the ONLY place you write.

THE BAR (attacker = a frontier model or agent system, ~10T parameters by assumption, {{WALLCLOCK_HOURS}} hours of test-time compute, full lawful tool access in the task)
CUT if, by ESTIMATED reckoning, ANY of these holds:
- a single valid run is likely > {{SINGLE_MAX}};
- the oracle best-of-4 mean is > {{BO4}};
- pass@4 at R >= {{TAU}} is > {{PASS4}};
- the projected upper-95% bound is >= {{UB95}}.

Lawful known recipes, paper recall and lawful generalization are valid solutions. Never rescue a task by forbidding a lawful winning method.

PROMOTION GATE (Amita, Nov 21 2026, 3:02 PM PT)
The STRICT rule is the promotion gate. The anchored verdict is an upper bound on survival, not the decision that advances a task.
- If attack_basis is LITERATURE-ONLY or ASSUMED, use the evidence-only / pre-anchoring scores and verdict. Treat that attack as executable by a {{WALLCLOCK_HOURS}}-hour frontier agent.
- Only DEMONSTRATED-AGENT evidence may lower an attack score below that pre-anchoring estimate.
Record both the evidence-only (or earlier-stage) verdict and the anchored verdict. The pipeline maps them to strict_verdict (the gate) and anchored_verdict (the upper bound). See method/evidence_grounding_rule.md.

HOW TO ESTIMATE
1. Derive the single-run estimate component by component: which part of the reward each attack component captures, how strongly the evidence supports it, and what residual remains.
2. State the run-to-run spread for THIS task and where it comes from (seed noise, whether the search finds the key insight, which is often bimodal, grader noise, workload variance).
3. From that stated distribution, derive:
   - best-of-4: the expected max of 4 runs;
   - pass@4 = 1 - (1 - p)^4, where p = P(single R >= {{TAU}});
   - ub95: the 95th percentile of the single-run distribution.
4. Show the short arithmetic. Never apply a fixed offset between single and best-of-4. Use two decimals.

Spread the scores honestly: don't park every task at 0.55-0.60.

CHECKPOINTING
If out/ already holds a partial report, continue it rather than starting over. When finished, write out/DONE.txt with one line: "<ISO time> {{TASK_ID}} {{STAGE}} verdict=<V>".
