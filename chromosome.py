"""Chromosome representation for genetic algorithm"""


class Chromosome:
    """Real-valued representation of a chromosome"""

    def __init__(self, genes, bounds, precision):
        if not isinstance(genes, list) or not all(isinstance(g, (int, float)) for g in genes):
            raise ValueError("Genes must be a list of real numbers.")
        if not isinstance(bounds, list) or not all(isinstance(b, tuple) and len(b) == 2 for b in bounds):
            raise ValueError(
                "Bounds must be a list of tuples with two numeric values.")
        if not isinstance(precision, int) or precision < 0:
            raise ValueError("Precision must be a non-negative integer.")
        if len(genes) != len(bounds):
            raise ValueError(
                "The number of genes must match the number of bounds.")

        self.genes = [round(g, precision) for g in genes]
        self.bounds = bounds
        self.precision = precision
        self.fitness = None

    def evaluate_fitness(self, func=None):
        """Evaluate the fitness of the chromosome using the provided function."""
        if func is None:
            raise ValueError(
                "A fitness function must be provided to evaluate the chromosome.")

        self.fitness = func(self.genes)
        return self.fitness
