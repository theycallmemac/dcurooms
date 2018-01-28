import unittest
import sys
import datetime
from scripts.utils import get_lst
from scripts.lookup import LookUp
from test_required import required
class LookupBuildingIntegrationTestCase(unittest.TestCase):
    def test_lab_lookups(self):
        parser, (options, arguments), rooms, info = required()
        (options, args) = parser.parse_args(["-L"])
        lst = get_lst(rooms[0], rooms[1], options)
        week, day, hour = '4', '5', '1600'
        look = LookUp(week, day, hour)
        look.check_args()
        look.check_time(info[0])

    def test_room_lookups(self):
        parser, (options, arguments), rooms, info = required()
        (options, args) = parser.parse_args(["-C"])
        lst = get_lst(rooms[0], rooms[1], options)
        week, day, hour = '9', '2', '0930'
        look = LookUp(week, day, hour)
        look.check_args()
        look.check_time(info[0])


    def test_incorrect_lookups(self):
        parser, (options, arguments), rooms, info = required()
        try:
            assert not isinstance(rooms, basestring) and not isinstance(info, basestring)
        except TypeError:
            print("Type error has occured")
            sys.exit(1)
        (options, args) = parser.parse_args(["-L"])
        lst = get_lst(rooms[0], rooms[1], options)
        week, day, hour = '53', '7', '1600'
        look = LookUp(week, day, hour)
        try:
            look.check_args()
            look.check_time(info[0])
        except SystemExit:
            pass

if __name__ == '__main__':
    unittest.main()

