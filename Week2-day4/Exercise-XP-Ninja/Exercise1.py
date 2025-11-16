class Temperature:
    """Abstract base class for temperature objects."""
    def to_celsius(self):
        raise NotImplementedError

    def to_kelvin(self):
        raise NotImplementedError

    def to_fahrenheit(self):
        raise NotImplementedError


class Celsius(Temperature):
    def __init__(self, value):
        self.value = value

    def to_celsius(self):
        return self.value

    def to_kelvin(self):
        return self.value + 273.15

    def to_fahrenheit(self):
        return (self.value * 9/5) + 32

    def __repr__(self):
        return f"{self.value}°C"


class Kelvin(Temperature):
    def __init__(self, value):
        self.value = value

    def to_celsius(self):
        return self.value - 273.15

    def to_kelvin(self):
        return self.value

    def to_fahrenheit(self):
        return (self.value - 273.15) * 9/5 + 32

    def __repr__(self):
        return f"{self.value}K"


class Fahrenheit(Temperature):
    def __init__(self, value):
        self.value = value

    def to_celsius(self):
        return (self.value - 32) * 5/9

    def to_kelvin(self):
        return ((self.value - 32) * 5/9) + 273.15

    def to_fahrenheit(self):
        return self.value

    def __repr__(self):
        return f"{self.value}°F"
