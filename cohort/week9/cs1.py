from libdw import sm

class CM(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        if state == 0:
            if inp == 50:
                return (1, (50, "--", 0))
            elif inp == 100:
                return (0, (0, "coke", 0))
            else:
                return (0, (0, "--", inp))
        elif state == 1:
            if inp == 50:
                return (0, (0, "coke", 0))
            elif inp == 100:
                return (0, (0, "coke", 50))
            else:
                return (1, (50, "--", inp))