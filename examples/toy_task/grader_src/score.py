"""Toy grader scoring code (white-box probe sees this; it never sees grader_src/hidden/)."""
import pickle
from pathlib import Path

HIDDEN = Path(__file__).with_name("hidden")


def _load_heldout():
    # Labels live under grader_src/hidden/, which is withheld from the white-box copy and every desk stage.
    import csv
    rows = list(csv.reader(open(HIDDEN / "heldout.csv")))
    X = [[float(c) for c in r[:-1]] for r in rows[1:]]
    y = [int(r[-1]) for r in rows[1:]]
    return X, y


def score(model_path: str) -> float:
    try:
        model = pickle.loads(Path(model_path).read_bytes())
        X, y = _load_heldout()
        pred = model.predict(X)
        return sum(int(a) == int(b) for a, b in zip(pred, y)) / len(y)
    except Exception:
        return 0.0   # fail-closed
