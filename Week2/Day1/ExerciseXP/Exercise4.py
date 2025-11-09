# Step 1: Define the Zoo Class
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    # Add one or more animals
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
        print(f"Animals after adding: {self.animals}")

    # Display all animals
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)
        print()  # Empty line for readability

    # Remove an animal if it exists
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
        print(f"Animals after selling: {self.animals}")

    # Sort and group animals alphabetically
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = [animal]
            else:
                grouped[first_letter].append(animal)

        self.grouped_animals = grouped
        print("Animals have been sorted and grouped!")
        return grouped

    # Display the grouped animals
    def get_groups(self):
        if hasattr(self, 'grouped_animals'):
            print("Animal Groups:")
            for letter, group in self.grouped_animals.items():
                print(f"{letter}: {group}")
        else:
            print("No groups found. Please run sort_animals() first.")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Zebra", "Lion", "Cougar", "Cat")
brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
