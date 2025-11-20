"""
Unit tests for the multiply operation.
"""
import pytest

# The multiply function will be in src.main
from src.main import multiply


@pytest.mark.parametrize("num1, num2, expected", [
    # T049: Multiplying positive integers
    (5, 3, 15),
    (10, 7, 70),
    # T049: Multiplying negative integers
    (-5, -3, 15),
    (-10, -2, 20),
    # T049: Multiplying positive and negative integers
    (5, -3, -15),
    (-5, 3, -15),
    # T049: Multiplying numbers with decimals
    (2.5, 3.2, pytest.approx(8.0)),
    (-1.5, 0.5, pytest.approx(-0.75)),
    (0.1, 0.2, pytest.approx(0.02)),
    # T050: Multiplying by zero
    (5, 0, 0),
    (0, 5, 0),
    (0, 0, 0),
    (-7, 0, 0),
])
def test_multiply_operation(num1, num2, expected):
    assert multiply(num1, num2) == expected
