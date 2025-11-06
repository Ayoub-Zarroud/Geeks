# Exercise 19: Mimic .split() method
def my_split(s, sep=' '):
    result = []
    word = ''
    for ch in s:
        if ch == sep:
            if word:
                result.append(word)
                word = ''
        else:
            word += ch
    if word:
        result.append(word)
    return result
print("Exercise 19:", my_split("hello world how are you"))
print("Exercise 19:", my_split("apple,banana,grape", ','))
