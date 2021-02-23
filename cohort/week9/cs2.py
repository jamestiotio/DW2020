from libdw import sm

class SimpleAccount(sm.SM):

    def __init__(self, balance):
        self.start_state = balance

    def get_next_values(self, state, inp):
        if state < 100:
            if inp < 0:
                return (state + inp - 5, state + inp - 5)

        return (state + inp, state + inp)