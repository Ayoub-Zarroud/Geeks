# Take input from the user
Reverseinp = input("Enter a sentence: ")

# Split the sentence into words, reverse the list, and join it back
reversed_sentence = ' '.join(Reverseinp.split()[::-1])

# Print the reversed sentence
print(reversed_sentence)
