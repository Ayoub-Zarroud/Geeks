import re

def validate_name(name):
    pattern = r"^[A-Z][a-zA-Z]+ [A-Z][a-zA-Z]+$"
    
    if re.fullmatch(pattern, name):
        print("Valid name!")
    else:
        print("Invalid name!")

user_name = input("Enter your full name: ")
validate_name(user_name)
