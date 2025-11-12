class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return self.weight / self.age * 10
    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}"
        else:
            return f"{other_dog.name} wins the fight against {self.name}"
# Step 2: Create dog instances
dog1 = Dog("Rex", 4, 20)
dog2 = Dog("Max", 2, 15)
dog3 = Dog("Buddy", 3, 25)
# Step 3: Test dog methods
print(dog1.bark())
print(f"{dog2.name}'s run speed: {dog2.run_speed()}")
print(dog1.fight(dog3))
