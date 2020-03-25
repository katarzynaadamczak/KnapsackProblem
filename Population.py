import numpy as np
from random import randint
from Task import Task


class Population:
    def __init__(self, ind_array: list):
        self.array_of_individuals = np.array(ind_array)

    def tournament(self, tournament_size, task: Task):
        temp_array = np.copy(self.array_of_individuals)
        tournament_arr = []                         #array of Individuals
        for i in range(tournament_size):
            tmp = randint(0, self.array_of_individuals.shape[0] - 1 - i)
            tournament_arr.append(temp_array[tmp])
            temp_array = np.delete(temp_array, tmp)

        # for i in tournament_arr:
        #     print(i.chromosome)
        # print(temp_array.shape)
        # print(tournament_arr[0].chromosome)
        bests = []

        for ind in tournament_arr:
            bests.append(ind.evaluate(task))

        best_index = (bests.index(max(bests)))
        return tournament_arr[best_index]

