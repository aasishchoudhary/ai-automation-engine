# AI Automation Engine

A provider-neutral reference implementation for reliable AI workflow automation.

> **Core principle:** probabilistic reasoning should not silently own irreversible authority.

## What this project demonstrates

- deterministic orchestration around model/tool calls
- explicit policy and approval boundaries
- typed execution records
- tool isolation
- structured telemetry
- failure-aware testing
- reproducible local execution
- provider-neutral model adapters

## Architecture

```
INPUT
  │
  ▼
VALIDATE
  │
  ▼
POLICY ───────► DENY / REQUIRE APPROVAL
  │
  ▼
ORCHESTRATOR
  │
  ├──► MODEL ADAPTER
  │
  └──► TOOL LAYER
          │
          ▼
      VALIDATION
          │
          ▼
      TELEMETRY
          │
          ▼
        OUTPUT
```

## Status

**Prototype / engineering reference implementation**

This repository intentionally makes no claims about production deployment, client usage, or commercial performance.

## Engineering priorities

1. deterministic controls
2. inspectable behavior
3. safe failure modes
4. reproducible tests
5. evidence before claims

## Run

```bash
python -m pip install -e ".[dev]"
pytest -q
python examples/basic_run.py
```

## Repository layout

```
src/
  adapters/       Model boundaries
  core/           Domain models, policy, orchestration
  telemetry/      Structured execution events
  tools/          Explicit tool implementations
tests/            Behavioral and failure-path tests
examples/         Minimal reproducible runs
docs/             Architecture, security, evaluation
```

## License

MIT
