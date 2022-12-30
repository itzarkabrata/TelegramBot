import telegram.ext

Token="5978028781:AAGQwAlawbkWL7_-UPepL0eqUxL4mmj2SrI"
up=telegram.ext.updater(Token,use_context=True)
dispatcher=up.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to GCECT")

def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to our college
        /help -> this message will show
        /content -> About the various weather details of different regions
        /basic_weather -> about the basic description , temperature , visibility, humidity
        /sunrise -> showing the time of sunrise
        /sunset -> showing the time of sunset
        /pressure -> showing atm pressure
        /wind_speed -> showing wind speed
        """
    )

def content(update, context):
    update.message.reply_text(
        """ We have various details regarding weather available :
                basic weather details
                sunrise
                sunset
                air pressure
                wind speed
        """)

""" basic_weather functions should be written here
    functions under basic function
"""
""" sunrise function
    sunset function
    pressure function
    wind_speed function
"""

dispatcher.add_handler(telegram.ext.Commandhandler('start', start))
dispatcher.add_handler(telegram.ext.Commandhandler('help', help))
dispatcher.add_handler(telegram.ext.Commandhandler('content', content))
dispatcher.add_handler(telegram.ext.Commandhandler('basic_weather', basic_weather))
dispatcher.add_handler(telegram.ext.Commandhandler('sunrise', sunrise))
dispatcher.add_handler(telegram.ext.Commandhandler('sunset', sunset))
dispatcher.add_handler(telegram.ext.Commandhandler('pressure', pressure))
dispatcher.add_handler(telegram.ext.Commandhandler('wind_speed', wind_speed))

updater.start_polling()
updater.idle()