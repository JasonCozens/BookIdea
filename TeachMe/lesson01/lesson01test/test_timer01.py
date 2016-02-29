"""
This is the first run at a distributed timer application.
"""
import unittest
from datetime import datetime
from lesson01.timer01 import Timer01


class Timer01Fixture(unittest.TestCase):

    def test_start(self):
        timer = Timer01()
        before = datetime.now()
        timer.start()
        after = datetime.now()
        self.assertGreaterEqual(timer.last_start, before)
        self.assertLessEqual(timer.last_start, after)
