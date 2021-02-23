import numpy as np
import matplotlib.pyplot as plt


def logistic(x):
    return 1 / (1 + np.exp(-x))


x_values = np.linspace(-5, 5, 11)

plt.plot(x_values, logistic(x_values), marker="o")
plt.title("Logistic Function")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()