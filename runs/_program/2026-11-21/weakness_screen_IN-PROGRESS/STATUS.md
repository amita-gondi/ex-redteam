# STATUS — weakness-task (Claude W01–W14) saturation screen (desk review, CPU only)

Go-ahead: Amita, Nov 21 2026 10:33 AM PT (relayed via Extrapolate RL Envs). Source /workspace/task_design_weakness_claude/ is READ-ONLY (Claude run still writing); SHA-256 snapshot of it at ref/source_sha256_before.txt (113 files, 10:35 AM PT).

## Readiness rule
A task is screened only once progress.json steps_done has rev_Wxx. At 10:34 AM PT: ready = W01 W02 W03 W04 W06. W05 rev running (W05.md exists but NOT ready). W07, W08 gen running; W09–W14 not started.

## Checkpoints (PT)
- 10:35 AM — Folder created; reference index ref/EXISTING_TASKS_INDEX.md (v3/FIX/catalog/D index copied read-only from the creative screen + creative v4 C-titles + sibling W titles). Prompt template prompts/TEMPLATE.md.
- 10:35 AM — Launched Codex S1 (W01 W02 W03) sid 01a1ff64-8b74-7d80-a182-7867f35246c1 and S2 (W04 W06) sid 01a1ff64-8b74-77a1-86a7-91590e278dcc. Max 2 concurrent (creative screen runs 4).
- Watcher logs/watcher.sh (90 s loop; JSONL-mtime stall >=15 min -> kill own pid, resume SAME session, <=4 resumes/session; auto-creates sessions S3, S4... of <=3 ids each as rev_ entries appear; exits when source ALLDONE exists or all 14 rev_ present and all screened, or after 24 h). Live: logs/watch_status.txt; events: logs/watcher.log. screen.tsv / screened.txt regenerated mechanically each loop from cards' Screen record blocks (tools/aggregate.py).

## Resume instructions
A card is complete iff it has "## Screen record" and "souping_flag:". If the watcher died, rerun `nohup bash logs/watcher.sh &` (resume counts persist in logs/S*_resumes). Only kill pids in logs/S*.pid. Other Codex sessions on the box (creative screen, Claude task design) are not ours.
- 10:41 AM — rev_W05 appeared (10:36 AM PT); watcher launched S3 (W05) sid 01a1ff6a-0b88-7293-81c6-50b7e8aa98bd.
- 10:48 AM — Batch 1 complete: W01–W06 all CUT (see 00_summary.md, screen.tsv). Wording audit 0 repeats; 28/28 URLs 200. Watcher continues for W07–W14 (none has rev_ yet).
- 1:23 PM — W10 screened CUT (bo4>0.60) and reported. Anchored addendum Codex session launched for W10 (pid in anchored_addendum/logs/W10.pid; output anchored_addendum/W10.md; prompt logs/W10_prompt.txt). Original screen cards never overwritten.
