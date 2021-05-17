import constants as const
import display as dy

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message == ('/start'):
        return const.welcome_message
    if user_message == ('/pin'):
        return const.findByPin_message

    if pin_request(user_message):
        return dy.displaySessionsByPin(user_message)

    return 'Still Working...but not exactly'
    

def pin_request(message):
    request = message.split()
    if len(request)<2 or request[0].lower() not in "pin":
        return False
    else:
        return True