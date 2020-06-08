import math

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __call__(self, x):
        return math.exp(- self.a * x) * math.sin(self.w * x)