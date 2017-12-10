#!/usr/bin/python
import sys
import cookielib
import mechanize
import requests
import datetime
from bs4 import BeautifulSoup

def get_current_time():
    current = []
    day = datetime.datetime.now().weekday()
    current.append(day + 1)
    hour = datetime.datetime.now().hour
    current.append(hour)
    minute = datetime.datetime.now().minute
    current.append(minute)
     
    return current

def build_timetable(room, week, day, hour):
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
    url = "https://www101.dcu.ie/timetables/feed.php?room=" + room + "&week1=" + week + "&hour=" + str(hour) + "&day=" + day + "&template=location"
    browser.open(url)

    return browser, url

def check_room(timetable_url):
    html = requests.get(timetable_url)
    soup = BeautifulSoup(html.text, "lxml")
    tr = soup.select('tr')

    return str(tr[12].getText().strip()) + " -> " + str(tr[14].getText().strip())

def main():
    arg = sys.argv[1]
    times = {'0800':'1',
            '0830':'2', 
            '0900':'3', 
            '0930':'4',
            '1000':'5', 
            '1030':'6',
            '1100':'7',
            '1130':'8',
            '1200':'9',
            '1230':'10',
            '1300':'11',
            '1330':'12',
            '1400':'13',
            '1430':'14',
            '1500':'15',
            '1530':'16',
            '1600':'17',
            '1630':'18',
            '1700':'19',
            '1730':'20',
            '1800':'21',
            '1830':'22',
            '1900':'23',
            '1930':'24',
            '2000':'25',
            '2030':'26',
            '2100':'27'}

    soc = ['LG25','LG26','LG27','L101','L114','L125','L128']
    hg = ['CG01', 'CG02','CG03','CG04','CG05','CG06','CG11','CG12','CG20','CG68','C166']
    current = get_current_time()
    
    if current[2] >= 30:
        current[2] = '30'
    else:
        current[2] = '00'

    time = str(current[1]) + str(current[2])

    for k,v in times.items():
        if k == time:
            time = v
            break
        else:
            pass

    if arg == '1':
        for room in hg:
            timetable, url = build_timetable("GLA." + room, '12', str(current[0]), time)
            status = check_room(url)
            print(room + ": " + status)

    else:
        for room in soc:
            timetable, url = build_timetable("GLA." + room, '12', str(current[0]), time)
            status = check_room(url)
            print(room + ": " + status)
if __name__ == '__main__':
    main()
