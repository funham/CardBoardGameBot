from bunny_lists import *
from game_instance import *
from telebot import types


def on_message(bot, message):
    if 'group' not in message.chat.type:
        return
    contentArr = message.text.split()[1:]
    cmd = contentArr[0]
    if contentArr and cmd == 'reg':
        try:
            bot.send_message(message.from_user.id, 'Вы были зарегестрированы')
            games[message.chat.id]["player_ids"].append(message.from_user.id)
        except Exception:
            bot.send_message(message.chat.id, 'Сначала начните со мной диалог')
    if contentArr and cmd == 'start':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура

        for cat in lists:
            cat_key = types.InlineKeyboardButton(
                text=cat, callback_data=cat)
            keyboard.add(cat_key)

        bot.send_message(message.chat.id, text='Выберете категорию:',
                         reply_markup=keyboard)
