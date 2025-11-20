"""
Unit tests for the subtract operation.
"""
import pytest

# The subtract function will be in src.main
from src.main import subtract


@pytest.mark.parametrize("num1, num2, expected", [
    # Subtracting positive integers
    (5, 3, 2),
    (10, 7, 3),
    # Subtracting negative integers
    (-5, -3, -2),
    (-10, -2, -8),
    # Subtracting positive and negative integers
    (5, -3, 8),
    (-5, 3, -8),
    (10, -10, 20),
    # Subtracting numbers with decimals
    (5.5, 2.2, pytest.approx(3.3)),
    (-1.5, 0.5, pytest.approx(-2.0)),
    (0.3, 0.1, pytest.approx(0.2)),
    # Subtracting zero values
    (5, 0, 5),
    (0, 5, -5),
    (0, 0, 0),
    (-7, 0, -7),
])
def test_subtract_operation(num1, num2, expected):
    assert subtract(num1, num2) == expected
