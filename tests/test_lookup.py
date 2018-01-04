import unittest
import sys
import datetime
import os
sys.path.append('../')


class LookupTestCase(unittest.TestCase):
    def test_options(self):
        room_result = os.system("""cd scripts/ &&
                                python dcurooms.py -l CG12 21 1 1800
                                > ../tests/lookup_room_output.txt""")
        building_result = os.system("""cd scripts/ &&
                                    python dcurooms.py -lL 9 4 1500
                                    > ../tests/lookup_building_output.txt""")

        self.assertTrue(room_result == 0)
        self.assertTrue(building_result == 0)

    def test_lookup_output(self):
        if self.test_options():
            with open('lookup_room_output.txt') as f:
                for line in f:
                    if len(line.strip()[14:]) > 0:
                        self.assertEqual("""Outside scheduled timetables.
                                        Try again at 08:00.""", line.strip())
                    else:
                        self.assertEqual("", line.strip()[14:])

            with open('lookup_building_output.txt') as f: 
                for line in f:
                    if len(line.strip()[14:]) > 0:
                        self.assertEqual("""Outside scheduled timetables.
                                        Try again at 08:00.""", line.strip())
                    else:
                        self.assertEqual("", line.strip()[14:])

if __name__ == '__main__':
    unittest.main()

