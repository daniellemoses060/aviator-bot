import asyncio
from playwright.async_api import async_playwright
import logging

async def get_live_multiplier():
    url = "https://www.betway.co.za/lobby/casino-games/launchgame/casino-games/trending/aviator?IsLoggedIn=true"
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(url)

            await page.wait_for_timeout(5000)  # Wait for page content to load

            # Modify this selector as per the latest Aviator multiplier element
            multiplier_element = await page.query_selector("css=span.multiplier")
            multiplier = await multiplier_element.text_content() if multiplier_element else None

            await browser.close()
            return float(multiplier.replace("x", "")) if multiplier else None

    except Exception as e:
        logging.error(f"[SCRAPER] Failed to get multiplier: {e}")
        return None

# For testing purposes:
if __name__ == "__main__":
    print(asyncio.run(get_live_multiplier()))
