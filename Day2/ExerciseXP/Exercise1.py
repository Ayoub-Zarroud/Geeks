# Exercise 1: Favorite Numbers

# Create a set of favorite numbers
my_fav_numbers = {3, 7, 13}
my_fav_numbers.add(21)
my_fav_numbers.add(42)
print("My favorite numbers after adding:", my_fav_numbers)

# Remove the last number added (42)
my_fav_numbers.remove(42)
print("After removing last added number:", my_fav_numbers)

# Friend's favorite numbers
friend_fav_numbers = {5, 13, 25}

# Concatenate using union
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)
