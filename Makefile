# ex-redteam developer tasks. CPU-only; no rollouts, no GPU, no network required for tests.
VENV ?= .venv
PY   := $(VENV)/bin/python
PIP  := $(VENV)/bin/pip

.PHONY: help venv install test lint fmt e2e secret-scan clean
help:
	@echo "make install     - create $(VENV) and install the package (editable) + dev deps"
	@echo "make test        - run the unit + end-to-end test suite (stub backend; offline)"
	@echo "make lint        - ruff lint (redteam/ and tests/)"
	@echo "make e2e         - run the toy task end to end with the stub backend"
	@echo "make secret-scan - scan the tree for obvious secrets (never prints values)"

$(VENV):
	python3 -m venv $(VENV)

venv: $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip >/dev/null
	$(PIP) install -e ".[dev]"

test: $(VENV)
	$(PY) -m pytest

lint: $(VENV)
	$(VENV)/bin/ruff check redteam tests

fmt: $(VENV)
	$(VENV)/bin/ruff check --fix redteam tests

e2e: $(VENV)
	REDTEAM_ROOT=$(CURDIR) $(PY) -m redteam run examples/toy_task --backend stub --offline --new-run

secret-scan:
	@bash tools/secret_scan.sh

clean:
	rm -rf $(VENV) .pytest_cache **/__pycache__ redteam/__pycache__ redteam/backends/__pycache__
