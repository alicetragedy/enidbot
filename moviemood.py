from uuid import uuid4
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultPhoto, InputTextMessageContent
import logging
import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Methods handling commands

def start(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id,
                  text="I'm a bot, please talk to me!")

def hello(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id,
                  text='Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
  bot.sendMessage(update.message.chat_id, text='Help!')

def justkillme(bot, update):
  bot.sendPhoto(chat_id=update.message.chat_id, photo='https://24.media.tumblr.com/tumblr_mebsc3BYeW1qkyz1oo2_500.png')

def inlinequery(bot, update):
  query = update.inline_query.query
  results = list()

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="ghost world",
                                          photo_url="http://www.radioteos.ru/kadr/wp-content/uploads/2013/11/ghost-world.jpg",
                                          thumb_url="http://www.radioteos.ru/kadr/wp-content/uploads/2013/11/ghost-world.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          photo_url="http://67.media.tumblr.com/tumblr_l3pbo60QXN1qzdstpo1_500.jpg",
                                          thumb_url="http://67.media.tumblr.com/tumblr_l3pbo60QXN1qzdstpo1_500.jpg",
                                          ))

  bot.answerInlineQuery(update.inline_query.id, results=results)



# Helpers

updater = Updater(config.TELEGRAM_SECRET_KEY)

# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('justkillme', justkillme))

# on noncommand i.e message - echo the message on Telegram
dispatcher.add_handler(InlineQueryHandler(inlinequery))

updater.start_polling()
updater.idle()
