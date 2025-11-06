# Exercise 5: Find max number in a list
def find_max(lst):
    max_num = lst[0]
    for x in lst:
        if x > max_num:
            max_num = x
    return max_num
print("Exercise 5:", find_max([0, 1, 3, 50]))