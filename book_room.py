import sys
import cookielib
import mechanize


def enter_data():
    date = raw_input("Enter date (1 - 31): ")
    if int(date) in range(1,32):
        pass
    else:
        print("Date not in range (1 - 31)")
        sys.exit()

    month = raw_input("Enter month (1 - 12): ")
    if int(month) in range(1,13):
        pass
    else:
        print("Month not in range (1 - 12)")
        sys.exit()

    year = raw_input("Enter year (2017 - 2019): ")
    if int(year) in range(2012,2020):
        pass
    else:
        print("Year not in range (2012 - 2019)")
        sys.exit()

    details = fill_form(date, month, year)

    return details


def fill_form(date, month, year):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)

    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    browser.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")]

    browser.open("http://www.dcu.ie/registry/booking.shtml")
    browser.select_form(nr=2)

    browser.form["submitted[name_of_club_society]"] = "Society"
    browser.form["submitted[name_of_person_making_booking]"] = "Name"
    browser.form["submitted[contact_telephone_number]"] = "Number"
    browser.form["submitted[date_room_required][day]"] = [date,]
    browser.form["submitted[date_room_required][month]"] = [month,]
    browser.form["submitted[date_room_required][year]"] = [year,]
    browser.form["submitted[room_capacity]"] = "Capacity"
    browser.form["submitted[description_of_event]"] = "Description"
    browser.form["submitted[hours_requiredfrom_to]"] = "Start - End"
    browser.form["submitted[building_room_reference]"] = "Room-Reference-Number"
    browser.form["submitted[email_address]"] = "Email"

    return browser


def format_form(lst):
    print("\n<Browser visiting http://www.dcu.ie/registry/booking.shtml")
    print("<post http://www.dcu.ie/registry/booking.shtml application/x-www-form-urlencoded")

    i = 3
    while i < len(lst) - 8:
        if lst[i] == "ImageControl(":
            pass
        elif lst[i] == "None>=)>":
            pass
        else:
            print("<" + lst[i].strip("\n selected form:\n"))
        i += 1


def make_booking(form):
    response = form.submit()
    request = form.request
    print("Header: " + request.header_items())
    if response.code == 200:
        return ("Response Code " + str(response.code) + ": form submitted successfully.")
    else:
        return ("Response Code " + str(response.code) + ": form not submitted.")


def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        form = enter_data()
    elif len(args) < 3 and len(details) >= 0:
        print("Incorrect number of parameters.")
        sys.exit()
    else:
        form = fill_form(args[0], args[1], args[2])

    form_lst = str(form).split("<")
    format_form(form_lst)

    confirmation = raw_input("\nIs this the correct input? (y/n): ")

    if confirmation == "y":
        room_booked = make_booking(form)
        print(room_booked)
    else:
        print("Form submission withdrawn.")

if __name__ == '__main__':
    main()
