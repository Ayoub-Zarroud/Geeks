# Exercise 2: Tuple

a_tuple = (10, 20, 30, 40)

# Tuples are immutable — you cannot modify them directly
# The following would cause an error if uncommented:
# a_tuple.append(50)

# Instead, you can create a new tuple by concatenation
a_tuple = a_tuple + (50, 60)
print("Updated tuple (by creating a new one):", a_tuple)
