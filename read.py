import pandas as pd
import numpy as np
from Task import Task

"""
function 'read' takes a file name inCSV format on the input.
"""


def read(input_file):
    data = pd.read_csv(input_file)
    w_i = data["w_i"].values
    s_i = data["s_i"].values
    c_i = data["c_i"].values

    n = w_i[0]
    w = s_i[0]
    s = c_i[0]

    w_i_del = np.delete(w_i, 0)
    s_i_del = np.delete(s_i, 0)
    c_i_del = np.delete(c_i, 0)

    print("Function 'read' executed.")

    return Task(w_i_del, s_i_del, c_i_del, n, w, s)




