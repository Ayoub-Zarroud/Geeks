import random

def throw_dice():
    """Return a random integer between 1 and 6."""
    return random.randint(1, 6)
def throw_until_doubles():
    """Keep rolling two dice until both show the same number."""
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        # Uncomment below to see each roll
        # print(f"Roll {count}: ({dice1}, {dice2})")
        if dice1 == dice2:
            break
    return count

def main():
    results = []

    for _ in range(100):
        throws = throw_until_doubles()
        results.append(throws)

    total_throws = sum(results)
    average_throws = round(total_throws / len(results), 2)

    print(f"Total throws to reach 100 doubles: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws}")
# Run the program
main()
