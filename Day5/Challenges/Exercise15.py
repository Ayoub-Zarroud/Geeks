# Exercise 15: Common divisors of 2 numbers
def common_div(a, b):
    divisors = []
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors
print("Exercise 15:", common_div(10, 20))