import constants as const
from datetime import datetime
import re
import requests

def getSessionsByPin(pincode):
    date = getDate()
    url = const.serverUrl + '/v2/appointment/sessions/public/findByPin?pincode=' + str(pincode) + '&date=' + str(date)
    print(url)
    headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    response = requests.get(url, headers= headers_dict)
    print(response.text)
    print(response.status_code)
    sessions = response.json()
    return sessions

def getDate():
    now = datetime.now()
    date_time = now.strftime("%d-%m-20%y")

    return str(date_time)


def main():
    getSessionsByPin(110001)

main()