class Line0:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __call__(self, x):
        m = (self.p1[1] - self.p2[1]) / (self.p1[0] - self.p2[0])
        c = self.p1[1] - (m * self.p1[0])
        y = (m * x) + c
        
        return y