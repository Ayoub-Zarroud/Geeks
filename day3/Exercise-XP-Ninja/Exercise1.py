# Exercise 1: Cars

# Step 1: Given string
car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Step 2: Convert the string into a list
car_list = car_string.split(", ")

# Step 3: Print how many manufacturers are in the list
print(f"There are {len(car_list)} manufacturers in the list.")

# Step 4: Print the list in reverse (Z–A)
print("Manufacturers in reverse (Z–A):")
print(sorted(car_list, reverse=True))

# Step 5: Count how many have the letter 'o'
count_o = sum(['o' in name.lower() for name in car_list])
print(f"Number of manufacturers with the letter 'o': {count_o}")

# Step 6: Count how many do NOT have the letter 'i'
count_no_i = sum(['i' not in name.lower() for name in car_list])
print(f"Number of manufacturers without the letter 'i': {count_no_i}")

# ==============================
# 🌟 BONUS PART
# ==============================

# Duplicate list
cars_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Step 7: Remove duplicates using set
unique_cars = list(set(cars_with_duplicates))

# Step 8: Print unique companies as a comma-separated string
print("\nCompanies without duplicates:")
print(", ".join(unique_cars))

# Step 9: Print how many unique companies there are
print(f"Number of unique companies: {len(unique_cars)}")

# Step 10: Print the list of manufacturers in ascending order (A–Z)
#          but reverse the letters of each manufacturer's name
sorted_reversed = [name[::-1] for name in sorted(unique_cars)]
print("\nManufacturers A–Z, but with names reversed:")
print(sorted_reversed)
