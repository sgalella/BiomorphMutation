import os
import shutil

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


MAX = 100
MAX_LEN = 9
DIR = 2
X = 0
Y = 0


def show_phenotype(x, y, length, d, dx, dy, ax):
    if d < 0:
        d += 8
    elif d >= 8:
        d -= 8
    if length > 0:
        x_new = x + length * dx[d]
        y_new = y + length * dy[d]
        draw_line(ax, x, y, x_new, y_new)
        show_phenotype(x_new, y_new, length - 1, d - 1, dx, dy, ax)
        show_phenotype(x_new, y_new, length - 1, d + 1, dx, dy, ax)


def gene_to_phenotype(gene):
    # Get points in the x-axis
    dx = np.zeros((8, ))
    dx[0] = - gene[1]
    dx[1] = - gene[0]
    dx[3] = gene[0]
    dx[4] = gene[1]
    dx[5] = gene[2]
    dx[7] = - gene[2]

    # Get points in the y-axis
    dy = np.zeros((8, ))
    dy[0] = gene[5]
    dy[1] = gene[4]
    dy[2] = gene[3]
    dy[3] = gene[4]
    dy[4] = gene[5]
    dy[5] = gene[6]
    dy[6] = gene[7]
    dy[7] = gene[6]

    # Get length of recursion
    length = gene[8]

    return length, dx, dy


def draw_line(ax, x, y, x_new, y_new):
    ax.plot([x, x_new], [y, y_new], 'k')


def initialize_random_gene():
    gene = np.zeros((9, ))
    gene[:-1] = np.random.randint(2 * MAX, size=(8, )) - MAX  # Between [-MAX, MAX]
    gene[-1] = 1
    return gene


def mutate_gene(gene):
    mutated_gene = gene.copy()
    idx = np.random.randint(9)
    if np.random.random() > 0.5:
        if idx == 8 and mutated_gene[idx] < MAX_LEN:  # Prevent recursion depth to be large
            mutated_gene[idx] += 1
    else:
        if idx != 8:
            mutated_gene[idx] -= 1
    return mutated_gene


def main():
    np.random.seed(123)
    if os.path.isdir('images'):
        shutil.rmtree('images')
    os.mkdir('images')
    num_generations = 300
    gene = initialize_random_gene()
    length, dx, dy = gene_to_phenotype(gene)

    f = plt.figure(figsize=(4, 4))
    ax = plt.gca()
    show_phenotype(X, Y, length, DIR, dx, dy, ax)
    ax.set_title('Generation 0')
    plt.axis('off')
    f.savefig(f'images/{0:04d}.png')
    
    for i in tqdm(range(1, num_generations + 1)):
        ax.cla()
        gene = mutate_gene(gene)
        length, dx, dy = gene_to_phenotype(gene)
        show_phenotype(X, Y, length, DIR, dx, dy, ax)
        ax.set_title(f'Generation {i}')
        plt.axis('off')
        f.savefig(f'images/{i:04d}.png')


if __name__ == '__main__':
    main()
