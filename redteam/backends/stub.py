"""Stub backend: runs stub_agent.py as a real subprocess (so supervision, isolation and resume are
exercised exactly as for codex) with the system python and no access to this package."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from .base import Backend, LaunchRequest

AGENT = Path(__file__).with_name("stub_agent.py")


def _python() -> str:
    exe = os.path.realpath(sys.executable)
    return exe if os.path.exists(exe) else "python3"


class StubBackend(Backend):
    name = "stub"

    def command(self, req: LaunchRequest, resume_sid: str | None = None) -> list[str]:
        cmd = [_python(), "-c", AGENT.read_text(encoding="utf-8"), req.stage, req.task_id]
        if resume_sid:
            cmd += ["resume", resume_sid]
        return cmd

    def env(self) -> dict:
        e = dict(os.environ)
        e["REDTEAM_STUB_CONFIG"] = json.dumps(self.cfg.get("stub") or {})
        return e

    def describe(self, req: LaunchRequest) -> dict:
        d = super().describe(req)
        d.update({"model": "stub", "note": "STUB backend output: not a desk judgement"})
        return d

    def find_session_id(self, req: LaunchRequest) -> str | None:
        try:
            for line in req.events_path.read_text(encoding="utf-8").splitlines():
                ev = json.loads(line)
                if ev.get("type") == "thread.started":
                    return ev.get("thread_id")
        except (OSError, ValueError):
            pass
        return None
