import telegram

# Telegram Bot configuration
BOT_TOKEN = "7828413663:AAG5yJpgDo2Q7tl7X8d6MKYvirAQBwPapII" 
CHAT_ID = "5002184829" 

def send_telegram_alert(message):
    """
    Sends a message to the specified Telegram chat.
    """
    try:
        bot = telegram.Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=message)
        print("Telegram alert sent successfully!")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
