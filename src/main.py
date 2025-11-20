import os
import sys

script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
sys.path.insert(0, project_root)

import argparse  # noqa: E402


# Inserted add function here
def add(num1: float, num2: float) -> float:
    """
    Adds two numbers.

    Parameters:
        num1 (float): The first operand.
        num2 (float): The second operand.

    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

# New subtract function
def subtract(num1: float, num2: float) -> float:
    """
    Subtracts the second number from the first.

    Parameters:
        num1 (float): The minuend.
        num2 (float): The subtrahend.

    Returns:
        float: The difference between num1 and num2.
    """
    return num1 - num2

# New multiply function
def multiply(num1: float, num2: float) -> float:
    """
    Multiplies two numbers.

    Parameters:
        num1 (float): The first operand.
        num2 (float): The second operand.

    Returns:
        float: The product of num1 and num2.
    """
    return num1 * num2

# New divide function
def divide(num1: float, num2: float) -> float:
    """
    Divides the first number by the second.

    Parameters:
        num1 (float): The dividend.
        num2 (float): The divisor.

    Returns:
        float: The quotient of num1 divided by num2.

    Raises:
        ZeroDivisionError: If num2 is 0.
    """
    if num2 == 0:
        raise ZeroDivisionError("division by zero")
    return num1 / num2

def main():
    parser = argparse.ArgumentParser(description="A simple calculator CLI.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"],
                        help="The operation to perform")
    parser.add_argument("num1", type=float, help="The first number")
    parser.add_argument("num2", type=float, help="The second number")

    args = parser.parse_args()

    result = None

    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operation == "multiply":
        result = multiply(args.num1, args.num2)
    elif args.operation == "divide":
        try:
            result = divide(args.num1, args.num2)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            sys.exit(1)

    if result is not None:
        print(f"Result: {result}")
    else:
        print(f"Unsupported operation: {args.operation}")

if __name__ == "__main__":
    main()
