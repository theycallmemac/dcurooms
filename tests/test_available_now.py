import unittest
import sys
import datetime
import os
sys.path.append('.')


class AvailableNowTestCase(unittest.TestCase):
    def test_options(self):
        available_result = os.system("""cd scripts/ && python dcurooms -anC
                                     > ../tests/available_output.txt""")
        self.assertTrue(available_result == 0)

    def test_available_output(self):
        if self.test_options():
            with open('available_output.txt') as f:
                for line in f:
                    if len(line.strip()[14:]) > 0:
                        self.assertEqual("""Outside scheduled timetables.
                                         Try again at 08:00.""", line.strip())
                    else:
                        self.assertEqual("", line.strip()[14:])


if __name__ == '__main__':
    unittest.main()

