import random

# Step 1: Choose a random word
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist).lower()
# Step 2: Initialize game state
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
# Display version of the word (hide letters with '*')
display_word = ['*' if letter != ' ' else ' ' for letter in word]
# Hangman stages (ASCII art)
stages = [
    """
      +---+
          |
          |
          |
        ===""",
    """
      +---+
      O   |
          |
          |
        ===""",
    """
      +---+
      O   |
      |   |
          |
        ===""",
    """
      +---+
      O   |
     /|   |
          |
        ===""",
    """
      +---+
      O   |
     /|\\  |
          |
        ===""",
    """
      +---+
      O   |
     /|\\  |
     /    |
        ===""",
    """
      +---+
      O   |
     /|\\  |
     / \\  |
        ==="""
]
    # Step 3: Main game loop
print("Welcome to Hangman!")
print("Try to guess the word before the man is hanged!\n")

while wrong_guesses < max_wrong and '*' in display_word:
    print(stages[wrong_guesses])  # show hangman stage
    print("\nWord:", ''.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    print(f"Remaining attempts: {max_wrong - wrong_guesses}\n")
    guess = input("Guess a letter or the full word: ").lower().strip()
    # Validate input
    if not guess.isalpha() and ' ' not in guess:
        print("Please enter a valid letter or word.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that.\n")
        continue
    guessed_letters.append(guess)
    # If guess is a single letter
    if len(guess) == 1:
        if guess in word:
            print("Correct letter!\n")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print("Wrong letter!\n")
            wrong_guesses += 1
    # If guess is the full word
    else:
        if guess == word:
            display_word = list(word)
            print("Amazing! You guessed the full word correctly!\n")
            break
        else:
            print("Wrong word guess! A body part is added!\n")
            wrong_guesses += 1
# Step 4: Game over — win or lose
print(stages[wrong_guesses])
print("\nThe word was:", word)

if '*' not in display_word:
    print("Congratulations! You guessed the word!")
else:
    print("Game over! The man has been hanged.")
