import requests
import time
from datetime import datetime

API_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1"
THRESHOLD = -5.0
PARAMETERS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": "false",
}


def check_crypto_prices():
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] checking prices...")

    try:
        response = requests.get(API_URL, params=PARAMETERS)
        if response.status_code == 429:
            print("(!) Rate Limit Hit. Cooling down for 2 minutes...")
            time.sleep(120)
            return
        if response.status_code != 200:
            print("Failed to retrieve data!!!")
            return

        data = response.json()
        alerts_triggered = 0
        for coin in data:
            name = coin.get("name")
            symbol = coin.get("symbol").upper()
            current_price = coin.get("current_price")
            change_24h = coin["price_change_24h"]
            if change_24h is None:
                continue
            if change_24h < THRESHOLD:
                print(
                    f"ALERT!!! {name} ({symbol}) dropped {change_24h}%! Current Price: ${current_price}"
                )
                alerts_triggered += 1

        if alerts_triggered == 0:
            print(f"No major drops detected.")
    except Exception as e:
        print(f"Error occured:{e}")


def main():
    print("--------Crypto crash monitor started--------")
    print(f"Scanning Top 50 coins for drops > {THRESHOLD}%")
    print("Press Ctrl+C to stop.")
    while True:
        check_crypto_prices()
        time.sleep(60)


if __name__ == "__main__":
    main()
