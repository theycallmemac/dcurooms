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
if sys.version_info[0] < 3:
    from cookielib import LWPCookieJar
else:
    from http.cookiejar import LWPCookieJar

__author__ = "theycallmemac"
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'

def check_arguments(week, day):
    if int(week) not in range(1, 53) or int(day) not in range(1, 7):
        print("Incorrect parameters passed.")
        sys.exit()
    else:
        pass
def email_version():
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
    return gmail_user, gmail_password, name, person

def form_version():
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
    return name, person, email, number

def check_version(func):
    if func == "email":
        return email_version()
    if func =="form":
        return form_version()


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

def check_room(timetable_url):
    html = get(timetable_url)
    soup = BeautifulSoup(html.text, "lxml")
    tr = soup.select('tr')
    return str(tr[12].getText().strip()) + " -> " + \
        str(tr[14].getText().strip())


def get_confirmation():
    if sys.version_info[0] < 3:
        confimation = raw_input(
        "\nIs this the correct information? (y/n): ").lower()
    else:
        confirmation = input(
        "\nIs this the correct information? (y/n): ").lower()

    return confirmation

