import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
if response.status_code == 200:
    print("Success! We got the page.")
else:
    print("Failed to retrieve the page.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

all_quotes = soup.find_all("span", class_="text")
all_authors = soup.find_all("small", class_="author")

print(f"I found {len(all_quotes)} quotes and it's author on this page:\n")

data = (all_quotes, all_authors)

for i in range(len(all_quotes)):
    print(all_quotes[i].text)
    print("-" + all_authors[i].text)

    print("----")
