import pandas as pd

"""
function 'read' takes a file name inCSV format on the input.
"""


def read(input_file):
    data = pd.read_csv(input_file)
    w_i = data["w_i"].values
    s_i = data["s_i"].values
    c_i = data["c_i"].values

    return Task
