import api_calls as api
import constants as const

def displaySessionsByPin(message):
    pincode = message.split()[1]
    sessions = api.getSessionsByPin(pincode)
    print(sessions)
    index = 0
    text = ""
    for details in sessions['sessions']:
        text = text + str(details['name']) + '\n' + str(details['address']) + '\n From : ' + str(details['from']) + '\n To : ' + str(details['to']) + '\n Fee : ' + str(details['fee']) + '\n Available Doses : ' + str(details['available_capacity']) + '\n Minimum Age Limit : ' + str(details['min_age_limit']) + '\n Vaccine : ' + str(details['vaccine'])  + '\n--------------------------\n'

    if text != '' :
        return text + 'Book your vaccination now at : https://www.cowin.gov.in/home'  
    else:
        return text

def displayCalendarByPin(message):
    pincode = message.split()[1]
    calendar = api.getCalendarByPin(pincode)
    print(calendar)
    text = ""
    if calendar['centers'] == '':
        return 'No Vaccination Slots available in your district.'

    for details in calendar['centers']:
        text = text + 'Center : ' + str(details['name']) + '\nAddress : ' + str(details['address']) + '\nFee Type : ' + str(details['fee_type']) + '\nFrom : '+ str(details['from'])+ '\nTo : ' + str(details['to']) + '\nSessions : \n'+'\t\t--------------------------'

        for sessions in details['sessions']:
            print(sessions)
            text = text +'\n' + '\t\tDate : ' + str(sessions['date']) + '\n' + '\n\t\t\t\tAvailable Doses : ' + str(sessions['available_capacity']) + '\n\t\t\t\tMinimum Age Limit : ' + str(sessions['min_age_limit']) + '\n\t\t\t\tVaccine : ' + str(sessions['vaccine']) +'\n'+'\t\t--------------------------'

            # for slots in sessions['slots']:
            #     text = text + '\t\t\t' + slots +'\n'
        text = text + '$'

    if len(text) > const.MAX_MESSAGE_LENGTH:
        centers = text.split('$')
        print('CENTERS TYPE IS :' + str(type(centers)))
        return centers           
    else:
        return text + '\nBook your vaccination now at : https://www.cowin.gov.in/home'

