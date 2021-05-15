import constants as const

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message == ('/start'):
        return const.welcome_message

    return 'Still Working...but not exactly'
    