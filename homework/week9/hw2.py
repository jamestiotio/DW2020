from libdw import sm

class FirstWordSM(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        if state == 0:
            if inp == " " or inp == "\n":
                return (0, None)
            
            return (1, inp)
        
        elif state == 1:
            if inp == " ":
                return (2, None)
            
            return (1, inp)
        
        elif state == 2:
            if inp == "\n":
                return (0, None)
            
            return (2, None)