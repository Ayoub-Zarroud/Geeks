# Exercise 11: Separate integers and strings
mixed = [1, "two", 3, "four", 5, "six"]
ints = []
strings = []
for x in mixed:
    if isinstance(x, int):
        ints.append(x)
    elif isinstance(x, str):
        strings.append(x)
print("Exercise 11:", "Integers:", ints, "Strings:", strings)