def move_disks(n, from_tower, to_tower, aux_tower, sol):
    if n >= 1:
        move_disks(n-1, from_tower, aux_tower, to_tower, sol)
        sol.append("Move disk " + str(n) + " from " + str(from_tower) + " to " + str(to_tower))
        move_disks(n-1, aux_tower, to_tower, from_tower, sol)

    return sol