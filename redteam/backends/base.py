from __future__ import annotations

import os
import signal
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class LaunchRequest:
    stage: str
    task_id: str
    prompt: str
    workdir: Path
    events_path: Path          # agent stdout (JSONL events); outside the workdir
    log_path: Path             # agent stderr; outside the workdir
    model: str
    effort: str
    web_search: bool = True
    sandbox: str = "workspace-write"
    extra_args: list = field(default_factory=list)
    wrap: list = field(default_factory=list)   # isolation prefix (bwrap ...), applied by the supervisor


class Handle:
    """A running (or finished) agent session."""

    def poll(self) -> int | None:
        raise NotImplementedError

    def terminate(self, grace: float = 10.0) -> None:
        raise NotImplementedError

    def last_activity(self) -> float:
        raise NotImplementedError

    def session_id(self) -> str | None:
        return None


class ProcessHandle(Handle):
    def __init__(self, cmd: list[str], req: LaunchRequest, stdin_text: str | None, append: bool = False,
                 env: dict | None = None):
        self.req = req
        self.cmd = cmd
        mode = "a" if append else "w"
        self._out = open(req.events_path, mode, encoding="utf-8")
        self._err = open(req.log_path, mode, encoding="utf-8")
        self.proc = subprocess.Popen(cmd, cwd=str(req.workdir), stdin=subprocess.PIPE if stdin_text is not None else subprocess.DEVNULL,
                                     stdout=self._out, stderr=self._err, text=True, start_new_session=True,
                                     env=env)
        if stdin_text is not None:
            try:
                self.proc.stdin.write(stdin_text)
                self.proc.stdin.close()
            except BrokenPipeError:
                pass
        self.started = time.time()

    def poll(self) -> int | None:
        rc = self.proc.poll()
        if rc is not None:
            self._close()
        return rc

    def _close(self):
        for f in (self._out, self._err):
            try:
                f.close()
            except OSError:
                pass

    def terminate(self, grace: float = 10.0) -> None:
        if self.proc.poll() is not None:
            self._close()
            return
        try:
            os.killpg(self.proc.pid, signal.SIGTERM)
        except (ProcessLookupError, PermissionError):
            self.proc.terminate()
        try:
            self.proc.wait(timeout=grace)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(self.proc.pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                self.proc.kill()
            self.proc.wait()
        self._close()

    def last_activity(self) -> float:
        t = self.started
        for p in (self.req.events_path, self.req.log_path):
            try:
                t = max(t, p.stat().st_mtime)
            except OSError:
                pass
        out = self.req.workdir / "out"
        if out.is_dir():
            for p in out.rglob("*"):
                try:
                    t = max(t, p.stat().st_mtime)
                except OSError:
                    pass
        return t


class Backend:
    name = "base"

    def __init__(self, desk_cfg: dict):
        self.cfg = desk_cfg or {}

    def describe(self, req: LaunchRequest) -> dict:
        return {"backend": self.name, "model": req.model, "reasoning_effort": req.effort, "web_search": req.web_search}

    def command(self, req: LaunchRequest, resume_sid: str | None = None) -> list[str]:
        raise NotImplementedError

    def start(self, req: LaunchRequest, resume_sid: str | None = None, message: str | None = None) -> Handle:
        """Start a fresh session (resume_sid None, prompt on stdin) or resume one with `message`."""
        cmd = req.wrap + self.command(req, resume_sid)
        return ProcessHandle(cmd, req, stdin_text=(message if resume_sid else req.prompt), append=bool(resume_sid),
                             env=self.env())

    def env(self) -> dict | None:
        """Environment for the agent process (None = inherit)."""
        return None

    def find_session_id(self, req: LaunchRequest) -> str | None:
        return None

    def preflight(self) -> str | None:
        """None if usable, else a reason string."""
        return None
