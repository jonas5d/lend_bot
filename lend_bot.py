TOKEN = "194904537:AAFgMlrpFkxBI-FTXZmcuLj0LuoCaK6iVXk"


from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import logging

# Enable logging
logging.basicConfig(
		        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
						        level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
	bot.sendMessage(update.message.chat_id, text='Help!')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def echo(bot,update):
  bot.sendMessage(update.message.chat_id,text="Got it")

def main():
  updater = Updater(TOKEN)
  dp = updater.dispatcher
  
  dp.addHandler(CommandHandler("start", start))
  dp.addHandler(CommandHandler("help", help))

  dp.addHandler(MessageHandler([filters.TEXT], echo))

  dp.addErrorHandler(error)

  updater.start_polling()

  updater.idle()

if __name__ == '__main__':
  main()