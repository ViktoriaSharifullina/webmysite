import telepot

token = '5183960744:AAGFAD-gDPrSc_OnZhliPYsdZ_A2UPiBn8g'
my_id = -1001532655583
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")
