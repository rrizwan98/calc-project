# Data Model: Basic Calculator Operations

This document describes the core data entities and their relationships for the basic calculator operations feature.

## Entities

### 1. Number (Operand)

Represents a numeric value used in calculations.

*   **Type**: `float` (Python's native float type)
*   **Description**: Can be positive, negative, zero, or a decimal value. Relies on Python's native float precision and handling of large/small numbers as per clarification in `spec.md`.

### 2. Operation

Represents a mathematical operation to be performed.

*   **Type**: String or Enum
*   **Description**: Defines the type of arithmetic calculation.
*   **Valid Values**:
    *   `"add"`
    *   `"subtract"`
    *   `"multiply"`
    *   `"divide"`

## Relationships

*   A calculation involves two `Number` entities (operands) and one `Operation` entity.
*   The `Operation` is performed on the operands to produce a single `Number` result.

## Example Data Flow

Input: `(operand1: Number, operand2: Number, operation: Operation)`
Output: `(result: Number)`
