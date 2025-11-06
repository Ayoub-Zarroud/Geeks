# Exercise 10: Print longest word in list
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    print("Exercise 10:", longest)
longest_word(["apple", "banana", "strawberry", "kiwi"])