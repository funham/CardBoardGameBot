import bunny_lists as bl
import game_instance
import copy

games = {}


def on_message(bot, message):
    if 'group' not in message.chat.type:
        return
    contentArr = message.text.split()[1:]
    if message.chat.id not in games:
        games[message.chat.id] = copy.deepcopy(game_instance.game_instance)
    if contentArr and contentArr[0] == 'reg':
        try:
            bot.send_message(message.from_user.id, 'Вы были зарегестрированы')
            games[message.chat.id]["player_ids"].append(message.from_user.id)
        except Exception:
            bot.send_message(message.chat.id, 'Сначала начните со мной диалог')
    elif contentArr and contentArr[0] == 'start':
        pass


def on_keyboard(call):
    pass