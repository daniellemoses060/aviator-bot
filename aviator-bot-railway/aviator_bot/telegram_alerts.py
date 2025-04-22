import telegram

def send_telegram_alert(message):
    bot = telegram.Bot(token="YOUR_BOT_TOKEN")
    chat_id = "YOUR_CHAT_ID"
    bot.send_message(chat_id=chat_id, text=message)
