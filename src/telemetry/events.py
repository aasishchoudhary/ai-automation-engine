from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def event(name: str, **fields: Any) -> dict[str, Any]:
    return {
        "name": name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fields": fields,
    }
