from telebot import types
import random
from .bunny_lists import *
from .game_instance import game_instance
from copy import deepcopy

sessions = {}


def on_message(bot, message):
    contentArr = message.text.split()[1:]
    if 'group' not in message.chat.type or not len(contentArr):
        return
    cmd = contentArr[0]
    chat_id = message.chat.id
    if chat_id not in sessions:
        sessions[chat_id] = deepcopy(
            game_instance)
    if cmd == 'reg':
        try:
            bot.send_message(message.from_user.id, 'Вы были зарегестрированы')
            sessions[chat_id]["player_ids"].append(
                message.from_user.id)
        except Exception:
            bot.send_message(message.chat.id, 'Сначала начните со мной диалог')
    if cmd == 'start':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура

        for cat in lists:
            cat_key = types.InlineKeyboardButton(
                text=cat, callback_data=cat)
            keyboard.add(cat_key)

        bot.send_message(message.chat.id, text='Выберете категорию:',
                         reply_markup=keyboard)


def on_keyboard(bot, call):
    if call.data in lists:
        start_game(bot, call)
    else:
        see_bunny(bot, call)
        pass


def see_bunny(bot, call):
    chat_id = call.message.chat.id
    p_id = call.data  # id
    p_name = bot.get_chat_member(chat_id, p_id).user.first_name
    bunny_id = sessions[chat_id]['bunny_id']
    bunny_un = bot.get_chat_member(chat_id, bunny_id).user.first_name
    if (str(p_id) == str(bunny_id)):
        msg = f'Охотники побеждают! {bunny_un} был зайцем!'
        sticker_id = 'CAACAgIAAxkBAAEEUexiRDY8qsNl5El9nserEwMd2pMvgwACtQIAAj-VzArH2fIsl0SiQiME'

    else:
        msg = f'Ой-ой-ой... {p_name} не был зайцем! {bunny_un} остался незамеченным xD'
        sticker_id = 'CAACAgIAAxkBAAEEUehiRDYw29iLwy7FF1qkk4a6-s9E5wACrQIAAj-VzAofR6oTAVmiYyME'

    bot.edit_message_text(
        chat_id=chat_id, message_id=call.message.id, text=msg)
    bot.send_sticker(chat_id, sticker_id)
    sessions[chat_id]['bunny_id'] = None


def start_game(bot, call):
    chat_id = call.message.chat.id
    if len(sessions[chat_id]['player_ids']) < 3:
        return bot.send_message(chat_id, text='Мало игроков')

    bot.edit_message_text(chat_id=chat_id, message_id=call.message.id,
                          text='тема выбрана')

    sample = random.sample(lists[call.data], 16)
    word = random.choice(sample)

    msg = '-' + '\n-'.join(sample)
    bot.send_message(chat_id, text=msg)

    print(sessions[chat_id]['player_ids'])
    player_ids = sessions[chat_id]['player_ids']
    bunny_id = random.choice(player_ids)
    sessions[chat_id]['bunny_id'] = bunny_id

    for id in player_ids:
        if id == bunny_id:
            bot.send_message(bunny_id, text='Ты заяц :3')
        else:
            bot.send_message(id, text=word)

    keyboard = types.InlineKeyboardMarkup()

    chat_id = call.message.chat.id
    for p_id in sessions[chat_id]['player_ids']:
        key = types.InlineKeyboardButton(
            text=bot.get_chat_member(chat_id, p_id).user.first_name,
            callback_data=p_id)
        keyboard.add(key)

    bot.send_message(chat_id, text='Кто же заяц?', reply_markup=keyboard)
