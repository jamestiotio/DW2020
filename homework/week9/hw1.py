from libdw import sm

class CommentsSM(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        if state == 0:
            if inp == "#":
                return (1, inp)
            
            return (0, None)
        
        elif state == 1:
            if inp == "\n":
                return (0, None)
            
            return (1, inp)