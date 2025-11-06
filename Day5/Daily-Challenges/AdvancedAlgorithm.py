# solution 1 simple loop 
import random
# Generate a list of 20,000 random numbers between 0 and 10,000
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
# Define the target number
target_number = 3728
# Go through all pairs to find sums that match the target
for i in range(len(list_of_numbers)):
    for j in range(i, len(list_of_numbers)):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            print(f"{list_of_numbers[i]} and {list_of_numbers[j]} sum to the target number {target_number}")
''' solution 2 using a set 
import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728
seen = set()  # To store numbers we’ve already checked
for num in list_of_numbers:
    complement = target_number - num  # The number we need to reach the target
    if complement in seen:
        print(f"{num} and {complement} sum to the target number {target_number}")
    seen.add(num)'''
