import time

class StopWatch:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = -1

    def start(self):
        self.start_time = time.time()
        self.end_time = -1

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.end_time == -1:
            return None
        elif self.end_time - self.start_time < 0:
            return None
        else:
            return round(self.end_time - self.start_time, 1)