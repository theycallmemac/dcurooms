import sys
from mechanicalsoup import StatefulBrowser
from http.cookiejar import LWPCookieJar
from requests import get

__author__ = "theycallmemac"
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2017 theycallmemac'
__license__ = 'GPL-3.0'

class RoomBooking(object):
    arguments = []
    email= ""
    number = ""
    name = ""
    society = ""

    def __init__(self, email, number, name, society, arguments):
        self.arguments = arguments
        self.email = email
        self.number = number
        self.name = name
        self.society = society

    def fill(self):
        browser = StatefulBrowser()
        cookie_jar = LWPCookieJar()
        browser.set_cookiejar(cookie_jar)
        room, date, start, end = self.arguments[0], self.arguments[1].split("/"), self.arguments[2][:2] + ":" + self.arguments[2][2:], self.arguments[3][:2] + ":" + self.arguments[3][2:]
        day, month, year = date[0], date[1], date[2]
        browser.open("http://www.dcu.ie/registry/booking.shtml")
        browser.select_form(nr=2)
        browser["submitted[name_of_club_society]"] = self.society
        browser["submitted[name_of_person_making_booking]"] = self.name
        browser["submitted[contact_telephone_number]"] = self.number
        browser["submitted[date_room_required][day]"] = day
        browser["submitted[date_room_required][month]"] = month
        browser["submitted[date_room_required][year]"] = year
        browser["submitted[room_capacity]"] = "18"
        browser["submitted[description_of_event]"] = "Meeting"
        browser["submitted[hours_requiredfrom_to]"] = start + " - " + end
        browser["submitted[building_room_reference]"] = room
        browser["submitted[email_address]"] = self.email
        return browser

    def submit(self, form):
        request = form.request
        response = form.submit_selected()
        return "Form submitted successfully."
