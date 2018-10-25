from telegram.ext import CommandHandler, Updater, MessageHandler, Filters


updater = Updater('774969442:AAGh4SNNeZDSInwZF_XqSf-e5BDjcTwu0Uwx')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)


updater.start_polling()
updater.idle()