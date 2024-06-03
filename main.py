# Importing the necessary libraries
from fractions import Fraction

# Getting user input for the sum, product, and n value
Poly_sum = Fraction(input("Enter the sum of polynomial: "))
product = Fraction(input("Enter the product of polynomial: "))
n = int(input("Enter the value of n: "))  # Convert input to integer

# Giving values to some integers
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
