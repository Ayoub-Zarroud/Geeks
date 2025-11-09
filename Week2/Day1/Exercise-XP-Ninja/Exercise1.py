class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Step 3 & Step 8: Add animals (supports single or multiple using kwargs)
    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Add single animal if provided
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # Add multiple animals using kwargs
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    # Step 4: Display farm info
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-O!"
        return info

    # Step 6: Get sorted list of animal types
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Step 7: Get short info about farm animals
    def get_short_info(self):
        animal_types = self.get_animal_types()
        if not animal_types:
            return f"{self.name}'s farm has no animals yet."

        # Create pluralized list
        formatted_animals = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                formatted_animals.append(animal + "s")
            else:
                formatted_animals.append(animal)

        # Format list nicely (with commas and 'and' before last item)
        if len(formatted_animals) > 1:
            animals_text = ", ".join(formatted_animals[:-1]) + " and " + formatted_animals[-1]
        else:
            animals_text = formatted_animals[0]

        return f"{self.name}'s farm has {animals_text}."

# -------------------- TESTING --------------------
macdonald = Farm("McDonald")

# Add animals individually
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Add multiple animals at once (bonus feature using kwargs)
macdonald.add_animal(chicken=4, duck=2)

# Print formatted info
print(macdonald.get_info())
print("\nAnimal types:", macdonald.get_animal_types())
print(macdonald.get_short_info())
