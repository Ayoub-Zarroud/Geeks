# Exercise 4: Floats

# A float is a number with a decimal point (e.g., 1.5) whereas an integer has no decimal (e.g., 1)

# Generate 1.5 to 5 with 0.5 steps
float_list = []
num = 1.5
while num <= 5:
    float_list.append(num)
    num += 0.5

print("Generated float list:", float_list)
