import numpy as np

def five_number_summary(x):
    if len(x.shape) != 2:
        return None

    result = []
    for i in range(len(x[0])):
        result.append({'minimum': np.min(x[:, [i]]), 'first quartile': np.percentile(x[:, [i]], 25), 'median': np.median(x[:, [i]]), 'third quartile': np.percentile(x[:, [i]], 75), 'maximum': np.max(x[:, [i]])})

    return result