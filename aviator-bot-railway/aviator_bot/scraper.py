import requests
from bs4 import BeautifulSoup
import logging

def scrape_data():
    url = "https://www.betway.co.za/lobby/casino-games/launchgame/casino-games/trending/aviator?IsLoggedIn=true"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Safely get multiplier
        multiplier_element = soup.find("span", class_="multiplier")
        if multiplier_element and multiplier_element.text:
            multiplier = float(multiplier_element.text.strip().replace("x", ""))
        else:
            logging.warning("Multiplier element not found.")
            multiplier = None

        # Safely get crash point
        crash_element = soup.find("span", class_="crash-point")
        if crash_element and crash_element.text:
            crash_point = float(crash_element.text.strip().replace("x", ""))
        else:
            logging.warning("Crash point element not found.")
            crash_point = None

        if multiplier is None or crash_point is None:
            logging.error("Missing key game data. Skipping prediction.")
            return None

        return {
            "multiplier": multiplier,
            "crash_point": crash_point,
        }

    except Exception as e:
        logging.error(f"Scraping error: {e}")
        return None
