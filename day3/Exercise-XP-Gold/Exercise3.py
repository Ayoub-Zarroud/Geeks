# Exercise 3: Add Your Own Birthday

birthdays = {
    "Alice": "1998/05/14",
    "Bob": "2000/09/22",
    "Charlie": "1995/12/30",
    "Diana": "2002/07/03",
    "Ethan": "1999/11/10"
}

print("Welcome to the Birthday Dictionary!")

# Step 1: Add new birthday
new_name = input("Enter a new person's name: ")
new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")

# Step 2: Add to dictionary
birthdays[new_name] = new_birthday

# Step 3: Show available names
print("\nHere are all the people in the list now:")
for person in birthdays:
    print("-", person)

# Step 4: Ask to look up a birthday
name = input("\nEnter a person's name to look up: ")

if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don't have the birthday information for {name}.")
