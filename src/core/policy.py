from __future__ import annotations

from .models import ExecutionRequest


class Policy:
    """Deterministic safety boundary for workflow execution."""

    def authorize(self, request: ExecutionRequest) -> tuple[bool, str | None]:
        if not request.action.strip():
            return False, "action is required"

        if request.irreversible:
            return False, "irreversible actions require explicit human approval"

        return True, None
