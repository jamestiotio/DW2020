import numpy as np
import matplotlib.pyplot as plt

mean_temperature = [24.8, 25.5, 26.5, 26.1, 26, 26.8, 26.9, 26.4, 27.2, 24.5, 23.9, 23.1, 23, 23.4,
                    25.2, 26.2, 27.2, 27.2, 26.9, 26.4, 27.2, 27.5, 26.8, 26.7, 26.6, 26.4, 27.1, 26.3, 27.7, 26.9, 27.3]

# Question 1
plt.boxplot(mean_temperature)
plt.show()

# Question 2
in_between = sum(27 < t < 28 for t in mean_temperature)
not_in_between = len([t for t in mean_temperature if not (27 < t < 28)])

x = np.arange(2)
y = np.array([in_between, not_in_between])
xticklabels = ["between 27 and 28", "not between 27 and 28"]

plt.bar(x, y, tick_label=xticklabels)
plt.show()
