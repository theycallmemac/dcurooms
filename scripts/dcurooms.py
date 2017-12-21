#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sys
if sys.version_info[0] < 3:
    from cookielib import LWPCookieJar
else:
    from http.cookiejar import LWPCookieJar
from optparse import OptionParser
from mechanicalsoup import StatefulBrowser
from requests import get
from bs4 import BeautifulSoup

__author__ = "theycallmemac"
__version__ = '0.4.2'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'

def setup_options():
    parser = OptionParser(description='Displays and books rooms around the DCU campus via provided timetable/module details', prog='dcurooms', version='%prog ' + __version__, usage='%prog [option]')
    parser.add_option("-a", "--available", action="store_true", help="returns only the rooms/labs that are free in a building")
    parser.add_option("-l", "--lookup", action="store_true", help="returns information given a specific room, week, day and hour")
    parser.add_option("-n", "--now", action="store_true", help="show the status of each room/lab as it is at the current time of checking")
    parser.add_option("-c", "--computing", action="store_true", help="displays the status of the labs in the School of Computing")
    parser.add_option("-g", "--grattan", action="store_true", help="displays the status of rooms in the Henry Grattan building")
    return parser

def check_arguments(week, day):
    if int(week) not in range(1, 53) or int(day) not in range(1,7):
        print("Incorrect parameters passed.")
        sys.exit()
    else:
        pass

def search_dictionary(times, time):
    if time not in times:
        print("Outside scheduled timetables. Please try again at 08:00.")
        sys.exit()
    for k,v in times.items():
        if k == time:
            time = v
            break
        else:
            pass
    return time

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

def build_timetable(room, week, day, hour):
    browser = StatefulBrowser()
    cookie_jar = LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    browser.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")]
    url = "https://www101.dcu.ie/timetables/feed.php?room=" + room + "&week1=" + week + "&hour=" + str(hour) + "&day=" + day + "&template=location"
    browser.open(url)
    return browser, url

def check_room(timetable_url):
    html = get(timetable_url)
    soup = BeautifulSoup(html.text, "lxml")
    tr = soup.select('tr')
    return str(tr[12].getText().strip()) + " -> " + str(tr[14].getText().strip())

def main():
    parser = setup_options()
    (options, arguments) = parser.parse_args()
    times = {'0800':'1', '0830':'2', '0900':'3', '0930':'4', '1000':'5', '1030':'6', '1100':'7', '1130':'8', '1200':'9', '1230':'10',
            '1300':'11', '1330':'12', '1400':'13', '1430':'14', '1500':'15', '1530':'16', '1600':'17', '1630':'18', '1700':'19', '1730':'20',
            '1800':'21', '1830':'22', '1900':'23', '1930':'24', '2000':'25', '2030':'26', '2100':'27', '2130':'28', '2200':'29', '2230':'30'
            }
    c = ['LG25','LG26','LG27','L101','L114','L125','L128']
    g = ['CG01', 'CG02','CG03','CG04','CG05','CG06','CG11','CG12','CG20','CG68','C166']
    details = sys.argv[2:]
    if len(details) > 5:
        print("Too many arguments passed.")
        sys.exit()
    elif options.lookup == True:
        if options.computing == True:
            lst = c
        elif options.grattan == True:
            lst = g
        else:
            if len(details) <= 3:
                print("Not enough arguments passed.")
                sys.exit()
            room, week, day, time = details[0], details[1], details[2], details[3]
            if room not in c and room not in g:
                print("That room does not exist or is not supported by this program.")
                sys.exit()
            check_arguments(week, day)
            time = search_dictionary(times, time)
            timetable, url = build_timetable("GLA." + room, week, day, time)
            status = check_room(url)
            print(room + ": " + status)
            sys.exit()
        week, day, time = details[0], details[1], details[2]
        check_arguments(week, day)
        time = search_dictionary(times, time)
        for room in lst:
            timetable, url = build_timetable("GLA." + room, week, day, time)
            status = check_room(url)
            if options.available == True:
                if len(status) <= 9:
                    print(room + ": " + status)
            else:
                print(room + ": " + status)
        sys.exit()
    elif options.now == True:
        week, day, hour, minute = get_current_time(datetime.datetime.now())
        if int(hour) < 8 or int(hour) >= 23:
            print("Outside scheduled timetables. Try again at 08:00.")
            sys.exit()
        if int(minute) >= 30:
            minute = '30'
        else:
            minute = '00'
        check_arguments(week, day)
        time = search_dictionary(times, hour + minute)
        if options.computing == True:
            lst = c
        elif options.grattan == True:
            lst = g
        for room in lst:
            timetable, url = build_timetable("GLA." + room, week, day, time)
            status = check_room(url)
            if options.available == True:
                if len(status) <= 9:
                    print(room + ": " + status)
            else:
                print(room + ": " + status)
    else:
        parser.print_help()
if __name__ == '__main__':
    main()
