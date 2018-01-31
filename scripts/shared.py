import sys
import smtplib


__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'

def confirm():
    if int(sys.version[0]) < 3:
        conf = raw_input("Is this information correct? (y/n): ")
    else:
        conf - input("Is this information correct? (y/n): ")
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
