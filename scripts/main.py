#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import libraries
import sys
import datetime
from optparse import OptionParser
from lab_booking import LabBooking
from room_booking import RoomBooking
from lookup import LookUp
from now import Now
import utils
import opts

__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'


def setup_options():
    parser = OptionParser(
        description="\033[1;97m{0}\033[00m".format(
            'Displays info and books room around DCU.'),
        prog="\033[1;97m{0}\033[00m".format('dcurooms'),
        version='%prog ' + __version__,
        usage='%prog [' + '\033[1;92m{0}\033[00m'.format("option") + ']')
    parser.add_option(
        "-l",
        "--lookup",
        action="store_true",
        help="returns information given a specific room, week, day and hour")
    parser.add_option(
        "-b", "--book", action="store_true",
        help="books a room by providing the room, D/M/YYYY, start, and end")
    parser.add_option(
        "-a", "--available", action="store_true",
        help="returns only the rooms/labs that are free in a building")
    parser.add_option(
        "-n", "--now", action="store_true",
        help="show the status of each room/lab as it is currently")
    # building options which can be passed
    parser.add_option(
        "-L", "--computing", action="store_true",
        help="displays the status of the labs in the School of Computing")
    parser.add_option(
        "-C", "--grattan", action="store_true",
        help="displays the status of rooms in the Henry Grattan building")
    return parser


def get_data():
    times = {'0800': '1', '0830': '2', '0900': '3',
             '0930': '4', '1000': '5', '1030': '6',
             '1100': '7', '1130': '8', '1200': '9',
             '1230': '10', '1300': '11', '1330': '12',
             '1400': '13', '1430': '14', '1500': '15',
             '1530': '16', '1600': '17', '1630': '18',
             '1700': '19', '1730': '20', '1800': '21',
             '1830': '22', '1900': '23', '1930': '24',
             '2000': '25', '2030': '26', '2100': '27',
             '2130': '28', '2200': '29', '2230': '30'}
    c = ['LG25', 'LG26', 'LG27', 'L101', 'L114', 'L125', 'L128']
    g = ['CG01', 'CG02', 'CG03', 'CG04', 'CG05', 'CG06', 'CG11',
         'CG12', 'CG20', 'CG68', 'C166']
    details = sys.argv[2:]
    return times, c, g, details


def required():
    parser = setup_options()
    (options, arguments) = parser.parse_args()
    times, c, g, details = get_data()
    return parser, (options, arguments), (c, g), (times, details)


def booking(options, info):
    if options.book and info[1][0][0] == "L":
        opts.booking_lab(info)
    elif options.book and info[1][0][0] == "C":
        opts.booking_room(info)


def lookup(options, rooms, info):
    if options.lookup and (options.grattan or options.computing):
        opts.lookup_building(rooms, info, options)
    elif options.lookup:
        opts.lookup_room(info)


def now(options, rooms, info):
    opts.now(rooms, info, options)


def main():
    parser, (options, arguments), rooms, info = required()
    if options.book:
        booking(options, info)
    elif options.lookup:
        lookup(options, rooms, info)
    elif options.now:
        now(options, rooms, info)


if __name__ == "__main__":
    main()
