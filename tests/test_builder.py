
import unittest
import sys
import requests
sys.path.append('.')
from scripts.dcurooms import build_timetable
class BuildTimetableTestCase(unittest.TestCase):
    def test_return_val(self):
        val = build_timetable("CG04", "24", "14", "4")
        self.assertEqual(type(val), tuple)

    def test_url_builder(self):
        tt, url = build_timetable("LG26", "4", "10", "1")
        info = requests.get(url)
        self.assertTrue('200', info.status_code)

if __name__ == '__main__':
    unittest.main()

