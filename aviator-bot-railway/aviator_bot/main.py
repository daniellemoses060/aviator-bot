import asyncio
import time
from telegram_alerts import send_telegram_alert
from scraper import get_live_multiplier
from predictor import update_history, predict_next_multiplier
import logging
import datetime

logging.basicConfig(level=logging.INFO)

def should_send_signal(prediction):
    return 1.8 <= prediction <= 10.0

def format_time(dt):
    return dt.strftime("%H:%M:%S")

async def main_loop():
    while True:
        try:
            multiplier = await get_live_multiplier()
            if multiplier:
                update_history(multiplier)
                prediction = predict_next_multiplier()

                if should_send_signal(prediction):
                    alert_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
                    message = (
                        f"*Aviator Signal*\n"
                        f"Entry Time: *{format_time(alert_time)}*\n"
                        f"Predicted Cashout: *{prediction}x*\n"
                        f"Current Multiplier: {multiplier}x\n"
                        f"Confidence: High\n"
                        f"#Aviator #Signal"
                    )
                    send_telegram_alert(message)

            time.sleep(10)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            time.sleep(15)

if __name__ == "__main__":
    asyncio.run(main_loop())
