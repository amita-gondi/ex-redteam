"""Pluggable desk-model backends. `codex` (default) runs the Codex CLI; `stub` is a deterministic fake
agent for tests and dry pipelines. Add a backend by subclassing Backend and registering it in BACKENDS."""
from .base import Backend, Handle, LaunchRequest, ProcessHandle
from .codex import CodexBackend
from .stub import StubBackend

BACKENDS = {"codex": CodexBackend, "stub": StubBackend}


def get_backend(name: str, desk_cfg: dict) -> Backend:
    try:
        cls = BACKENDS[name]
    except KeyError:
        raise ValueError(f"unknown desk backend {name!r}; known: {sorted(BACKENDS)}") from None
    return cls(desk_cfg)


__all__ = ["Backend", "Handle", "LaunchRequest", "ProcessHandle", "BACKENDS", "get_backend"]
