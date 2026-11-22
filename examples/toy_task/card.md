# Toy: tune a tiny classifier under a frozen accuracy grader

## Problem
Train a small tabular classifier on a provided training split and submit it to a grader that scores held-out
accuracy. The aim is the highest lawful held-out accuracy within the budget.

## Start state
The repo provides `train.csv` (features + labels), a starter `train.py` that fits a logistic-regression
baseline, and a grader that loads a submitted pickled estimator and scores it on a held-out split it keeps hidden.

## Action surface and allowed resources
Python with scikit-learn, running on one CPU core, no network, no GPU. The solver may train any model from
scratch and tune it with cross-validation on the training split.

## Reward and north star
R is held-out accuracy in [0, 1]. R~0 is an empty or constant submission at or below the majority-class rate
(0.5). R~1 is near-perfect held-out accuracy; the north star is the generator's Bayes-optimal accuracy (~0.95).
The reward scale is frozen.

## Budget
One CPU core, one hour of wall clock. No GPU.

## Submission format
A pickled scikit-learn estimator passed to the grader's `score(model)` entrypoint. Malformed or over-limit
submissions score 0.

## Anti-shortcut design
The held-out split and its labels are hidden from the solver. The grader exposes only a scalar accuracy and a
fixed query budget, so the split cannot be memorized or probed row by row.
