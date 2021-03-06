import unittest
import sys
import datetime
import os
sys.path.append('.')


class AvailableNowTestCase(unittest.TestCase):
    def setUp(self):
        available_result = os.system(
            """python scripts/dcurooms -anC > tests/available_output.txt""")
        self.assertTrue(available_result == 0)

    def test_available_output(self):
        if self.setUp():
            with open('available_output.txt') as f:
                for line in f:
                    if len(line.strip()[14:]) > 0:
                        self.assertEqual("""Outside scheduled timetables.
                                         Try again at 08:00.""", line.strip())
                    else:
                        self.assertEqual("", line.strip()[14:])
            self.tearDown()

    def tearDown(self):
        del_result = os.system("""rm tests/*.txt""")
        self.assertTrue(del_result == 0)


if __name__ == '__main__':
    unittest.main()
