from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world


class MySMClass(sm.SM):
    start_state = None

    def get_next_values(self, state, inp):
        ground = inp.prox_ground.delta
        left = ground[0]
        right = ground[1]
        print(left, right)
        next_state = state
        return next_state, io.Action(fv=0.1, rv=-0.1)

MySM = MySMClass()

############################

m = ThymioSMSim(MySM, thymio_world, scale=2)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()