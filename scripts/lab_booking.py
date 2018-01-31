import sys
import smtplib


__author__ = "theycallmemac"
__version__ = '2.0.0'
__copyright__ = 'Copyright (c) 2018 theycallmemac'
__license__ = 'GPL-3.0'


class LabBooking(object):
    arguments = []
    email= ""
    password = ""
    name = ""
    society = ""

    def __init__(self, email, password, name, society, arguments):
        self.arguments = arguments
        self.email = email
        self.password = password
        self.name = name
        self.society = society

    def draft(self):
        FROM = self.email
        TO = ['irene.mcevoy@dcu.ie']
        SUBJECT = 'Lab Booking'
        BODY = "Just wondering if you could book " + self.arguments[0] + " on the " + \
                self.arguments[1] + " from " + self.arguments[2][:2] + ":" + \
                self.arguments[2][2:] + " to " + self.arguments[3][:2] + ":" + \
                self.arguments[3][2:] + " for " + self.society + ".\n\nThank you,\n" + self.name + "."
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, BODY)
        return (FROM, TO), message


    def send(self, FROM, TO, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(FROM, TO, message)
            server.close()
            return "Your email has been sent."
        except BaseException:
            return "Email failed to send."

