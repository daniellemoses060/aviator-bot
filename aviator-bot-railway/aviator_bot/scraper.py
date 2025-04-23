import requests
from bs4 import BeautifulSoup

def scrape_data():
    """
    Scrapes the Betway Aviator page and returns the latest game stats.
    """
    url = "https://www.betway.co.za/lobby/casino-games/launchgame/casino-games/trending/aviator?IsLoggedIn=true"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the multiplier (this part is for demonstration, you need to adjust the selector based on actual HTML structure)
        multiplier_element = soup.find("span", class_="multiplier")
        multiplier = float(multiplier_element.text) if multiplier_element else None

        # Find the crash point
        crash_point_element = soup.find("span", class_="crash-point")
        crash_point = float(crash_point_element.text) if crash_point_element else None

        # Return game stats as a dictionary
        game_stats = {
            "multiplier": multiplier,
            "crash_point": crash_point,
        }

        return game_stats

    except Exception as e:
        print(f"Error scraping data: {e}")
        return None
