import constants as const
from telegram.ext import *
import responses as R 
import telegram
import api_calls as api
import display as dy
import os

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = const.API_KEY
print('Bot started ...')
bot = telegram.Bot(token=const.API_KEY)
print (bot.getMe())
print (api.getDate())

def start_command(update, context):
    bot.send_message(update.message.chat_id, const.welcome_message)

def help_command(update, context):
    bot.send_message(update.message.chat_id, const.help_message)

def pin_command(update, context):
    bot.send_message(update.message.chat_id, const.findByPin_message)

def calendar_command(update,context):
    bot.send_message(update.message.chat_id, const.findCalendarByPin_message)


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    if isinstance(response, list):
        for i in response:
            if i == response[-1]:
                bot.send_message(update.message.chat_id, i + '\nBook your vaccination now at : https://www.cowin.gov.in/home')
            else:
                bot.send_chat_action(chat_id = update.message.chat_id, action= telegram.ChatAction.TYPING)
                bot.send_message(update.message.chat_id, i)
    else:
        bot.send_chat_action(chat_id = update.message.chat_id, action= telegram.ChatAction.TYPING)
        update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(const.API_KEY, use_context=True)
    dp = updater.dispatcher #dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("pin", pin_command))
    dp.add_handler(CommandHandler("calendar", calendar_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    #Start the bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url='https://stark-castle-26205.herokuapp.com/' + const.API_KEY)
    #updater.bot.setWebhook('https://peaceful-atoll-46044.herokuapp.com/' + const.API_KEY)

    # updater.start_polling()   #command that starts the programme. If want time delay before taking next input from user, use : updater.start_polling(5) (means delay of 5 seconds)
    updater.idle()

main()