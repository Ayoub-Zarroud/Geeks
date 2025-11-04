# Exercise 2: Birthdays Advanced

birthdays = {
    "Alice": "1998/05/14",
    "Bob": "2000/09/22",
    "Charlie": "1995/12/30",
    "Diana": "2002/07/03",
    "Ethan": "1999/11/10"
}

print("Welcome to the Birthday Dictionary!")
print("Here are the people in the list:")

# Print all names
for person in birthdays:
    print("-", person)

# Ask for name
name = input("\nEnter a person's name: ")

# Check and print birthday
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")
