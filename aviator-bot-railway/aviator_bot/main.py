import time
import logging
from datetime import datetime, timedelta
from scraper import scrape_data
from telegram_alerts import send_telegram_alert
from predictor import update_history, predict_next_cashout

logging.basicConfig(level=logging.INFO)

def format_bet_time(delay_minutes=2):
    future_time = datetime.now() + timedelta(minutes=delay_minutes)
    return future_time.strftime("%H:%M:%S")

def run_bot():
    while True:
        try:
            logging.info("Scraping Betway Aviator data...")
            game_data = scrape_data()

            if game_data and "multiplier" in game_data:
                multiplier = game_data["multiplier"]
                update_history(multiplier)

                # Run AI prediction
                cashout_range, confidence = predict_next_cashout()
                bet_time = format_bet_time(delay_minutes=2)

                # Create and send the Telegram message
                message = (
                    f"**Aviator Signal Alert**\n"
                    f"Time to Bet: *{bet_time}*\n"
                    f"Predicted Cashout Range: *{cashout_range}*\n"
                    f"Confidence Score: *{confidence}%*\n"
                    f"Last Multiplier: *{multiplier}x*\n"
                    f"Prepare to enter in 2 minutes!"
                )
                send_telegram_alert(message)

            else:
                logging.warning("No multiplier data found during scraping.")

            time.sleep(300)  # 5-minute interval

        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            time.sleep(60)  # Retry after 1 minute if an error occurs

if __name__ == "__main__":
    run_bot()
