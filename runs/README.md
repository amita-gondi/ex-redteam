# runs/ (generated; git-ignored)

`redteam run` writes new desk runs here as `runs/<task_id>/v<version>/<run_id>/<stage>/run.yaml` (plus each
stage's report and prompt) and maintains `runs/INDEX.tsv`. The directory is git-ignored: run records are local
working state, not source. The imported historical runs live in `archive/runs/` instead.

Every verdict written here is an **ESTIMATED desk verdict, UNMEASURED** (an LLM judgement). No rollout, canary
or panel is run. A 4x4 panel can kill a task but not clear it.
