# Exercise 12: Check if string is palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
print("Exercise 12:", is_palindrome('radar'))
print("Exercise 12:", is_palindrome('John'))