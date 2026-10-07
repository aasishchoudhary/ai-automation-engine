from __future__ import annotations


class CalculatorError(ValueError):
    pass


def calculate(operation: str, a: float, b: float) -> float:
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise CalculatorError("division by zero")
        return a / b
    raise CalculatorError(f"unsupported operation: {operation}")
