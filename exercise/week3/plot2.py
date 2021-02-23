import matplotlib.pyplot as plt
import itertools
import secrets

x1 = [0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
y1 = [0, -2.0, 2.5, -1.0, 1.0, 3.0, 2.0]

path_coords = list(secrets.choice(
    list(itertools.permutations(list(zip(x1, y1))))))

x_coords = list(map(list, zip(*path_coords)))[0]
y_coords = list(map(list, zip(*path_coords)))[1]

x = list(itertools.chain([0], x_coords, [0]))
y = list(itertools.chain([0], y_coords, [0]))

plt.plot(x, y, marker="o")
plt.show()