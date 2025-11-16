import math

def accepts_radius_or_diameter(func):
    def wrapper(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("You must provide either radius or diameter.")
        if radius is not None and diameter is not None:
            raise ValueError("Provide only radius OR diameter, not both.")

        # Convert diameter → radius if needed
        if diameter is not None:
            radius = diameter / 2

        func(self, radius)
    return wrapper


class Circle:

    @accepts_radius_or_diameter
    def __init__(self, radius):
        self.radius = radius

    # Properties 
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    # Dunder Methods 
    def __repr__(self):
        return f"Circle(radius={self.radius:.2f})"

    def __str__(self):
        return f"Circle with radius {self.radius:.2f} and diameter {self.diameter:.2f}"

    # Add two circles → new circle
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    # Compare greater-than
    def __gt__(self, other):
        return self.radius > other.radius

    # Compare equality
    def __eq__(self, other):
        return self.radius == other.radius

    # Compare less-than → required for sorting lists
    def __lt__(self, other):
        return self.radius < other.radius

# Test

if __name__ == "__main__":

    c1 = Circle(radius=4)
    c2 = Circle(diameter=10)
    c3 = Circle(radius=2)
    c4 = Circle(diameter=20)

    print(c1)
    print(c2)
    print(c3)
    print(c4)
    # Areas
    print("\nAreas:")
    print(c1.area)
    print(c2.area)
    # Addition
    new_circle = c1 + c2
    print("\nNew Circle from Addition:", new_circle)
    # Comparisons
    print("\nComparisons:")
    print("c1 > c2 ?", c1 > c2)
    print("c1 == c2 ?", c1 == c2)
    print("c3 < c4 ?", c3 < c4)
    # Sorting
    circles = [c1, c2, c3, c4]
    sorted_circles = sorted(circles)
    print("\nSorted Circles:")
    for c in sorted_circles:
        print(c)
