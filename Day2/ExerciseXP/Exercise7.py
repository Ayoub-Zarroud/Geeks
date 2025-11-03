# Exercise 7: Favorite Fruits

fav_fruits = input("Enter your favorite fruits (separated by spaces): ").split()
chosen_fruit = input("Enter a fruit name: ")

if chosen_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
