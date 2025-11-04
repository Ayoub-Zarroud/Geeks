# Ask for user input
word = input("Enter a word: ")

# Initialize a variable to hold the result
result = ""

# Loop through each character in the word
for i in range(len(word)):
    # Add the character only if it's not the same as the previous one
    if i == 0 or word[i] != word[i - 1]:
        result += word[i]

# Display the final string
print(result)
