# Challenge 1: Letter Index Dictionary

# Step 1: Get user input
word = input("Enter a word: ")

# Step 2: Create an empty dictionary
letter_indices = {}

# Step 3: Loop through each letter with its index
for index, letter in enumerate(word):
    if letter in letter_indices:
        # Append index to existing list
        letter_indices[letter].append(index)
    else:
        # Create new key with index in a list
        letter_indices[letter] = [index]

# Step 4: Print the dictionary
print(letter_indices)
