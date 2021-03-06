import sys
from mechanicalsoup import StatefulBrowser
from requests import get
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import utils

if sys.version_info[0] < 3:
    from cookielib import LWPCookieJar
else:
    from http.cookiejar import LWPCookieJar


__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'


class Now(object):
    week = ""
    day = ""
    hour = ""
    minute = ""

    def __init__(self, week, day, hour, minute):
        self.week = week
        self.day = day
        self.hour = hour
        self.minute = minute

    def check_args(self):
        if int(
                self.week) not in range(
                1,
                53) or int(
                self.day) not in range(
                    1,
                7):
            print("\033[1;91m{0}\033[00m".format(
                "Incorrect parameters passed."))
            sys.exit()
        else:
            pass

    def round_it(self):
        if int(self.hour) < 8 or int(self.hour) >= 23:
            print("\033[1;93m{0}\033[00m".format(
                "Outside scheduled timetables. Try again at 08:00."))
            sys.exit()
        if int(self.minute) >= 30:
            self.minute = '30'
        else:
            self.minute = '00'

    def check_time(self, times):
        time = "0" + self.hour + self.minute
        if time not in times:
            print("\033[1;93m{0}\033[00m".format(
                "Outside scheduled timetables. Please try again at 08:00."))
            sys.exit()
        for k, v in times.items():
            if k == time:
                self.hour = v
                break
            else:
                pass
        return self.hour

    def get_status(self, options, room, status):
        if options.available:
            if len(status) <= 9:
                print("\033[1;92m{0}\033[00m".format(room) +
                      ": " + "\033[1;97m{0}\033[00m".format(status))
        elif len(status) > 9:
            print("\033[1;91m{0}\033[00m".format(room) +
                  ": " + "\033[1;90m{0}\033[00m".format(status))
        else:
            print("\033[1;92m{0}\033[00m".format(room) +
                  ": " + "\033[1;97m{0}\033[00m".format(status))

    def building_option(self, lst, options):
        for room in lst:
            status = Now.build_timetable(self, room)
            Now.get_status(self, options, room, status)

    def build_timetable(self, room):
        browser = StatefulBrowser()
        cookie_jar = LWPCookieJar()
        browser.set_cookiejar(cookie_jar)
        browser.user_agent = [
            ("User-Agent",
             """Mozilla/5.0 (Windows NT 10.0; Win64; x64)
             AppleWebKit/537.36 (KHTML, like Gecko)
             Chrome/58.0.3029.110
             Safari/537.36""")]
        url = "http://www101.dcu.ie/timetables/feed.php?room=GLA." + room + "&week1=" + \
            self.week + "&hour=" + self.hour + "&day=" + self.day + "&template=location"
        browser.open(url, verify=False)
        result = utils.check_room(url)
        return result
