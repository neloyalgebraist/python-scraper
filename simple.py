import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
books = soup.select("article.product_pod")

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["title", "price", "availability"])
    for book in books:
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)
        print(title, price, availability)

        writer.writerow([title, price, availability])

print("Done! Saved data to books.csv")
