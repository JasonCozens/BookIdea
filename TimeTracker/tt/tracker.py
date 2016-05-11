from datetime import datetime


class Tracker:

    def __init__(self, now=datetime.now):
        self._now = now
        self._history = []

    @property
    def history(self):
        h = ""
        for t in range(len(self._history)):
            next_time = str(self._history[t])
            if Tracker.__is_start_time(self._history[0:t + 1]):
                h += "(" + next_time
            else:
                h += "," + next_time + ")"
        if Tracker.__is_start_time(self._history):
            h += "]"
        return h

    def start(self):
        now = self._now()
        if Tracker.__is_start_time(self._history):
            self._history.append(now)
        self._history.append(now)

    def stop(self):
        if Tracker.__is_start_time(self._history):
            self._history.append(self._now())

    @staticmethod
    def __is_start_time(history):
        return len(history) % 2 == 1

if __name__ == "__main__":
    print("WELCOME TO TIME TRACKING")
    input("ARE YOU READY?")
