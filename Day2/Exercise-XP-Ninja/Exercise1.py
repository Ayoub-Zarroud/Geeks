# Exercise 1: Formula
# Q = Square root of [(2 * C * D) / H]

import math

C = 50
H = 30

# Get user input
values = input("Enter comma-separated values for D: ").split(',')

# Compute Q for each D
results = []
for D in values:
    D = int(D)
    Q = round(math.sqrt((2 * C * D) / H))
    results.append(Q)

# Print the result
print(",".join(map(str, results)))
