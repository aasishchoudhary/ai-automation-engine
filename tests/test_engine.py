from core.models import ExecutionRequest, ExecutionStatus
from core.orchestrator import Orchestrator
from core.policy import Policy
from tools.calculator import CalculatorError, calculate


def test_policy_denies_irreversible_request() -> None:
    result = Orchestrator(Policy()).run(
        ExecutionRequest(action="delete_data", irreversible=True),
        lambda _: "should not run",
    )
    assert result.status is ExecutionStatus.DENIED
    assert "human approval" in (result.reason or "")


def test_successful_execution_is_recorded() -> None:
    result = Orchestrator().run(
        ExecutionRequest(action="calculate", payload={"a": 2, "b": 3}),
        lambda payload: calculate("add", payload["a"], payload["b"]),
    )
    assert result.status is ExecutionStatus.COMPLETED
    assert result.output == 5
    assert result.events[-1]["name"] == "execution.completed"


def test_action_failure_is_contained() -> None:
    result = Orchestrator().run(
        ExecutionRequest(action="calculate"),
        lambda _: calculate("divide", 1, 0),
    )
    assert result.status is ExecutionStatus.FAILED
    assert result.reason == "division by zero"


def test_calculator_rejects_unknown_operation() -> None:
    try:
        calculate("power", 2, 3)
    except CalculatorError as exc:
        assert "unsupported operation" in str(exc)
    else:
        raise AssertionError("expected CalculatorError")
