import asyncio
from src.scraper import fetch_multiplier
from src.predictor import predict_entry
from src.telegram_alerts import send_telegram_alert
import datetime
import logging

logging.basicConfig(level=logging.INFO)

async def main():
    while True:
        try:
            multiplier = await fetch_multiplier()
            if multiplier:
                prediction = predict_entry(multiplier)
                if prediction["signal"]:
                    now = datetime.datetime.now().strftime("%H:%M:%S")
                    entry_time = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%H:%M:%S")
                    message = (
                        f"**Aviator Signal**\n"
                        f"Entry Time: {entry_time}\n"
                        f"Predicted Cashout: {prediction['cashout']}x\n"
                        f"Current Multiplier: {multiplier}x\n"
                        f"Confidence: {prediction['confidence']}\n"
                        f"#Aviator #Signal"
                    )
                    send_telegram_alert(message)
            await asyncio.sleep(10)  # check every 10 seconds
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
