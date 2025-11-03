# Exercise 6: While Loop

while True:
    name = input("Enter your name: ")
    if not name.isdigit() and len(name) >= 3:
        print("Thank you!")
        break
    else:
        print("Invalid name. Please try again.")
