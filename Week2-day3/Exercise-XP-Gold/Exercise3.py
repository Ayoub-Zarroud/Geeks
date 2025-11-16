import re

def return_numbers(text):
    digits = re.findall(r"\d", text)
    return "".join(digits)

print(return_numbers("k5k3q2g5z6x9bn"))  # Output: 532569
