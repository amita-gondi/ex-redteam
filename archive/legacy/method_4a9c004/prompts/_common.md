HARD LIMITS (non-negotiable; they apply to every stage)
- CPU and desk work only. No GPU jobs, no training, no rollouts, nothing that spends money. You may reason, search and fetch from the web, and read the local files named below.
- Do not write to any Google Doc. Send nothing, contact no one, and share nothing with any lab, GDM or anyone outside the team.
- Write ONLY to {{OUT_DIR}}/. Never modify tasks/, method/, config/ or any earlier run.
- Never read, print or write keys, tokens, credentials or .env files.
- Never invent numbers or sources. Every number you produce is a forecast and must be labelled ESTIMATED. Every measurement field (rollout scores, grader noise, score ladders, observed runs) is UNMEASURED, followed by the planned measurement.
  - Cite only sources you opened in this session (title, author or org, year, URL). Mark each one "fetched" or "search-only".
  - If you cannot verify a source, write "unverified" and give no URL.
- Souping and model merging (weight averaging, model soups, task arithmetic, TIES/DARE, any merging) are EXCLUDED entirely. Never use them as an attack, a fix or a redesign ingredient. If the task's core depends on them, write souping_flag: yes and give the verdict CUT.
- Grader access is limited to the interface described in the task's grader.md. Do not read grader internals, hidden seeds or private data, even if you find them.
- Do not write or run any script that generates, templates or batch-writes your report's prose. Write it by hand, specifically for this task. Ordinary read-only shell commands are fine.

TASK FILES (read fully; read-only)
- {{TASK_DIR}}/card.md
- {{TASK_DIR}}/grader.md   (if absent, say so and use the grader description in card.md)
- {{TASK_DIR}}/sota_sources.md   (if absent, say so; you must then find the sources yourself)

METHOD FILES (read-only)
- method/kill_thresholds.md: the kill lines, the attacker model, and why a panel can kill but not clear.
- method/evidence_grounding_rule.md: DEMONSTRATED-AGENT vs LITERATURE-ONLY vs ASSUMED.
- method/verdict_schema.md: the field meanings.

THE BAR (attacker = a frontier model or agent system, ~10T parameters by assumption, 12 hours of test-time compute, full lawful tool access in the task)
CUT if, by ESTIMATED reckoning, ANY of these holds:
- a single valid run is likely > 0.70;
- the oracle best-of-4 mean is > 0.60;
- pass@4 at R ≥ 0.60 is > 0.50;
- the projected upper-95% bound is ≥ 0.75.

Lawful known recipes, paper recall and lawful generalization are valid solutions. Never rescue a task by forbidding a lawful winning method.

PROMOTION GATE (Amita, 3:02 PM PT, Nov 21 2026)
The **strict** rule is the promotion gate. The anchored verdict is an upper bound on survival, not the decision that advances a task.
- If attack_basis is LITERATURE-ONLY or ASSUMED, use the evidence-only / pre-anchoring scores and verdict. Treat that attack as executable by a 12-hour frontier agent.
- Only DEMONSTRATED-AGENT evidence may lower an attack score below that pre-anchoring estimate.
Record both the evidence-only (or earlier-stage) verdict and the anchored verdict. The wrapper maps them to `strict_verdict` (the gate) and `anchored_verdict` (the upper bound). See method/evidence_grounding_rule.md.

HOW TO ESTIMATE
1. Derive the single-run estimate component by component: which part of the reward each attack component captures, how strongly the evidence supports it, and what residual remains.
2. State the run-to-run spread for THIS task and where it comes from (seed noise, whether the 12-hour search finds the key insight, which is often bimodal, grader noise, workload variance).
3. From that stated distribution, derive:
   - best-of-4: the expected max of 4 runs;
   - pass@4 = 1 − (1 − p)^4, where p = P(single R ≥ 0.60);
   - ub95: the 95th percentile of the single-run distribution.
4. Show the short arithmetic. Never apply a fixed offset between single and best-of-4. Use two decimals.

Spread the scores honestly: don't park every task at 0.55–0.60.

CHECKPOINTING
If {{OUT_DIR}}/ already holds a partial report, continue it rather than starting over. When finished, write {{OUT_DIR}}/DONE.txt with one line: "<ISO time> {{TASK_ID}} {{STAGE}} verdict=<V>".
