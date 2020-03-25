import numpy as np
from Task import Task


class Individual:
    def __init__(self, given_chromosome, given_chromosome_length):
        self.chromosome = np.array(given_chromosome)
        # print(type(chromosome))
        self.chromosome_length = given_chromosome_length

    def evaluate(self, task: Task):
        # print(self.chromosome, task.w_i, self.chromosome*task.w_i)
        # print(self.chromosome.shape, task.w_i.shape)
        test = np.multiply(self.chromosome, task.w_i)
        # print("max {}".format(max(test)))
        # print("min {}".format(min(test)))
        sum_w_i = np.sum(test)
        sum_s_i = np.sum(np.multiply(self.chromosome, task.s_i))
        sum_c_i = np.sum(np.multiply(self.chromosome, task.c_i))

        # print(sum_w_i, task.w)
        # print(sum_c_i)

        if sum_w_i < task.w and sum_s_i < task.s:
            return sum_c_i
        else:
            return 0

    def best_individual(self, task : Task):
        sum_c_i = np.sum(np.multiply(self.chromosome, task.c_i))
        return sum_c_i


