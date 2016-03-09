from datetime import datetime


class Tracker:

    def __init__(self, now=datetime.now):
        self._now = now
        self._history = []

    @property
    def history(self):
        h = ""
        t = -1
        for t in range(len(self._history)):
            if Tracker.__is_start_time(t):
                h += "(" + str(self._history[t])
            else:
                h += "," + str(self._history[t]) + ")"
        if Tracker.__is_start_time(t):
            h += "]"
        return h

    def start(self):
        self._history.append(self._now())

    def stop(self):
        if len(self._history) == 0:
            return
        if Tracker.__is_start_time(len(self._history) - 1):
            self._history.append(self._now())

    @staticmethod
    def __is_start_time(t):
        return t % 2 == 0
