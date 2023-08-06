import unittest
import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now, you can import the function from time_utils
from time_utils import round_up_to_nearest_quarter, minutes_to_hhmm

class TestRoundUpToNearestQuarter(unittest.TestCase):

    def test_rounding(self):
        # Test für exakte Viertelstunden
        self.assertEqual(round_up_to_nearest_quarter(0), 0)
        self.assertEqual(round_up_to_nearest_quarter(15), 15)
        self.assertEqual(round_up_to_nearest_quarter(30), 30)
        self.assertEqual(round_up_to_nearest_quarter(45), 45)

        # Test für Zeiten, die aufgerundet werden sollten
        self.assertEqual(round_up_to_nearest_quarter(1), 15)
        self.assertEqual(round_up_to_nearest_quarter(16), 30)
        self.assertEqual(round_up_to_nearest_quarter(31), 45)
        self.assertEqual(round_up_to_nearest_quarter(46), 60)

        # Test für größere Werte
        self.assertEqual(round_up_to_nearest_quarter(75), 75)
        self.assertEqual(round_up_to_nearest_quarter(76), 90)

    def test_minutes_to_hhmm(self):
        # Test for minutes_to_hhmm function
        self.assertEqual(minutes_to_hhmm(0), "00:00")
        self.assertEqual(minutes_to_hhmm(30), "00:30")
        self.assertEqual(minutes_to_hhmm(60), "01:00")
        self.assertEqual(minutes_to_hhmm(90), "01:30")
        self.assertEqual(minutes_to_hhmm(123), "02:03")
        self.assertEqual(minutes_to_hhmm(999), "16:39")
        self.assertEqual(minutes_to_hhmm(1439), "23:59")

if __name__ == "__main__":
    unittest.main()
