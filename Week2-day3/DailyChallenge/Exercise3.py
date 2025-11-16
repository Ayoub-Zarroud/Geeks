# Daily Challenge GOLD - User Info

data = []

print("Enter user info 5 times: Name Age Score")
for _ in range(5):
    user_input = input("Enter Name,Age,Score (example: Tom,19,80): ")
    name, age, score = user_input.split(",")
    data.append((name, age, score))
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1]), int(x[2])))

print(sorted_data)
