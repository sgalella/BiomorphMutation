import numpy as np


MAX_LEN = 9
MAX = 100


def show_phenotype(ax, x, y, length, d, dx, dy):
    """
    Displays the phenotype of the individual.

    Args:
        ax (matplotlib.axes): Figure axis to display the phenotype.
        x (int): Starting point x-axis.
        y (int): Starting point y-axis.
        length (int): Recursion length.
        d (int): Beginning index phenotype.
        dx (np.array): Phenotype x-axis.
        dy (np.array): Phenotype y-axis.
    """
    if d < 0:
        d += 8
    elif d >= 8:
        d -= 8
    if length > 0:
        x_new = x + length * dx[d]
        y_new = y + length * dy[d]
        draw_line(ax, x, y, x_new, y_new)
        show_phenotype(ax, x_new, y_new, length - 1, d - 1, dx, dy)
        show_phenotype(ax, x_new, y_new, length - 1, d + 1, dx, dy)


def genome_to_phenotype(genome):
    """
    Generates the phenotype dx and dy for a given gene.

    Args:
        gene (np.array): Genome of the biomorph.

    Returns:
        tuple: Recursion length, phenotype dx and phenotype dy
    """
    # Get points in the x-axis
    dx = np.zeros((8, ))
    dx[0] = - genome[1]
    dx[1] = - genome[0]
    dx[3] = genome[0]
    dx[4] = genome[1]
    dx[5] = genome[2]
    dx[7] = - genome[2]

    # Get points in the y-axis
    dy = np.zeros((8, ))
    dy[0] = genome[5]
    dy[1] = genome[4]
    dy[2] = genome[3]
    dy[3] = genome[4]
    dy[4] = genome[5]
    dy[5] = genome[6]
    dy[6] = genome[7]
    dy[7] = genome[6]

    # Get length of recursion
    length = genome[8]

    return length, dx, dy


def draw_line(ax, x, y, x_new, y_new):
    """
    Draws biomorph line.

    Args:
        ax (matplotlib.axes): Figure axis to display the phenotype.
        x (int): Starting point x-axis.
        y (int): Starting point y-axis.
        x_new (int): Next point x-axis.
        y_new (int): Next point y-axis.
    """
    ax.plot([x, x_new], [y, y_new], 'k')


def initialize_random_genome():
    """
    Creates a random genome for a biomorph.

    Returns:
        np.array: Genome with 9 different genes.
    """
    genome = np.zeros((9, ))
    genome[:-1] = np.random.randint(2 * MAX, size=(8, )) - MAX  # Between [-MAX, MAX]
    genome[-1] = 1
    return genome


def mutate_genome(genome):
    """
    Changes one gene from the genome.

    Args:
        gene (np.array): Genome with 9 different genes.

    Returns:
        np.array: Genome with one gene mutated.
    """
    mutated_genome = genome.copy()
    gene = np.random.randint(9)
    if np.random.random() > 0.5:
        if gene == 8 and mutated_genome[gene] < MAX_LEN:  # Prevent recursion depth to be large
            mutated_genome[gene] += 1
    else:
        if gene != 8:
            mutated_genome[gene] -= 1
    return mutated_genome
