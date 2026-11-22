# Grader interface (black-box)

This is the ONLY way a solver obtains a score. Do not describe grader internals, hidden seeds or private data here.

- **Input:** <what the solver submits and in what format>.
- **Scoring:** <how the score in [0,1] is computed, at a black-box level>.
- **Query limit:** <N grader calls per run>.
- **Determinism / seeds:** <what is fixed, what is held out; do NOT reveal secret seeds>.
- **Fail-closed rules:** <malformed or over-limit submissions score 0>.
- **Anti-gaming fixtures:** <benign banks, format checks, re-grade policy>.
