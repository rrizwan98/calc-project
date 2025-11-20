# API Contracts: Calculator Operations

This document defines the interface for the core calculator functions. These contracts specify the function signatures, expected inputs, and guaranteed outputs for each basic operation.

## Functions

### 1. `add(num1: float, num2: float) -> float`

*   **Description**: Adds two numbers.
*   **Parameters**:
    *   `num1` (float): The first operand.
    *   `num2` (float): The second operand.
*   **Returns**: (float) The sum of `num1` and `num2`.
*   **Error Handling**: Assumes valid float inputs. Relies on Python's native float behavior for edge cases (e.g., overflow).

### 2. `subtract(num1: float, num2: float) -> float`

*   **Description**: Subtracts the second number from the first.
*   **Parameters**:
    *   `num1` (float): The minuend.
    *   `num2` (float): The subtrahend.
*   **Returns**: (float) The difference between `num1` and `num2`.
*   **Error Handling**: Assumes valid float inputs. Relies on Python's native float behavior for edge cases.

### 3. `multiply(num1: float, num2: float) -> float`

*   **Description**: Multiplies two numbers.
*   **Parameters**:
    *   `num1` (float): The first operand.
    *   `num2` (float): The second operand.
*   **Returns**: (float) The product of `num1` and `num2`.
*   **Error Handling**: Assumes valid float inputs. Relies on Python's native float behavior for edge cases.

### 4. `divide(num1: float, num2: float) -> float`

*   **Description**: Divides the first number by the second.
*   **Parameters**:
    *   `num1` (float): The dividend.
    *   `num2` (float): The divisor.
*   **Returns**: (float) The quotient of `num1` divided by `num2`.
*   **Error Handling**:
    *   If `num2` is `0`, a `ZeroDivisionError` should be raised.
    *   Assumes valid float inputs (non-zero `num2`). Relies on Python's native float behavior for edge cases.
