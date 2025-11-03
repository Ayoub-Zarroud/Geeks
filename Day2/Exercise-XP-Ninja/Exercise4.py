# Exercise 4: Frequency Of The Words

text = input("Enter a sentence: ")

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

# Print frequency (sorted alphabetically)
for word in sorted(freq.keys()):
    print(f"{word}:{freq[word]}")
