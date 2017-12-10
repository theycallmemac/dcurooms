import smtplib
import sys
import random


def draft_email(user, password, recipient, subject, body):
    gmail_user = user
    gmail_password = password
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    BODY = body

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
    except:
        print("Email failed to send.")


def main():

    details = raw_input("\nWhat days, times and rooms are you booking?: ")
    template1 = "Hi Irene,\n\nJust wondering if you could book " + details + " on behalf of Redbrick.\n\nThanking you,\nJames McDermott.\nRedbrick Events Officer."
    template2 = "Hello again,\n\nCould you please book " + details + " for Redbrick.\n\nThanks,\nJames McDermott.\nRedbrick Events Officer."
    template3 = "Just wondering if you could book " + details + " for Redbrick.\n\nThank you,\nJames McDermott.\nRedbrick Events Officer."

    templates = [template1,template2,template3]
    body = random.choice(templates)

    draft = draft_email("my-email","password","irene.mcevoy@dcu.ie","Lab Booking", body)
    print("\n" + " ".join(draft[4:]))

    confirmation = raw_input("\nIs this the correct input? (y/n): ")

    if confirmation.lower() == "y":
        sent = send_email(draft[0],draft[1],draft[2],draft[3],draft[4])
    else:
        print("Email cancelled and not sent.")

if __name__ == '__main__':
    main()
