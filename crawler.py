import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "http://quotes.toscrape.com"
current_endpoint = "/"

file = open("all_quotes.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Quote", "Author", "Tags"])

page_count = 1

while current_endpoint:
    full_url = base_url + current_endpoint
    print(f"Scraping Page {page_count} ({full_url})...")

    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes_box = soup.find_all("div", class_="quote")
    for box in quotes_box:
        quote_text = box.find("span", class_="text").text
        author = box.find("small", class_="author").text
        tags_list = box.find_all("a", class_="tag")
        tags_text = ",".join([tag.text for tag in tags_list])

        writer.writerow([quote_text, author, tags_text])

    next_button = soup.find("li", class_="next")

    if next_button:
        next_link = next_button.find("a")
        current_endpoint = next_link["href"]
        page_count += 1

        time.sleep(2)
    else:
        print("No more pages found. Job done.")
        current_endpoint = None
file.close()
