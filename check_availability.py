#!/usr/bin/python
import sys
import cookielib
import mechanize
import requests
from bs4 import BeautifulSoup


def enter_data():
    room = raw_input("Enter room code (example: LG25): ")
    room = "GLA." + room
    if type(room) == str:
        pass
    else:
        print("Not a string.)")
        sys.exit()

    week = raw_input("Enter week (1 - 52): ")
    if int(week) in range(1,53):
        pass
    else:
        print("Week not in range (1 - 52)")
        sys.exit()

    day = raw_input("Enter day (1[Mon] - 6[Sat]: ")
    if int(day) in range(1,7):
        pass
    else:
        print("Day not in range (1 - 6)")
        sys.exit()

    time = raw_input("Enter starting time (1 - 20): ")
    if int(time) in range(1,21):
        pass
    else:
        print("time not in range (1 - 20)")
        sys.exit()

    details = build_timetable(room, week, day, time)
    return details


def check_args(room, week, day, hour):
    if type(room) != str:
        print("First argument must be a string.")
        sys.exit()
    elif int(week) not in range(1,53):
        print("Second argument not in range")
        sys.exit()
    elif int(day) not in range(1,7):
        print("Third argument not in range")
        sys.exit()
    elif int(hour) not in range(1,21):
        print("Fourth argument not in range")
        sys.exit()


def build_timetable(room, week, day, hour):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)

    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)

    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    browser.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")]
    url = "https://www101.dcu.ie/timetables/feed.php?room=" + room + "&week1=" + week + "&hour=" + str(hour) + "&day=" + day + "&template=location"
    browser.open(url)

    return browser, url


def check_room(timetable_url):
    html = requests.get(timetable_url)
    soup = BeautifulSoup(html.text, "lxml")
    tr = soup.select('tr')

    return str(tr[12].getText().strip()) + " -> " + str(tr[14].getText().strip())


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("1 - 8:00, 2 - 8:30, 3 - 9:00, 4 - 9:30, 5 - 10:00,\n6 - 10:30, 7 - 11:00, 8 - 11:30, 9 - 12:00, 10 - 12:30,\n11 - 13:00, 12 - 13:30, 13 - 14:00, 14 - 14:30, 15 - 15:00,\n16 - 15:30, 17 - 16:00, 18 - 16:30, 19 - 17:00, 20 - 17:30\n")
        timetable, url = enter_data()
    elif len(args) < 3 and len(details) >= 0:
        print("Incorrect number of parameters.")
        sys.exit()
    else:
        check_args("GLA." + str(args[0]), args[1], args[2], args[3])
        timetable, url = build_timetable("GLA." + str(args[0]), args[1], args[2], args[3])

    print(timetable)
    confirmation = raw_input("\nIs this the correct input? (y/n): ")

    if confirmation.lower() == "y":
        status = check_room(url)
        if status == "":
            print("That room is free.")
        else:
            print(status)
    else:
        print("Action cancelled.")

if __name__ == '__main__':
    main()
