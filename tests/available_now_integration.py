import unittest
import sys
import datetime
from scripts.utils import get_lst
from scripts.now import Now
from test_required import required
class AvailableNowIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        return required()

    def test_lab(self):
        parser, (options, arguments), rooms, info = self.setUp()
        (options, args) = parser.parse_args(["-L"])
        lst = get_lst(rooms[0], rooms[1], options)
        week, day, hour, minute = '2', '1', '14', '30'
        now = Now(week, day, hour, minute)
        now.check_args()
        now.check_time(info[0])

    def test_room(self):
        parser, (options, arguments), rooms, info = self.setUp()
        (options, args) = parser.parse_args(["-C"])
        lst = get_lst(rooms[0], rooms[1], options)
        week, day, hour, minute = '24', '2', '08', '00'
        now = Now(week, day, hour, minute)
        now.check_args()
        now.check_time(info[0])

    def test_incorrect_input(self):
        parser, (options, arguments), rooms, info = self.setUp()
        (options, args) = parser.parse_args(["-L"])
        lst = get_lst(rooms[0], rooms[1], options)
        week, day, hour, minute  = '60', '7', '23', '57'
        now = Now(week, day, hour, minute)
        try:
            now.check_args()
            now.check_time(info[0])
        except SystemExit:
            pass
if __name__ == '__main__':
    unittest.main()

