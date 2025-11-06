# Exercise 18: Count data types in keyworded arguments
def type_count(**kwargs):
    type_dict = {}
    for value in kwargs.values():
        t = type(value).__name__
        type_dict[t] = type_dict.get(t, 0) + 1
    for t, count in type_dict.items():
        print(f"{t}: {count}")
type_count(a=1, b='string', c=1.0, d=True, e=False)
