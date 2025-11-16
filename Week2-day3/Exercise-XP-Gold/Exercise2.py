earth_year_seconds = 31557600
def age_on_planets(seconds):
    earth_year_seconds = 31557600

    planets = {
        "Earth": 1,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }

    for planet, period in planets.items():
        age = seconds / (earth_year_seconds * period)
        print(f"Age on {planet}: {age:.2f} years")

age_on_planets(1_000_000_000)
