import datetime
import sys
from requests import get
from bs4 import BeautifulSoup

__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'

def confirm():
    if int(sys.version[0]) < 3:
        conf = raw_input("Is this information correct? (y/n): ")
    else:
        conf = input("Is this information correct? (y/n): ")
    if conf == "y":
        return conf
    else:
        return "n"


def check_args(week, day):
    if int(week) not in range(1, 53) or int(day) not in range(1, 7):
        print("Incorrect parameters passed.")
        sys.exit()
    else:
        pass

def check_room(timetable_url):
    html = get(timetable_url)
    soup = BeautifulSoup(html.text, "lxml")
    tr = soup.select('tr')
    return str(tr[12].getText().strip()) + " -> " + str(tr[14].getText().strip())

def get_lst(c, g, options):
    if options.computing == True: lst = c
    elif options.grattan == True: lst = g
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
        email = raw_input("Your gmail: ")
        password = raw_input("Your gmail password: ")
        your_name = raw_input("Your name: ")
        society = raw_input("Society name: ")
        return email, password, your_name, society
    else:
        email = str(input("Your gmail: "))
        password = input("Your gmail password: ")
        your_name = input("Your name: ")
        society = input("Society name: ")
    return email, password, your_name, society


def get_version_form():
    if int(sys.version[0]) < 3:
        name = raw_input("Your name: ")
        email = raw_input("Your email: ")
        number = raw_input("Your number: ")
        society = raw_input("Society name: ")
        return email, number, name, society
    else:
        name = input("Your name: ")
        email = input("Your email: ")
        number = input("Your number: ")
        society = input("Society name: ")
        return email, number, name, society
