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
import checks
if sys.version_info[0] < 3:
    from cookielib import LWPCookieJar
else:
    from http.cookiejar import LWPCookieJar

__author__ = "theycallmemac"
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'

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
    room, date, from_time, to_time = args[0], args[1].split("/"), args[2][:2] + ":" + args[2][2:], args[3][:2] + ":" + args[3][2:]
    day, month, year = date[0], date[1], date[2]
    name, person, email, number = checks.check_version("form")
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


def make_booking(form):
    request = form.request
    response = form.submit_selected()
    return "Form submitted successfully."


def draft_email(args):
    gmail_user, gmail_password, name, person = checks.check_version("email")
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

def send_email(gmail_credentials, FROM, TO, message):
    try:
        gmail_user, gmail_password = gmail_credentials[0], gmail_credentials[1]	
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(FROM, TO, message)
        server.close()
        print("Your email has been sent.")
    except BaseException:
        print("Email failed to send.")

