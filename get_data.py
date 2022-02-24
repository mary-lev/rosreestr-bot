import json
import pandas as pd


with open("./data/palkino.csv", "r") as f:
    df = pd.read_csv(f)

print(df.head())
print(df.describe())
print(df.columns)