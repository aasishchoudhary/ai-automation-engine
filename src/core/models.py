from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ExecutionStatus(str, Enum):
    ACCEPTED = "accepted"
    DENIED = "denied"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True)
class ExecutionRequest:
    action: str
    payload: dict[str, Any] = field(default_factory=dict)
    irreversible: bool = False


@dataclass(frozen=True)
class ExecutionResult:
    status: ExecutionStatus
    output: Any = None
    reason: str | None = None
    events: tuple[dict[str, Any], ...] = ()
