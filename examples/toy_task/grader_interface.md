# Grader interface (black-box)

- **Input:** a pickled scikit-learn estimator exposing `predict(X)`.
- **Scoring:** the grader runs `predict` on a hidden held-out split and returns accuracy in [0, 1].
- **Query limit:** 200 scoring calls per run.
- **Determinism:** the held-out split is fixed; scoring is deterministic. The split and its labels are hidden.
- **Fail-closed:** a submission that fails to unpickle, lacks `predict`, or exceeds the query limit scores 0.
- **Anti-gaming:** the grader returns only the scalar accuracy, never per-row predictions or labels.
