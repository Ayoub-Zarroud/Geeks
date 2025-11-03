longest_sentence = ""

while True:
    sentence = input("Enter a sentence without the character 'A': ")
    if "A" in sentence.upper():
        print("Your sentence contains 'A'. Try again.")
    elif len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! you make one without A")
    else:
        print("Try again to beat the longest sentence!")
