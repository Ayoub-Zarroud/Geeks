# Exercise 4: Sum of list (without sum function)
def my_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total
print("Exercise 4:", my_sum([1, 5, 4, 2]))