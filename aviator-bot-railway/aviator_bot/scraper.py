import asyncio
from playwright.async_api import async_playwright
import logging

async def fetch_multiplier():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://www.betway.co.za/lobby/casino-games/launchgame/casino-games/trending/aviator?IsLoggedIn=true", timeout=60000)
            await page.wait_for_timeout(5000)

            # Update this selector based on actual Betway structure (placeholder)
            element = await page.query_selector("span.multiplier")
            if not element:
                logging.warning("Multiplier element not found.")
                return None

            text = await element.inner_text()
            multiplier = float(text.strip().replace("x", ""))
            await browser.close()
            return multiplier
    except Exception as e:
        logging.error(f"Scraper error: {e}")
        return None
