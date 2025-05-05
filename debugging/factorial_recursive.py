#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number using recursion.
# It multiplies the number by the factorial of the number minus one,
# until the base case of 0 is reached, where it returns 1.

# Parameters:
# n (int): The number for which the factorial is to be calculated. 
#          This must be a non-negative integer.

# Returns:
# int: The factorial of the given number `n`. The factorial of a number n is 
#      the product of all positive integers less than or equal to n.
def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1.
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1).

# The following line calls the factorial function with the command line argument.
# It converts the argument (which is a string) to an integer using `int()` and 
# passes it to the `factorial` function.
f = factorial(int(sys.argv[1]))

# Prints the result of the factorial calculation to the console.
print(f)

