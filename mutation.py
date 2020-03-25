import numpy as np
from random import random
from Individual import Individual
from Task import Task


def mutate(individual: Individual, mutation_rate):
    no_of_genes_to_mutate = int(mutation_rate * individual.chromosome_length)
    for i in range(no_of_genes_to_mutate):
        gene_to_mutate = np.random.randint(0, individual.chromosome_length - 1)
        if individual.chromosome[gene_to_mutate] == 1:
            individual.chromosome[gene_to_mutate] = 0
        else:
            individual.chromosome[gene_to_mutate] = 1
    return individual

