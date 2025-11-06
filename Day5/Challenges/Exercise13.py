# Exercise 13: Count words longer than k
def sum_over_k(sentence, k):
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > k:
            count += 1
    return count
print("Exercise 13:", sum_over_k('Do or do not there is no try', 2))

