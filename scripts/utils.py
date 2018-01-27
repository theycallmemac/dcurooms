import datetime
import sys

__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'


def get_lst(c, g, options):
    if options.computing: lst = c
    elif options.grattan: lst = g
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
        name = string(input("Your name: "))
        email = input("Your email: ")
        number = input("Your number: ")
        society = input("Society name: ")
        return email, number, name, society
