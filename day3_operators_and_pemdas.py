print("My age: " + str(12))
# "My age: " is a string and 12 is an integer.
# str(12) converts the integer into a string.
# The + operator joins the two strings and prints: My age: 12

print(123 + 456)
# Adds two integers using arithmetic addition.
# Output will be 579.

print(7 - 3)
# Subtracts 3 from 7.
# Output will be 4.

print(3 * 2)
# Multiplies 3 by 2.
# Output will be 6.

print(5 / 3)
# Performs division and always returns a float in Python.
# Output will be approximately 1.6666666666666667.

print(5 // 3)
# Performs floor division.
# Divides 5 by 3 and keeps only the whole number part.
# Output will be 1.

print(2 ** 3)
# Raises 2 to the power of 3 (exponentiation).
# Output will be 8.

# PEMDASLR Order
# ()   → Parentheses (highest priority)
# **   → Exponents
# * /  → Multiplication and Division (left to right)
# + -  → Addition and Subtraction (left to right)

# Outputs 7
print(3 * 3 + 3 / 3 - 3)
# Python first evaluates multiplication and division:
# 3 * 3 = 9, 3 / 3 = 1
# Then it evaluates addition and subtraction:
# 9 + 1 - 3 = 7

# Outputs 7
print(3 * 3 + 3 / 3 - 3)
# This line is identical to the previous one.
# Since the expression is the same, the output is also 7.
