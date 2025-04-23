import telegram
import asyncio

bot_token = "7828413663:AAG5yJpgDo2Q7tl7X8d6MKYvirAQBwPapII"
chat_id = "5002184829"

async def send_alert(message):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
