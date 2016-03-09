import unittest
from tt.tracker import Tracker


class TrackerTest(unittest.TestCase):

    def test_init(self):
        tracker = Tracker()
        self.assertEqual(tracker.history, "")
