import random
class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reversed_list(self):
        return list(reversed(self.letters))

    def sorted_list(self):
        return sorted(self.letters)

    # Bonus: generate a list of random numbers with same length
    def random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]
# Example usage:
my_list = MyList(['d', 'a', 'c', 'b'])
print("Original List:", my_list.letters)
print("Reversed List:", my_list.reversed_list())
print("Sorted List:", my_list.sorted_list())
print("Random List:", my_list.random_list())
