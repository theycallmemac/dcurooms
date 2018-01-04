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
        prog='dcurooms',
        version='%prog ' + __version__,
        usage='%prog [option]')
    parser.add_option(
        "-l",
        "--lookup",
        action="store_true",
        help="returns information given a specific room, week, day and hour")
    parser.add_option(
        "-b",
        "--book",
        action="store_true",
        help="books a room by providing the room, D/M/YYYY, start, and end")
    parser.add_option(
        "-a",
        "--available",
        action="store_true",
        help="returns only the rooms/labs that are free in a building")
    parser.add_option(
        "-n",
        "--now",
        action="store_true",
        help="show the status of each room/lab as it is currently")
    # building options which can be passed
    parser.add_option(
        "-L",
        "--computing",
        action="store_true",
        help="displays the status of the labs in the School of Computing")
    parser.add_option(
        "-C",
        "--grattan",
        action="store_true",
        help="displays the status of rooms in the Henry Grattan building")
    return parser


def check_arguments(week, day):
    if int(week) not in range(1, 53) or int(day) not in range(1, 7):
        print("Incorrect parameters passed.")
        sys.exit()
    else:
        pass


def search_dictionary(times, time):
    if time not in times:
        print("Outside scheduled timetables. Please try again at 08:00.")
        sys.exit()
    for k, v in times.items():
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
    browser.user_agent = [
        ("User-Agent",
         """Mozilla/5.0 (Windows NT 10.0; Win64; x64)
         AppleWebKit/537.36 (KHTML, like Gecko)
         Chrome/58.0.3029.110
         Safari/537.36""")]
    url = "https://www101.dcu.ie/timetables/feed.php?room=" + room + \
          "&week1=" + week + "&hour=" + str(hour) + \
          "&day=" + day + "&template=location"
    browser.open(url)
    return browser, url


def fill_form(args):
    browser = StatefulBrowser()
    cookie_jar = LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    room, date, from_time, to_time = args[0], args[1].split(
        "/"), args[2][:2] + ":" + args[2][2:], args[3][:2] + ":" + args[3][2:]
    day, month, year = date[0], date[1], date[2]
    if sys.version_info[0] < 3:
        name = raw_input("Name of society: ")
        person = raw_input("Your name: ")
        email = raw_input("Your email: ")
        number = raw_input("Your number: ")
    else:
        name = input("Name of society: ")
        person = input("Your name: ")
        email = input("Your email: ")
        number = input("Your number: ")
    browser.open("http://www.dcu.ie/registry/booking.shtml")
    browser.select_form(nr=2)
    browser["submitted[name_of_club_society]"] = name
    browser["submitted[name_of_person_making_booking]"] = person
    browser["submitted[contact_telephone_number]"] = number
    browser["submitted[date_room_required][day]"] = day
    browser["submitted[date_room_required][month]"] = month
    browser["submitted[date_room_required][year]"] = year
    browser["submitted[room_capacity]"] = "18"
    browser["submitted[description_of_event]"] = "Meeting"
    browser["submitted[hours_requiredfrom_to]"] = from_time + " - " + to_time
    browser["submitted[building_room_reference]"] = room
    browser["submitted[email_address]"] = email
    return browser


def check_room(timetable_url):
    html = get(timetable_url)
    soup = BeautifulSoup(html.text, "lxml")
    tr = soup.select('tr')
    return str(tr[12].getText().strip()) + " -> " + \
        str(tr[14].getText().strip())


def make_booking(form):
    request = form.request
    response = form.submit_selected()
    return "Form submitted successfully."


