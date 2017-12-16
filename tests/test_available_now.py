

import unittest
import sys
import datetime
import os
sys.path.append('../')
from scripts.dcurooms import build_timetable, get_current_time, check_room, main

class AvailableNowTestCase(unittest.TestCase):
    def test_options(self):
        anc_result = os.system("cd ../scripts/ && python dcurooms.py -anc > ../tests/output.txt")
        return self.assertTrue(free_result == 0)

    def test_output(self):
        if self.test_options():
            with open('output.txt') as f:
                for line in f:
                    if len(line.strip()[14:]) > 0:
                        return self.assertEqual("Outside scheduled timetables. Try again at 08:00.", line.strip())
                    else:
                       return  self.assertEqual("", line.strip()[14:])


if __name__ == '__main__':
    unittest.main()

