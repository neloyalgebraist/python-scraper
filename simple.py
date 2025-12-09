import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
books = soup.select("article.product_pod")

for book in books:
    title = book.select_one("h3 a")["title"]
    price = book.select_one(".price_color").get_text(strip=True)
    availability = book.select_one(".availability").get_text(strip=True)
    print(title, price, availability)
