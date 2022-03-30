import bunny_lists as bl

games = {}


def on_message(bot, message):
    if 'group' not in message.chat.type:
        return
    contentArr = message.text.split()[1:]
    if contentArr and contentArr[0] == 'reg':
        try:
            bot.send_message(message.from_user.id, 'hello')
        except Exception:
            bot.send_message(message.chat.id, 'Сначала начните со мной диалог')
