# Exercise 9: Cinemax Tickets

ages = input("Enter ages of family members (separated by spaces): ").split()
ages = [int(age) for age in ages]

total_cost = 0
for age in ages:
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost

print("Total ticket cost: $", total_cost)

# Bonus: Restricted movie (16–21)
allowed = [age for age in ages if 16 <= age <= 21]
print("Allowed attendees (ages 16–21):", allowed)
