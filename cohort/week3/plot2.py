import numpy as np
import matplotlib.pyplot as plt

daily_total_rainfall = [0.2, 7.8, 0.4, 3.4, 0.4, 3.8, 12, 5.4, 1.6, 0, 0.8, 12.4,
                        2.4, 2, 4.6, 0.8, 18.4, 7.4, 20.6, 4, 13.2, 2, 4, 0, 4.8, 14.4, 9.6, 0, 5.6, 7.6]

# Task 1
plt.hist(daily_total_rainfall, bins=5)
plt.show()

# Task 2
plt.hist(daily_total_rainfall, bins=[0, 4, 8, 12, 16, 20, 24])
plt.show()

# Task 3
plt.boxplot(daily_total_rainfall)
plt.show()

# Task 4
dry_days = sum(x == 0 for x in daily_total_rainfall)
rainy_days = len([x for x in daily_total_rainfall if x != 0])

x = np.arange(2)
y = np.array([dry_days, rainy_days])
xticklabels = ["dry days", "rainy days"]

plt.bar(x, y, tick_label=xticklabels)
plt.show()