# Exercise 9: Check if array is monotonic
def is_mono(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)
print("Exercise 9:", is_mono([7, 6, 5, 5, 2, 0]))
print("Exercise 9:", is_mono([1, 2, 0, 4]))