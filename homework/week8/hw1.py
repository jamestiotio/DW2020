class Time:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_time(self):
        return (self._hours * 3600) + (self._minutes * 60) + (self._seconds)

    def set_time(self, seconds):
        seconds %= 86400
        self._hours = seconds // 3600
        self._minutes = (seconds - (seconds // 3600) * 3600) // 60
        self._seconds = seconds - ((seconds // 3600) * 3600) - ((seconds - (seconds // 3600) * 3600) // 60) * 60

    def __str__(self):
        return f"Time: {self._hours}:{self._minutes}:{self._seconds}"

    elapsed_time = property(get_time, set_time)