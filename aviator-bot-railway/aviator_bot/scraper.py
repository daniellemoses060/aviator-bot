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

            # This selector must be updated if Betway changes structure
            multiplier_element = await page.query_selector("span.multiplier")  # Example selector
            if multiplier_element:
                multiplier_text = await multiplier_element.inner_text()
                multiplier = float(multiplier_text.replace("x", ""))
                await browser.close()
                return multiplier

            await browser.close()
            return None
    except Exception as e:
        logging.error(f"[SCRAPER] Failed to get multiplier: {e}")
        return None
