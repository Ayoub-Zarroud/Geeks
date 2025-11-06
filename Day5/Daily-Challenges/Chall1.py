# Step 1: Get Input
words = input("Enter words separated by commas: ")  # e.g., "without,hello,bag,world"
# Step 2: Split the String into a List
word_list = words.split(",")  # ['without', 'hello', 'bag', 'world']
# Step 3: Sort the List Alphabetically
word_list.sort()  # ['bag', 'hello', 'without', 'world']
# Step 4: Join the Sorted List Back into a String
sorted_words = ",".join(word_list)
# Step 5: Print the Result
print("Sorted words:", sorted_words)
