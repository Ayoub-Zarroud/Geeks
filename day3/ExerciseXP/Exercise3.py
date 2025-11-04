# Create dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 1. Change number_stores to 2
brand["number_stores"] = 2

# 2. Print sentence describing Zara’s clients
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")

# 3. Add new key
brand["country_creation"] = "Spain"

# 4. Add 'Desigual' to competitors if key exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 5. Delete creation_date
brand.pop("creation_date")

# 6. Print last international competitor
print("Last competitor:", brand["international_competitors"][-1])

# 7. Print major colors in the US
print("Major colors in the US:", brand["major_color"]["US"])

# 8. Print number of keys
print("Number of keys:", len(brand))

# 9. Print all keys
print("All keys:", list(brand.keys()))

# Bonus: Merge another dictionary
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print("\nMerged dictionary:", brand)
