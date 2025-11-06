# Exercise 3: Count uppercase and lowercase letters
s = "Hello World!"
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Exercise 3:", "Uppercase:", upper, "Lowercase:", lower)