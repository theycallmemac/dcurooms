import unittest
import sys
import datetime
import os
sys.path.append('.')
from scripts.utils import get_current_time
class RequiredTestCase(unittest.TestCase):
    def test_time(self):
        now = get_current_time(datetime.datetime.now())
        hr = int(now[2]) + 2
        mn = int(now[3])
        hr_d = datetime.datetime.now().hour
        mn_d = datetime.datetime.now().minute
        self.assertTrue(hr == hr_d and mn == mn_d)
if __name__ == '__main__':
    unittest.main()

