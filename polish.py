import pandas as pd

df = pd.read_csv("mystery_books_complete.csv")
df["Price"] = df["price"].str.replace("Â£", "").astype(float)
df["Stock_Count"] = df["Availability"].str.extract("(\d+)").astype(int)

df.to_csv("mystery_books_clean.csv", index=False)
print("Data cleaned and ready for analysis.")
