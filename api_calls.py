import constants as const
from datetime import datetime

def getSessionsByPin(pincode):
    date = getDate()
    url = const.serverUrl + '/v2/appointment/sessions/public/findByPin?pincode=' + pincode + '&date=' + date
    print (date)
    print (url)


def getDate():
    now = datetime.now()
    date_time = now.strftime("%d-%m-%y")

    return str(date_time)