def draft_email(args):
    if sys.version_info[0] < 3:
        gmail_user = raw_input("Your gmail: ")
        gmail_password = raw_input("Your gmail password: ")
        name = raw_input("Society name: ")
        person = raw_input("Your name: ")
    else:
        gmail_user = input("Your gmail: ")
        gmail_password = input("Your gmail password: ")
        name = input("Society name: ")
        person = input("Your name: ")
    FROM = gmail_user
    TO = ['irene.mcevoy@dcu.ie']
    SUBJECT = 'Lab Booking'
    BODY = "Just wondering if you could book " + args[0] + " on the " + \
           args[1] + " from " + args[2][:2] + ":" + \
           args[2][2:] + " to " + args[3][:2] + ":" + args[3][2:] + \
           " for " + name + \
           ".\n\nThank you,\n" + person + "."
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, BODY)
    return gmail_user, gmail_password, FROM, TO, message


def send_email(gmail_user, gmail_password, FROM, TO, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(FROM, TO, message)
        server.close()
        print("Your email has been sent.")
    except BaseException:
        print("Email failed to send.")


def main():
    parser = setup_options()
    (options, arguments) = parser.parse_args()
    times = {
        '0800': '1',
        '0830': '2',
        '0900': '3',
        '0930': '4',
        '1000': '5',
        '1030': '6',
        '1100': '7',
        '1130': '8',
        '1200': '9',
        '1230': '10',
        '1300': '11',
        '1330': '12',
        '1400': '13',
        '1430': '14',
        '1500': '15',
        '1530': '16',
        '1600': '17',
        '1630': '18',
        '1700': '19',
        '1730': '20',
        '1800': '21',
        '1830': '22',
        '1900': '23',
        '1930': '24',
        '2000': '25',
        '2030': '26',
        '2100': '27',
        '2130': '28',
        '2200': '29',
        '2230': '30'}
    c = ['LG25', 'LG26', 'LG27', 'L101', 'L114', 'L125', 'L128']
    g = [
        'CG01',
        'CG02',
        'CG03',
        'CG04',
        'CG05',
        'CG06',
        'CG11',
        'CG12',
        'CG20',
        'CG68',
        'C166']
    details = sys.argv[2:]

    if options.book:
        if len(details) < 4:
            print("Booking requires more arguments. See the help for details.")
            sys.exit()
        else:
            if details[0] in c:
                user, password, from_who, to_who, message = draft_email(
                    details)
                if sys.version_info[0] < 3:
                    confimation = raw_input(
                        "\nIs this the correct information? (y/n): ").lower()
                else:
                    confirmation = input(
                        "\nIs this the correct information? (y/n): ").lower()
                if confirmation == "y":
                    send_email(user, password, from_who, to_who, message)
                else:
                    print("Draft withdrawn.")
                sys.exit()

            elif details[0] in g:
                form = fill_form(details)
                if sys.version_info[0] < 3:
                    confimation = raw_input(
                        "\nIs this the correct information? (y/n): ").lower()
                else:
                    confirmation = input(
                        "\nIs this the correct information? (y/n): ").lower()
                if confirmation == "y":
                    room_booked = make_booking(form)
                    print(room_booked)
                else:
                    print("Form submission withdrawn.")
                sys.exit()
            else:
                print("That room is not supported by this tool.")
                sys.exit()

    elif len(details) > 5:
        print("Too many arguments passed.")
        sys.exit()
    elif options.lookup:
        if options.computing:
            lst = c
        elif options.grattan:
            lst = g
        else:
            if len(details) <= 3:
                print("Not enough arguments passed.")
                sys.exit()
            room, week = details[0], details[1]
            day, time = details[2], details[3]
            if room not in c and room not in g:
                print("That room is not supported by this program.")
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
            if options.available:
                if len(status) <= 9:
                    print(room + ": " + status)
            else:
                print(room + ": " + status)
        sys.exit()
    elif options.now:
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
        if options.computing:
            lst = c
        elif options.grattan:
            lst = g
        for room in lst:
            timetable, url = build_timetable("GLA." + room, week, day, time)
            status = check_room(url)
            if options.available:
                if len(status) <= 9:
                    print(room + ": " + status)
            else:
                print(room + ": " + status)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

