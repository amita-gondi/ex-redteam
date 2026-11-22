"""Run one desk session under supervision: stall detection + auto-resume, retries with exponential backoff,
and a per-stage wall-clock timeout. This is the generic form of the watcher.sh logic used for the
historical batches (idle session log >= stall_minutes -> kill own pid -> resume the same session, up to
max_resumes; exited before done -> resume). The clock is injectable so the logic is testable without waiting.
"""
from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass, field


class Clock:
    def now(self) -> float:
        return time.time()

    def sleep(self, s: float) -> None:
        if s > 0:
            time.sleep(s)


def backoff_delay(n: int, initial: float, factor: float, maximum: float) -> float:
    """Delay before retry n (1-based): initial * factor**(n-1), capped at maximum. Deterministic (no jitter)."""
    if n < 1:
        return 0.0
    return float(min(maximum, initial * (factor ** (n - 1))))


RESUME_MESSAGE = ("Continue from where you stopped. Re-read the files in this working directory (task/, method/ "
                  "and anything you already wrote in out/). Do not start over: finish {report} with every required "
                  "section and the record block exactly as specified, then write out/DONE.txt. All the original "
                  "rules still apply (desk only, write only to out/, cite only sources you opened, label estimates "
                  "ESTIMATED, measurements UNMEASURED, no souping or merging).")


@dataclass
class SupervisorResult:
    status: str                      # OK | STALLED | TIMEOUT | FAILED
    session_id: str | None = None
    resumes: int = 0
    errors: int = 0
    attempts: list = field(default_factory=list)
    reason: str = ""


def supervise(backend, req, is_done: Callable[[], bool], sup_cfg: dict, retry_cfg: dict, timeout_s: float,
              clock: Clock | None = None, resume_sid: str | None = None, report_name: str = "the report",
              log: Callable[[str], None] = lambda m: None) -> SupervisorResult:
    clock = clock or Clock()
    stall_s = float(sup_cfg.get("stall_minutes", 15)) * 60.0
    poll_s = float(sup_cfg.get("poll_seconds", 30))
    max_resumes = int(sup_cfg.get("max_resumes", 4))
    grace = float(sup_cfg.get("kill_grace_seconds", 10))
    max_attempts = int(retry_cfg.get("max_attempts", 4))
    b0 = float(retry_cfg.get("backoff_initial_seconds", 30))
    bf = float(retry_cfg.get("backoff_factor", 2.0))
    bmax = float(retry_cfg.get("backoff_max_seconds", 600))
    msg = RESUME_MESSAGE.format(report=report_name)

    res = SupervisorResult(status="FAILED", session_id=resume_sid)
    t0 = clock.now()
    sid = resume_sid
    while True:
        kind = "resume" if sid else "fresh"
        a = {"kind": kind, "started": clock.now(), "session_id": sid}
        handle = backend.start(req, resume_sid=sid, message=msg if sid else None)
        outcome, rc = None, None
        while True:
            rc = handle.poll()
            if rc is not None:
                break
            now = clock.now()
            if now - t0 >= timeout_s:
                handle.terminate(grace)
                outcome = "timeout"
                break
            if now - handle.last_activity() >= stall_s:
                handle.terminate(grace)
                outcome = "stall"
                break
            clock.sleep(poll_s)
        sid = backend.find_session_id(req) or handle.session_id() or sid
        res.session_id = sid
        a.update({"ended": clock.now(), "exit_code": rc})
        if outcome is None:
            outcome = "done" if is_done() else ("exit0-incomplete" if rc == 0 else "error")
        a["outcome"] = outcome
        res.attempts.append(a)
        log(f"{req.stage}: attempt {len(res.attempts)} ({kind}) -> {outcome} rc={rc}")
        if outcome == "done":
            res.status = "OK"
            return res
        if outcome == "timeout":
            res.status, res.reason = "TIMEOUT", f"stage timeout {timeout_s:.0f}s reached"
            return res
        if outcome in ("stall", "exit0-incomplete"):
            res.resumes += 1
            if res.resumes > max_resumes:
                res.status, res.reason = "STALLED", f"{outcome}; resume cap {max_resumes} reached"
                return res
            continue   # resume the same session (fresh if no session id was recorded)
        # error: retry with backoff
        res.errors += 1
        if res.errors >= max_attempts:
            res.status, res.reason = "FAILED", f"agent exited non-zero {res.errors} times (cap {max_attempts})"
            return res
        d = backoff_delay(res.errors, b0, bf, bmax)
        a["backoff_seconds"] = d
        if clock.now() + d - t0 >= timeout_s:
            res.status, res.reason = "TIMEOUT", "stage timeout would be reached during backoff"
            return res
        log(f"{req.stage}: backing off {d:.0f}s before retry {res.errors + 1}")
        clock.sleep(d)
