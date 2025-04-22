import time
import telegram
from scraper import scrape_data
from predictor import predict_bet
from utils.scheduler import schedule_predictions
from utils.logger import log_error, log_info

def send_telegram_alert(message):
    bot = telegram.Bot(token="YOUR_BOT_TOKEN")
    chat_id = "YOUR_CHAT_ID"
    bot.send_message(chat_id=chat_id, text=message)

def run():
    while True:
        try:
            # Scrape live data
            data = scrape_data()
            
            # Make prediction
            prediction = predict_bet(data)
            
            # Send Telegram alert
            send_telegram_alert(prediction)
            
            # Log
            log_info(f"Prediction sent: {prediction}")
            
            # Wait before the next prediction
            time.sleep(30)
        
        except Exception as e:
            log_error(f"Error in main loop: {e}")
            time.sleep(60)  # Wait a bit before retrying

if __name__ == "__main__":
    run()
