import sys
import os

script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
sys.path.insert(0, project_root)

import argparse
from src.calculator.add import add

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

    if result is not None:
        print(f"Result: {result}")
    else:
        print(f"Unsupported operation: {args.operation}")

if __name__ == "__main__":
    main()
