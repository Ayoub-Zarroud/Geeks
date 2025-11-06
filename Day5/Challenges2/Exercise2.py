my_list = [2, 24, 12, 354, 233]  # initial list
# Outer loop → runs from i = 0 to len(my_list)-2
for i in range(len(my_list) - 1):  # i = 0 → 3
    minimum = i                    # assume the current i is the minimum index
    for j in range(i + 1, len(my_list)):  # inner loop checks all remaining elements
        if my_list[j] < my_list[minimum]: # if we find a smaller element
            minimum = j                   # update the index of minimum
            if minimum != i:              # if smaller element found at a different index
                # swap elements
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# Print final sorted list
print(my_list)

# output: [2, 12, 24, 233, 354]