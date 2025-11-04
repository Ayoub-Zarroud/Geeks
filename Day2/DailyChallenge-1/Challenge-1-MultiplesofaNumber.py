# Ask for user inputs
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Create an empty list to store multiples
multiples = []

# Generate the multiples using a loop
for i in range(1, length + 1):
    multiples.append(number * i)

# Display the result
print(multiples)
