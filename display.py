import api_calls as api

def displaySessionsByPin(message):
    pincode = message.split()[1]
    sessions = api.getSessionsByPin(pincode)
    print(sessions)
    index = 0
    text = ""
    for details in sessions['sessions']:
        text = text + str(details['name']) + '\n' + str(details['address']) + '\n From : ' + str(details['from']) + '\n To : ' + str(details['to']) + '\n Fee : ' + str(details['fee']) + '\n Available Doses : ' + str(details['available_capacity']) + '\n Minimum Age Limit : ' + str(details['min_age_limit']) + '\n Vaccine : ' + str(details['vaccine'])  + '\n--------------------------\n'

    return text + 'Book your vaccination now at : https://www.cowin.gov.in/home'  

def displayCalendarByPin(message):
    pincode = message.split()[1]
    calendar = api.getCalendarByPin(pincode)
    print(calendar)
    text = ""
    #for details in calendar['centers']:
