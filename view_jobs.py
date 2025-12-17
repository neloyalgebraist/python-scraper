import pandas as pd
from tabulate import tabulate

df = pd.read_csv("jobs.csv")

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)


print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))
