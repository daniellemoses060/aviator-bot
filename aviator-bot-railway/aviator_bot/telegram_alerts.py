import telegram
import logging

# Your actual Telegram Bot credentials
BOT_TOKEN = "7828413663:AAG5yJpgDo2Q7tl7X8d6MKYvirAQBwPapII"
CHAT_ID = "5002184829"

def send_telegram_alert(message):
    """
    Sends a formatted message to Telegram safely with logging.
    """
    try:
        bot = telegram.Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.constants.ParseMode.MARKDOWN)
        logging.info("Telegram alert sent.")
    except Exception as e:
        logging.error(f"Error sending Telegram alert: {e}")
