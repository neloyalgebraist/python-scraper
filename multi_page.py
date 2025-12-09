import requests
from bs4 import BeautifulSoup
import csv

all_books = []

for page in range(1, 6):
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print("Scraping", url)

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    books = soup.select("article.product_pod")

    for book in books:
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)

        all_books.append([title, price, availability])

with open("all_books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "price", "availability"])
    writer.writerow(all_books)

print("Done! Scraped", len(all_books), "books.")
