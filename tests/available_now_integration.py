import unittest
import sys
import datetime
from scripts import utils
from scripts import now
from test_required import required

class AvailableNowIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        return required()

    def test_lab(self):
        parser, (options, arguments), rooms, info = self.setUp()
        (options, args) = parser.parse_args(["-L"])
        lst = utils.get_lst(rooms[0], rooms[1], options)
        week, day, hour, minute = '2', '1', '14', '30'
        now_obj = now.Now(week, day, hour, minute)
        utils.check_args(week, day)
        now_obj.check_time(info[0])

    def test_room(self):
        parser, (options, arguments), rooms, info = self.setUp()
        (options, args) = parser.parse_args(["-C"])
        lst = utils.get_lst(rooms[0], rooms[1], options)
        week, day, hour, minute = '24', '2', '08', '00'
        now_obj = now.Now(week, day, hour, minute)
        utils.check_args(week, day)
        now_obj.check_time(info[0])

    def test_incorrect_input(self):
        parser, (options, arguments), rooms, info = self.setUp()
        (options, args) = parser.parse_args(["-L"])
        lst = utils.get_lst(rooms[0], rooms[1], options)
        week, day, hour, minute  = '60', '7', '23', '57'
        now_obj = now.Now(week, day, hour, minute)
        try:
            utils.check_args(week, day)
        except SystemExit:
            pass
if __name__ == '__main__':
    unittest.main()

