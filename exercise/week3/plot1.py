import matplotlib.pyplot as plt
import secrets


def random_walk(n):
    x = [0]
    y = [0]

    for _ in range(n):
        xrand = secrets.SystemRandom().uniform(-0.5, 0.5)
        yrand = secrets.SystemRandom().uniform(-0.5, 0.5)

        x.append(x[-1] + xrand)
        y.append(y[-1] + yrand)

    plt.scatter(x, y)
    plt.show()
