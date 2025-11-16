import string
import random

letters = string.ascii_letters   # A-Z + a-z

result = ""
for _ in range(5):
    result += random.choice(letters)

print(result)
