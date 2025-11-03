# Exercise 3: Check the Index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")

if user_name in names:
    print(f"The index of the first occurrence of {user_name} is:", names.index(user_name))
else:
    print("Name not found in the list.")
