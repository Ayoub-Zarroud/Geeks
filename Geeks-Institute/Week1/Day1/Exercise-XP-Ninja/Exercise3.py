print(3 <= 3 < 9)        # True (3 <= 3 and 3 < 9)
print(3 == 3 == 3)       # True (all equal)
print(bool(0))            # False (0 is falsy)
print(bool(5 == "5"))     # False (int 5 != str "5")
print(bool(4 == 4) == bool("4" == "4"))  # True (True == True)
print(bool(bool(None)))   # False (None is falsy, bool(None) = False, bool(False) = False)

x = (1 == True)           # True (True is 1)
y = (1 == False)          # False
a = True + 4              # 5 (True = 1, 1+4=5)
b = False + 10            # 10 (False = 0, 0+10=10)

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
