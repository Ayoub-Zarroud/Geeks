list1 = [5, 10, 15, 20, 25, 50, 20]

# Check if 20 is in the list
if 20 in list1:
    index = list1.index(20)   # Get index of first occurrence
    list1[index] = 200        # Replace with 200

print(list1)

