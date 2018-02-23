import datetime
import sys
from requests import get
from bs4 import BeautifulSoup
import getpass

__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'


def confirm():
    if int(sys.version[0]) < 3:
        conf = raw_input("\033[1;93m{0}\033[00m".format(
            "\nIs this information correct? (y/n): "))
    else:
        conf = input("\033[1;93m{0}\033[00m".format(
            "\nIs this information correct? (y/n): "))
    if conf == "y":
        return conf
    else:
        return "n"


def check_args(week, day):
    if int(week) not in range(1, 53) or int(day) not in range(1, 7):
        print("\033[1;91m{0}\033[00m".format("Incorrect parameters passed."))
        sys.exit()
    else:
        pass


def check_room(timetable_url):
    html = get(timetable_url)
    soup = BeautifulSoup(html.text, "lxml")
    tr = soup.select('tr')
    return str(tr[12].getText().strip()) + " -> " + \
        str(tr[14].getText().strip())


def get_lst(c, g, options):
    if options.computing:
        lst = c
    elif options.grattan:
        lst = g
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


def get_version_email():
    if int(sys.version[0]) < 3:
        email = raw_input("\033[1;97m{0}\033[00m".format("Your gmail: "))
        password = getpass.getpass(
            "\033[1;97m{0}\033[00m".format("Your gmail password: "))
        your_name = raw_input("\033[1;97m{0}\033[00m".format("Your name: "))
        society = raw_input("\033[1;97m{0}\033[00m".format("Society name: "))
        return email, password, your_name, society
    else:
        email = input("\033[1;97m{0}\033[00m".format("Your gmail: "))
        password = getpass.getpass(
            "\033[1;97m{0}\033[00m".format("Your gmail password: "))
        your_name = input("\033[1;97m{0}\033[00m".format("Your name: "))
        society = input("\033[1;97m{0}\033[00m".format("Society name: "))
    return email, password, your_name, society


def get_version_form():
    if int(sys.version[0]) < 3:
        name = raw_input("\033[1;97m{0}\033[00m".format("Your name: "))
        email = raw_input("\033[1;97m{0}\033[00m".format("Your email: "))
        number = raw_input("\033[1;97m{0}\033[00m".format("Your number: "))
        society = raw_input("\033[1;97m{0}\033[00m".format("Society name: "))
        return email, number, name, society
    else:
        name = input("\033[1;97m{0}\033[00m".format("Your name: "))
        email = input("\033[1;97m{0}\033[00m".format("Your email: "))
        number = input("\033[1;97m{0}\033[00m".format("Your number: "))
        society = input("\033[1;97m{0}\033[00m".format("Society name: "))
        return email, number, name, society
