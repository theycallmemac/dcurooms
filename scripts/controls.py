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
sys.path.append('.')
from builders import *
from checks import *
if sys.version_info[0] < 3:
    from cookielib import LWPCookieJar
else:
    from http.cookiejar import LWPCookieJar

__author__ = "theycallmemac"
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'

def booking_control(c, g, details):
    if details[0] in c:
        user, password, from_who, to_who, message = draft_email(
                details)
        conf = get_confirmation()
        if conf == "y":
            send_email(user, password, from_who, to_who, message)
        else:
            print("Draft withdrawn.")
            sys.exit()

    elif details[0] in g:
        form = fill_form(details)
        if sys.version_info[0] < 3:
            conf = raw_input(
                "\nIs this the correct information? (y/n): ").lower()
        else:
            conf = input(
                "\nIs this the correct information? (y/n): ").lower()
        if conf == "y":
            room_booked = make_booking(form)
            print(room_booked)
        else:
            print("Form submission withdrawn.")
            sys.exit()
    else:
        print("That room is not supported by this tool.")
        sys.exit()

def lookup_room_control(g, c, details, times):
    if len(details) <= 3:
        print("Not enough arguments passed.")
        sys.exit()
    room, week = details[0], details[1]
    day, time = details[2], details[3]
    if room not in g and room not in c:
        print("That room is not supported by this program.")
        sys.exit()
    check_arguments(week, day)
    time = search_dictionary(times, time)
    timetable, url = build_timetable("GLA." + room, week, day, time)
    status = check_room(url)
    print(room + ": " + status)
    sys.exit()

def lookup_building_control(options, lst, details, times):
    week, day, time = details[0], details[1], details[2]
    check_arguments(week, day)
    time = search_dictionary(times, time)
    for room in lst:
        timetable, url = build_timetable("GLA." + room, week, day, time)
        status = check_room(url)
        if options.available:
            if len(status) <= 9:
                print(room + ": " + status)
        else:
            print(room + ": " + status)
    sys.exit()

def available_now_control(options, lst, times):
    week, day, hour, minute = get_current_time(datetime.datetime.now())

    if int(hour) < 8 or int(hour) >= 23:
        print("Outside scheduled timetables. Try again at 08:00.")
        sys.exit()
    if int(minute) >= 30:
        minute = '30'
    else:
        minute = '00'
    check_arguments(int(week), int(day))
    time = search_dictionary(times, hour + minute)
    for room in lst:
        timetable, url = build_timetable("GLA." + room, week, day, time)
        status = check_room(url)
        if options.available:
            if len(status) <= 9:
                print(room + ": " + status)
        else:
            print(room + ": " + status)
    sys.exit()


