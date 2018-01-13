#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import libraries
import sys
import datetime
import smtplib
from optparse import OptionParser
from mechanicalsoup import StatefulBrowser
from requests import get
from bs4 import BeautifulSoup
sys.path.append(".")
from scripts import controls
if sys.version_info[0] < 3:
    from cookielib import LWPCookieJar
else:
    from http.cookiejar import LWPCookieJar

__author__ = "theycallmemac"
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'


def setup_options():
    parser = OptionParser(
        description='Displays info and books room around DCU.',
        prog='dcurooms', version='%prog ' + __version__,
        usage='%prog [option]')
    parser.add_option(
        "-l", "--lookup", action="store_true",
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

def main():
    parser = setup_options()
    (options, arguments) = parser.parse_args()
    times, c, g, details = {'0800': '1', '0830': '2', '0900': '3', '0930': '4', '1000': '5', '1030': '6', '1100': '7', '1130': '8', '1200': '9', '1230': '10', '1300': '11', '1330': '12', '1400': '13','1430': '14', '1500': '15', '1530': '16', '1600': '17', '1630': '18', '1700': '19', '1730': '20', '1800': '21', '1830': '22', '1900': '23', '1930': '24', '2000': '25', '2030': '26', '2100': '27', '2130': '28', '2200': '29', '2230': '30'}, ['LG25', 'LG26', 'LG27', 'L101', 'L114', 'L125', 'L128'], ['CG01', 'CG02', 'CG03', 'CG04', 'CG05', 'CG06', 'CG11', 'CG12', 'CG20', 'CG68', 'C166'], sys.argv[2:]
    if options.book:
        print("Booking requires more arguments. See the help for details.") if len(details) < 4 else controls.booking_control(c, g, details)
        sys.exit()
    elif len(details) > 5:    
        print("Too many arguments passed.") 
    elif options.lookup:
        if options.computing: lst = c
        elif options.grattan: lst = g
        else:
            controls.lookup_room_control(g, c, details, times)
        controls.lookup_building_control(options, lst, details, times)
    elif options.now:
        if options.computing: lst = c
        elif options.grattan: lst = g
        controls.available_now_control(options, lst, times) 
    else:
        parser.print_help()
if __name__ == '__main__':
    main()

