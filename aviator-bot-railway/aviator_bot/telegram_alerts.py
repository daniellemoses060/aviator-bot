import telegram
from datetime import datetime, timedelta

# Your credentials
bot = telegram.Bot(token="7828413663:AAG5yJpgDo2Q7tl7X8d6MKYvirAQBwPapII")
chat_id = "5002184829"

def send_telegram_alert(predicted_cashout_range, confidence_score=None):
    play_time = datetime.now() + timedelta(minutes=2)
    formatted_time = play_time.strftime("%H:%M:%S")

    message = f"**Aviator Entry Signal**\n\n" \
              f"**Time to Bet:** {formatted_time}\n" \
              f"**Target Cashout Range:** {predicted_cashout_range}\n"

    if confidence_score is not None:
        message += f"**Confidence Level:** {confidence_score:.2f}%\n"

    message += "\nPlace your bet manually 2 minutes from now."
    
    bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.constants.ParseMode.MARKDOWN)
