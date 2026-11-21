#!/usr/bin/env python3
"""Post-hoc blindness check for a red-team session (best effort; a CHECKER, not enforcement).

Usage: tools/independence_check.py EVENTS_OR_SESSION.jsonl [...]

Reads a `codex exec --json` event stream (what bin/redteam saves as codex_events.jsonl) or a Codex
session JSONL, collects every command / tool-call input the agent issued, and flags:
  RUNS_ACCESS       any command that touches runs/ (earlier verdicts live there)
  RECURSIVE_SEARCH  grep -r / rg / find aimed at the repo root or a parent directory
The prompt text itself is not scanned. A clean result does not prove blindness (e.g. the agent could
have read runs/ via a tool that leaves no command string); treat it as evidence, not proof.
"""
import json, re, sys
CMD_KEYS = {"command", "cmd", "input", "arguments", "action", "args"}
RUNS = re.compile(r"(^|[\s'\"=/])runs(/|\b)")
RECUR = re.compile(r"(grep\s+-[a-zA-Z]*[rR]|\brg\b|\bfind\b)[^\n]*?(\s\.(\s|$|/?\*)|\s\.\.|\s/(\s|$))")

def strings(node, under=False):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from strings(v, under or k in CMD_KEYS)
    elif isinstance(node, list):
        for v in node:
            yield from strings(v, under)
    elif isinstance(node, str) and under:
        yield node

def scan(path):
    n, flags = 0, []
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        for s in strings(d):
            n += 1
            if RUNS.search(s):
                flags.append(("RUNS_ACCESS", s[:200]))
            if RECUR.search(s):
                flags.append(("RECURSIVE_SEARCH", s[:200]))
    return n, flags

rc = 0
for p in sys.argv[1:]:
    n, f = scan(p)
    print(f"{p}: command_strings={n} flags={len(f)}")
    for x in f[:20]:
        print("   ", x)
    rc |= bool(f)
sys.exit(rc)
