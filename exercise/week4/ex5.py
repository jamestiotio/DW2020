import random

def game(r, N):
    wins = 0
    for experiment in range(N):
        if sum([random.randint(1, 6) for die in range(4)]) < 9:
            wins += 1
    
    expected = (r * wins) - (1 * N)
    
    if expected > 0:
        return True
    
    return False