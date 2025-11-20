"""
Unit tests for the add operation.
"""
import pytest

from src.main import add


@pytest.mark.parametrize("num1, num2, expected", [
    # T008: Adding positive integers
    (5, 3, 8),
    (100, 200, 300),
    # T009: Adding negative integers
    (-5, -3, -8),
    (-10, -20, -30),
    # T010: Adding positive and negative integers
    (5, -3, 2),
    (-5, 3, -2),
    (10, -10, 0),
    # T011: Adding numbers with decimals
    (2.5, 3.2, pytest.approx(5.7)),
    (-1.5, 0.5, pytest.approx(-1.0)),
    (0.1, 0.2, pytest.approx(0.3)),
    # T012: Adding zero values
    (5, 0, 5),
    (0, 5, 5),
    (0, 0, 0),
    (-7, 0, -7),
])
def test_add_operation(num1, num2, expected):
    assert add(num1, num2) == expected
