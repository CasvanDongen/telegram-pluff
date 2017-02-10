from telegram.ext import Updater, Filters, BaseFilter, MessageHandler

# Set token
updater = Updater("")
dispatcher = updater.dispatcher

# Set all commands
def txtGetRooster(bot, update):
    #TODO: Check if user exists in database
    message = "Voordat ik je je rooster voor vandaag kan geven moet ik eerst weten in welke klas je zit. Dit kun je instellen door het volgende commando uit te voeren: /klas \"klasnummer\"."
    bot.sendMessage(chat_id=update.message.chat_id, text=message)

# Unknown text, please try again
def unknownCmd(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, ik snap niet wat je bedoelt.")

# Define custom filter
class FilterRooster(BaseFilter):
    def filter(self, message):
        return 'rooster' in message.text.lower()
filterRooster = FilterRooster()

# Add handler to updater for unknown command
dispatcher.add_handler(MessageHandler(filterRooster, txtGetRooster))
dispatcher.add_handler(MessageHandler((Filters.text | Filters.command), unknownCmd))

# Let it run continuously
updater.start_polling()
updater.idle()
