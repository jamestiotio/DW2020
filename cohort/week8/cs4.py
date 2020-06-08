import numpy as np

class Line:
    def __init__(self, c0=0, c1=0):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return float(self.c0 + self.c1 * x)

    def table(self, L, R, n):
        table_string = ""

        if L == R:
            n = 1

        for x in np.linspace(L, R, n):
            y = self.c0 + self.c1 * x
            table_string += "{:10.2f}{:10.2f}\n".format(x, y)

        if n == 0 or table_string == "" or L > R:
            return "Error in printing table"

        return table_string