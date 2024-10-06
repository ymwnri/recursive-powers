# Program: Calculate Powers Using Recursion
# Features: Takes a base and exponent as input and calculates the power using a recursive method.
# Procedure:
# 1. Take user inputs for the base and exponent.
# 2. Validate the inputs to ensure they are of the correct type.
# 3. Define and use a recursive function to calculate the power.
# 4. Print the result of the power calculation.

def calculate_powers(base, exponent):
    """Calculate the power of a number using recursion.

    Args:
        base (float): The base number to be raised.
        exponent (int): The exponent value.
        
    Returns:
        float: The result of base raised to the power of exponent.
    """
    if exponent == 0:
        return 1
    else:
        return base * calculate_powers(base, exponent - 1)

# Start of the program
invalid = True

while invalid:
    try:
        # Take inputs for base and exponent
        base = float(input("Enter a number to raise to a power: "))
        exponent = int(input("Enter the exponent: "))
        invalid = False  # Exit loop when inputs are valid
    except ValueError:
        print("Invalid input. Please enter valid numbers for base and exponent.")

# Print the calculated power
print(f"{base} raised to the power of {exponent} is: {calculate_powers(base, exponent)}")
