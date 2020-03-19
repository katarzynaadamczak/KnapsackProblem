import numpy as np


class Task:
    def __init__(self, data_w_i, data_s_i, data_c_i, data_n, data_w, data_s):
        self.w_i = np.array(data_w_i)
        self.s_i = np.array(data_s_i)
        self.c_i = np.array(data_c_i)
        self.n = data_n
        self.w = data_w
        self.s = data_s
