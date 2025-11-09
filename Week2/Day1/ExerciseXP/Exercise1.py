# Step 1: Define the Cat class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 2: Create cat objects
cat1 = Cat("Hassan", 2)
cat2 = Cat("hamza", 5)
cat3 = Cat("lili", 3)

# Step 3: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = max([cat1, cat2, cat3], key=lambda cat: cat.age)
    return oldest

# Step 4: Get and print the oldest cat’s details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
