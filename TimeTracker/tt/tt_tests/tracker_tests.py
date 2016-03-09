import unittest
from tt.tracker import Tracker
from datetime import datetime


class NowMock:

    def __init__(self, times=[]):
        self._times = times

    def now(self):
        return self._times.pop(0)


class TrackerTest(unittest.TestCase):

    def test_init(self):
        tracker = Tracker()
        self.assertEqual(tracker.history, "")

    def test_start_time_is_now(self):
        tracker = Tracker(NowMock([
            datetime(2016, 3, 9, 14, 38, 47),
        ]).now)
        tracker.start()
        self.assertEqual("(2016-03-09 14:38:47]", tracker.history)

    def test_start_stop(self):
        tracker = Tracker(NowMock([
            datetime(2016, 3, 9, 14, 38, 47),
            datetime(2016, 3, 9, 15, 50, 12),
        ]).now)
        tracker.start()
        tracker.stop()
        self.assertEqual(
            "(2016-03-09 14:38:47,2016-03-09 15:50:12)",
            tracker.history)

    def test_stop_before_start(self):
        tracker = Tracker(NowMock([
            datetime(2016, 3, 9, 14, 38, 47),
        ]).now)
        tracker.stop()
        self.assertEqual("", tracker.history)

    def test_duplicate_stops_are_ignored(self):
        tracker = Tracker(NowMock([
            datetime(2016, 3, 9, 14, 38, 47),
            datetime(2016, 3, 9, 15, 50, 12),
            datetime(2016, 3, 9, 16, 50, 10),
        ]).now)
        tracker.start()
        tracker.stop()
        tracker.stop()
        self.assertEqual(
            "(2016-03-09 14:38:47,2016-03-09 15:50:12)",
            tracker.history)
