# Exercise 8: L2-norm (square root of sum of squares)
import math
def norm(lst):
    total = 0
    for x in lst:
        total += x ** 2
    return math.sqrt(total)
print("Exercise 8:", norm([1, 2, 2]))