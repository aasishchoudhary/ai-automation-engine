from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .models import ExecutionRequest, ExecutionResult, ExecutionStatus
from .policy import Policy
from telemetry.events import event


class Orchestrator:
    def __init__(self, policy: Policy | None = None) -> None:
        self.policy = policy or Policy()

    def run(
        self,
        request: ExecutionRequest,
        action: Callable[[dict[str, Any]], Any],
    ) -> ExecutionResult:
        events: list[dict[str, Any]] = [
            event("execution.received", action=request.action)
        ]

        allowed, reason = self.policy.authorize(request)
        if not allowed:
            events.append(event("execution.denied", reason=reason))
            return ExecutionResult(
                status=ExecutionStatus.DENIED,
                reason=reason,
                events=tuple(events),
            )

        try:
            output = action(request.payload)
        except Exception as exc:
            events.append(event("execution.failed", error=type(exc).__name__))
            return ExecutionResult(
                status=ExecutionStatus.FAILED,
                reason=str(exc),
                events=tuple(events),
            )

        events.append(event("execution.completed"))
        return ExecutionResult(
            status=ExecutionStatus.COMPLETED,
            output=output,
            events=tuple(events),
        )
