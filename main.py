import constants as const
from telegram.ext import *
import responses as R 

print('Bot started ...')

def start_command(update, context):
    update.message.reply_text('Start Reply >!')

def help_command(update, context):
    update.message.reply_text('Help Reply >!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(const.API_KEY, use_context=True)
    dp = updater.dispatcher #dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()   #command that starts the programme. If want time delay before taking next input from user, use : updater.start_polling(5) (means delay of 5 seconds)
    updater.idle()

main()