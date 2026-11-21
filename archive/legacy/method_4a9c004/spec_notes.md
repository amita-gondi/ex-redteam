# Red-team attacker prompt + rollout spec (DRAFT, 2026-11-21)

Amita gave the GO for this draft at 12:18 PM PT on Nov 21. It is internal only: nothing has been run, shared or sent to GDM. Every results field is UNMEASURED and every cost is ESTIMATED.

## Summary

`attacker_prompt.md` is a task-agnostic red-team prompt. Its slots are {TASK_CARD}, {GRADER_INTERFACE}, {ALLOWED_RESOURCES}, {COMPUTE_BUDGET}, {WALLCLOCK=12h} and {SUBMISSION_FORMAT}. It makes the attacker do four things:
- survey every lawful known recipe first, then stack them (the combined-recipe attack);
- use the whole 12 h, with checkpointed PLAN and BUDGET files and a named next experiment;
- re-measure every claim, with unverified claims counting as zero;
- explore under sparse feedback, using structural changes and a scheduled explore/exploit split.

These target the known Opus 5.5 / GPT-6.x weaknesses: stopping early, incremental changes and unchecked claims. The prompt sets lawful and unlawful boundaries and a required report schema. Each pairing gets a short block of harness notes. A separate exploit-probe variant feeds the environment fix list and is never counted in saturation metrics.

`rollout_spec.md` covers the run plan:
- gating: 1 canary per pairing with a pass/fail checklist, and the 4×4 panel only on Amita's written GO;
- seeds, run IDs, hard budget caps and model-provenance logging, with a policy for reroutes to Opus 5;
- the four kill-line metrics and the interval methods, plus the n = 4 caveats;
- clean re-grading, retention, and contamination and exploit checks;
- an ESTIMATED cost table of about 3,072–4,608 GPU-h and $11.6k–$16.2k per task, including probes and excluding the S2 study.

Pairings: the canonical set, picked by Amita on Nov 21 at 12:27 PM PT (source: `/workspace/task_tabs_v4/prompts/COMMON.md`, `task_tabs_v4/ref/model_tab.txt`):
- P1 Claude Opus 5.5 + Claude Code
- P2 Gemini 4 Argon + Antigravity
- P3 Qwen 3.8 Max + Qwen Code
- P4 GPT-6.2 Sol + Codex

## Alignment debt (old roster in other files)

Status after Amita's migration GO (Nov 21, 1:18 PM PT); the full log is `/workspace/pairing_migration_log.md`, with backups in `/workspace/pairing_migration_backup/`.
- **Migrated:**
  - `task_packets_codex.md` and `task_packets_codex/` (13 files)
  - `task_tabs_v4/tabs/*.md` and `*.sources.md` (16 files)
  - annotations in `extrapolate/summary.md`

  Estimates that depended on the old roster are marked "ESTIMATED — needs re-check".
- **Queued until running jobs finish:**
  - `task_design_weakness_claude/`: Claude's pipeline, no ALLDONE file yet
  - `task_catalog_v3_full/packet_core.py` and `packets/T01–T23`: read by that pipeline's dedupe
  - `fix_packets_v4/*/packet.md`: hashed by the v4 red team; T08 is also read by the live screen audit
- **Left as source or historical records:**
  - `extrapolate/docs*`
  - `task_packet_template.md` and `task_template_gdoc.txt`: copies of the sample packet with real results; use them for structure only
  - the `ex_review/` mirror, including the agentic_search harness README; the real harness on the Mac still needs a 6.2 Sol re-pin
  - `task_tabs_v4/build/`
  - evidence files
- **Google Docs (updated Nov 21 after Amita's 1:30 PM PT GO):**
  - Task Tabs (v4): T02, T06, T08, T09, T10, T11, T13, T16, T17 and T18. Each reconcile note now reads "Roster settled by Amita, Nov 21: …" with the canonical set. The T06, T10 and T18 packet-roster costs are marked "ESTIMATED — needs re-check (old roster)". The local mirror (`task_tabs_v4/tabs/`) and `task_tabs_v4/build/` were synced to the live wording.
  - AG Tasks: "Reward-model repair task" (model-name note closed as GPT-6.2 Sol) and "RLVR and proof tasks" (six-model harness and pack runs marked pre-migration history; canonical set stated in one line).
  - Held pending Amita: cost flags for T08 (native panel 3,072 H100-GPU-h) and T13/T16 (768/3,072 H100-h). These are already sized at 16 runs and not labelled packet-roster.
  - Waiting on Amita checking the Docs UI: AG Tasks "Full catalog v3 (35 task families)" (`t.vujmbny4tatd`). The connector can't find this tab, so it was not edited.

## Open questions for partner alignment

1. **RESOLVED (Amita, Nov 21 12:27 PM PT): the Task Tabs set is canonical:** Opus 5.5 + Claude Code, Gemini 4 Argon + Antigravity, Qwen 3.8 Max + Qwen Code, GPT-6.2 Sol + Codex. This also settles the F7 Sol question (6.2, not 6.1). The old roster is still in older files; see Alignment debt above.
2. **The panel cannot certify.** At n = 4 per pairing, and even at 16 pooled runs, the pass@4 upper bound stays above 0.50. So the panel can kill a task but not clear it, and a no-kill panel result is HOLD. Do partners accept that clearing needs the bar v2 S2 study (≥ 3 blocks × ≥ 8 runs), or do they want to redefine pass@4 or the borderline-CI rule?
3. **Reroute and mismatch policy.** Runs routed to Opus 5 (P1), or with any main-model mismatch (P2–P4), are excluded from that pairing's metrics but still count toward the > 0.70 kill. Is that the right policy, and what is the re-run allowance?
4. **Pass threshold τ** for pass@4: keep R ≥ 0.60 (bar v2 S2), or set it per task?
5. **Is "upper 95%" the bound on the observed mean, the S4 projection, or both?**
6. **Network for the recipe survey.** Should the attacker get allowlisted web search, an offline literature pack, or nothing? (Bar F7 mentions disabling web search as a pinned flag.) This choice strongly shapes the combined-recipe attack.
7. **Exploit probes.** Run 1 per pairing, or fewer? Should they be white-box (grader code visible) or black-box?
8. **Caps.** Per-run GPU, token and API caps. Is $100 per run (the bar B10 default) enough for 12 h at max effort? Real token costs are UNMEASURED.
9. **Retention period** and who may access the transcripts.
10. **Harness details.** Antigravity's tool names, continuation and model-ID field are TODO. For Qwen Code, the effort level (`xhigh` vs `max`), the memory-off settings and the subagent policy on 0.26.6 are TODO. Is 0.26.6 still the pin, given that 0.28.3 shipped on Nov 20 PT? Who confirms them?
11. **Prompt pressure vs. realism.** Does the "no early stop / survey ≥ 15 recipes" pressure measure the attacker's best case (intended), and do partners agree the saturation bar should be judged against that elicited best case?
