import sys
from mechanicalsoup import StatefulBrowser
from http.cookiejar import LWPCookieJar
from requests import get
from bs4 import BeautifulSoup

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
        if int(self.week) not in range(1, 53) or int(self.day) not in range(1, 7):
            print("Incorrect parameters passed.")
            sys.exit()
        else:
            pass

    def round_it(self):
        if int(self.hour) < 8 or int(self.hour) >= 23:
            print("Outside scheduled timetables. Try again at 08:00.")
            sys.exit()
        if int(self.minute) >= 30:
            self.minute = '30'
        else:
            self.minute = '00'

    def check_time(self, times):
        if self.hour not in times:
            print("Outside scheduled timetables. Please try again at 08:00.")
        for k, v in times.items():
            if k == self.hour + self.minute:
                self.hour = v
                break
            else:
                pass

    def get_status(self, options, room, status):
        if options.available:
            if len(status) <= 9:
                print(room + ": " + status)
        else:
            print(room + ": " + status)

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
        url = "https://www.dcu.ie/timetables/feed.php?room=GLA." + room + "&week1=" + self.week + "&hour=" + self.hour + "&day=" +  self.day  + "&template=location"
        browser.open(url)
        result = Now.check_room(self, url)
        return result

    def check_room(self, url):
        html = get(url)
        soup = BeautifulSoup(html.text, "lxml")
        tr = soup.select('tr')
        return str(tr[12].getText().strip()) + " -> " + str(tr[14].getText().strip())
