import requests
import csv

url = "https://dummyjson.com/products?limit=100"
print(f"Hitting API endpoint:{url}")
response = requests.get(url)

if response.status_code != 200:
    print("Blocked or Failed.")
    exit()

data = response.json()
products_list = data["products"]
print(f"API gave us {len(products_list)} items directly\n")
file = open("api_data.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["ID", "Title", "Price", "Stock", "Brand"])

for item in products_list:
    i_id = item.get("id")
    title = item.get("title")
    price = item.get("price")
    stock = item.get("stock")
    brand = item.get("brand")

    writer.writerow([i_id, title, price, stock, brand])

print("Done. Saved to 'api_data.csv'.")
file.close()
