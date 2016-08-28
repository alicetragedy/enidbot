from uuid import uuid4
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultPhoto, InlineQueryResultGif, InputTextMessageContent
import logging
import os
#import config

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
                                          title="drawing enid",
                                          photo_url="http://www.radioteos.ru/kadr/wp-content/uploads/2013/11/ghost-world.jpg",
                                          thumb_url="http://www.radioteos.ru/kadr/wp-content/uploads/2013/11/ghost-world.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="only stupid people",
                                          photo_url="https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/3/19/16/enhanced-buzz-3056-1363724853-4.jpg",
                                          thumb_url="https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/3/19/16/enhanced-buzz-3056-1363724853-4.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="punk rock enid",
                                          photo_url="https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr01/2013/3/19/16/enhanced-buzz-1962-1363723752-1.jpg",
                                          thumb_url="https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr01/2013/3/19/16/enhanced-buzz-1962-1363723752-1.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="so bad",
                                          photo_url="https://65.media.tumblr.com/tumblr_m8dv6zyXIW1raezz2o1_500.jpg",
                                          thumb_url="https://65.media.tumblr.com/tumblr_m8dv6zyXIW1raezz2o1_500.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="just disappear",
                                          photo_url="https://24.media.tumblr.com/tumblr_me1g7wPYcc1rsyukao1_1280.jpg",
                                          thumb_url="https://24.media.tumblr.com/tumblr_me1g7wPYcc1rsyukao1_1280.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="sick of everybody",
                                          photo_url="https://41.media.tumblr.com/4c522a9a47efb66847759c08d503fe94/tumblr_nk6n8w7yel1rsyukao1_500.jpg",
                                          thumb_url="https://41.media.tumblr.com/4c522a9a47efb66847759c08d503fe94/tumblr_nk6n8w7yel1rsyukao1_500.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="cannot relate",
                                          photo_url="https://67.media.tumblr.com/tumblr_m8dv0iU7lT1raezz2o1_500.jpg",
                                          thumb_url="https://67.media.tumblr.com/tumblr_m8dv0iU7lT1raezz2o1_500.jpg",
                                          ))

  results.append(InlineQueryResultPhoto(id=uuid4(),
                                          type="photo",
                                          title="sick of the weirdos",
                                          photo_url="https://data.whicdn.com/images/124205910/large.jpg",
                                          thumb_url="https://data.whicdn.com/images/124205910/large.jpg",
                                          ))

  results.append(InlineQueryResultGif(id=uuid4(),
                                          type="gif",
                                          title="all I hate",
                                          gif_url="http://starcrush.com/files/2013/08/ghost-world6.gif",
                                          thumb_url="http://starcrush.com/files/2013/08/ghost-world6.gif",
                                          ))

  results.append(InlineQueryResultGif(id=uuid4(),
                                          type="gif",
                                          title="poisoning everybody",
                                          gif_url="https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/3/19/16/anigif_enhanced-buzz-28104-1363723463-20.gif",
                                          thumb_url="https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/3/19/16/anigif_enhanced-buzz-28104-1363723463-20.gif",
                                          ))

  results.append(InlineQueryResultGif(id=uuid4(),
                                          type="gif",
                                          title="I hate my interests",
                                          gif_url="https://s3-ak.buzzfed.com/static/enhanced/webdr02/2013/3/19/16/anigif_enhanced-buzz-25232-1363724828-12.gif",
                                          thumb_url="https://s3-ak.buzzfed.com/static/enhanced/webdr02/2013/3/19/16/anigif_enhanced-buzz-25232-1363724828-12.gif",
                                          ))

  results.append(InlineQueryResultGif(id=uuid4(),
                                          type="gif",
                                          title="High on life",
                                          gif_url="https://24.media.tumblr.com/b3eedb9df5de2e457768849d5635710c/tumblr_mi8x0dX5Gd1qd4d7jo2_500.gif",
                                          thumb_url="https://24.media.tumblr.com/b3eedb9df5de2e457768849d5635710c/tumblr_mi8x0dX5Gd1qd4d7jo2_500.gif",
                                          ))

  results.append(InlineQueryResultGif(id=uuid4(),
                                          type="gif",
                                          title="excited",
                                          gif_url="https://24.media.tumblr.com/tumblr_lyjiut8frh1qev1kto1_500.gif",
                                          thumb_url="https://24.media.tumblr.com/tumblr_lyjiut8frh1qev1kto1_500.gif",
                                          ))

  bot.answerInlineQuery(update.inline_query.id, results=results)



# Helpers

updater = Updater(os.environ['TELEGRAM_SECRET_KEY'])

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
