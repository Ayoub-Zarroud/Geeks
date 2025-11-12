import random
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
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args] + [self.name])
        print(f"{dog_names} all play together")
    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs",
                      "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet.")
# Step 3: Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
dog_buddy = PetDog("Buddy", 3, 15)
dog_max = PetDog("Max", 1, 8)
my_dog.train()
my_dog.play(dog_buddy, dog_max)
my_dog.do_a_trick()
