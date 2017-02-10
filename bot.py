from telegram.ext import Updater, Filters, BaseFilter, MessageHandler, CommandHandler

# Set token
updater = Updater("")
dispatcher = updater.dispatcher

# rooster command
def txtGetRooster(bot, update):
    #TODO: Check if user exists in database
    message = "Voordat ik je je rooster voor vandaag kan geven moet ik eerst weten in welke klas je zit. Dit kun je laten weten door je pcn op te geven, dit kan met het volgende commando: /pcn \"000000\"."
    bot.sendMessage(chat_id=update.message.chat_id, text=message)

# PCN command
def cmdPcn(bot, update, args):
    arguments = ' '.join(args).upper()
    if len(arguments) > 1 or len(arguments) < 1:
        message = "Je gebruikt het commando niet helemaal correct. Probeer het opnieuw als /pcn \"000000\""
    else:
        #save pcn to databse with chat user id or slug
        message = "Top!"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)

# Help command
def cmdHelp(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="De volgende commando's kun je gebruiken:\r\n\r\n/pcn \"000000\" - PCN nummer instellen om rooster te bepalen\r\n/rooster - Om je rooster op te halen voor vandaag, je kunt ook gewoon het woord rooster in een zin gebruiken.\r\n/help, /cmd of /commands - Huidige uitleg.")

# Unknown text, please try again
def unknownCmd(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, ik snap niet wat je bedoelt. Vraag om hulp óf gebruik het commando /help")

# Define custom filter
class FilterRooster(BaseFilter):
    def filter(self, message):
        return 'rooster' in message.text.lower()
filterRooster = FilterRooster()

# Add handler to dispatcher for rooster command
dispatcher.add_handler(MessageHandler(filterRooster, txtGetRooster))
dispatcher.add_handler(CommandHandler('rooster', txtGetRooster))

# Add handler to dispatcher for PCN command
dispatcher.add_handler(CommandHandler('pcn', cmdPcn, pass_args=True))

# Add handler to dispatcher for /help command
dispatcher.add_handler(CommandHandler('help', cmdHelp))
dispatcher.add_handler(CommandHandler('cmd', cmdHelp))
dispatcher.add_handler(CommandHandler('commands', cmdHelp))

# Add handler to dispatcher for unknown command
dispatcher.add_handler(MessageHandler((Filters.text | Filters.command), unknownCmd))

# Let it run continuously
updater.start_polling()
updater.idle()
