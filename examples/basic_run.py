from core.models import ExecutionRequest
from core.orchestrator import Orchestrator
from tools.calculator import calculate


def main() -> None:
    request = ExecutionRequest(
        action="calculate",
        payload={"a": 8, "b": 4},
    )

    result = Orchestrator().run(
        request,
        lambda payload: calculate("divide", payload["a"], payload["b"]),
    )

    print(result.status.value)
    print(result.output)
    print(result.events)


if __name__ == "__main__":
    main()
