# Let's create a simple Python library for calculating basic math functions.
# The library will include functions for addition, subtraction, multiplication, and division.

# Directory structure:
# mathlib/
# ├── mathlib/
# │   ├── __init__.py
# │   └── operations.py
# └── setup.py

# mathlib/mathlib/operations.py
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b