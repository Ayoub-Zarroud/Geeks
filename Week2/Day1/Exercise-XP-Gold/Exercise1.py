import math
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("A circle is a shape consisting of all points in a plane that are a given distance (radius) from a given point (the center).")
# Example usage:
circle1 = Circle(5)
print(f"Perimeter: {circle1.perimeter():.2f}")
print(f"Area: {circle1.area():.2f}")
circle1.definition()
