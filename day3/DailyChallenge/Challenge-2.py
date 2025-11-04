# Challenge 2: Affordable Items

# Step 1: Store the given data
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Step 2: Clean the data
# Convert wallet amount to integer
wallet = int(wallet.replace("$", "").replace(",", ""))

# Convert prices in the dictionary to integers
cleaned_items = {item: int(price.replace("$", "").replace(",", "")) for item, price in items_purchase.items()}

# Step 3: Determine affordable items
basket = []

for item, price in cleaned_items.items():
    if wallet >= price:
        basket.append(item)
        wallet -= price  # Subtract the price from wallet

# Step 4: Print the result
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
