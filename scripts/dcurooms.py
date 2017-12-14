#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sys
from optparse import OptionParser
from cookielib import LWPCookieJar
from mechanize import Browser, _http
from requests import get
from bs4 import BeautifulSoup

__author__ = "theycallmemac"
__version__ = '0.2.1'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'

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
    browser = Browser()
    cookie_jar = LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    browser.set_handle_refresh(_http.HTTPRefreshProcessor(), max_time=1)
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
    parser = OptionParser(description='Displays and books rooms around the DCU campus via provided timetable/module details', prog='dcurooms', version='%prog ' + __version__, usage='%prog [option]')
    parser.add_option("-f", "--free", action="store_true", help="returns only the rooms/labs that are free in a building")
    parser.add_option("-n", "--now", action="store_true", help="show the status of each room/lab as it is at the current time of checking")
    parser.add_option("-c", "--computing", action="store_true", help="displays the status of the labs in the School of Computing")
    parser.add_option("-g", "--grattan", action="store_true", help="displays the status of rooms in the Henry Grattan building")

    (options, arguments) = parser.parse_args()

    times = {'0800':'1', 
            '0830':'2', 
            '0900':'3',
            '0930':'4', 
            '1000':'5',
            '1030':'6',
            '1100':'7',
            '1130':'8', 
            '1200':'9', 
            '1230':'10',
            '1300':'11', 
            '1330':'12', 
            '1400':'13', 
            '1430':'14', 
            '1500':'15',
            '1530':'16', 
            '1600':'17', 
            '1630':'18', 
            '1700':'19', 
            '1730':'20', 
            '1800':'21', 
            '1830':'22', 
            '1900':'23', 
            '1930':'24',
            '2000':'25', 
            '2030':'26', 
            '2100':'27', 
            '2130':'28', 
            '2200':'29', 
            '2230':'30'}

    if options.now == True:
        c = ['LG25','LG26','LG27','L101','L114','L125','L128']
        g = ['CG01', 'CG02','CG03','CG04','CG05','CG06','CG11','CG12','CG20','CG68','C166']
        week, day, hour, minute = get_current_time(datetime.datetime.now())
        if int(hour) < 8 or int(hour) >= 23:
            print("Outside scheduled timetables. Try again at 08:00.")
            sys.exit()
        if int(minute) >= 30:
            minute = '30'
        else:
            minute = '00'
        current_time = hour + minute
        for k,v in times.items():
            if k == current_time:
                current_time = v
                break
            else:
                pass
        if options.computing == True:
            if options.free == True:
                for room in c:
                    timetable, url = build_timetable("GLA." + room, week, day, current_time)
                    status = check_room(url)
                    if len(status) <= 9:
                        print(room + ": " + status)
            else:
                for room in c:
                    timetable, url = build_timetable("GLA." + room, week, day, current_time)
                    status = check_room(url)
                    print(room + ": " + status)

        elif options.grattan == True:
            if options.free == True:
                for room in g:
                    timetable, url = build_timetable("GLA." + room, week, day, current_time)
                    status = check_room(url)
                    if len(status) <= 9:
                        print(room + ": " + status)       
            else:
                for room in g:
                    timetable, url = build_timetable("GLA." + room, week, day, current_time)
                    status = check_room(url)
                    print(room + ": " + status) 
        
        else:
            parser.print_help()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
