import constants as const
from datetime import datetime
import re
import requests
import json

def getSessionsByPin(pincode):
    date = getDate()
    print(date)
    url = const.serverUrl + '/v2/appointment/sessions/public/findByPin?pincode=' + str(pincode) + '&date=' + str(date)
    #headers_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    print(url)
    response = requests.get(url)#, headers= headers_dict)
    print('this is response : ' + str(response))
    print('here?' + str(response.status_code))
    sessions = json.loads(response.text)
    return sessions

def getCalendarByPin(pincode):
    date = getDate()
    url = const.serverUrl + '/v2/appointment/sessions/public/calendarByPin?pincode=' + str(pincode) + '&date=' + str(date)
    headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    response = requests.get(url, headers= headers_dict)
    print(response.status_code)
    calendar = response.json()
    return calendar

def getDate():
    now = datetime.now()
    date_time = now.strftime("%d-%m-20%y")
    return str(date_time)

# def main():
#     getSessionsByPin(110001)

# main()
