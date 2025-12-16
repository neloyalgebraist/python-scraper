from playwright.sync_api import sync_playwright
import time


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        page = browser.new_page()

        print("1. Navigating to site...")
        page.goto("http://quotes.toscrape.com/js/")
        page.wait_for_selector("div.quote")

        quotes = page.query_selector_all("div.quote")
        print(f"Found {len(quotes)} quotes via javascript!")

        for quote in quotes:
            text = quote.query_selector("span.text").inner_text()
            print(f"-{text[:50]}...")

        page.screenshot(path="js_scrape_proof.png")
        print("Screenshot saved.")

        browser.close()


if __name__ == "__main__":
    run()
