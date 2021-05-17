import constants as const
import display as dy

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message == ('/start'):
        return const.welcome_message
    if user_message == ('/pin'):
        return const.findByPin_message

    if pin_request(user_message):
        text =  dy.displaySessionsByPin(user_message)
        if text == '':
            return 'No Vaccination Slot registered under COWIN available in your district.'
        else:
            return text
    
    if calendar_request(user_message):
        text = dy.displayCalendarByPin(user_message)
        if text == '':
            return 'No Vaccination Slot registered under COWIN available in your district.'
        else:
            return text

    return 'Request not valid. Kindly enter the request/command in the correct format.'
    

def pin_request(message):
    request = message.split()
    if len(request)<2 or request[0].lower() not in "pin":
        return False
    else:
        return True

def calendar_request(message):
    request = message.split()
    if len(request)<2 or request[0].lower() not in "calendar":
        return False
    else:
        return True