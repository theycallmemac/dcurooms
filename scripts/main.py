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

__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
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

def get_data():
        times, c, g, details = {'0800': '1', '0830': '2', '0900': '3', '0930': '4', '1000': '5', '1030': '6', '1100': '7', '1130': '8', '1200': '9', '1230': '10', '1300': '11', '1330': '12', '1400': '13','1430': '14', '1500': '15', '1530': '16', '1600': '17', '1630': '18', '1700': '19', '1730': '20', '1800': '21', '1830': '22', '1900': '23', '1930': '24', '2000': '25', '2030': '26', '2100': '27', '2130': '28', '2200': '29', '2230': '30'}, ['LG25', 'LG26', 'LG27', 'L101', 'L114', 'L125', 'L128'], ['CG01', 'CG02', 'CG03', 'CG04', 'CG05', 'CG06', 'CG11', 'CG12', 'CG20', 'CG68', 'C166'], sys.argv[2:]
        return times, c, g, details

def required():
    parser = setup_options()
    (options, arguments) = parser.parse_args()
    times, c, g, details = get_data()
    return parser, (options, arguments), (c, g), (times, details)

def get_lab_credentials():
    email = input("Your gmail: ")
    password = input("Your gmail password: ")
    your_name = input("Your name: ")
    society = input("Society name: ")
    return email, password, your_name, society

def get_room_credentials():
    name = input("Your name: ")
    email = input("Your email: ")
    number = input("Your number: ")
    society = input("Society name: ")
    return email, number, name, society

def get_lst(c, g, options):
    if options.computing: lst = c
    elif options.grattan: lst = g
    return lst

def get_current_time(date):
    day = date.weekday()
    hour = date.hour
    minute = date.minute
    year, week_no, weekday = date.isocalendar()
    start = 36
    if week_no >= start:
        offset = -start
    else:
        offset = 52 - start
    week = week_no + offset - 1
    return str(week), str(day + 1), str(hour), str(minute)

def main():
    parser, (options, arguments), rooms, info = required()
    if options.book and info[1][0][0] == "L":
        email, password, your_name, society = get_lab_credentials()
        lab = LabBooking(email, password, your_name, society, info[1])
        emails, message = lab.draft()
        print(message)
        result = lab.send(emails[0], emails[1], message)
    elif options.book and info[1][0][0] == "C":
        email, number, name, society = get_room_credentials()
        room = RoomBooking(email, number, name, society, info[1])
        form = room.fill()
        result = room.submit(form)
    if options.lookup and (options.grattan or options.computing):
        lst = get_lst(rooms[0], rooms[1], options)
        week, day, hour = info[1]
        look = LookUp(week, day, hour)
        look.check_args()
        look.check_time(info[0])
        look.building_option(lst)
    elif options.lookup:
        room, week, day, hour = info[1]
        look = LookUp(week, day, hour)
        look.check_args()
        look.check_time(info[0])
        look.room_option(room)
    if options.now:
        week, day, hour, minute = get_current_time(datetime.datetime.now())
        now = Now(week, day, hour, minute)
        now.round_it()
        now.check_args()
        now.check_time(info[0])
        lst = get_lst(rooms[0], rooms[1], options)
        now.building_option(lst, options)
if __name__ == "__main__":
    main()
