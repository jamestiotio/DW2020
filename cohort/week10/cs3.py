import numpy as np

def normalize_minmax(data):
    if len(data.shape) != 2:
        return None

    for i in range(len(data[0])):
        maximum = np.max(data[:, i])
        minimum = np.min(data[:, i])
        data[:, i] = (data[:, i] - minimum) / (maximum - minimum)

    return data