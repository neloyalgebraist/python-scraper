from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


def run():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("Applying stealth patches...")
        stealth_sync(page)

        print("Navigating to detection site...")
        page, goto("https://bot.sannysoft.com/")
        page.screenshot(path="stealth_library_check.png", full_page=True)
        print("Check 'stealth_library_check.png'.WebDriver should be Green.")

        browser.close()


if __name__ == "__main__":
    run()
