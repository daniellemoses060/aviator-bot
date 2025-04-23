import telegram
import logging

BOT_TOKEN = "7828413663:AAG5yJpgDo2Q7tl7X8d6MKYvirAQBwPapII"
CHAT_ID = "5002184829"

def send_telegram_alert(message):
    try:
        bot = telegram.Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.constants.ParseMode.MARKDOWN)
    except Exception as e:
        logging.error(f"Failed to send Telegram alert: {e}")
