from redteam.supervisor import Clock, backoff_delay, supervise


def test_backoff_delay_exponential_capped():
    assert backoff_delay(1, 30, 2.0, 600) == 30
    assert backoff_delay(2, 30, 2.0, 600) == 60
    assert backoff_delay(3, 30, 2.0, 600) == 120
    assert backoff_delay(10, 30, 2.0, 600) == 600   # capped


class FakeClock(Clock):
    def __init__(self):
        self.t = 0.0
        self.sleeps = []

    def now(self):
        return self.t

    def sleep(self, s):
        self.sleeps.append(s)
        self.t += s


class FakeHandle:
    def __init__(self, script, clock):
        # script: list of (rc_or_None) per poll; last activity advances with clock unless frozen
        self.script = list(script)
        self.clock = clock
        self._last = clock.now()
        self.terminated = False

    def poll(self):
        return self.script.pop(0) if self.script else 0

    def terminate(self, grace=10.0):
        self.terminated = True

    def last_activity(self):
        return self._last

    def session_id(self):
        return "sid-xyz"


class FakeBackend:
    def __init__(self, behaviour):
        # behaviour: list of (handle_script, done_after) per start() call
        self.behaviour = list(behaviour)
        self.starts = []

    def start(self, req, resume_sid=None, message=None):
        self.starts.append({"resume": resume_sid})
        script, self._done = self.behaviour.pop(0)
        h = FakeHandle(script, req_clock)
        return h

    def find_session_id(self, req):
        return "sid-xyz"


req_clock = None


def _run(behaviour, done_seq, clock, **kw):
    """done_seq: a list consumed by is_done() across all poll calls."""
    global req_clock
    req_clock = clock
    be = FakeBackend(behaviour)
    state = {"i": 0}

    def is_done():
        state["i"] += 1
        return done_seq[min(state["i"] - 1, len(done_seq) - 1)]

    class Req:
        stage = "screen"
    sup = {"stall_minutes": 1, "max_resumes": 4, "poll_seconds": 10, "kill_grace_seconds": 1}
    ret = {"max_attempts": 4, "backoff_initial_seconds": 30, "backoff_factor": 2.0, "backoff_max_seconds": 600}
    return supervise(be, Req(), is_done, sup, ret, timeout_s=kw.get("timeout", 10000), clock=clock), be


def test_success_first_try():
    clock = FakeClock()
    res, be = _run([([None, 0], True)], [True], clock)
    assert res.status == "OK"
    assert res.resumes == 0 and res.errors == 0
    assert len(be.starts) == 1


def test_stall_then_resume_completes():
    clock = FakeClock()
    # first session never finishes and goes idle (stall_minutes=1 -> 60s; poll 10s). Freeze last_activity.
    res, be = _run([([None] * 20, False), ([None, 0], True)], [True], clock)
    assert res.status == "OK"
    assert res.resumes == 1
    assert be.starts[1]["resume"] == "sid-xyz"   # resumed the SAME session


def test_error_retries_with_backoff_then_fails():
    clock = FakeClock()
    res, be = _run([([1], False)] * 4, [False] * 8, clock)
    assert res.status == "FAILED"
    assert res.errors == 4
    # backoff sleeps happened: 30, 60, 120
    assert 30 in clock.sleeps and 60 in clock.sleeps and 120 in clock.sleeps


def test_resume_cap_reached():
    clock = FakeClock()
    # always stalls; max_resumes=4 -> gives up as STALLED
    res, be = _run([([None] * 20, False)] * 10, [False] * 20, clock)
    assert res.status == "STALLED"
    assert res.resumes == 5   # one over the cap triggers the stop


def test_timeout():
    clock = FakeClock()
    res, be = _run([([None] * 1000, False)], [False] * 50, clock, timeout=25)
    assert res.status == "TIMEOUT"
