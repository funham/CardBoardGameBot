import telebot
from games import mafia

bot = telebot.TeleBot('5153566900:AAEnwjIGmi2g1KlRCDow7zTWCBM_hMnpySY')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['mafia'])
def on_mafia(message):
    mafia.on_message(message)

bot.infinity_polling()