from datetime import datetime

class Tracker:

    def __init__(self, now=datetime.now):
        self._now = now
        self._history = []

    @property
    def history(self):
        h = ""
        for task in self._history:
            h += "(" + task.strftime("%Y/%m/%d - %H:%M:%S") + "]"
        return h

    def start(self):
        self._history.append(self._now())

# datetime.datetime.strftime(now(), "%Y/%m/%d - %H:%M:%S")