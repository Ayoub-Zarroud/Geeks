# Exercise 1: Birthday Look-up

# Step 1: Create dictionary of birthdays
birthdays = {
    "Alice": "1998/05/14",
    "Bob": "2000/09/22",
    "Charlie": "1995/12/30",
    "Diana": "2002/07/03",
    "Ethan": "1999/11/10"
}

# Step 2: Welcome message
print("Welcome to the Birthday Dictionary!")
print("You can look up the birthdays of the people in the list!\n")

# Step 3: Ask for a name
name = input("Enter a person's name: ")

# Step 4: Print their birthday
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")
