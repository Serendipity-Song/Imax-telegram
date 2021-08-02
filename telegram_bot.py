import telegram

bot = telegram.Bot(token='1931579366:AAH_sXi20hHIFjDlYnk4Ul7klN1NACKUTuQ')

for i in bot.getUpdates():
    print(i.message)