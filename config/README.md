# config/

`runner.yaml` is the single pipeline config. The `redteam` CLI loads it and merges it over the built-in
defaults in `redteam/config.py`, so you only set what you want to change. Every path is relative to the
project root unless it is absolute; nothing is pinned to one machine.

Key sections:
- **kill_lines / gate_rule / anchored_upper_bound** - the kill thresholds and the strict promotion gate (the
  anchored verdict is only an upper bound). `gate_rule` must stay `strict`.
- **pairings** - the canonical four for any later rollout (not used by the desk stages).
- **desk_agent** - which model backend runs the desk stages. `backend: codex` (default) or `stub` (tests).
- **probe_modes** - 1 white-box + 1 black-box desk exploit probe per task; findings never count toward saturation.
- **supervisor / retries / stage_timeouts_minutes** - stall-resume, backoff and timeouts.
- **isolation** - enforced blindness (copy-only workdir; bubblewrap masking when available).
- **checks** - wording/boilerplate, URL liveness, independence; `enforce` decides whether a failure blocks COMPLETE.
- **gates / gate_go_records** - rollout gates, OFF; the CLI never launches rollouts regardless.
