# Exercise 6: Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Exercise 6:", factorial(4))