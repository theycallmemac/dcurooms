import datetime
from optparse import OptionParser
from lab_booking import LabBooking
from room_booking import RoomBooking
from lookup import LookUp
from now import Now
import utils
import shared

__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'

def get_lab_credentials():
    return utils.get_version_email()

def get_room_credentials():
    return utils.get_version_form()

def booking_lab(info):
    email, password, your_name, society = get_lab_credentials()
    lab = LabBooking(email, password, your_name, society, info[1])
    emails, message = lab.draft()
    print(message)
    conf = shared.confirm()
    if conf == "y":
        result = lab.send(emails[0], emails[1], message)
        print(result)
    else:
        "Booking cancelled."

def booking_room(info):
    email, number, name, society = get_room_credentials()
    room = RoomBooking(email, number, name, society, info[1])
    form = room.fill()
    conf = shared.confirm()
    if conf == "y":
        result = room.submit(form)
        print(result)
    else:
        "Booking cancelled."

def lookup_building(rooms, info, options):
    lst = utils.get_lst(rooms[0], rooms[1], options)
    week, day, hour = info[1]
    look = LookUp(week, day, hour)
    shared.check_args(week, day)
    look.check_time(info[0])
    look.building_option(lst)

def lookup_room(info):
    room, week, day, hour = info[1]
    look = LookUp(week, day, hour)
    utils.check_args(week, day)
    look.check_time(info[0])
    look.room_option(room)

def now(rooms, info, options):
    week, day, hour, minute = utils.get_current_time(datetime.datetime.now())
    now = Now(week, day, hour, minute)
    now.round_it()
    utils.check_args(week, day)
    now.check_time(info[0])
    lst = utils.get_lst(rooms[0], rooms[1], options)
    now.building_option(lst, options)

