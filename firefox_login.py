from playwright.sync_api import sync_playwright
import time


def run():
    with sync_playwright() as p:
        Browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = Browser.new_context()
        page = context.new_page()

        print("1. Navigating to the login page...")
        page.goto("http://quotes.toscrape.com/login")

        print("2. Entering credentials...")
        page.fill("input#username", "admin")
        page.fill("input#password", "password")

        print("3. Clicking Login...")
        page.click('input[type="submit"]')

        try:
            page.wait_for_selector('a[href="/logout"]', timeout=3000)
            print("SUCCESS:We are logged in!")

        except:
            print("FAILED:Could not log in.")

        page.screenshot(path="login_success.png")
        time.sleep(2)
        Browser.close()

    if __name__ == "__main__":
        run()
