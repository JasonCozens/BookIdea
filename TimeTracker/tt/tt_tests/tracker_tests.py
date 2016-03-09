import unittest
from tt.tracker import Tracker


class TrackerTest(unittest.TestCase):

    def test_init(self):
        tracker = Tracker()
        self.assertEqual(tracker.history, "")

    def test_start_time_is_now(self):
        tracker = Tracker()
        tracker.start()
        self.assertEqual("(2016/03/09 - 14:38:47]", tracker.history)