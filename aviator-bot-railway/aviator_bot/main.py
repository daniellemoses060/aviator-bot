import asyncio
import logging
from datetime import datetime, timedelta
from src.scraper import fetch_multiplier
from src.predictor import predict_entry
from src.telegram_alerts import send_alert

logging.basicConfig(level=logging.INFO)

async def main_loop():
    while True:
        try:
            multiplier = await fetch_multiplier()
            if multiplier is None:
                logging.warning("No multiplier data.")
                await asyncio.sleep(10)
                continue

            prediction = predict_entry(multiplier)

            if prediction["signal"]:
                bet_time = datetime.utcnow() + timedelta(minutes=2)
                time_str = bet_time.strftime("%H:%M:%S")
                message = f"**BET SIGNAL**\n\nEntry time: {time_str} UTC\nPredicted Cashout: {prediction['cashout']}x\nConfidence: {prediction['confidence']}"
                await send_alert(message)
                logging.info(f"Sent alert: {message}")

            await asyncio.sleep(20)

        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main_loop())
