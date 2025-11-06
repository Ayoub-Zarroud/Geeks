
# Exercise 7: Count element in list (without .count())
def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
print("Exercise 7:", list_count(['a', 'a', 't', 'o'], 'a'))