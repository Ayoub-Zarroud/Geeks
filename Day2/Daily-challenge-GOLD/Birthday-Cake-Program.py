from datetime import datetime

# Ask for user input
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert the string to a date object
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
today = datetime.today()

# Calculate age
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Get the last digit of age
candles = age % 10

# Create candles string
candle_line = "i" * candles

# Display the cake
print("       ___" + candle_line + "___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")

# Display age info
print(f"\nYou are {age} years old! 🎂")
