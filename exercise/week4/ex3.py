import random

def throw_dice(n, nExp):
    sixes = 0
    for experiment in range(nExp):
        for die in range(n):
            if random.randint(1, 6) == 6:
                sixes += 1
                break

    return round(sixes / nExp, 2)