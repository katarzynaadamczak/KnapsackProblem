import numpy as np
import random as random
from Individual import Individual
from Population import Population

"""
init_population(n_items, size)
n_items - number of items from which the subset to be packed into the knapsack
is selected
size - population size

"""


def init_population(n_items, size) -> Population:
    population_size = (size, n_items)
    # print("Population size = {}".format(population_size))
    initial_population = np.random.random(size=population_size)
    for i in range(size):
        for j in range(n_items):
            if initial_population[i][j] > 0.15:
                initial_population[i][j] = 0
            else:
                initial_population[i][j] = 1
    # print(type(initial_population))
    # print("leci test")
    # print(initial_population)
    # print(len(initial_population))
    # print(sum(initial_population[0]))
    # print(initial_population)


    # initial_population_objects = []
    # for i in range(size):
    #   initial_population_objects.append(Individual(initial_population[i], n_items))

    initial_population_objects = [Individual(initial_population[i], n_items) for i in range(size)]

    # print(initial_population_objects[0].chromosome)

    return Population(initial_population_objects)
