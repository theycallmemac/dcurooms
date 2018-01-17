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
from scripts import builders
from scripts import checks
if sys.version_info[0] < 3:
    from cookielib import LWPCookieJar
else:
    from http.cookiejar import LWPCookieJar

__author__ = "theycallmemac"
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'

def get_statuses(status, options, room):
    if options.available:
        if len(status) <= 9: 
            print(room + ": " + status)
    else:
        print(room + ": " + status)
        
def run_loop(lst, options, details):
    week, day, time = details[0:3]
    for room in lst:
        timetable, url = builders.build_timetable("GLA." + room, week, day, time)
        status = checks.check_room(url)
        get_statuses(status, options, room)

def book_grattan(details):
    form = builders.fill_form(details)
    conf = checks.get_confirmation()
    if conf == "y":
        room_booked = builders.make_booking(form)
        print(room_booked)
    else:
        print("Form submission withdrawn.")
    sys.exit()
        
def book_computing(details):
    creds = []
    user, password, from_who, to_who, message = builders.draft_email(details)
    creds = [user, password]
    conf = checks.get_confirmation()
    if conf == "y":
        builders.send_email(creds, from_who, to_who, message)
    else:
        print("Draft withdrawn.")
    sys.exit()

def booking_control(c, g, details):
    if details[0] in c:
        book_computing(details)
    elif details[0] in g:
        book_grattan(details)
    else:
        print("That room is not supported by this tool.")
        sys.exit()

def lookup_room_control(g, c, details, times):
    if len(details) <= 3:
        print("Not enough arguments passed.")
        sys.exit()
    room, week = details[0:2]
    day, time = details[2:4]
    if room not in g and room not in c:
        print("That room is not supported by this program.")
        sys.exit()
    checks.check_arguments(week, day)
    time = checks.search_dictionary(times, time)
    timetable, url = builders.build_timetable("GLA." + room, week, day, time)
    status = checks.check_room(url)
    print(room + ": " + status)
    sys.exit()

def lookup_building_control(options, lst, details, times):
    week, day, time = details[0:3]
    checks.check_arguments(week, day)
    time = checks.search_dictionary(times, time)
    details =[week, day, time]
    run_loop(lst, options, details)
    sys.exit()

def available_now_control(options, lst, times):
    week, day, hour, minute = checks.get_current_time(datetime.datetime.now())
    if int(hour) < 8 or int(hour) >= 23:
        print("Outside scheduled timetables. Try again at 08:00.")
        sys.exit()
    if int(minute) >= 30:
        minute = '30'
    else:
        minute = '00'
    checks.check_arguments(int(week), int(day))
    time = checks.search_dictionary(times, hour + minute)
    details = [week, day, time]    
    run_loop(lst, options, details)    
    sys.exit()


