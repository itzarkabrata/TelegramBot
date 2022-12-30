import os,telebot

API_KEY='5978028781:AAHo8vS2cIYKTamNbvCHNvIoYb1UcaZHkQI'
bot=telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['do'])
def show(message):
    bot.reply_to(message,"Hey What can i do for you?")

bot.infinity_polling()