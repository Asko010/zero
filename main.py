import telebot

bot = telebot.TeleBot("8159450337:AAG2Dgtw5leh-yavyMjh7pnK0GXyUS2qVOM")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "привет, я бот, который умеет отвечать как попугай")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, "чтобы получить помощь, введите /help")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()