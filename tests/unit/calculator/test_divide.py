"""
Unit tests for the divide operation.
"""
import pytest

# The divide function will be in src.main
from src.main import divide


@pytest.mark.parametrize("num1, num2, expected", [
    # T054: Dividing positive integers
    (10, 2, 5),
    (7, 2, 3.5),
    # T054: Dividing negative integers
    (-10, -2, 5),
    (-7, -2, 3.5),
    # T054: Dividing positive and negative integers
    (10, -2, -5),
    (-10, 2, -5),
    # T054: Dividing numbers with decimals
    (7.5, 2.5, pytest.approx(3.0)),
    (-9.0, 3.0, pytest.approx(-3.0)),
    (0.5, 0.2, pytest.approx(2.5)),
    # T055: Zero as dividend and non-zero divisor
    (0, 5, 0),
    (0, -5, 0),
])
def test_divide_operation(num1, num2, expected):
    assert divide(num1, num2) == expected

# T056: Implement test case for division by zero (expecting ZeroDivisionError)
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(10, 0)
