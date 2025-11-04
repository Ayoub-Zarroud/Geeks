users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Characters to indices
dict1 = {name: i for i, name in enumerate(users)}

# 2. Indices to characters
dict2 = {i: name for i, name in enumerate(users)}

# 3. Alphabetically sorted characters
sorted_users = sorted(users)
dict3 = {name: i for i, name in enumerate(sorted_users)}

print("1.", dict1)
print("2.", dict2)
print("3.", dict3)
