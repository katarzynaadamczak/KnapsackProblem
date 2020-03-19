import numpy as np
from random import randrange
import pandas as pd

"""
generate(n, w, s, output_file)
n - number of objects to choose (int)
w - maximum carrying capacity of the knapsack (int)
s - maximum knapsack size (int)
output_file - name of the file into which the task is to be saved

"""


def generate(n, w, s, output_file):
    assert 1000 < n < 2000, "n out of range (1000,2000)"
    assert 10000 < w < 20000, "w out of range (10000,20000)"
    assert 10000 < s < 20000, "s out of range (10000,20000)"

    w_i = np.zeros(n+1)
    s_i = np.zeros(n+1)
    c_i = np.zeros(n+1)

    w_i[0] = n
    s_i[0] = w
    c_i[0] = s

    w_i_min = 1
    s_i_min = 1
    c_i_min = 1
    w_i_max = np.ceil(10 * w / n)
    s_i_max = np.ceil(10 * s / n)
    c_i_max = n
    sum_w_i_min = 2 * w
    sum_s_i_min = 2 * s

    for i in range(1, n+1):
        w_i[i] = randrange(w_i_min, w_i_max)
        s_i[i] = randrange(s_i_min, s_i_max)
        c_i[i] = randrange(c_i_min, c_i_max)

    while sum(w_i) < sum_w_i_min:
        w_i = w_i * 2

    while sum(s_i) < sum_s_i_min:
        s_i = s_i * 2


    df = pd.DataFrame({"w_i": w_i, "s_i": s_i, "c_i": c_i})
    df.to_csv(output_file, index=False)

    print("Function 'generate' executed.")
