import sys

# Unused import
import os

# Hardcoded password (security hotspot)
PASSWORD = "admin@123"

# Unused variable
UNUSED_VAR = 42

# Function with multiple issues
def divide(a, b):
    # No error handling for division by zero
    return a / b

# Duplicated code (code smell)
def add(a, b):
    return a + b

def sum(a, b):  # Duplicate of add()
    return a + b

# Inconsistent variable naming
def calculate_total(PriceList, discount):
    total_price = sum(PriceList)
    return total_price - (total_price * discount)

# Unreachable code
def unused_function():
    print("This is never called")
    return True
unused_function()  # This makes the next line unreachable
print("This line is unreachable")

# Potential NoneType error
def get_length(s):
    # No check for None input
    return len(s)

# Example usage with multiple issues
if __name__ == "__main__":
    print(divide(10, 0))  # Division by zero
    print(get_length(None))  # Will throw TypeError
