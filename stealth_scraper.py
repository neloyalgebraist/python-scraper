from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import time


def run():
    with sync_playwright() as p:
        fake_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
        browser = p.firefox.launch(headless=True)
        context = browser.new_context(
            user_agent=fake_user_agent,
            viewport={"width": 1920, "height": 1080},
            locale="en-us",
            timezone_id="Asia/Kolkata",
        )
        page = context.new_page()
        page.add_init_script("""
                             Object.defineProperty(navigator, 'webdriver',{
                                get: () => undefined
                             }
                             )
                             """)
        print("Stealth Bot initialized.")
        print("Navigating to a detection test site...")
        page.goto("http://bot.sannysoft.com/")
        print("Page loaded. Taking a screenshot of the report...")
        time.sleep(2)
        page.screenshot(path="Stealth_report.png", full_page=True)
        print("Check 'Stealth_report.png'. Look for green 'Passed' labels.")
        browser.close()


if __name__ == "__main__":
    run()
