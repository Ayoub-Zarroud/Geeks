# Exercise 3: Working on a Paragraph

paragraph = """Artificial intelligence is transforming the world. 
It helps us solve complex problems, automate tasks, and make decisions faster. 
However, it also raises important questions about ethics and responsibility."""

# Count characters
char_count = len(paragraph)

# Split into sentences and words
sentences = paragraph.split('.')
sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty ones
words = paragraph.split()
unique_words = set(words)

# Basic analysis
print("Characters:", char_count)
print("Sentences:", len(sentences))
print("Words:", len(words))
print("Unique words:", len(unique_words))

# Bonus
non_whitespace_chars = len(paragraph.replace(" ", ""))
avg_words_per_sentence = len(words) / len(sentences)
non_unique = len(words) - len(unique_words)

print("Non-whitespace characters:", non_whitespace_chars)
print("Average words per sentence:", round(avg_words_per_sentence, 2))
print("Non-unique words:", non_unique)
