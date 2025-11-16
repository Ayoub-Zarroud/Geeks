import random

class QuantumParticle:
    def __init__(self, x=None, p=None):
        # initial classical attributes
        self.position_value = x if x is not None else self._rand_position()
        self.momentum_value = p if p is not None else self._rand_momentum()
        self.spin_value = self._rand_spin()

        # entanglement partner
        self.entangled_with = None
    # Random generators

    def _rand_position(self):
        return random.randint(1, 10_000)

    def _rand_momentum(self):
        return random.uniform(0, 1)

    def _rand_spin(self):
        return random.choice([0.5, -0.5])
    # Disturbance rule
    def _disturb(self):
        self.position_value = self._rand_position()
        self.momentum_value = self._rand_momentum()
        print("Quantum Interferences!!")

    # Measurements
    def position(self):
        self._disturb()
        return self._rand_position()

    def momentum(self):
        self._disturb()
        return self._rand_momentum()

    def spin(self):
        self._disturb()

        # if entangled, enforce opposite spin
        if self.entangled_with:
            opposite = -self.spin_value
            self.entangled_with.spin_value = opposite
        return self.spin_value

    # Entanglement   
    def entangle(self, other):
        if not isinstance(other, QuantumParticle):
            print("Only two quantum particles can be entangled!")
            return

        # mutual entanglement
        self.entangled_with = other
        other.entangled_with = self

        print("Spooky Action at a Distance !!")

        print(f"Particle {id(self)} is now in quantum entanglement with Particle {id(other)}")
    # Representation
        return (f"QuantumParticle(pos={self.position_value}, "
                f"mom={self.momentum_value:.3f}, "
                f"spin={self.spin_value})")
