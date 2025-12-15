import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

file = open("quotes.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)

writer.writerow(["Quote", "Author", "Tags"])
quotes_box = soup.find_all("div", class_="quote")
print("Scraping data...")

for box in quotes_box:
    quotes_text = box.find("span", class_="text").text
    author = box.find("small", class_="author").text
    tags_list = box.find_all("a", class_="tag")
    tags_text = ",".join([tag.text for tag in tags_list])

    writer.writerow([quotes_text, author, tags_text])

print("Done! Check the 'quotes.csv' file in your folder.")
file.close()
