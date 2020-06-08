class Diff:
    def __init__(self, f, h=1e-4):
        self.f = f
        self.h = h
        
    def __call__(self, x):
        return (self.f(x + self.h) - self.f(x)) / self.h