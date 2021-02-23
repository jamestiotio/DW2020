import numpy as np
import matplotlib.pyplot as plt


def sine_wave(t):
    return 2 * np.sin(3 * t)


t_values = np.linspace(0, 2 * np.pi, 150)

plt.plot(t_values, sine_wave(t_values), marker="o")
plt.show()