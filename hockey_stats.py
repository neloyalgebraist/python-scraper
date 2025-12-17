import requests
from bs4 import BeautifulSoup
import csv

file = open("hockey_stats.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Team Name", "Year", "Wins", "Losses"])

base_url = "https://www.scrapethissite.com/pages/forms/?page_num="

for page in range(1, 6):
    print(f"Scraping Page {page}...")
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find_all("tr", class_="team")

    for row in table:
        name = row.find("td", class_="name").text.strip()
        year = row.find("td", class_="year").text.strip()
        wins = row.find("td", class_="wins").text.strip()
        losses = row.find("td", class_="losses").text.strip()

        writer.writerow([name, year, wins, losses])
