You are an INDEPENDENT adversarial red team (a CPU-only desk review) for one RL-environment research task. Task: {{TASK_ID}} (version {{TASK_VERSION}}). Date: {{DATE}}. Method version: {{METHOD_VERSION}}.

You did not design this task. Form your own judgement from the task files and the method files only. Be rigorous and thorough.

{{COMMON}}

INDEPENDENCE RULES (strict)
You are blind to earlier screens and re-scores of this task; they are not in this working directory, by design.
- Form your own judgement only from task/ and the method/ files named below.
- Do NOT look for prior verdicts, run records, the originating repository or the grader's hidden data. Do not run recursive searches (grep -r, rg, find) outside this working directory.
- For duplicate awareness, read only the cards in peers/ (card prose only), by explicit path.

Blindness is enforced by the isolated, copy-only working directory (and, when available, an OS mount namespace that hides everything else), plus a post-hoc check of your session log. Stay inside out/ for writing.

WRITE out/redteam.md with this structure (about 1,400–2,400 words of task-specific content):
1. `# {{TASK_ID}}: <task title>: independent adversarial review`, then a bold verdict line (**Verdict: HOLDS / FIX / CUT.**) with a 2–3 sentence task-specific reason.
2. `## Independent attack table`: EXACTLY 11 rows, with these columns: | Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
   - Rows 1–3: three attacks you invent for THIS task (lawful shortcuts, metric gaming, proxy collapse).
   - Rows 4–10: one row per category below, each made concrete for this task's actual files, processes and metrics:
     - (4) filesystem/mount/proc/IPC/frozen-asset access;
     - (5) interface or encoded-state smuggling;
     - (6) spoofed verdict / skipped execution / benign-bank fingerprint;
     - (7) timing / check-decoupling / branch laundering;
     - (8) dev-to-hidden leakage / cue inference;
     - (9) adaptive aggregate oracle;
     - (10) slice abandonment / denominator optimization.
   - Row 11: "Strongest lawful combined recipe", scored as an ESTIMATED point with an ESTIMATED range. Security fixes do not reduce it.
   - Every reward cell reads "ESTIMATED x" or "ESTIMATED a–b".
3. `## Published recipe shortcut: web checked`: at least 2 (prefer 3–4) real sources found this session (title + URL), each with one line on what it establishes. Then give the strongest combined known-recipe estimate (ESTIMATED).
4. `## Demonstrated-agent evidence`: apply method/evidence_grounding_rule.md. Give attack_basis, at least 2 demonstrated refs with the gap, and the subfield SOTA with its year.
5. `## Saturation against the hypothetical 10T researcher / 12h`: ESTIMATED single-run, best-of-4, pass@4 and projected upper-95%, each against its kill line. Say which line it likely breaches. Intervals touching a line mean HOLD, not pass.
6. `## Boilerplate and missing build content`: the ESTIMATED generic vs task-specific fraction, and what is missing.
7. `## Duplicate check`: name ids only if you opened their card.
8. `## Verdict, required fixes and cheapest decisive check`:
   - HOLDS: plausible as specified, subject to the empirical gates.
   - FIX: give numbered, bounded required fixes.
   - CUT: give the reason.

   Then the cheapest decisive experiment, with a realistic ESTIMATED GPU-h (0 if it is CPU-only). This is a plan only; nothing is run.
9. `## Verdict record`: exactly these key: value lines (numbers ESTIMATED):
id: {{TASK_ID}}
verdict: HOLDS|FIX|CUT
strongest_attack: ESTIMATED x (a–b)
combined_recipe_attack: ESTIMATED x (a–b)
best_of_4: ESTIMATED x
pass_at_4: ESTIMATED x
single_run_max: ESTIMATED x
upper95_projected: ESTIMATED x
kill_line_breached: none|single|bo4|pass4|upper95 (comma list)
attack_basis: DEMONSTRATED-AGENT|LITERATURE-ONLY|ASSUMED
demonstrated_ref: <short; ';'-separated>
gap_to_attack: <short phrase>
subfield_sota_ref: <short>
decisive_gpu_h: ESTIMATED x
required_fixes: short semicolon list or none
main_kill_reason: one short phrase or n/a
duplicate_of: id or none
souping_flag: no|yes

If the lawful combined recipe reaches the reference or likely breaches a kill line, the verdict is CUT or FIX, not HOLDS.
