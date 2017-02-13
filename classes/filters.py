from telegram.ext import Filters, BaseFilter

class FilterRooster(BaseFilter):
    def filter(self, message):
        return 'rooster' in message.text.lower()
