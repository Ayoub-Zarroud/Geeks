# Exercise 2: List of Integers

numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2a. Print list
print("List of numbers:", numbers)

# 2b. Sorted descending
print("Sorted descending:", sorted(numbers, reverse=True))

# 2c. Sum of all numbers
print("Sum of numbers:", sum(numbers))

# 3. First and last numbers
print("First and last numbers:", [numbers[0], numbers[-1]])

# 4. Numbers greater than 50
greater_50 = [n for n in numbers if n > 50]
print("Numbers > 50:", greater_50)

# 5. Numbers smaller than 10
smaller_10 = [n for n in numbers if n < 10]
print("Numbers < 10:", smaller_10)

# 6. Squares of numbers
squares = [n ** 2 for n in numbers]
print("Squared numbers:", squares)

# 7. Unique numbers
unique_nums = list(set(numbers))
print("Unique numbers:", unique_nums)
print("Count of unique numbers:", len(unique_nums))

# 8. Average
average = sum(numbers) / len(numbers)
print("Average:", average)

# 9. Largest
print("Largest number:", max(numbers))

# 10. Smallest
print("Smallest number:", min(numbers))

# Bonus 1: Sum, Average, Largest, Smallest (no built-ins)

total = 0
largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    total += n
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

average_manual = total / len(numbers)
print("\nManual Calculations:")
print("Sum:", total)
print("Average:", average_manual)
print("Largest:", largest)
print("Smallest:", smallest)

# Bonus 2: Ask user for 10 numbers

user_numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i+1} between -100 and 100: "))
    user_numbers.append(num)

print("Your numbers:", user_numbers)

# Bonus 3: Generate 10 random numbers between -100 and 100

import random

random_numbers = [random.randint(-100, 100) for _ in range(10)]
print("Random numbers:", random_numbers)

# Bonus 4: Random count of random integers
import random

count = random.randint(50, 100)  # Random amount, no smaller than 50
random_nums = [random.randint(-100, 100) for _ in range(count)]

print(f"Generated {count} random numbers.")
print(random_nums)
