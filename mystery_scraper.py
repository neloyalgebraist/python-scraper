import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

base_url = "http://https://books.toscrape.com/"
start_url = "https://books.toscrape.com/catalogue/category/books/mystery_3/"


def get_soup(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml")
        else:
            print(f"Error: Status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Error fetching {url}:{e}")
        return None


def scrape_book_details(book_url):
    soup = get_soup(book_url)
    if not soup:
        return None

    try:
        title = soup.find("h1").text
        price = soup.find("p", class_="price_color").text
        availability = soup.find("p", class_="instock availability").text
        upc_table = soup.find("table", class_="table-striped")
        upc = upc_table.find("td").text

        return [upc, title, price, availability]

    except AttributeError:
        return ["N/A", "Error", "N/A", "N/A"]


def main():
    filename = "mystery_books_complete.csv"
    file = open(filename, "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["UPC", "Title", "price", "Availability"])

    current_url = start_url
    page_count = 1
    print("---------Spider Started-----------")
    while current_url:
        print(f"\nProcessing Page {page_count}...")
        soup = get_soup(current_url)

        if not soup:
            break

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            relative_link = book.find("h3").find("a")["href"]

            full_book_url = urljoin(current_url, relative_link)
            print(f" ->Scraping book details...")
            details = scrape_book_details(full_book_url)

            if details:
                writer.writerow(details)

        next_button = soup.find("li", class_="next")

        if next_button:
            next_relative_url = next_button.find("a")["href"]
            current_url = urljoin(current_url, next_relative_url)
            page_count += 1
        else:
            print("\n No 'Next button' found. Reached the end.")
            current_url = None

    file.close()
    print(f"--------Mission Complete. Data saved to {filename}---------")


if __name__ == "__main__":
    main()
