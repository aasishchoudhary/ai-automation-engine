# Architecture

The engine separates probabilistic reasoning from deterministic authority.

## Execution flow

1. Receive a typed execution request.
2. Apply deterministic policy.
3. Deny actions that violate policy.
4. Execute an explicitly supplied action.
5. Contain action failures.
6. Emit structured execution events.
7. Return a typed result.

## Why this matters

AI systems can produce uncertain outputs. The orchestration layer therefore owns control flow, authorization boundaries, and failure semantics rather than delegating those decisions to a model.

## Current scope

This repository is an engineering reference implementation, not a claim of production readiness.

## Next increments

- model adapter interface
- approval-token workflow
- persistent event store
- retry policy
- idempotency keys
- evaluation harness
- secret-provider abstraction
