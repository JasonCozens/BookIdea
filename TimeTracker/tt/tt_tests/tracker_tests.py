import unittest
from tt.tracker import Tracker
from datetime import datetime


class NowMock:

    def now(self):
        return datetime(2016, 3, 9, 14, 38, 47)


class TrackerTest(unittest.TestCase):

    def test_init(self):
        tracker = Tracker()
        self.assertEqual(tracker.history, "")

    def test_start_time_is_now(self):
        tracker = Tracker(NowMock().now)
        tracker.start()
        self.assertEqual("(2016-03-09 14:38:47]", tracker.history)