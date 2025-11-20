"""
Integration tests for the CLI argument parsing and error handling.
"""
import subprocess
import sys
import pytest

# Path to the main CLI script
CLI_SCRIPT = ["python", "src/main.py"]

def run_cli_command(command_args):
    """Helper to run the CLI script and capture output/error."""
    full_command = CLI_SCRIPT + command_args
    # Use uv run to ensure the virtual environment's python is used
    process = subprocess.run(["uv", "run"] + full_command, capture_output=True, text=True, check=False)
    return process

@pytest.mark.parametrize("operation, num1, num2, expected_output", [
    ("add", "5", "3", "Result: 8.0\n"),
    ("subtract", "10", "4", "Result: 6.0\n"),
    ("multiply", "2.5", "4", "Result: 10.0\n"),
    ("divide", "10", "2", "Result: 5.0\n"),
    ("add", "5.5", "3.2", "Result: 8.7\n"),
])
def test_cli_operations_success(operation, num1, num2, expected_output):
    """Test successful execution of basic operations via CLI."""
    process = run_cli_command([operation, num1, num2])
    assert process.returncode == 0
    assert process.stdout == expected_output
    assert process.stderr == ""

def test_cli_divide_by_zero_error():
    """Test CLI handles division by zero error."""
    process = run_cli_command(["divide", "10", "0"])
    assert process.returncode == 1 # Expect a non-zero exit code for error
    assert "Error: division by zero" in process.stdout # Check for error message
    assert process.stderr == ""

def test_cli_invalid_operation_error():
    """Test CLI handles invalid operation arguments."""
    process = run_cli_command(["power", "10", "2"]) # "power" is not a valid operation
    assert process.returncode == 2 # argparse typically returns 2 for invalid arguments
    assert "invalid choice: 'power'" in process.stderr
    assert "usage: main.py" in process.stderr
    assert process.stdout == ""

@pytest.mark.parametrize("operation, num1, num2", [
    ("add", "not_a_number", "3"),
    ("subtract", "10", "abc"),
])
def test_cli_invalid_number_input_error(operation, num1, num2):
    """Test CLI handles invalid number inputs."""
    process = run_cli_command([operation, num1, num2])
    assert process.returncode == 2 # argparse typically returns 2 for invalid arguments
    assert "invalid float value" in process.stderr
    assert "usage: main.py" in process.stderr
    assert process.stdout == ""