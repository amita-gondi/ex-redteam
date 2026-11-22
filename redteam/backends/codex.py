"""Codex CLI backend: `codex [--search] exec -m MODEL -c model_reasoning_effort=E ... -` with the prompt on stdin
(so it never shows in `ps`), JSONL events on stdout. Resume: `codex [--search] exec resume <SID> ... -`."""
from __future__ import annotations

import json
import re
import shutil
import subprocess

from .base import Backend, LaunchRequest

_UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


class CodexBackend(Backend):
    name = "codex"

    def exe(self) -> str:
        return self.cfg.get("cli") or "codex"

    def command(self, req: LaunchRequest, resume_sid: str | None = None) -> list[str]:
        cli = shutil.which(self.exe()) or self.exe()
        cmd = [cli]
        if req.web_search:
            cmd.append("--search")
        cmd.append("exec")
        if resume_sid:
            cmd += ["resume", resume_sid]
        cmd += ["-m", req.model, "-c", f"model_reasoning_effort={req.effort}", "--skip-git-repo-check", "--json"]
        if resume_sid:
            # `exec resume` takes no -s/-C: pin the sandbox via config and rely on cwd = workdir
            cmd += ["-c", f'sandbox_mode="{req.sandbox}"']
        else:
            cmd += ["-s", req.sandbox, "-C", str(req.workdir)]
        cmd += ["-o", str(req.workdir / "out" / "last_message.md")]
        cmd += list(req.extra_args or [])
        cmd.append("-")
        return cmd

    def find_session_id(self, req: LaunchRequest) -> str | None:
        for path in (req.events_path, req.log_path):
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for line in text.splitlines():
                line = line.strip()
                if line.startswith("{"):
                    try:
                        ev = json.loads(line)
                    except ValueError:
                        continue
                    for k in ("thread_id", "session_id", "conversation_id"):
                        v = ev.get(k) or (ev.get("msg") or {}).get(k) if isinstance(ev, dict) else None
                        if isinstance(v, str) and _UUID.fullmatch(v):
                            return v
                elif "session id:" in line:
                    m = _UUID.search(line)
                    if m:
                        return m.group(0)
        return None

    def preflight(self) -> str | None:
        exe = shutil.which(self.exe())
        if not exe:
            return f"codex CLI {self.exe()!r} not found on PATH (install it and log in with your own access)"
        try:
            r = subprocess.run([exe, "login", "status"], capture_output=True, text=True, timeout=20)
        except (OSError, subprocess.SubprocessError) as e:
            return f"codex login status failed: {type(e).__name__}"
        if r.returncode != 0:
            return "codex is not logged in (run `codex login`; never commit credentials)"
        return None
