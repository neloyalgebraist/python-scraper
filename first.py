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

first_quote = soup.find("span", class_="text")

print("\n ----The Data----")
print(first_quote.text)
