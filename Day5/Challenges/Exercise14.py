# Exercise 14: Average value in dictionary
def dict_avg(d):
    total = 0
    count = 0
    for value in d.values():
        total += value
        count += 1
    return total / count
print("Exercise 14:", dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))
