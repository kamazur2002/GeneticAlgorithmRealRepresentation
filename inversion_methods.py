import random


class InversionMethods:
    """Class implementing inversion operations for real-representation chromosomes."""

    @staticmethod
    def two_point_inversion(genes, bounds):
        """
        Standard two-point inversion — reverse order of genes between two random points.
        """
        new_genes = genes.copy()
        if len(genes) < 2:
            return new_genes

        i, j = sorted(random.sample(range(len(genes)), 2))
        new_genes[i:j + 1] = reversed(new_genes[i:j + 1])

        for index in range(i, j + 1):
            if not (bounds[index][0] <= new_genes[index] <= bounds[index][1]):
                return genes
        return new_genes