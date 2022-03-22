from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def candle_command (update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    candy = 21
    candy_stap = 3
    update.message.reply_text(f'На столе --- {candy} конфета')
    while candy > 1:
        update.message.reply_text(f'Возьмите от 1 до {candy_stap} конфет... ')
        if candy > 0:
            player_1 = int(items[1])
            candy -= player_1
        update.message.reply_text(f'На столе --- {candy}')
        if candy == 0:
            update.message.reply_text('Победил 1 игрок')
            break
        if candy == 1:
            update.message.reply_text('Победил 2 игрок')
            break
    
        player_2 = random.randint(1, 3)
        candy -= player_2
        update.message.reply_text(f'На столе --- {candy}')
        if candy == 0:
            update.message.reply_text('Победил 2 игрок')
        if candy == 1:
            update.message.reply_text('Победил 1 игрок') 
