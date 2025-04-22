import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://www.betway.co.za/lobby/casino-games/launchgame/casino-games/trending/aviator?IsLoggedIn=true"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the multiplier (this part is for demonstration, you need to adjust the selector based on actual HTML structure)
    multiplier = soup.find("span", class_="multiplier").text

    # Find the crash point
    crash_point = soup.find("span", class_="crash-point").text

    # Get game stats, history, etc.
    game_stats = {
        "multiplier": float(multiplier),
        "crash_point": float(crash_point),
    }

    return game_stats
