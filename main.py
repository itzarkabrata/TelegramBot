# def hello_world(request):
import os
import telebot
import requests
import json,datetime

API_KEY = '5978028781:AAHo8vS2cIYKTamNbvCHNvIoYb1UcaZHkQI'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def show(message):
    bot.reply_to(message, "Hello! Welcome to GCECT")


@bot.message_handler(commands=['helpline'])
def show(message):
    bot.reply_to(message, """following commands will perform as stated below:
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
    bot.reply_to(message, """ We have various details regarding weather available :
                basic weather details
                sunrise
                sunset
                air pressure
                wind speed""")


@bot.message_handler(func=lambda message: True)
def weather(message):
    c = message.text

    W_Url = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = '4961dfe8dac0eb120ff56f0dd8af8f0a'
    URL = W_Url + "q=" + c + "&appid=" + API_KEY

    City = ""
    response = requests.get(URL)

    # ---->Condition request
    if response.status_code == 200:
        # ---->formating to Json
        data = response.json()
        # ---->gettingt ta dictionary
        main = data['main']
        # ----->Temperature
        temp = (int(main['temp'])-273.0)
        # ----->Visibilty
        visibility = (data['visibility'])
        # ---->Humidity
        humid = (main['humidity'])
        # ---->Status
        status = data['weather']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        City += f"-----{c}-----"+'\n'+f"Temperature: {temp} Celsius"+'\n'+f"Humidity: {humid} g/kg" + \
            '\n'+f"Visibility: {visibility} "+'\n' +f"Sunrise {sunrise}"+'\n'+f"Sunset {sunset}"+'\n'+ \
                f"Weather Condition: {status[0]['description']}"

        bot.send_message(message.chat.id, City)
    else:
        # Invalid City message
        bot.send_message(message.chat.id, """Enter  a  Valid City""")


bot.infinity_polling()
#   return 'OK'