import numpy as np
import random
from Individual import Individual

def crossover(parent1 : Individual, parent2 : Individual, crossover_rate):
    rand = np.random.uniform(0,1)
    cutting_point = int(parent1.chromosome_length/2)
    # print(rand)
    # print(parent1.chromosome, parent2.chromosome)
    # print(parent1.chromosome[0:cutting_point], parent2.chromosome[cutting_point:parent2.chromosome_length])
    if rand <= crossover_rate:
        offspring_arr = []
        offspring_arr = np.append(parent1.chromosome[0:cutting_point], parent2.chromosome[cutting_point:parent2.chromosome_length])
        offspring = Individual(offspring_arr, parent2.chromosome_length)
        return offspring
    return parent1






