# Exercise 17: Print elements if index and value are even
def weird_print(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            result.append(lst[i])
    return result
print("Exercise 17:", weird_print([1, 2, 2, 3, 4, 5]))