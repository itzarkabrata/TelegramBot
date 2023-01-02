import os,telebot

def telegrambot():
    API_KEY='5978028781:AAHo8vS2cIYKTamNbvCHNvIoYb1UcaZHkQI'
    bot=telebot.TeleBot(API_KEY)

    @bot.message_handler(commands=['start'])
    def show(message):
        bot.reply_to(message,"Hello! Welcome to GCECT")

    @bot.message_handler(commands=['helpline'])
    def show(message):
        bot.reply_to(message,"""following commands will perform as stated below:
            /start -> Welcome to our college
            /helpline -> this message will show
            /content -> About the various weather details of different regions
            /basic_weather -> about the basic description , temperature , visibility, humidity
            /sunrise -> showing the time of sunrise
            /sunset -> showing the time of sunset
            /pressure -> showing atm pressure
            /wind_speed -> showing wind speed""")

    @bot.message_handler(commands=['content'])
    def show(message):
        bot.reply_to(message,""" We have various details regarding weather available :
                    basic weather details
                    sunrise
                    sunset
                    air pressure
                    wind speed""")    
    bot.infinity_polling()
    return "ok"