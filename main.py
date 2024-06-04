# Importing the necessary libraries
from fractions import Fraction
import re

# Getting user input for the quadratic equation and n value
Quad_eq = input("Enter the quadratic equation in the form ax^2 + bx + c: ")
n = int(input("Enter the value of n: "))

Quad_eq = Quad_eq.replace(" ", "")  # Remove any spaces from the equation

# Define the regular expression pattern to find the value of (a, b, c)
pattern = r'([-+]?\d*\.?\d*)x\^2([-+]?\d*\.?\d*)x([-+]?\d*\.?\d*)'

# Check if the equation matches the pattern
match = re.match(pattern, Quad_eq)
if not match:
    raise ValueError("The equation is not in the correct format.")

# Extract the coefficients
a_str, b_str, c_str = match.groups()

# Convert string to integers, with appropriate default values for empty strings
a = int(a_str) if a_str else 1
b = int(b_str) if b_str else 1
c = int(c_str)

# Calculating the sum and product of the polynomial
Poly_sum = Fraction(-b, a)
product = Fraction(c, a)

# Giving values to some constant integers
P0 = 2
P1 = Poly_sum

Pn_1 = P1
Pn_2 = P0
Pn = 0

# Checking the value of constant n
if n == 0:
    print(2)
elif n == 1:
    print(Poly_sum)
else:
    # Calculating the value of Pn
    for i in range(2, n + 1):
        Pn = Poly_sum * Pn_1 - product * Pn_2
        Pn_2 = Pn_1
        Pn_1 = Pn
    print(Pn)
