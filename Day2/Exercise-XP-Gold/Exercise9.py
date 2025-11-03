# Exercise 9: Random Number Guessing Game

import random

wins = 0
losses = 0

while True:
    user_input = input("Guess a number from 1 to 9 (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break

    user_num = int(user_input)
    random_num = random.randint(1, 9)

    if user_num == random_num:
        print("🎉 Winner!")
        wins += 1
    else:
        print(f"Better luck next time! The correct number was {random_num}.")
        losses += 1

print(f"\nGame over! You won {wins} times and lost {losses} times.")
