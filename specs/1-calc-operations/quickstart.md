# Quickstart Guide: Basic Calculator Operations

This guide provides a quick overview of how to use and interact with the basic calculator operations feature.

## 1. Installation

Assuming you have Python 3.12+ and `uv` (our package manager) installed:

```bash
# Clone the repository (if you haven't already)
git clone <repository-url>
cd calc-project

# Install dependencies using uv
uv sync
```

## 2. Usage (Command Line Interface)

The calculator operations will be exposed via a command-line interface.

### Example: Addition

```bash
python src/main.py add <number1> <number2>
# Example:
python src/main.py add 5 3.5
# Expected output: 8.5
```

### Example: Subtraction

```bash
python src/main.py subtract <number1> <number2>
# Example:
python src/main.py subtract 10 -4
# Expected output: 14.0
```

### Example: Multiplication

```bash
python src/main.py multiply <number1> <number2>
# Example:
python src/main.py multiply 2.5 4
# Expected output: 10.0
```

### Example: Division

```bash
python src/main.py divide <number1> <number2>
# Example:
python src/main.py divide 10 2
# Expected output: 5.0
```

### Handling Division by Zero

Division by zero will result in an error message:

```bash
python src/main.py divide 10 0
# Expected output: Error: Cannot divide by zero.
```

## 3. Running Tests

To ensure the functionality is working correctly and adheres to quality standards:

```bash
# Run all tests
pytest tests/

# Run tests for a specific operation (e.g., addition)
pytest tests/unit/calculator/test_add.py
```
