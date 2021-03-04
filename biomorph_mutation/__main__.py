import os
import shutil

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

import biomorph_mutation.utils as utils

# Set seed (for reproducibility)
np.random.seed(4321)

# Create output folders
if os.path.isdir('biomorphs'):
    shutil.rmtree('biomorphs')
os.mkdir('biomorphs')

# Initialize genotype and phenotype
dir = 2
x = 0
y = 0
num_generations = 1000
gene = utils.initialize_random_genome()
length, dx, dy = utils.genome_to_phenotype(gene)

# Generate biomorphs
f = plt.figure(figsize=(4, 4))
ax = plt.gca()
utils.show_phenotype(ax, x, y, length, dir, dx, dy)
ax.set_title('Generation 0')
plt.axis('off')
f.savefig(f'biomorphs/{0:04d}.png')

for i in tqdm(range(1, num_generations + 1)):
    ax.cla()
    gene = utils.mutate_genome(gene)
    length, dx, dy = utils.genome_to_phenotype(gene)
    utils.show_phenotype(ax, x, y, length, dir, dx, dy)
    ax.set_title(f'Generation {i}')
    plt.axis('off')
    f.savefig(f'biomorphs/{i:04d}.png')
