x = int(input('Enter the Number: '))

# Initialize sum of divisors
sum_divisors = 0

# Find all divisors (excluding the number itself)
for i in range(1, x):
    if x % i == 0:
        sum_divisors += i

# Check if it’s a perfect number
if sum_divisors == x:
    print(True)
else:
    print(False)
