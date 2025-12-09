# books_scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time
import random

BASE = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}


def fetch(url, session):
    resp = session.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text


def parse_page(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for article in soup.select("article.product_pod"):
        a = article.select_one("h3 > a")
        title = (
            a["title"].strip()
            if a and a.has_attr("title")
            else a.get_text(strip=True)
            if a
            else ""
        )
        rel_link = a["href"] if a and a.has_attr("href") else ""
        link = urljoin(base_url, rel_link)
        price = article.select_one("p.price_color")
        price = price.get_text(strip=True) if price else ""
        avail = article.select_one("p.instock.availability")
        avail = avail.get_text(strip=True) if avail else ""
        rows.append(
            {"title": title, "price": price, "availability": avail, "url": link}
        )
    return rows


def save_csv(rows, fname="books.csv"):
    keys = ["title", "price", "availability", "url"]
    with open(fname, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(rows)


def main():
    s = requests.Session()
    all_rows = []
    # we'll scrape the first 3 pages to keep it quick — you can increase pages later
    for page in range(1, 4):
        if page == 1:
            url = urljoin(BASE, "index.html")
        else:
            url = urljoin(BASE, f"catalogue/page-{page}.html")
        print("Fetching:", url)
        try:
            html = fetch(url, s)
        except Exception as e:
            print("Failed to fetch", url, ":", e)
            break
        rows = parse_page(html, url)
        all_rows.extend(rows)
        # polite random delay
        time.sleep(1 + random.random() * 1.5)
    save_csv(all_rows)
    print("Done — saved", len(all_rows), "rows to books.csv")


if __name__ == "__main__":
    main()
