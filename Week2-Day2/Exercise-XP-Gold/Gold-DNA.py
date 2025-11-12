import random

class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.choice([0, 1])
    def mutate(self):
        """Flip the gene value (0 → 1 or 1 → 0)."""
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)

class Chromosome:
    def __init__(self, genes=None):
        self.genes = genes if genes else [Gene() for _ in range(10)]
    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()
    def all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __repr__(self):
        return "".join(str(g) for g in self.genes)
class DNA:
    def __init__(self, chromosomes=None):
        self.chromosomes = chromosomes if chromosomes else [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()
    def all_ones(self):
        return all(chromosome.all_ones() for chromosome in self.chromosomes)

    def __repr__(self):
        return "\n".join(str(chromosome) for chromosome in self.chromosomes)
class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment
    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.all_ones()
if __name__ == "__main__":
    random.seed() 
    population_size = 20
    environment_factor = 0.6  

    organisms = [Organism(DNA(), environment_factor) for _ in range(population_size)]
    generations = 0
    perfect_found = False
    while not perfect_found:
        generations += 1
        for organism in organisms:
            organism.mutate()
            if organism.is_perfect():
                perfect_found = True
                break
    print(f"✅ Perfect DNA achieved after {generations} generations!")
    print("\nExample of a perfect DNA:\n")
    print(organisms[0].dna)
