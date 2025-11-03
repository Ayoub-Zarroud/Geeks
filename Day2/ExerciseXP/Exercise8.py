# Exercise 8: Pizza Toppings

toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)

total_cost = 10 + len(toppings) * 2.5
print("\nYour pizza toppings:", toppings)
print("Total cost: $", total_cost)
