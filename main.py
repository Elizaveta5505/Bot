from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5199753571:AAGlrk4Vzlr_Aflf4Txsm-dRf2QP8O3iZPA')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('candle', candle_command))

print('server start')
updater.start_polling()
updater.idle()