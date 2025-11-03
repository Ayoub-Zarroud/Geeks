# Exercise 6: Words and Letters

words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

letter = input("Enter a single letter: ")

for word in words:
    if letter in word:
        print(f"In '{word}', the letter '{letter}' first appears at index {word.index(letter)}.")
    else:
        print(f"The letter '{letter}' does not appear in '{word}'.")
