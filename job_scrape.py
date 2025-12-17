import requests
from bs4 import BeautifulSoup
import csv


url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")


cards = soup.find_all("div", class_="card")

file = open("jobs.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Title", "Company", "Location", "Apply Link"])

print(f"-------------Start Scraping------------")
for card in cards:
    print("Finding jobs...")
    title = card.find("h2", class_="title is-5").text.strip()
    company = card.find("h3", class_="subtitle is-6 company").text.strip()
    location = card.find("p", class_="location").text.strip()

    links = card.find_all("a", class_="card-footer-item")
    if len(links) > 1:
        link = links[1]["href"]
    else:
        link = "N/A"
    writer.writerow([title, company, location, link])


file.close()
