def longest_word(sentence):
    # Step 2: Split the Sentence into Words
    words = sentence.split()  # Split by spaces into a list of words
    # Step 3: Initialize Variables
    longest = ""  # This will store the longest word found so far
    # Step 4: Iterate Through the Words
    for word in words:
        # Step 5: Compare Word Lengths
        if len(word) > len(longest):
            longest = word  # Update the longest word  
    # Step 6: Return the Longest Word
    return longest
print(longest_word("Margaret's toy is a pretty doll."))        # Expected → Margaret's
print(longest_word("A thing of beauty is a joy forever."))     # Expected → forever.
print(longest_word("Forgetfulness is by all means powerless!")) # Expected → Forgetfulness
